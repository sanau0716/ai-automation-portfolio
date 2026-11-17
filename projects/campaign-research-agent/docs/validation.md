# Validation and practical limits

[← Project](../README.md)

Snapshot date: **November 17, 2026**. Execution numbers below are evidence references from the development n8n instance, not public links or bundled customer records.

| Scenario | Evidence | Result and scope |
| --- | --- | --- |
| Real company website supplied | Execution 471 | Local Crawl4AI research, Ollama drafting and queue persistence completed; one draft record was saved for review. About 4 minutes 17 seconds on the development PC. This timing is an observation, not a performance guarantee. |
| Review of saved queue | Execution 474 | Read the existing record and calculated review/follow-up fields. |
| Repeated supplied domain | Execution 475 | Did not add another copy of the existing business record in that version. |
| Empty discovery responses | Simulated execution 485 | Retried up to six times, then returned `NO_NEW_WEBSITES_AFTER_RETRIES`. |
| Blocked discovery providers | Simulated execution 486 | Skipped blocked providers, then returned `SEARCH_BLOCKED`. |
| Existing supplied domain with new discovery result | Simulated execution 487 | Fell back to discovery and reached draft review. Persistence was pinned to prevent fixture writes. |
| Blank website input with real public search | Execution 488 | Public providers were denied by robots restrictions; returned `SEARCH_BLOCKED`. This did not find a new business. |
| Serper discovery response | Simulated execution 489 | Parsed organic results and reached draft review. API output and persistence were pinned; this was not a live Serper query. |
| Current source node configuration | MCP validation, November 17 | All 37 node configurations across the two workflows passed schema validation. |

## Export checks

The portfolio update checks JSON parsing, unique node identities, connection targets, credential/metadata removal, and JavaScript syntax. Exported workflows are inactive, contain no execution or pinned data, and use a replacement form path and generic sender defaults. The local adapter's existing unit tests cover request validation, authentication and concurrent-request rejection.

## Outstanding acceptance work

- Run a live blank-input Serper campaign after configuring the private credential. The source snapshot has Serper selected, but no live Serper result is claimed here.
- Reimport the sanitized exports in a clean n8n project, select credentials and verify Data Table resolution and form behavior. Source-instance execution is not proof that another installation has identical capabilities.
- Evaluate more businesses, categories and locations, especially custom categories and service-area spelling. Keyword-based source checks are deliberately restrictive and can reject relevant companies.
- Validate manual contact-status maintenance and follow-up dates with actual business operations. There is no mailbox reply integration in this project.

## Known limits

The search loop retries candidate discovery, not final lead qualification. Finding a new domain does not guarantee readable pages, the right location, a public email or an accepted draft. Source quotation validation checks supporting service/area evidence; it does not prove every sentence of AI-written copy is correct. Human review remains required.

Deduplication uses existing queue records and assumes sequential runs. It is not a transactional lock against simultaneous campaigns. Stored skipped/error domains also count as known domains. Public providers can block automated access; the system reports the restriction and does not bypass it.

The local Python adapter is intended for this trusted local workflow and binds to loopback. Its URL checks are basic input validation, not a hardened network isolation boundary for an internet-facing scraping service. It runs a headless browser and consumes local resources; local AI avoids a cloud model token bill but still uses electricity and hardware.

No outreach messages were sent by these workflows. No client revenue, conversion rate, saved-hours figure or production uptime claim is established by these tests.
