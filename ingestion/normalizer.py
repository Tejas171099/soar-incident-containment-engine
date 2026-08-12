from datetime import datetime


def normalize_alert(alert: dict) -> dict:

    timestamp = alert.get("time")

    # Convert datetime object to ISO string
    if isinstance(timestamp, datetime):
        timestamp = timestamp.isoformat()

    normalized = {

        "alert_id": alert.get("id"),

        "timestamp": timestamp,

        "source_ip": (
            alert.get("src_ip")
            or alert.get("source_ip")
        ),

        "alert_type": alert.get("type"),

        "target_host": alert.get("host"),

        "severity": alert.get(
            "severity",
            "medium"
        )

    }

    return normalized
