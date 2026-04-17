## § 10 — Common Pitfalls

### Anti-Pattern 1: Claiming Quantum Speedup Without Classical Baseline

❌ BAD:
```python
# "Our QAOA solves MaxCut faster than any classical method!"
result = qaoa.compute_minimum_eigenvalue(cost_operator)
print(f"QAOA found cut: {-result.eigenvalue:.2f}")
# No classical comparison provided
```

✅ GOOD:
```python
qaoa_cut = -qaoa.compute_minimum_eigenvalue(cost_operator).eigenvalue
gw_cut = goemans_williamson(G)          # 0.878 SDP approximation
optimal_cut = brute_force_maxcut(G)     # exact for small graphs

print(f"QAOA:              {qaoa_cut:.2f} ({qaoa_cut/optimal_cut:.3f} ratio)")
print(f"Goemans-Williamson: {gw_cut:.2f} ({gw_cut/optimal_cut:.3f} ratio)")
print(f"Optimal:           {optimal_cut:.2f}")
```

**Why it matters**: Quantum advantage claims without classical baselines are scientifically invalid. MaxCut QAOA at shallow depth consistently underperforms Goemans-Williamson.

---

### Anti-Pattern 2: Ignoring Transpilation Depth

❌ BAD:
```python
qc = QuantumCircuit(5)
qc.cx(0, 4)  # Long-range CX impossible on linear topology
# Claim: "circuit has depth 10" using abstract gate count
```

✅ GOOD:
```python
from qiskit.compiler import transpile
qc_transpiled = transpile(qc, backend=backend, optimization_level=3)
print(f"Abstract depth:   {qc.depth()}")
print(f"Transpiled depth: {qc_transpiled.depth()}")
print(f"CNOT count:       {qc_transpiled.count_ops().get('cx', 0)}")
print(f"SWAPs inserted:   {qc_transpiled.count_ops().get('swap', 0)}")
```

**Why it matters**: Long-range gates require SWAP chains that can triple effective depth. Always quote transpiled depth on target hardware topology.

---

### Anti-Pattern 3: Statevector Simulation Beyond 30 Qubits

❌ BAD:
```python
dev = qml.device("default.qubit", wires=50)
# 2^50 amplitudes = 1 petabyte RAM -- will crash or thrash memory
```

✅ GOOD:
```python
n_qubits = 50
if n_qubits <= 30:
    dev = qml.device("default.qubit", wires=n_qubits)
elif n_qubits <= 100:
    dev = qml.device("default.tensor", wires=n_qubits, max_bond_dim=64)
else:
    dev = qml.device("default.clifford", wires=n_qubits)  # stabilizer only
print(f"Using {dev.name} for {n_qubits} qubits")
```

**Why it matters**: Statevector requires 2^n complex128 amplitudes. At 50 qubits: 16 PB RAM. Always plan simulation strategy before designing experiments.

---

### Anti-Pattern 4: Barren Plateau Ignorance in Deep Ansatz

❌ BAD:
```python
# Random 50-layer ansatz -- gradients exponentially vanish ~10^-15
for layer in range(50):
    for i in range(n_qubits):
        qml.RY(params[layer, i], wires=i)
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
```

✅ GOOD:
```python
def gradient_variance_check(circuit, params, n_samples=100):
    grads = [qml.grad(circuit)(
        np.random.uniform(0, 2*np.pi, params.shape)
    ).flatten() for _ in range(n_samples)]
    var = np.var(grads, axis=0).mean()
    if var < 1e-6:
        print(f"WARNING: Barren plateau detected (var={var:.2e}). "
              "Reduce depth or use local cost function.")
    return var
```

**Why it matters**: Barren plateaus make gradient-based VQE training exponentially harder as system size grows. Detect early; switch to local cost functions or layer-by-layer training.

---

### Anti-Pattern 5: ZNE Without Validating Assumptions

❌ BAD:
```python
from mitiq import zne
result = zne.execute_with_zne(circuit, executor, scale_factors=[1, 3, 5])
# Report as "error-mitigated" without checking ZNE validity conditions
```

✅ GOOD:
```python
from mitiq import zne
result, metadata = zne.execute_with_zne(
    circuit, executor,
    scale_factors=[1, 2, 3],
    extrapolator=zne.RichardsonFactory([1, 2, 3]),
    return_metadata=True
)
scaled_results = metadata['unmitigated_results']
# Results must degrade monotonically with scale factor (higher noise = worse result)
if not all(scaled_results[i] >= scaled_results[i+1]
           for i in range(len(scaled_results)-1)):
    print("WARNING: ZNE extrapolation unreliable -- noise model mismatch")
```

**Why it matters**: ZNE assumes noise scales linearly with gate duration. This fails for coherent errors, leakage, and crosstalk. Blind application produces biased results with false confidence.

---

### Anti-Pattern 6: Misinterpreting Quantum Volume

❌ BAD:
```
"Our device has Quantum Volume 512, so it can solve 9-qubit problems perfectly."
```

✅ GOOD:
```
QV 512 = 2^9 means the device executes square circuits of 9 qubits x 9 layers
with heavy output probability >2/3.

QV does NOT mean:
- Arbitrary 9-qubit algorithms run at that fidelity
- Circuits deeper than 9 layers are reliable
- The device surpasses classical simulation for 9-qubit problems

Use CLOPS for throughput and per-gate RB error rates for circuit design budgeting.
QV is a marketing-friendly single number; engineering decisions need more detail.
```

**Why it matters**: QV is widely misquoted. A QV 512 device is still limited to shallow circuits; Shor's algorithm requires millions of fault-tolerant gates. Know what the benchmark actually measures.

---

