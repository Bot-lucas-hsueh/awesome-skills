## § 7 · Audit Sampling Methodology

### 7.1 Statistical vs Non-Statistical Sampling

| Aspect | Statistical Sampling | Non-Statistical Sampling |
|--------|---------------------|-------------------------|
| **Sample Size** | Calculated using probability theory | Based on professional judgment |
| **Selection Method** | Random, systematic, probability-proportional | Haphazard, block, directed |
| **Result Evaluation** | Objective, quantifiable sampling risk | Subjective, judgmental |
| **Documentation** | Statistical parameters documented | Judgment rationale documented |
| **Standards** | AU-C 530, AS 2301 | AU-C 530.A14 (judgment-based) |

### 7.2 Sample Size Calculation

**Attributes Sampling (Tests of Controls):**
```
Sample Size Formula (Simplified):

n = (Confidence Factor / Tolerable Deviation Rate) × (1 + Expected Deviation Rate)

Common Parameters (Big 4 Practices):
┌──────────────────┬──────────────────┬────────────────────┐
│ Confidence Level │ Tolerable Rate   │ Expected Deviations│
├──────────────────┼──────────────────┼────────────────────┤
│ 90%              │ 5% - 10%         │ 0                  │
│ 95%              │ 5%               │ 0                  │
│ 90-95%           │ 6-10%            │ 0-1                │
└──────────────────┴──────────────────┴────────────────────┘

Typical Sample Sizes: 25 (90%/10%/0) to 60 (95%/5%/0)
```

**Monetary Unit Sampling (Substantive Tests):**
```
Sample Size = (Book Value × Confidence Factor) / Tolerable Misstatement

Where:
- Confidence Factor from AICPA tables (Risk of Incorrect Acceptance)
- Tolerable Misstatement = Performance Materiality (typically 50-75% of PM)
```

### 7.3 Sampling Risk

| Type | Definition | Consequence |
|------|------------|-------------|
| **Risk of Overreliance** | Conclude controls more effective than they are | Insufficient substantive testing |
| **Risk of Underreliance** | Conclude controls less effective than they are | Excessive substantive testing |
| **Risk of Incorrect Acceptance** | Conclude balance not materially misstated when it is | Inappropriate audit opinion |
| **Risk of Incorrect Rejection** | Conclude balance materially misstated when it's not | Inefficient follow-up procedures |

---
