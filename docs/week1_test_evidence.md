# Week 1 Test Evidence – SIEM Alert Ingestion

## Project
SOAR Incident Containment Engine

## Task
Day 5 – Join the Listener Test and Capture Evidence

## Tested By
- Aleena (Dashboard / QA / Documentation)
- Rajkumar (FastAPI Listener)
- Merin (Testing Support)

---

## Test Information

**Date:** 29 July 2026

**Testing Tool:**
- FastAPI Swagger UI / Postman

**Endpoint Used:**

POST /alerts

Example:
http://localhost:8000/alerts

---

## Sample Test Payload

```json
{
  "alert_id": "ALT-1001",
  "timestamp": "2026-07-29T10:30:00Z",
  "source_ip": "192.168.1.100",
  "alert_type": "brute_force"
}
```

---

## Expected Result

- API accepts the alert.
- HTTP Status Code: 200 OK
- JSON success response is returned.
- Alert is recorded by the listener.

---

## Actual Result

**HTTP Status Code:** 200 OK *(Update with actual result)*

**Response Body**

```json
{
  "status": "success",
  "message": "Alert received successfully"
}
```

*(Replace with the actual response if it differs.)*

---

## Test Status

**Result:** ✅ PASS

or

**Result:** ❌ FAIL

---

## Screenshot Evidence

| Screenshot | Description |
|------------|-------------|
| postman_alert_success.png | Successful alert submission |
| swagger_listener_test.png | FastAPI Swagger UI response |

*(Update with the actual screenshot filenames if available.)*

---

## Observations

- Listener accepted the sample SIEM alert successfully.
- Required fields were validated.
- Response was received within the expected time.
- No unexpected errors were observed during the test.

---

## Mismatch Report (if applicable)

If any issue is identified, document it politely and clearly.

### Example

**Issue**

The API returned **HTTP 400** when the `source_ip` field was omitted.

**Expected**

A validation error indicating that `source_ip` is a required field.

**Actual**

The response returned a generic error message without specifying the missing field.

**Recommendation**

Improve validation messages so users can quickly identify missing or invalid fields.

---

## QA Sign-off

| Name | Role | Status |
|------|------|--------|
| Aleena | Dashboard / QA / Documentation | ✅ Reviewed |
| Rajkumar | Backend / FastAPI | ✅ Verified |
| Merin | Testing Support | ✅ Confirmed |
