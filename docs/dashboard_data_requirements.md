# Dashboard Data Requirements

## Purpose
This document defines the data required for the SOAR Dashboard. It helps the backend team understand which fields must be sent to the dashboard and identifies which fields are available in Week 1 and which will be added in later development.

| Field | Description | Required | Available in Week 1 | Available Later |
|--------|-------------|----------|---------------------|-----------------|
| Alert ID | Unique identifier for each alert | Yes | ✅ Yes | - |
| Time Received | Timestamp when the alert is received | Yes | ✅ Yes | - |
| Source IP | IP address that generated the alert | Yes | ✅ Yes | - |
| Alert Type | Type of security event (Brute Force, Malware, etc.) | Yes | ✅ Yes | - |
| Host | Target system or endpoint | Yes | ✅ Yes | - |
| Severity | Alert severity (Low, Medium, High, Critical) | Yes | ✅ Yes | - |
| Risk Score | Calculated numerical risk score | Yes | ❌ No | ✅ Week 2+ |
| Action Taken | Automated SOAR response (Block IP, Isolate Host, etc.) | Yes | ❌ No | ✅ Week 2+ |
| Action Status | Success, Failed, Pending Approval | Yes | ❌ No | ✅ Week 2+ |
| Timeline Events | Chronological log of investigation and actions | Yes | ❌ No | ✅ Week 3+ |

## Week 1 Available Data
- Alert ID
- Time Received
- Source IP
- Alert Type
- Host
- Severity

## Future Dashboard Data
- Risk Score
- Action Taken
- Action Status
- Timeline Events

## Notes
- Week 1 focuses on receiving and displaying alert information.
- Future weeks will integrate automated response data and case timeline information.
- The dashboard should be designed to support additional fields without major UI changes.
