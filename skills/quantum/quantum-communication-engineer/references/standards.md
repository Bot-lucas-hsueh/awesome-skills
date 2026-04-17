## § 7 · Standards & Reference

**Key Standards:**

| Standard | Scope | Key Requirements |
|----------|-------|-----------------|
| ETSI GS QKD 002 | Use cases and security requirements | Defines threat model, security parameters, deployment scenarios |
| ETSI GS QKD 004 | QKD API (key delivery interface) | REST API for key management; interoperability between QKD and KMS |
| ETSI GS QKD 007 | Security framework | Composable security definitions; side-channel characterization requirements |
| ETSI GS QKD 011 | Component characterization | Measurement methods for optical components; detector timing specs |
| ISO/IEC 23837 | QKD security requirements | International standard for QKD system security evaluation |
| ITU-T Y.3800 | Quantum communication network framework | Network architecture, functional requirements, terminology |
| NIST IR 8413 | Status of NIST post-quantum cryptography | Kyber, Dilithium, SPHINCS+ specifications for PQC migration |

**Protocol Security Metrics:**

| Protocol | QBER Threshold | SKR Formula | Key Assumptions |
|----------|---------------|-------------|-----------------|
| BB84 (decoy-state) | 11% (1-way) | R = Q_1*(1 - h(e_1)) - Q_mu*h(QBER) | Infinite-key, trusted source/detector |
| MDI-QKD | 8.3% | R = Q_11^Z * (1 - h(e_11^X)) - Q_mu_nu * f * h(QBER) | Untrusted detectors; trusted sources |
| TF-QKD | Phase QBER < 50% | R = (1/2) * Q_1 * (1 - h(e_ph)) - Q * h(QBER) | Single-photon interference at relay |
| CV-QKD (Gaussian) | SNR dependent | R = beta*I(A:B) - chi(B:E) | Trusted detector; Gaussian modulation |

**Performance Targets:**

| Metric | Target Value | Notes |
|--------|-------------|-------|
| QBER | < 3% normal operation | > 5% triggers alarm; > 11% abort (BB84) |
| Secret Key Rate | > 1 kbps at 100 km | Benchmark for metropolitan QKD |
| Detector Dark Count Rate | < 100 cps (SNSPD) | InGaAs: < 10^4 cps at 10% efficiency |
| SNSPD Efficiency | > 90% at 1550 nm | System detection efficiency including coupling losses |
| Memory Coherence T2 | > 1 ms for 100-km node spacing | Pr:YSO: T2 up to 6 hours with spin-echo |
| Entanglement Fidelity | > 90% after distribution | Threshold for productive entanglement purification |
| Finite-key security parameter | epsilon < 10^-10 | Composable security framework requirement |

---
