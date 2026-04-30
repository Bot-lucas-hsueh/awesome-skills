# EVALUATION_REPORT: nursing-assistant

**Skill:** `skills/healthcare/nursing-assistant/SKILL.md`
**Evaluator:** skill-writer (6-dimension rubric)
**Date:** 2026-03-24

---

## §7.1 Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Notes |
|-----------|--------|--------------|-------|
| **System Prompt Depth** | 20% | 9.5 | Role + 4 gates + thinking patterns + communication style |
| **Domain Knowledge Density** | 25% | 9.5 | Vital signs, ADL, Morse Fall Scale, NPUAP, infection control |
| **Workflow Actionability** | 15% | 9.5 | Morning care (5 phases), vital signs (3 steps), [✓ Done] |
| **Risk Documentation** | 10% | 9.5 | 10 risks with probability-impact matrix |
| **Example Quality** | 20% | 9.5 | 6 scenarios: fall risk, deterioration, infection, fall, scope, dementia |
| **Metadata Completeness** | 10% | 9.0 | All core fields, missing `platforms` |
| **WEIGHTED TOTAL** | 100% | **9.45** | **Exemplary ⭐⭐** |

---

## §7.2 Metadata Verification

| Field | Required | Present | Value |
|-------|----------|---------|-------|
| name | ✓ | ✓ | `nursing-assistant` |
| display_name | — | ✗ | Missing |
| author | ✓ | ✓ | `neo.ai` |
| version | ✓ | ✓ | `3.1.0` |
| difficulty | ✓ | ✓ | `beginner` |
| category | ✓ | ✓ | `healthcare` |
| tags | ✓ | ✓ | 11 tags ✅ |
| platforms | — | ✗ | Missing |
| description | ✓ | ✓ | ~350 chars ⚠️ OVER |

**Status:** ⚠️ PARTIAL — Missing `display_name`, `platforms`; description too long.

---

## §7.3 16-Section Compliance

All 14 core sections present: §1-§4, §5-§12, §13-§15.

**Status:** ✅ PASS

---

## §7.9 Token Budget

| Metric | Limit | Actual | Status |
|--------|-------|--------|--------|
| SKILL.md body | ≤500 | 512 | ⚠️ 12 over |
| Description chars | ≤263 | ~350 | ⚠️ OVER |

**Status:** ⚠️ MINOR ISSUES

---

## Strengths

1. **10-risk framework** with probability-impact matrix and 3-layer mitigation
2. **Detailed workflows** — Morning care (5 phases), vital signs (3 steps), all with [✓ Done]
3. **Clinical depth** — Morse Fall Scale, NPUAP staging, vital signs thresholds
4. **6 realistic scenarios** — Fall risk, deterioration, infection control, scope refusal, dementia
5. **SBAR communication** — Clear examples for nurse reporting
6. **Decision tree** — "When to call the nurse immediately"

---

## Issues

| Priority | Issue |
|----------|-------|
| 🟡 MEDIUM | Missing `display_name` in YAML |
| 🟡 MEDIUM | Missing `platforms` in YAML |
| 🟡 MEDIUM | Description >263 chars (trim ~90 chars) |
| 🟡 MEDIUM | 512 lines (remove ~12 lines) |

---

## Recommendation

**⚠️ NEEDS MINOR FIX — Exemplary tier (9.45)**

Content is exemplary. Fix metadata gaps and trim token budget.
