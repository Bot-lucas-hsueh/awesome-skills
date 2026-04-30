## § 4 · Domain Knowledge

### Material Properties

| Material | Ftu (ksi) | Fty (ksi) | Density (lb/in³) | Application |
|----------|-----------|-----------|------------------|-------------|
| 2024-T3 Al | 64 | 42 | 0.100 | Fuselage skin |
| 7075-T6 Al | 78 | 67 | 0.101 | Wing structure |
| 2195 Al-Li | 77 | 72 | 0.093 | Space, advanced |
| Ti-6Al-4V | 134 | 126 | 0.160 | High temp, bolts |
| CFRP (T800) | 300+ | - | 0.057 | Primary structure |

### Allowables Philosophy

```
A-Basis Allowable: 99% probability, 95% confidence
├── Used for single-load-path structure
├── No redistribution possible
└── More conservative

B-Basis Allowable: 90% probability, 95% confidence
├── Used for multiple-load-path structure
├── Load redistribution possible
└── Less conservative, lighter
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
