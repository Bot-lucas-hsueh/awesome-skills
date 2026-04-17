## § 6 — Professional Toolkit

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Qiskit** | IBM's full-stack quantum SDK; transpiler, pulse, runtime | Circuit design targeting IBM hardware; CLOPS benchmarking |
| **Cirq** | Google's quantum circuit library; native to Sycamore topology | Google hardware experiments; custom gate definitions |
| **PennyLane** | Differentiable quantum computing; automatic differentiation for VQE/QML | Gradient-based variational optimization; quantum ML models |
| **Qiskit Runtime (Sampler/Estimator)** | Serverless QPU access with error mitigation built-in | Production VQE/QAOA runs on IBM Quantum |
| **Mitiq** | Open-source error mitigation library (ZNE, PEC, CDR) | Applying ZNE/PEC to any circuit framework |
| **TensorCircuit** | TensorFlow/JAX-backend quantum simulator | Large-scale tensor network simulation; GPU acceleration |
| **QuTiP** | Quantum toolbox in Python; Lindblad master equation | Noise modeling; open quantum system simulation |
| **PyQuil + Quil** | Rigetti's quantum instruction language | Rigetti QPU experiments; pulse-level control |
| **Amazon Braket SDK** | Multi-hardware access (IonQ, Rigetti, OQC) | Hardware-agnostic algorithm testing |
| **Q# + Azure Quantum** | Microsoft's quantum language with resource estimation | Fault-tolerant algorithm resource counting (T-gate count) |
| **Classiq** | High-level quantum algorithm synthesis | Automated circuit synthesis from functional specifications |
| **Stim** | Fast Clifford/stabilizer circuit simulator | Surface code simulation; error correction threshold analysis |

---
