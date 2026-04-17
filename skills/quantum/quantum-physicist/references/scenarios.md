## § 9 — Scenario Examples

### Scenario A — Diagnosing Sudden T1 Drop After Cooldown

**User**: Our 5-qubit chip had T1 > 80 μs last cooldown. After remounting, T1 dropped to 15 μs on 3 qubits. What happened?

**Expert**: This is a classic multi-cause failure. Here is a systematic diagnostic:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# T1 measurement data (simulated)
times = np.linspace(0, 200e-6, 50)  # 0 to 200 μs

def t1_decay(t, T1, A, offset):
    return A * np.exp(-t

# Fit T1 from inversion recovery data
def fit_t1(times, populations):
    popt, pcov = curve_fit(t1_decay, times, populations,
                           p0=[50e-6, 0.9, 0.05],
                           bounds=([0, 0.5, 0], [1e-3, 1.0, 0.2]))
    T1_fit = popt[0]
    T1_err = np.sqrt(pcov[0, 0])
    return T1_fit, T1_err

# Diagnostic checklist (automated where possible)
diagnostic_checks = {
    "thermal_photons": "Measure qubit excited population at thermal eq. > 1% → warm stage issue",
    "tls_frequency_dependence": "Sweep qubit frequency; if T1 has sharp dips → TLS bath",
    "quasiparticle": "Check T1 vs temperature 10-50 mK; if T1 ∝ T^(-1) → QP poisoning",
    "purcell_filter": "Verify readout resonator bandwidth κ/2π; Purcell: 1/T1 ~ (g/Δ)²·κ",
    "wiring_change": "Compare cable/attenuator configuration to previous cooldown log"
}

for check, description in diagnostic_checks.items():
    print(f"[CHECK] {check}: {description}")
```

**Root cause priority order**:
1. **Thermal photons** (most common after remounting): Check if qubit excited-state population in thermal equilibrium jumped from 0.5% → 5%. Fix: Add 20 dB cold attenuator at 4K stage on drive lines.
2. **New TLS from surface contamination**: Qubit frequency may now be near a TLS resonance. Fix: Sweep ωq by flux tuning; if T1 varies >3× across 50 MHz, surface treatment needed.
3. **Quasiparticle poisoning**: Vortex trapping from imperfect shielding or stray magnetic flux. Fix: Improve mu-metal shielding; add infrared filter at cold plate stage.
4. **Purcell enhanced decay**: If readout resonator Q changed due to connector damage. Fix: Re-measure resonator Q_internal; check SMA connector torque specification (1 N·m).

---

### Scenario B — DRAG Pulse Calibration for 99.9% Single-Qubit Gate

**User**: How do I implement and calibrate DRAG pulses to reduce leakage errors below 0.05%?

**Expert**: DRAG (Derivative Removal via Adiabatic Gate) adds a quadrature component to cancel leakage to |2⟩. Here is the complete calibration protocol:

```python
import numpy as np
from scipy.optimize import minimize_scalar

# DRAG pulse definition
def drag_pulse(t, t_gate, Omega_max, beta, sigma):
    """
    Gaussian DRAG pulse:
    I(t) = Omega_max * exp(-t²/2σ²)  [in-phase]
    Q(t) = -beta * dI/dt              [quadrature, corrects leakage]
    """
    gaussian = Omega_max * np.exp(-t**2
    d_gaussian = -t
    return gaussian, -beta * d_gaussian

# DRAG parameter sweep via ALLXY protocol
# 21 gate combinations; ideal output sequence:
allxy_ideal = [1, 1, 0.5, 0.5, 0.5, -1, -1, -0.5, 0.5, -0.5,
               0.5, -0.5, 0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5]

def allxy_cost(beta_drag, pulse_simulator):
    """Minimize deviation from ideal ALLXY pattern to find optimal DRAG β."""
    measured = pulse_simulator.run_allxy(beta=beta_drag)
    return np.sum((np.array(measured) - np.array(allxy_ideal))**2)

# Leakage-sensitive RB to verify |2⟩ suppression
def leakage_rb(n_cliffords, n_sequences, backend):
    """
    Standard RB measures P(|0⟩ + |1⟩) decay.
    Leakage RB additionally tracks P(|2⟩) to extract leakage rate L1.
    """
    results = []
    for m in n_cliffords:
        leakage_sum = 0
        for _ in range(n_sequences):
            sequence = generate_random_clifford_sequence(m)
            counts = backend.run(sequence, shots=1024)
            # |2⟩ population measured via ancilla-sensitive readout or cavity photon number
            L1 = counts.get('2', 0)
            leakage_sum += L1
        results.append(leakage_sum
    return results

# Target specifications
print("DRAG Calibration Targets:")
print(f"  ALLXY residual < 0.02 (arbitrary units)")
print(f"  Leakage L1 < 0.05% per gate")
print(f"  Single-qubit EPC < 0.1% from standard RB")
print(f"  β_DRAG optimal: typically 0.3–0.8 × (1/anharmonicity) in ns")
```

**Calibration procedure**:
1. Fix pulse duration t_gate = 20–40 ns (shorter = less dephasing, more leakage risk)
2. Calibrate π amplitude via Rabi oscillation
3. Sweep β_DRAG from −1 to +1 (units of 1/MHz); run ALLXY at each β
4. Select β minimizing ALLXY deviation
5. Confirm with leakage-sensitive RB: L1 < 0.05% per gate verifies suppression
6. Run standard RB: EPC < 0.1% confirms overall gate quality

---

### Scenario C — Surface Code Stabilizer Measurement Implementation

**User**: How do I implement a weight-4 stabilizer measurement for a surface code patch and estimate the syndrome extraction fidelity threshold?

**Expert**: Surface code stabilizer circuits require ancilla qubits measuring 4-body Pauli operators. Here is the hardware implementation:

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def surface_code_plaquette_measurement(plaquette_type='Z'):
    """
    Weight-4 stabilizer measurement circuit for surface code.
    Uses 1 ancilla + 4 data qubits in standard cross arrangement.
    Ancilla: a | Data: d0, d1, d2, d3 (NW, NE, SW, SE)
    """
    qr_ancilla = QuantumRegister(1, 'a')
    qr_data = QuantumRegister(4, 'd')
    cr = ClassicalRegister(1, 'syndrome')
    qc = QuantumCircuit(qr_ancilla, qr_data, cr)

    if plaquette_type == 'Z':
        # Z-type stabilizer: measure ZZZZ = ancilla in |+⟩ basis, CNOT from data
        qc.h(qr_ancilla[0])
        for i in range(4):
            qc.cx(qr_ancilla[0], qr_data[i])
        qc.h(qr_ancilla[0])
    else:
        # X-type stabilizer: measure XXXX = ancilla in |0⟩, CNOT to data
        for i in range(4):
            qc.cx(qr_data[i], qr_ancilla[0])

    qc.measure(qr_ancilla[0], cr[0])
    return qc

# Syndrome fidelity threshold calculation
def syndrome_extraction_fidelity(p_gate_1q, p_gate_2q, p_readout, n_cnot=4):
    """
    Estimate effective syndrome measurement error probability.
    Each weight-4 stabilizer uses 4 CNOTs + 2 Hadamards + 1 readout.
    """
    p_hadamard = p_gate_1q
    p_syndrome_error = (
        2 * p_hadamard +          # H gates on ancilla
        n_cnot * p_gate_2q +      # 4 CNOT gates
        p_readout                  # ancilla measurement
    )
    return p_syndrome_error

# Surface code threshold analysis
for p_phys in [0.001, 0.005, 0.01, 0.015]:
    p_syn = syndrome_extraction_fidelity(p_phys, p_phys, p_phys * 2)
    threshold = 0.01  # ~1% for standard depolarizing model
    status = "✓ below threshold" if p_phys < threshold else "✗ above threshold"
    print(f"p_physical={p_phys:.3f} → p_syndrome≈{p_syn:.3f} | {status}")
```

**Threshold requirements**:
- Physical gate error rate p < 1% (depolarizing) for threshold operation
- Ancilla readout fidelity > 99% with < 500 ns measurement time (< T1/200)
- Syndrome extraction cycle time: 500 ns–2 μs depending on gate speed and readout time
- At d=5 surface code (25 data + 24 ancilla qubits): expect 10× logical error suppression per distance unit at p = 0.5%

---

