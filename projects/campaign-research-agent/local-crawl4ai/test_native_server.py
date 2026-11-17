import http.client
import json
import threading
import unittest
from types import SimpleNamespace

from native_server import LocalServer, serialize_result, validate_urls


class NativeAdapterTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        def simulated_crawl(urls):
            self.calls.append(urls)
            return [{'url': url, 'success': True, 'markdown': {'raw_markdown': 'Business'}} for url in urls]
        self.server = LocalServer(('127.0.0.1', 0), 'test-local-password', simulated_crawl)
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.worker.join()

    def request(self, method, path, body=None, authorized=True):
        headers = {'Content-Type': 'application/json'}
        if authorized:
            headers['Authorization'] = 'Bearer test-local-password'
        conn = http.client.HTTPConnection('127.0.0.1', self.server.server_port, timeout=3)
        try:
            conn.request(method, path, json.dumps(body) if body is not None else None, headers)
            response = conn.getresponse()
            return response.status, json.loads(response.read())
        finally:
            conn.close()

    def test_health_does_not_start_browser(self):
        status, data = self.request('GET', '/health', authorized=False)
        self.assertEqual(status, 200)
        self.assertEqual(data['concurrency'], 1)
        self.assertFalse(self.calls)

    def test_unauthorized_request_never_crawls(self):
        status, _ = self.request('POST', '/crawl', {'urls': ['https://example.com']}, authorized=False)
        self.assertEqual(status, 401)
        self.assertFalse(self.calls)

    def test_workflow_payload_and_duplicate_urls(self):
        status, data = self.request('POST', '/crawl', {'urls': ['https://example.com', 'https://example.com'], 'crawler_config': {'type': 'CrawlerRunConfig', 'params': {'semaphore_count': 99}}})
        self.assertEqual(status, 200)
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(self.calls, [['https://example.com']])

    def test_limit_is_enforced(self):
        status, _ = self.request('POST', '/crawl', {'urls': ['https://example.com'] * 6})
        self.assertEqual(status, 400)
        self.assertFalse(self.calls)

    def test_busy_service_does_not_start_second_crawl(self):
        self.server.crawl_lock.acquire()
        try:
            status, _ = self.request('POST', '/crawl', {'urls': ['https://example.com']})
            self.assertEqual(status, 429)
            self.assertFalse(self.calls)
        finally:
            self.server.crawl_lock.release()

    def test_invalid_target_is_rejected(self):
        for url in ['file:///etc/passwd', 'http://localhost', 'http://127.0.0.1', 'http://user:pass@example.com']:
            with self.assertRaises(ValueError):
                validate_urls({'urls': [url]})

    def test_result_matches_n8n_contract(self):
        result = SimpleNamespace(success=True, url='https://www.example.com/', redirected_status_code=200, status_code=301, markdown=SimpleNamespace(raw_markdown='Website text'), links={}, metadata={}, html='<html></html>', cleaned_html='')
        serialized = serialize_result(result, 'https://example.com')
        self.assertEqual(serialized['url'], 'https://example.com')
        self.assertEqual(serialized['redirected_url'], 'https://www.example.com/')
        self.assertEqual(serialized['markdown']['raw_markdown'], 'Website text')
        self.assertEqual(serialized['status_code'], 200)
        self.assertEqual(serialized['links']['external'], [])


if __name__ == '__main__':
    unittest.main()
