# Setup Notes

## Required connections

### OpenRouter
Attach your own OpenRouter credential to:

- `OpenRouter Chat Model1`
- `OpenRouter - Draft Generator`

### Airtable
Attach your own Airtable credential to all Airtable nodes and select your own base/table.

Expected table name in the workflow is `Jobs`.

### JobSpy
The workflow expects a JobSpy HTTP service at:

`http://host.docker.internal:8000/api/v1/search_jobs`

Change this to your own endpoint when the service is hosted elsewhere.

Set the `x-api-key` header to your own JobSpy API key after import.

## Before enabling the schedule

Review:

- search term
- target locations
- sites to query
- results count
- remote requirement
- Airtable mappings
- score thresholds
- application-draft prompt

The public repository copy intentionally leaves these environment-specific connection details for the person importing the workflow.
