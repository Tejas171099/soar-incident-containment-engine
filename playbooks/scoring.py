def decide_risk(score: int) -> str:
    if score >= 75:
        return "high"
    elif score >= 30:
        return "medium"
    return "low"
