# AwtomateAI — Anna Omnichannel Receptionist (Groq · Portfolio)

**Functional AI-powered receptionist | Successfully tested with real n8n executions**

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

The receptionist has been exercised through repeated n8n tests, including successful end-to-end execution of the AI text-receptionist path. Development tests were used to troubleshoot and refine the Supabase integration.

| Execution | Verified outcome |
| --- | --- |
| #440 | **End-to-end success:** webhook → validation → Groq AI Agent → Supabase log → response |
| #439 | Manual demonstration and Supabase read ran successfully |
| #423 | Safe rule-based consultation-request response passed |

**Successfully verified:** genuine AI-generated responses to business questions, complete text-chat processing, session-memory/model node execution, and successful Supabase logging. The workflow is functional and supported by saved execution evidence.

**Next integration validations:** End-to-end Calendar bookings, Gmail escalations and Vapi/PSTN calling. The tested conversational workflow is kept inactive while those external integrations are finalized.

## Engineering and safeguards

The workflow uses header authentication for inbound requests, validates message length, and keeps actual booking and messaging claims dependent on successful external operations. Future iterations should separate conversational logs from the website's existing lead-intake table.

**Portfolio context:** Independently built and tested for AwtomateAI, not a paid-client case study.

[Browse all projects](../../PROJECTS.md)
