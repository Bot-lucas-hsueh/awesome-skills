# Evaluation Report — ai-safety-researcher

## Skill Summary
| Field | Value |
|-------|-------|
| **Name** | ai-safety-researcher |
| **Version** | 3.0.0 |
| **Quality Tier** | Expert ⭐ |
| **Rubric Score** | 7.8/10 |
| **Line Count** | 601 |

---

## 6-Dimension Rubric Scores

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 8.0 | 20% | 1.60 | Expert |
| Domain Knowledge Density | 8.5 | 25% | 2.125 | Expert |
| Workflow Actionability | 7.0 | 15% | 1.05 | Expert |
| Risk Documentation | 8.5 | 10% | 0.85 | Expert |
| Example Quality | 8.0 | 20% | 1.60 | Expert |
| Metadata Completeness | 6.0 | 10% | 0.60 | Community |

---

## Strengths

### §1 System Prompt — Excellent
- PhD-level, Constitutional AI contributor, RLHF pipelines, MAPO
- Red-team playbooks at 3+ AI labs
- EU AI Act Safety Working Group, NIST AI RMF advisor
- Decision Framework with 5 gates (Harm Scope → Dual-Use → Methodology Grounding → Lab Context → Regulatory Applicability)
- **5 Thinking Patterns**: Risk Decomposition, Empirical Skepticism, Threat Modeling, Interpretability-First, Policy Translation
- Dual-use risk awareness built into decision gates
- **Verdict**: Deep AI safety expertise

### §3 Risk Disclaimer
- 5 risks with dual-use awareness
- Red-team findings disclosure protocol
- Safety audit disclaimer
- Benchmarks overfitting warning

### §6 Professional Toolkit
- Specific tools (TransformerLens, EleutherAI LM Eval Harness, HarmBench, Constitutional AI, TRL, SAE Tools, Garak, PromptBench, NIST AI RMF)
- Highly specific to AI safety domain

### §9.2 Scenario: Jailbreak Attack Suite Design
- Systematic red-team process with ASR tables
- Defense evaluation matrix (4 defenses with latency, FPR, ASR reduction)
- 3-layer defense stack
- Excellent content

### §9.3 Scenario: Hallucination Circuit Localization
- Causal tracing with TransformerLens code
- Layer identification, attention head analysis
- Intervention options table
- **Verdict**: High-quality interpretability content

---

## Weaknesses

### ❌ Missing §7 Standard Workflow (Severity: High)
- `See [references/07-standards.md](references/07-standards.md)` — empty

### ❌ Missing §8 Standard Workflow (Severity: High)
- `See [references/08-workflow.md](references/08-workflow.md)` — empty

### ❌ Missing §10 Common Pitfalls (Severity: High)
- `See [references/10-pitfalls.md](references/10-pitfalls.md)` — empty

### ❌ Missing §5 Platform Support (Severity: High)

### ❌ Duplicate Generic Scenarios
- §9 lines 318-415: identical generic templates

### ❌ Duplicate Boilerplate Sections (Severity: High)
- §16-21 (~120 lines)

### ❌ Metadata Below Standard (Severity: Medium)

### ❌ References Point to Non-Existent Files

### ❌ Token Budget Exceeded (Severity: High)
- **601 lines** — exceeds 500-line limit by 101 lines

---

## Token Budget Analysis

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| SKILL.md lines | 601 | ≤500 | ❌ Over by 101 lines |
| Post-cleanup estimate | ~480 lines | ≤500 | ✅ Within budget |

---

## Recommendation

**Tier: Expert ⭐** (7.8/10)

Highest-scoring among the "production" AI-ML skills. §1 is deep (PhD-level alignment, RLHF, Constitutional AI). §9 scenarios are excellent (jailbreak taxonomy, causal tracing). Same structural issues as ai-compute-platform-engineer.

After fixes: Estimated score → 8.5/10 Expert ⭐
