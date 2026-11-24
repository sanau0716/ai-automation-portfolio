#!/usr/bin/env python3
"""Endpoint sanity check helper for a deployed Zero-Leak Executive Guardrail suite."""

import argparse
import json
import urllib.error
import urllib.request


HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ZeroLeakVerify/1.0)"}


def request_http(url: str, method: str = "GET", payload: dict | None = None, extra_headers: dict | None = None):
    hdrs = dict(HEADERS)
    if extra_headers:
        hdrs.update(extra_headers)
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify public endpoints for the Zero-Leak suite.")
    parser.add_argument("--base-url", required=True, help="Base URL of your n8n instance, e.g. https://n8n.example.com")
    parser.add_argument("--intake-secret", default="", help="Optional X-Intake-Secret value for positive POST intake check")
    args = parser.parse_args()

    base = args.base_url.rstrip("/")
    failures = 0

    # 1. Verify intake webhook blocks unauthenticated callers (expects 401/403)
    code, body = request_http(f"{base}/webhook/zero-leak/intake", method="POST", payload={"name": "Unauthorized Check"})
    ok = code in (401, 403)
    print(f"[{'PASS' if ok else 'FAIL'}] Unauthenticated POST /webhook/zero-leak/intake -> HTTP {code}")
    if not ok:
        failures += 1

    # 2. Verify hosted Public Intake Form renders cleanly (expects 200)
    code, body = request_http(f"{base}/form/zero-leak-intake", method="GET")
    ok = code == 200 and "Inbound Inquiry" in body
    print(f"[{'PASS' if ok else 'FAIL'}] Public Form GET /form/zero-leak-intake -> HTTP {code}")
    if not ok:
        failures += 1

    # 3. Verify Decision Gate rejects malformed GET params (expects 400)
    code, body = request_http(f"{base}/webhook/zero-leak/decision?lead_key=TEST&token=x&action=invalid&format=json")
    ok = code == 400
    print(f"[{'PASS' if ok else 'FAIL'}] Bad Params GET /webhook/zero-leak/decision -> HTTP {code}")
    if not ok:
        failures += 1

    # 4. Verify Slackbot prefetch guard blocks auto-execution safely (expects 200 mutated=false)
    code, body = request_http(
        f"{base}/webhook/zero-leak/decision?lead_key=TEST&token=x&action=approve&format=json",
        extra_headers={"User-Agent": "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)"},
    )
    ok = code == 200 and '"mutated":false' in body.replace(" ", "")
    print(f"[{'PASS' if ok else 'FAIL'}] Slackbot Prefetch Guard GET /webhook/zero-leak/decision -> HTTP {code}")
    if not ok:
        failures += 1

    # 5. Verify Commit endpoint returns 404 for unknown lead_key (expects 404)
    code, body = request_http(
        f"{base}/webhook/zero-leak/commit",
        method="POST",
        payload={"lead_key": "ZL-NONEXISTENT-999", "token": "tok_none", "action": "approve", "format": "json"},
    )
    ok = code == 404
    print(f"[{'PASS' if ok else 'FAIL'}] Unknown Lead POST /webhook/zero-leak/commit -> HTTP {code}")
    if not ok:
        failures += 1

    if args.intake_secret:
        code, body = request_http(
            f"{base}/webhook/zero-leak/intake",
            method="POST",
            payload={"name": "Bad Payload"},
            extra_headers={"X-Intake-Secret": args.intake_secret},
        )
        ok = code == 400
        print(f"[{'PASS' if ok else 'FAIL'}] Authenticated Validation 400 POST /webhook/zero-leak/intake -> HTTP {code}")
        if not ok:
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
