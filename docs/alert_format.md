# Alert Format Documentation

## Purpose

This document defines the standard alert format used by the SOAR Incident Containment Engine.

The ingestion service receives alerts from external SIEM platforms and converts them into a common internal format for downstream processing.

---

## Incoming SIEM Alert

Example:

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

## Normalized Alert

```json
{
  "alert_id": "ALERT-001",
  "timestamp": "2026-07-29T10:30:00",
  "source_ip": "8.8.8.8",
  "alert_type": "Malware",
  "target_host": "DESKTOP-01",
  "severity": "High"
}
```

---

## Field Mapping

| Incoming Field | Normalized Field |
|---------------|------------------|
| id | alert_id |
| time | timestamp |
| src_ip | source_ip |
| type | alert_type |
| host | target_host |
| severity | severity |

---

## Purpose of Normalization

Normalization ensures alerts from different SIEM platforms have a consistent schema before enrichment and automated response.
