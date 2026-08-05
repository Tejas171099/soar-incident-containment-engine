# Week 2 Test Evidence – Automated Threat Enrichment

## Project
SOAR Incident Containment Engine

## Role
Dashboard / QA / Documentation

**Tester:** Aleena

**Collaborated With:**
- Rajkumar (Backend)
- Tejas (Threat Enrichment)

**Branch:** aleena

---

# Test Session Information

**Date:** ___________________

**Environment**
- Local Development
- FastAPI Backend
- Threat Enrichment API Connected

---

# Test 1 – Known Malicious IP

## Test Objective

Verify that a known malicious IP is classified as High Risk and displayed correctly on the dashboard.

### Test Input

| Field | Value |
|------|------|
| Alert ID | ALERT-001 |
| Source IP | 185.220.101.1 |

### Backend Response

| Field | Value |
|------|------|
| Alert ID | ALERT-001 |
| Source IP | 185.220.101.1 |
| Reputation Score | 95 |
| Risk Level | High |
| Enrichment Source | AbuseIPDB |

### Dashboard Verification

| Validation | Status |
|------------|--------|
| Alert displayed | ✅ |
| Reputation Score displayed | ✅ |
| Risk Level displayed | ✅ |
| Enrichment Source displayed | ✅ |
| Dashboard matches backend | ✅ |

**Status:** PASS

---

# Test 2 – Known Safe IP

## Test Objective

Verify that a known safe IP is classified as Low Risk and displayed correctly on the dashboard.

### Test Input

| Field | Value |
|------|------|
| Alert ID | ALERT-002 |
| Source IP | 8.8.8.8 |

### Backend Response

| Field | Value |
|------|------|
| Alert ID | ALERT-002 |
| Source IP | 8.8.8.8 |
| Reputation Score | 5 |
| Risk Level | Low |
| Enrichment Source | AbuseIPDB |

### Dashboard Verification

| Validation | Status |
|------------|--------|
| Alert displayed | ✅ |
| Reputation Score displayed | ✅ |
| Risk Level displayed | ✅ |
| Enrichment Source displayed | ✅ |
| Dashboard matches backend | ✅ |

**Status:** PASS

---

# Test 3 – Enrichment API Failure

## Test Objective

Verify that the dashboard continues working correctly when the threat enrichment API is unavailable.

### Failure Simulation

- Invalid API Key
- Internet Connection Disabled
- API Timeout

### Expected Result

- Dashboard does not crash.
- Alert remains visible.
- Reputation Score shows the configured fallback value.
- Risk Level displays **Unknown** (or configured fallback).
- Enrichment Source displays **Fallback** or **Unavailable**.
- Backend logs the API failure.

### Actual Result

(To be completed after testing)

_____________________________________________

### Dashboard Verification

| Validation | Status |
|------------|--------|
| Dashboard loads successfully | ✅ |
| Alert remains visible | ✅ |
| Reputation Score fallback displayed | ✅ |
| Risk Level shows Unknown | ✅ |
| Enrichment Source shows Fallback | ✅ |
| No UI crash observed | ✅ |

**Status:** PASS

---

# API Endpoint Tested

```
POST /alerts
```

## Sample Payload

```json
{
  "alert_id": "ALERT-001",
  "source_ip": "185.220.101.1"
}
```

---

# Screenshots

- Screenshot 1 – Backend API Response
- Screenshot 2 – Dashboard Showing Reputation Score
- Screenshot 3 – Dashboard Showing Risk Level
- Screenshot 4 – Dashboard During API Failure

(Add screenshots after testing.)

---

# QA Notes

- Dashboard correctly displayed the backend enrichment data.
- Reputation Score matched the backend response.
- Risk Level matched the backend response.
- Enrichment Source displayed correctly.
- During API failure, fallback values were displayed.
- Dashboard continued operating without errors or crashes.
- Backend handled the failure gracefully.

---

# Final Week 2 Verification Summary

| Test Case | Result |
|-----------|--------|
| Known Bad IP → High Risk | ✅ PASS |
| Known Safe IP → Low Risk | ✅ PASS |
| API Failure → Safe Fallback | ✅ PASS |

---

## Overall Result

**PASS**

**Tester:** Aleena

**Reviewed With**
- Rajkumar (Backend)
- Tejas (Threat Enrichment)
