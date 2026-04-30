## § 8 · Standard Workflow

### 8.1 Constitutional AI Implementation

```
Phase 1: Principle Design
├── Gather diverse stakeholder input on values and edge cases
├── Draft constitutional principles (10-20 high-level statements)
├── Test principles on held-out scenarios for ambiguity
└── ✓ Pass: Principles cover >90% of safety scenarios
    ✗ Fail: Revise principles; identify coverage gaps

Phase 2: Critique-Revision Training
├── Train critique model to evaluate outputs against constitution
├── Train revision model to improve based on critique
├── Validate AI feedback quality against human preferences
└── ✓ Pass: AI preferences correlate >85% with human judgments
    ✗ Fail: Iterate critique model; add constitutional examples

Phase 3: RLAIF Integration & Deployment
├── Generate preference dataset using constitutional critique
├── Train policy with RL from AI Feedback (RLAIF)
├── Red-team for specification gaming and reward hacking
└── ✓ Pass: No critical failures in adversarial testing
    ✗ Fail: Return to Phase 2; strengthen constitution
```

### 8.2 Mechanistic Interpretability Investigation

```
Step 1: Behavioral Observation — Document capability/behavior to explain
Step 2: Activation Analysis — Identify components (heads, neurons) that correlate
Step 3: Causal Intervention — Use activation patching to verify necessity
Step 4: Circuit Tracing — Map information flow through the model
Step 5: Uncertainty Quantification — Document what remains unexplained
```

### 8.3 RSP Compliance Workflow

```
Pre-Training: Define ASL target; ensure safety investment proportional to capability
├── During Training: Continuous capability evaluation; checkpoint safety reviews
├── Pre-Deployment: Full ASL evaluation; red-teaming; security audit
├── Deployment Decision: Conditional on meeting all ASL requirements
└── Post-Deployment: Continuous monitoring; incident response protocols
```

---
