# Standard Workflow

## 8.1 SiC/GaN Power Device Characterization Workflow

```
Phase 1: Device Selection & Datasheet Review
├── Verify AEC-Q101/Grade 0 qualification (automotive)
├── Cross-check VDS/VGS ratings, RDS(on), Qg parameters
├── Verify body diode characteristics (SiC) and 0V turn-off capability (GaN)
└── Review gate drive requirements: Vgs(on) ~15V, Vgs(off) = -3 to -5V (SiC)

Phase 2: Double Pulse Test (DPT) Setup
├── Configure half-bridge: upper device as load, lower as DUT
├── Set VDC = 80% of rated voltage
├── Select Lload to achieve desired di/dt (~100–500 A/µs)
├── Configure gate driver: Rg_on, Rg_off per datasheet recommendation
└── Capture Eon, Eoff, body diode recovery (SiC) at rated current

Phase 3: Loss Measurement & Thermal Assessment
├── Measure RDS(on) at operating temperature (T_j_measured via thermal camera)
├── Calculate total losses: P_cond = I²×RDS(on)×D + E_sw×f_sw
├── Verify junction temperature stays < 80% of Tj_max under worst case
└── If Tj > limit: derate current or improve cooling

Phase 4: Parasitic Management & EMI Assessment
├── Analyze dv/dt and di/dt for overshoot/ringing
├── Add snubber (RC or RCD) if Vds overshoot > 10%
├── Measure CM/CM noise spectrum for EMI compliance
└── Verify gate oscillation is damped (< 5V ringing)
```

## 8.2 Common Workflows

### SiC MOSFET Inverter Design (EV Drive Train, 800V)

1. Select SiC MOSFET module: 1200V, 400A, RDS(on) = 6.5 mΩ
2. Design gate drive: Vgs = +15V/-3V, Rg = 2.2 Ω, isolated DC-DC
3. Double pulse test: measure Eon/Eoff at 400A, 800V, Tj = 25°C and 150°C
4. Calculate losses: P_total = 3 × (P_cond + P_sw) per phase
5. Thermal design: water cooling, Rth_heatsink < 0.05 °C/W
6. EMI design: add CM filter, DC bus RC snubber
7. Validate: 1000h HTRB + power cycling to AEC-Q101

### GaN HEMT Synchronous Buck Converter (48V/12V, 400W)

1. Select 650V GaN: E-HEMT for hard switching, L-HEMT for synchronous rectification
2. Design PCB: Kelvin source connection, minimize parasitic inductance (< 2 nH)
3. Gate drive: Vgs = +6V/-3V (GaN-specific); Rg_on = 5 Ω, Rg_off = 1 Ω
4. Switching characterization: Eon/Eoff at 10A, 400V; expect < 50 µJ total
5. Thermal: GaN can be mounted without isolation pad (source cool)
6. EMI: high dv/dt (100+ V/ns) — careful layout critical

### GaN Class-D Audio Amplifier

1. Select GaN HEMT: 650V, low Coss, high FOM
2. Design gate drive: +6V/-6V push-pull, < 5 ns propagation delay
3. Layout: symmetric half-bridge, star-ground for gate return
4. EMI filter: differential and CM chokes per IEC 61000-4-6
5. Thermal: junction temperature monitoring at rated power

## 8.3 Reliability Qualification Protocol

| Step | Activity | Output |
|------|----------|--------|
| 1 | HTRB @ 150°C, 100% Vrat | 168h report, early failure detection |
| 2 | HTGB @ Vgs_max, 150°C | Gate threshold stability data |
| 3 | Power cycling ΔT_j=100°C | Thermal fatigue failure analysis |
| 4 | High humidity H3TRB | Moisture sensitivity level (MSL) |
| 5 | AEC-Q101 supplemental tests | Automotive-grade certification |
