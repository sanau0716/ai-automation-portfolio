# AI Customer Engagement System

**Status:** Runnable portfolio implementation  not deployed in a live business environment.

An AI-powered customer engagement and email response system developed with n8n.

The project contains two complementary workflows with **36 nodes in total**, demonstrating customer risk analysis, AI-assisted email classification, conditional routing, automated responses, historical data management, and human escalation.

## Project Overview

| Workflow | Nodes | Primary Function |
|---|---:|---|
| Customer Engagement Monitor | 16 | Customer risk assessment and follow-up routing |
| Customer Response Manager | 20 | AI-assisted incoming email processing and response management |

These are separate workflows that can be configured and executed independently. They are not presented as an active production integration.

## Workflow 1  Customer Engagement Monitor

**File:** [phase-1-customer-engagement-monitor.json](phase-1-customer-engagement-monitor.json)

### Processing Architecture

1. Receive customer data through an n8n webhook.
2. Validate the customer entry using an AI node.
3. Parse the validation result and route accepted data.
4. Retrieve previous customer analysis from an n8n Data Table.
5. Prepare customer information and historical context.
6. Run AI customer risk analysis.
7. Parse and save the analysis results.
8. Route the customer according to risk classification.

### Risk-Based Routing

| Risk Level | Configured Path |
|---|---|
| HEALTHY | Record healthy customer information |
| AT RISK | Prepare follow-up content and send a Gmail message |
| URGENT | Prepare urgent alert details and send a Gmail notification |

### Integrations

- n8n Webhook
- AI analysis and validation nodes
- n8n Data Tables
- JavaScript Code nodes
- Switch routing
- Gmail

## Workflow 2  Customer Response Manager

**File:** [phase-2-customer-response-manager.json](phase-2-customer-response-manager.json)

### Processing Architecture

1. Receive an incoming customer email through Gmail Trigger.
2. Retrieve the email details.
3. Check the sender to reduce self-reply loops.
4. Retrieve matching customer history from an n8n Data Table.
5. Route unknown customers to a notification path.
6. Analyze recognized customer emails using Gemini.
7. Parse the structured AI response.
8. Route the email according to urgency.
9. Send a response or escalate to a human.
10. Log customer interactions or escalations.

### AI Analysis

The Gemini node requests structured information about:

- Customer intent and message category
- Sentiment
- Urgency
- Human intervention requirements
- Recommended next action
- Personalized response

The configured model is `models/gemini-flash-lite-latest`.

### Priority-Based Routing

| Urgency | Configured Path |
|---|---|
| LOW | Prepare and send low-priority reply |
| MEDIUM | Prepare and send medium-priority reply |
| HIGH | Prepare human escalation and send an alert |

Successful email response paths connect to customer interaction logging. The human escalation path connects to separate escalation logging.

### Error and Exception Handling

The workflow includes:

- A sender-address check intended to prevent self-reply loops
- A customer lookup and unknown-customer notification path
- A separate parsing-error output connected to an AI error alert
- Human escalation for high-urgency messages

The exported self-reply condition contains an email placeholder that must be configured before use.

The AI parser normalizes urgency to uppercase but does not fully validate all expected response fields. Unexpected urgency values may not match the configured routing rules.

## Technologies

| Category | Technology |
|---|---|
| Automation | n8n |
| AI | Gemini and AI analysis nodes |
| Email | Gmail Trigger and Gmail |
| Data Storage | n8n Data Tables |
| Logic | JavaScript, IF nodes, Switch nodes |
| Integration | Webhooks and structured JSON |

## Running the Workflows

1. Import the workflow JSON files into a compatible n8n instance.
2. Configure the required Gmail and AI credentials.
3. Configure the customer data tables and expected fields.
4. Replace any placeholder configuration values.
5. Review sender filters, routing rules, and AI output handling.
6. Test each workflow with sample customer records and messages.
7. Verify the response, escalation, and error paths before enabling unattended execution.

## Deployment Status and Limitations

Both workflows were developed as portfolio projects and are not currently published as live business automations.

The workflows are available for execution when their dependencies and credentials are configured.

The repository demonstrates workflow architecture and implementation, but does not establish production uptime, measured customer retention, verified delivery success, or commercial results.

Additional validation, security review, and end-to-end testing would be appropriate before production deployment.