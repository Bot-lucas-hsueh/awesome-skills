## § 2 · What This Skill Does

This skill provides four core capabilities for privacy-preserving computation:

**Capability 1 — Cryptographic Privacy Computation Design**
Architects and implements homomorphic encryption (BFV, CKKS, TFHE schemes),
secure multi-party computation (GMW, SPDZ, ABY protocols), and zero-knowledge
proof systems (Groth16, PLONK, STARKs). Selects the appropriate primitive based
on circuit depth, number of parties, malicious/semi-honest adversary model, and
latency requirements. Produces annotated circuit diagrams and noise budget
analysis for HE deployments.

**Capability 2 — Federated Learning with Formal Privacy Guarantees**
Designs federated learning architectures using PySyft, Flower, and FATE, then
layers differential privacy using OpenDP, TensorFlow Privacy, and Opacus with
formal Renyi DP or zCDP accounting. Prevents gradient inversion and membership
inference attacks. Validates that federation topology, aggregation protocol, and
DP mechanism jointly satisfy the stated privacy budget across all training rounds.

**Capability 3 — Trusted Execution Environment Deployment**
Deploys and audits Intel SGX enclaves (SGX SDK, Gramine, Occlum), AMD SEV-SNP
confidential VMs, and ARM TrustZone secure worlds using Enarx as a portable TEE
runtime. Implements remote attestation flows, sealed storage, and side-channel
hardening. Produces enclave threat models addressing Foreshadow, SGAxe, and
speculative execution leakage classes.

**Capability 4 — Regulatory Compliance Architecture**
Maps privacy-preserving architectures to GDPR Art. 25, EU AI Act risk tiers,
PIPL Chapter 4, HIPAA Safe Harbor, and ISO/IEC 27701 controls. Produces Data
Protection Impact Assessments (DPIAs), architecture decision records with
regulatory basis, and evidence packages for supervisory authority inquiries.
Distinguishes pseudonymization (Art. 4(5)) from anonymization under WP29/EDPB
guidance and applies the appropriate legal basis.

---
