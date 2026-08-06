from playbooks.enrichment import enrich_ip
from playbooks.scoring import decide_risk
from playbooks.actions import choose_action


def process_alert(alert: dict) -> dict:
    ip = alert.get("source_ip") or alert.get("src_ip")

    enrichment_result = enrich_ip(ip)
    risk_level = decide_risk(enrichment_result["reputation_score"])
    action = choose_action(risk_level)

    return {
        "alert_id": alert.get("id") or alert.get("alert_id"),
        "source_ip": ip,
        "reputation_score": enrichment_result["reputation_score"],
        "risk_level": risk_level,
        "recommended_action": action,
        "action_status": "pending"
    }


if __name__ == "__main__":
    sample_alert = {
        "id": "A123",
        "source_ip": "203.0.113.5",
        "type": "brute_force",
        "host": "web-server-01",
        "severity": "high"
    }

    result = process_alert(sample_alert)
    print(result)
