# Autonomous Job Sourcing & Drafting Pipeline

An n8n-based AI automation system for sourcing, analyzing, qualifying, and preparing job opportunities for application.

## What this project demonstrates

This project demonstrates how AI can be combined with workflow automation to turn unstructured job-posting data into a structured decision pipeline.

The workflow includes:

- Job intake and normalization
- AI-powered job analysis
- Candidate/job matching
- Recommendation routing
- Airtable-based job tracking
- Application-drafting workflow
- Automated status updates

## High-level architecture

```text
Job Data
   │
   ▼
Normalize / Prepare Data
   │
   ▼
AI Job Analysis
   │
   ├──────────────► Job Requirements
   │
   ├──────────────► Candidate Fit
   │
   └──────────────► Recommendation
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
           APPLY      CONSIDER      SKIP
             │
             ▼
     Application Drafting
             │
             ▼
       Airtable Tracking
```

## Why this workflow exists

Manually reviewing job postings creates repetitive work:

1. Read the posting.
2. Identify requirements.
3. Compare the role against a candidate profile.
4. Decide whether the opportunity is worth pursuing.
5. Record the opportunity.
6. Prepare application material.

The workflow moves those repetitive analysis steps into an automated pipeline while keeping the final application decision under human control.

## AI decision layer

The workflow does not simply generate text. It uses AI to analyze job information and produce structured decisions that can drive subsequent workflow branches.

The portfolio version is configured with placeholders for external credentials and identifiers. It is intentionally not connected to the original production resources.

## Repository structure

```text
autonomous-job-sourcing-ai/
├── README.md
├── workflow/
│   └── autonomous-job-sourcing-pipeline.json
├── docs/
│   ├── architecture.md
│   └── setup.md
├── prompts/
│   ├── job-analysis.md
│   └── application-drafting.md
├── sample-data/
│   └── sample-job.json
└── screenshots/
    └── README.md
```

## Portfolio / demo version

This repository contains a sanitized n8n export.

Before importing it into another environment, replace the following placeholders with the user's own resources:

- Airtable base/table identifiers
- n8n webhook or environment-specific URLs
- AI/API credentials
- Other environment-specific configuration

**Do not commit real API keys, OAuth tokens, passwords, or private customer data.**

## Importing into n8n

1. Download the workflow JSON.
2. Open an n8n instance.
3. Use the workflow import option.
4. Import `workflow/autonomous-job-sourcing-pipeline.json`.
5. Configure your own credentials.
6. Replace placeholder Airtable IDs and other environment-specific values.
7. Test with sample data before connecting production systems.

## Important design principle

The workflow is designed as an **AI-assisted decision system**, not an autonomous system that blindly submits applications.

A recommendation such as `APPLY` should be treated as an automation output that can be reviewed before an external action is taken.

## Security

This repository is intentionally sanitized for public demonstration.

Never publish:

- API keys
- OAuth tokens
- Passwords
- Private webhook URLs
- Personal applicant/customer data
- Production database identifiers when they expose private infrastructure

## Technology

- n8n
- AI/LLM workflow nodes
- Airtable
- Webhooks / structured job data
- JavaScript workflow logic

## Status

**Portfolio project — sanitized demonstration version**

The production workflow may contain environment-specific configuration that is intentionally removed from this repository.
