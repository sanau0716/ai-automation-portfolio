# Projects I've Built

[← Back to the portfolio](README.md) · [Browse project folders](projects/README.md)

Here's a closer look at what each project does, why I built it, and how far I've taken it.

## Leads, sales, and business research

### AI Lead Management & Qualification

[**Explore the project**](projects/lead-management/n8n) · [See the earlier Zapier version](projects/lead-management/zapier)

I wanted a better way to handle inquiries coming through [awtomateai.com](https://awtomateai.com). Instead of just sending every form submission to an inbox, I built a workflow that captures the details, uses AI to help qualify the inquiry, and routes information for a response.

I first made this in Zapier, then recreated it in my self-hosted n8n setup. **It's the same project across two platforms**, not two separate client systems. The lead qualification part is running on my website and has received real inquiries. The scheduled follow-up component is still a portfolio implementation.

**Built with:** n8n, webhooks, Gmail, Google Sheets, JavaScript, AI analysis.  
**What I've verified:** Live website lead intake and qualification. I haven't closed a paying automation client from these inquiries, so I don't present conversion or revenue results.

### Business Opportunity Finder

[**Explore the project**](projects/business-opportunity-finder) · [See sample results](projects/business-opportunity-finder/screenshots/business-opportunity-results.png)

Researching businesses one at a time can take a lot of effort. I built this workflow to collect business information, examine websites, and suggest where automation might help.

I ran it using real-world business research data and kept a screenshot of the results. The scores and recommendations are starting points for research, **not proof that a business needs a particular solution**.

**Built with:** Google Maps discovery, Crawl4AI, OpenRouter, Google Sheets.  
**Current stage:** Tested prototype, not a continuously operating service.

### Business Automation Auditor

[**Explore the project**](projects/business-automation-auditor)

This project came from a simple question: *Could I make the first pass of a business automation audit faster?*

I put together two workflows that gather website and business information, analyze it with AI, and produce possible areas to investigate further. It's designed to support a conversation with a business owner—not replace actually understanding how their team works.

**Built with:** Apify, Firecrawl, AI analysis, JavaScript scoring, Google Sheets.  
**Current stage:** Documented portfolio implementation with workflow exports.

## Customer support and property management

### AI Customer Engagement System

[**Explore the project**](projects/customer-engagement)

I wanted to explore how a team could spot customer issues earlier and keep responses organized. I built one workflow to monitor engagement signals and another to help manage incoming responses.

The goal was to make it easier to notice when a message deserves attention, while keeping controls around automated replies.

**Built with:** n8n, AI-assisted classification, conditional routing, email workflows.  
**Current stage:** Two-part prototype; not deployed for live customer support.

### PropertyFix AI 2.0

[**Explore the project**](projects/propertyfix-ai)

Maintenance requests don't always arrive with a clear priority. I built PropertyFix AI to collect the details, suggest a category and urgency level, and help a manager decide what to review first.

It also checks for warning signs such as smoke or dangerous wiring, keeps a case record, and supports Gmail approval and Slack alerts. I designed it to **assist a manager, not send contractors or make safety decisions on its own**.

**Built with:** n8n, OpenRouter, JavaScript, Gmail, Slack, n8n Data Tables.  
**What I've tested:** Simulated routine and emergency scenarios, including manager decisions. The workflow is now active in n8n. The documented PropertyFix-specific Slack tests were simulated, though the Slack bot connection was separately tested with a real message. This is **not** a verified emergency-response or contractor-dispatch service.

### Anna Omnichannel Receptionist (Groq · Portfolio)

[**Explore the tested project**](projects/anna-omnichannel-receptionist)

I built Anna to handle customer messages with a real AI Agent rather than a hardcoded chatbot. The protected webhook accepts inquiries, Groq generates helpful service answers, session memory supplies context, and Supabase records the request and answer.

**Built with:** n8n, Groq (`openai/gpt-oss-20b`), LangChain AI Agent, Window Buffer Memory, Supabase, Gmail and Google Calendar tools.  
**Successful functional testing:** Verified an actual end-to-end webhook → AI-generated reply → Supabase log → response execution (#440), alongside successful manual demonstration and data-access tests. Calendar booking, Gmail escalation and PSTN calling are additional integrations undergoing end-to-end validation.

## Personal productivity

### Intelligent Gmail Manager

[**Explore the tested project**](projects/intelligent-gmail-manager)

I built a command-driven Gmail management workflow so an MCP-connected AI assistant can search and inspect emails, organize cleanup proposals, and preserve control over mailbox changes. Gmail OAuth and an n8n command router supply the core integration.

**Built with:** n8n, Gmail OAuth/API, JavaScript, webhooks and MCP-assisted engineering.  
**Functional testing:** Live inbox search successfully returned five real messages (#441); after fixing formatting, #442 returned correct sender, subject, timestamp, snippet and labels. A simulated unauthorized Trash command was safely rejected (#443). **Mailbox modifications are deliberately disabled** until a secure approval mechanism and webhook authentication are completed.

### Autonomous Job Sourcing & Application Drafting

[**Explore the project**](projects/autonomous-job-sourcing) · [See the workflow](projects/autonomous-job-sourcing/screenshots/autonomous-job-sourcing-workflow.png)

Looking through job listings and comparing requirements can get repetitive. I built this tool to help find opportunities, check how closely a role matches a candidate's experience, and prepare an application draft.

The important part is that **a person reviews the draft before applying**. It doesn't automatically submit applications.

**Built with:** n8n, JobSpy API, Airtable, AI scoring and drafting.  
**Current stage:** Portfolio implementation; I haven't verified a fully deployed, unattended production run.

### Smart Scheduler V1

[**Explore the project**](projects/smart-scheduler)

I built Smart Scheduler to make it easier to turn confirmed appointments in Gmail into calendar events—without blindly booking everything that shows up in an email.

The workflow reads appointment details, prepares an event, and asks for approval first. I tested real approved event creation and the record-keeping that prevents obvious repeat handling.

**Built with:** n8n, Gmail, Google Calendar, OpenRouter, Data Tables.  
**Current stage:** Live in my n8n instance for my own Gmail and Calendar; real event creation verified. Sustained polling and every possible failure case have not been independently verified.

---

## Where to find the workflow files

| Folder | What's inside |
| --- | --- |
| [Project folders](projects/README.md) | All projects organized by the problem they solve, with workflow exports and documentation |

I try to make it clear which systems are live, which have been tested, and which are still prototypes. These are personal and portfolio projects, **not examples of paid client work**.

[← Back to the portfolio](README.md)
