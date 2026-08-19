# Week 3 Summary – Tejas

## Overview

During Week 3, the playbook engine was extended to support multiple alert types and different response actions based on alert type and threat intelligence enrichment results.

## Alert Types Implemented

The playbook engine supports:

- `brute_force`
- `malware_detection`
- `suspicious_login`

## Risk-Based Decisions

The playbook engine uses the reputation score from threat enrichment to determine the risk level:

- High: score >= 80
- Medium: score 40–79
- Low: score < 40

## Automated and Manual Actions

The implemented response mapping is:

- High-risk brute force → `block_ip`
- High-risk malware detection → `isolate_host`
- High-risk suspicious login → `manual_review`
- Medium-risk alerts → `manual_review`
- Low-risk alerts → `no_action`

## Enrichment Failure

When threat intelligence enrichment fails, the system does not perform an aggressive automated containment action.

Instead:

- Risk level → `unknown`
- Recommended action → `manual_review`
- Action status → `pending`

## Testing

Week 3 tests cover:

1. High-risk brute-force alert.
2. High-risk malware detection alert.
3. Medium-risk suspicious-login alert.
4. Threat intelligence enrichment failure.

The tests verify both the calculated risk level and the recommended action.

## Outcome

The Week 3 implementation provides a multi-alert playbook engine with risk-based response decisions and safe handling of threat intelligence failures.
