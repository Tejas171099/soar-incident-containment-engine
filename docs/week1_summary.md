# Week 1 Summary

## Team Member

Rajkumar

Role: Backend / Ingestion Developer

---

## Objectives Completed

- Created FastAPI application.
- Implemented POST /alerts endpoint.
- Added request validation using Pydantic.
- Developed alert normalization module.
- Configured application logging.
- Integrated AbuseIPDB threat intelligence lookup.
- Tested API using Swagger UI.

---

## Files Implemented

- ingestion/main.py
- ingestion/normalizer.py
- ingestion/logger.py
- ingestion/threat_lookup.py
- ingestion/merge_alert.py

---

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Requests
- python-dotenv
- AbuseIPDB API

---

## Outcome

The ingestion service successfully receives SIEM alerts, validates the payload, normalizes alert fields, enriches the source IP using AbuseIPDB, and returns a structured JSON response for downstream SOAR processing.
