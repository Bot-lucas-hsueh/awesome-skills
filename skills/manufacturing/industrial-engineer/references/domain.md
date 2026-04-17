## § 4 · Domain Knowledge

### OEE Calculation

```
Overall Equipment Effectiveness:
OEE = Availability × Performance × Quality

Availability = Run Time / Planned Production Time
├── Planned stops (breaks, changeovers) excluded
└── Downtime: Breakdowns, setups, adjustments

Performance = (Ideal Cycle Time × Total Count) / Run Time
├── Speed losses: Running slow, micro-stops
└── Theoretical max vs actual output

Quality = Good Count / Total Count
├── Defects, rework, scrap
└── First-pass yield

World-Class Targets:
├── Availability: 90%+
├── Performance: 95%+
├── Quality: 99%+
└── OEE: 85%+
```

### Line Balancing

| Station | Task Time (s) | Takt Time (s) | Utilization |
|---------|---------------|---------------|-------------|
| 1 | 45 | 60 | 75% |
| 2 | 58 | 60 | 97% |
| 3 | 52 | 60 | 87% |
| 4 | 55 | 60 | 92% |

```
Line Efficiency = (Sum of task times) / (Number of stations × Takt time)
                = (45+58+52+55) / (4 × 60) = 210 / 240 = 87.5%

Balance Delay = 1 - Efficiency = 12.5%
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
