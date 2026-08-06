 branch/merin
# Week 2 End-to-End Enrichment Test

## Tested By
Merin

## Verification Summary

- Reviewed Rajkumar's threat enrichment module.
- Confirmed the AbuseIPDB API key is securely loaded using load_dotenv() and os.getenv("ABUSEIPDB_API_KEY").
- Confirmed the enrichment module returns reputation_score and source.
- Reviewed Tejas' playbook_engine.py and confirmed it generates risk_level, recommended_action, and action_status using the enrichment result.
- Confirmed the playbook processes a sample alert and includes the reputation_score in its output.
- Reviewed Aleena's dashboard requirements and confirmed the dashboard displays Reputation Score, Risk Level, Recommended Action, and Enrichment Source.

## Result

Verified the documented end-to-end Week 2 enrichment flow through GitHub code and documentation review.

# Week 2 Threat Enrichment Test Evidence

## Project

**SOAR Incident Containment Engine**

**Role:** Backend / Ingestion Developer

---

## Objective

Verify that every incoming SIEM alert is automatically normalized and passed to the threat enrichment module.

---

## Test Environment

* Operating System: Windows
* Framework: FastAPI
* API Testing: Swagger UI (`http://127.0.0.1:8000/docs`)
* Python Version: 3.x

---

## Test Case 1 – Valid Alert

### Input

```json
{
  "id": "A123",
  "time": "2026-07-21T10:00:00Z",
  "src_ip": "203.0.113.5",
  "type": "brute_force",
  "host": "web-server-01",
  "severity": "high"
}
```

### Expected Result

* Alert is received successfully.
* Alert is normalized.
* Threat enrichment function is triggered automatically.
* Enrichment data is returned in the API response.

### Actual Result

**Passed**

---

## Test Case 2 – Missing Source IP

### Input

Removed the `src_ip` field.

### Expected Result

Request validation fails and FastAPI returns **HTTP 422 Unprocessable Entity**.

### Actual Result

**Passed**

---

## Test Case 3 – Invalid Timestamp

### Input

```json
{
  "id": "A124",
  "time": "invalid-date",
  "src_ip": "8.8.8.8",
  "type": "malware",
  "host": "database-server",
  "severity": "medium"
}
```

### Expected Result

Request validation fails with **HTTP 422**.

### Actual Result

**Passed**

---

## Test Case 4 – Threat Enrichment Trigger

### Input

Valid alert containing a source IP address.

### Expected Result

The application automatically calls the `check_ip_reputation()` function after normalization and includes the enrichment result in the response.

### Actual Result

**Passed**

---

## Test Case 5 – Logging Verification

### Expected Result

Application logs record the received alert ID and source IP, and confirm that the threat lookup process was executed.

### Actual Result

**Passed**

---

## Summary

All planned Week 2 tests completed successfully.

* Alert ingestion working.
* Alert normalization working.
* Automatic enrichment trigger working.
* Input validation working.
* Application logging working.

The enrichment pipeline is ready for integration with a live threat intelligence service (such as AbuseIPDB or VirusTotal) in the next stage of development.
 main
