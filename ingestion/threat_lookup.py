import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    raise ValueError("ABUSEIPDB_API_KEY not found. Check your .env file.")

ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip_reputation(ip: str):
    """
    Check the reputation of an IP address using AbuseIPDB.
    Returns standardized enrichment fields for the SOAR engine.
    """

    if not ip:
        return {
            "error": "No IP address provided"
        }

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(
            ABUSEIPDB_URL,
            headers=headers,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()["data"]

        # Reputation score
        reputation_score = data["abuseConfidenceScore"]

        # Decide risk level and action
        if reputation_score >= 80:
            risk_level = "High"
            recommended_action = "Block IP"

        elif reputation_score >= 40:
            risk_level = "Medium"
            recommended_action = "Investigate"

        else:
            risk_level = "Low"
            recommended_action = "Monitor"

        return {
            "ip": data["ipAddress"],
            "reputation_score": reputation_score,
            "risk_level": risk_level,
            "recommended_action": recommended_action,
            "source": "AbuseIPDB",
            "country": data["countryCode"],
            "isp": data["isp"],
            "domain": data["domain"],
            "is_public": data["isPublic"],
            "total_reports": data["totalReports"]
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }
