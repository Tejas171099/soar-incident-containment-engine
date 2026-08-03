# Dashboard Data Requirements

## Project
SOAR Incident Containment Engine

## Purpose
This document defines the data fields required by the dashboard to display security alerts and enriched threat intelligence information. These requirements support the integration of alert ingestion, automated threat enrichment, and SOAR playbook execution.

| Field Name | Week | Source | Required | Description |
|------------|------|--------|----------|-------------|
| Alert ID | Week 1 | Alert Ingestion | Yes | Unique identifier for each security alert. |
| Timestamp | Week 1 | Alert Ingestion | Yes | Time the alert was received. |
| Source IP | Week 1 | Alert Ingestion | Yes | IP address that generated the alert. |
| Alert Type | Week 1 | Alert Ingestion | Yes | Type of security event detected. |
| Host | Week 1 | Alert Ingestion | Yes | Host or endpoint associated with the alert. |
| Severity | Week 1 | Alert Ingestion | Yes | Initial severity assigned to the alert. |
| Reputation Score | Week 2 | Threat Enrichment | Yes | Numerical score indicating the reputation of the source IP or domain. |
| Risk Level | Week 2 | Threat Enrichment | Yes | Overall threat level such as Low, Medium, High, or Critical. |
| Recommended Action | Week 2 | SOAR Playbook | Yes | Suggested response based on the enrichment results. |
| Enrichment Source | Week 2 | Threat Enrichment | Yes | External intelligence provider used for enrichment (for example VirusTotal or AbuseIPDB). |

## Dashboard Display Requirements

The dashboard should display:

- Alert ID
- Timestamp
- Source IP
- Alert Type
- Host
- Severity
- Reputation Score
- Risk Level
- Recommended Action
- Enrichment Source

## Notes

- Week 1 focused on alert ingestion and dashboard planning.
- Week 2 introduces automated threat enrichment.
- The dashboard must clearly display the enrichment results for each alert.
- QA testing must verify that enrichment data is displayed correctly and that the dashboard behaves safely if the external enrichment service is unavailable.
