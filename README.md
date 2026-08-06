# SOAR Incident Containment Engine

## Project Overview

This project is an automated SOAR (Security Orchestration, Automation, and Response) system that receives SIEM alerts, enriches threat information, selects the appropriate response playbook, logs the actions taken, and displays incident information through a dashboard.

## Objectives

- Receive alerts from SIEM platforms
- Enrich alerts with additional threat information
- Automatically select response playbooks
- Log response actions and results
- Display incidents and actions on a dashboard

## Team Roles

| Member | Responsibility |
|----------|----------------|
| Mariya Merin | Project Structure & Documentation |
| Rajkumar | Alert Ingestion Module |
| Tejas | Playbook Development |
| Aleena | Dashboard Development |

## Project Structure

- ingestion/ - Alert collection and processing
- playbooks/ - Incident response playbooks
- dashboard/ - Dashboard and visualization
- docs/ - Project documentation
- tests/ - Test files

## Workflow

1. Receive SIEM Alert
2. Enrich Alert Data
3. Select Appropriate Playbook
4. Execute Response Action
5. Log Results
6. Display Results on Dashboard

## Technologies

- Python
- FastAPI
- Requests
- Pydantic
- Pytest
