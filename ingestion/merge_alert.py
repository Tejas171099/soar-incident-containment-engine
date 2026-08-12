"""
merge_alert.py

Combines the normalized alert with threat enrichment
into one enriched alert object.
"""


def merge_alert(normalized_alert: dict, enrichment: dict) -> dict:
    """
    Merge normalized alert data with enrichment results.

    Parameters
    ----------
    normalized_alert : dict
        Alert after normalization.

    enrichment : dict
        Threat intelligence lookup result.

    Returns
    -------
    dict
        Complete enriched alert.
    """

    return {

        "alert_id": normalized_alert.get("alert_id"),

        "timestamp": normalized_alert.get("timestamp"),

        "source_ip": normalized_alert.get("source_ip"),

        "alert_type": normalized_alert.get("alert_type"),

        "target_host": normalized_alert.get("target_host"),

        "severity": normalized_alert.get("severity"),

        "enrichment": {

            "reputation_score":
                enrichment.get("reputation_score", 0),

            "source":
                enrichment.get("source", "lookup_failed"),

            "country":
                enrichment.get("country", "Unknown"),

            "isp":
                enrichment.get("isp", "Unknown"),

            "asn":
                enrichment.get("asn", "Unknown")

        }

    }
