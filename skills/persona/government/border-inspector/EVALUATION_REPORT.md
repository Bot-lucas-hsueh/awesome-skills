# Skill Evaluation Report — border-inspector

**Skill:** skills/government/border-inspector/SKILL.md  
**Version:** 3.0.0  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimensional Quality Rubric Scores

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Role + 3 gates + thinking patterns. Strong document integrity + admissibility focus. |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks (INA §212(a), visa category analysis, document fraud checklist), specific tools (TECS, SAVE, IDENT). |
| **Workflow Actionability** | 15% | 9/10 | 4-phase primary inspection + fraud indicators checklist. Each step specific. |
| **Risk Documentation** | 10% | 9/10 | 4 risks (all 🔴 High), domain-specific (document fraud miss, civil rights violation). |
| **Example Quality** | 20% | 7/10 | 9.1 VWP eligibility + 9.2 marriage fraud are excellent. But §9 scenarios are generic. |
| **Metadata Completeness** | 10% | 10/10 | All 9 fields present. |

**Weighted Score:** 8.55  
**Tier:** Expert ⭐

---

## Strengths

1. **Traveler Inspection Framework** (§4.1) — Clear flowchart from primary through decision
2. **Document Fraud Indicators** (§8.2) — Comprehensive physical + electronic + database checklist
3. **INA-referenced** — Cites specific sections (INA §212(a))
4. **Real tools** — TECS, SAVE, IDENT, NCIC with specific purposes

---

## Critical Issues

| Issue | Severity | Action Required |
|-------|----------|----------------|
| **SKILL.md body 600 lines** | 🔴 | Exceeds 500-line limit. Must offload to `references/` |
| **Generic §9 scenarios** | 🟡 | Template placeholders |
| **Section 16-21 bloat** | 🟡 | Auto-generated |

---

## Required Fixes

### Priority 1: Token Budget

Move §16-21 to `references/`.

### Priority 2: §9 Templates

Add border-specific scenarios (e.g., "How to handle a traveler with expired visa and no ESTA?").

---

## Metadata Verification

| Field | Status |
|-------|--------|
| name | ✅ border-inspector |
| description | ✅ 196 chars |
| platforms | ⚠️ Missing |

---

## Recommendation

**Status:** Expert ⭐ — Token budget fix required
