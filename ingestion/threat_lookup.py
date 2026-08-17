"""
Threat intelligence lookup module.

This module queries AbuseIPDB for IP reputation information.

Week 4 requirements:
- Handle missing API key safely.
- Handle timeout errors.
- Handle network errors.
- Handle HTTP errors.
- Handle malformed/unexpected provider responses.
- Never allow enrichment failure to crash the FastAPI service.
- Return safe defaults when enrichment fails.
"""

import logging
import os
from typing import Any, Dict

import requests


# Use the same logger configured by ingestion/logger.py
logger = logging.getLogger("soar")


ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip_reputation(ip: str) -> Dict[str, Any]:
    """
    Check an IP address against AbuseIPDB.

    Returns a dictionary containing enrichment information.

    Successful lookup example:

    {
        "ip": "8.8.8.8",
        "reputation_score": 0,
        "source": "AbuseIPDB",
        "country": "US",
        "isp": "Google LLC",
        "asn": "15169"
    }

    Failure example:

    {
        "ip": "8.8.8.8",
        "reputation_score": 0,
        "source": "lookup_failed",
        "reason": "missing_api_key"
    }
    """

    # ---------------------------------------------------------
    # 1. Read API key from environment
    # ---------------------------------------------------------
    api_key = os.getenv("ABUSEIPDB_API_KEY")

    if not api_key:
        logger.error(
            "ENRICHMENT_FAILURE ip=%s reason=missing_api_key",
            ip,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "missing_api_key",
        }

    # ---------------------------------------------------------
    # 2. Prepare AbuseIPDB request
    # ---------------------------------------------------------
    headers = {
        "Accept": "application/json",
        "Key": api_key,
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
    }

    logger.info(
        "ENRICHMENT_START ip=%s provider=AbuseIPDB",
        ip,
    )

    # ---------------------------------------------------------
    # 3. Perform external API request
    # ---------------------------------------------------------
    try:
        response = requests.get(
            ABUSEIPDB_URL,
            headers=headers,
            params=params,
            timeout=5,
        )

        # -----------------------------------------------------
        # 4. Handle bad HTTP status codes
        # -----------------------------------------------------
        response.raise_for_status()

        # -----------------------------------------------------
        # 5. Parse JSON response
        # -----------------------------------------------------
        data = response.json()

    except requests.exceptions.Timeout:
        logger.error(
            "ENRICHMENT_FAILURE ip=%s reason=timeout",
            ip,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "timeout",
        }

    except requests.exceptions.ConnectionError:
        logger.error(
            "ENRICHMENT_FAILURE ip=%s reason=network_error",
            ip,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "network_error",
        }

    except requests.exceptions.HTTPError as exc:
        logger.error(
            "ENRICHMENT_FAILURE ip=%s reason=http_error error=%s",
            ip,
            exc,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "http_error",
        }

    except ValueError:
        logger.error(
            "ENRICHMENT_FAILURE ip=%s reason=invalid_json",
            ip,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "invalid_json",
        }

    except requests.exceptions.RequestException as exc:
        logger.error(
            "ENRICHMENT_FAILURE ip=%s reason=request_error error=%s",
            ip,
            exc,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "request_error",
        }

    except Exception as exc:
        logger.exception(
            "ENRICHMENT_FAILURE ip=%s reason=unexpected_error error=%s",
            ip,
            exc,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "unexpected_error",
        }

    # ---------------------------------------------------------
    # 6. Extract AbuseIPDB data safely
    # ---------------------------------------------------------
    try:
        data_section = data.get("data", {})

        if not isinstance(data_section, dict):
            raise ValueError("Invalid AbuseIPDB data structure")

        abuse_score = data_section.get(
            "abuseConfidenceScore",
            0,
        )

        country_code = data_section.get(
            "countryCode"
        )

        isp = data_section.get(
            "isp"
        )

        asn = data_section.get(
            "asn"
        )

        # -----------------------------------------------------
        # 7. Build successful enrichment result
        # -----------------------------------------------------
        result = {
            "ip": ip,
            "reputation_score": abuse_score,
            "source": "AbuseIPDB",
            "country": country_code or "Unknown",
            "isp": isp or "Unknown",
            "asn": str(asn) if asn else "Unknown",
        }

        logger.info(
            "ENRICHMENT_SUCCESS ip=%s reputation_score=%s",
            ip,
            abuse_score,
        )

        return result

    except Exception as exc:
        logger.exception(
            "ENRICHMENT_FAILURE ip=%s reason=response_parsing_error error=%s",
            ip,
            exc,
        )

        return {
            "ip": ip,
            "reputation_score": 0,
            "source": "lookup_failed",
            "reason": "response_parsing_error",
        }
