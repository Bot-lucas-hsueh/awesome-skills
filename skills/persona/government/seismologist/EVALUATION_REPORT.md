# Skill Evaluation Report — seismologist

**Skill:** skills/government/seismologist/SKILL.md  
**Version:** 3.0.0  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimensional Quality Rubric Scores

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Role + 3 gates + thinking patterns. Probability vs certainty focus is crucial. |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks (PSHA, DSHA, GMPE, ETAS), USGS tools, correct terminology (MMI, PGA). |
| **Workflow Actionability** | 15% | 9/10 | 4-phase hazard assessment + EEW interpretation. Technical but actionable. |
| **Risk Documentation** | 10% | 9/10 | 4 risks (3 🔴 High, 1 🟡 Medium). Prediction misrepresentation + hazard-risk conflation emphasized. |
| **Example Quality** | 20% | 7/10 | 9.1 building code + 9.2 aftershock are excellent. But §9 scenarios are generic. |
| **Metadata Completeness** | 10% | 10/10 | All 9 fields present. |

**Weighted Score:** 8.55  
**Tier:** Expert ⭐

---

## Strengths

1. **Seismic Risk Framework** (§4.1) — Clear hazard × exposure × vulnerability formula
2. **Correct terminology** — Mw vs MMI vs PGA used correctly
3. **PSHA/DSHA frameworks** — Technical methodologies properly explained
4. **USGS tools integration** — ShakeAlert, PAGER, NSHM with specific uses

---

## Critical Issues

| Issue | Severity | Action Required |
|-------|----------|----------------|
| **SKILL.md body 597 lines** | 🔴 | Exceeds 500-line limit. Must offload to `references/` |
| **Generic §9 scenarios** | 🟡 | Template placeholders |
| **Section 16-21 bloat** | 🟡 | Auto-generated |

---

## Required Fixes

### Priority 1: Token Budget

Move §16-21 to `references/`.

### Priority 2: §9 Templates

Add seismologist-specific scenarios (e.g., "How to communicate aftershock risk to the public?").

---

## Metadata Verification

| Field | Status |
|-------|--------|
| name | ✅ seismologist |
| description | ✅ 250 chars |
| platforms | ⚠️ Missing |

---

## Recommendation

**Status:** Expert ⭐ — Token budget fix required
