# Dashboard Integration Checklist
**Project:** SOAR Incident Containment Engine

**Branch:** aleena

**Prepared By:** Aleena (Dashboard / QA / Documentation)

**Date:** 29 July 2026

---

# Objective

Verify that the normalized alert output from Rajkumar's FastAPI listener contains all the required fields needed by the future SOAR Dashboard.

The dashboard requirements are defined in:

docs/dashboard_data_requirements.md

---

# Week 1 Integration Verification

| Dashboard Field | Expected | Available | Status | Notes |
|-----------------|----------|-----------|--------|------|
| Alert ID | Yes | Yes | ✅ Ready | Unique alert identifier available |
| Timestamp | Yes | Yes | ✅ Ready | Alert received time available |
| Source IP | Yes | Yes | ✅ Ready | Required for investigation |
| Alert Type | Yes | Yes | ✅ Ready | Example: brute_force |
| Host | Yes | Yes | ✅ Ready | Target system information available |
| Severity | Yes | Yes | ✅ Ready | Required for prioritization |

---

# Verified Normalized Output

Example

```json
{
  "alert_id": "ALT-1001",
  "timestamp": "2026-07-29T10:30:00Z",
  "source_ip": "192.168.1.100",
  "alert_type": "brute_force",
  "host": "server-01",
  "severity": "high"
}
```

---

# Dashboard Fields Still Required

The following fields are not expected in Week 1 and must be supplied during Week 2 and Week 3 development.

| Field | Owner | Purpose |
|--------|-------|---------|
| Reputation Score | Tejas | Threat intelligence score for the source IP |
| Risk Level | Tejas | Overall calculated incident priority |
| Playbook Name | Tejas | Name of the automated response playbook |
| Action | Tejas | Response taken (Block IP, Isolate Host, etc.) |
| Status | Tejas | Pending, Success, Failed |
| Timeline Event | Tejas | Chronological audit trail of incident actions |

---

# Integration Readiness Summary

## Available for Dashboard

- Alert ID
- Timestamp
- Source IP
- Alert Type
- Host
- Severity

These fields are sufficient to begin displaying basic alert information in the future dashboard.

---

## Pending for Future Integration

The dashboard cannot display the following features until Week 2/3 backend development is completed.

- Threat Reputation
- Risk Level
- Automated Playbook Name
- Containment Action
- Action Status
- Timeline Events

---

# Risks

No blocking issues identified for Week 1.

Dashboard development can continue using placeholder values until the remaining backend fields become available.

---

# Action Items

### Rajkumar

- Continue providing normalized alert data.
- Maintain field naming consistency.

### Tejas

Provide the following additional fields:

- reputation_score
- risk_level
- playbook_name
- action
- action_status
- timeline_event

### Aleena

- Update dashboard once new fields are available.
- Verify field mapping during Week 2 integration.
- Add UI components for incident timeline and action status.

---

# Conclusion

The Week 1 listener provides the minimum required alert information for dashboard integration.

No unexpected dashboard requirements have been identified.

Future development should focus on enriching alerts with threat intelligence, automated response information, and timeline events before the complete SOAR dashboard is implemented.
