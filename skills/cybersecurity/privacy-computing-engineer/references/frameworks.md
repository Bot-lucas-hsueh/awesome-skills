## 7. Standards & Reference

**NIST Privacy Framework (NIST PF 1.0) Functions:**

| Function | Core Activities | Privacy-Computing Relevance |
|----------|----------------|----------------------------|
| **Identify-P** | Inventory data processing; understand privacy risks | Run LINDDUN threat model; classify data assets; map data flows |
| **Govern-P** | Establish policies, roles, and accountability | Document ADRs with regulatory basis; assign data steward roles |
| **Control-P** | Apply data management policies; enable individual rights | Implement DP mechanisms; deploy access-controlled enclaves |
| **Communicate-P** | Maintain transparency with individuals | Publish privacy notices for federated participants; disclose DP epsilon to DPA |
| **Protect-P** | Secure data against unauthorized access | Deploy HE/SMPC/TEE; implement key management; pen-test attestation flows |

**LINDDUN Privacy Threat Taxonomy:**

| Threat | Example in Privacy Computing | Countermeasure |
|--------|------------------------------|----------------|
| **L**inkability | Linking model updates to data subjects | DP noise on gradients; secure aggregation |
| **I**dentifiability | Re-identifying individuals from statistics | k-anonymity + DP composition |
| **N**on-repudiation | Logging that enables retroactive profiling | Minimize logging; use anonymous credentials |
| **D**etectability | Detecting participation in federated learning | Padding + dummy updates |
| **D**isclosure of Information | HE decryption key compromise | HSM key storage; threshold decryption |
| **U**nawareness | Data subjects unaware of FL use of their data | Informed consent; DPIA publication |
| **N**on-compliance | DP epsilon not meeting regulatory threshold | Formal DP accounting; regulatory pre-approval |

**ISO/IEC 27701:** Privacy Information Management System extending ISO 27001;
maps to GDPR controller/processor obligations; requires privacy controls catalog,
DPIA procedures, and data subject rights workflows.

**Key Metrics with Target Ranges:**

| Metric | Symbol | Target Range | Notes |
|--------|--------|-------------|-------|
| DP Privacy Budget (epsilon) | epsilon | <= 1 (strong), <= 10 (moderate), > 10 (weak) | Lower is stronger; justify choice against threat model |
| DP Delta (failure probability) | delta | delta < 1/n^2 where n = dataset size | Typically 10^-5 to 10^-8 for production |
| HE Computation Overhead | — | 10x-1000x vs plaintext | CKKS multiplication: ~1ms-10ms per operation |
| HE Ciphertext Expansion | — | 100x-10000x raw data size | Budget storage and bandwidth accordingly |
| SGX Enclave Page Cache (EPC) | — | 128MB-512MB (hardware limited) | Exceeding EPC causes expensive page swaps |
| SMPC Communication Rounds | — | O(n) for GMW, O(1) amortized for SPDZ | Measure on actual network topology |
| Federated Rounds to Convergence | — | 100-10000 rounds (model dependent) | Each round adds DP composition cost |
| Noise Multiplier (DP-SGD) | sigma | sigma >= 0.5 for meaningful privacy | Tune with privacy accountant, not heuristics |

---
