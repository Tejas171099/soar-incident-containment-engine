def choose_action(risk_level):
    if risk_level == "high":
        return "block_ip"
    elif risk_level == "medium":
        return "manual_review"
    return "no_action"
