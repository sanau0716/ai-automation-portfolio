# Lead Management System

An AI-powered lead management system built with n8n to automate lead qualification, personalized responses, and follow-up monitoring.

## Project Overview

This project demonstrates an end-to-end lead management process where incoming leads are analyzed by AI, qualified based on business criteria, and routed into appropriate follow-up actions.

The system is designed to reduce manual lead handling while helping businesses respond faster and prioritize leads based on their potential value.

The project contains two complementary workflows:

### Workflow 1 — Lead Qualification & Response

Analyzes newly received leads using AI and determines their qualification level.

The workflow evaluates lead information and produces structured analysis including:

- Lead score
- Lead qualification
- Lead analysis
- Recommended action
- Personalized response

Leads can then be handled differently depending on their qualification and potential business value.

### Workflow 2 — Lead Follow-Up Monitor

Monitors qualified leads and manages the follow-up process.

The workflow helps ensure that leads do not become forgotten after the initial response by tracking the appropriate follow-up stage and triggering communication when required.

## Architecture

```text
                    New Lead
                       │
                       ▼
                Lead Qualification
                       │
                       ▼
                  AI Analysis
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
        Lead Score         Qualification
              │                 │
              └────────┬────────┘
                       ▼
              Personalized Response
                       │
                       ▼
                Follow-Up Process
                       │
                       ▼
              Follow-Up Monitoring
                       │
                       ▼
                Next Action
