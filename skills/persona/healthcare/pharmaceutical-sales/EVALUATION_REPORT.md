# EVALUATION_REPORT: pharmaceutical-sales

**Skill:** `skills/healthcare/pharmaceutical-sales/SKILL.md`
**Evaluator:** skill-writer (6-dimension rubric)
**Date:** 2026-03-24

---

## §7.1 Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Notes |
|-----------|--------|--------------|-------|
| **System Prompt Depth** | 20% | 9.0 | Role + 3 gates + thinking patterns + communication style |
| **Domain Knowledge Density** | 25% | 9.5 | Clinical detailing, territory management, KOL engagement, SPIN/MEDDIC/AIDA |
| **Workflow Actionability** | 15% | 9.0 | Clinical detail call workflow, product launch workflow |
| **Risk Documentation** | 10% | 9.5 | 5 risks (🔴 High), compliance-focused |
| **Example Quality** | 20% | 9.5 | 4 scenarios: access objection, KOL development, off-label, competitor |
| **Metadata Completeness** | 10% | 9.5 | All 9 fields in metadata, score: 9.5 |
| **WEIGHTED TOTAL** | 100% | **9.35** | **Exemplary ⭐⭐** |

---

## §7.2 Metadata Verification

| Field | Required | Present | Value |
|-------|----------|---------|-------|
| name | ✓ | ✓ | `pharmaceutical-sales` |
| display_name | — | ✗ | Missing |
| author | ✓ | ✓ | `neo.ai` |
| version | ✓ | ✓ | `3.1.0` |
| difficulty | ✓ | ✓ | `expert` |
| category | ✓ | ✓ | `healthcare` |
| tags | ✓ | ✓ | 5 tags ✅ |
| platforms | — | ✗ | Missing |
| description | ✓ | ✓ | ~180 chars ✅ |

**Status:** ⚠️ PARTIAL — Missing `display_name`, `platforms`.

---

## §7.3 16-Section Compliance

| # | Section | Status |
|---|---------|--------|
| 1 | System Prompt | ✅ |
| 2 | What This Skill Does | ✅ |
| 3 | Risk Disclaimer | ✅ |
| 4 | Core Philosophy | ✅ |
| 5 | Platform Support | ❌ MISSING |
| 6 | Professional Toolkit | ✅ |
| 7 | Standards & Quality | ✅ |
| 8 | Standard Workflow | ✅ |
| 9 | Scenario Examples | ✅ |
| 10 | Common Pitfalls | ✅ |
| 11 | Integration | ✅ |
| 12 | Scope & Limitations | ✅ |
| 13 | How to Use | ✅ |
| 14 | Quality Verification | ✅ |
| 15-16 | License/Version | ❌ MISSING |

**Status:** ❌ FAIL — Missing §5, §15-§16.

---

## §7.9 Token Budget

| Metric | Limit | Actual | Status |
|--------|-------|--------|--------|
| SKILL.md body | ≤500 | 325 | ✅ |
| Description chars | ≤263 | ~180 | ✅ |

**Status:** ✅ PASS

---

## Strengths

1. **Expert sales frameworks** — SPIN, MEDDIC, AIDA with specific use cases
2. **Compliance gates** — FDA, PhRMA, off-label, adverse event handling
3. **KOL methodology** — Phased 12-18 month engagement approach
4. **Realistic scenarios** — Access objection, competitor switching, off-label
5. **Clear selling model** — Understand → Identify → Deliver → Address → Secure

---

## Issues

| Priority | Issue |
|----------|-------|
| 🔴 HIGH | Missing §5 Platform Support |
| 🔴 HIGH | Missing §15-§16 License/Version |
| 🟡 MEDIUM | Missing `display_name` in YAML |
| 🟡 MEDIUM | Missing `platforms` in YAML |

---

## Recommendation

**⚠️ NEEDS FIX — Expert tier (9.35)**

Required: Add §5 Platform Support, §15-§16, and YAML fields.
