from playbooks.playbook_engine import process_enriched_alert


def test_high_risk_brute_force_alert():
    alert = {
        "alert_id": "ALT-1001",
        "source_ip": "203.0.113.10",
        "alert_type": "brute_force",
        "reputation_score": 90,
        "source": "abuseipdb",
    }
    result = process_enriched_alert(alert)
    assert result["risk_level"] == "high"
    assert result["recommended_action"] == "block_ip"


def test_high_risk_malware_alert():
    alert = {
        "alert_id": "ALT-1002",
        "source_ip": "203.0.113.20",
        "alert_type": "malware_detection",
        "reputation_score": 95,
        "source": "abuseipdb",
    }
    result = process_enriched_alert(alert)
    assert result["risk_level"] == "high"
    assert result["recommended_action"] == "isolate_host"


def test_medium_risk_suspicious_login():
    alert = {
        "alert_id": "ALT-1003",
        "source_ip": "203.0.113.30",
        "alert_type": "suspicious_login",
        "reputation_score": 55,
        "source": "abuseipdb",
    }
    result = process_enriched_alert(alert)
    assert result["risk_level"] == "medium"
    assert result["recommended_action"] == "manual_review"


def test_failed_enrichment_requires_manual_review():
    alert = {
        "alert_id": "ALT-1004",
        "source_ip": "203.0.113.40",
        "alert_type": "brute_force",
        "reputation_score": 0,
        "source": "lookup_failed",
    }
    result = process_enriched_alert(alert)
    assert result["risk_level"] == "unknown"
    assert result["recommended_action"] == "manual_review"