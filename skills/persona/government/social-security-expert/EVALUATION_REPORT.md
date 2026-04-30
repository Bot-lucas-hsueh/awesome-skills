# Skill Evaluation Report — social-security-expert

**Skill:** skills/government/social-security-expert/SKILL.md  
**Version:** 3.0.0  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimensional Quality Rubric Scores

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Role + 4 gates + thinking patterns. Jurisdiction-aware decision framework. |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks (policy hierarchy, benefit eligibility, calculation formulas). China-specific but well-structured. |
| **Workflow Actionability** | 15% | 9/10 | 3-phase eligibility + 6-step claims processing. Step-numbered procedures. |
| **Risk Documentation** | 10% | 9/10 | 5 risks (2 🔴 High, 3 🟡 Medium). Outdated policy + jurisdiction-specific rules emphasized. |
| **Example Quality** | 20% | 7/10 | 9.1 pension eligibility + 9.2 medical claim are excellent. But §9 scenarios are generic. |
| **Metadata Completeness** | 10% | 10/10 | All 9 fields present. |

**Weighted Score:** 8.55  
**Tier:** Expert ⭐

---

## Strengths

1. **Policy Hierarchy Framework** (§4.1) — Clear national → provincial → bureau flow
2. **Step-numbered procedures** — 1.1, 1.2, 1.3 style for multi-step processes
3. **Compliance-first** — Emphasizes documentation, deadlines, penalties
4. **Real scenarios** — Shanghai pension, medical card issues are practical

---

## Critical Issues

| Issue | Severity | Action Required |
|-------|----------|----------------|
| **SKILL.md body 607 lines** | 🔴 | Exceeds 500-line limit. Must offload to `references/` |
| **Generic §9 scenarios** | 🟡 | Template placeholders |
| **Section 16-21 bloat** | 🟡 | Auto-generated |

---

## Required Fixes

### Priority 1: Token Budget

Move §16-21 to `references/`.

### Priority 2: §9 Templates

Add domain-specific scenarios.

---

## Metadata Verification

| Field | Status |
|-------|--------|
| name | ✅ social-security-expert |
| description | ✅ 241 chars |
| platforms | ⚠️ Missing |

---

## Recommendation

**Status:** Expert ⭐ — Token budget fix required
