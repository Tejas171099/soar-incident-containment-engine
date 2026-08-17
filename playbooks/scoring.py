def decide_risk(score):
    if score >= 80:
        return "high"
    elif score >= 40:
        return "medium"
    return "low"