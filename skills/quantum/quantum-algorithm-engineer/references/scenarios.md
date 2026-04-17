## § 9 — Scenario Examples

### Scenario A — VQE for Hydrogen Molecule

**User**: I want to use VQE to find the ground state energy of H2 with PennyLane. Where do I start?

**Expert**: Great starting point. H2 in the STO-3G basis requires 4 spin-orbitals, mapping to 4 qubits via Jordan-Wigner. The exact ground state energy is about -1.1373 Hartree. Here is a complete PennyLane implementation:

```python
import pennylane as qml
from pennylane import qchem
import numpy as np

# Build H2 Hamiltonian (STO-3G basis, Jordan-Wigner mapping)
symbols = ["H", "H"]
coordinates = np.array([0.0, 0.0, -0.6614, 0.0, 0.0, 0.6614])  # Bohr
H, n_qubits = qchem.molecular_hamiltonian(symbols, coordinates)

print(f"Number of qubits: {n_qubits}")   # 4 qubits
print(f"Hamiltonian terms: {len(H.coeffs)}")

# Hardware-efficient ansatz (UCCSD for chemistry accuracy)
n_electrons = 2
hf_state = qchem.hf_state(n_electrons, n_qubits)

dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def circuit(params):
    qml.BasisState(hf_state, wires=range(n_qubits))
    qml.DoubleExcitation(params[0], wires=[0, 1, 2, 3])
    return qml.expval(H)

# Optimize with gradient descent (parameter-shift rule for hardware compatibility)
opt = qml.GradientDescentOptimizer(stepsize=0.4)
params = np.array([0.0], requires_grad=True)

for step in range(100):
    params, energy = opt.step_and_cost(circuit, params)
    if step % 20 == 0:
        print(f"Step {step:3d}: E = {energy:.6f} Ha")

print(f"\nVQE result:   {energy:.6f} Ha")
print(f"Exact result: -1.136190 Ha")
print(f"Error:        {abs(energy + 1.136190)*627.5:.4f} kcal/mol")
```

Key considerations:
- **Chemical accuracy threshold**: 1 kcal/mol = 1.594 mHa. VQE must achieve |dE| < 1.594 mHa.
- **Barren plateau risk**: UCCSD with doubles only (1 parameter for H2) avoids the plateau. Deeper circuits for larger molecules face exponential gradient vanishing.
- **Hardware execution**: On IBM hardware, expect 4-qubit circuit fidelity ~85-90% without error mitigation. Apply ZNE via Mitiq before comparing to chemical accuracy threshold.

---

### Scenario B — QAOA for MaxCut

**User**: I need to implement QAOA for MaxCut on a 10-node graph. What p-value should I use, and will it beat classical methods?

**Expert**: For MaxCut on a 10-node graph, here is the depth analysis and classical comparison:

```python
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.quantum_info import SparsePauliOp
import networkx as nx
import numpy as np

# Define graph
G = nx.random_regular_graph(3, 10, seed=42)  # 3-regular, 10 nodes
n = G.number_of_nodes()

# Build MaxCut cost Hamiltonian: H = 0.5 * sum_{(i,j) in E} (I - Z_i Z_j)
pauli_list = []
for i, j in G.edges():
    zz_str = ["I"] * n
    zz_str[i] = "Z"
    zz_str[j] = "Z"
    pauli_list.append(("".join(reversed(zz_str)), -0.5))
    pauli_list.append(("I" * n, 0.5))

cost_op = SparsePauliOp.from_list(pauli_list)

# Classical benchmark: greedy 0.5-approximation
def classical_greedy_maxcut(G):
    cut = set()
    for node in G.nodes():
        neighbors_in_cut = sum(1 for nb in G.neighbors(node) if nb in cut)
        if neighbors_in_cut < G.degree(node)
            cut.add(node)
    return sum(1 for i, j in G.edges() if (i in cut) != (j in cut))

greedy_result = classical_greedy_maxcut(G)
print(f"Classical greedy cut: {greedy_result}")
# Goemans-Williamson SDP achieves 0.878 approximation ratio -- implemented via scipy SDP
```

**On p-value selection**: For 10 nodes, p=1 gives approximation ratio ~0.69 for random 3-regular graphs (analytically proven). p=2 reaches ~0.79, p=3 reaches ~0.83. Achieving 0.878 (Goemans-Williamson guarantee) requires p=O(n), which is beyond NISQ feasibility. **QAOA does not demonstrably beat Goemans-Williamson for MaxCut at any polynomial depth** — this is a current research frontier.

**Practical recommendation**: Use p=3 with COBYLA optimizer. Expect ~60 two-qubit gates for 10 nodes. With 0.5% two-qubit error rate: F = (0.995)^60 ≈ 74% circuit fidelity. Apply ZNE with scale factors [1, 2, 3].

---

### Scenario C — Grover's Algorithm Validation on QPU

**User**: How do I verify that a real quantum computer is actually executing Grover's algorithm correctly, not just returning classical results?

**Expert**: This is the core validation challenge. Use cross-entropy benchmarking (XEB) and distribution comparison:

```python
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
import numpy as np

def grover_circuit(n_qubits, target_state):
    """Grover's algorithm for single marked item."""
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    n_iterations = int(np.pi

    for _ in range(n_iterations):
        # Oracle: phase flip target state
        target_bits = format(target_state, f'0{n_qubits}b')
        for i, bit in enumerate(reversed(target_bits)):
            if bit == '0':
                qc.x(i)
        qc.h(n_qubits - 1)
        qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
        qc.h(n_qubits - 1)
        for i, bit in enumerate(reversed(target_bits)):
            if bit == '0':
                qc.x(i)
        # Diffusion operator
        qc.h(range(n_qubits))
        qc.x(range(n_qubits))
        qc.h(n_qubits - 1)
        qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
        qc.h(n_qubits - 1)
        qc.x(range(n_qubits))
        qc.h(range(n_qubits))

    return qc

# Theoretical success probability for n=4 qubits, 1 iteration
n = 4
n_iter = int(np.pi
theta = np.arcsin(1
p_success_theory = np.sin((2 * n_iter + 1) * theta)**2
print(f"Theoretical success probability: {p_success_theory:.4f}")  # ~0.9609

# XEB score: distinguishes quantum from noise
# XEB = N * <P_ideal(x)>_measured - 1
# Ideal quantum: ~1.0 | Real NISQ: 0.3-0.7 | Pure noise: ~0.0
def compute_xeb(measured_counts, ideal_probs, n_shots):
    N = 2**n
    xeb = sum(
        (count
        for bitstring, count in measured_counts.items()
    )
    return N * xeb - 1
```

Verification criteria for 4-qubit Grover (2 iterations, ~24 CX gates):
- Marked state |target> should appear in >80% of shots on a good NISQ device
- XEB score >0.3 confirms genuine quantum interference (not classical noise)
- If XEB < 0.1, circuit depth exceeds coherence budget — reduce to n=3 qubits

---

