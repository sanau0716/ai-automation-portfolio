# Setup and operation

[← Project](../README.md)

## Prerequisites

- An n8n instance with Form Trigger, HTTP Request, Code, Wait and Data Table support. Exports preserve the versions from the source instance; older installations may require an upgrade.
- Python 3.12 and Windows PowerShell 5.1 or later for the included launcher.
- Ollama with `hermes3:3b` installed.
- A Serper account/key for API discovery. Obtain the key from [Serper](https://serper.dev/); enter it only in an n8n credential.

## Start the local services

Keep `Start-LeadFinder.ps1` and `native_server.py` in the same directory. In PowerShell, change to that directory first:

```powershell
cd "C:\path\to\ai-automation-portfolio\projects\campaign-research-agent\local-crawl4ai"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Start-LeadFinder.ps1
```

The first run creates a virtual environment and installs Crawl4AI and Chromium. Later starts reuse them. Keep this window open. The adapter binds to `127.0.0.1:11235`, starts a browser only when needed, and reads one page at a time.

In another PowerShell window, verify Ollama:

```powershell
ollama list
```

If the service is not running, run `ollama serve` in its own window. A port-11434 "address already in use" error usually means it is already running. If `hermes3:3b` is missing from the model list, download it once with `ollama pull hermes3:3b`.

Optional health checks:

```powershell
Invoke-RestMethod http://127.0.0.1:11235/health
Invoke-RestMethod http://127.0.0.1:11434/api/tags
```

`127.0.0.1` works only when n8n and these services run on the same host/network context. A remote n8n server cannot reach your Windows computer through its own loopback address. Configure a suitable private authenticated connection if hosting them separately; do not expose the local services publicly just to make this URL work.

## Import and credentials

1. Import `workflows/campaign-research-and-drafts.json` and `workflows/campaign-queue-review.json` from the project directory.
2. In the research workflow, open **Local Service Settings**. Set the Crawl4AI and Ollama base URLs, model, sender name, business website and mailing address. `search_source` defaults to `serper`; `max_search_attempts` defaults to `6`.
3. Copy the locally generated Crawl4AI token:

   ```powershell
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Start-LeadFinder.ps1 -CopyToken
   ```

4. Create an n8n **Header Auth** credential for Crawl4AI: header name `Authorization`, value `Bearer ` followed by the copied token. Select it on **Discover Company Websites**, **Research Business Websites** and **Research Contact Pages**. The token is stored locally using Windows user encryption and is not included in this repository.
5. Create a separate **Header Auth** credential for Serper: header name `X-API-KEY`, value your raw Serper key, without `Bearer`. Select it on **Search API - Serper**. Never reuse the Crawl4AI credential on this external API.
6. Both workflows create/reuse **AwtomateAI Campaign Review Queue** by name. Keep them in the same n8n project and verify all Data Table nodes resolve the same table. If you rename the queue, update every reference in both workflows.

The included native adapter implements `POST /crawl` with a JSON body such as `{"urls":["https://example.com/"]}` and a response containing `results`. It enforces a five-URL request limit and robot checks. It does not implement arbitrary Crawl4AI configuration payloads.

## First test

1. Start the local services and execute the research workflow manually.
2. Open the form using the test URL displayed by n8n. Choose one business, a specific area and your offer.
3. First use one relevant company website to verify local crawling, drafting and persistence.
4. Then leave the websites field blank to verify a real Serper search. Inspect **Search API - Serper**, the discovery attempt history and final queue status. A technically successful n8n run may still end in a blocked/no-new-candidates outcome.
5. Open **Review Drafts in n8n** and inspect the shared table. Confirm source evidence, contact details, sender information and draft wording before using any message.

The sanitized form path is `portfolio-campaign-request`; customize it if needed. The production form URL works only after publishing the workflow. Executing a workflow through an API does not automatically open a browser tab or copy a link.

## Queue and follow-up

The queue stores domain, name, website, category, location, public contact/source URL, evidence, opportunity, drafts, review status, contact date, research date, error and run identifier. Existing domains are skipped even when a previous record is `SKIPPED` or `RESEARCH_ERROR`; review the record before deliberately retrying it.

After manually contacting a business, set `review_status` to `CONTACTED` and `contacted_at` to the actual date. Run the queue review workflow to see the five-day follow-up flags. Update statuses manually for replies, completed follow-ups or opt-outs. Nothing is sent automatically.

In the default Serper mode, each discovery attempt makes one search request, up to six per execution. New supplied websites bypass search and use no Serper queries; already-known supplied domains fall back to discovery. The loop stops after finding candidates, which may later be rejected during research. Keep batches small and run only one at a time.
