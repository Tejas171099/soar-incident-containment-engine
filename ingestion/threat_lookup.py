import os
import logging
import requests


logger = logging.getLogger(__name__)

ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"

ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")


def check_ip_reputation(ip: str) -> dict:
    """
    Look up IP reputation from AbuseIPDB.

    The function always returns a dictionary containing:
    - reputation_score
    - source

    If the external lookup fails, safe default values are returned.
    """

    # Safe default result
    safe_result = {
        "ip": ip,
        "reputation_score": 0,
        "source": "lookup_failed",
        "country": "Unknown",
        "isp": "Unknown",
        "asn": "Unknown"
    }

    # Check API key before making the request
    if not ABUSEIPDB_API_KEY:
        logger.warning(
            "AbuseIPDB API key is not configured"
        )
        return safe_result

    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:

        # 1. External API request with timeout
        response = requests.get(
            ABUSEIPDB_URL,
            headers=headers,
            params=params,
            timeout=5
        )

        # 2. Check HTTP status
        if response.status_code != 200:

            logger.warning(
                "Enrichment failed for IP %s: HTTP status %s",
                ip,
                response.status_code
            )

            return safe_result

        # 3. Parse JSON safely
        data = response.json()

        abuse_data = data.get("data", {})

        score = abuse_data.get(
            "abuseConfidenceScore",
            0
        )

        country = abuse_data.get(
            "countryCode",
            "Unknown"
        )

        isp = abuse_data.get(
            "isp",
            "Unknown"
        )

        asn = abuse_data.get(
            "asn",
            "Unknown"
        )

        logger.info(
            "Enrichment completed for IP %s with score %s",
            ip,
            score
        )

        return {
            "ip": ip,
            "reputation_score": int(score),
            "source": "abuseipdb",
            "country": country,
            "isp": isp,
            "asn": asn
        }

    # 4. Timeout handling
    except requests.Timeout:

        logger.error(
            "Enrichment timeout for IP %s",
            ip
        )

        return safe_result

    # 5. Other network errors
    except requests.RequestException as e:

        logger.error(
            "Network error during enrichment for IP %s: %s",
            ip,
            e
        )

        return safe_result

    # 6. JSON parsing errors
    except ValueError as e:

        logger.error(
            "JSON parse error during enrichment for IP %s: %s",
            ip,
            e
        )

        return safe_result

    # 7. Any unexpected error
    except Exception as e:

        logger.error(
            "Unexpected enrichment error for IP %s: %s",
            ip,
            e
        )

        return safe_result
