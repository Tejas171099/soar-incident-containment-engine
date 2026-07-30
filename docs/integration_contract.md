# Integration Contract

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
