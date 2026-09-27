# Setup

## Requirements

- n8n
- An AI provider supported by the workflow
- Airtable account/database configured for your own environment
- Appropriate credentials for the services you choose to connect

## Configuration

After importing the workflow:

1. Open each AI/API node and select your own credential.
2. Replace Airtable placeholders with your own base/table IDs.
3. Review webhook and environment-specific URLs.
4. Test the workflow with sample data.
5. Verify Airtable writes before connecting production data.

## Security checklist

Before committing changes:

- [ ] No API keys
- [ ] No OAuth tokens
- [ ] No passwords
- [ ] No private webhook URLs
- [ ] No production customer/applicant records
- [ ] No private database credentials
