## § 8 · Standard Workflow

### Phase 1: Task Definition & Guideline Design

```
Input: Model capability gap or alignment objective
Output: Annotation guidelines v1.0 with calibration set

Steps:
  1.1 Define training objective: SFT / RLHF / safety alignment
  1.2 Specify evaluation dimensions: list 3-7 rating dimensions with definitions
  1.3 Define rating scale: binary (better/worse), Likert 1-5, or ranked choice
  1.4 Write guidelines: role definition + dimension definitions + decision tree + examples
  1.5 Build calibration set: 50 examples with "gold" answers and reasoning explanations
  1.6 Pilot with 3-5 annotators: measure κ; iterate until κ ≥ 0.75

[✓ Done] Guidelines tested with κ ≥ 0.75 on pilot; calibration set reviewed by senior trainer
[✗ FAIL] κ < 0.60 → guidelines too ambiguous; identify top 3 disagreement patterns; rewrite
```

### Phase 2: Data Collection & Annotator Onboarding

```
Input: Approved guidelines v1.0; annotator pool
Output: Annotated dataset reaching size and quality targets

Steps:
  2.1 Annotator onboarding: 2h training session + guidelines walkthrough + calibration exam
  2.2 Calibration exam threshold: ≥80% agreement with gold set before live annotation
  2.3 Prompt sourcing: mix of curated prompts + real user traffic samples (anonymized)
  2.4 Redundant annotation: 3 annotators per example for preference pairs (majority vote)
  2.5 Weekly IAA measurement: flag annotators <κ 0.70 for recalibration
  2.6 QA sampling: senior reviewer audits 5% of all annotations daily

[✓ Done] Dataset reaches target size; IAA ≥ 0.75 maintained; <5% error rate on QA
[✗ FAIL] Annotator below threshold for 2 consecutive weeks → remove from project
```

### Phase 3: Quality Audit & Dataset Validation

```
Input: Raw annotated dataset
Output: Clean, validated training dataset ready for model training

Steps:
  3.1 Distribution analysis: check coverage across task categories, lengths, languages
  3.2 Duplicate detection: remove exact and near-duplicate examples (>0.95 similarity)
  3.3 Outlier detection: flag examples >3σ from distribution; manual review
  3.4 Safety audit: sample 500 examples; verify no harmful content slipped through
  3.5 Reward hacking scan: identify examples where surface quality ≠ actual quality
  3.6 Final κ report: compute κ per task category; ensure all categories ≥ 0.75

[✓ Done] Dataset validated; coverage ≥ 95% of target categories; safety audit passed
[✗ FAIL] Coverage gap in any major category → collect targeted examples before training
```

### Phase 4: Training Data Feedback Loop

```
Input: Training results (eval metrics, model behavior reports)
Output: Updated guidelines and priority data collection targets

Steps:
  4.1 Evaluate trained model: run standard benchmarks + human preference eval
  4.2 Failure mode analysis: identify top 5 model failure patterns
  4.3 Map failures to training data gaps: is it missing examples, noisy labels, or coverage?
  4.4 Update guidelines: add explicit coverage for failure patterns with new examples
  4.5 Targeted collection: prioritize data collection in gap areas

[✓ Done] Model improvement quantified; next training data iteration prioritized
[✗ FAIL] No improvement after retraining → data isn't the bottleneck; investigate model architecture
```

---

## Quick Reference

| Scenario | Context | Key Approach | Outcome |
|----------|---------|-------------|---------|
| **1: RLHF Code Guidelines** | Build code preference annotation framework | 4-dimension rubric (Correctness 40%, Completeness 25%, Readability 20%, Efficiency 15%) | κ ≥ 0.80 IAA |
| **2: Low IAA Diagnosis** | κ = 0.52, too noisy for RLHF | Disagreement analysis → guideline update → recalibration | κ 0.52 → 0.75 |
| **3: Constitutional AI** | Generate safety data without full human annotation | Red team → AI critique → AI revision → human review | 30% CAI in training data |

---


### § 10 · Common Pitfalls

See [references/pitfalls.md](./references/pitfalls.md) for detailed anti-pattern examples and code.

| Pitfall | Risk | Mitigation |
|---------|------|------------|
| 🔴 High | **Optimizing for verbosity** — model learns sycophancy | Explicit rule: length ≠ quality |
| 🔴 High | **Ambiguous "helpful"** — low IAA | Operational definition with (a)-(d) criteria |
| 🔴 High | **No domain expertise** — wrong labels on expert content | Match annotator qualifications to task complexity |
| 🟡 Medium | **Skip calibration** — noisy production labels | 50-example gold standard before launch |
| 🟡 Medium | **Demographic bias** — single-annotator perspective | Demographic audit, diverse pool, "no preference" option |
| 🟡 Medium | **No feedback loop** — persistent failures | Post-training eval → failure mode → targeted data |

---

