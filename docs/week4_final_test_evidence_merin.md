# Week 4 Final End-to-End Test Evidence

## Test 1 – End-to-End Alert Processing

### 1. Input Alert

```json
{
  "id": "A123",
  "time": "2026-07-21T10:00:00Z",
  "src_ip": "203.0.113.5",
  "type": "brute_force",
  "host": "web-server-01",
  "severity": "high"
}

### 2. Enrichment Result

{
  "reputation_score": 92,
  "source": "AbuseIPDB"
}

### 3. Playbook Output

{
  "risk_level": "high",
  "recommended_action": "block_ip",
  "action_status": "completed"
}

### 4. Dashboard Result

The following fields were checked on the dashboard:

- alert_id
- source_ip
- reputation_score
- risk_level
- recommended_action
- action_status

### 5. Test Status

IN PROGRESS

### 6. Notes

The end-to-end test is being performed to verify the flow from alert ingestion through enrichment and playbook processing to the dashboard.
