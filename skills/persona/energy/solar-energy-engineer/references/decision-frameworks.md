## § 5 · Decision Frameworks

### Site Selection Criteria

```
Solar Resource (30%):
├── Min GHI: 1,400 kWh/m²/year
├── Consistency: Low interannual variability
└── Seasonal: Match to demand pattern

Land & Access (25%):
├── Flat to gently rolling terrain
├── Proximity to transmission (<5 miles)
├── Road access for construction
└── No flood zones, wetlands

Grid Interconnection (25%):
├── Available transmission capacity
├── Interconnection voltage level
├── Queue position, timing
└── Upgrade costs

Permits & Community (20%):
├── Zoning compatibility
├── Environmental clearances
├── Community support
└── Tax incentives
```

### String Sizing Methodology

| Parameter | Calculation | Limit |
|-----------|-------------|-------|
| Max Voc | Voc × 1.25 (low temp) | < Inverter max DC |
| Min Vmp | Vmp × 0.85 (high temp) | > Inverter min MPPT |
| Max Isc | Isc × 1.25 | < Inverter max current |
| String Length | Based on above | Typically 20-34 modules |

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
