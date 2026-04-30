## § 5 · Decision Frameworks

### Orbit Selection Process

```
Step 1: Mission Requirements
├── Coverage: Regional, global, specific targets
├── Revisit: Frequency of observation
├── Latency: Time from observation to product
└── Payload constraints: Field of view, resolution

Step 2: Orbit Trade
├── LEO: Low latency, low cost, needs constellation
├── MEO: Navigation orbits, radiation environment
├── GEO: Fixed ground track, communications
└── Specialized: Sun-synchronous, dawn-dusk, frozen

Step 3: Constellation Design
├── Number of satellites
├── Orbital planes and phasing
├── Launch and deployment strategy
└── Replacement strategy

Step 4: Validation
├── Coverage analysis
├── Launch vehicle compatibility
├── Debris and spectrum coordination
└── Cost analysis
```

### Propulsion Trade Matrix

| Type | Isp (s) | Thrust | Use Case |
|------|---------|--------|----------|
| Cold Gas | 50-75 | Low | AOCS, small sats |
| Monoprop | 200-250 | Low-Med | AOCS, orbit adjust |
| Biprop | 300-450 | High | Large maneuvers |
| Electric (Ion) | 3,000+ | Very Low | Orbit raising, station keeping |

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
