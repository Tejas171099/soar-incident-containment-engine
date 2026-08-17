# Week 4 Final Test Evidence – Merin

## 1. Ingestion Result

The alert was successfully received and normalized through the /alerts endpoint.

Test alert:

json
{
  "id": "ALERT-001",
  "time": "2026-07-25T12:00:00Z",
  "src_ip": "192.168.1.100",
  "type": "Malware",
  "host": "PC-01",
  "severity": "High"
}


API response:

- HTTP Status: 200
- Status: received
- Alert ID: ALERT-001
- Source IP: 192.168.1.100
- Alert Type: Malware
- Target Host: PC-01
- Severity: High
- Message: Alert normalized successfully

This confirms successful alert ingestion and normalization.

<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/dd639613-bdbb-44bb-9d25-bb36009c59f4" />

## 2. Enrichment Result

json
{
  "reputation_score": 92,
  "source": "AbuseIPDB"
}


The alert was successfully enriched using AbuseIPDB.

## 3. Playbook Output

json
{
  "risk_level": "high",
  "recommended_action": "block_ip",
  "action_status": "completed"
}


The playbook successfully processed the enriched alert and generated the recommended action.

## 4. Dashboard Result

The following fields were checked on the dashboard:

- alert_id
- source_ip
- reputation_score
- risk_level
- recommended_action
- action_status

All required final fields were verified on the dashboard.

## 5. Final Test Status

PASS

## 6. Conclusion

The end-to-end flow was verified from alert ingestion through enrichment and playbook processing to the final dashboard output.

The final test confirmed that the required alert data and processing results were successfully passed through the system.
