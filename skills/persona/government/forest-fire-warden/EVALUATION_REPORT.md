# Evaluation Report: forest-fire-warden

**Skill Path:** `skills/government/forest-fire-warden/SKILL.md`  
**Evaluator:** skill-writer methodology  
**Date:** 2026-03-24

---

## 6-Dimension Quality Rubric

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt Depth** | 20% | 9/10 | Structured prompt with 20+ years, ICS certified, FFT1/FFT2 qualified. Decision gates (4 gates), thinking patterns (4 dimensions: fire triangle, fire behavior prediction, life safety priority, containment vs control), communication style (urgency when needed, action-oriented, technical accuracy). |
| **Domain Knowledge Density** | 25% | 9/10 | Deep frameworks: fire danger assessment (fuel + weather + topography), defensible space zones, controlled burn planning. Quantified metrics: FWI (>30 = high danger), ERC, wind speed (>20mph restricts burning), relative humidity (<15%), fuel moisture (<10%). NFDRS integration. |
| **Workflow Actionability** | 15% | 9/10 | Two detailed workflows: fire danger assessment procedure (4 phases), controlled burn protocol (6 steps). Each phase has sub-steps, checkpoints, and specific actions. Includes escape routes and safety zones for controlled burns. |
| **Risk Documentation** | 10% | 9/10 | 5 risks with severity: wildfire emergency (🔴 High), controlled burn gone wrong (🔴 High), smoke & air quality (🟡 Medium), property damage (🔴 High), personal safety (🔴 High). Domain-specific mitigations. Strong disclaimer about contacting emergency services. |
| **Example Quality** | 20% | 9/10 | 2 excellent scenarios: fire danger assessment (with FWI ranges table, specific weather thresholds), defensible space guidance (detailed Zone 1/2/3 breakdown with do/don't table). Strong anti-pattern section with ❌/✅ contrasts. Realistic and actionable. |
| **Metadata Completeness** | 10% | 8/10 | All 9 fields present. Description is 218 chars (within limit). Tags: government, emergency, fire-safety, forestry, conservation. Includes Chinese trigger (防火). Good. |

---

## Weighted Score Calculation

```
Score = (Prompt×0.20) + (Domain×0.25) + (Workflow×0.15) + (Risk×0.10) + (Examples×0.20) + (Metadata×0.10)
      = (9×0.20) + (9×0.25) + (9×0.15) + (9×0.10) + (9×0.20) + (8×0.10)
      = 1.80 + 2.25 + 1.35 + 0.90 + 1.80 + 0.80
      = 8.90
```

**Final Score: 8.90/10 → Expert ⭐**

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

1. **Comprehensive fire danger framework** — ASCII diagram showing fuel + weather + topography → fire behavior → danger rating levels
2. **NFDRS metrics integration** — FWI, ERC, wind, humidity, fuel moisture with specific thresholds
3. **Defensible space zones** — Zone 1 (0-30ft), Zone 2 (30-100ft), Zone 3 (100-200ft) with specific actions per zone
4. **Controlled burn protocols** — 6-step protocol with escape routes, safety zones, medical standby
5. **Excellent examples** — Fire danger assessment with FWI range table, defensible space with do/don't comparison table

---

## Areas for Improvement

1. **Generic scenarios in §9** — Scenarios 1-4 use generic templates (should match other sections that are domain-specific)
2. **Missing platform section** (§5) — No platform-specific installation guidance
3. **Section 16-20 boilerplate** — Domain Deep Dive, Risk Management sections add ~100 lines without fire-warden-specific content

---

## Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| **Medium** | Remove or relocate boilerplate sections (§16-20) to references/ | Token savings |
| **Medium** | Add platform-specific guidance in §5 | Installation clarity |
| **Low** | Replace generic §9 scenarios with forest-fire-warden-specific ones | Consistency |

---

## Anti-Pattern Check

| # | Anti-Pattern | Status |
|---|--------------|--------|
| 1 | Ignoring weather conditions | ✅ Fixed - "never conduct burns without checking weather" |
| 2 | Underestimating wind | ✅ Addressed - "wind is #1 factor in fire spread" |
| 3 | Inadequate containment lines | ✅ Addressed - "must extend beyond fire edge" |
| 4 | No contingency plan | ✅ Addressed - "always have escape route" |
| 5 | Public complacency | ✅ Addressed - "don't assume it won't happen here" |

---

## Conclusion

**Tier: Expert ⭐** — This skill demonstrates excellent fire management expertise with comprehensive frameworks, NFDRS metrics integration, and highly actionable examples (defensible space tables, FWI thresholds). The main areas for improvement are boilerplate content removal and platform installation guidance. Strongest of the 5 skills evaluated. Suitable for production use.