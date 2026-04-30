# Evaluation Report: civil-servant

**Skill Path:** `skills/government/civil-servant/SKILL.md`  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimension Quality Rubric

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt Depth** | 20% | 9/10 | Structured prompt with 15+ years, GS-15 equivalent, multi-agency experience. Decision gates (3 gates), thinking patterns (4 dimensions: legal authority, process integrity, stakeholder balance, implementation reality), communication style (memo-format, regulatory register, action-oriented). |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks: regulatory decision framework ( OMB A-4), policy memo development (6-step). Quantified metrics: regulatory cost per affected party, timeline to implementation, public participation rate. Tools: OMB Circular A-4, APA, Regulatory Flexibility Act, Paperwork Reduction Act, regulations.gov. |
| **Workflow Actionability** | 15% | 9/10 | Two detailed workflows: regulatory impact assessment (5 phases), policy memo development (6 steps). Each phase has sub-steps and specific outputs. Clear templates for decision documentation. |
| **Risk Documentation** | 10% | 8/10 | 4 risks with severity: legal error (🔴 High), jurisdictional misapplication (🔴 High), outdated information (🟡 Medium), political sensitivity (🟡 Medium). Domain-specific mitigations. Disclaimer about not providing legal advice present. |
| **Example Quality** | 20% | 8/10 | 2 strong scenarios: regulatory impact assessment request (emissions standards), interagency coordination challenge (AI governance). Good anti-pattern section. Minor: generic scenarios in §9.1-9.4 are template-like. |
| **Metadata Completeness** | 10% | 7/10 | All 9 fields present but description has redundancy ("Senior civil servant and policy analyst specializing in public policy..." appears twice). Description is 237 chars. Tags: government, policy, civil servant, regulatory, public-administration. |

---

## Weighted Score Calculation

```
Score = (Prompt×0.20) + (Domain×0.25) + (Workflow×0.15) + (Risk×0.10) + (Examples×0.20) + (Metadata×0.10)
      = (9×0.20) + (9×0.25) + (9×0.15) + (8×0.10) + (8×0.20) + (7×0.10)
      = 1.80 + 2.25 + 1.35 + 0.80 + 1.60 + 0.70
      = 8.50
```

**Final Score: 8.50/10 → Expert ⭐**

---

## Tier Classification

| Tier | Range | Result |
|------|-------|--------|
| Basic | 1-3 | ❌ |
| Community | 4-6 | ❌ |
| Expert | 7-8.9 | ✅ |
| Exemplary | 9+ | ❌ |

---

## Strengths

1. **Regulatory impact framework** — OMB A-4 compliance with cost-benefit analysis methodology
2. **Legal authority emphasis** — "Everything must trace to lawful delegation" - strong grounding in administrative law
3. **Process integrity awareness** — APA requirements, notice-and-comment, interagency review properly addressed
4. **Implementability focus** — Explicit consideration of operational capacity, resources, training
5. **Clear scope limitations** — Distinguishes policy analysis from legal advice, legislative drafting, advocacy

---

## Areas for Improvement

1. **Description redundancy** — "Senior civil servant and policy analyst specializing in public policy..." appears twice in description
2. **Generic scenarios in §9** — Scenarios 1-4 use generic templates
3. **Missing platform section** (§5) — No platform-specific installation guidance
4. **Section 16-20 boilerplate** — Domain Deep Dive, Risk Management sections add ~100 lines

---

## Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| **Medium** | Fix description redundancy - remove duplicate text | Clarity |
| **Medium** | Remove or relocate boilerplate sections (§16-20) | Token savings |
| **Medium** | Add platform-specific guidance in §5 | Installation clarity |
| **Low** | Replace generic §9 scenarios with civil-servant-specific ones | Example quality |

---

## Anti-Pattern Check

| # | Anti-Pattern | Status |
|---|--------------|--------|
| 1 | Analysis paralysis | ✅ Fixed - recommends decision deadlines, phased analysis |
| 2 | Skipping the baseline | ✅ Addressed - "No Action" baseline emphasized |
| 3 | Treating stakeholders as obstacles | ✅ Addressed - early engagement recommended |
| 4 | Outdated legal citations | ✅ Addressed - verification recommended |

---

## Conclusion

**Tier: Expert ⭐** — This skill demonstrates strong public administration expertise with proper regulatory framework knowledge (OMB A-4, APA), legal authority grounding, and clear process orientation. The main issues are description redundancy and boilerplate content. No critical blockers; suitable for production use with minor cleanup.