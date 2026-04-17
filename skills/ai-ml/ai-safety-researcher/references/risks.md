## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Dual-Use Attack Info** | 🔴 Critical | Detailed jailbreak payloads or attack vectors could be misused by malicious actors | Only share attack methodology at the conceptual level; never provide working exploit payloads beyond published research |
| **Alignment Overconfidence** | 🔴 High | Prematurely claiming a model is "aligned" before sufficient evaluation can create false safety guarantees | Require multi-domain red-team + behavioral eval + interpretability audit before safety claims |
| **Benchmark Overfitting** | 🟡 Medium | Models optimized for safety benchmarks (TruthfulQA, HarmBench) may still fail on real-world adversarial inputs | Always supplement benchmark eval with domain-specific red-teaming; treat benchmarks as necessary but not sufficient |
| **Governance Lag** | 🟡 Medium | EU AI Act
| **Interpretability Overreach** | 🟢 Low | Mechanistic interpretability findings may not generalize across model families or scales | Report findings with scope limitations; test at multiple model sizes and families |

**⚠️ IMPORTANT
- This skill provides research-grade guidance; it does not replace formal safety audits by accredited labs for high-stakes deployments

- Red-team findings must be disclosed responsibly; follow coordinated vulnerability disclosure (CVD) protocols

---
