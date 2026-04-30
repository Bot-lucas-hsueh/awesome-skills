## § 8 · Standard Workflow

### 8.1 Instrument Specification

```
Phase 1: Process Requirements
├── Define measured variable: (temperature, pressure, flow, level)
├── Determine operating range: (min, normal, max values)
├── Specify accuracy requirements: (% of reading or URL)
└── Identify process conditions: (media, temperature, pressure, hazards)

Phase 2: Instrument Selection
├── Select sensor type: (thermocouple, RTD, pressure transducer, etc.)
├── Determine range: (URL = 1.25 × max operating)
├── Choose output signal: (4-20mA, HART, Fieldbus)
└── Specify materials: (wetted materials, housing)

Phase 3: Installation & Commissioning
├── Verify location: (representative measurement point)
├── Check installation requirements: (orientation, insertion depth, piping)
└── Configure transmitter: (range, damping, linearization)
└── Perform loop check: (signal verification from sensor to DCS)

Phase 4: Documentation
├── Create instrument data sheets: (ISA format)
├── Update P&IDs: (instrument tag, type, range)
└── Establish calibration schedule: (interval based on stability data)
```

### 8.2 Control Loop Troubleshooting

```
Step 1: Identify symptoms - Oscillation, slow response, offset
Step 2: Check valve - Positioner calibration, sticking, stiction
Step 3: Check transmitter - Range, output, calibration
Step 4: Check controller - Mode, PID settings, output
Step 5: Tune or adjust - Based on root cause analysis
```

---
