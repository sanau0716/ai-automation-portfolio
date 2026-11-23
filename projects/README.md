# Project folders

[← Portfolio home](../README.md) · [Technical case studies](../PROJECTS.md) · [Visual proof gallery](../VISUAL_PROOFS.md) · [n8n workflow audit](../N8N_WORKFLOW_AUDIT.md)

Open a project by the business problem it addresses. Each project README explains its implementation stage, technical approach, evidence, and limitations.

## Featured systems

| Project | Engineering focus | Current stage and evidence |
|---|---|---|
| **[CommercePilot — Shopify AI Shopping Assistant](commercepilot)** | Shopify app + n8n orchestration, catalog-grounded AI, App Proxy HMAC, Redis controls, variant availability, monitoring | Preview / development store; 44 successful assistant execution records; 42-node draft vs 37-node published version |
| **[AI Lead Management](lead-management)** | Website-connected lead intake, OpenRouter qualification, JavaScript parsing, conditional Gmail routing, Google Sheets | Active 18-node workflow; 18 successful execution records; current workflow differs from historical exports |
| **[PropertyFix AI 2.0](propertyfix-ai)** | Maintenance intake, AI triage, deterministic safety rules, persistent case records, manager approval | Active 17-node internal POC; 10 successful synthetic test runs; notifications/approval pinned or simulated |
| **[Smart Scheduler V1](smart-scheduler)** | Gmail/Calendar integration, event extraction, validation, deduplication, approval, final conflict recheck | Active 30-node workflow; 20 successful execution records; real event creation verified |

## Supporting projects

| Project | Why open it | Stage |
|---|---|---|
| [Pre-Call Account Intelligence Engine](account-intelligence-engine) | Live SSRF-safe web crawl, DNS/tech-stack detection, deterministic signal scoring, grounded Groq brief & Slack JSON | Live web tool at awtomateai.com/tools/account-intel; sanitized n8n export |
| [AI Business Automation Auditor](business-automation-auditor) | Business discovery, website research, AI opportunity analysis, scoring, and Sheets reporting | Research prototype; source/provider errors documented |
| [Campaign Research & Drafting Agent](campaign-research-agent) | Crawl4AI research, local Ollama drafting, evidence checks, persistent review queue | Inactive; no outbound sending |
| [Voice Inquiry & Support Dispatcher](voice-inquiry-dispatcher) | Audio intake, transcription, AI conversation, memory, and speech synthesis | Fresh end-to-end audio acceptance test required |
| [Anna Omnichannel Receptionist](anna-omnichannel-receptionist) | Groq text receptionist, session memory, and Supabase logging | Inactive portfolio prototype |
| [Intelligent Gmail Manager](intelligent-gmail-manager) | Read-only Gmail search, thread retrieval, and fail-closed mutation controls | Inactive; mailbox mutations disabled |
| [Business Opportunity Finder](business-opportunity-finder) | Business discovery, website crawling, AI research assessment, and Sheets output | Inactive current workflow; historical JSON snapshot |
| [Customer Engagement](customer-engagement) | Customer monitoring and response-management workflow patterns | Portfolio prototypes |
| [Autonomous Job Sourcing](autonomous-job-sourcing) | Job research, fit scoring, application drafting, and human review | Prototype; no automatic submissions |

## How to review these projects

1. Start with the case study to understand the business problem and scope.
2. Open the architecture visual to see the simplified system flow.
3. Read the verification section for dated execution evidence and test cases.
4. Check the limitations before interpreting the project as a production service.
5. Treat public workflow exports as sanitized historical/inspection artifacts; configure and review credentials, nodes, and external actions before any import or activation.

The [visual proof gallery](../VISUAL_PROOFS.md) collects the four flagship diagrams and clearly labels the existing historical output screenshot and CommercePilot promotional artwork.
