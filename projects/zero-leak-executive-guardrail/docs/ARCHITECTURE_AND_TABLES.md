# Zero-Leak Architecture & Data Table Schemas

## Storage Layer (4 Isolated n8n Data Tables)

The suite persists state locally inside four isolated n8n Data Tables (`ZL_*`), avoiding brittle external database dependencies during intake while guaranteeing atomic auditability.

### 1. `ZL_Leads_Vault`
Primary persist-first intake vault (`upsert` keyed on `lead_key`).

| Column | Type | Purpose |
| --- | --- | --- |
| `lead_key` | string | Unique idempotency & correlation key (caller-supplied or FNV-1a hash of email + inquiry + UTC date) |
| `source` | string | Channel tag (`web_api`, `web_form`, `missed_call`, `email`, `dlq_retry`) |
| `name` | string | Normalized prospect name |
| `email` | string | Lowercased, format-validated prospect email |
| `phone` | string | Optional phone number |
| `company` | string | Company name (`Unspecified` default) |
| `inquiry_text` | string | Sanitized inquiry payload (`max 2000 chars`) |
| `requested_slot` | string | Normalized ISO-8601 consultation start timestamp |
| `status` | string | State machine: `RECEIVED` \| `RETRYING` \| `QUEUED_FOR_APPROVAL` \| `MANUAL_REVIEW` \| `DISPATCHED` \| `HELD` \| `SLOT_CONFLICT` |
| `lead_score` | number | Clamped `0..100` score from AI triage |
| `intent` | string | Triage intent (`consultation`, `quote_request`, `support_urgent`, `manual_review`, etc.) |
| `urgency` | string | `LOW` \| `NORMAL` \| `HIGH` \| `CRITICAL` |
| `ai_provider` | string | `gemini_pro_plus` \| `openrouter_fallback` \| `deterministic_fallback` |
| `draft_subject` | string | Generated reply email subject (held until approved) |
| `draft_reply` | string | Generated reply body (held until approved) |
| `approval_token` | string | One-time verification token (`tok_<16 hex chars>`) |
| `safety_flags` | string | Comma-separated matched deterministic risk flags or `none` |
| `calendar_status` | string | `NONE` \| `SLOT_CLEAR` \| `SLOT_CONFLICT` \| `BOOKING_CONFIRMED` \| `NO_SLOT_REQUESTED` |
| `booking_id` | string | Confirmed `BKG-<lead_key>` once dispatched |
| `retry_count` | number | Incremented automatically by `Workflow 03` retry cycles |
| `last_error` | string | Latest dispatch or runtime failure message |
| `created_at` | dateTime | Initial intake timestamp |
| `updated_at` | dateTime | Latest state mutation timestamp |

---

### 2. `ZL_Retry_Queue`
Dead-letter & self-healing recovery queue populated whenever both Primary and Backup AI models are unavailable (`MANUAL_REVIEW` state).

| Column | Type | Purpose |
| --- | --- | --- |
| `event_key` | string | Unique DLQ identifier (`DLQ-<lead_key>-<executionId>`) |
| `lead_key` | string | Reference into `ZL_Leads_Vault` |
| `workflow_name` | string | Originating workflow name |
| `failed_stage` | string | Stage label (`AI_TRIAGE_ALL_MODELS_FAILED`, etc.) |
| `error_message` | string | Failure detail |
| `payload_json` | string | Full JSON snapshot required to deterministically replay intake |
| `retry_count` | number | Number of recovery attempts performed |
| `max_retries` | number | Maximum attempts before `PERMANENT_FAIL` escalation (default `3`) |
| `status` | string | `PENDING_RETRY` \| `RECOVERED` \| `PERMANENT_FAIL` |
| `created_at` | dateTime | Enqueue timestamp |
| `updated_at` | dateTime | Last worker update timestamp |

---

### 3. `ZL_Bookings`
Deterministic consultation reservation ledger checked both during initial intake AND immediately before dispatching approved client replies.

| Column | Type | Purpose |
| --- | --- | --- |
| `booking_id` | string | `BKG-<lead_key>` |
| `lead_key` | string | Correlated Vault lead |
| `attendee_name` | string | Confirmed prospect name |
| `attendee_email` | string | Confirmed prospect email |
| `slot_start` | string | ISO-8601 start timestamp |
| `slot_end` | string | ISO-8601 end timestamp (+30m default consultation block) |
| `title` | string | Calendar consultation title |
| `status` | string | `CONFIRMED` |
| `created_at` | dateTime | Confirmation commit timestamp |

---

### 4. `ZL_Audit_Log`
Append-only compliance ledger recording every raw persist event, fallback recovery, invalid token block, conflict halt, hold, dispatch, error alert, and daily brief.

| Column | Type | Purpose |
| --- | --- | --- |
| `event_code` | string | Unique audit identifier |
| `lead_key` | string | Lead key, workflow ID, or `EXECUTIVE_BRIEF` |
| `actor` | string | `intake_gateway`, `gemini_pro_plus`, `openrouter_fallback`, `executive_decision_gate`, `dlq_retry_worker`, `error_handler` |
| `event_type` | string | Event classification (`INTAKE_PERSISTED_BEFORE_AI`, `AI_FALLBACK_RECOVERED`, `APPROVAL_QUEUED`, `INVALID_APPROVAL_TOKEN`, `BOOKING_SLOT_CONFLICT`, `LEAD_HELD`, `LEAD_APPROVED_AND_DISPATCHED`, `DLQ_RETRY_RECOVERED`, `EXECUTIVE_BRIEF_SENT`, etc.) |
| `summary` | string | Human-readable event description |
| `details_json` | string | JSON diagnostic payload |
| `created_at` | dateTime | Event UTC timestamp |
