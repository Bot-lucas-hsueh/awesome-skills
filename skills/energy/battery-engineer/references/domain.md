## § 4 · Domain Knowledge

### Cell Specifications Comparison

| Parameter | NMC 811 | LFP | Na-ion |
|-----------|---------|-----|--------|
| Nominal Voltage | 3.7V | 3.2V | 3.0V |
| Gravimetric Energy | 250-300 Wh/kg | 160-200 Wh/kg | 100-160 Wh/kg |
| Volumetric Energy | 600-700 Wh/L | 350-450 Wh/L | 200-300 Wh/L |
| Cycle Life | 1,000-3,000 | 3,000-8,000 | 3,000-5,000 |
| C-rate (cont) | 2-3C | 1-2C | 0.5-1C |
| Operating Temp | -20 to 60°C | -20 to 60°C | -40 to 60°C |

### Degradation Mechanisms

```
CAPACITY FADE:
├── SEI Growth: Continuous electrolyte consumption
├── Active Material Loss: Particle cracking, isolation
├── Lithium Loss: Trapped lithium, plating
└── Impedance Rise: SEI thickening, contact loss

POWER FADE:
├── Electrode degradation
├── Current collector corrosion
└── Electrolyte depletion

MITIGATION:
├── Voltage limits: Avoid <2.5V, >4.2V
├── Temperature control: 15-35°C optimal
├── C-rate limits: Derate for aging
└── Storage: 50% SOC, cool temperature
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
