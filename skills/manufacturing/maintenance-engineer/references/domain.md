## § 4 · Domain Knowledge

### Condition Monitoring Techniques

| Technique | Detects | Frequency | Cost |
|-----------|---------|-----------|------|
| Vibration Analysis | Bearing, gear, imbalance | Monthly | Medium |
| Thermography | Hot connections, bearings | Quarterly | Low |
| Oil Analysis | Wear, contamination | Monthly | Medium |
| Ultrasonic | Leaks, electrical, bearing | Monthly | Low |
| Motor Current | Electrical, mechanical | Continuous | Medium |
| Visual Inspection | Obvious issues | Daily | Low |

### Reliability Metrics

```
MTBF (Mean Time Between Failures):
MTBF = Total Operating Time / Number of Failures

MTTR (Mean Time To Repair):
MTTR = Total Repair Time / Number of Repairs

Availability:
Availability = MTBF / (MTBF + MTTR)

or

Availability = (Planned Production Time - Downtime) / Planned Production Time

Target: >95% for critical equipment
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
