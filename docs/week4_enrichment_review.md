# Week 4 Enrichment API Review

## Overview

This document provides the Week 4 review of the Enrichment API for the SOAR Incident Containment Engine.

The primary objective of Week 4 was to harden and finalize the enrichment API so that it remains stable when the external Threat Intelligence provider is unavailable, times out, returns an HTTP error, or cannot be queried successfully.

The API was developed using FastAPI and is responsible for receiving SIEM alerts, validating and normalizing the alert data, performing threat intelligence enrichment, and returning a consistent response to downstream SOAR components.

Weeks 1–3 established the alert ingestion, validation, normalization, and threat enrichment functionality. Week 4 focused on reliability, error handling, safe fallback behavior, logging, and final API verification.

## Role and Scope

**Role:** Backend / Ingestion Developer

**Primary responsibility:**

* Receive incoming SIEM alerts through the FastAPI endpoint.
* Validate the incoming alert structure.
* Normalize alert fields into a common format.
* Perform IP reputation enrichment.
* Handle external Threat Intelligence provider failures safely.
* Return a predictable response format.
* Provide useful logging for troubleshooting and monitoring.
* Verify the API behavior under both successful and failure conditions.

The scope of this work is limited to the ingestion and enrichment API. Automated IP blocking, firewall actions, SOAR playbooks, and dashboard functionality are outside the scope of this component.

## API Endpoint

The primary endpoint is:

```text
POST /alerts
```

The endpoint accepts a SIEM alert as JSON and processes it through the following flow:

```text
SIEM Alert
    |
    v
FastAPI /alerts
    |
    v
Validation
    |
    v
Alert Normalization
    |
    v
Threat Intelligence Enrichment
    |
    v
Error Handling / Safe Fallback
    |
    v
Normalized + Enriched Response
```

The endpoint is designed to return a successful response even when the external enrichment provider cannot be reached. In such cases, the API uses a safe fallback instead of crashing or returning an unusable response.

## Normalized Alert Fields

The incoming alert is converted into a consistent structure.

The normalized alert contains the following fields:

* `alert_id`
* `timestamp`
* `source_ip`
* `alert_type`
* `target_host`
* `severity`

Normalization ensures that downstream SOAR components receive predictable field names regardless of the original SIEM alert representation.

Example:

```json
{
  "alert_id": "ALERT-001",
  "timestamp": "2026-07-29T10:30:00",
  "source_ip": "8.8.8.8",
  "alert_type": "Malware",
  "target_host": "DESKTOP-01",
  "severity": "High"
}
```

## Enrichment Fields

The enrichment stage performs an IP reputation lookup using the configured Threat Intelligence provider.

The response contains enrichment information such as:

* `ip`
* `reputation_score`
* `risk_level`
* `recommended_action`
* `source`

The enrichment response provides downstream components with a consistent representation of the reputation result.

Example:

```json
{
  "ip": "8.8.8.8",
  "reputation_score": 0,
  "risk_level": "Low",
  "recommended_action": "Monitor",
  "source": "AbuseIPDB"
}
```

The exact reputation score and risk classification depend on the information returned by the external provider.

## Threat Intelligence Provider

The enrichment API uses AbuseIPDB for IP reputation lookups.

The API is designed so that provider credentials are not hard-coded into the source code. Credentials are supplied through environment variables.

This approach prevents sensitive API credentials from being committed to the repository and makes the application easier to configure across development and testing environments.

The external provider request also uses a timeout so that the API does not remain blocked indefinitely when the provider is slow or unreachable.

## Error Handling

Week 4 introduced stronger handling for external enrichment failures.

The API handles conditions such as:

* Threat Intelligence provider timeout.
* HTTP errors returned by the provider.
* Provider connection failures.
* Unexpected exceptions during the lookup.
* Missing or unavailable enrichment results.

The API should not terminate or crash because an external enrichment service is temporarily unavailable.

Instead, the failure is logged and a safe enrichment response is returned.

This allows the SOAR pipeline to continue processing the alert while clearly indicating that enrichment was not successfully completed.

## Safe Defaults

When the Threat Intelligence lookup fails, the API uses a safe fallback instead of treating the alert as malicious based on missing information.

The fallback includes:

```json
{
  "reputation_score": 0,
  "source": "lookup_failed"
}
```

An optional `reason` field can also be included to provide additional information about the failure.

The safe fallback prevents an unavailable Threat Intelligence service from causing the entire ingestion process to fail.

The fallback value must not be interpreted as proof that the IP is safe. It indicates that a reputation result could not be obtained.

## Logging and Observability

Logging was reviewed and strengthened as part of the Week 4 hardening work.

Important events are logged, including:

* Incoming alert processing.
* Alert normalization.
* Threat intelligence lookup attempts.
* Successful enrichment.
* Provider timeout conditions.
* Provider HTTP errors.
* Provider lookup failures.
* Unexpected enrichment exceptions.

Logs provide sufficient information to identify where processing failed without exposing sensitive credentials.

API keys and other secrets must not be written to application logs.

## Limitations and Assumptions

The current enrichment implementation depends on the availability of the external AbuseIPDB service.

The following limitations apply:

1. Threat intelligence results depend on the external provider.
2. Provider API limits may affect the number of enrichment requests.
3. A failed lookup does not indicate that an IP is safe.
4. The current implementation performs IP-based reputation enrichment.
5. Automated containment actions are handled outside this API.
6. API credentials must be configured through environment variables.
7. Network connectivity is required for live AbuseIPDB enrichment.

The API is therefore designed to fail safely when external enrichment is unavailable rather than allowing the failure to stop alert ingestion.

## Week 4 Completion Summary

Week 4 focused on finalizing and hardening the Enrichment API.

The following areas were completed:

* FastAPI enrichment endpoint reviewed and stabilized.
* Incoming alert validation and normalization verified.
* Threat intelligence enrichment verified.
* External provider timeout handling implemented.
* External provider HTTP error handling implemented.
* Exception handling reviewed.
* Safe fallback enrichment response implemented.
* Logging and observability reviewed.
* API credentials kept outside source code through environment configuration.
* Successful enrichment behavior tested.
* Safe IP behavior tested.
* Threat Intelligence provider failure behavior tested.
* Final API response structure reviewed.

The Enrichment API is now suitable for integration with the downstream SOAR workflow because it provides a predictable response even when the external Threat Intelligence service experiences a failure.
