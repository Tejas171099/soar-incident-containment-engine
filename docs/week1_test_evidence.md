# Week 1 Test Evidence

## Environment

Operating System

Windows 11

Python Version

Python 3.12

Framework

FastAPI

Testing Tool

Swagger UI

---

## Test Input

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

## Expected Result

- API accepts request.
- Alert is normalized.
- Threat intelligence lookup is performed.
- HTTP 200 response is returned.

---

## Actual Result

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

## Test Status

PASS

The API successfully completed all required Week 1 functionality, including validation, normalization, enrichment, and response generation.
