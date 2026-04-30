## § 3 — Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| Quantum advantage overclaim | HIGH | Misleads investment/research decisions; classical algorithms may outperform | Always benchmark against best classical baseline (e.g., QAOA vs Goemans-Williamson for MaxCut) |
| Circuit depth underestimation | HIGH | Circuit fidelity collapses on real hardware; results dominated by noise | Transpile to native gates and device topology; compute T1-limited depth budget |
| Barren plateau in variational circuits | HIGH | Optimizer stalls; exponentially vanishing gradients prevent VQE/QAOA training | Use hardware-efficient ansatz, parameter-shift gradients, layer-by-layer initialization |
| Error mitigation overhead | MEDIUM | ZNE/PEC can require 10-100x circuit repetitions, exceeding QPU time budget | Estimate shot overhead before committing; use CDR for low-depth circuits |
| Classical simulation limit | MEDIUM | Claiming "quantum simulation" of >50 qubits with statevector is computationally infeasible | Use tensor network or Clifford simulators; state simulation complexity explicitly |
| Hardware calibration drift | MEDIUM | Gate fidelities degrade between calibration cycles; results non-reproducible | Re-calibrate or use dynamical decoupling; timestamp all hardware runs |
| IP and patent risk in QC commercialization | CRITICAL | Patent landscape for quantum algorithms is complex; implementation may infringe | Consult IP counsel before commercializing; use open-source frameworks under Apache 2.0 |

---
