## § 8 · Standard Workflow

### 8.1 Utility-Scale BESS Specification

```
Phase 1: Requirements Definition
├── Gather: Site constraints, grid connection point, utility tariffs
├── Define: Target capacity (MWh), power (MW), discharge duration
├── Assess: Ambient temperature range, seismic zone, fire marshal requirements
└── Deliverable: Project requirements document with site constraints

Phase 2: System Design
├── Select: Battery chemistry (LFP vs NMC), cell form factor, module configuration
├── Size: Container count, rack layout, HVAC capacity
├── Specify: BMS functionality, communication protocols, SCADA integration
└── Deliverable: Single-line diagram, equipment schedule, layout plan

Phase 3: Safety & Compliance
├── Analyze: UL 9540A results or request testing
├── Design: Fire suppression, ventilation, detection systems
├── Review: NFPA 855 compliance, obtain AHJ approval
└── Deliverable: Safety data sheet, fire protection plan, permit package

Phase 4: Economic Analysis
├── Model: 20-year cash flow with degradation curves
├── Calculate: LCOS, NPV, IRR
├── Optimize: Contract structure, tax credits (ITC), utility tariffs
└── Deliverable: Financial model, levelized cost comparison
```

### 8.2 BMS Algorithm Development

```
Step 1: Define cell characteristics (capacity, impedance, chemistry)
Step 2: Select SOC estimation method (Coulomb counting, KF, neural network)
Step 3: Design SOH estimation (capacity fade, internal resistance growth)
Step 4: Specify balancing strategy (passive vs active, threshold, timing)
Step 5: Define thermal management setpoints (cooling, heating, limits)
Step 6: Implement safety limits (UVP, OVP, OCP, OTP, short circuit)
Step 7: Test with accelerated aging and diverse operating conditions
```

---
