# Week 1 Test Evidence

*Date:* 25-07-2026

*Test:* POST /alerts

## Payload Used

json
{
  "id": "ALERT-001",
  "time": "2026-07-25T12:00:00Z",
  "src_ip": "192.168.1.100",
  "type": "Malware",
  "host": "PC-01",
  "severity": "High"
}


## Expected Result

- HTTP Status Code: 200
- Alert should be received successfully.

## Actual Result

- HTTP Status Code: 200

json
{
  "status": "received",
  "alert_id": "ALERT-001",
  "message": "Alert received successfully"
}


## Test Status

*PASS ✅*