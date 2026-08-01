# Week 2 API Key Security Verification

## Verified By
Merin

## Module
Threat Enrichment (Rajkumar)

## Verification Result

- Verified that the AbuseIPDB API key is loaded using an environment variable.
- The code uses os.getenv("ABUSEIPDB_API_KEY").
- The API key is not hardcoded in the source code.
- The application checks whether the API key exists before use.

## Status

API key handling verified and confirmed secure for Week 2.
