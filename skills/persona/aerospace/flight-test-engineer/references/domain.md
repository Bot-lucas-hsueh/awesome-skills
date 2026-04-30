## § 4 · Domain Knowledge

### Standard Atmosphere Parameters

| Altitude (ft) | Pressure (psf) | Temperature (°R) | Density (slug/ft³) |
|---------------|----------------|------------------|---------------------|
| Sea Level | 2,116 | 518.7 | 0.002377 |
| 5,000 | 1,761 | 500.9 | 0.002048 |
| 10,000 | 1,456 | 483.1 | 0.001756 |
| 35,000 | 499 | 394.0 | 0.000738 |
| 41,000 | 392 | 390.0 | 0.000587 |

### Data Acquisition Systems

```
Typical Instrumentation Suite:
├── Air Data: Pitot-static probes, ADS, vanes
├── Inertial: INS/GPS, accelerometers, rate gyros
├── Control Position: Potentiometers, LVDTs, encoders
├── Structural: Strain gauges, accelerometers
├── Engine: N1, N2, EGT, fuel flow, vibration
├── Environment: OAT, humidity, pressure altitude
└── Video: Cockpit, external, instrument panel

Sampling Rates:
├── High-speed: 1,000 Hz (structural dynamics)
├── Standard: 100 Hz (control response)
├── Medium: 10 Hz (performance parameters)
└── Low: 1 Hz (environmental, status)
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
