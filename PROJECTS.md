# Projects I've Built

[← Back to the portfolio](README.md) · [Browse project folders](projects/README.md) · [n8n workflow alignment audit](N8N_WORKFLOW_AUDIT.md)

This portfolio contains independently developed AI automation systems, workflow prototypes, and application integrations. Each project distinguishes what is implemented, what has been tested, and what remains a prototype or validation task.

## Commerce and AI shopping

### CommercePilot — Shopify AI Shopping Assistant

[**Open the technical case study**](projects/commercepilot)

CommercePilot is the flagship platform project: a Shopify-native AI shopping assistant using n8n orchestration, Groq, store-scoped conversation context, Shopify catalog data, live variant availability checks, and conversation logging.

The surrounding platform includes Shopify App Proxy verification, Redis replay/rate controls, a health and latency monitor, and a Shopify app deployed to a Vercel Preview environment.

**Built with:** Shopify Admin GraphQL, Shopify App Proxy, n8n, Groq, Upstash Redis, Supabase/PostgreSQL, Prisma, TypeScript and Vercel.

**Verification snapshot (November 20, 2026):** 44 successful storefront-assistant executions; 26 successful catalog-sync executions and one recorded error; the health monitor has 212 executions in the November 1–20 window. The Shopify app Preview deployment is READY. The catalog sync workflow is explicitly limited to the development store. The assistant's current draft has 42 nodes while its published active version has 37, so draft-only changes are not described as published functionality.

This is a development project, not a paid-merchant deployment. The current location-level inventory implementation still requires end-to-end validation against the connected Shopify development store.

## Leads, sales, and business research

### AI Lead Qualification & Response

[**Explore the project**](projects/lead-management/n8n)

The active AwtomateAI website workflow captures incoming inquiries, uses an AI agent to qualify them, routes leads according to business rules, and integrates Gmail and Google Sheets.

**Built with:** n8n, webhooks, OpenRouter, JavaScript, Gmail and Google Sheets.  
**What I've verified:** 18 successful executions in the November 1–20, 2026 history window. The public workflow JSONs in this folder are older snapshots; the current 18-node active website-connected workflow is a separate n8n workflow and is documented as such.

The separate follow-up monitor is inactive. Its current 16-node n8n version differs from the older 15-node repository export.

### Campaign Research & Drafting Agent

[**Explore the project**](projects/campaign-research-agent) · [Setup](projects/campaign-research-agent/docs/setup.md) · [Validation](projects/campaign-research-agent/docs/validation.md)

A form-driven n8n system that researches supplied business websites with Crawl4AI, prepares evidence-checked outreach drafts using local Ollama, and stores them in a persistent review queue.

**Built with:** n8n Forms, HTTP Request, JavaScript, Serper, Crawl4AI, Python, PowerShell, Ollama and n8n Data Tables.  
**What I've verified:** 16 successful recorded executions in the November 1–20 window. The workflows are inactive and do not send messages. Supplied-website research was tested end-to-end; live search-provider acceptance remains a separate validation item.

### Business Opportunity Finder

[**Explore the project**](projects/business-opportunity-finder)

A business research workflow that discovers businesses, reads websites, and prepares AI-assisted automation opportunity assessments for human review.

**Built with:** n8n, Google Maps discovery, Crawl4AI, OpenRouter, JavaScript and Google Sheets.  
**Current state:** The current 19-node n8n workflow is inactive and had one recorded error in the November 1–20 window. The public 17-node JSON is an earlier snapshot. Earlier saved research outputs are historical examples, not proof of a continuously operating service.

### AI Business Automation Auditor

[**Explore the project**](projects/business-automation-auditor)

Two connected workflows gather business and website information, analyze possible automation opportunities, calculate an audit score, and prepare a report.

**Built with:** Apify, Firecrawl, OpenRouter, Groq, Ollama, JavaScript and Google Sheets.  
**What I've verified:** In the November 1–20 history window, the parent workflow recorded 23 successes, 2 errors and 1 cancellation; the website-audit engine recorded 39 successes and 7 errors. The system remains a research prototype; results need human verification.

## Customer support and property operations

### PropertyFix AI 2.0 — Maintenance Intelligence

[**Explore the project**](projects/propertyfix-ai)

A 17-node human-supervised maintenance intake and triage proof of concept. It preserves the original request, uses AI to suggest a category and priority, applies deterministic safety overrides, and routes a manager decision to a persistent case ledger.

**Built with:** n8n, OpenRouter, JavaScript, Data Tables, Gmail and Slack.  
**What I've verified:** 10 successful executions in the November 1–20 window using synthetic test data. It does not dispatch contractors, call emergency services, or make tenant-facing safety promises.

### Automated Voice Inquiry & Support Dispatcher

[**Explore the project and workflow**](projects/voice-inquiry-dispatcher)

An authenticated audio request/response pipeline that normalizes uploaded audio, transcribes it with Whisper, prepares a response through an AI Agent with session memory, and synthesizes WAV audio with Piper.

**Built with:** n8n, Whisper, OpenRouter, AI Agent, Window Buffer Memory, Piper and JavaScript.  
**Evidence and scope:** The current source workflow is active. In the November 1–20 window, the 50 most recent retrieved execution records contained 35 successes and 15 errors (68 matching records existed in the full window). A fresh end-to-end audio acceptance test is required. This is not a PSTN telephone or call-transfer system.

### Anna AI — Intelligent Front Desk & Business Operations Agent

[**Explore the project**](projects/anna-omnichannel-receptionist)

A Groq-powered text receptionist prototype with session memory and Supabase conversation logging.

**Built with:** n8n, Groq, LangChain AI Agent, Window Buffer Memory, Supabase and JavaScript.  
**Evidence and scope:** A successful historical end-to-end text/Supabase execution is documented. The portfolio workflow is currently inactive; 9 of 19 recorded executions in the November 1–20 window succeeded. Calendar, Gmail and voice actions remain separate validation items.

### Customer Engagement System

[**Explore the project**](projects/customer-engagement)

Two portfolio workflows explore customer-engagement monitoring and response management. Both are inactive and should be treated as design/prototype work unless a project-specific test is documented.

## Personal productivity

### Smart Scheduler V1

[**Explore the project**](projects/smart-scheduler)

An AI-assisted Gmail-to-Google-Calendar workflow that validates event details, checks conflicts, requests explicit approval, rechecks the calendar, creates the approved event, and persists a ledger record.

**Built with:** n8n, Gmail, Google Calendar, OpenRouter, JavaScript and Data Tables.  
**What I've verified:** 20 successful executions in the November 1–20 window. Real event creation was verified; sustained polling and load testing remain unverified.

### Intelligent Gmail Manager

[**Explore the project**](projects/intelligent-gmail-manager)

A command-driven Gmail assistant for searching and reading messages, summarizing threads, classifying mail, and preparing cleanup proposals.

**Built with:** n8n, Gmail OAuth/API, JavaScript, webhooks and MCP-assisted development.  
**What I've verified:** Three successful recorded tests. Read-only search and a simulated unauthorized Trash command were tested. The workflow is inactive and mailbox mutations remain disabled.

### Autonomous Job Sourcing & Application Drafting

[**Explore the project**](projects/autonomous-job-sourcing)

A research tool that discovers job listings, compares requirements with a candidate profile, scores fit, and prepares application drafts for human review.

**Built with:** n8n, JobSpy API, Airtable and AI scoring/drafting.  
**Current state:** Prototype; no automatic applications are submitted.

---

## Portfolio standards

- Public workflow exports are kept inactive and sanitized before sharing.
- Credentials, live webhook paths, private spreadsheet identifiers, and execution payloads are not intended for publication.
- A workflow being active in n8n does not by itself mean it is a production customer deployment.
- Test counts are execution-history evidence, not uptime or business-outcome claims.
- Preview deployments and development-store work are labeled separately from production.
- The [n8n workflow alignment audit](N8N_WORKFLOW_AUDIT.md) records the full connected workflow inventory and known snapshot differences.

[← Back to the portfolio](README.md)
