# Evaluation Report: petition-officer

**Skill Path:** `skills/government/petition-officer/SKILL.md`  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimension Quality Rubric

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt Depth** | 20% | 9/10 | Structured prompt with 12+ years, Chief Petition Officer identity, administrative law expertise. Decision gates (4 gates), thinking patterns (4 dimensions: due process priority, dual accountability, fact-finding discipline, realistic resolution), communication style (clear expectations, procedure transparency, neutral language, helpful direction). |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks: petition resolution framework (intake → classify → resolve/escalate/refer → response/closure), complaint handling frameworks (administrative grievance, mediation, expedited review, class complaint). Metrics: first contact resolution, response time (<3 days), resolution time (<30 days). Tools: case management systems, ADR, FOIA, CRM, department liaison protocols. |
| **Workflow Actionability** | 15% | 9/10 | Two detailed workflows: complaint processing protocol (4 phases with sub-steps), citizen communication template (5-step: acknowledge→investigate→decide→respond→close). Clear process flow with specific actions at each step. |
| **Risk Documentation** | 10% | 8/10 | 5 risks with severity: conflict of interest (🔴 High), retaliation perception (🔴 High), procedural errors (🔴 High), information mishandling (🔴 High), promise overreach (🔴 High). Domain-specific mitigations. Disclaimer about not providing legal advice. |
| **Example Quality** | 20% | 8/10 | 2 strong scenarios: standard complaint (building permit delay - shows routing and resolution), cross-jurisdictional complaint (federal building noise - shows jurisdictional limits). Good anti-pattern section. Minor: generic scenarios in §9.1-9.4 are template-like. |
| **Metadata Completeness** | 10% | 7/10 | All 9 fields present but description has redundancy ("Expert petition officer specializing in public complaint handling..." appears twice). Description is 232 chars. Tags: petition, grievance, public-complaint, administrative, citizen-services. |

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

1. **Petition resolution framework** — Clear ASCII diagram showing intake → classification → resolve/escalate/refer → closure workflow
2. **Dual accountability principle** — Balances citizen's right to be heard with government's need for orderly administration
3. **Performance metrics** — Response time (<3 days), resolution time (<30 days), first contact resolution targets
4. **Jurisdictional awareness** — Clear about when to escalate, refer, or explain limitations (e.g., federal building case)
5. **Documentation emphasis** — "If it isn't documented, it didn't happen" - strong records focus

---

## Areas for Improvement

1. **Description redundancy** — "Expert petition officer specializing in public complaint handling..." appears twice
2. **Generic scenarios in §9** — Scenarios 1-4 use generic templates
3. **Missing platform section** (§5) — No platform-specific installation guidance
4. **Section 16-20 boilerplate** — Domain Deep Dive, Risk Management sections add ~100 lines

---

## Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| **Medium** | Fix description redundancy - remove duplicate text | Clarity |
| **Medium** | Remove or relocate boilerplate sections (§16-20) to references/ | Token savings |
| **Medium** | Add platform-specific guidance in §5 | Installation clarity |
| **Low** | Replace generic §9 scenarios with petition-officer-specific ones | Example quality |

---

## Anti-Pattern Check

| # | Anti-Pattern | Status |
|---|--------------|--------|
| 1 | Defensive responses | ✅ Fixed - "acknowledge first" |
| 2 | Procedural rigidity | ✅ Addressed - "apply spirit of regulations" |
| 3 | Promise without authority | ✅ Addressed - "stay within defined authority" |
| 4 | Incomplete documentation | ✅ Addressed - emphasis on records |
| 5 | Tunnel vision | ✅ Addressed - "consider both citizen and administrative viewpoints" |

---

## Conclusion

**Tier: Expert ⭐** — This skill demonstrates strong administrative grievance expertise with proper process orientation, dual accountability principle, and clear jurisdictional awareness. The main issues are description redundancy and boilerplate content. No critical blockers; suitable for production use with minor cleanup.