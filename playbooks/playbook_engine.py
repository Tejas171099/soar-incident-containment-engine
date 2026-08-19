from playbooks.scoring import decide_risk
from playbooks.actions import choose_action


def process_enriched_alert(enriched_alert: dict) -> dict:
    """
    Process an enriched security alert and determine the appropriate
    risk level and response action.

    The function handles:
    - Multiple alert types
    - Threat intelligence enrichment failures
    - Missing required alert fields
    - Risk-based action selection
    - Alert-type-specific response actions
    """

    alert_id = enriched_alert.get("alert_id", "unknown")
    source_ip = enriched_alert.get("source_ip")
    alert_type = enriched_alert.get("alert_type")
    score = enriched_alert.get("reputation_score", 0)
    source = enriched_alert.get("source", "lookup_failed")

    # Handle missing required fields safely
    if not source_ip or not alert_type:
        return {
            "alert_id": alert_id,
            "source_ip": source_ip or "unknown",
            "alert_type": alert_type or "unknown",
            "reputation_score": score,
            "risk_level": "unknown",
            "recommended_action": "manual_review",
            "action_status": "pending",
            "decision_reason": (
                "Required alert fields are missing, "
                "so analyst review is required."
            )
        }

    # Handle threat intelligence enrichment failure
    if source == "lookup_failed":
        return {
            "alert_id": alert_id,
            "source_ip": source_ip,
            "alert_type": alert_type,
            "reputation_score": 0,
            "risk_level": "unknown",
            "recommended_action": "manual_review",
            "action_status": "pending",
            "decision_reason": (
                "Threat enrichment lookup failed, "
                "so analyst review is required."
            )
        }

    # Calculate risk level from the reputation score
    risk_level = decide_risk(score)

    # Select the default action based on risk level
    recommended_action = choose_action(risk_level)

    # Alert-type-specific response actions
    if alert_type == "malware_detection" and risk_level == "high":
        recommended_action = "isolate_host"

    if alert_type == "suspicious_login" and risk_level == "high":
        recommended_action = "manual_review"

    # Return the final playbook decision
    return {
        "alert_id": alert_id,
        "source_ip": source_ip,
        "alert_type": alert_type,
        "reputation_score": score,
        "risk_level": risk_level,
        "recommended_action": recommended_action,
        "action_status": "pending",
        "decision_reason": (
            "Decision created from alert type and "
            "enrichment reputation score."
        )
    }
