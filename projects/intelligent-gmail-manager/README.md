# AwtomateAI — Intelligent Gmail Manager

**Functional Intelligent Gmail Assistant | Successfully tested Gmail search and safety controls**

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
| #442 | **Success:** five real inbox results returned with accurate sender, subject, ISO date, snippet, and labels |
| #443 | **Security test passed:** a simulated Trash command was rejected before any Gmail mutation node ran |

These are recorded, successful n8n executions. The read-only search functionality is operational, not merely a mockup.

## Safety design and scope

**Safety by design:** Label changes, archiving, drafts and Trash commands remain disabled until verified authorization and user-approval controls are in place. The workflow is inactive while external access and permission management are finalized.

Additional commands for reading messages, thread retrieval, classification and cleanup reviews are configured for further testing. There was no email deletion, archiving, labeling, or sending during the verified tests.

### Example input

```json
{"command":"search_emails","params":{"query":"in:inbox","limit":5}}
```

**Portfolio context:** Independently engineered and tested for personal productivity; not a paid-client deployment.

[Browse all projects](../../PROJECTS.md)
