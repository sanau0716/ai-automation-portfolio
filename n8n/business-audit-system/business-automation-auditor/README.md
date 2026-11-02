# AI Business Automation Auditor

An n8n-based automation project that combines business discovery, website analysis, AI-assisted opportunity identification, audit scoring, and reporting.

## Project Status

Portfolio automation project. The repository contains workflow definitions demonstrating the system architecture. Production reliability, commercial deployment, and measured business outcomes are not claimed.

## Business Problem

Evaluating businesses for potential automation opportunities can require repetitive research, website reviews, and manual analysis.

This project explores how AI agents and workflow automation can streamline that process.

## Solution Overview

The system is organized into two connected workflows.

### 1. Business Automation Auditor

**File:** `ai-business-automation-auditor.json`

- Receives business discovery requests through an n8n webhook.
- Uses Apify to search for businesses through Google Maps.
- Retrieves discovered business information.
- Checks whether a business has a website.
- Processes eligible businesses through a loop.
- Calls the Website Auditor Engine as a subworkflow.

### 2. Website Auditor Engine

**File:** `website-auditor-engine.json`

- Accepts input from the parent workflow.
- Uses HTTP requests and Firecrawl for website data retrieval.
- Prepares website content for AI processing.
- Uses AI agents to analyze businesses and identify automation opportunities.
- Uses structured output parsing for opportunity analysis.
- Calculates an audit score through a JavaScript Code node.
- Includes Google Sheets storage and AI-generated report steps.
- Contains conditional scraping checks and a dedicated scrape-failure handling node.

## Technology Stack

| Technology | Purpose |
|---|---|
| n8n | Workflow orchestration |
| Apify | Business discovery through Google Maps |
| Firecrawl | Website content extraction |
| OpenRouter | AI model connectivity |
| n8n AI Agents | Business analysis and opportunity identification |
| JavaScript | Data preparation, scoring, and failure processing |
| Google Sheets | Audit data storage |
| Webhooks and HTTP | Workflow initiation and API communication |

## Architecture

```text
Business Discovery Webhook
          |
          v
Apify Google Maps Search
          |
          v
Retrieve Business Results
          |
          v
Check Website Availability
          |
          v
Loop Through Eligible Businesses
          |
          v
Website Auditor Subworkflow
          |
          +-- HTTP / Firecrawl Website Retrieval
          |             |
          |             +-- Scraping Failure Handling
          |
          +-- AI Business Analysis
          |
          +-- AI Opportunity Identification
          |
          +-- Audit Scoring
          |
          +-- Google Sheets Storage
          |
          +-- AI Report Generation
```

This diagram is a simplified representation of the workflow architecture.

## Reliability Considerations

The workflow definitions include:

- Conditional website and scraping checks.
- Retry configuration on the Firecrawl node.
- Error-output handling on HTTP and Firecrawl nodes.
- A dedicated scraping failure handler.

Additional production hardening may include monitoring, error notifications, provider fallbacks, and retry policies for other external services.

## Skills Demonstrated

- Multi-workflow orchestration
- API and webhook integration
- AI agent orchestration
- Structured AI output processing
- JavaScript data transformation
- Conditional routing and iteration
- Third-party service integration
- Workflow failure handling

## Limitations

The repository documents workflow design and implementation. It does not independently establish successful end-to-end execution, production uptime, client deployment, or measured ROI.

## Intended Use

Technical portfolio demonstration of AI-assisted business auditing and workflow automation.