# EVALUATION REPORT: social-worker

## Overall Assessment

| Metric | Value |
|--------|-------|
| **Weighted Score** | 9.3/10 |
| **Quality Tier** | Exemplary ⭐⭐ |
| **Recommendation** | APPROVED - Minimal updates needed |

---

## Dimension Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| **System Prompt Depth** | 9.5 | 20% | 1.90 |
| **Domain Knowledge Density** | 9.5 | 25% | 2.38 |
| **Workflow Actionability** | 9.5 | 15% | 1.43 |
| **Risk Documentation** | 9.5 | 10% | 0.95 |
| **Example Quality** | 9.5 | 20% | 1.90 |
| **Metadata Completeness** | 8.0 | 10% | 0.80 |
| **TOTAL** | | 100% | **9.3** |

---

## Detailed Evaluation

### ✅ System Prompt Depth (9.5/10)
- **Strengths**: Complete identity with LCSW, 15+ years, clinical supervision experience; decision hierarchy (Safety → Crisis Stabilization → Basic Needs → Stability → Growth); 5 quality gates; 4 thinking patterns (Biopsychosocial Assessment, Trauma-Informed Care, Systems Thinking, Strengths-Based Practice)
- **Suggestions**: Consider adding specific thresholds for risk assessment tools

### ✅ Domain Knowledge Density (9.5/10)
- **Strengths**: Suicide risk assessment (C-SSRS) with response actions; child maltreatment indicators table; evidence-based practices (CBT, DBT, MI, TF-CBT); social determinants of health framework
- **Suggestions**: Add more domain-specific metrics (e.g., specific risk score thresholds)

### ✅ Workflow Actionability (9.5/10)
- **Strengths**: 5-phase case management process (Engagement → Assessment → Planning → Implementation → Evaluation) with clear deliverables
- **Suggestions**: Add failure criteria for each phase

### ✅ Risk Documentation (9.5/10)
- **Strengths**: 6 risks with severity ratings and mitigation: client harm, abuse, boundary violations, vicarious trauma, confidentiality breach, misdiagnosis
- **Suggestions**: Add escalation triggers

### ✅ Example Quality (9.5/10)
- **Strengths**: 5 diverse comprehensive scenarios: Child Welfare Investigation, Mental Health Crisis, Hospital Discharge, Trauma-Informed Family Therapy, Advocacy for Homeless Client; detailed tables and decision frameworks
- **Suggestions**: Consider adding one anti-pattern correction scenario

### ⚠️ Metadata Completeness (8.0/10)
- **Strengths**: All required fields present
- **Issues**:
  - Non-standard YAML with custom fields
  - Missing platforms field
  - Description ~320 chars (over limit)

---

## Token Budget Analysis

| Metric | Current | Limit | Status |
|--------|---------|-------|--------|
| SKILL.md lines | 830 | 500 | ⚠️ OVER |
| Description chars | ~320 | 263 | ⚠️ OVER |

---

## Recommendations

### Priority 1 - Required
1. Add `platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]`
2. Trim description to ≤263 chars
3. Move reference content to `references/` to reduce lines

### Priority 2 - Suggested
4. Add failure criteria to workflow phases
5. Add risk score thresholds to domain knowledge

---

## Summary

**Exemplary** skill with comprehensive social work coverage. Similar issues to emergency-manager: token budget and metadata. Minimal updates required.
