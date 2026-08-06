 branch/merin
# Standard SIEM Alert Format

## Purpose

This document defines the standard alert format used by all project modules. Every alert generated in the system should follow this structure.

## Alert Fields

| Field | Description |
|---------|------------|
| id | Unique alert identifier |
| time | Date and time when the alert was generated |
| src_ip | Source IP address that triggered the alert |
| type | Type of security event |
| host | Hostname or device name |
| severity | Alert severity level |

## Example Alert

json
{
  "id": "ALERT-001",
  "time": "2026-07-22T10:30:00Z",
  "src_ip": "192.168.1.100",
  "type": "Failed Login",
  "host": "server01",
  "severity": "High"
}


## Expected Response Format

When an alert is received, the system should return:

json
{
  "status": "received",
  "alert_id": "ALERT-001",
  "message": "Alert processed successfully"
}


## Notes

- Use unique alert IDs.
- Time should follow ISO 8601 format.
- Severity values can be Low, Medium, High, or Critical.
- All modules should follow this format.

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
 main
