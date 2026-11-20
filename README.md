# AI Automation Portfolio

### AI Automation Specialist | n8n Workflow Engineering | LLM Agents | API Integrations | JavaScript & Python

I design and build practical AI-powered automations that connect language models, business processes, APIs, and operational tools.

My work goes beyond connecting nodes. I build complete workflows with input validation, structured AI outputs, deterministic business rules, human approval where needed, persistent records, error handling, and monitoring.

**Current focus:** CommercePilot — a Shopify AI shopping assistant combining a Shopify app, n8n orchestration, Groq, Redis security controls, catalog synchronization, and live availability checks.

[**Explore all projects**](PROJECTS.md) · [**Review the n8n workflow audit**](N8N_WORKFLOW_AUDIT.md) · [**Browse project folders**](projects/README.md) · [**AwtomateAI**](https://awtomateai.com)

---

## Featured projects

### 1. [CommercePilot — Shopify AI Shopping Assistant](projects/commercepilot)

**Flagship platform build · Preview deployment ready · Development-store validation**

A Shopify-native shopping assistant designed to answer product questions using the merchant's own catalog, match relevant products, check live variant availability, maintain store-scoped conversation context, and log conversations. The wider implementation includes Shopify App Proxy verification, Redis replay/rate controls, catalog synchronization, location-level inventory work, and health monitoring.

**Stack:** Shopify Admin GraphQL · Shopify App Proxy · n8n · Groq · Upstash Redis · Supabase/PostgreSQL · Prisma · TypeScript · Vercel.

**Evidence:** 44 successful storefront-assistant executions in the November 1–20, 2026 history window; 26 successful catalog-sync runs out of 27 recorded runs. The Shopify app Preview deployment is marked READY. This is still a development-store project, not a paid-merchant deployment. The current assistant draft and published version differ; see the [case study](projects/commercepilot) for the exact release boundary.

### 2. [AI Lead Qualification & Response](projects/lead-management/n8n)

An active n8n workflow connected to the AwtomateAI website. It receives inquiries, uses an AI agent to qualify leads, routes them by business rules, and connects Gmail and Google Sheets for follow-up and records.

**Stack:** n8n · Webhooks · OpenRouter · JavaScript · Gmail · Google Sheets.

**Evidence:** 18 successful executions recorded in the November 1–20, 2026 history window. The repository also contains older workflow snapshots; the current active workflow is documented separately from those exports.

### 3. [PropertyFix AI 2.0 — Maintenance Intelligence](projects/propertyfix-ai)

A human-supervised maintenance intake and triage proof of concept. It preserves the original request, uses AI to suggest a category and priority, applies deterministic safety overrides, and routes a manager decision to a persistent case ledger.

**Stack:** n8n · OpenRouter · JavaScript · Data Tables · Gmail · Slack.

**Evidence:** 10 successful recorded executions in the November 1–20, 2026 window, using synthetic test data. It does not dispatch contractors or provide emergency response.

### 4. [Smart Scheduler V1](projects/smart-scheduler)

An AI-assisted Gmail-to-Google-Calendar workflow with structured event extraction, date/time validation, duplicate screening, calendar conflict checks, explicit approval, and a final recheck before creating an event.

**Stack:** n8n · Gmail · Google Calendar · OpenRouter · JavaScript · Data Tables.

**Evidence:** 20 successful recorded executions in the November 1–20, 2026 window. Real event creation was verified; load testing and sustained production polling remain unverified.

### 5. [AI Business Automation Auditor](projects/business-automation-auditor)

A multi-workflow research system that discovers businesses, gathers website content, uses AI to identify possible automation opportunities, calculates a score, and prepares a report for human review.

**Stack:** n8n · Apify · Firecrawl · OpenRouter · Groq · Ollama · JavaScript · Google Sheets.

**Evidence:** The parent workflow has 23 successful runs, 2 errors, and 1 cancellation; the website-audit engine has 39 successful runs and 7 errors in the November 1–20 history window. It remains a research prototype, not a validated commercial audit service.

### 6. [Campaign Research & Drafting Agent](projects/campaign-research-agent)

A form-driven research workflow that uses Crawl4AI and local Ollama to investigate supplied business websites, validate supporting evidence, prepare outreach drafts, and store them in a persistent review queue.

**Stack:** n8n · Python · Crawl4AI · Serper · Ollama · JavaScript · Data Tables.

**Evidence:** 16 successful recorded executions in the November 1–20 window. The workflows are currently inactive and do not send outreach.

---

## More projects

| Project | What it demonstrates | Current state |
|---|---|---|
| [Automated Voice Inquiry & Support Dispatcher](projects/voice-inquiry-dispatcher) | Audio intake, Whisper transcription, AI conversation, session memory, Piper speech synthesis | Active source; fresh audio acceptance test required |
| [Anna AI — Intelligent Front Desk](projects/anna-omnichannel-receptionist) | Groq AI Agent, session memory, structured customer response, Supabase logging | Portfolio workflow inactive; historical tests documented |
| [Intelligent Gmail Manager](projects/intelligent-gmail-manager) | Gmail search, message/thread retrieval, classification design, fail-closed mutation controls | Inactive; read-only tests verified |
| [Business Opportunity Finder](projects/business-opportunity-finder) | Google Maps discovery, website crawling, AI opportunity assessment, Sheets reporting | Inactive; current n8n version differs from repository snapshot |
| [Customer Engagement System](projects/customer-engagement) | Customer monitoring and response-management workflow patterns | Portfolio prototypes |
| [Autonomous Job Sourcing](projects/autonomous-job-sourcing) | Job discovery, match scoring, application drafting, manual review | Prototype; no automatic submissions |

[**See all project details →**](PROJECTS.md)

---

## Core engineering capabilities

- **Workflow engineering:** n8n, Zapier, triggers, webhooks, subworkflows, scheduling, branching, batching, retries, and error workflows.
- **AI orchestration:** LLM agents, prompt design, structured output parsing, session memory, model routing, and local inference.
- **API integration:** REST and GraphQL APIs, request normalization, HMAC verification, authenticated webhooks, and third-party service integration.
- **Business logic:** JavaScript and Python transformations, validation, deterministic rules, deduplication, idempotency, and human-in-the-loop approvals.
- **Data and persistence:** Supabase/PostgreSQL, n8n Data Tables, Google Sheets, Redis/Upstash, and structured audit records.
- **Reliability:** health checks, latency monitoring, alert routing, failure handling, safe fallbacks, and execution-history review.
- **Commerce automation:** Shopify Admin GraphQL, App Proxy, catalog synchronization, product discovery, and inventory availability.

## Tools and technologies

**Automation:** n8n, Zapier, webhooks, subworkflows  
**AI:** Groq, OpenRouter, Ollama, Gemini, LangChain AI Agent, structured output parsers  
**Development:** JavaScript, TypeScript, Python, JSON, PowerShell  
**Data:** Supabase, PostgreSQL, Redis/Upstash, n8n Data Tables, Google Sheets, Airtable  
**Integrations:** Shopify, Gmail, Google Calendar, Slack, Apify, Firecrawl, Crawl4AI, Serper  
**Deployment and operations:** Vercel, self-hosted n8n, local AI services, health monitoring

## How I approach automation

1. Understand the actual business process and the failure cases.
2. Normalize and validate inputs before sending them to an AI model.
3. Use AI for interpretation and drafting—not as the only source of truth.
4. Apply deterministic rules for permissions, safety, routing, and state changes.
5. Require human approval for consequential actions where appropriate.
6. Persist useful records and make failures observable.
7. Test the workflow and document what is verified, simulated, pending, or intentionally disabled.

## Evidence and transparency

This repository distinguishes active workflows, inactive prototypes, historical exports, and preview deployments. Execution counts are n8n history snapshots, not uptime guarantees or customer outcome metrics. Synthetic tests are identified as synthetic. No paid-client results, revenue gains, conversion lifts, or time-saved figures are claimed without evidence.

See the [n8n-to-GitHub alignment audit](N8N_WORKFLOW_AUDIT.md) for the 36-workflow inventory and known version differences.

## Contact and opportunities

I am interested in **AI Automation Specialist, n8n Automation Developer, Workflow Automation Engineer, and AI Integration Developer** opportunities, as well as practical automation projects.

- **GitHub:** https://github.com/sanau0716
- **Portfolio:** https://github.com/sanau0716/ai-automation-portfolio
- **AwtomateAI:** https://awtomateai.com
