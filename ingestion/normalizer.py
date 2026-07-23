def normalize_alert(alert):

    return {

        "alert_id": alert.get("id"),

        "timestamp": alert.get("time"),

        "source_ip": alert.get("src_ip") or alert.get("source_ip"),

        "alert_type": alert.get("type"),

        "target_host": alert.get("host"),

        "severity": alert.get("severity","medium")
    }
