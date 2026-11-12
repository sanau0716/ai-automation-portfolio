# AwtomateAI — Anna Omnichannel Receptionist (Groq · Portfolio)

**Functional AI-powered receptionist prototype | Extensively tested through 18 n8n execution runs**

Anna is an AI receptionist built using self-hosted n8n. It receives customer messages, validates requests, generates dynamic responses with a Groq-hosted model, maintains conversational session context, and logs inquiries to Supabase. A separate deterministic manual demonstration is available for offline testing.

## Functional architecture

- Protected webhook intake and customer-message normalization, including voice-channel metadata
- n8n AI Agent powered by Groq (`openai/gpt-oss-20b` at latest inspection)
- Window Buffer Memory attached to the AI Agent
- Structured chat responses suitable for downstream voice or chat interfaces
- Supabase insertion of inquiry and agent reply
- Google Calendar and Gmail escalation **tools configured** for scheduling and human handoff
- Dedicated rule-based manual demo branch

**Tools:** n8n, Groq, AI Agent, conversational memory, Supabase, Google Calendar, Gmail, JavaScript, MCP-assisted engineering.

## Successful and extensive testing

The recorded development history includes **18 manual executions: 8 successful and 10 failed**. Failed iterations were used to diagnose and correct implementation issues.

| Execution | Verified outcome |
| --- | --- |
| #440 | **End-to-end success:** webhook → validation → Groq AI Agent → Supabase log → response |
| #439 | Manual demonstration and Supabase read ran successfully |
| #438 | Database constraint issue identified while testing; later resolved for #440 |
| #436 | Missing-ID database issue identified; subsequent insertion passed |
| #423 | Safe rule-based consultation-request response passed |

**Successfully verified:** genuine AI-generated responses to business questions, complete text-chat processing path, execution of session-memory/model nodes, and successful Supabase logging. This is demonstrably functional, with recorded execution evidence rather than a purely conceptual design.

**Scope of verification:** Calendar event creation, actual Gmail escalation delivery, and live Vapi/PSTN calling are connected or prepared integration areas but were **not** independently established by those execution records. The workflow was inactive at inspection and is not represented as a production telephone service.

## Engineering and safeguards

The workflow uses header authentication for inbound requests, validates message length, and keeps actual booking and messaging claims dependent on successful external operations. Future iterations should separate conversational logs from the website's existing lead-intake table.

**Portfolio context:** Independently built and tested for AwtomateAI, not a paid-client case study.

[Browse all projects](../../PROJECTS.md)
