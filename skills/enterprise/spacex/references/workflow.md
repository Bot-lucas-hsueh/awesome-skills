## §3 · Workflow

### §3.1 Hardware-Rich Development Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    DESIGN-BUILD-TEST-FLY                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐      │
│  │  DESIGN │───→│  BUILD  │───→│   TEST  │───→│   FLY   │      │
│  │  (Days) │    │ (Weeks) │    │ (Days)  │    │ (Hours) │      │
│  └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘      │
│       ↑              │              │              │            │
│       └──────────────┴──────────────┴──────────────┘            │
│                    LEARN → ITERATE                              │
│                                                                 │
│  Target cycle time: 2-4 weeks per iteration                     │
└─────────────────────────────────────────────────────────────────┘
```

**Phase 1: Design (Days)**
- CAD modeling in Siemens NX
- Structural FEA (in-house tools)
- CFD for aerodynamics/propulsion
- Peer review (red team/blue team)

**Phase 2: Build (Weeks)**
- Fabricate at Starfactory (Starship) or Hawthorne (Falcon/Dragon)
- Friction stir welding for tanks
- Additive manufacturing for complex components
- Minimal tooling (fabricate tooling as fast as parts)

**Phase 3: Test (Days)**
- Component testing at McGregor, TX
- Structural load testing
- Propulsion hot-fire (short duration → long duration)
- Software-in-the-loop simulation

**Phase 4: Fly (Hours)**
- Launch from Starbase (TX) or LC-39A (FL)
- Telemetry collection (10,000+ sensors on Starship)
- Controlled test-to-failure if needed
- Rapid data analysis post-flight

### §3.2 Cost Reduction Methodology

**The 10x Cost Reduction Formula:**

| Lever | Approach | Impact |
|-------|----------|--------|
| Reusability | Fly 10+ times per vehicle | 5-10x |
| Vertical Integration | Build 70% in-house | 3-5x |
| Design Simplicity | Reduce parts count | 2-3x |
| Manufacturing Automation | Weld, don't bolt | 2-3x |
| Commercial Components | Use automotive-grade | 2-5x |

**Applied Example - Falcon 9:**
- Traditional cost: $400M per launch (ULA)
- SpaceX cost: $62M per launch (new), $30M (reused)
- Factor: 6.5x reduction with reusability

### §3.3 Safety vs. Speed Balance

**Risk Acceptance Framework:**
- **Test Articles**: Accept 30% failure rate (learn from breaks)
- **Operational Vehicles**: 99%+ reliability required
- **Crew Missions**: 99.9%+ with escape systems

**Pre-Flight Checklist:**
- [ ] All critical systems green
- [ ] Weather within limits
- [ ] Range clear
- [ ] Abort modes verified
- [ ] Flight termination system armed

**Post-Flight Analysis:**
- [ ] Telemetry review (all anomalies categorized)
- [ ] Hardware inspection (if recovered)
- [ ] Failure analysis (if applicable)
- [ ] Design updates for next iteration

---
