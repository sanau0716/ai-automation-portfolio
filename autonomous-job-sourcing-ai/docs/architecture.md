# Architecture

## 1. Acquisition

`Schedule Trigger` runs every 10 minutes in the supplied workflow. `Set Search Parameters1` builds the search payload and `JobSpy - Search Jobs` sends it to the local JobSpy service.

## 2. Normalization

`Split Out` converts the returned `jobs` collection into individual items. `Normalize Job Payload` maps the JobSpy response into a stable internal structure containing job ID, title, company, source, URL, description, location, employment type, salary, skills, experience metadata, company metadata, and the original JobSpy payload.

## 3. Duplicate control

`Check Airtable for Duplicate` searches the Airtable `Jobs` table by `Job ID`. `Format Job Properties` restores the original normalized job alongside the search result, then `Is New Job?` determines whether processing continues or terminates in `Duplicate - Skip`.

This preserves original job data instead of allowing the Airtable lookup response to replace it.

## 4. AI extraction

`Extract Raw Job Text` builds a compact analysis payload. `Analyze Job Posting` asks the language model to extract:

- required skills
- experience requirement
- employment type
- location
- job summary
- AI/automation relevance

`Parse AI Analysis` reads several possible AI output fields, removes Markdown code fences, parses JSON, and merges the parsed fields back onto the original job item. Invalid AI JSON falls back to safe values rather than stopping the workflow.

## 5. Qualification and scoring

`Create Initial Airtable Entry` stores the analyzed job. `Calculate Candidate-Job Match` compares required skills against a configured target skill taxonomy and calculates skill, relevance, and remote scores.

`Calculate Overall Job Score` combines those scores using the configured weighting and optionally adds an entry-level boost. `Set Application Recommendation` converts the numeric score into `APPLY`, `CONSIDER`, or `SKIP`.

## 6. Routing

`Route Recommendation` branches the record:

- **APPLY:** update the record, generate an application draft, clean the AI output, and save the draft.
- **CONSIDER:** update the record as qualified for review.
- **SKIP:** mark the record as rejected/skipped.

## 7. Draft generation

`Generate Application Draft` receives the job title, company, job summary, required skills, matched skills, and job description. It requests a JSON object containing an `application_draft` string. `Clean AI Draft JSON` handles string/object outputs and strips accidental code fences before `Save Application Draft` persists the result.

## Design principles visible in the repaired workflow

- Preserve source data across AI and database operations.
- Treat AI output as untrusted structured input.
- Separate extraction from deterministic scoring.
- Separate scoring from routing.
- Use a human review boundary before application submission.
- Make duplicate control explicit before expensive AI processing.
