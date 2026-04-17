## § 4 Core Philosophy

### Mental Model: Vertiport as a System

```
┌─────────────────────────────────────────────────────────┐
│  AIRSPACE INTERFACE                                      │
│  Approach/departure paths, UTM OV filing, noise abatement│
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│  FATO
│  Landing pads, obstacle limitation surfaces, lighting    │
│  ← Safety-critical; aviation authority jurisdiction →   │
├─────────────────────────────────────────────────────────┤
│  TRANSITION ZONE                                         │
│  Passenger marshaling, aircraft towing/positioning       │
├─────────────────────────────────────────────────────────┤
│  CHARGING
│  Charging stations, basic maintenance, turnaround ops   │
├─────────────────────────────────────────────────────────┤
│  TERMINAL
│  Passenger processing, ticketing, ground transport      │
│  ← Building authority
└─────────────────────────────────────────────────────────┘
```

### Guiding Principles

1. **Airside is Aviation Authority's Domain**: Any area where aircraft operate or taxi is subject to aviation authority jurisdiction; building departments cannot override FAA/EASA requirements for FATO design, obstacle surfaces, or lighting
2. **Design the Bottleneck, Not the Average**: Vertiport capacity is set by the slowest step (usually charging time); design around 90th percentile turnaround time, not mean; model queuing under disruption scenarios, not just smooth operations
3. **Community Is a Permitting Authority**: Local governments cannot block FAA airspace approval, but they can block building permits, zoning variances, and operating licenses; treat community relations as a critical path item from Day 1

---

