# Enrichment API Contract

## Project

**SOAR Incident Containment Engine**

**Module:** Ingestion & Threat Intelligence Enrichment

**Developer:** Rajkumar

---

# Purpose

This document defines the request and response format for the enrichment API. It provides a stable interface for other team members to integrate with the enrichment service without needing to understand its internal implementation.

---

# Endpoint

**URL**

```
POST /alerts
```

**Content-Type**

```
application/json
```

---

# Request Schema

| Field    | Type     | Required | Description                        |
| -------- | -------- | -------- | ---------------------------------- |
| id       | string   | Yes      | Unique alert identifier            |
| time     | datetime | Yes      | Alert timestamp in ISO 8601 format |
| src_ip   | string   | Yes      | Source IP address                  |
| type     | string   | Yes      | Alert type                         |
| host     | string   | Yes      | Target host                        |
| severity | string   | Yes      | Alert severity                     |

---

# Example Request

```json
{
    "id": "A123",
    "time": "2026-07-21T10:00:00Z",
    "src_ip": "203.0.113.5",
    "type": "brute_force",
    "host": "web-server-01",
    "severity": "high"
}
```

---

# Response Schema

The API returns a normalized alert together with enrichment information.

| Field            | Type   | Description                     |
| ---------------- | ------ | ------------------------------- |
| status           | string | Processing status               |
| normalized_alert | object | Standardized alert fields       |
| enrichment       | object | Threat intelligence information |
| message          | string | Response message                |

---

## Normalized Alert Fields

| Field       | Type     |
| ----------- | -------- |
| alert_id    | string   |
| timestamp   | datetime |
| source_ip   | string   |
| alert_type  | string   |
| target_host | string   |
| severity    | string   |

---

## Enrichment Fields

| Field            | Type              | Description                  |
| ---------------- | ----------------- | ---------------------------- |
| reputation_score | integer           | Threat reputation score      |
| source           | string            | Threat intelligence provider |
| country          | string (optional) | Country of the IP address    |
| isp              | string (optional) | Internet Service Provider    |
| asn              | string (optional) | Autonomous System Number     |

---

# Example Response

```json
{
    "status": "received",
    "normalized_alert": {
        "alert_id": "A123",
        "timestamp": "2026-07-21T10:00:00+00:00",
        "source_ip": "203.0.113.5",
        "alert_type": "brute_force",
        "target_host": "web-server-01",
        "severity": "high"
    },
    "enrichment": {
        "reputation_score": 95,
        "source": "AbuseIPDB",
        "country": "United States",
        "isp": "Google LLC",
        "asn": "AS15169"
    },
    "message": "Alert received and enriched successfully"
}
```

---

# Error Response

If enrichment fails because of a timeout, network issue, or API error, the API returns safe default values.

```json
{
    "status": "received",
    "normalized_alert": {
        "alert_id": "A123",
        "timestamp": "2026-07-21T10:00:00+00:00",
        "source_ip": "203.0.113.5",
        "alert_type": "brute_force",
        "target_host": "web-server-01",
        "severity": "high"
    },
    "enrichment": {
        "reputation_score": 0,
        "source": "lookup_failed",
        "country": "Unknown",
        "isp": "Unknown",
        "asn": "Unknown"
    },
    "message": "Threat lookup failed. Default enrichment applied."
}
```

---

# Notes

* All incoming alerts are validated before enrichment.
* Alert fields are normalized into a common format before processing.
* Threat enrichment is triggered automatically after normalization.
* API keys are stored securely using environment variables.
* The API continues processing even if the external threat intelligence provider is unavailable.
