# Week 2 API Key Security Verification

## Verified By
Merin

## Module
Threat Enrichment (Rajkumar)

## Verification Result

- Verified that the AbuseIPDB API key is loaded securely using os.getenv("ABUSEIPDB_API_KEY") after loading environment variables with load_dotenv().
- The API key is not hardcoded in the source code.
- The application checks whether the API key exists before use.

## Status

API key handling verified and confirmed secure for Week 2.
