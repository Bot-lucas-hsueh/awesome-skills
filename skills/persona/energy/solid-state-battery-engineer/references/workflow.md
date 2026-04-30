## § 8 · Standard Workflow

### 8.1 Solid Electrolyte Development

```
Phase 1: Material Selection & Synthesis
├── Review: Literature for promising compositions (LGPS, argyrodite, LLZO dopants)
├── Synthesize: Solid-state reaction, ball milling, solution precipitation
├── Characterize: XRD for phase purity, SEM for morphology
└── Deliverable: Pure phase electrolyte powder

Phase 2: Electrochemical Characterization
├── Measure: Conductivity (EIS) from -20°C to 80°C
├── Test: Electrochemical stability window (CV)
├── Evaluate: Air stability (for sulfides: H2S evolution)
└── Deliverable: Conductivity vs temperature, stability window

Phase 3: Interface Compatibility
├── Pair: With target cathode (NMC811, NCA) or Li metal
├── Characterize: Interface impedance (EIS), cross-section (SEM)
├── Identify: Degradation products (XPS, ToF-SIMS)
└── Deliverable: Interface resistance, failure mechanism analysis

Phase 4: Cell Demonstration
├── Assemble: Coin cell or pouch cell with composite electrode
├── Cycle: Galvanostatic cycling at various rates
├── Test: Rate capability, temperature performance
└── Deliverable: Cycling data, energy density calculation
```

### 8.2 Interface Engineering Protocol

```
Step 1: Baseline Measurement - Assemble cell without coating, measure initial ASR
Step 2: Degradation Analysis - After cycling, analyze interface composition
Step 3: Coating Selection - Choose coating based on cathode voltage (LNO for NMC, Li3P for Li)
Step 4: Deposition - Apply thin coating (1-10 nm via ALD, or sol-gel)
Step 5: Re-test - Compare initial ASR and growth rate with baseline
Step 6: Optimization - Iterate coating thickness, material, deposition method
```

---
