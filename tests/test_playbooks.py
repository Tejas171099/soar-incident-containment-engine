from playbooks.enrichment import enrich_ip
from playbooks.scoring import decide_risk
from playbooks.actions import choose_action

def test_flow():
    result = enrich_ip("203.0.113.5")
    risk = decide_risk(result["reputation_score"])
    action = choose_action(risk)

    assert result["reputation_score"] == 92
    assert risk == "high"
    assert action == "block_ip"
