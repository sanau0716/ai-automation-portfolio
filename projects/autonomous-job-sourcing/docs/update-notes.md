# Update Notes — Repaired Workflow Snapshot

## Source

Updated from the repaired n8n workflow export supplied on 2026-09-28.

## Notable changes reflected in this portfolio version

- Repaired `Calculate Candidate-Job Match` implementation is included rather than the older placeholder.
- Repaired `Extract Raw Job Text` implementation is included and uses safe field lookup across body, fields, or root JSON.
- JobSpy request body is driven by `Set Search Parameters1` instead of a hard-coded request body.
- Duplicate detection remains based on `Job ID` and is explicitly routed to `Duplicate - Skip`.
- AI output parsing and data-integrity merge logic are included.
- The repaired workflow keeps the 10-minute schedule trigger.
- The current search configuration is represented as workflow configuration rather than described as a fixed product behavior.
- Public GitHub sanitization removes credentials, Airtable resource IDs, Airtable URLs, the JobSpy API key, and instance-specific n8n metadata.

## Portfolio wording correction

The project is presented as an autonomous **sourcing, qualification, routing, and drafting** pipeline. It does not automatically submit job applications.
