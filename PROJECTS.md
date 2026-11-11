# Project Directory

[← Portfolio home](README.md) · [n8n catalog](n8n/README.md) · [Zapier catalog](zapier/README.md)

Use this directory to locate each project by **business problem, technology, deployment status, and evidence**. Links are to existing locations on `main` unless labeled as a pending PR.

## Sales and marketing operations

### AI Lead Management & Qualification

**[Open project](n8n/lead-management-system)** · [Original Zapier version](zapier/leadflow-ai)

- **Purpose:** Intake, AI-assisted qualification, routing, and lead responses for AwtomateAI.
- **Stack:** n8n, website webhook, Gmail, Google Sheets, JavaScript.
- **Evidence:** Lead qualification connected to the author's live business website and has received real inquiries.
- **Scope:** Follow-up monitoring is a portfolio implementation; the Zapier and n8n versions represent a migration of the *same* system, not two separate delivered projects.
- **Limitations:** No verified paying-client conversions or revenue gains.

### Business Opportunity Finder

**[Open project](n8n/business-opportunity-system)** · [Sample result screenshot](n8n/business-opportunity-system/screenshots/business-opportunity-results.png)

- **Purpose:** Discover businesses, analyze their websites, and identify possible automation opportunities.
- **Stack:** Google Maps discovery, Crawl4AI, OpenRouter, Google Sheets.
- **Evidence:** Real-world business research execution and result screenshot.
- **Limitations:** Exploration and generated scores are not verified commercial results or a continuously running service.

### Business Automation Auditor

**[Open project](n8n/business-audit-system/business-automation-auditor)**

- **Purpose:** Website and business audit workflows that identify possible automation opportunities.
- **Stack:** Apify, Firecrawl, AI analysis, JavaScript scoring, Google Sheets.
- **Evidence:** Workflow documentation and exports in the project directory.
- **Status:** Portfolio implementation.

## Customer and property operations

### AI Customer Engagement System

**[Open project](n8n/customer-engagement-system)**

- **Purpose:** Monitor engagement risks and support AI-assisted response management.
- **Stack:** n8n, classification, conditional routing, email response logic.
- **Evidence:** Documented two-phase workflow implementation.
- **Status:** Portfolio implementation, not deployed live.

### PropertyFix AI 2.0 — Maintenance Intelligence

**[Preview PR #2](https://github.com/sanau0716/ai-automation-portfolio/pull/2)** — *pending review; its folder does not yet exist on `main`*

- **Purpose:** Structured maintenance intake, AI triage, deterministic safety elevation, manager review, and a persistent case ledger.
- **Stack:** n8n, OpenRouter, JavaScript, Gmail, Slack, n8n Data Tables.
- **Evidence:** Synthetic routine and electrical-hazard tests and recorded manager decisions.
- **Status:** Unpublished portfolio proof of concept, not a live tenant system.
- **Limitations:** No automatic dispatch. PropertyFix Slack notifications in the workflow were simulated during tests; wider safety and production testing remain.

## Personal productivity and scheduling

### Autonomous Job Sourcing & Application Drafting

**[Open project](autonomous-job-sourcing-ai)** · [Workflow screenshot](autonomous-job-sourcing-ai/screenshots/autonomous-job-sourcing-workflow.png)

- **Purpose:** Find job opportunities, assess fit, and draft applications for human review.
- **Stack:** JobSpy API, Airtable, AI scoring, n8n.
- **Evidence:** Documentation, workflow export, and workflow image.
- **Status:** Portfolio implementation with no verified end-to-end production deployment.
- **Limitation:** Does **not** automatically submit applications.

### Smart Scheduler V1

**[Preview PR #1](https://github.com/sanau0716/ai-automation-portfolio/pull/1)** — *pending review; its folder does not yet exist on `main`*

- **Purpose:** Convert selected confirmed appointment emails into Google Calendar events after explicit approval.
- **Stack:** n8n, Gmail, Google Calendar, OpenRouter, Data Tables.
- **Evidence:** Real approved event creation and ledger persistence demonstrated in n8n tests.
- **Status:** Activated for own Gmail/Calendar; sustained production polling has not yet been verified.
- **Limitations:** Concurrency and live error-trigger behavior still need broader testing.

---

## Where code and exports live

| Location | Contents |
| --- | --- |
| [`n8n/`](n8n/README.md) | Automation project folders, READMEs, and workflow exports |
| [`zapier/`](zapier/README.md) | Original Zapier LeadFlow AI implementation |
| [`autonomous-job-sourcing-ai/`](autonomous-job-sourcing-ai) | Job research architecture, prompts, sample data, workflow and screenshot |

**How statuses are used:** *Live* means running for the author's own operations; *tested* means the described test was observed; *portfolio implementation* means a documented demo/POC without a verified production deployment; *pending PR* means the change has not yet been merged into `main`.

[↑ Back to portfolio home](README.md)
