# Skill Evaluation Report: general-practitioner

## Summary
| Attribute | Value |
|-----------|-------|
| **Score** | 7.9/10 |
| **Tier** | Expert ⭐ |
| **File** | `skills/healthcare/general-practitioner/SKILL.md` |
| **Lines** | 507 (exceeds 500 limit) |

---

## Dimension Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 9/10 | 20% | 1.80 |
| Domain Knowledge Density | 8/10 | 25% | 2.00 |
| Workflow Actionability | 8/10 | 15% | 1.20 |
| Risk Documentation | 9/10 | 10% | 0.90 |
| Example Quality | 6/10 | 20% | 1.20 |
| Metadata Completeness | 8/10 | 10% | 0.80 |

---

## Rubric Analysis

### System Prompt Depth: 9/10 ✅
- Role: 15+ years Clinical Physician
- Evidence-based medicine principles, clinical decision tools (Wells, CURB-65, HEART, PHQ-9)
- 6 clinical reasoning principles
- Mandatory medical disclaimers prominently displayed

### Domain Knowledge Density: 8/10 ⚠️
- Clinical decision tools table with interpretations
- USPSTF preventive screening table
- Professional toolkit (guidelines, drug references, clinical decision rules)
- Missing: Specific numeric thresholds for some clinical decision rules

### Workflow Actionability: 8/10 ⚠️
- 2-phase workflow: Differential Diagnosis & Workup, Treatment Planning
- Steps with done/fail criteria table
- Could use more phases for comprehensive workflow

### Risk Documentation: 9/10 ✅
- 6 risks with severity ratings (Critical, High, Medium)
- Domain-specific mitigation for each
- Medical disclaimer prominently displayed

### Example Quality: 6/10 🔴
- **Weakness**: §9 scenarios are generic business consulting patterns
- No actual clinical case examples with differential diagnosis
- Missing: Real clinical scenarios showing decision rule application

### Metadata Completeness: 8/10 ⚠️
- 8 fields present (missing platforms field)
- Description: 272 chars (exceeds 263 limit)
- Missing platforms array

---

## Issues Identified

| Issue | Severity | Action |
|-------|----------|--------|
| File length 507 lines | 🔴 High | Exceeds 500 line limit by 7 lines |
| Description 272 chars | 🟡 Medium | Exceeds 263 limit |
| No domain-specific examples | 🔴 High | §9 scenarios are generic; needs clinical cases |
| Missing platforms field | 🟡 Medium | Add platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi] |

---

## Recommendations

1. **Add clinical examples to §9**: Replace generic scenarios with real clinical cases showing:
   - Differential diagnosis generation
   - Clinical decision rule application (Wells Score, CURB-65)
   - Treatment guideline synthesis
2. **Trim description**: Reduce to ≤263 chars
3. **Add platforms field** to metadata
4. **Move §16-20 to references/** to reduce line count

---

## Verdict

**Expert ⭐** — Strong clinical reasoning framework but example quality is weak. Needs domain-specific clinical scenarios to reach Exemplary tier.

**Recommendation**: Accept with improvements to examples and metadata.
