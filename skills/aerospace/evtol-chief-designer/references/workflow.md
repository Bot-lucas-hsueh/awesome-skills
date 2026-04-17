## § 7 Standard Workflow

See [references/08-workflow.md](references/08-workflow.md)

---

---

## Anti-Pattern 2: Ignoring OEI in Hover During Takeoff
**❌ BAD**: Sizing hover rotors for nominal power, not OEI-survivable power
**✅ GOOD**: The FAA requires the vehicle to complete the takeoff and land safely following any single propulsion failure. For 6-rotor systems:
```
Nominal hover power: 6 × P_rotor
OEI hover power:     5 × P_rotor × 1.25 = 6.25 × P_rotor  (25% excess on remaining 5)

Therefore: each motor must be sized for 1.25 × (MTOW × g / 5)
NOT:                                     MTOW × g / 6
```
This typically means motors are 25% heavier than minimum sizing — this weight is mandatory, not optional.

---

### Anti-Pattern 3: Treating Transition as a "Fly It and See" Problem
**❌ BAD**: Deferring transition control law development to flight test
**✅ GOOD**: Transition is the highest-risk flight phase for tiltwing/tiltrotor configs. Design requirements:
- Transition must be abortable at any point (full reverse to hover capability)
- Minimum airspeed for transition initiation: 1.3 × V_stall in hover-assisted mode
- Maximum pitch attitude during transition: ≤ 12° (pilot spatial disorientation risk)
- Control authority must be demonstrated through ± 50% transition axis maneuvers at each tilt angle

Model transition dynamics in Simulink from Day 1 of PDR; do not wait for flight test.

---

### Anti-Pattern 4: Single-String Flight Control Architecture
**❌ BAD**: Implementing a single flight control computer (FCC) to save weight
**✅ GOOD**: FAA SC-VTOL-01 and Part 23 requires that no single failure can cause loss of control. For eVTOL this means:
```
Architecture requirement:
- Triple-redundant FCC (active-active-active or active-active-standby)
- Cross-monitoring with dissimilar voting logic
- Physical separation of FCC units (separate fuselage compartments)
- Independent power supply from at least 2 sources
```
Weight cost: ~15-25 kg. This is non-negotiable for certification.

---

### Anti-Pattern 5: Acoustic Afterthought
**❌ BAD**: Designing rotor and motor geometry without noise analysis, then trying to fix acoustics after PDR
**✅ GOOD**: Acoustic targets must be design requirements from Day 1:
```
Design requirement example:
- Maximum tip speed at hover: 170 m/s (limits BPF amplitude)
- Blade count ≥ 5 per rotor (reduces per-blade loading, reduces BPF tonal prominence)
- Non-integer blade count ratios between rotors (avoids synchronous noise superposition)
- Motor switching frequency > 15 kHz (above human hearing sensitivity peak range)
```
Retrofitting noise fixes after blade molds are cut adds 12-18 months of schedule.

---

