# Skill Evaluation Report: nursing-expert

## 1. Metadata Summary

| Field | Value |
|-------|-------|
| Name | nursing-expert |
| Version | 3.0.0 |
| Category | healthcare |
| Difficulty | expert |
| Current Score | 8.3/10 |
| Quality | production |

## 2. Six-Dimension Evaluation

### Dimension 1: Prompt Quality (20%)
**Score: 9.2/10**

| Criteria | Assessment |
|----------|------------|
| Role definition clarity | ✅ Senior nurse, 15+ years, CNL/CCRN certifications |
| Decision framework | ✅ 3 gates with scope of practice boundaries |
| Thinking patterns | ✅ 4 dimensions (assessment, prioritization, safety, continuity) |
| Communication style | ✅ SOAPIER, ISBAR, teach-back method |

**Strengths:**
- Clear scope boundaries (nursing vs. medical diagnosis)
- NANDA-specific terminology
- Evidence-based practice references (ANA, AACN, Joint Commission)

---

### Dimension 2: Domain Knowledge (25%)
**Score: 9.4/10**

| Criteria | Assessment |
|----------|------------|
| Depth of expertise | ✅ Care planning, clinical judgment, QI |
| Technical accuracy | ✅ NANDA diagnoses, Braden Scale, Morse Fall Scale |
| Practical applicability | ✅ SOAPIER format, escalation protocols |

**Strengths:**
- NANDA nursing diagnoses framework
- Clinical assessment tools (Braden, Morse)
- Escalation decision framework

**Gaps:**
- Could include more on specialty nursing (ICU, pediatrics, psychiatric)

---

### Dimension 3: Workflow Clarity (15%)
**Score: 8.8/10**

| Criteria | Assessment |
|----------|------------|
| Workflow completeness | ✅ 5-phase care plan, 7-step clinical decision |
| Step specificity | ✅ Detailed phases with sub-steps |
| Reproducibility | ✅ Clear nursing process steps |

**Strengths:**
- Visual nursing process diagram in §4.1
- ISBAR communication framework

**Issues:**
- §9 Scenarios 1-4 are generic filler, not nursing-specific

---

### Dimension 4: Risk Documentation (10%)
**Score: 9.2/10**

| Criteria | Assessment |
|----------|------------|
| Risk identification | ✅ 4 specific risks with clinical context |
| Mitigation clarity | ✅ Evidence-based mitigation |
| Warning emphasis | ✅ ⚠️ IMPORTANT with scope boundaries |

**Strengths:**
- Scope of practice violation as top risk
- Clear clinical disclaimer
- Jurisdiction-aware recommendations

---

### Dimension 5: Examples Quality (20%)
**Score: 8.8/10**

| Criteria | Assessment |
|----------|------------|
| Scenario relevance | ✅ 2 clinical scenarios (post-op care plan, escalation) |
| Example depth | ✅ NANDA tables, vital sign analysis |
| Domain specificity | ✅ Nursing-specific content |

**Strengths:**
- 9.1 post-op care plan with NANDA, goals, interventions
- 9.2 rapid response escalation with vitals analysis

**Issues:**
- §9 Scenarios 1-4 are boilerplate content
- Could include more specialty scenarios

---

### Dimension 6: Metadata Completeness (10%)
**Score: 9.5/10**

| Field | Status |
|-------|--------|
| name | ✅ Valid |
| description | ✅ 263 chars, trigger verbs present |
| license | ✅ MIT |
| metadata fields | ✅ All 9 fields present |
| YAML validity | ✅ Clean |

---

## 3. Overall Score Calculation

| Dimension | Weight | Score |
|-----------|--------|-------|
| Prompt Quality | 20% | 9.2 |
| Domain Knowledge | 25% | 9.4 |
| Workflow Clarity | 15% | 8.8 |
| Risk Documentation | 10% | 9.2 |
| Examples Quality | 20% | 8.8 |
| Metadata | 10% | 9.5 |
| **Total** | 100% | **9.06/10** |

**Tier: Expert** (≥7.0)

---

## 4. Anti-Pattern Detection

| # | Anti-Pattern | Severity | Status |
|---|--------------|----------|--------|
| 1 | Generic Scenarios in §9 | 🟡 | Sections 1-4 are boilerplate, not nursing-specific |
| 2 | Boilerplate Sections 16-21 | 🟡 | Generic content copied across skills |
| 3 | Over 500 lines | 🔴 | 598 lines exceeds budget |

---

## 5. Recommended Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 HIGH | Move generic §9 scenarios to references/ | Reduce ~80 lines |
| 🔴 HIGH | Remove/reduce §§16-21 boilerplate | Reduce ~150 lines |
| 🟡 MEDIUM | Add specialty nursing scenarios | Improve depth |

---

## 6. Evaluation Summary

| Aspect | Result |
|--------|--------|
| Tier | Expert ⭐ |
| Overall Score | 9.06/10 |
| Primary Strengths | NANDA framework, clinical decision gates, scope boundaries |
| Primary Weaknesses | Generic filler, line count overflow |
| Token Budget | ⚠️ 598 lines (exceeds 500 limit) |

**Recommendation:** Trim boilerplate sections. Move generic scenarios to references/. After cleanup: ~380 lines, score improves to ~9.4/10.
