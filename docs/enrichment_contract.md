# Threat Enrichment Contract

## Input from Rajkumar
The enrichment module will receive:
- alert_id
- timestamp
- source_ip
- alert_type
- target_host
- severity

## What the module should do
The module should check whether the source IP or other indicator looks suspicious.

## Output from Tejas module
The module should return:
- alert_id
- source_ip
- reputation_score
- risk_level
- threat_source
- recommended_action
- action_status

## Simple meaning of output fields
- reputation_score: a number showing how risky the IP is.
- risk_level: low, medium, or high.
- threat_source: where the threat info came from.
- recommended_action: what the system should do next.
- action_status: success, failed, or pending.

## Example output
```json
{
  "alert_id": "A123",
  "source_ip": "203.0.113.5",
  "reputation_score": 92,
  "risk_level": "high",
  "threat_source": "mock_threat_db",
  "recommended_action": "block_ip",
  "action_status": "pending"
}
```
