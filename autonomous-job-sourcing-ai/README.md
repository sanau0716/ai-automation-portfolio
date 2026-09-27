# Autonomous Job Sourcing & Application Drafting Pipeline

An n8n-based AI job sourcing pipeline that finds job listings, normalizes and de-duplicates them, analyzes requirements, scores candidate fit, routes the result, and generates an application draft for roles that meet the configured threshold.

## What this demonstrates

- Job aggregation through a local JobSpy API
- Data normalization before downstream processing
- Airtable-backed duplicate detection using Job ID
- Defensive parsing of structured AI output
- Candidate/job matching using an explicit skill taxonomy
- Weighted scoring for skill fit, AI/automation relevance, and remote compatibility
- Entry-level / low-experience scoring boost
- Rule-based APPLY / CONSIDER / SKIP routing
- AI-generated application drafting for APPLY results
- Airtable state updates across qualification stages
- Loop-based processing so multiple job results can move through the same pipeline

## Workflow architecture

```text
Schedule Trigger (10 min)
        |
        v
Set Search Parameters
        |
        v
JobSpy Search API
        |
        v
Split Out Jobs
        |
        v
Normalize Job Payload
        |
        v
Check Airtable for Duplicate ----> Duplicate - Skip
        |
        v
Format / restore job data
        |
        v
Is New Job?
        |
        v
Loop Over Items
        |
        v
Extract Raw Job Text
        |
        v
AI Job Analysis
        |
        v
Parse + merge AI output safely
        |
        v
Create Initial Airtable Entry
        |
        v
Candidate / Job Match
        |
        v
Overall Job Score
        |
        v
Application Recommendation
        |
        v
Route Recommendation
   /        |        \
 APPLY    CONSIDER    SKIP
   |          |          |
 Draft     Qualified   Rejected
   |
 Clean Draft JSON
   |
 Save Application Draft
```

## Scoring logic

The current workflow calculates:

- **Skill score:** 40% of the base score
- **AI/automation relevance:** 40%
- **Remote compatibility:** 20%
- **Entry-level boost:** +15 points when the posting indicates junior/entry-level/no-experience/training-friendly conditions

The final score is capped at 100.

Routing thresholds in the current workflow are:

- `81+` → `APPLY`
- `50–80` → `CONSIDER`
- `<50` → `SKIP`

These are implementation rules for the automation, not claims that the model's recommendation is objectively correct.

## AI components

The workflow currently uses OpenRouter-backed chat models. The job-analysis model is configured as `openai/gpt-oss-120b`; the application-drafting model is configured as `qwen/qwen3-235b-a22b-2507`.

The analysis prompt is instructed to return a fixed JSON schema and not invent unsupported job requirements. A separate parser strips accidental Markdown code fences and falls back to safe defaults when AI output cannot be parsed.

## Human-in-the-loop boundary

The pipeline automates sourcing, analysis, qualification, routing, and draft generation. It does **not** submit applications automatically. The generated application is stored for review, keeping the final submission decision under human control.

## Dependencies

- n8n
- JobSpy service/API reachable from n8n
- Airtable
- OpenRouter

## Import / setup

1. Import `workflow/autonomous-job-sourcing-drafting.json` into n8n.
2. Connect your own OpenRouter credential to the two OpenRouter nodes.
3. Connect your own Airtable credential to the Airtable nodes.
4. Select your own Airtable base and `Jobs` table in the Airtable nodes.
5. Configure the JobSpy API endpoint and API key.
6. Review the search parameters before enabling the schedule trigger.

The GitHub copy is intentionally sanitized; it does not contain the original Airtable IDs or credential references.

## Project status

This repository version represents a repaired and updated workflow snapshot. The n8n workflow itself remains the source of truth for the implementation details.
