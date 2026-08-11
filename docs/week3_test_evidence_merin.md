# Week 3 Test Evidence – Merin

## 1. Test Objective

The objective of this test was to verify that a sample SIEM alert can be received by the SOAR ingestion service through the API.

## 2. Test Environment

- Branch: branch/merin
- API: FastAPI
- Server: Uvicorn
- Endpoint: POST /alerts
- Local URL: http://127.0.0.1:8000

## 3. Test Alert Payload

```json
{
  "id": "TEST-W3-001",
  "time": "2026-08-11T10:00:00",
  "src_ip": "8.8.8.8",
  "type": "suspicious_login",
  "host": "test-host",
  "severity": "high"
}
