## § 10 — Common Pitfalls

### Anti-Pattern 1: Quoting T1 from a Single Cooldown

❌ BAD:
```
"Our qubit has T1 = 200 μs"
# Measured once, on Monday, at one operating point
```

✅ GOOD:
```python
# T1 statistics across multiple cooldowns and operating points
t1_measurements = {
    "cooldown_1": [185, 192, 178, 203, 196],  # μs, 5 measurements
    "cooldown_2": [168, 175, 181, 170, 177],
    "cooldown_3": [210, 215, 198, 205, 212],
}
import numpy as np
all_t1 = [v for vals in t1_measurements.values() for v in vals]
print(f"T1 = {np.mean(all_t1):.1f} ± {np.std(all_t1):.1f} μs "
      f"(n={len(all_t1)} across {len(t1_measurements)} cooldowns)")
```

**Why it matters**: T1 fluctuates due to TLS drifts, quasiparticle activity, and flux noise. A single measurement is not reproducible science; report mean ± std across cooldowns.

---

### Anti-Pattern 2: Calibrating DRAG Without Leakage Verification

❌ BAD:
```python
# Tune β to minimize ALLXY error, declare gate calibrated
beta_optimal = minimize_allxy(beta_range)
print(f"Gate calibrated with β={beta_optimal}")
# Never check |2⟩ state population
```

✅ GOOD:
```python
beta_optimal = minimize_allxy(beta_range)
# Verify leakage is actually suppressed
L1 = run_leakage_rb(beta=beta_optimal)
if L1 > 0.001:  # > 0.1% leakage per gate
    print(f"WARNING: Leakage L1={L1:.4f} exceeds threshold. "
          "Reduce gate speed or re-optimize β with leakage-sensitive metric.")
else:
    print(f"Gate calibrated: β={beta_optimal:.3f}, L1={L1:.5f} ✓")
```

**Why it matters**: ALLXY detects coherent gate errors but is insensitive to leakage to |2⟩. Leakage accumulates invisibly and corrupts multi-qubit algorithms; only leakage-sensitive RB reveals it.

---

### Anti-Pattern 3: Ignoring Purcell Decay in Readout Design

❌ BAD:
```
# Design: qubit at 5 GHz, resonator at 6 GHz, g/2π = 100 MHz
# "Coupling is in dispersive regime since g/Δ = 0.1 ≪ 1"
# Deploy without calculating Purcell rate
```

✅ GOOD:
```python
# Purcell decay rate calculation
g_2pi = 100e6    # Hz, qubit-resonator coupling
Delta_2pi = 1e9  # Hz, qubit-resonator detuning (Δ/2π = 1 GHz)
kappa_2pi = 10e6 # Hz, resonator linewidth

gamma_purcell = (g_2pi
T1_purcell = 1

print(f"Purcell decay rate: {gamma_purcell/1e3:.1f} kHz")
print(f"Purcell-limited T1: {T1_purcell*1e6:.1f} μs")

# Add Purcell filter if T1_purcell < target T1
if T1_purcell < 100e-6:
    print("WARNING: Purcell decay limits T1 < 100 μs. "
          "Install bandpass Purcell filter or increase Δ.")
```

**Why it matters**: Purcell decay can limit T1 to tens of microseconds even with perfect substrate. Always compute Purcell rate before finalizing qubit-resonator geometry.

---

### Anti-Pattern 4: Skipping Simultaneous RB for Multi-Qubit Crosstalk

❌ BAD:
```
# Run RB on each qubit individually → all pass < 0.1% EPC
# Report multi-qubit system ready for algorithms
# Never check crosstalk under simultaneous operation
```

✅ GOOD:
```python
# Individual RB: baseline per-qubit performance
epc_individual = {q: run_rb(qubit=q) for q in range(5)}

# Simultaneous RB: all qubits driven concurrently
epc_simultaneous = run_simultaneous_rb(qubits=range(5))

# Flag crosstalk
for q in range(5):
    ratio = epc_simultaneous[q]
    if ratio > 1.5:
        print(f"WARNING: Qubit {q} EPC degraded {ratio:.1f}× under simultaneous "
              "operation → crosstalk detected. Check frequency crowding and ZZ coupling.")
    else:
        print(f"Qubit {q}: simultaneous/individual ratio = {ratio:.2f} ✓")
```

**Why it matters**: ZZ coupling and spectral crowding cause qubit errors to spike 2–10× when neighboring qubits are driven simultaneously. Algorithms fail even if individual qubit RB passes.

---

### Anti-Pattern 5: Confusing T2* and T2 in Noise Analysis

❌ BAD:
```
"T2 = 30 μs from Ramsey experiment. Qubit is dephasing-limited."
# Used Ramsey (measures T2*), reported as T2 (Hahn echo)
# Cannot distinguish slow vs fast noise without echo
```

✅ GOOD:
```python
def analyze_dephasing(T1_us, T2star_us, T2_echo_us):
    """Decompose dephasing into pure dephasing and T1-related contributions."""
    # 1/T2* = 1/(2T1) + 1/Tphi_star  (includes slow noise)
    # 1/T2  = 1/(2T1) + 1/Tphi_echo  (slow noise refocused)
    Tphi_star = 1 / (1/T2star_us - 1/(2*T1_us))
    Tphi_echo = 1 / (1/T2_echo_us - 1/(2*T1_us))

    print(f"T1 = {T1_us} μs")
    print(f"T2* = {T2star_us} μs (Ramsey) → Tφ* = {Tphi_star:.1f} μs")
    print(f"T2 = {T2_echo_us} μs (Echo)  → Tφ_echo = {Tphi_echo:.1f} μs")
    if Tphi_star < 0.5 * Tphi_echo:
        print("→ Low-frequency (DC) noise dominant: charge jumps or slow flux drift")
    else:
        print("→ High-frequency noise dominant: thermal photons or TLS at qubit frequency")

analyze_dephasing(T1_us=80, T2star_us=30, T2_echo_us=65)
```

**Why it matters**: T2* includes low-frequency noise that echo refocuses; T2 retains only the non-refocusable component. The ratio T2/T2* diagnoses whether noise is below (charge jumps, flux drift) or above the echo bandwidth (photon shot noise, TLS). The wrong diagnosis leads to ineffective remediation.

---

### Anti-Pattern 6: Reporting Readout Fidelity Without Accounting for T1 During Measurement

❌ BAD:
```
"Readout fidelity = 99.5% (average of P(0|0) and P(1|1))"
# Measured with 2 μs readout pulse, T1 = 80 μs
# Ignored T1 decay contribution to |1⟩→|0⟩ misassignment
```

✅ GOOD:
```python
def corrected_readout_fidelity(P_0given0, P_1given1, T1_us, t_readout_us):
    """
    Account for T1 decay during readout window.
    During readout, |1⟩ decays with probability 1 - exp(-t_ro/T1),
    contributing to false |0⟩ assignments.
    """
    t1_decay_during_readout = 1 - np.exp(-t_readout_us
    P_1given1_corrected = P_1given1
    F_avg = (P_0given0 + P_1given1_corrected)
    print(f"Raw F_avg = {(P_0given0 + P_1given1)/2:.4f}")
    print(f"T1-corrected F_avg = {F_avg:.4f}")
    print(f"T1 decay contribution: {t1_decay_during_readout*100:.2f}% of |1⟩ misassigned")
    return F_avg

corrected_readout_fidelity(P_0given0=0.998, P_1given1=0.991, T1_us=80, t_readout_us=2.0)
```

**Why it matters**: With T1 = 80 μs and 2 μs readout, ~2.5% of |1⟩ states decay during measurement, inflating apparent readout error. Disentangling T1-induced misassignment from genuine readout error requires corrected analysis.

---

