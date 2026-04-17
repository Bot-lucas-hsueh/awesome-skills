## § 4 · Core Philosophy

### 4.1 The Safety Stack

```
        ┌──────────────────────────────────┐
        │   GOVERNANCE & POLICY            │  EU AI Act · NIST AI RMF · RSPs
        │   (when & how to deploy)         │
      ┌─┴──────────────────────────────────┴─┐
      │   EVALUATION & AUDITING              │  Red-team · Benchmarks · Audits
      │   (does it behave safely?)           │
    ┌─┴──────────────────────────────────────┴─┐
    │   ALIGNMENT TRAINING                      │  RLHF · DPO · Constitutional AI
    │   (shaping model behavior)               │
  ┌─┴──────────────────────────────────────────┴─┐
  │   INTERPRETABILITY                            │  SAE · Causal tracing · Circuits
  │   (understanding internal mechanisms)        │
  └──────────────────────────────────────────────┘
```

Each layer must be addressed: training alone is insufficient without evaluation; evaluation without governance lacks deployment guardrails.

### 4.2 Guiding Principles

1. **Empirical First**: Safety claims require empirical evidence — attack success rates, benchmark scores, activation-level evidence; not intuition or model card assertions

2. **Adversarial Stress-Testing**: Every safety property must be stress-tested by an adversary; uncontested safety is unvalidated safety

3. **Defense in Depth**: No single safety layer is sufficient; combine alignment training + output filters + monitoring + governance

---

