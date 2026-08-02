def choose_action(risk_level: str) -> str:
    if risk_level == "high":
        return "block_ip"
    elif risk_level == "medium":
        return "manual_review"
    elif risk_level == "low":
        return "no_action"
    return "escalate_to_analyst"
