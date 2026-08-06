# Integration Contract

 branch/merin
## Purpose

This document defines the data exchanged between the Alert Normalization module and the Threat Enrichment module.

## Input Required by Threat Enrichment Module

| Field | Description |
|--------|-------------|
| alert_id (or id) | Tracks which alert the enrichment result belongs to |
| source_ip (or src_ip) | IP address to check reputation |
| alert_type (or type) | Type of alert (e.g., brute_force, malware) |
| target_host (or host) | Target host involved in the alert |
| severity | Alert severity level |

## Notes

- The most critical field is *source_ip*.
- The enrichment module uses *source_ip* to check the IP reputation.
- The normalized alert should always provide a consistent IP field name.

## Dashboard Requirements

The dashboard should display the following fields:

| Field | Description |
|--------|-------------|
| Alert ID | Unique identifier for each alert |
| Time Received | Timestamp when the alert is received |
| Source IP | IP address that generated the alert |
| Alert Type | Type of security event |
| Host | Target system or endpoint |
| Severity | Alert severity level |
| Risk Score | Calculated numerical risk score |
| Action Taken | Automated SOAR response |
| Action Status | Success, Failed, or Pending |
| Timeline Events | Chronological log of investigation and actions |

### Week 1 Available Data
- Alert ID
- Time Received
- Source IP
- Alert Type
- Host
- Severity

### Future Dashboard Data
- Risk Score
- Action Taken
- Action Status
- Timeline Events

## Endpoint

```
POST /alerts
```

---

## Request Format

Content-Type

```
application/json
```

Example Request

```json
{
  "id": "ALERT-001",
  "time": "2026-07-29T10:30:00",
  "src_ip": "8.8.8.8",
  "type": "Malware",
  "host": "DESKTOP-01",
  "severity": "High"
}
```

---

## Response

HTTP Status

```
200 OK
```

Example Response

```json
{
  "status": "received",
  "normalized_alert": {
    "alert_id": "ALERT-001",
    "timestamp": "2026-07-29T10:30:00",
    "source_ip": "8.8.8.8",
    "alert_type": "Malware",
    "target_host": "DESKTOP-01",
    "severity": "High"
  },
  "enrichment": {
    "reputation_score": 0,
    "risk_level": "Low",
    "recommended_action": "Monitor",
    "source": "AbuseIPDB"
  },
  "message": "Alert received and enriched successfully"
}
```

---

## Validation

The API validates incoming JSON using Pydantic.

Required fields

- id
- time
- src_ip
- type
- host
- severity

---

## Error Responses

400 Bad Request

Invalid JSON.

422 Unprocessable Entity

Missing or invalid fields.

500 Internal Server Error

Unexpected server-side error.
 main
