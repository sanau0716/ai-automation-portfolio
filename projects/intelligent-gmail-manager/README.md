# AwtomateAI — Intelligent Gmail Manager

**Functional, successfully tested read-only Gmail management workflow**

This n8n project provides Gmail search, structured outputs, message and thread retrieval architecture, email classification, label inventory, and cleanup proposals for an MCP-connected AI assistant.

## What works

- Gmail OAuth integration and successful live mailbox search
- Query-based search capped at ten messages, with message identifiers and metadata
- Correct sender, recipient, subject, timestamp, snippet, and label formatting
- Command-based workflow routing through an n8n webhook
- Read-only cleanup proposals and safe rejection of unauthorized modifications
- Dedicated nodes for further classification, summarization, label, archive, and draft features

**Stack:** Self-hosted n8n, Gmail API/OAuth, JavaScript, webhooks, Model Context Protocol (MCP)-assisted development.

## Successfully tested against Gmail

| Execution | Verified result |
| --- | --- |
| #441 | Real Gmail search returned five messages and exposed a result-formatting bug |
| #442 | **Success:** five real inbox results returned with accurate sender, subject, ISO date, snippet, and labels |
| #443 | **Security test passed:** a simulated Trash command was rejected before any Gmail mutation node ran |

These are recorded, successful n8n executions. The read-only search functionality is operational, not merely a mockup.

## Safety design and scope

The original generated approval tokens were Base64-encoded rather than securely authenticated. They were therefore disabled: **label changes, archive, drafts, and Trash commands are blocked at the command router** until a trusted approval system is built. The workflow is inactive; public webhook authentication also requires hardening before any deployment.

Message reading, thread retrieval, classification, and cleanup rules are configured but should be validated individually before claiming complete coverage. There was no email deletion, archiving, labeling, or sending during the verified tests.

### Example input

```json
{"command":"search_emails","params":{"query":"in:inbox","limit":5}}
```

**Portfolio context:** Independently engineered and tested for personal productivity; not a paid-client deployment.

[Browse all projects](../../PROJECTS.md)
