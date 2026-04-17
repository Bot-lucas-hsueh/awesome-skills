## § 4 · Domain Knowledge

### Key Engine Parameters

| Parameter | Symbol | Civil Transport | Regional Jet | Business Jet |
|-----------|--------|-----------------|--------------|--------------|
| Bypass Ratio | BPR | 8-12 | 4-6 | 2-4 |
| Overall Pressure Ratio | OPR | 40-60 | 20-30 | 15-25 |
| Fan Pressure Ratio | FPR | 1.3-1.6 | 1.6-2.0 | 2.0-3.0 |
| Turbine Inlet Temp | TIT | 1,700-1,900K | 1,600-1,750K | 1,500-1,650K |
| Thrust Range | - | 20K-115K lbf | 5K-25K lbf | 2K-10K lbf |

### Engine Performance Metrics

```
Specific Fuel Consumption (SFC):
├── Units: lb fuel / lbf thrust / hour
├── Cruise SFC: 0.50-0.55 (modern turbofans)
├── Improvement: ~1% per year (historical trend)
└── GTF advantage: 15-16% vs conventional

Propulsive Efficiency (ηp):
├── ηp = 2 / (1 + Ve/V0)
├── Higher BPR → higher ηp
├── Limit: Fan diameter, weight, drag
└── GTF: Optimize fan speed independently

Thermal Efficiency (ηth):
├── ηth = 1 - (1/OPR)^((γ-1)/γ)
├── Higher OPR → higher ηth
├── Limit: Compressor efficiency, TIT
└── Current: ~55% combined efficiency target
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
