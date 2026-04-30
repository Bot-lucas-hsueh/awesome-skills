# EVALUATION_REPORT: resident-physician

**Skill:** `skills/healthcare/resident-physician/SKILL.md`
**Evaluator:** skill-writer (6-dimension rubric)
**Date:** 2026-03-24

---

## §7.1 Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Notes |
|-----------|--------|--------------|-------|
| **System Prompt Depth** | 20% | 9.0 | Role + 4 gates + thinking patterns |
| **Domain Knowledge Density** | 25% | 9.0 | SOAP, SBAR, VINDICATE, ACGME competencies |
| **Workflow Actionability** | 15% | 9.0 | Patient workup (4 phases), presenting workflow |
| **Risk Documentation** | 10% | 8.5 | 5 risks with severity, lacks probability matrix |
| **Example Quality** | 20% | 9.5 | 6 scenarios: presentation, workup, night float, handoff |
| **Metadata Completeness** | 10% | 8.5 | Missing `platforms` |
| **WEIGHTED TOTAL** | 100% | **9.00** | **Expert ⭐** |

---

## §7.2 Metadata Verification

| Field | Required | Present | Value |
|-------|----------|---------|-------|
| name | ✓ | ✓ | `resident-physician` |
| display_name | — | ✗ | Missing |
| author | ✓ | ✓ | `neo.ai` |
| version | ✓ | ✓ | `3.1.0` |
| difficulty | ✓ | ✓ | `intermediate` |
| category | ✓ | ✓ | `healthcare` |
| tags | ✓ | ✓ | 9 tags ✅ |
| platforms | — | ✗ | Missing |
| description | ✓ | ✓ | ~200 chars ✅ |

**Status:** ⚠️ PARTIAL — Missing `display_name`, `platforms`.

---

## §7.3 16-Section Compliance

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | System Prompt | ✅ | |
| 2 | What This Skill Does | ✅ | |
| 3 | Risk Disclaimer | ✅ | |
| 4 | Core Philosophy | ✅ | |
| 5 | Platform Support | ⚠️ WEAK | Generic placeholder |
| 6-16 | All others | ✅ | |

**Status:** ⚠️ PARTIAL — §5 exists but is generic.

---

## §7.9 Token Budget

| Metric | Limit | Actual | Status |
|--------|-------|--------|--------|
| SKILL.md body | ≤500 | 432 | ✅ |
| Description chars | ≤263 | ~200 | ✅ |

**Status:** ✅ PASS

---

## Strengths

1. **ACGME integration** — 6 core competencies mapped to practice
2. **6 realistic scenarios** — Ward presentation, chest pain, night float, handoff
3. **VINDICATE differential** — Systematic approach
4. **Progressive autonomy** — Clear learning progression focus
5. **SBAR handoff workflow** — Contingency planning included

---

## Issues

| Priority | Issue |
|----------|-------|
| 🟡 MEDIUM | Missing `display_name` in YAML |
| 🟡 MEDIUM | Missing `platforms` in YAML |
| 🟡 MEDIUM | §5 Platform Support is placeholder |

---

## Recommendation

**⚠️ NEEDS FIX — Expert tier (9.00)**

Add metadata fields and replace §5 placeholder.
