## § 8 Standard Workflow

### Phase 1: Mission Requirements & Concept
```
1.1 Mission Analysis
  - [ ] Define target orbit (altitude, inclination, circular/elliptical)
  - [ ] Compute ideal orbital velocity and total delta-V requirement (including losses)
  - [ ] Define payload mass and fairing volume envelope
  - [✓ Done] Output: Mission Requirements Document with delta-V budget
  - [✗ FAIL] If delta-V > 10,500 m/s for LEO → mission not viable with single launch vehicle

1.2 Vehicle Concept Trade Study
  - [ ] Compare 2-stage vs. 3-stage architecture for target payload
  - [ ] Evaluate reusable vs. expendable first stage economics
  - [ ] Compute GLOW and payload fraction for 3 candidate configurations
  - [✓ Done] Output: Vehicle Architecture Trade Report with selected baseline
  - [✗ FAIL] If GLOW > $300M equivalent (rough mass proxy) → redesign or accept performance shortfall
```

### Phase 2: Vehicle Sizing & Design
```
2.1 Staging Optimization
  - [ ] Optimize delta-V split using Lagrange multiplier or parametric sweep
  - [ ] Compute stage wet mass, dry mass, propellant mass from Tsiolkovsky equation
  - [ ] Iterate to convergence (change in GLOW < 0.5% between iterations)
  - [✓ Done] Output: Stage Mass Budget v1.0 with positive payload margin
  - [✗ FAIL] If payload fraction < 1.5% → reconsider propellant combination or staging

2.2 Structural Design & Load Definition
  - [ ] Compute max-Q altitude and dynamic pressure from trajectory analysis
  - [ ] Define design load cases: max-Q, Max alpha Q, liftoff, staging, engine-out
  - [ ] Size interstage and fairing for maximum load case + 1.4 factor (NASA-STD-5001)
  - [✓ Done] Output: Structural Design Loads document + preliminary structure mass estimate
  - [✗ FAIL] If structural mass fraction > 12% of stage wet mass → investigate design efficiency

2.3 GNC Architecture
  - [ ] Define guidance law (zero-lift gravity turn, linear tangent, optimal steering)
  - [ ] Size grid fins (reusable first stage) for target entry loads and drag requirement
  - [ ] Design AFSS (Autonomous Flight Termination System) per AFSSUI requirements
  - [✓ Done] Output: GNC Architecture Document with control authority budget
```

### Phase 3: Integration, Testing & Launch Campaign
```
3.1 Systems Integration
  - [ ] Full vehicle mass properties calculation (CG, MOI) at all propellant loadings
  - [ ] Propulsion integration: engine gimbal range vs. CG shift; verify control authority
  - [ ] Fairing payload environment: acoustic, vibration, thermal for customer payload
  - [✓ Done] Output: Vehicle Configuration Document and Interface Control Documents (ICDs)

3.2 Test Campaign
  - [ ] Engine-level hot-fire: all engines at flight duration + margin
  - [ ] Stage-level static fire: flight-ready stage at launch pad
  - [ ] Flight test: no-orbit hop test (reusable); then first orbital mission
  - [✓ Done] Output: Flight Readiness Review (FRR) approval for first launch
```

