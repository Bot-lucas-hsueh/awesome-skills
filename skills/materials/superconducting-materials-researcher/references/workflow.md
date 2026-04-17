# Standard Workflow

## 8.1 Superconducting Wire/Magnet Development Workflow

```
Phase 1: Material Selection & Specification
├── Define application: MRI (1.5–3T), accelerator (5–16T), NMR (>20T)
├── Select conductor: Nb₃Sn (≤16T), NbTi (≤8T), REBCO (≥10T)
├── Define strand/wire specs: Ic, RRR, filament count, twist pitch
└── Establish mechanical requirements: stress limits, strain budget

Phase 2: Procurement & Characterization
├── Receive vendor certification data
├── Perform incoming inspection: Ic, RRR, cross-section, twist
├── Statistical sampling for lot acceptance
└── Store in controlled environment (temperature, humidity)

Phase 3: Coil Winding & Processing
├── Winding: react&wind (Nb₃Sn) vs. wind&react (NbTi)
├── Impregnation: vacuum-pressure impregnation (VPI) or no-insulation
├── Terminal焊接: resistive or ultrasonic welding
└── Ground insulation: Kapton wrapping, mica tape

Phase 4: Testing & Validation
├── Room-temperature resistance measurement
├── Low-temperature test: Ic, field quality, training cycles
├── Persistent switch test (if applicable)
└── Long-term stability monitoring
```

## 8.2 Common Workflows

### MRI Magnet Workflow (NbTi, 1.5T)

1. Define target field: 1.5T at 50 cm DSV, homogeneity < 10 ppm
2. Select NbTi wire: Ic > 300 A at 5T (77% wire fill factor)
3. Design coils: main solenoids + shielding
4. Wind and react: 650°C for 48h (Nb₃Sn) or as per spec
5. Impregnate with epoxy under vacuum
6. Cool down with liquid He; perform training
7. Final field mapping: homogeneity < 10 ppm over DSV

### High-Field Accelerator Dipole (Nb₃Sn, 12T)

1. Define gradient: > 12 T at aperture 90 mm
2. Select ROXY wire: Ic(12T, 4.2K) > 400 A; RRR > 100
3. Stress management: bladder/key or yoke preloading
4. Wind react&wind: 650°C/48h reaction, then winding
5. Coil assembly into iron yoke with pre-stress
6. Cryogenic test: training to 90% of short-sample current
7. Magnetic measurement: field quality at 12 T

### REBCO HTS Magnet (No-Insulation Winding)

1. Select coated conductor: Ic > 500 A/cm-w at 77K self-field
2. Design: no-insulation winding for thermal stability
3. Winding: turn-to-turn contact, no inter-layer insulation
4. Test: charge at 0.5 A/s, monitor voltage
5. Protection: discharge time constant ~100s (passive)

## 8.3 Quench Protection Protocol

| Step | Action | Threshold |
|------|--------|-----------|
| 1 | Voltage detection (V > 0.1V) | V > 0.1 V |
| 2 | Confirm quench (2nd voltage tap) | V > 0.1 V |
| 3 | Dump energy: activate quench heaters or diode | < 5 ms |
| 4 | Close valves (if cryogenless) | Immediate |
| 5 | Personnel safety: evacuate area | Per facility SOP |
