# Evaluation Report: statistician

**Skill Path:** `skills/government/statistician/SKILL.md`  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimension Quality Rubric

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt Depth** | 20% | 9/10 | Structured prompt with 15+ years, national statistical office identity, survey methodology expertise. Decision gates (4 gates), thinking patterns (4 dimensions with statistical perspectives), communication style (margin of error aware, methodology visible). |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks: statistical validity (internal/external, precision/accuracy), survey design process (4 phases), data analysis protocol (5 steps). Quantified metrics: margin of error, response rate, statistical power, coefficient of variation with targets. Tools: R, SPSS, sample size calculators, IPUMS. |
| **Workflow Actionability** | 15% | 9/10 | Two detailed workflows: survey design process (4 phases with sub-steps), data analysis protocol (5 steps with Explore→Assess→Analyze→Synthesize→Communicate). Each phase has templates and checkpoints. |
| **Risk Documentation** | 10% | 9/10 | 5 risks with severity ratings: misleading statistics (🔴 High), sampling bias (🔴 High), p-hacking (🔴 High), privacy violations (🔴 High), cherry-picking (🟡 Medium). Domain-specific mitigations. Important disclaimer about statistical vs. practical significance. |
| **Example Quality** | 20% | 8/10 | 2 strong scenarios: survey analysis (with actual percentages, margins of error, confidence intervals), small sample size (shows limitations, recommends n≥400). Good anti-pattern section with ❌/✅ contrasts. Minor: generic scenarios in §9.1-9.4 are template-like. |
| **Metadata Completeness** | 10% | 8/10 | All 9 fields present. Description is 221 chars (within limit). Tags: statistics, data-analysis, census, survey, population, government-data. Good. |

---

## Weighted Score Calculation

```
Score = (Prompt×0.20) + (Domain×0.25) + (Workflow×0.15) + (Risk×0.10) + (Examples×0.20) + (Metadata×0.10)
      = (9×0.20) + (9×0.25) + (9×0.15) + (9×0.10) + (8×0.20) + (8×0.10)
      = 1.80 + 2.25 + 1.35 + 0.90 + 1.60 + 0.80
      = 8.70
```

**Final Score: 8.70/10 → Expert ⭐**

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

1. **Statistical validity framework** — Comprehensive diagram showing internal/external validity, precision/accuracy dimensions
2. **Rigorous methodology emphasis** — Explicit about representativeness, uncertainty, correlation vs. causation, garbage in/garbage out
3. **Margin of error integration** — Consistently includes confidence intervals, significance levels in examples
4. **P-hacking and data dredging awareness** — Strong risk section addressing this common statistical pitfall
5. **Clear limitations communication** — Shows what can/cannot be done with small samples (n=45 case)

---

## Areas for Improvement

1. **Generic scenarios in §9** — Scenarios 1-4 use generic "new client" templates rather than statistician-specific situations
2. **Missing platform section** (§5) — No platform-specific installation guidance
3. **Tool references incomplete** — §6 lists tools but some entries truncated (R, SPSS show without full descriptions)
4. **Section 16-21 boilerplate** — Domain Deep Dive, Risk Management, Excellence Framework sections add ~130 lines without domain-specific content

---

## Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| **Medium** | Remove or relocate boilerplate sections (§16-21) to references/ | Token savings, focus |
| **Medium** | Add platform-specific guidance in §5 | Installation clarity |
| **Low** | Fix truncated tool references in §6 | Completeness |
| **Low** | Replace generic §9 scenarios with statistician-specific ones | Example quality |

---

## Anti-Pattern Check

| # | Anti-Pattern | Status |
|---|--------------|--------|
| 1 | Ignoring margin of error | ✅ Fixed - explicitly requires confidence intervals |
| 2 | Conflating correlation with causation | ✅ Addressed - "associated with" language emphasized |
| 3 | Underpowered analysis | ✅ Addressed - warns about small samples, recommends power calculation |
| 4 | P-hacking | ✅ Addressed - pre-specification, multiple comparison corrections |
| 5 | Cherry-picking | ✅ Addressed - transparency about exclusions |

---

## Conclusion

**Tier: Expert ⭐** — This skill demonstrates strong statistical methodology with proper uncertainty quantification, representative sampling emphasis, and clear limitations. The main areas for improvement are reducing boilerplate content and adding platform installation guidance. No critical blockers; suitable for production use.