## § 7 · Standards & Reference

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

## Phase 1 — Privacy Threat Modeling (LINDDUN)

**[Step 1] Asset Inventory**
- Enumerate all data assets: types, classification, data subject categories.
- Map all data flows: ingestion, processing, transmission, storage, deletion.
- Identify all parties: data owners, processors, sub-processors, recipients.
- `[✓ Done]` DFD (Data Flow Diagram) produced with trust boundaries marked.
- `[✗ FAIL]` Any data flow lacks identified controller or processor.

**[Step 2] LINDDUN Threat Elicitation**
- Apply each LINDDUN category to each DFD element.
- Score threats by likelihood x impact using DREAD or STRIDE-equivalent.
- Prioritize: Linkability and Identifiability threats are typically highest risk.
- `[✓ Done]` Threat register contains >= 1 entry per LINDDUN category per DFD element.
- `[✗ FAIL]` Any DFD element has zero associated threats (missed coverage).

**[Step 3] Technology Selection**
- For each HIGH/CRITICAL threat: select countermeasure from {DP, HE, SMPC, ZKP, TEE}.
- Validate selection against performance budget (Gate 4) and regulatory scope (Gate 5).
- Document selection rationale in ADR with explicit adversarial model.
- `[✓ Done]` Each threat has assigned countermeasure with adversarial model documented.
- `[✗ FAIL]` Countermeasure selected without explicit adversary model (semi-honest/malicious).

**[Step 4] DPIA Production**
- Draft DPIA per GDPR Art. 35 if processing is high-risk.
- Include: purpose, necessity, proportionality, risks, countermeasures, residual risk.
- `[✓ Done]` DPIA reviewed by DPO and legal counsel; residual risk accepted in writing.
- `[✗ FAIL]` DPIA omits description of technical countermeasures with effectiveness assessment.

---

### Phase 2 — TEE Deployment Pipeline

**[Step 1] Enclave Design**
- Define trusted computing base (TCB): minimize code in enclave.
- Separate secret-handling from business logic; implement host/enclave interface.
- Perform SGX threat model: identify which SGX attack classes apply (side-channel, rollback, Iago).
- `[✓ Done]` Enclave code < 10K LOC (TCB minimized); interface surface documented.
- `[✗ FAIL]` Entire application inside enclave (unnecessary TCB expansion).

**[Step 2] Remote Attestation Implementation**
- Implement DCAP (Data Center Attestation Primitives) or EPID attestation.
- Verify quote signature chain to Intel Attestation Service or local PCCS.
- Bind attestation to session key for secure channel establishment.
- `[✓ Done]` Attestation verified before any secret injected into enclave; session key bound.
- `[✗ FAIL]` Attestation is "optional" or skipped in any environment (including staging).

**[Step 3] Side-Channel Hardening**
- Apply all Intel-recommended microcode patches; verify with sgx-stest.
- Implement constant-time algorithms for cryptographic operations in enclave.
- Evaluate memory access pattern leakage; apply ORAM if access pattern is sensitive.
- `[✓ Done]` Patch level verified; constant-time implementations audited; ORAM analysis documented.
- `[✗ FAIL]` Secret-dependent branches or memory accesses present in enclave code.

**[Step 4] Sealed Storage & Key Management**
- Use SGX seal with MRSIGNER or MRENCLAVE policy per confidentiality requirement.
- Implement key rotation: sealed keys must have expiry and re-sealing procedure.
- Document key escrow procedure for enclave migration and disaster recovery.
- `[✓ Done]` Sealed storage policy documented; rotation procedure tested; escrow procedure approved.
- `[✗ FAIL]` Keys sealed to MRENCLAVE with no migration procedure (bricking risk on enclave update).

---
