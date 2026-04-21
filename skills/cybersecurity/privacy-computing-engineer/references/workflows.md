## 8. Standard Workflow

### Phase 1 — Privacy Threat Modeling (LINDDUN)

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
