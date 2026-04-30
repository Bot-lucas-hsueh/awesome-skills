## § 5 · Decision Frameworks

### Criticality Analysis Matrix

```
Consequence Rating:
├── Safety: 10 = Potential fatality
├── Environmental: 10 = Major release
├── Production: 10 = Plant shutdown
└── Cost: 10 = >$1M impact

Probability Rating:
├── 10 = Failure imminent or frequent
├── 5 = Likely within 1-2 years
└── 1 = Rare or never

Criticality = Consequence × Probability

Priority:
├── 80-100: Immediate action required
├── 50-79: High priority
├── 25-49: Medium priority
└── <25: Low priority
```

### RCM Decision Logic

| Question | Yes Action | No Action |
|----------|------------|-----------|
| Safety consequence? | Must prevent - redesign or PM | Continue analysis |
| Hidden failure? | Inspection to find | Continue analysis |
| Multiple failures? | Prevent multiple | Continue analysis |
| Wear-out pattern? | Age-based maintenance | Continue analysis |
| P-F interval long? | Condition monitoring | No scheduled maintenance |

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
