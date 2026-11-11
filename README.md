# AI Automation Portfolio

### Hi, I'm an automation builder who enjoys turning repetitive work into simpler processes.

I work with **n8n, AI tools, APIs, and JavaScript** to connect systems and make everyday business tasks easier to manage.

I started building these projects to solve practical problems: following up with leads, understanding customer messages, researching potential clients, and keeping track of requests that would otherwise get lost in an inbox. Some are running in my own business; others are working prototypes that I've built and tested as I develop my skills.

You can explore the projects below, look through the workflows, and see what I've actually tested.

**[See all projects](PROJECTS.md)** · **[Project folders](projects/README.md)** · **[My website](https://awtomateai.com)**

## Start with these projects

If you're looking at my work for an automation or AI role, these three show different sides of what I can build.

### 1. [AI Lead Management — a workflow running on my website](projects/lead-management/n8n)

I built this to handle inquiries coming through [AwtomateAI](https://awtomateai.com). A new lead enters through the website, goes through AI-assisted qualification, and moves into the response workflow. I first tried the idea in Zapier, then rebuilt it in self-hosted n8n.

**Why it's worth a look:** It connects a real website to automation and has already handled genuine inquiries. It's my clearest example of building something I actually use. The follow-up workflow is still a prototype, and I don't claim closed client deals from it.

### 2. [Smart Scheduler V1 — Gmail to Calendar, with approval](projects/smart-scheduler)

I wanted a scheduling assistant that could read appointment emails without creating events based on guesses. It extracts the details, checks the calendar, asks for approval, and only then creates the event.

**Why it's worth a look:** I verified an actual Gmail-to-Google-Calendar event creation and saved the result in a ledger. The workflow is activated for my account, although longer-term unattended polling still needs verification.

### 3. [PropertyFix AI 2.0 — maintenance triage with human oversight](projects/propertyfix-ai)

I built this around a practical property-management problem: how to separate a routine repair request from something that needs immediate attention. It saves each request, suggests a priority and trade, applies safety rules, and sends the case for a manager's decision.

**Why it's worth a look:** It brings together AI classification, JavaScript safety checks, persistent records, Gmail approval, and Slack alert routing. I've tested routine and emergency examples with synthetic data. It's an unpublished prototype, not a tenant-facing emergency service.

## All seven projects

| Project | What it helps with | Current stage |
| --- | --- | --- |
| **[AI Lead Management](projects/lead-management/n8n)** | Captures and qualifies inquiries from my business website; includes an earlier [Zapier version](projects/lead-management/zapier). | Live qualification for my own business |
| **[Smart Scheduler V1](projects/smart-scheduler)** | Turns confirmed appointment emails into calendar events after approval and conflict checks. | Real event creation verified; ongoing polling not yet established |
| **[PropertyFix AI 2.0](projects/propertyfix-ai)** | Helps managers triage maintenance issues, spot safety concerns, and track review decisions. | Unpublished; synthetic tests completed |
| **[Business Opportunity Finder](projects/business-opportunity-finder)** | Researches businesses and identifies possible automation opportunities. | Tested with real research data |
| **[Customer Engagement System](projects/customer-engagement)** | Helps monitor customer concerns and organize responses. | Portfolio prototype |
| **[Business Automation Auditor](projects/business-automation-auditor)** | Reviews websites and suggests where process automation may help. | Portfolio prototype |
| **[Autonomous Job Sourcing](projects/autonomous-job-sourcing)** | Finds relevant jobs, compares requirements, and drafts applications for review. | Portfolio prototype |

[**Explore the full project stories and evidence →**](PROJECTS.md) · [Browse project folders](projects/README.md)

## How I work

I usually begin with the part of a process that's taking too much time or creating confusion. Then I sketch out the steps, connect the tools, add the logic, and test what happens when the information isn't as clean as expected.

I'm especially interested in the point where **AI helps make sense of information, but a person still makes the important decision**. You'll see that approach in projects that involve customer replies, scheduling, and maintenance requests.

### Tools I've worked with

**Automation:** n8n, Zapier, webhooks, REST APIs  
**AI:** OpenRouter, Gemini, structured AI responses  
**Code and data:** JavaScript, JSON, Google Sheets, Airtable  
**Other integrations:** Gmail, Slack, Google Calendar, Apify, Firecrawl, Crawl4AI  
**Infrastructure:** Self-hosted n8n and local development setups

## A quick note about the projects

I want the portfolio to show the work as it is, not make it sound bigger than it is.

The lead qualification workflow is connected to my own live website and has received actual inquiries. The Business Opportunity Finder has been tested on real research data. Smart Scheduler is activated for my own account but still needs longer-term monitoring. PropertyFix and the other projects are demonstrations or works in progress unless their README says otherwise. **These are not paid-client case studies**, and I don't claim results like revenue increases or hours saved without evidence.

If you're reviewing my work for a role or a project, I'd be glad for you to look at the workflow structure, decisions, and safeguards—not just the screenshots.

## Find me

- **GitHub:** https://github.com/sanau0716
- **AwtomateAI:** https://awtomateai.com
