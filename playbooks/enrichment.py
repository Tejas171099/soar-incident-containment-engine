def enrich_ip(ip):
    mock_db = {
        "203.0.113.5": 92,
        "8.8.8.8": 0
    }
    score = mock_db.get(ip, 10)
    return {
        "ip": ip,
        "reputation_score": score,
        "threat_source": "mock_threat_db"
    }
