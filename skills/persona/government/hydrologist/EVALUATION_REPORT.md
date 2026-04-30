# Evaluation Report: hydrologist

**Skill Path:** `skills/government/hydrologist/SKILL.md`  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimension Quality Rubric

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt Depth** | 20% | 9/10 | Structured prompt with 18+ years experience, USGS-equivalent identity, decision gates (3 gates), thinking patterns (4 dimensions), communication style. Distinct domain-specific heuristics. |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks: flood forecasting (NWS procedures), watershed modeling (HEC-HMS/RAS), water supply assessment. Quantified metrics: AEP, bankfull discharge, baseflow index, flashiness index with target ranges. Real tools: USGS NWIS, NWS RFC, FEMA Flood Map Service. |
| **Workflow Actionability** | 15% | 9/10 | Two detailed workflows: flood forecast interpretation (4 phases with sub-steps), water supply assessment (5 steps). Each phase has templates and checkpoints. Failure criteria implicit in uncertainty communication. |
| **Risk Documentation** | 10% | 9/10 | 4 risks with severity ratings: forecast inaccuracy (🔴 High), data misapplication (🔴 High), model misuse (🔴 High), outdated info (🟡 Medium). Domain-specific mitigations. Important disclaimer about probabilistic forecasts. |
| **Example Quality** | 20% | 8/10 | 2 strong scenarios: flood forecast interpretation (stage-impact translation), watershed development impact (with curve number/flow calculations). Good anti-pattern section with ❌/✅ contrasts. Minor: generic scenarios in §9.1-9.4 are template-like. |
| **Metadata Completeness** | 10% | 8/10 | All 9 fields present. Description is 263 chars (at limit). Tags include government, hydrology, water-resources, flood-forecasting, environmental. Slight issue: description could be tighter (no "Use when" redundancy). |

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

1. **Comprehensive hydrologic frameworks** — Flood risk assessment flows from precipitation through watershed response to impact translation (ASCII diagram)
2. **Uncertainty quantification methodology** — Explicit emphasis on ranges vs. point estimates; distinguishes measurement error from model uncertainty
3. **NWS/USGS tools integration** — References real tools: NWIS, AHPS, River Forecast Centers
4. **Detailed flood forecast workflow** — 4-phase workflow with situational awareness, impact assessment, uncertainty communication, decision support
5. **Land use impact quantification** — Provides actual curve number changes, time of concentration reduction, peak discharge increases (+87%)

---

## Areas for Improvement

1. **Generic scenarios in §9** — Scenarios 1-4 use generic "new client" templates rather than hydrologist-specific situations
2. **Description character count** — At 263 chars, borderline for activation with many skills installed
3. **Missing platform section** (§5) — No platform-specific installation guidance (OpenCode, Claude Code, etc.)
4. **Section 16-21 bloat** — Domain Deep Dive, Risk Management, Excellence Framework sections appear boilerplate and add ~120 lines without domain-specific content

---

## Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| **Medium** | Remove or relocate boilerplate sections (§16-21) to references/ | Token savings, focus |
| **Medium** | Add platform-specific guidance in §5 | Installation clarity |
| **Low** | Tighten description to <250 chars | Activation reliability |
| **Low** | Replace generic §9 scenarios with hydrologist-specific ones | Example quality |

---

## Anti-Pattern Check

| # | Anti-Pattern | Status |
|---|--------------|--------|
| 1 | Presenting point forecasts as certain | ✅ Fixed - explicitly provides ranges |
| 2 | Ignoring antecedent conditions | ✅ Addressed - "Dry vs. saturated basin produces dramatically different runoff" |
| 3 | Extrapolating beyond data | ✅ Addressed - warns about 30-year record limitations |
| 4 | Confusing stage and flow | ✅ Addressed - distinguishes in communication style |

---

## Conclusion

**Tier: Expert ⭐** — This skill demonstrates strong hydrological domain expertise with proper uncertainty quantification, realistic frameworks, and appropriate risk disclaimers. The main areas for improvement are reducing boilerplate content and adding platform installation guidance. No critical blockers; suitable for production use.