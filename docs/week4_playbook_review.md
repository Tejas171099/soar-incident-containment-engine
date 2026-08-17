# Week 4 Playbook Review – Tejas

## Risk Scoring
- High: score >= 80
- Medium: score 40–79
- Low: score < 40

## Action Mapping
- High + brute_force → block_ip
- High + malware_detection → isolate_host
- High + suspicious_login → manual_review
- Medium → manual_review
- Low → no_action
- Enrichment failure → manual_review

## Safety Principle
The system never performs aggressive automated action when threat data is missing.