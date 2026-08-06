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
def decide_risk(score: int) -> str:
    if score >= 75:
        return "high"
    elif score >= 30:
        return "medium"
    return "low"

def choose_action(risk_level: str) -> str:
    if risk_level == "high":
        return "block_ip"
    elif risk_level == "medium":
        return "manual_review"
    elif risk_level == "low":
        return "no_action"
    return "escalate_to_analyst"


def process_enriched_alert(enriched_alert: dict) -> dict:
    score = enriched_alert.get("reputation_score", 0)
    risk_level = decide_risk(score)
    action = choose_action(risk_level)

    return {
        "alert_id": enriched_alert.get("alert_id"),
        "source_ip": enriched_alert.get("source_ip") or enriched_alert.get("ip"),
        "reputation_score": score,
        "risk_level": risk_level,
        "recommended_action": action,
        "action_status": "pending"
    }
