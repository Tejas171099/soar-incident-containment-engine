# Week 2 QA Test Cases – Automated Threat Enrichment

## Project
SOAR Incident Containment Engine

## Week 2 Objective
Verify that automated threat enrichment correctly assigns reputation scores and risk levels to alerts, and that the system safely handles external API failures without crashing.

---

## Test Case 1: Known Bad IP Returns High Risk

### Test ID
W2-TC-001

### Objective
Verify that a known malicious IP address is classified as High Risk.

### Test Data
Source IP: 185.220.101.1 (Example malicious IP)

### Steps
1. Send an alert containing the known bad IP.
2. Allow the enrichment process to complete.
3. Check the returned enrichment data.

### Expected Result
- Reputation score indicates malicious.
- Risk Level = High
- Enrichment source is displayed.
- Alert processing completes successfully.

### Actual Result
_________________________

### Status
☐ Pass
☐ Fail

---

## Test Case 2: Known Safe IP Returns Low Risk

### Test ID
W2-TC-002

### Objective
Verify that a trusted IP address is classified as Low Risk.

### Test Data
Source IP: 8.8.8.8 (Example trusted IP)

### Steps
1. Send an alert containing the safe IP.
2. Wait for enrichment.
3. Verify returned values.

### Expected Result
- Reputation score indicates safe.
- Risk Level = Low
- Enrichment source is displayed.
- Alert is processed successfully.

### Actual Result
_________________________

### Status
☐ Pass
☐ Fail

---

## Test Case 3: External API Failure Uses Safe Fallback

### Test ID
W2-TC-003

### Objective
Verify that the application handles enrichment API failures gracefully.

### Test Data
Simulate enrichment API timeout or service unavailable.

### Steps
1. Disable or mock the enrichment API.
2. Submit a valid alert.
3. Observe application behavior.

### Expected Result
- Application does not crash.
- Alert is still accepted.
- Default (fallback) reputation score is assigned.
- Risk level is set to Unknown or Safe Fallback.
- Error is logged for troubleshooting.

### Actual Result
_________________________

### Status
☐ Pass
☐ Fail

---

# QA Checklist

| Check | Status |
|--------|--------|
| Known malicious IP returns High Risk | ☐ |
| Known safe IP returns Low Risk | ☐ |
| Reputation score is displayed | ☐ |
| Risk level is displayed | ☐ |
| Enrichment source is displayed | ☐ |
| API failure does not crash application | ☐ |
| Fallback reputation score is assigned | ☐ |
| Error is logged correctly | ☐ |

---

## QA Summary

**Tester:** Aleena

**Date:** ___________________

**Overall Result:**
☐ Pass

☐ Fail

**Comments:**

____________________________________________________

____________________________________________________
