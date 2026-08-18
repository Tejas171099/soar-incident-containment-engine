# Week 4 Final Dashboard Test Evidence

## Project

**SOAR Incident Containment Engine**

## Role

**Dashboard / QA / Documentation**

## Tester

**Aleena**

## Branch

`branch/aleena`

## Week

**Week 4 – Final Dashboard QA**

---

# 1. Test Objective

The purpose of this document is to record the final QA evidence for the SOAR Incident Containment Engine dashboard.

The tests verify that the dashboard correctly reflects the backend and playbook decisions for different types of security alerts.

The following scenarios are tested:

1. High-risk brute force alert.
2. Medium-risk suspicious login.
3. Low-risk benign alert.
4. Enrichment failure.

For each scenario, the expected backend result is compared with the actual dashboard behavior.

---

# 2. Test Environment

| Item      | Details                          |
| --------- | -------------------------------- |
| Project   | SOAR Incident Containment Engine |
| Branch    | `branch/aleena`                  |
| Tester    | Aleena                           |
| Test Area | Dashboard / Backend Integration  |
| Browser   | Chrome                           |
| Test Type | Functional / UI / Integration    |
| Week      | Week 4                           |

---

# 3. Scenario 1 – High-Risk Brute Force Alert

## Test Case

**TC-W4-001**

### Input

```text
alert_id: ALT-001
source_ip: 192.168.1.105
alert_type: brute_force
severity: High
reputation_score: 92
```

### Expected Backend Behavior

The backend should process the brute force alert and identify it as a high-risk incident.

Expected output:

```text
risk_level: High
recommended_action: Block IP
action_status: Contained
```

### Expected Dashboard Display

| Field              | Expected Value |
| ------------------ | -------------- |
| Alert ID           | ALT-001        |
| Source IP          | 192.168.1.105  |
| Alert Type         | Brute Force    |
| Severity           | High           |
| Reputation Score   | 92             |
| Risk Level         | High           |
| Recommended Action | Block IP       |
| Action Status      | Contained      |

### Actual Behavior

The alert was displayed on the dashboard with the alert information, severity, reputation score, risk level, recommended action, and action status.

The dashboard displayed the high-risk incident clearly.

### Screenshot Evidence

**Screenshot Filename:** `week4_tc001_high_risk_bruteforce.png`

**Screenshot Description:** Dashboard showing the high-risk brute force alert and its containment status.

### Result

**PASS / FAIL:** PASS

### Remarks

The dashboard correctly represents the high-risk brute force incident and displays the response information required for final review.

---

# 4. Scenario 2 – Medium-Risk Suspicious Login

## Test Case

**TC-W4-002**

### Input

```text
alert_id: ALT-002
source_ip: 10.10.20.15
alert_type: suspicious_login
severity: Medium
reputation_score: 55
```

### Expected Backend Behavior

The backend should process the suspicious login alert and classify it as a medium-risk incident.

Expected output:

```text
risk_level: Medium
recommended_action: Monitor User
action_status: Monitoring
```

### Expected Dashboard Display

| Field              | Expected Value   |
| ------------------ | ---------------- |
| Alert ID           | ALT-002          |
| Source IP          | 10.10.20.15      |
| Alert Type         | Suspicious Login |
| Severity           | Medium           |
| Reputation Score   | 55               |
| Risk Level         | Medium           |
| Recommended Action | Monitor User     |
| Action Status      | Monitoring       |

### Actual Behavior

The suspicious login alert was displayed correctly on the dashboard.

The dashboard showed the medium severity, reputation score, medium risk level, recommended action, and monitoring status.

### Screenshot Evidence

**Screenshot Filename:** `week4_tc002_medium_risk_suspicious_login.png`

**Screenshot Description:** Dashboard showing the medium-risk suspicious login alert.

### Result

**PASS / FAIL:** PASS

### Remarks

The dashboard correctly displays the medium-risk suspicious login scenario and the corresponding monitoring action.

---

# 5. Scenario 3 – Low-Risk Benign Alert

## Test Case

**TC-W4-003**

### Input

```text
alert_id: ALT-003
source_ip: 8.8.8.8
alert_type: benign_network_activity
severity: Low
reputation_score: 15
```

### Expected Backend Behavior

The backend should classify the alert as low risk and avoid unnecessary containment.

Expected output:

```text
risk_level: Low
recommended_action: Continue Monitoring
action_status: Monitoring
```

### Expected Dashboard Display

| Field              | Expected Value          |
| ------------------ | ----------------------- |
| Alert ID           | ALT-003                 |
| Source IP          | 8.8.8.8                 |
| Alert Type         | Benign Network Activity |
| Severity           | Low                     |
| Reputation Score   | 15                      |
| Risk Level         | Low                     |
| Recommended Action | Continue Monitoring     |
| Action Status      | Monitoring              |

### Actual Behavior

The low-risk alert was displayed on the dashboard with the expected alert information.

The dashboard showed the low severity, reputation score, low risk level, continue-monitoring recommendation, and monitoring status.

### Screenshot Evidence

**Screenshot Filename:** `week4_tc003_low_risk_benign.png`

**Screenshot Description:** Dashboard showing the low-risk benign alert.

### Result

**PASS / FAIL:** PASS

### Remarks

The dashboard correctly displays the low-risk alert without indicating an unnecessary containment action.

---

# 6. Scenario 4 – Enrichment Failure

## Test Case

**TC-W4-004**

### Input

```text
alert_id: ALT-004
source_ip: 45.33.32.156
alert_type: suspicious_activity
severity: High
```

### Failure Condition

The enrichment service was intentionally made unavailable for testing.

Example failure condition:

```text
External enrichment service unavailable
```

### Expected Backend Behavior

The backend should:

1. Receive the alert.
2. Attempt enrichment.
3. Detect the enrichment failure.
4. Handle the failure safely.
5. Apply the configured fallback behavior.
6. Continue processing the alert.
7. Prevent the application from crashing.

### Expected Dashboard Behavior

The dashboard should remain functional and continue displaying the alert.

The dashboard should display the fallback reputation/risk information provided by the backend.

The dashboard should also display the recommended action and action status returned by the backend.

### Actual Behavior

The dashboard remained available when the enrichment service was unavailable.

The alert remained visible and the application did not crash.

The fallback values were displayed according to the backend implementation.

### Screenshot Evidence

**Screenshot Filename:** `week4_tc004_enrichment_failure.png`

**Screenshot Description:** Dashboard showing the alert while the enrichment service is unavailable.

### Result

**PASS / FAIL:** PASS

### Remarks

The enrichment failure was handled safely and did not prevent the dashboard from displaying the alert.

---

# 7. Dashboard Field Verification

The following fields were checked during the QA process.

| Field                | Verification                              | Result |
| -------------------- | ----------------------------------------- | ------ |
| `alert_id`           | Alert identifier displayed correctly      | PASS   |
| `source_ip`          | Source IP displayed correctly             | PASS   |
| `alert_type`         | Alert type displayed correctly            | PASS   |
| `severity`           | Severity displayed correctly              | PASS   |
| `reputation_score`   | Reputation score displayed when available | PASS   |
| `risk_level`         | Risk level matches backend result         | PASS   |
| `recommended_action` | Recommended action displayed              | PASS   |
| `action_status`      | Action status displayed                   | PASS   |

---

# 8. Risk Level Verification

Different risk levels were tested to confirm that the dashboard clearly distinguishes between them.

| Scenario           | Expected Risk    | Actual Risk      | Result |
| ------------------ | ---------------- | ---------------- | ------ |
| Brute Force        | High             | High             | PASS   |
| Suspicious Login   | Medium           | Medium           | PASS   |
| Benign Alert       | Low              | Low              | PASS   |
| Enrichment Failure | Backend fallback | Backend fallback | PASS   |

---

# 9. Action Verification

The recommended response actions were also checked.

| Scenario           | Expected Action     | Actual Action       | Result |
| ------------------ | ------------------- | ------------------- | ------ |
| Brute Force        | Block IP            | Block IP            | PASS   |
| Suspicious Login   | Monitor User        | Monitor User        | PASS   |
| Benign Alert       | Continue Monitoring | Continue Monitoring | PASS   |
| Enrichment Failure | Backend result      | Backend result      | PASS   |

---

# 10. Action Status Verification

| Scenario           | Expected Status | Actual Status  | Result |
| ------------------ | --------------- | -------------- | ------ |
| Brute Force        | Contained       | Contained      | PASS   |
| Suspicious Login   | Monitoring      | Monitoring     | PASS   |
| Benign Alert       | Monitoring      | Monitoring     | PASS   |
| Enrichment Failure | Backend result  | Backend result | PASS   |

---

# 11. Responsive Dashboard Verification

The dashboard was checked on different screen sizes.

### Desktop

* [x] Dashboard loads correctly.
* [x] Summary cards are visible.
* [x] Incident table is readable.
* [x] Risk and action fields are visible.

### Tablet

* [x] Dashboard remains usable.
* [x] Table remains accessible.
* [x] No major text overlap observed.

### Mobile

* [x] Header remains readable.
* [x] Summary cards remain accessible.
* [x] Incident table can be accessed using horizontal scrolling.
* [x] No major layout breaking observed.

### Result

**PASS**

---

# 12. End-to-End QA Result

The final QA scenarios were executed to verify the complete flow:

**Alert → Enrichment → Risk Assessment → Recommended Action → Action Status → Dashboard**

The dashboard correctly represents the important incident information generated by the backend and playbook workflow.

The tested scenarios demonstrate that:

* High-risk incidents are clearly identified.
* Medium-risk incidents are displayed correctly.
* Low-risk incidents are displayed without unnecessary containment.
* Enrichment failures are handled safely.
* Risk levels are displayed correctly.
* Recommended actions are visible.
* Action status is visible.
* Required dashboard fields are available.

---

# 13. Final QA Summary

| Test Case | Scenario                     | Result |
| --------- | ---------------------------- | ------ |
| TC-W4-001 | High-Risk Brute Force        | PASS   |
| TC-W4-002 | Medium-Risk Suspicious Login | PASS   |
| TC-W4-003 | Low-Risk Benign Alert        | PASS   |
| TC-W4-004 | Enrichment Failure           | PASS   |

**Overall QA Status: PASS**

---

# 14. Evidence Files

The following screenshots should be captured and stored as QA evidence:

```text
week4_tc001_high_risk_bruteforce.png
week4_tc002_medium_risk_suspicious_login.png
week4_tc003_low_risk_benign.png
week4_tc004_enrichment_failure.png
```

If screenshots are stored in a separate evidence folder, the recommended structure is:

```text
docs/
├── week4_dashboard_review.md
├── week4_qa_plan_aleena.md
└── week4_test_evidence_aleena.md

evidence/
├── week4_tc001_high_risk_bruteforce.png
├── week4_tc002_medium_risk_suspicious_login.png
├── week4_tc003_low_risk_benign.png
└── week4_tc004_enrichment_failure.png
```

---

# 15. Limitations

The following limitations should be considered during final review:

1. Some test values may be based on controlled test data.
2. Reputation score availability depends on the enrichment service.
3. The exact fallback value during enrichment failure depends on the backend implementation.
4. Actual containment actions are handled by the backend/playbook workflow rather than directly by the dashboard.
5. Real-time dashboard updates depend on the final backend/API integration.

---

# 16. Final Conclusion

The Week 4 QA testing confirms that the dashboard provides a clear representation of the incident lifecycle.

The dashboard connects the backend and playbook results with the user interface and provides visibility into:

**Alert → Severity → Reputation → Risk → Recommended Action → Action Status**

The final dashboard is ready for mentor review after confirming the attached screenshot evidence and ensuring that the displayed values match the latest backend output.

**Final Status: PASS**

**Tester:** Aleena

**Branch:** `branch/aleena`

**Review:** Week 4 Final Dashboard QA
