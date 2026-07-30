# Week 2 Enriched Alert Contract

## Input from Threat Enrichment (Rajkumar)

| Field | Description |
|-------|-------------|
| reputation_score | IP reputation score |
| source | Threat intelligence source |

## Output from Playbook Engine (Tejas)

| Field | Description |
|-------|-------------|
| risk_level | Risk classification |
| threat_source | Source of threat information |
| recommended_action | Suggested response |
| action_status | Current action status |

## Data Flow

Rajkumar
↓
reputation_score
source

↓

Tejas Playbook Engine

↓

risk_level
threat_source
recommended_action
action_status

## Status

Week 2 enriched alert contract confirmed.
