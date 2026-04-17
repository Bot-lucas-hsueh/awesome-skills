## § 3 · Risk Disclaimer

> IMPORTANT: Privacy-preserving computation systems handle some of the most
> sensitive data in existence. Errors in cryptographic parameters, DP
> calibration, or attestation verification can silently eliminate the privacy
> guarantee while the system appears to function correctly. Review all
> deployments with qualified cryptographers before production use.

| # | Risk | Severity | Domain | Mitigation |
|---|------|----------|--------|------------|
| 1 | **HE Performance Overhead** — Homomorphic encryption operations run 10x-1000x slower than plaintext; ciphertext expansion is 100x-10000x. Incorrect scheme selection can make a system operationally infeasible. | HIGH | Engineering | Profile circuit depth and multiplicative depth before scheme selection. Use CKKS for approximate arithmetic, BFV/BGV for exact integer arithmetic. Benchmark on representative workloads before committing. |
| 2 | **SGX Side-Channel Attacks** — Foreshadow (L1TF), SGAxe, Plundervolt, and cache-timing attacks can extract secrets from SGX enclaves even with valid attestation. Memory access patterns alone can leak sensitive data. | CRITICAL | Security | Apply ORAM for memory access pattern hiding; use constant-time implementations; apply all Intel microcode patches; consider AMD SEV-SNP or Enarx for workloads where SGX patch lag is unacceptable. |
| 3 | **Federated Learning Poisoning** — Malicious participants can submit poisoned model updates (model poisoning) or manipulate training to embed backdoors (backdoor attacks). Byzantine-robust aggregation is non-trivial. | HIGH | ML Security | Deploy Byzantine-robust aggregation (Krum, Bulyan, FLTrust); implement anomaly detection on update norms; use TEE-verified gradient submission where threat model warrants. |
| 4 | **Differential Privacy Misconfiguration** — Setting epsilon too high (>10) provides negligible protection; using naive composition instead of Renyi/zCDP accounting underestimates true privacy loss across rounds; incorrect sensitivity analysis invalidates all guarantees. | CRITICAL | Privacy | Always use formal DP accountants (OpenDP, Autodp); derive sensitivity from code analysis not intuition; document epsilon choice with threat model justification; have accountant reviewed by cryptographer. |
| 5 | **SMPC Communication Complexity** — Secure multi-party computation protocols require O(n^2) or higher communication rounds; with n > 10 parties or high-latency networks, round-trip costs dominate and latency becomes prohibitive. | HIGH | Engineering | Prototype with 3-5 parties on actual network topology before scaling; consider threshold HE as alternative for large n; use offline/online protocol phases (SPDZ-style) to amortize preprocessing cost. |
| 6 | **Key Management for Homomorphic Systems** — HE secret keys are long-lived and their compromise retroactively decrypts all ciphertexts. Key generation, storage, rotation, and escrow for HE systems require specialized HSM support. | CRITICAL | Operations | Store HE secret keys in FIPS 140-2 Level 3 HSMs; implement key rotation procedures with re-encryption protocol; never derive HE keys from password-based KDFs; audit key access logs continuously. |
| 7 | **Regulatory Uncertainty Around TEE Compliance** — Supervisory authorities (EDPB, ICO, CNIL) have not issued definitive guidance on whether TEE-processed data constitutes "processing" under GDPR or achieves "anonymization." Relying on TEE alone as a GDPR compliance mechanism carries legal risk. | HIGH | Regulatory | Do not position TEEs as anonymization; treat TEE-processed data as pseudonymized at best; layer TEE with DP or HE for stronger claims; engage DPA in pre-deployment consultation for high-risk use cases. |

---
