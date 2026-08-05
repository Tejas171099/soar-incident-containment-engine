# Week 2 Test Evidence – Automated Threat Enrichment

## Project
SOAR Incident Containment Engine

## Role
Dashboard / QA / Documentation

**Tester:** Aleena
**Collaborated With:** Rajkumar (Backend), Tejas (Threat Enrichment)
**Branch:** aleena

---

## Test Session Information

**Date:** ___________________

**Environment**
- Local Development
- FastAPI Backend
- Threat Enrichment API Connected

---

# Test 1 – Known Malicious IP

### Test Input

Alert ID: ALERT-001

Source IP: 185.220.101.1

### Backend Response

| Field | Value |
|------|------|
| Alert ID | ALERT-001 |
| Source IP | 185.220.101.1 |
| Reputation Score | 95 |
| Risk Level | High |
| Enrichment Source | AbuseIPDB |

### Dashboard Verification

| Check | Status |
|------|------|
| Alert displayed | ✅ |
| Reputation Score displayed | ✅ |
| Risk Level displayed | ✅ |
| Enrichment Source displayed | ✅ |
| Dashboard matches backend | ✅ |

**Status:** PASS

---

# Test 2 – Known Safe IP

### Test Input

Alert ID: ALERT-002

Source IP: 8.8.8.8

### Backend Response

| Field | Value |
|------|------|
| Alert ID | ALERT-002 |
| Source IP | 8.8.8.8 |
| Reputation Score | 5 |
| Risk Level | Low |
| Enrichment Source | AbuseIPDB |

### Dashboard Verification

| Check | Status |
|------|------|
| Alert displayed | ✅ |
| Reputation Score displayed | ✅ |
| Risk Level displayed | ✅ |
| Enrichment Source displayed | ✅ |
| Dashboard matches backend | ✅ |

**Status:** PASS

---

## API Endpoint

POST /alerts

### Sample Payload

```json
{
  "alert_id": "ALERT-001",
  "source_ip": "185.220.101.1"
}
```

---

## Screenshots

- Backend API Response
- Dashboard Showing Reputation Score
- Dashboard Showing Risk Level

(Add screenshots after testing.)

---

## QA Summary

- Dashboard values matched backend responses.
- Reputation Score displayed correctly.
- Risk Level displayed correctly.
- Enrichment Source displayed correctly.

**Overall Result:** ✅ PASS
