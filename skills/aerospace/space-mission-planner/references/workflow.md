## § 8 Standard Workflow

### Phase 1: Mission Concept Definition
```
1.1 Science/Operational Requirements Flowdown
  - [ ] Define primary science objectives with measurable success criteria
  - [ ] Identify driving instrument/payload requirements (resolution, coverage, sensitivity)
  - [ ] Translate payload requirements to spacecraft requirements (pointing, data volume, power)
  - [✓ Done] Output: Mission Requirements Document (MRD)
  - [✗ FAIL] If payload requirements exceed launch vehicle mass → descope or change LV

1.2 Mission Architecture Trade Study
  - [ ] Identify 3 candidate architectures (vary orbit, spacecraft class, launch vehicle)
  - [ ] Compute delta-V budget for each architecture
  - [ ] Estimate spacecraft mass for each architecture (SMAD statistical relationships)
  - [ ] Score against cost, risk, technical maturity, schedule
  - [✓ Done] Output: Mission Architecture Trade Report with selected baseline
```

### Phase 2: Trajectory & Spacecraft Design
```
2.1 Trajectory Analysis
  - [ ] Compute launch windows for next 5 years (identify optimal and backup windows)
  - [ ] Design nominal trajectory with all required maneuvers (launch + TCMs + orbit insertion)
  - [ ] Compute total delta-V budget; add 15% margin for trajectory correction maneuvers
  - [ ] Verify launch vehicle can deliver wet mass on required C3
  - [✓ Done] Output: Trajectory Design Report with delta-V budget and launch window calendar
  - [✗ FAIL] If LV cannot deliver spacecraft → reduce wet mass or change LV

2.2 Spacecraft Mass Budget
  - [ ] Estimate subsystem masses (payload, propulsion, power, structure, ADCS, telecom, C&DH)
  - [ ] Apply mass margins (30% at concept, 15% at PDR, 10% at CDR)
  - [ ] Verify propellant mass matches delta-V budget using rocket equation
  - [✓ Done] Output: Mass Budget v1.0 with positive mass margin to LV capability
  - [✗ FAIL] If mass margin < 10% at PDR → design-to-cost/mass activity required

2.3 Power System Sizing
  - [ ] Calculate worst-case power load (all instruments powered simultaneously)
  - [ ] Compute solar array size for mission distance and eclipse fraction
  - [ ] Size battery for eclipse operation (DoD < 80% for Li-ion)
  - [✓ Done] Output: Power Budget with positive margin at all mission phases
```

### Phase 3: Operations & Risk
```
3.1 Ground System Architecture
  - [ ] Identify ground station network (DSN, commercial, national agency)
  - [ ] Compute contact duration and data volume per contact
  - [ ] Design link budget (forward and return links)
  - [✓ Done] Output: Ground System Architecture Document with contact schedule

3.2 Mission Risk Assessment
  - [ ] Identify top-10 risk drivers (technical, schedule, programmatic)
  - [ ] Estimate P(LOM) for critical failure modes
  - [ ] Define mitigation measures; verify residual risk is acceptable
  - [✓ Done] Output: Mission Risk Register with mitigation plan accepted by stakeholders
```

