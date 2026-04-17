## § 8 · Standard Workflow

### Phase 1 — QKD Link Feasibility Assessment

**Steps:**
1. Define link parameters: distance L (km), fiber type (SMF-28: 0.2 dB/km at 1550 nm), connector losses, required secret key rate SKR_target.
2. Select protocol: BB84 for mature deployment, MDI-QKD for untrusted-node topology, TF-QKD for >300 km without repeaters, CV-QKD for high-rate metropolitan links.
3. Model optical loss: total_loss_dB = L * 0.2 + n_connectors * 0.3 + detector_coupling_loss.
4. Estimate secret key rate using decoy-state BB84:
   - Compute signal and decoy photon detection rates
   - Estimate single-photon contribution Q_1 and phase error rate e_1 via decoy analysis
   - Apply: SKR ≈ Q_1 * [1 - h(e_1)] - Q_signal * f_EC * h(QBER)
5. Verify finite-key security: block size N > 10^6; compute epsilon via Chernoff bounds.

**[Done]** criteria: SKR > SKR_target; QBER modeled below threshold; finite-key N feasible in target operation window.
**[FAIL]** criteria: Loss > 60 dB (detection events < 1 Hz) — link requires quantum repeater or satellite relay.

### Phase 2 — Hardware Specification and Procurement

**Steps:**
1. Specify photon source: SPDC (PPKTP, BBO) for entanglement-based; attenuated laser with decoy states (WCP: 3-state decoy: mu, nu, omega) for prepare-and-measure.
2. Specify detectors: SNSPD for long-haul (η > 90%, dark count < 100 cps, jitter < 50 ps); InGaAs APD for <50 km cost-sensitive links (η ~ 20%, dark count < 10^4 cps).
3. Design timing electronics: synchronization clock distribution with <10 ps stability; FPGA-based coincidence logic for entanglement-based QKD.
4. Specify quantum memory (if repeater node): AFC protocol with Pr:YSO or Eu:YSO crystals; characterize storage efficiency (target >50%) and retrieval fidelity (target >95%).
5. Plan classical post-processing hardware: dedicated FPGA or secure enclave for LDPC decoding and privacy amplification; minimum throughput 10x raw photon rate.

**[Done]** criteria: Hardware specifications meet protocol requirements; vendor datasheets verified against performance model.
**[FAIL]** criteria: SNSPD efficiency < 80% or timing jitter > 100 ps — respecify detector or switch to InGaAs + shorter link.

### Phase 3 — Post-Processing Pipeline Deployment and Key Management Integration

**Steps:**
1. Implement sifting: discard mismatched basis measurements (BB84: ~50% sifting efficiency with random basis choice; BB84 with biased basis: >90% efficiency).
2. Deploy error correction: Cascade algorithm for low-QBER links; LDPC codes for high-throughput (target: reconciliation efficiency f < 1.05, approaching Shannon limit).
3. Implement privacy amplification: universal hash function (Toeplitz matrix seeded from fresh randomness); compress sifted key by security factor s = n * (1 - h(QBER) - h(e_phase)).
4. Authenticate classical channel: CRYSTALS-Dilithium (NIST PQC Level 3) for bootstrapping; transition to QKD-derived symmetric MAC once key is established.
5. Integrate with Key Management System (KMS): ETSI GS QKD 004 REST API; connect to application layer encryption (AES-256-GCM one-time pad or key refresh).
6. Deploy QBER monitoring: continuous real-time QBER tracking; automated abort and alarm at threshold crossing; log all anomalies for side-channel analysis.

**[Done]** criteria: End-to-end secret key rate meets design target; NIST SP 800-22 randomness tests passed on 1 GB key sample; ETSI QKD 004 API integration tested.
**[FAIL]** criteria: LDPC frame error rate > 10^-5 — check QBER model; increase block size or switch to Cascade for robustness.

---

