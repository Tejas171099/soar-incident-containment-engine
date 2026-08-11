# Dashboard Integration Checklist

## Purpose

This checklist tracks the integration of Week 1, Week 2, and Week 3 backend fields with the SOAR Incident Containment Engine dashboard.

---

## Dashboard Field Integration Status

| Field | Week | Expected | Available | Status | Provider | Notes |
|---|---|---|---|---|---|---|
| alert_id | Week 1 | Yes | Yes | Ready | Alert Ingestion / Backend | Required for identifying each alert |
| timestamp | Week 1 | Yes | Yes | Ready | Alert Ingestion / Backend | Required for displaying alert time |
| source_ip | Week 1 | Yes | Yes | Ready | Alert Ingestion / Backend | Required for identifying source |
| alert_type | Week 1 | Yes | Yes | Ready | Alert Ingestion / Backend | Required for identifying alert category |
| host | Week 1 | Yes | Yes | Ready | Alert Ingestion / Backend | Required for identifying affected host |
| severity | Week 1 | Yes | Yes | Ready | Alert Ingestion / Backend | Initial alert severity |
| reputation_score | Week 2 | Yes | Yes | Ready | Rajkumar / Enrichment Engine | Provided by threat enrichment |
| risk_level | Week 2 | Yes | Yes | Ready | Rajkumar / Enrichment Engine | Displays Low, Medium, or High risk |
| enrichment_source | Week 2 | Yes | Yes | Ready | Rajkumar / Enrichment Engine | Identifies enrichment source |
| recommended_action | Week 3 | Yes | Yes | Ready | Tejas / Playbook Engine | Recommended response from playbook |
| action_status | Week 3 | Yes | Yes | Ready | Tejas / Playbook Engine | Tracks current action status |

---

## Week 3 Integration Checklist

### Risk Level

- [x] `risk_level` field is expected.
- [x] `risk_level` is available from the enrichment engine.
- [x] Dashboard displays the risk level.
- [x] High, Medium, and Low risk levels have visual indicators.
- [x] Field is provided by Rajkumar's enrichment implementation.

### Reputation Score

- [x] `reputation_score` field is expected.
- [x] `reputation_score` is available from the enrichment engine.
- [x] Dashboard displays the reputation score.
- [x] Field is provided by Rajkumar's enrichment implementation.

### Recommended Action

- [x] `recommended_action` field is expected.
- [x] `recommended_action` is available from the playbook engine.
- [x] Dashboard displays the recommended action.
- [x] Field is provided by Tejas's playbook implementation.

### Action Status

- [x] `action_status` field is expected.
- [x] `action_status` is available from the playbook engine.
- [x] Dashboard displays the current action status.
- [x] Field is provided by Tejas's playbook implementation.

---

## Backend Availability Check

Before marking a field as `Available = Yes`, confirm that the field is actually present in the backend alert response.

Expected Week 2 fields:

```text
reputation_score
risk_level
enrichment_source
