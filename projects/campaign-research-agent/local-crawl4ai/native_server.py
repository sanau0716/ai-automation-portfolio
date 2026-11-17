"""Small local REST adapter for Crawl4AI; single browser, sequential pages.

This is a project adapter, not the official Crawl4AI Docker server. It accepts
the subset of /crawl used by the bundled n8n workflow and never evaluates
configuration classes or code supplied in requests.
"""
from __future__ import annotations

import argparse
import asyncio
import hmac
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

MAX_URLS = 5
MAX_BODY = 64 * 1024


def validate_urls(body):
    if not isinstance(body, dict):
        raise ValueError('Request must be a JSON object.')
    urls = body.get('urls')
    if not isinstance(urls, list) or not 1 <= len(urls) <= MAX_URLS:
        raise ValueError('Supply between 1 and 5 public website URLs.')
    output = []
    for url in urls:
        if not isinstance(url, str) or len(url) > 4096:
            raise ValueError('Every URL must be a string of at most 4096 characters.')
        parsed = urlsplit(url)
        hostname = parsed.hostname or ''
        if parsed.scheme not in ('http', 'https') or not hostname or parsed.username or parsed.password:
            raise ValueError('Use public http:// or https:// website URLs without login credentials.')
        if '.' not in hostname or hostname.endswith(('.local', '.internal', '.localhost')):
            raise ValueError('Use a public business website, not a local machine address.')
        # The workflow uses public DNS names, not numeric IP targets.
        if hostname.replace('.', '').isdigit() or ':' in hostname:
            raise ValueError('Use public business domain names, not IP addresses.')
        if url not in output:
            output.append(url)
    return output


def serialize_result(result, requested_url):
    markdown = getattr(result, 'markdown', '')
    if not isinstance(markdown, str):
        markdown = getattr(markdown, 'raw_markdown', '') or ''
    raw_links = getattr(result, 'links', None) or {}
    links = {kind: (raw_links.get(kind) or [])[:150] for kind in ('internal', 'external')}
    return {
        'url': requested_url,
        'redirected_url': getattr(result, 'redirected_url', None) or getattr(result, 'url', requested_url),
        'success': bool(result.success),
        'status_code': getattr(result, 'redirected_status_code', None) or getattr(result, 'status_code', None),
        'error_message': str(getattr(result, 'error_message', '') or '')[:1000],
        'metadata': getattr(result, 'metadata', None) or {},
        'markdown': {'raw_markdown': markdown[:40000]},
        'html': str(getattr(result, 'html', '') or '')[:200000],
        'cleaned_html': str(getattr(result, 'cleaned_html', '') or '')[:100000],
        'links': links,
    }


async def crawl_pages(urls):
    # Lazy import: starting the idle HTTP service does not launch Chromium.
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

    browser = BrowserConfig(
        headless=True, text_mode=True, light_mode=True,
        viewport_width=800, viewport_height=600, verbose=False,
    )
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS, page_timeout=25000,
        wait_until='domcontentloaded', check_robots_txt=True,
        word_count_threshold=10,
    )
    results = []
    # One browser per request, one page at a time. Closing this context releases
    # the browser even if a crawl fails. No parallel arun_many dispatcher.
    async with AsyncWebCrawler(config=browser) as crawler:
        for url in urls:
            try:
                result = await crawler.arun(url=url, config=config)
                results.append(serialize_result(result, url))
            except Exception as error:
                results.append({'url': url, 'success': False, 'error_message': str(error)[:1000], 'links': {}})
    return results


class LocalServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, token, crawl_runner=None):
        super().__init__(address, Handler)
        self.token = token
        self.crawl_lock = threading.Lock()
        self.crawl_runner = crawl_runner or (lambda urls: asyncio.run(crawl_pages(urls)))


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # Do not log request URLs, headers or local passwords.

    def reply(self, status, payload):
        data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == '/health':
            self.reply(200, {'status': 'ok', 'mode': 'native-python', 'concurrency': 1, 'max_urls': MAX_URLS})
        else:
            self.reply(404, {'detail': 'Use POST /crawl or GET /health.'})

    def do_POST(self):
        if self.path != '/crawl':
            self.reply(404, {'detail': 'Unknown endpoint.'})
            return
        expected = 'Bearer ' + self.server.token
        if not hmac.compare_digest(self.headers.get('Authorization', '').encode(), expected.encode()):
            self.reply(401, {'detail': 'Use the local Crawl4AI Bearer credential.'})
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= MAX_BODY:
                raise ValueError('Supply a JSON body smaller than 64 KiB.')
            body = json.loads(self.rfile.read(length))
            urls = validate_urls(body)
        except (ValueError, TypeError) as error:
            self.reply(400, {'detail': str(error)})
            return
        if not self.server.crawl_lock.acquire(blocking=False):
            self.reply(429, {'detail': 'A crawl is already running. Run one lead search at a time.'})
            return
        try:
            results = self.server.crawl_runner(urls)
            self.reply(200, {'success': True, 'results': results})
        except Exception as error:
            self.reply(500, {'detail': 'Crawl4AI could not start: ' + str(error)[:700]})
        finally:
            self.server.crawl_lock.release()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=11235)
    parser.add_argument('--check', action='store_true', help='Run one real example.com crawl, then exit.')
    args = parser.parse_args()
    if args.check:
        results = asyncio.run(crawl_pages(['https://example.com']))
        result = results[0]
        print(json.dumps({'success': result['success'], 'url': result['url'], 'error': result.get('error_message', '')}))
        return 0 if result['success'] else 1
    token = os.environ.get('CRAWL4AI_API_TOKEN', '')
    if not token:
        parser.error('Start with Start-LeadFinder.ps1 so a local password is configured.')
    server = LocalServer(('127.0.0.1', args.port), token)
    print(f'Crawl4AI native service: http://127.0.0.1:{args.port}', flush=True)
    print('Ready for n8n. One page at a time. Keep this window open; press Ctrl+C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
