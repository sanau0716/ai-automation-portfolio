# Workflow Architecture

## Pipeline

The workflow follows a staged automation pattern:

```text
Input
  ↓
Preparation / normalization
  ↓
AI analysis
  ↓
Matching and qualification
  ↓
Recommendation
  ↓
Conditional routing
  ↓
Application drafting
  ↓
Airtable tracking
```

## Core design idea

The important part of the system is the decision layer between raw job information and downstream actions.

Instead of treating every job equally, the workflow analyzes the available information and routes the opportunity according to the resulting recommendation.

## Human-in-the-loop

External actions should remain reviewable.

The recommended portfolio interpretation is:

```text
AI analyzes
    ↓
AI recommends
    ↓
Human reviews
    ↓
Application is submitted
```

This reduces the risk of automatically applying to unsuitable or misleading opportunities.

## Data boundary

The public repository contains a sanitized workflow export. Production credentials and environment-specific identifiers must be configured separately.
