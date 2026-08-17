from playbooks.scoring import decide_risk
from playbooks.actions import choose_action


def process_enriched_alert(enriched_alert: dict) -> dict:
    alert_id = enriched_alert.get("alert_id", "unknown")
    source_ip = enriched_alert.get("source_ip", "unknown")
    alert_type = enriched_alert.get("alert_type", "unknown")
    score = enriched_alert.get("reputation_score", 0)
    source = enriched_alert.get("source", "lookup_failed")

    if source == "lookup_failed":
        return {
            "alert_id": alert_id,
            "source_ip": source_ip,
            "alert_type": alert_type,
            "reputation_score": 0,
            "risk_level": "unknown",
            "recommended_action": "manual_review",
            "action_status": "pending",
            "decision_reason": "Threat enrichment lookup failed, so analyst review is required."
        }

    risk_level = decide_risk(score)
    recommended_action = choose_action(risk_level)

    if alert_type == "malware_detection" and risk_level == "high":
        recommended_action = "isolate_host"

    if alert_type == "suspicious_login" and risk_level == "high":
        recommended_action = "manual_review"

    return {
        "alert_id": alert_id,
        "source_ip": source_ip,
        "alert_type": alert_type,
        "reputation_score": score,
        "risk_level": risk_level,
        "recommended_action": recommended_action,
        "action_status": "pending",
        "decision_reason": "Decision created from alert type and enrichment reputation score."
    }
