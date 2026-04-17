## 8. Standard Workflow

### 8.1 AI Red Team Exercise

```
Phase 1: Scoping & Authorization (范围确定与授权)
├── Define target AI system: model, API, agent, or full pipeline
├── Document rules of engagement: in-scope attack types, rate limits, authorized accounts
├── Identify safety impact: what happens if attack succeeds in production?
└── [✓ Done]: Written authorization + threat model complete
    [✗ FAIL]: No written authorization → halt all offensive testing

Phase 2: Reconnaissance (侦察)
├── Map AI attack surface: input modalities, output channels, tool integrations
├── Identify model family and training data indicators (behavioral fingerprinting)
├── Enumerate plugins/tools: what can the agent DO if compromised?
└── [✓ Done]: Attack surface diagram; tool permission inventory complete

Phase 3: Adversarial Probing (对抗探测)
├── LLM: Run Garak probes (50+ vulnerability detectors)
│   garak --model openai --model_type openai --probes all --report_prefix red_team
├── Classifiers: ART robustness evaluation (PGD-20 accuracy)
│   from art.attacks.evasion import ProjectedGradientDescent
│   attack = ProjectedGradientDescent(classifier, eps=0.3, eps_step=0.01, max_iter=20)
├── Data: Membership inference test (threshold attack)
└── [✓ Done]: Vulnerability inventory with ASR per attack type

Phase 4: Exploitation & Documentation (利用与文档)
├── Develop proof-of-concept for highest-ASR vulnerabilities
├── Capture evidence: attack inputs, model outputs, reproduction steps
├── STOP at first successful critical exploit; notify stakeholder immediately
└── [✓ Done]: Report: ASR table + PoC + remediation priority + compliance impact
    [✗ FAIL]: Critical safety impact found → immediate halt + emergency escalation
```

### 8.2 MLSecOps Pipeline Implementation

```
Stage 1: Data Security (数据安全)
├── Validate training data sources: provenance, integrity hash, license
├── Run data poisoning detection: compute influence scores for outliers
│   from torch_influence import AutogradInfluenceFunction
├── Implement DP data collection if GDPR/HIPAA applies
└── [✓ Done]: Data card complete; poisoning audit passed; legal basis documented

Stage 2: Training Security (训练安全)
├── Enable DP-SGD if privacy-sensitive training data
│   from opacus import PrivacyEngine
│   privacy_engine = PrivacyEngine(); ε tracked per epoch
├── Set gradient clipping (max_grad_norm=1.0) to limit memorization
├── Log all training hyperparameters + data versions (MLflow + DVC)
└── [✓ Done]: ε budget documented; no single training example memorized at > threshold

Stage 3: Model Artifact Security (模型制品安全)
├── Scan model file before registry upload
│   modelscan scan -p ./model.pkl
├── Sign model artifact (cosign or Sigstore)
├── Verify no backdoor: clean-label backdoor detection on model
└── [✓ Done]: ModelScan clean; signature verified; backdoor test passed

Stage 4: Deployment Security (部署安全)
├── Add input validation: Llama Guard + custom classifier
├── Add output filtering: Presidio PII filter + format validation
├── Implement rate limiting: token budget per user per minute
├── Enable monitoring: Evidently AI drift detection + anomaly alerts
└── [✓ Done]: All security controls active; dashboards live; alert thresholds set
```

---

