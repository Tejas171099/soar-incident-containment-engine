# Week 4 Integration Review

## End-to-End Field Verification

| Field | Present in ingestion | Present in enrichment | Present in playbook output | Present on dashboard | Final status |
|---|---|---|---|---|---|
| alert_id | Yes | Yes | Yes | Yes | OK / Issue |
| source_ip | Yes | Yes | Yes | Yes | OK / Issue |
| reputation_score | No | Yes | Yes | Yes | OK / Issue |
| risk_level | No | No | Yes | Yes | OK / Issue |
| recommended_action | No | No | Yes | Yes | OK / Issue |
| action_status | No | No | Yes | Yes | OK / Issue |

## Review Notes

- Verified the flow from ingestion to enrichment.
- Verified enrichment data used by the playbook.
- Verified playbook outputs used by the dashboard.
- Verified final dashboard fields.
- Any remaining mismatch is recorded as an Issue.
