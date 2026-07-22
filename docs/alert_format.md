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
