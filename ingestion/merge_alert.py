"""
merge_alert.py

Combines a normalized SIEM alert with threat intelligence
enrichment into a single enriched alert object.
"""


def merge_alert(
    normalized_alert: dict,
    enrichment: dict,
) -> dict:
    """
    Merge normalized alert information with enrichment data.

    The function always returns a predictable structure.

    Safe defaults are used when enrichment information is
    missing or when the threat intelligence lookup failed.
    """

    # ---------------------------------------------------------
    # Determine enrichment source
    # ---------------------------------------------------------
    source = enrichment.get(
        "source",
        "lookup_failed",
    )

    # Normalize source formatting
    if isinstance(source, str):
        source = source.lower()

    # ---------------------------------------------------------
    # Build final enriched alert
    # ---------------------------------------------------------
    return {
        "alert_id": normalized_alert.get(
            "alert_id"
        ),

        "timestamp": normalized_alert.get(
            "timestamp"
        ),

        "source_ip": normalized_alert.get(
            "source_ip"
        ),

        "alert_type": normalized_alert.get(
            "alert_type"
        ),

        "target_host": normalized_alert.get(
            "target_host"
        ),

        "severity": normalized_alert.get(
            "severity"
        ),

        "enrichment": {
            "reputation_score": enrichment.get(
                "reputation_score",
                0,
            ),

            "source": source,

            "country": enrichment.get(
                "country",
                "Unknown",
            ),

            "isp": enrichment.get(
                "isp",
                "Unknown",
            ),

            "asn": enrichment.get(
                "asn",
                "Unknown",
            ),
        },
    }
