## § 4 · Core Philosophy

### 4.1 AI Security Attack Surface Model

```
┌─────────────────────────────────────────────────────────┐
│  AI System Attack Surface                                │
│                                                          │
│  [Training Pipeline]  [Model Artifact]  [Inference API]  │
│       ↓                    ↓                 ↓           │
│  Data Poisoning       Backdoor/Trojan    Prompt Injection │
│  Label Flipping       Weight Tampering   Jailbreaking     │
│  Adversarial Train    Serialization      Model Extraction │
│  Membership Inf.      IP Theft           DoS/Throttling   │
│       ↓                    ↓                 ↓           │
│  [MLOps Platform]  [Agent/Tool Layer]  [Output Channel]  │
│  Model Registry       Tool Injection     Output Filtering │
│  Experiment Track     Prompt Leakage     PII Exfiltration │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Every AI input is untrusted**: User prompts, retrieved documents, tool outputs, and API responses are all potential attack vectors; implement defense-in-depth validation at each boundary

2. **Measure robustness, don't assume it**: Adversarial accuracy on PGD-20 attacks is the benchmark, not clean accuracy; an untested model is an untrustworthy model

3. **Privacy budget is a finite resource**: Once differential privacy budget (ε) is exhausted, the model must be retrained; account for every query in formal DP accounting

---

