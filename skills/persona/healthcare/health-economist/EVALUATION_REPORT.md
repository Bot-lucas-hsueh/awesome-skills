# EVALUATION REPORT: health-economist

## Summary Scores

| Dimension | Weight | Score (1-10) | Weighted |
|-----------|--------|---------------|----------|
| **Prompt Quality** | 20% | 9.0 | 1.80 |
| **Domain Depth** | 25% | 9.5 | 2.38 |
| **Workflow Clarity** | 15% | 9.0 | 1.35 |
| **Risk Documentation** | 10% | 9.0 | 0.90 |
| **Examples Quality** | 20% | 9.5 | 1.90 |
| **Metadata Completeness** | 10% | 8.5 | 0.85 |
| **TOTAL** | 100% | | **9.18/10** |

**Tier: Exemplary ⭐⭐**

---

## Detailed Evaluation

### §1 - System Prompt (9.0/10)

**Strengths:**
- Strong identity with 10+ years at HTA bodies (NICE, ICER), pharma, academia
- Professional DNA: Value Architect, Resource Optimizer, Evidence Synthesizer, Policy Advisor
- Credentials: PhD/MSc, ISPOR certification, decision modeling training
- Decision framework: Economic evaluation hierarchy table (5 types)
- 4 thinking patterns: Opportunity Cost, Multi-Stakeholder, Uncertainty, Long-Term

**Areas for Improvement:**
- System prompt ~65 lines; dense but room for optimization
- Missing explicit trigger words for activation

### §2-4 - Core Content (9.5/10)

- Capabilities: 6 domains (Economic Evaluation, HTA, Modeling, Outcomes, Market Access, Policy)
- Risk table: 5 risks with severity/likelihood/mitigation
- Core philosophy: Value assessment framework ASCII diagram
- 5 guiding principles

### §5-6 - Toolkit & Domain (9.5/10)

**Excellent:**
- Modeling software table (5 tools)
- Key references (NICE, ISPOR, CHEERS, Drummond, CEA Registry)
- Utility instruments table (EQ-5D-5L, SF-6D, HUI3, disease-specific)
- Cost-Effectiveness Analysis steps (7 steps)
- Markov model structure explanation

### §7 - Scenario Examples (9.5/10)

5 detailed scenarios:
1. Oncology Drug CEA - ICER calculation with real numbers
2. Budget Impact Analysis - Medicaid population
3. Device HTA Submission - NICE submission
4. Vaccine Economics - RSV vaccine
5. RWE Economic Analysis - Claims database study

**Quality Signal:** Includes actual ICER values, utility weights, model structures - demonstrates deep technical knowledge.

### §8-10 - Workflow & Anti-Patterns (9.0/10)

- Workflow: 6 phases with protocol → evidence → modeling → validation → reporting → dissemination
- Anti-patterns: 4 patterns (black box, cherry-pick, ignored heterogeneity, static models)
- References: 4 resources (ISPOR, NICE, ICER, CEA Registry)

### §11 - Metadata (8.5/10)

| Field | Status |
|-------|--------|
| name | ✅ health-economist |
| description | ⚠️ 265 chars (slightly over 263 limit) |
| license | ✅ MIT |
| author | ✅ Present |
| version | ✅ 2.0.0 |
| updated | ✅ 2026-03-21 |
| tags | ✅ 6 tags |
| category | ✅ healthcare |
| difficulty | ✅ expert |
| score | ✅ 9.5/10 |
| quality | ✅ exemplary |

**Issue:** Description 265 chars - exceeds 263-char budget by 2 chars. Minor but should trim.

---

## Anti-Pattern Check

| Anti-Pattern | Status | Notes |
|--------------|--------|-------|
| Scope Creep | ✅ Pass | Single domain (health economics) |
| Shallow Depth | ✅ Pass | Technical depth evident |
| Metadata Errors | ⚠️ Warn | Description 2 chars over limit |
| Token Waste | ⚠️ Warn | 435 lines (high) |
| False Activation | ✅ Pass | 6 tags, focused |

---

## Recommendations

### Must Fix
- Trim description by 2-3 characters to meet ≤263 char budget

### Should Fix
- Add explicit trigger words (e.g., "cost-effectiveness", "HTA", "ICER", "pharmacoeconomics")
- Consider moving reference tables to references/ folder to reduce line count

### Nice to Have
- Add §5 platform support section
- Include decision tree for analysis type selection

---

## Verification Checklist

- [x] YAML frontmatter valid
- [x] All 16 sections present
- [x] System prompt in §1
- [x] Decision framework present
- [x] Thinking patterns present
- [x] Risk disclaimer present
- [x] At least 3 scenario examples
- [x] Workflow table present
- [x] Anti-patterns section present
- [x] References with URLs
- [ ] Description ≤ 263 chars ❌ (265 chars)

---

## Verdict

**Expert Verified** ✅

Technical depth is exceptional - includes actual ICER calculations, Markov model structures, utility instruments. The domain expertise is clearly from a practicing health economist. One metadata fix needed (description trim).

**Comparison to Template:** 95% compliance with template.

---

*Evaluated: 2026-03-24 | Reviewer: skill-writer methodology*
