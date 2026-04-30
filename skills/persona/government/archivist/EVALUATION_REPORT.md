# Skill Evaluation Report — archivist

**Skill:** skills/government/archivist/SKILL.md  
**Version:** 3.0.0  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimensional Quality Rubric Scores

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Role + 5 gates + thinking patterns + communication style. Strong decision framework. |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks (records lifecycle, appraisal, FOIA exemption analysis), specific standards (EAD, DACS, OAIS). |
| **Workflow Actionability** | 15% | 9/10 | 3-phase records management + 5-step archival processing with clear steps. |
| **Risk Documentation** | 10% | 9/10 | 5 risks (3 🔴 High, 2 🟡 Medium), severity-rated, domain-specific (litigation holds, chain of custody). |
| **Example Quality** | 20% | 7/10 | 9.1 retention schedule + 9.2 FOIA analysis are excellent. But §9 scenarios are generic. |
| **Metadata Completeness** | 10% | 10/10 | All 9 fields present, proper versioning. |

**Weighted Score:** 8.55  
**Tier:** Expert ⭐

---

## Strengths

1. **Records Lifecycle Model** ( §4.1) — Clear visual framework showing creation through disposition
2. **FOIA Exemption Analysis** ( §9.2) — Practical step-by-step guidance with specific exemptions cited
3. **Provenance thinking** — Skill correctly emphasizes chain of custody and original order
4. **Risk-aware** — Litigation hold emphasis is critical and present

---

## Critical Issues

| Issue | Severity | Action Required |
|-------|----------|----------------|
| **SKILL.md body 572 lines** | 🔴 | Exceeds 500-line limit. Must offload to `references/` |
| **Generic §9 scenarios** | 🟡 | Template placeholders not archivist-specific |
| **Section 16-21 bloat** | 🟡 | Auto-generated sections need offloading |

---

## Required Fixes

### Priority 1: Token Budget (SKILL.md > 500 lines)

Move to `references/`:
- §16 Domain Deep Dive (lines 459-476) 
- §17 Risk Management Deep Dive (lines 478-503)
- §18 Excellence Framework (lines 505-522)
- §19 Best Practices Library (lines 525-535)
- §20 Case Studies (lines 537-545)
- §21 Resources & References (lines 547-554)

### Priority 2: Replace §9 Generic Templates

Replace with archivist-specific scenarios (e.g., "How do we handle a records request from litigation?").

---

## Metadata Verification

| Field | Status |
|-------|--------|
| name | ✅ archivist |
| description | ✅ ≤263 chars, trigger verbs |
| author | ✅ neo.ai |
| version | ✅ 3.0.0 |
| difficulty | ✅ intermediate |
| category | ✅ government |
| tags | ✅ 5 tags |
| platforms | ⚠️ Missing |

---

## Recommendation

**Status:** Expert ⭐ — Token budget fix required
