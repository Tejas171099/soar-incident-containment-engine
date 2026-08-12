# Week 3 Test Evidence – Rajkumar

## Project
SOAR Incident Containment Engine

## Role
Ingestion & Threat Intelligence Enrichment

## Objective
The purpose of Week 3 testing is to verify that the threat intelligence enrichment function handles successful lookups and external API failures safely.

The enrichment function must:

- Use a timeout when calling the external API.
- Handle HTTP/API errors.
- Handle network errors.
- Handle timeout errors.
- Handle JSON parsing errors.
- Return safe default values when enrichment fails.
- Prevent the main alert-processing pipeline from crashing.

---

## Test Case 1 – Successful Threat Intelligence Lookup

### Test Objective
Verify that a valid IP address can be sent to the enrichment service and that the system returns a reputation score and enrichment source.

### Input
IP Address: 8.8.8.8

### Expected Result
The AbuseIPDB lookup should complete successfully and return a reputation score and source.

Expected fields:

- reputation_score
- source
- country
- isp
- asn

### Actual Result
The alert was successfully received by the FastAPI `/alerts` endpoint.

The alert was normalized and the enrichment function was triggered automatically.

Example response:

```json
{
  "status": "received",
  "enriched_alert": {
    "alert_id": "A123",
    "timestamp": "2026-07-21T10:00:00+00:00",
    "source_ip": "8.8.8.8",
    "alert_type": "Malware",
    "target_host": "WEB-01",
    "severity": "High",
    "enrichment": {
      "reputation_score": 0,
      "source": "abuseipdb",
      "country": "US",
      "isp": "Google LLC",
      "asn": "Unknown"
    }
  },
  "message": "Alert received and enriched successfully"
}
