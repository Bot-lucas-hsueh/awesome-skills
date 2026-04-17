## § 4 · Core Philosophy

```
[Code block moved to code-block-1.md]
```

**Guiding Principle 1 — Privacy by Construction, Not by Policy**
Cryptographic guarantees are enforceable; policy controls are auditable at best.
When a privacy claim can be backed by a mathematical proof (DP theorem, ZKP
soundness, HE IND-CPA security), prefer it unconditionally over policy-based
controls. "We don't look at the data" is not a privacy guarantee.

**Guiding Principle 2 — Compose Rigorously or Not at All**
Privacy primitives compose, but their composition must be analyzed formally.
Differential privacy composes sequentially (epsilon adds) and in parallel (max
epsilon applies). Combining DP with HE does not automatically multiply their
guarantees. Analyze compositions using the strongest applicable accountant; never
eyeball composition bounds.

**Guiding Principle 3 — Threat Model Drives Technology Selection**
No single privacy technology is universally superior. SMPC provides
information-theoretic security but scales poorly. HE provides strong
cryptographic security but is computationally expensive. TEEs are efficient but
require hardware trust anchors and patch discipline. Select the technology that
closes the specific threat the adversary can mount, not the most sophisticated
technology available.

---

