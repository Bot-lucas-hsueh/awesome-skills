## § 7 — Standards & Reference

**Frameworks**

- **IBM Quantum Volume (QV)**: Holistic single-number benchmark. QV = 2^n where n is the largest square circuit (n qubits, n layers) executed with heavy output probability >2/3. IBM Eagle: QV 512+.
- **CLOPS (Circuit Layer Operations Per Second)**: Measures QPU throughput. CLOPS = (M x K x S x D)
- **Randomized Benchmarking (RB)**: Extracts average Clifford gate fidelity via exponential decay F(m) = A·p^m + B. Error per Clifford (EPC) = (1-p)(1-1/2^n). Industry target: <0.1% two-qubit EPC.

**Metrics Table**

| Metric | Formula | Target Range | Notes |
|--------|---------|-------------|-------|
| Circuit Fidelity | F_circuit = product of all gate fidelities | >50% for useful results | Product of all gate fidelities |
| Two-qubit gate error | EPC_2Q = (1 - F_2Q) | <0.5% NISQ, <0.01% FT | Hardware calibration spec |
| T1 (relaxation time) | P(|1>,t) = exp(-t/T1) | >100 us superconducting | Limits gate depth |
| T2 (dephasing time) | Ramsey decay envelope | >50 us superconducting | Limits coherent operations |
| Quantum Volume | QV = 2^n (heavy output >2/3) | QV>=512 current NISQ | IBM benchmark standard |
| CLOPS | (M·K·S·D)
| Grover speedup | T_Grover = O(sqrt(N)) | Verified for unstructured search | vs O(N) classical |
| VQE energy error | dE = |E_VQE - E_exact| | <chemical accuracy: 1 kcal/mol | Convergence criterion |
| QAOA approximation ratio | r = C_QAOA

---

