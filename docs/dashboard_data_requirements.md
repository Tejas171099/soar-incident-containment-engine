# Dashboard Data Requirements

## Purpose

This document defines the data fields required by the SOAR Incident Containment Engine dashboard.

The dashboard requirements are updated through Week 1, Week 2, and Week 3 to reflect alert ingestion, threat enrichment, and playbook/action data.

---

## Dashboard Data Requirements Table

| Field | Description | Available From | Provider | Dashboard Use |
|---|---|---|---|---|
| alert_id | Unique identifier for the alert | Week 1 | Alert ingestion/backend | Identifies each alert |
| timestamp | Date and time when the alert was generated | Week 1 | Alert ingestion/backend | Displays alert time |
| source_ip | Source IP address associated with the alert | Week 1 | Alert ingestion/backend | Identifies the source |
| alert_type | Type/category of the security alert | Week 1 | Alert ingestion/backend | Identifies alert type |
| host | Host or system associated with the alert | Week 1 | Alert ingestion/backend | Identifies affected host |
| severity | Initial severity of the alert | Week 1 | Alert ingestion/backend | Displays initial severity |
| reputation_score | Reputation score assigned during threat enrichment | Week 2 | Rajkumar / Enrichment Engine | Shows threat reputation |
| risk_level | Risk level calculated from enrichment data | Week 2 | Rajkumar / Enrichment Engine | Displays Low, Medium, or High risk |
| enrichment_source | Source used to obtain enrichment information | Week 2 | Rajkumar / Enrichment Engine | Shows enrichment source |
| recommended_action | Recommended response based on the alert risk and playbook logic | Week 3 | Tejas / Playbook Engine | Displays the recommended security action |
| action_status | Current status of the recommended/playbook action | Week 3 | Tejas / Playbook Engine | Displays Pending, In Progress, Completed, or Failed |

---

## Week 3 Field Availability

### Week 1 – Alert Ingestion

The following fields are available from the initial alert ingestion stage:

- `alert_id`
- `timestamp`
- `source_ip`
- `alert_type`
- `host`
- `severity`

These fields represent the basic information received when an alert enters the system.

### Week 2 – Threat Enrichment

The enrichment engine adds:

- `reputation_score`
- `risk_level`
- `enrichment_source`

These fields are provided through the enrichment work handled by Rajkumar.

The `risk_level` field represents the assessed risk of the alert, such as:

- High
- Medium
- Low

### Week 3 – Playbook and Action

The playbook engine adds:

- `recommended_action`
- `action_status`

These fields are provided through the playbook implementation handled by Tejas.

The `recommended_action` field identifies the response suggested by the playbook engine.

The `action_status` field tracks the current state of the action, such as:

- Pending
- In Progress
- Completed
- Failed

---

## Week 3 Dashboard Data Flow

The expected data flow is:

```text
Alert Ingestion
      ↓
Week 1 Fields
      ↓
Threat Enrichment
      ↓
Week 2 Fields
      ↓
Risk Assessment
      ↓
Playbook Engine
      ↓
Week 3 Fields
      ↓
Dashboard
