def merge_alert(normalized, enrichment):

    return {
        **normalized,
        "reputation_score": enrichment["reputation_score"],
        "risk_level": enrichment["risk_level"],
        "recommended_action": enrichment["recommended_action"],
        "source": enrichment["source"],
        "country": enrichment["country"],
        "isp": enrichment["isp"],
        "domain": enrichment["domain"],
        "is_public": enrichment["is_public"],
        "total_reports": enrichment["total_reports"]
    }
