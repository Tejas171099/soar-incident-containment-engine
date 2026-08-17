from playbooks.playbook_engine import process_enriched_alert


def test_low_risk_alert_has_no_action():
    alert = {
        "alert_id": "ALT-2001",
        "source_ip": "198.51.100.10",
        "alert_type": "brute_force",
        "reputation_score": 10,
        "source": "abuseipdb",
    }
    result = process_enriched_alert(alert)
    assert result["risk_level"] == "low"
    assert result["recommended_action"] == "no_action"


def test_high_risk_malware_isolates_host():
    alert = {
        "alert_id": "ALT-2002",
        "source_ip": "198.51.100.20",
        "alert_type": "malware_detection",
        "reputation_score": 88,
        "source": "abuseipdb",
    }
    result = process_enriched_alert(alert)
    assert result["risk_level"] == "high"
    assert result["recommended_action"] == "isolate_host"


def test_lookup_failure_does_not_block_ip():
    alert = {
        "alert_id": "ALT-2003",
        "source_ip": "198.51.100.30",
        "alert_type": "brute_force",
        "reputation_score": 0,
        "source": "lookup_failed",
    }
    result = process_enriched_alert(alert)
    assert result["recommended_action"] == "manual_review"
    assert result["action_status"] == "pending"