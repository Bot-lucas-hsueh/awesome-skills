# Skill Evaluation Report — meteorologist

**Skill:** skills/government/meteorologist/SKILL.md  
**Version:** 3.0.0  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimensional Quality Rubric Scores

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Role + 4 gates + thinking patterns + communication style. Comprehensive but could add domain heuristics. |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks (confidence matrix, deterministic/probabilistic/impact-based), quantified metrics, real tools (GFS, ECMWF, radar). |
| **Workflow Actionability** | 15% | 9/10 | 3-phase operational forecasting + 5-step severe weather protocol. Each step actionable with clear criteria. |
| **Risk Documentation** | 10% | 9/10 | 5 risks (2 🔴 High, 3 🟡 Medium), severity-rated, domain-specific mitigations. |
| **Example Quality** | 20% | 7/10 | 9.1 + 9.2 real scenarios are excellent. But §9 scenarios are generic templates not meteorologist-specific. |
| **Metadata Completeness** | 10% | 10/10 | All 9 fields present, no HTML in YAML, proper versioning. |

**Weighted Score:** 8.55  
**Tier:** Expert ⭐

---

## Strengths

1. **Forecast Confidence Framework** ( §4.1) — Excellent decision matrix showing HIGH vs LOW confidence communication strategies
2. **Probability-focused thinking** — Skill correctly emphasizes uncertainty communication
3. **Impact-first messaging** — Translates meteorological data to practical impacts
4. **Real scenarios** — 9.1 (weekend forecast) and 9.2 (hurricane approach) are domain-specific and actionable

---

## Critical Issues

| Issue | Severity | Action Required |
|-------|----------|----------------|
| **SKILL.md body 610 lines** | 🔴 | Exceeds 500-line limit. Must offload to `references/` |
| **Generic §9 scenarios** | 🟡 | Sections 9.3-9.6 are template placeholders, not meteorologist-specific |
| **Section 16-21 bloat** | 🟡 | These sections appear auto-generated from template, not domain-specific |

---

## Required Fixes

### Priority 1: Token Budget (SKILL.md > 500 lines)

Move to `references/`:
- §16 Domain Deep Dive (lines 495-515) → `references/domain-deep-dive.md`
- §17 Risk Management Deep Dive (lines 517-542) → `references/risk-management.md`
- §18 Excellence Framework (lines 544-561) → `references/excellence.md`
- §19 Best Practices Library (lines 563-573) → `references/best-practices.md`
- §20 Case Studies (lines 575-584) → `references/case-studies.md`
- §21 Resources & References (lines 586-592) → `references/resources.md`

### Priority 2: Replace §9 Generic Templates

Remove or replace with meteorologist-specific scenarios:
- Scenario: "How do we improve forecast accuracy?"
- Scenario: "A colleague misinterprets model output — how to correct?"
- Scenario: "Media requests dramatic forecast — how to balance accuracy vs engagement?"

### Priority 3: Trim Self-Score Section

Lines 492-493 and 598-609 are redundant. Keep only essential test cases.

---

## Anti-Patterns Detected

| # | Anti-Pattern | Present |
|---|--------------|---------|
| 1 | Scope Creep (multiple domains) | ❌ |
| 2 | Shallow Depth (generic content) | ❌ |
| 3 | Metadata Errors | ❌ |
| 4 | Token Waste (long SKILL.md) | ✅ |
| 5 | False Activation (bloat triggers) | ❌ |
| 6 | Translation Drift | ❌ |

---

## Recommendation

**Status:** Expert ⭐ — Requires fixes to pass token budget gate

**Action:** Fix token budget issues by offloading to `references/` as specified above. Re-score after fixes.

---

## Metadata Verification

| Field | Status |
|-------|--------|
| name | ✅ meteorologist |
| description | ✅ ≤263 chars, trigger verbs front-loaded |
| author | ✅ neo.ai |
| version | ✅ 3.0.0 |
| difficulty | ✅ expert |
| category | ✅ government |
| tags | ✅ 5 tags |
| platforms | ⚠️ Missing from metadata (but §5 absent) |

**Note:** platforms field should be added per §7.2 spec, or §5 Platform Support section should be added.
