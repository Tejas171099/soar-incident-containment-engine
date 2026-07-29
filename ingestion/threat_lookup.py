import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    raise ValueError("ABUSEIPDB_API_KEY not found. Check your .env file.")

ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip_reputation(ip: str):
    """
    Check the reputation of an IP address using AbuseIPDB.
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

        return {
            "ip": data["ipAddress"],
            "abuse_confidence_score": data["abuseConfidenceScore"],
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
