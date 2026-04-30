# Evaluation Report — bioinformatics-scientist

**Evaluated:** 2026-03-24  
**Quality Rubric Score:** Expert ⭐ (8.8/10)

---

## 6-Dimension Scoring

| Dimension | Weight | Score | Assessment |
|-----------|--------|-------|------------|
| **System Prompt Depth** | 20% | 9/10 | Deep structured prompt with identity, decision framework, 4 thinking patterns |
| **Domain Knowledge Density** | 25% | 9/10 | Specific tools, quantified metrics (Q30≥85%, MAPQ≥30), ACMG guidelines |
| **Workflow Actionability** | 15% | 9/10 | 7 phases with done/fail criteria, clear gate questions |
| **Risk Documentation** | 10% | 8/10 | 6 risks with severity + mitigation; clinical disclaimer present |
| **Example Quality** | 20% | 9/10 | 5 full scenarios covering WGS, RNA-seq, scRNA-seq, cancer, pharmacogenomics |
| **Metadata Completeness** | 10% | 10/10 | All 9 fields present; quality tier documented |

**Weighted Score:** 8.8/10 → Expert ⭐

---

## Strengths

1. **Decision Framework** — Priority hierarchy table with pass/fail criteria is exemplary
2. **Thinking Patterns** — GIGO, Reproducibility, Bio Context, Statistical Rigor cover core patterns
3. **Domain Metrics** — Quantified thresholds (Q30, MAPQ, coverage) enable measurable quality
4. **ACMG Classification** — Real clinical variant classification framework present
5. **Pipeline Code Examples** — Actual BWA, GATK commands add practical value
6. **Scenario Coverage** — 5 scenarios spanning rare disease, cancer, RNA-seq, scRNA-seq, pharmacogenomics

---

## Issues Found

### 🔴 Critical

| Issue | Location | Fix |
|-------|----------|-----|
| **Missing §5 Platform Support** | After §4 | Add installation table for all 7 platforms |

### 🟠 Medium

| Issue | Location | Impact |
|-------|----------|--------|
| **SKILL.md at 458 lines** | Overall | Approaches 500-line limit; consider offloading pipeline code to `references/` |
| **No references/ directory** | File structure | Pipeline code and ACMG table could move to `references/` |

---

## Upgrade Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| **1** | Add §5 Platform Support (install table) | +0.5 weighted; required for Expert |
| **2** | Create `references/pipeline-examples.md` | Offload §6 code; reduces SKILL.md to ~380 lines |
| **3** | Create `references/acmg-guidelines.md` | Offload ACMG table; token efficiency |

---

## Final Assessment

**Status:** Expert ⭐ (8.8/10)  
**Verdict:** High-quality skill with deep bioinformatics knowledge. Missing §5 Platform Support is the only blocking issue. Strong candidate for Exemplary after addressing.

**Confidence in score:** High
