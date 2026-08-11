# Week 3 QA Scenarios – Dashboard

## Project
SOAR Incident Containment Engine

## Role
Dashboard / QA / Documentation

## Objective

The purpose of these QA scenarios is to verify that the dashboard correctly displays
threat enrichment and playbook information for different alert types and risk levels.

The following Week 2 and Week 3 fields are validated:

- reputation_score
- risk_level
- recommended_action
- action_status

---

## Scenario 1 – High-Risk Brute Force Alert

### Test ID
W3-QA-001

### Input

```text
Alert Type: brute_force
Reputation Score: 90
Severity: High
Source IP: 192.168.1.100
