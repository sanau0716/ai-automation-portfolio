# LeadFlow AI

**Status:** Original Zapier implementation; subsequently rebuilt in self-hosted n8n.

LeadFlow AI is an AI-assisted lead qualification and response automation project originally developed using Zapier.

After the Zapier trial expired, the project was rebuilt using self-hosted n8n. The n8n lead qualification workflow is currently deployed on awtomateai.com.

This repository preserves the original Zapier implementation as evidence of cross-platform automation development.

## Project Overview

LeadFlow AI was designed to automate lead intake, qualification, scoring, and follow-up.

The original Zapier implementation incorporates AI analysis, Google Sheets, Gmail, Slack, and workflow routing.

## Original Zapier Workflow

The documented process includes:

1. Capture incoming lead information.
2. Check for duplicate submissions.
3. Filter incomplete or invalid records.
4. Analyze lead information using AI.
5. Generate lead qualification scores.
6. Store lead information in Google Sheets.
7. Route leads according to qualification.
8. Send email follow-ups.
9. Notify the team about high-value leads.

## Lead Scoring

The original project documentation describes an AI-generated score from 1 to 100.

Example routing:

- **80-100:** High-value lead
- **Below 80:** Standard lead

These thresholds describe the original Zapier design and should not be assumed to match the current n8n implementation.

## Migration from Zapier to n8n

The project was initially implemented using Zapier.

Following the expiration of the Zapier trial, the lead qualification automation was rebuilt using self-hosted n8n.

The migration demonstrates experience with:

- Rebuilding business automation workflows across platforms
- Reconfiguring triggers and integrations
- Implementing AI-assisted lead qualification
- Working with email and structured data
- Maintaining the underlying lead-management use case

The n8n implementation is the currently deployed version.

## Current Implementation

The live n8n lead qualification workflow is integrated with awtomateai.com.

The repository also contains a separate n8n follow-up monitoring workflow developed for portfolio purposes.

These are related implementations and extensions of the same lead-management project, not unrelated client deploymentss.

[View the n8n Lead Management System](../../n8n/lead-management-system/README.md)

## Technologies

### Original Implementation

- Zapier
- AI / LLM
- Google Sheets
- Gmail
- Slack
- Webhooks
- Lead capture forms

### Rebuilt Implementation

- Self-hosted n8n
- AI-assisted lead qualification
- Webhooks
- Gmail
- Google Sheets
- JavaScript

## Workflow Export

[Sanitized Zapier Workflow JSON](zapier-workflows-sanitized.json)

The export is provided for portfolio review and may require additional configuration to run.

## Project Scope and Limitations

This README documents the original Zapier implementation and its subsequent migration to n8n.

The live n8n workflow has received real website inquiries, but this project does not claim verified customer conversions, paying clients, or quantified revenue improvements.

The Zapier and n8n versions should not be assumed to have identical node structures or feature sets.