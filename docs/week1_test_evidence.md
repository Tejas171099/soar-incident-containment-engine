# Week 1 Test Evidence

## Project
SOAR Incident Containment Engine

## Objective
Verify that the FastAPI alert ingestion endpoint accepts valid alerts and correctly handles invalid requests.

---

## Test Case 1: Valid Alert

**Date:** 03-Aug-2026

**Endpoint:** /alerts

**Test Payload:**

```json
{
  "alert_id": "ALRT-001",
  "timestamp": "2026-08-03T10:15:00Z",
  "source_ip": "192.168.1.50",
  "alert_type": "Brute Force",
  "host": "WEB-SRV-01",
  "severity": "High"
}
```

**Expected Result**

- Alert accepted successfully
- HTTP Status: 200 OK

**Actual Result**

- Alert accepted successfully
- HTTP Status: 200 OK

**Status:** PASS

**Screenshot:** alert_ingestion_success.png

---

## Test Case 2: Missing Source IP

**Expected Result**

Validation error returned.

**Actual Result**

HTTP 400 Bad Request returned because the source IP field was missing.

**Status:** PASS

**Screenshot:** missing_source_ip.png

---

## Test Case 3: Invalid Timestamp

**Expected Result**

Validation error returned.

**Actual Result**

HTTP 400 Bad Request returned for invalid timestamp format.

**Status:** PASS

**Screenshot:** invalid_timestamp.png

---

## Test Case 4: Missing Alert ID

**Expected Result**

Validation error returned.

**Actual Result**

HTTP 400 Bad Request returned because the alert ID was missing.

**Status:** PASS

**Screenshot:** missing_alert_id.png

---

## Summary

All planned Week 1 alert ingestion test cases were executed successfully.

The FastAPI listener correctly accepted valid alerts and rejected invalid requests with appropriate validation errors.

The dashboard documentation and QA evidence are ready for Week 2 integration.
