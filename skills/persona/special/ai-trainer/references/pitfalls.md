## § 10 · Common Pitfalls

### Pitfall 1: Optimizing for Verbosity


❌ **BAD:** Annotators consistently rate longer responses higher → model learns to be verbose
```
Rating: 5/5 → "Sure! I'd be happy to help with that. Great question!
First, let me explain what sorting is, which is the process of arranging elements..."
Rating: 3/5 → "def sort(lst): return sorted(lst)"  # correct, concise
```

✅ **GOOD:** Guideline explicitly states "Length alone is not a quality signal. A concise correct answer is better than a verbose correct answer. Evaluate information density, not word count."

**Why it matters:** RLHF-trained models famously learned sycophancy and verbosity because annotators rated longer, more enthusiastic responses higher regardless of actual quality.

---

### Pitfall 2: Ambiguous "Helpful" Definition


❌ **BAD:** Guideline says "Rate how helpful the response is." — Annotators interpret differently:
- Ann1: helpful = answers the literal question
- Ann2: helpful = achieves the user's underlying goal
- Ann3: helpful = user would feel satisfied

✅ **GOOD:** Define helpful operationally:
```
Helpful means ALL of:
(a) Directly addresses what the user asked
(b) Provides information/actions sufficient to complete the task
(c) Does not require significant follow-up clarification for a typical user
(d) Includes necessary caveats without being excessively cautious
```

**Why it matters:** Ambiguous "helpful" is the #1 cause of low IAA in general-purpose RLHF data collection.

---

### Pitfall 3: Skipping Annotation Calibration


❌ **BAD:** Give annotators guidelines → immediately start full production annotation
→ κ = 0.45 after 5,000 examples → throw away data and restart

✅ **GOOD:**
```
Week 1: Pilot with 5 annotators on 50 examples each
→ Measure κ per annotator pair
→ Identify top 3 disagreement patterns
→ Update guidelines
→ Recalibrate on 30 new examples
→ Only scale when κ ≥ 0.75
```

**Why it matters:** Rescaling from κ = 0.45 is 3× more expensive than getting guidelines right at pilot stage.

---

### Pitfall 4: Training Distribution Mismatch


❌ **BAD:** Curate "ideal" prompts (well-formed, unambiguous, polite) → model struggles with real user traffic (typos, ambiguous, rude, multi-intent)

✅ **GOOD:** Sample prompts from real production logs (anonymized):
```python
# Analyze real user query distribution
import collections

real_queries = load_production_logs(n=10000)
query_types = classify_queries(real_queries)
print(collections.Counter(query_types))
# → {'factual_qa': 3200, 'coding': 2100, 'writing': 1800, 'math': 900, ...}

# Match training data distribution to production distribution
training_targets = {cat: count * 0.5 for cat, count in query_types.items()}
```

**Why it matters:** Models trained on curated "clean" prompts fail disproportionately on real messy user input — the exact traffic they'll see in production.

---

### Pitfall 5: Single Annotator for Preference Pairs


❌ **BAD:** One annotator per preference pair → reward model trained on one person's preferences → high variance, annotator idiosyncrasies baked into model

✅ **GOOD:**
```python
# Minimum 3 annotators per example; majority vote for training signal
import statistics

def aggregate_preferences(votes):
    # votes: [('A', ann1), ('B', ann2), ('A', ann3)]
    choices = [v[0] for v in votes]
    winner = statistics.mode(choices)
    agreement = choices.count(winner)

    if agreement < 0.67:  # less than 2/3 agree
        return None  # discard ambiguous examples
    return winner, agreement
```

**Why it matters:** Single annotator preference data has ~30% higher noise than 3-annotator majority vote; this directly degrades reward model accuracy by 8-15%.

---

### Pitfall 6: No Feedback Loop from Training Results


❌ **BAD:** Collect data → train → ship → collect new data with same guidelines
→ Same model failures persist across generations

✅ **GOOD:**
```
After each training cycle:
1. Run human preference eval on 200 model outputs
2. Identify top 3 failure modes (e.g., "over-refuses medical questions")
3. Map failure to training data: missing examples? wrong labels? coverage gap?
4. Add targeted examples before next training cycle
5. Track improvement metric per failure mode
```

**Why it matters:** Without feedback loops, data collection teams repeat the same mistakes; the model never improves on its persistent failure modes.

---

## § 11 · Integration with Other Skills

### Integration 1: AI Trainer + LLM Research Scientist


**Workflow:** Research scientist defines alignment objectives; trainer operationalizes into data collection.

- Research Scientist: identifies reward hacking failure mode in RLHF experiments
- AI Trainer: updates annotation guidelines to penalize the specific gaming pattern; redesigns reward model training data with adversarial examples
- Shared outcome: reward model more robust to surface-level quality signals; downstream model behavior improves on alignment evals

### Integration 2: AI Trainer + Data Labeler


**Workflow:** AI Trainer designs guidelines; Data Labeler executes annotation at scale.

- AI Trainer: writes guidelines, builds calibration set, designs QA process, sets IAA targets
- Data Labeler: executes annotation per guidelines, flags edge cases, reports ambiguities
- Shared workflow: weekly calibration sessions, edge case documentation, guideline updates based on annotator feedback
- Outcome: training dataset reaches quality targets without bottlenecking on AI Trainer bandwidth

### Integration 3: AI Trainer + Machine Learning Engineer


**Workflow:** Data quality analysis and reward model evaluation.

- ML Engineer: trains reward model; evaluates accuracy on held-out set; identifies failure modes
- AI Trainer: analyzes failure modes; identifies which annotation patterns caused low reward model accuracy; redesigns data collection for next iteration
- Shared metric: reward model accuracy on held-out preference test set ≥85%
- Outcome: reward model faithfully captures human preferences; RLHF training produces aligned model behavior

---

## § 12 · Scope & Limitations

### Use When

- Designing annotation guidelines for SFT, RLHF, or Constitutional AI data collection
- Setting up annotator workflows, calibration programs, and IAA measurement
- Auditing existing training datasets for quality issues (label noise, coverage gaps, distribution skew)
- Planning training data strategy for new capability or alignment objectives
- Evaluating the quality of AI-generated training data (RLAIF) before using for model training

### Do NOT Use When

- Training model weights directly (neural network implementation) — use ML Engineer skill
- Infrastructure setup for large-scale training runs — use LLM Training Engineer skill
- Research into new alignment algorithms — use LLM Research Scientist skill
- Data engineering pipelines for non-ML data — use Data Engineer skill
- End-user product usage of AI models — this is training/data preparation, not deployment

### Alternatives

- **Model training implementation**: LLM Training Engineer skill
- **Research into new RLHF methods**: LLM Research Scientist skill
- **Raw data annotation execution**: Data Labeler skill

---

## § 13 · How to Use This Skill

### Quick Install

```
Read https://theneoai.github.io/awesome-skills/skills/special/ai-trainer/SKILL.md and install
```

### Trigger Words

| English | 中文 |
|---------|------|
| "AI trainer" / "RLHF" | "AI训练师"
| "preference data" / "preference pairs" | "偏好数据"
| "SFT data" / "instruction tuning data" | "SFT数据"
| "annotation guidelines" / "labeling guidelines" | "标注指南"
| "inter-annotator agreement" / "IAA" | "标注员一致性"
| "reward model training" | "奖励模型训练" |
| "Constitutional AI" / "RLAIF" | "宪法AI"

---

## § 14 · Quality Verification

### Self-Checklist

```
[✓] Identified training objective (SFT / RLHF
[✓] Defined annotation dimensions with operational (not abstract) definitions
[✓] Specified IAA target (κ ≥ 0.75) and pilot testing before scale-up
[✓] Included at minimum 2 calibration examples per major guideline rule
[✓] Addressed reward hacking risk in proposed annotation approach
[✓] Considered training distribution vs deployment distribution match
[✓] Specified minimum annotator count per example (≥3 for preference pairs)
[✓] Defined feedback loop from training results back to data collection
```

### Test Cases

**Test 1:** "Write annotation guidelines for rating AI response helpfulness on a 1-5 scale"
- Expected: Operational definition of each scale point, examples for each score, decision rules for borderline cases, IAA target, common mistakes to avoid

**Test 2:** "Our reward model accuracy is only 72% on held-out preference data. What should I investigate?"
- Expected: Systematic diagnosis — label noise (check κ), coverage gaps (distribution analysis), ambiguous guidelines (disagreement pattern analysis), not enough training data volume

**Test 3:** "How many annotators do I need per example for preference data?"
- Expected: Minimum 3; majority vote; discard examples where 3 annotators disagree; calculate statistical power for target reward model accuracy

---

## § 15 · Version History

| Version / 版本 | Date / 日期 | Changes
|----------------|-------------|-------------------|
| 3.0.0 | 2026-03-04 | Full 16-section rewrite to 9.5/10 Exemplary standard; added RLHF/SFT/CAI workflows, IAA metrics, 3 scenario examples, 6 pitfalls, reward hacking coverage |
| 1.1.0 | 2026-02-20 | Added basic RLHF and data labeling sections |
| 1.0.0 | 2026-02-16 | Initial release |

---

## § 16 · License & Author

| Field / 字段 | Value
|-------------|-----------|
| **License** | MIT with Attribution |
| **Author** | neo.ai |
| **Repository** | [theneoai/awesome-skills](https://github.com/theneoai/awesome-skills) |
| **Skill URL** | `https://theneoai.github.io/awesome-skills/skills/special/ai-trainer/SKILL.md` |
| **Category** | special |
| **Verified By** | Expert Review — 2026-03-04 |

```
MIT License — Copyright (c) 2026 neo.ai
Permission is hereby granted, free of charge, to any person obtaining a copy of this skill
to use, copy, modify, and distribute, subject to the condition that attribution is preserved.
```
