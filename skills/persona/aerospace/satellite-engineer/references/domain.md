## § 4 · Domain Knowledge

### Orbit Characteristics

| Orbit | Altitude | Period | Applications |
|-------|----------|--------|--------------|
| LEO | 200-2,000 km | 90-120 min | EO, ISS, Starlink |
| MEO | 2,000-35,786 km | 2-12 hrs | Navigation (GPS) |
| GEO | 35,786 km | 24 hrs | Communications |
| GSO | 35,786 km | 24 hrs | Weather, comms |
| HEO | Elliptical | Variable | Coverage, SIGINT |
| L2 | ~1.5M km | - | JWST, future missions |

### Power Subsystem Sizing

```
Power Budget Example:
├── Payload: 500W average
├── AOCS: 150W (peak during maneuvers)
├── Communications: 200W (transmit)
├── Thermal: 100W (heaters)
├── OBDH: 50W (computers)
├── Margin: 20% (200W)
└── Total: 1,200W requirement

Solar Array Sizing:
├── Solar constant: 1,361 W/m²
├── Cell efficiency: 28-30% (GaAs)
├── Degradation: 2-3% per year
├── Angle losses: Cosine of incidence
└── Array size: ~4 m² for 1,200W at EOL
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
