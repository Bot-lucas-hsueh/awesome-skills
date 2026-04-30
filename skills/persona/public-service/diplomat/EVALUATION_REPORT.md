# EVALUATION_REPORT: diplomat Skill

**Skill Path:** `skills/public-service/diplomat/SKILL.md`  
**Version:** 3.0.0  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24  

---

## Executive Summary

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| **Prompt** | 8.0 | ×0.20 | 1.60 |
| **Domain Knowledge** | 6.5 | ×0.25 | 1.63 |
| **Workflow** | 5.0 | ×0.15 | 0.75 |
| **Risk** | 7.0 | ×0.10 | 0.70 |
| **Examples** | 6.0 | ×0.20 | 1.20 |
| **Metadata** | 7.5 | ×0.10 | 0.75 |
| **TOTAL** | | | **6.63/10** |

**Classification:** Community (needs upgrade to Expert ≥7.0)  

---

## Before/After Analysis

### Before (Current State)
- System prompt is strong with clear diplomat identity, decision gates, and thinking patterns
- Good risk coverage with diplomatic-specific incidents
- Decent scope coverage across 8 function areas
- Professional toolkit references real resources (Vienna Convention, etc.)

### After (Target State)
- Workflow should be diplomatic-specific (not generic PM)
- Domain deep dive needs real diplomatic knowledge (not generic placeholder tables)
- Examples need authentic diplomatic scenarios (not consulting templates)
- Reduce bloat by moving content to references/

---

## Specific Issues Found

### 🔴 Critical Issues

**1. Workflow Mismatch (§8)**
- **Problem:** Generic project management workflow (Discovery → Analysis → Implementation → Review) doesn't reflect how diplomats actually work
- **Impact:** AI will apply wrong problem-solving approach for diplomatic situations
- **Fix:** Replace with diplomatic-specific phases:
  - **Phase 1: Intelligence & Assessment** — Gather info, assess context, identify stakeholders
  - **Phase 2: Strategy Development** — Define objectives, identify leverage, plan approach
  - **Phase 3: Engagement & Negotiation** — Conduct discussions, manage dynamics, adapt
  - **Phase 4: Agreement & Follow-through** — Document outcomes, coordinate implementation

**2. Domain Deep Dive is Placeholder (§16)**
- **Problem:** Tables contain generic content ("Foundation", "Implementation", "Optimization") with no actual diplomatic knowledge
- **Impact:** No real domain expertise conveyed
- **Fix:** Replace with specific diplomatic knowledge areas:
  - Bilateral negotiations, multilateral forums, summit diplomacy
  - Diplomatic reporting (cable formats), intelligence assessment
  - Protocol (precedence, ceremonies, gifts), consular operations
  - Sanctions regimes, visa policy, diplomatic immunity

### 🟠 High Issues

**3. Generic Scenarios (§9)**
- **Problem:** Scenarios read like consulting templates, not diplomatic situations
- **Example:** "Initial Consultation" — "What is your current level of experience?" (generic)
- **Fix:** Use authentic diplomatic contexts:
  - Pre-negotiation briefing, post-meeting debrief
  - Crisis response (evacuation, kidnapping, attack)
  - Summit preparation, bilateral visit planning
  - Diplomatic note drafting, demarche preparation

**4. Content Bloat (>500 lines)**
- **Problem:** 680 lines exceeds token budget; much content is generic
- **Fix:** Move to references/:
  - §7 Standards → references/07-standards.md
  - §10 Pitfalls → references/10-pitfalls.md  
  - §17 Risk Register → references/17-risk.md
  - §18-21 frameworks/cases → references/18-21-frameworks.md

**5. Description Duplication**
- **Problem:** "Expert-level Diplomat skill..." repeated in description
- **Fix:** Trim to single concise description ≤263 chars

### 🟡 Medium Issues

**6. Knowledge Maturity Model (§16.2)**
- **Problem:** Generic 5-level model not diplomatic-specific
- **Fix:** Define diplomatic competency levels (Attaché → Counselor → Deputy Chief → Ambassador)

**7. Excellence Framework (§18)**
- **Problem:** Generic "Good/Great/World-Class" not specific to diplomacy
- **Fix:** Remove or make diplomatic-specific

---

## Concrete Fix Recommendations

| Priority | Section | Action | Est. Lines |
|----------|---------|--------|------------|
| 🔴 | §8 Workflow | Replace with diplomatic 4-phase workflow | Replace 88 lines |
| 🔴 | §16 Domain Deep Dive | Fill with real diplomatic knowledge areas | Replace 20 lines |
| 🟠 | §9 Examples | Rewrite with 4 authentic diplomatic scenarios | Rewrite 190 lines |
| 🟠 | Body | Move §§7,10,17-21 to references/ | Save ~150 lines |
| 🟠 | YAML | Fix description duplication | 1 line |
| 🟡 | §18-21 | Remove or integrate into domain section | Save ~80 lines |

---

## Scoring Rationale

### Prompt (8.0/10)
- ✅ Clear 25+ year diplomat identity
- ✅ 5 decision gates with fail actions
- ✅ 5 thinking patterns (National Interest, Reciprocity, etc.)
- ✅ Communication style defined
- ⚠️ Could add specific diplomatic frameworks

### Domain Knowledge (6.5/10)
- ✅ 8 function areas well covered
- ✅ Core philosophy (ZOPA, 6 principles) solid
- ✅ Professional toolkit references real resources
- ❌ §16 Domain Deep Dive is placeholder
- ⚠️ Missing: diplomatic reporting formats, specific protocol rules

### Workflow (5.0/10)
- ✅ 4 phases with clear structure
- ✅ Done/Fail criteria defined
- ❌ Generic PM workflow, not diplomatic-specific

### Risk (7.0/10)
- ✅ Good risk table with 7 items
- ✅ Diplomatic-specific risks (gauge, cultural misstep)
- ✅ Mitigation strategies provided
- ⚠️ Some risks generic (§17 risk register)

### Examples (6.0/10)
- ✅ 4 scenario types cover different use cases
- ✅ Structured response format
- ❌ Not authentic diplomatic scenarios
- ❌ Generic "consulting" language

### Metadata (7.5/10)
- ✅ All required fields present
- ✅ Correct category, difficulty, tags
- ⚠️ Description has duplication
- ⚠️ text_score/runtime_score in metadata is unusual

---

## Recommended Next Steps

1. **Rewrite §8 Workflow** — Replace with diplomatic-specific phases
2. **Rewrite §16 Domain Deep Dive** — Add real diplomatic knowledge
3. **Rewrite §9 Examples** — Create authentic diplomatic scenarios
4. **Trim body** — Move non-essential sections to references/
5. **Verify** — Run through skill-writer QA checklist

---

## Result

| Current Score | Target Score | Action Required |
|---------------|--------------|-----------------|
| **6.63/10** | ≥7.0/10 | Upgrade from Community to Expert |

The skill has strong foundational elements (system prompt, risk section, core philosophy) but needs workflow and examples rewritten to be diplomatic-specific rather than generic consulting/PM patterns.