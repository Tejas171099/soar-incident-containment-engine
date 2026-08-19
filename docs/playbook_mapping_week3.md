# Week 3 Playbook Mapping – Tejas

## Purpose

This document maps supported alert types to their expected inputs, risk logic, and recommended response actions.

The playbook engine supports multiple alert types and uses the threat enrichment reputation score to determine the risk level and recommended action.

---

## 1. Brute Force

### Alert Type
`brute_force`

### Required Inputs
- `alert_id`
- `source_ip`
- `alert_type`
- `reputation_score`
- `source`

### Risk Logic
- Score >= 80 → High risk
- Score 40–79 → Medium risk
- Score < 40 → Low risk

### Action
- High risk → `block_ip`
- Medium risk → `manual_review`
- Low risk → `no_action`

### Notes
High-risk brute-force alerts may indicate a malicious source IP and should be escalated through the containment workflow.

---

## 2. Malware Detection

### Alert Type
`malware_detection`

### Required Inputs
- `alert_id`
- `source_ip`
- `alert_type`
- `reputation_score`
- `source`

### Risk Logic
- Score >= 80 → High risk
- Score 40–79 → Medium risk
- Score < 40 → Low risk

### Action
- High risk → `isolate_host`
- Medium risk → `manual_review`
- Low risk → `no_action`

### Notes
High-risk malware detection results in host isolation rather than only blocking the source IP.

---

## 3. Suspicious Login

### Alert Type
`suspicious_login`

### Required Inputs
- `alert_id`
- `source_ip`
- `alert_type`
- `reputation_score`
- `source`

### Risk Logic
- Score >= 80 → High risk
- Score 40–79 → Medium risk
- Score < 40 → Low risk

### Action
- High risk → `manual_review`
- Medium risk → `manual_review`
- Low risk → `no_action`

### Notes
Suspicious login alerts are reviewed by an analyst rather than automatically blocked when they are high risk.

---

## 4. Enrichment Failure

### Condition
Threat intelligence enrichment fails and the alert contains:

`source = lookup_failed`

### Risk Logic
The system does not assign a normal high/medium/low risk level when enrichment data is unavailable.

### Action
`manual_review`

### Action Status
`pending`

### Notes
The system follows a safe-by-default approach and does not perform an aggressive automated action when threat intelligence data is unavailable.

---

## 5. Missing Required Fields

The playbook engine should safely handle alerts where required fields such as:

- `source_ip`
- `alert_type`

are missing.

Such alerts should not result in an aggressive automated containment action.

### Recommended Action

`manual_review`

### Reason

Missing required alert information prevents the playbook engine from making a reliable automated decision.
