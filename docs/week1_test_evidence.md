# Week 1 Test Evidence — Tejas (Threat Intelligence / Playbook Module)

## Test 1: Mock enrichment with known bad IP

### Date
2026-07-30

### Tester
Tejas

### Purpose
To verify that the mock enrichment function correctly identifies a high-risk IP and the playbook engine chooses the correct action.

### Input
```json
{
  "id": "A123",
  "source_ip": "203.0.113.5",
  "type": "brute_force",
  "host": "web-server-01",
  "severity": "high"
}
```

### Code path tested
enrichment.py -> scoring.py -> actions.py -> playbook_engine.py (process_alert)

### Expected result
- reputation_score: 92
- risk_level: high
- recommended_action: block_ip

### Actual result
- reputation_score: 92
- risk_level: high
- recommended_action: block_ip

### Status
PASS

---

## Test 2: Mock enrichment with known safe IP

### Date
2026-07-30

### Tester
Tejas

### Purpose
To verify that a safe/low-risk IP does not trigger an unnecessary containment action.

### Input
```json
{
  "id": "A124",
  "source_ip": "8.8.8.8",
  "type": "info",
  "host": "server-02",
  "severity": "low"
}
```

### Expected result
- reputation_score: 0
- risk_level: low
- recommended_action: no_action

### Actual result
- reputation_score: 0
- risk_level: low
- recommended_action: no_action

### Status
PASS

---

## Test 3: Unknown IP not in mock database

### Date
2026-07-30

### Tester
Tejas

### Purpose
To verify the fallback score behaves reasonably for an IP not present in the mock database.

### Input
```json
{
  "id": "A125",
  "source_ip": "192.0.2.99",
  "type": "unknown",
  "host": "server-03",
  "severity": "medium"
}
```

### Expected result
- reputation_score: 10 (default fallback)
- risk_level: low

### Actual result
- reputation_score: 10
- risk_level: low

### Status
PASS

---

## Summary

All three mock enrichment and playbook decision test cases passed successfully. The module correctly classifies risk level and selects the appropriate action based on the reputation score. This confirms the Week 1 mock logic is stable and ready to be replaced with real enrichment data (AbuseIPDB/VirusTotal) in Week 2.

## Pending for Week 2
- Replace mock enrichment with real API-based enrichment (from Rajkumar's ingestion module).
- Re-verify risk thresholds against real reputation score ranges.
- Add more playbook action types (isolate_host, escalate_to_analyst).
