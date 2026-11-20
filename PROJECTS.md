# Projects & Technical Case Studies

[← Portfolio home](README.md) · [Visual proof gallery](VISUAL_PROOFS.md) · [Project folders](projects/README.md) · [n8n workflow audit](N8N_WORKFLOW_AUDIT.md)

This catalog is organized around the business problem and engineering capability each project demonstrates. Every entry distinguishes implemented behavior, verified evidence, and remaining limitations.

## Featured systems

### 1. CommercePilot — Shopify AI Shopping Assistant

[**Technical case study**](projects/commercepilot) · [**Architecture visual**](projects/commercepilot/assets/workflow-overview.svg)

A Shopify-first AI shopping assistant that uses the merchant's own catalog, store-scoped conversation context, and live Shopify variant availability when stock questions require it. The wider platform includes Shopify App Proxy HMAC validation, Redis replay/rate controls, n8n orchestration, catalog sync, conversation persistence, and operational monitoring.

**Stack:** Shopify Admin GraphQL · Shopify App Proxy · Shopify Theme App Extension · React Router · TypeScript · Prisma · Supabase/PostgreSQL · n8n · Groq · Upstash Redis · Vercel.

**Evidence snapshot (November 1–21, 2026):** 44 successful assistant execution records. The current n8n draft has 42 nodes and the published active version has 37; the graphs differ. Catalog sync has 26 successes and 1 error across 27 records and is development-store-only. The health monitor has 277 execution records; the 200 most recent records retrieved were successful.

**Stage and limits:** Shopify app Preview deployment was marked READY in the November 20 project snapshot. This is a development-store project, not a paid-merchant production deployment. Location-level inventory still requires end-to-end acceptance testing.

### 2. AI Lead Qualification & Automation Platform

[**Technical case study**](projects/lead-management/n8n) · [**Architecture visual**](projects/lead-management/n8n/assets/workflow-overview.svg)

The active AwtomateAI website workflow captures inquiries, normalizes lead data, uses an OpenRouter-connected AI agent to qualify the lead, parses structured results, records the lead in Google Sheets, and routes high-value, qualified, and lower-value paths to Gmail actions and status updates.

**Stack:** n8n · Webhooks · OpenRouter · JavaScript · Gmail · Google Sheets.

**Evidence snapshot (November 1–21, 2026):** Current active workflow is 18 nodes and recorded 18 successful executions. Its active version matches the current draft. The public 14-node Phase 3 JSON is an older inactive variant; the current website workflow is separate. The follow-up monitor is also separate and inactive: its current 16-node graph differs from the older 15-node export.

**Stage and limits:** Operational on the developer's own business website, not a paid-client deployment. No conversion, revenue, or guaranteed uptime claim is made.

### 3. PropertyFix AI 2.0 — Maintenance Intelligence

[**Technical case study**](projects/propertyfix-ai) · [**Architecture and test visual**](projects/propertyfix-ai/assets/workflow-overview.svg)

A human-supervised maintenance intake and triage proof of concept. It preserves the original request, uses AI to suggest a category and priority, applies deterministic safety and confidence overrides, routes manager notifications, and persists a manager's approval/rejection decision.

**Stack:** n8n · n8n Form Trigger · Data Tables · OpenRouter · JavaScript · Gmail · Slack.

**Evidence snapshot (November 1–21, 2026):** Current connected workflow is 17 nodes and recorded 10 successful executions using synthetic test data. Regression tests include a negated-hazard case (#405) that remained routine and a sparks/smoke case (#406) that remained emergency.

**Stage and limits:** Internal proof of concept, not a tenant-facing service. Gmail/Slack notifications and approval responses were pinned or simulated in documented tests; a separate Slack credential delivery test succeeded, but delivery through the actual PropertyFix notification nodes still needs dedicated verification. It does not dispatch contractors or call emergency services.

### 4. Smart Scheduler V1 — AI-Assisted Email-to-Calendar

[**Technical case study**](projects/smart-scheduler) · [**Architecture and test visual**](projects/smart-scheduler/assets/workflow-overview.svg)

An AI-assisted Gmail-to-Google-Calendar workflow with structured event extraction, date/time and timezone validation, duplicate screening, calendar conflict checks, explicit approval, a final ledger/calendar recheck, and event persistence.

**Stack:** n8n · Gmail · Google Calendar · OpenRouter · JavaScript · Data Tables.

**Evidence snapshot (November 1–21, 2026):** Current connected workflow is 30 nodes and recorded 20 successful executions. Real event creation and ledger persistence were verified in execution #395; rejection stopped before writing in #385; a simulated post-approval conflict was blocked in #390.

**Stage and limits:** Active on the developer's own Gmail and Google Calendar account. The alert email node delivered successfully in test #398, but the actual Error Trigger was not fired. Sustained polling, concurrency, and load testing remain unverified.

---

## Leads, sales, and business research

### Campaign Research & Drafting Agent

[**Explore the project**](projects/campaign-research-agent) · [Setup](projects/campaign-research-agent/docs/setup.md) · [Validation](projects/campaign-research-agent/docs/validation.md)

A form-driven n8n system that researches supplied business websites with Crawl4AI, prepares evidence-checked outreach drafts using local Ollama, and stores them in a persistent review queue.

**Stack:** n8n Forms · HTTP Request · JavaScript · Serper · Crawl4AI · Python · PowerShell · Ollama · n8n Data Tables.

**Evidence and boundary:** 16 successful recorded executions in the November 1–20 window. Workflows are inactive and do not send messages. Supplied-website research was tested end-to-end; live search-provider acceptance remains a separate validation item.

### AI Business Automation Auditor

[**Explore the project**](projects/business-automation-auditor)

Two connected workflows gather business and website information, analyze possible automation opportunities, calculate an audit score, and prepare a report for human review.

**Stack:** Apify · Firecrawl · OpenRouter · Groq · Ollama · JavaScript · Google Sheets · n8n.

**Evidence and boundary:** In the November 1–20 history window, the parent workflow recorded 23 successes, 2 errors, and 1 cancellation; the website-audit engine recorded 39 successes and 7 errors. This remains a research prototype; recommendations need human verification.

### Business Opportunity Finder

[**Explore the project**](projects/business-opportunity-finder)

A research workflow that discovers businesses, reads websites, and prepares AI-assisted automation opportunity assessments for human review.

**Stack:** n8n · Google Maps discovery · Crawl4AI · OpenRouter · JavaScript · Google Sheets.

**Evidence and boundary:** The current 19-node n8n workflow is inactive and had one recorded error in the November 1–20 window. The public 17-node JSON is an earlier snapshot. Existing Google Sheets output is historical evidence, not proof of a continuously operating service. AI scores and recommendations are research suggestions, not verified business performance measurements.

## Customer support and property operations

### Automated Voice Inquiry & Support Dispatcher

[**Explore the project and workflow**](projects/voice-inquiry-dispatcher)

An authenticated audio request/response pipeline that normalizes uploaded audio, transcribes it with Whisper, prepares a response through an AI Agent with session memory, and synthesizes WAV audio with Piper.

**Stack:** n8n · Whisper · OpenRouter · AI Agent · Window Buffer Memory · Piper · JavaScript.

**Evidence and boundary:** The current source workflow is active. In the November 1–20 window, the 50 most recent retrieved execution records contained 35 successes and 15 errors (68 matching records existed in the full window). A fresh end-to-end audio acceptance test is required. This is not a PSTN telephone or call-transfer system.

### Anna AI — Intelligent Front Desk & Business Operations Agent

[**Explore the project**](projects/anna-omnichannel-receptionist)

A Groq-powered text receptionist prototype with session memory and Supabase conversation logging.

**Stack:** n8n · Groq · LangChain AI Agent · Window Buffer Memory · Supabase · JavaScript.

**Evidence and boundary:** A successful historical end-to-end text/Supabase execution is documented. The portfolio workflow is inactive; 9 of 19 recorded executions in the November 1–20 window succeeded. Calendar, Gmail, and voice actions remain separate validation items.

### Customer Engagement System

[**Explore the project**](projects/customer-engagement)

Two portfolio workflows explore customer-engagement monitoring and response management. Both are inactive and should be treated as design/prototype work unless a project-specific test is documented.

## Personal productivity

### Intelligent Gmail Manager

[**Explore the project**](projects/intelligent-gmail-manager)

A command-driven Gmail assistant for searching and reading messages, summarizing threads, classifying mail, and preparing cleanup proposals.

**Stack:** n8n · Gmail OAuth/API · JavaScript · Webhooks · MCP-assisted development.

**Evidence and boundary:** Three successful recorded tests. Read-only search and a simulated unauthorized Trash command were tested. The workflow is inactive and mailbox mutations remain disabled.

### Autonomous Job Sourcing & Application Drafting

[**Explore the project**](projects/autonomous-job-sourcing)

A research tool that discovers job listings, compares requirements with a candidate profile, scores fit, and prepares application drafts for human review.

**Stack:** n8n · JobSpy API · Airtable · AI scoring/drafting.

**Evidence and boundary:** Prototype; no automatic applications are submitted.

---

## Portfolio standards

- Public workflow exports are sanitized and intended for inspection, not one-click production use.
- Credentials, live webhook paths, private spreadsheet identifiers, and personal execution payloads are not published.
- A workflow marked active in n8n is not automatically a paid-client production deployment.
- Execution counts are dated history snapshots, not uptime or business-outcome metrics.
- Synthetic tests and simulated integrations are labeled.
- Preview deployments and development-store work are separated from production claims.
- The [visual proof gallery](VISUAL_PROOFS.md) distinguishes architecture maps, historical output screenshots, synthetic tests, and promotional artwork.
- The [n8n workflow alignment audit](N8N_WORKFLOW_AUDIT.md) records the connected inventory and known version differences.

[← Back to portfolio](README.md)
