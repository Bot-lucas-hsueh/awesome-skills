## § 7 Standard Workflow

See [references/08-workflow.md](references/08-workflow.md)

---

---

## Anti-Pattern 2: Insufficient Injector ΔP for Stability
**❌ BAD**: Designing injector with ΔP_inj = 5% of Pc to reduce pump power requirements
**✅ GOOD**: Minimum injector pressure drop for feed system coupled stability (chug prevention):
```
Rule of thumb: ΔP_injector ≥ 15% × Pc for stable combustion
  (Zucrow/Hoffman criterion for preventing low-frequency chug)

At ΔP_inj = 5% × Pc: high probability of chug at <50 Hz
At ΔP_inj = 15% × Pc: marginal stability
At ΔP_inj = 20-25% × Pc: stable for most configurations

Consequence of underestimating ΔP:
  → Turbopump power requirement is lower (good)
  → But combustion instability destroys engine (catastrophic)
```

---

### Anti-Pattern 3: Ignoring Cavitation in Turbopump Design
**❌ BAD**: Computing turbopump speed for peak efficiency without checking NPSH requirements
**✅ GOOD**: Always verify NPSH margin (NPSHa vs. NPSHr):
```
NPSHa (available NPSH) = (P_tank - P_vapor)
NPSHr (required NPSH) = empirical from turbopump Suction Specific Speed (Nss)

Required margin: NPSHa ≥ 1.5 × NPSHr (safety factor per NASASP-8120)

Cavitation failure modes:
  - Performance drop (5-20% before catastrophic)
  - Bubble collapse erosion → impeller pitting → structural failure
  - LOX cavitation → oxygen-rich turbopump → fire risk

If NPSHa < NPSHr: Reduce turbopump speed, add inducer, or increase tank pressure
```

---

### Anti-Pattern 4: Single-Point Combustion Stability Test
**❌ BAD**: Testing stability only at design point throttle and O/F
**✅ GOOD**: Stability must be demonstrated across the operating envelope:
```
Required stability test matrix:
  Throttle range: 50%, 75%, 90%, 100%, 110% rated thrust
  O/F range: -5%, nominal, +5% O/F
  Propellant temperature range: expected min/max
  Pressure variations: ±10% feed pressure

Bomb testing (pulse gun): introduce artificial perturbation
  → Measure recovery time and amplitude
  → Target: recovery within 20 ms (AIAA S-080 criterion)

Engine that is only tested at design point: unknowns at every off-nominal condition
```

---

### Anti-Pattern 5: No Abort Capability in Test Sequence
**❌ BAD**: Hot-fire test sequence with no automated abort on anomalous data
**✅ GOOD**: Every hot-fire test must have automated abort system:
```python
# Required abort triggers (example thresholds):
abort_conditions = {
    "chamber_pressure": {"max": 1.15 * Pc_nominal, "min": 0.85 * Pc_nominal},
    "turbopump_speed": {"max": 1.05 * N_rated},
    "vibration_rms": {"max": 50 * g_nominal},  # MOOG criterion: 50× baseline
    "coolant_temp_delta": {"max": T_coolant_out - T_coolant_in + 50},  # 50°C above nominal
    "leakage_flowrate": {"max": 0.1},  # kg/s leakage threshold
}

# Automated abort: CLD (command to shutdown) within 200ms of trigger
# Manual abort: Test conductor override always available
# Hard abort (explosive separation): For test stand protection
```

---

