## 8. Standard Workflow

### 8.1 Phase 1: AI Opportunity Assessment

```
Step 1: User Pain Point Identification
├── Conduct problem interviews (not solution interviews)
├── Quantify pain: frequency × severity × addressable population
├── Map current workaround: what do users do today without AI?
└── [✓ Done]: Pain is validated with user research, not assumption
    [✗ FAIL]: Pain is hypothetical → conduct 10+ user interviews before proceeding

Step 2: AI Solvability Check (5 Gate Questions)
├── Gate 1: Is the problem well-defined enough for ML? (input/output clear?)
├── Gate 2: What is the cost of a wrong answer? (annoying / trust-damaging
├── Gate 3: Is there labeled data or a labeling strategy?
├── Gate 4: What accuracy level is "good enough" for the use case?
└── Gate 5: Is the problem actually solvable by rules/heuristics?
    [✓ Done]: All 5 gates passed; AI is appropriate; accuracy threshold defined
    [✗ FAIL]: Problem better solved deterministically → STOP; document why AI was rejected

Step 3: Data Availability Assessment
├── Inventory existing data: volume, quality, recency, coverage of edge cases
├── Identify labeling needs: how many labeled examples? at what cost?
├── Assess data privacy constraints: GDPR lawful basis, third-party data restrictions
└── [✓ Done]: Data plan defined with timeline, cost, and quality criteria
    [✗ FAIL]: Data gap >6 months to close → revisit priority vs. other AI opportunities

Step 4: Build / Buy
├── Core differentiation check: is AI capability a competitive moat?
├── Time-to-market vs. accuracy: API (3 weeks) vs. fine-tune (3 months) vs. build (12 months)
├── Cost at scale: model inference cost at projected query volume
└── [✓ Done]: Decision documented with trade-offs; stakeholder alignment confirmed
```

### 8.2 Phase 2: Product Design & Development

```
Step 1: AI UX Design
├── Design success state (AI correct) AND failure state (AI wrong
├── Define confidence threshold: above → show AI output; below → escalate to human
├── Choose AI UX pattern: Copilot suggestion / Autopilot action
└── [✓ Done]: UX design reviewed with human-AI interaction specialist; error path tested

Step 2: Success Metrics Definition
├── Primary: AI Adoption Rate (target: >30% in month 1)
├── Quality: AI Override Rate (target: <30%); AI Trust Score (track NPS)
├── Business: Time saved / revenue attributed
└── Guardrails: Latency P99 SLO; harmful output rate <0.1%; availability >99.9%

Step 3: Evaluation Framework Setup
├── Define offline evaluation benchmark and passing threshold (e.g., F1 > 0.85)
├── Set up shadow mode infrastructure: model runs on live traffic, output not shown to users
├── Define A/B test design: sample size, duration, primary + guardrail metrics
└── [✓ Done]: Evaluation pipeline implemented; baseline measurements captured

Step 4: Phased Rollout Plan
├── Phase 0: Shadow mode (2 weeks) — validate offline-online agreement >90%
├── Phase 1: 1% canary (3 days) — watch for anomalies in guardrail metrics
├── Phase 2: 10% → 50% → 100% (weekly gates) — confirm lift on primary metrics
└── [✓ Done]: Rollback plan documented; kill switch tested; on-call runbook written
    [✗ FAIL]: Shadow mode agreement <85% → investigate distribution shift before canary
```

### 8.3 Phase 3: Launch & Optimization

```
Step 1: Shadow Mode Validation
├── Compare model output vs. human decision
├── Measure agreement rate by segment (user type, use case, edge case)
├── Investigate disagreements: model error? labeling error? valid alternative?
└── [✓ Done]: Agreement rate >90%; failure modes understood and UX-handled

Step 2: User Feedback Integration
├── Instrument thumbs up/down and override signals from day 1
├── Weekly qualitative review of low-rated AI outputs (sample 50/week)
├── Segment feedback by user cohort: power users vs. new users vs. churned users
└── [✓ Done]: Feedback loop feeds model improvement pipeline within 30-day cycle

Step 3: Model Improvement Cycle
├── Review override signals as implicit negative labels for retraining
├── Identify underperforming segments (edge cases, domain gaps, demographic gaps)
├── Define retraining cadence: monthly for LLM fine-tunes; continuous for ranking models
└── [✓ Done]: Model improvement cycle documented; performance trend tracked weekly

Step 4: Responsible AI Review (ongoing)
├── Quarterly bias audit: measure disparate impact across protected attributes
├── Model drift monitoring: alert if accuracy drops >5% from launch baseline
├── Privacy review: confirm no PII leakage in model outputs (sample 100/week)
└── [✓ Done]: Responsible AI dashboard live; escalation path for ethics issues defined
```

---

