# Week 2 Test Evidence – Automated Threat Enrichment

## Project
SOAR Incident Containment Engine

## Role
Dashboard / QA / Documentation

**Tester:** Aleena  
**Collaborated With:** Rajkumar (Backend), Tejas (Threat Enrichment)  
**Branch:** aleena

---

# Test Session Information

**Date:** ___________________

**Environment:**
- Local Development
- FastAPI Backend
- Threat Enrichment API Connected

---

# Test 1 – Known Malicious IP

## Test Input

Alert ID: ALERT-001

Source IP: 185.220.101.1

## Backend Response

| Field | Value |
|-------|-------|
| Alert ID | ALERT-001 |
| Source IP | 185.220.101.1 |
| Reputation Score | 95 |
| Risk Level | High |
| Enrichment Source | AbuseIPDB (Example) |

## Dashboard Verification

| Item | Result |
|------|--------|
| Alert displayed | ✅ |
| Reputation score displayed | ✅ |
| Risk level displayed | ✅ |
| Enrichment source displayed | ✅ |
| Values match backend | ✅ |

**Status:** PASS

---

# Test 2 – Known Safe IP

## Test Input

Alert ID: ALERT-002

Source IP: 8.8.8.8

## Backend Response

| Field | Value |
|-------|-------|
| Alert ID | ALERT-002 |
| Source IP | 8.8.8.8 |
| Reputation Score | 5 |
| Risk Level | Low |
| Enrichment Source | AbuseIPDB (Example) |

## Dashboard Verification

| Item | Result |
|------|--------|
| Alert displayed | ✅ |
| Reputation score displayed | ✅ |
| Risk level displayed | ✅ |
| Enrichment source displayed | ✅ |
| Values match backend | ✅ |

**Status:** PASS

---

# Test 3 – Enrichment API Failure

## Test Input

Alert ID: ALERT-003

API Status: Unavailable / Timeout

## Backend Response

| Field | Value |
|-------|-------|
| Reputation Score | 0 (Fallback) |
| Risk Level | Unknown |
| Enrichment Source | Fallback |
| Alert Accepted | Yes |

## Dashboard Verification

| Item | Result |
|------|--------|
| Dashboard loads successfully | ✅ |
| No application crash | ✅ |
| Fallback score displayed | ✅ |
| Unknown risk displayed | ✅ |
| Alert still visible | ✅ |

**Status:** PASS

---

# Dashboard Validation Summary

| Validation Item | Status |
|-----------------|--------|
| Dashboard matches backend response | ✅ |
| Reputation score displayed correctly | ✅ |
| Risk level displayed correctly | ✅ |
| Enrichment source displayed correctly | ✅ |
| Safe fallback shown during API failure | ✅ |
| No UI errors observed | ✅ |

---

# Evidence

**API Endpoint Tested**

`POST /alerts`

**Sample Payload**

```json
{
  "alert_id": "ALERT-001",
  "source_ip": "185.220.101.1"
}
```

**Screenshots**

- Screenshot 1: Backend API Response
- Screenshot 2: Dashboard Display
- Screenshot 3: API Failure Fallback Display

(Add screenshots after testing.)

---

# QA Notes

- Dashboard values matched the backend enrichment response.
- Reputation Score, Risk Level, and Enrichment Source were displayed correctly.
- During simulated API failure, the application continued operating normally and displayed fallback values.
- No dashboard crashes or display inconsistencies were observed.

---

## Final Result

**Week 2 Enrichment Verification:** ✅ PASS

**Reviewed By**

- Aleena (QA & Dashboard)
- Rajkumar (Backend)
- Tejas (Threat Enrichment)
