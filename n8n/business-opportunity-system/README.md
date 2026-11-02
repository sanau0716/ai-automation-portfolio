# AI Business Opportunity Finder

**Status:** Tested with real-world business data; independently developed and used for business opportunity research.

A 17-node n8n automation workflow that discovers businesses within a configured geographic search area, crawls their websites, and uses AI to identify potential opportunities for business process automation.

## Real-World Application

This workflow has been used to research actual businesses within selected geographic search areas.

AI-generated business opportunity assessments were successfully saved to Google Sheets.

This demonstrates practical execution with real business data, rather than only a conceptual workflow design.

## Workflow Architecture

1. **Start Business Finder** - Initiates the research workflow.
2. **Create Google Maps Job** - Submits a business discovery job.
3. **Check Scraper Job Status** - Checks the external scraping job.
4. **Wait and Retry** - Waits 30 seconds before checking again when required.
5. **Download Scraper Results** - Retrieves business discovery data.
6. **Extract Business Records** - Extracts structured business records.
7. **Has Website?** - Filters businesses based on website availability.
8. **Limit** - Limits the records passed to website analysis.
9. **Crawl4AI Website Audit** - Requests website information.
10. **Clean Crawl4AI Data** - Processes the retrieved website data.
11. **Loop Over Items** - Coordinates iterative AI analysis.
12. **AI Business Opportunity Analysis** - Uses an OpenRouter-connected language model.
13. **Parse AI Analysis** - Processes AI-generated assessment data.
12. **AI Business Opportunity Analysis** - Uses an OpenRouter-connected language model.
13. **Parse AI Analysis** - Processes AI-generated assessment data.
14. **Save Business Audit** - Records successful assessments in Google Sheets.

The workflow also includes an AI error-handling path that reconnects to item processing.

## Technologies

| Category | Technology |
|---|---|
|---|---|
| Automation | n8n |
| Business Discovery | Google Maps scraping integration |
| Website Research | Crawl4AI |
| AI | OpenRouter Chat Model and LLM Chain |
| Data Processing | JavaScript Code nodes |
| Reporting | Google Sheets |
| API Integration | HTTP Request nodes |
| Workflow Control | IF, Wait, Limit, Split in Batches |

## Technical Features

- Configurable geographic business discovery
- Asynchronous scraping job polling
- Business record extraction and filtering
- Website crawling and data cleaning
- AI-assisted identification of automation opportunities
- Iterative processing of business records
- AI error-handling branch
- Google Sheets reporting

## Workflow File

[crawl4ai-business-opportunity-finder.json](crawl4ai-business-opportunity-finder.json)

## Running the Workflow

1. Import the JSON workflow into a compatible n8n instance.
2. Configure the required external scraping and Crawl4AI services.
3. Configure OpenRouter credentials and the selected model.
4. Configure the Google Sheets destination and credentials.
5. Review the geographic search parameters and processing limits.
6. Test the workflow with a small business discovery batch.
7. Verify the generated assessments and saved Google Sheets records.

## Deployment Status and Limitations

This workflow has been executed using real-world business data, and generated assessments have been saved to Google Sheets.

It is not presented as a continuously operating production service.

AI-generated opportunities are research suggestions that require human verification. The project does not claim verified business savings, customer acquisition, or commercial revenue.

Before wider deployment, additional review of API reliability, retry limits, error handling, data quality, and scraping-service terms would be appropriate.