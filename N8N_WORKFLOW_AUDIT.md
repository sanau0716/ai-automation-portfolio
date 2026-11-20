# n8n Workflow Inventory & GitHub Portfolio Alignment

**Audit date:** November 20, 2026  
**Connected n8n inventory:** 36 workflows — 12 active and 24 inactive at the time of review.  
**Purpose:** Reconcile the public GitHub portfolio with the current n8n workspace so reviewers can distinguish active workflows, historical exports, prototypes, and test exercises.

> An n8n workflow marked active is not automatically a production customer deployment. Many active workflows are personal-business automations, internal prototypes, development-store services, or monitoring jobs.

## Portfolio alignment and execution evidence

Execution counts below are n8n history records in the November 1–20, 2026 search window unless otherwise noted. They are not uptime guarantees or customer outcome metrics.

| Project / workflow | n8n state | Recorded evidence | GitHub treatment |
|---|---|---|---|
| CommercePilot Storefront Shopping Assistant API (Groq) | Active | 44 successful executions; latest retrieved run Nov 19 | Featured case study; note 42-node draft vs 37-node published version |
| CommercePilot Shopify Catalog Sync | Active | 26 successes, 1 error across 27 records | Featured as development-store-only catalog sync |
| CommercePilot Health & Latency Monitor | Active | 212 records in the window; 50 most recent retrieved records succeeded | Included in CommercePilot architecture |
| CommercePilot Error Alert Handler | Active | One successful test execution recorded | Included in CommercePilot reliability design; real error-trigger firing is not claimed |
| CommercePilot Ollama Rollback | Inactive | Rollback copy, not current serving workflow | Not promoted as a separate project |
| CommercePilot Shopify Store & Theme QA (Read Only) | Inactive | 19 successes and 1 error across 20 records | Internal read-only QA; not a customer feature |
| AI Lead Qualification & Automation Platform | Active | 18 successful executions | Featured; connected to AwtomateAI website |
| Older Phase 3 AI Lead Qualification & Response Automation | Inactive | No executions in the Nov 1–20 window | Historical workflow variant; not the current active website workflow |
| Phase 3 AI Lead Follow-Up Monitor | Inactive | No executions in the Nov 1–20 window | Prototype; current 16-node n8n workflow differs from the older 15-node GitHub export |
| PropertyFix AI 2.0 | Active | 10 successful executions | Featured; synthetic test data, no contractor dispatch |
| Smart Scheduler V1 | Active | 20 successful executions | Featured; personal Gmail/Calendar workflow, not a paid-client deployment |
| AI Business Automation Auditor | Active | 23 successes, 2 errors, 1 cancellation across 26 records | Featured as a research prototype |
| Website Auditor Engine | Active | 39 successes and 7 errors across 46 records | Included under Business Automation Auditor |
| Automated Voice Inquiry & Support Dispatcher | Active | 35 successes and 15 errors in the 50 most recent retrieved records (68 total matches) | Documented with explicit retest requirement |
| Anna Omnichannel Receptionist (Groq · Portfolio) | Inactive | 9 successes and 10 errors across 19 records | Historical text/Supabase prototype; not presented as active |
| Intelligent Gmail Manager | Inactive | 3 successful test executions | Documented as read-only; mailbox mutations remain disabled |
| Campaign Research and Drafts | Inactive | 16 successful executions | Documented as internal research; no outbound messages |
| Campaign Queue Review | Inactive | 4 successful executions | Supporting manual review workflow |
| Crawl4AI AI Business Opportunity Finder | Inactive | One recorded error in the Nov 1–20 window | Historical research prototype; 19-node n8n version vs 17-node GitHub export |
| AI Niche Lead Finder | Inactive | 14 successes, 2 waiting, 2 errors across 18 records | Not promoted until its waiting/error cases are reviewed |
| HVAC Lead Response Demo | Active | 2 successes and 3 errors across 5 records | Experimental demo; not featured as a verified service |
| Apollo Prospecting & Outreach Drafts | Inactive | One successful manual execution | Manual research/drafting only; no sending or enrollment |
| Prospect Contact Discovery | Inactive | 2 successful executions | Internal prototype |
| Zoho FSM Webhook Receiver | Active | No execution records in the Nov 1–20 window | Active source, but not described as verified |
| Portfolio GitHub Sync & Docs | Inactive | 4 successes and 1 error across 5 records | Manual helper; this portfolio refresh was committed directly to GitHub |
| Autonomous Job Sourcing & Drafting Pipeline | Inactive | No executions in the Nov 1–20 window | Prototype; manual application review |
| Website Auditor (legacy wrapper) | Inactive | No executions in the Nov 1–20 window | Legacy wrapper; not featured |
| AI Customer Engagement Monitor | Inactive | No executions in the Nov 1–20 window | Historical prototype |
| AI Customer Response Manager | Inactive | No executions in the Nov 1–20 window | Historical prototype |
| Medic Paths Inbound Client Inquiry & AI Response Engine | Inactive | No executions in the Nov 1–20 window | Internal prototype; not featured |
| Local Ollama Code Generation Sandbox | Inactive | No executions in the Nov 1–20 window | Development experiment |
| Supabase Lead Queue Processor | Inactive | No executions in the Nov 1–20 window | Prototype |
| Section 1 — Academy Registration | Inactive | One successful learning exercise | Training workflow; not a portfolio project |
| Section 2 — Sales Data Pipeline | Inactive | One successful learning exercise | Training workflow; not a portfolio project |
| ACME — Coordinator Dispatch Approval | Inactive | One successful challenge execution | Challenge prototype |
| ACME — Job Readiness Verification | Inactive | One successful challenge execution | Challenge prototype |

## Important version and publication differences

1. **CommercePilot assistant:** The active workflow has a 42-node draft and a 37-node published version. The latest draft additions must not be represented as already published. The public case study separates those states.
2. **CommercePilot catalog sync:** The workflow description explicitly limits the protected sync endpoint to the development store. It is not a general merchant onboarding flow yet.
3. **Lead qualification:** The current active website-connected workflow is an 18-node AI Lead Qualification & Automation Platform with 18 successful recent executions. The repository's 14-node phase-3-lead-qualification-response.json is an older inactive workflow variant.
4. **Lead follow-up:** The current n8n follow-up monitor is inactive and has 16 nodes. The repository's older export contains 15 nodes and is retained as a historical snapshot.
5. **Business Opportunity Finder:** The current inactive n8n workflow has 19 nodes; the public JSON snapshot has 17 nodes.
6. **Voice Inquiry:** The current source is active, but its recent history contains errors and the exact current audio path needs a fresh acceptance test.
7. **Anna:** The portfolio workflow is inactive. A successful historical text/Supabase execution exists, but recent history is mixed.
8. **Portfolio exports:** Public JSON exports are sanitized and marked inactive. They are learning/inspection artifacts, not ready-to-run production deployments.

## Workflow inventory by purpose

### CommercePilot platform (6)
- Storefront Shopping Assistant API (Groq)
- Shopify Catalog Sync (Development Store)
- Health & Latency Monitor
- Error Alert Handler
- Storefront Shopping Assistant API (Ollama Rollback)
- Shopify Store & Theme QA (Read Only)

### Lead generation, sales and research (12)
- HVAC Lead Response Demo
- Campaign Research and Drafts
- Campaign Queue Review
- AI Niche Lead Finder
- Apollo Prospecting & Outreach Drafts
- Prospect Contact Discovery
- AI Lead Qualification & Response Automation (older Phase 3)
- Crawl4AI AI Business Opportunity Finder
- AI Lead Follow-Up Monitor (Phase 3)
- Supabase Lead Queue Processor
- AI Lead Qualification & Automation Platform
- Autonomous Job Sourcing & Drafting Pipeline

### Customer support and engagement (6)
- Automated Voice Inquiry & Support Dispatcher
- Anna Omnichannel Receptionist
- Intelligent Gmail Manager
- AI Customer Engagement Monitor
- Medic Paths Inbound Client Inquiry & AI Response Engine
- AI Customer Response Manager

### Website audit and business analysis (3)
- AI Business Automation Auditor
- Website Auditor Engine
- Website Auditor (legacy wrapper)

### Operations and scheduling (4)
- PropertyFix AI 2.0
- Smart Scheduler V1
- Zoho FSM Webhook Receiver
- ACME — Job Readiness Verification

### Internal tooling and learning (5)
- Portfolio GitHub Sync & Docs
- Local Ollama Code Generation Sandbox
- Academy Registration
- Sales Data Pipeline
- ACME Coordinator Dispatch Approval

The categories above are practical groupings, not mutually exclusive business domains. The inventory is intentionally broader than the public project list: training, rollback, duplicate, and unvalidated experiments are not automatically promoted into the hiring portfolio.


---

## Focused follow-up verification — November 21, 2026

A read-only follow-up was performed against the connected n8n workspace on November 21, 2026. This section supplements (and does not silently rewrite) the November 20, 36-workflow inventory above.

| Featured workflow | Current n8n state | Current graph | Execution records, Nov 1–21 | Important boundary |
|---|---|---:|---:|---|
| CommercePilot — Storefront Shopping Assistant API (Groq) | Active | 42-node draft / 37-node published version; graphs differ | 44 success / 44 records | Development-store project; draft-only changes are not published |
| CommercePilot — Shopify Catalog Sync | Active | Current workflow inspected | 26 success / 1 error / 27 records | Protected sync is configured for the development store only |
| CommercePilot — Health & Latency Monitor | Active | Current workflow inspected | 277 total records; 200 most recent retrieved were successful | The remaining 77 records were not individually retrieved in this query; this is not an uptime SLA |
| CommercePilot — Error Alert Handler | Active | Error-handler workflow; no trigger nodes reported | 1 successful manual test | This does not prove a real production error-trigger event was handled |
| AI Lead Qualification & Automation Platform | Active | 18 nodes; active version matches draft | 18 success / 18 records | Website-connected workflow for the developer's own business |
| PropertyFix AI 2.0 — Maintenance Intelligence | Active | 17 nodes; active version matches draft | 10 success / 10 records | Synthetic test data; Gmail/Slack notifications and approval responses were pinned/simulated in documented tests |
| AwtomateAI — Smart Scheduler V1 | Active | 30 nodes; active version matches draft | 20 success / 20 records | Own Gmail/Calendar account; sustained polling and load testing remain unverified |

### Version and publication boundaries

- **CommercePilot:** The current draft contains 42 nodes and the published active version contains 37. The two graphs are not identical. The current draft uses newer store/catalog API retrieval and conversation load/save nodes; the published graph contains different registered-store, active-product, conversation-log, and session-recommendation nodes. Do not describe draft-only changes as published behavior.
- **Lead Qualification:** The active website-connected workflow is the current 18-node implementation and uses OpenRouter model nodes. The public 14-node Phase 3 qualification JSON is an older inactive variant; the older export's model configuration must not be attributed to the current workflow.
- **Lead Follow-Up Monitor:** The separate monitor is inactive and has 16 nodes; the public JSON is a 15-node historical snapshot.
- **PropertyFix:** The 17-node workflow is an internal proof of concept. The successful execution records use synthetic data. Tests #405 and #406 cover a negated-hazard routine case and a positive sparks/smoke emergency case. Gmail/Slack notifications and approval responses were pinned/simulated; the separate Slack credential delivery test #407 does not prove delivery through the PropertyFix notification nodes.
- **Smart Scheduler:** The 30-node active workflow matches its current draft. Execution #395 verified a real calendar event creation and ledger write; #385 stopped on rejected approval; #390 simulated a new conflict after approval; #398 verified the alert email node, not a real Error Trigger firing.

### Evidence interpretation

All counts above are n8n execution-history records for the stated workflow IDs and time window. A successful execution is not proof of business impact, uptime, or paid-client deployment. "Active" describes the n8n workflow state; it does not by itself mean a workflow is externally offered as a production service.

[← Portfolio home](README.md) · [Visual proof gallery](VISUAL_PROOFS.md)
