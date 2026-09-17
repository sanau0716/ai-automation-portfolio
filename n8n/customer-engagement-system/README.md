# AI Customer Engagement System

An AI-powered customer engagement system built with n8n to monitor customer activity, assess customer risk, and manage customer responses using AI-driven workflows.

## Project Overview

This project contains two complementary n8n workflows that work together to support customer engagement and communication.

### Workflow 1 — Customer Engagement Monitor

Monitors customer activity and analyzes customer health using AI.

The workflow evaluates customer information and interaction history, identifies potential customer risk, and determines whether a customer is:

- HEALTHY
- AT RISK
- URGENT

Based on the analysis, the workflow can trigger appropriate automated actions such as recording customer status, sending follow-up communication, or generating urgent alerts.

### Workflow 2 — Customer Response Manager

Analyzes incoming customer messages and helps manage appropriate responses.

The workflow uses AI to evaluate customer communication, including:

- Intent
- Category
- Sentiment
- Urgency
- Human intervention requirements
- Recommended action
- Personalized response

This allows customer communications to be analyzed and routed consistently while reducing repetitive manual work.

## Architecture

```text
Customer Activity / Message
            │
            ▼
      ┌───────────────┐
      │ Engagement    │
      │ Monitor       │
      └───────┬───────┘
              │
              ▼
       AI Customer Risk
           Analysis
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
    HEALTHY AT RISK URGENT
              │
              ▼
       Automated Actions


Incoming Customer Message
            │
            ▼
      ┌───────────────┐
      │ Customer      │
      │ Response      │
      │ Manager       │
      └───────┬───────┘
              │
              ▼
        AI Message
          Analysis
              │
              ▼
    Intent / Sentiment /
    Urgency / Category
              │
              ▼
      Recommended Action
              │
              ▼
      Personalized Response
