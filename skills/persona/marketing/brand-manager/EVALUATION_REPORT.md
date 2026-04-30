# Evaluation Report: brand-manager

## Skill Overview
- **Name**: brand-manager
- **Category**: marketing
- **Current Score**: 9.5/10
- **Version**: 3.0.0

---

## 6-Dimension Quality Rubric

| Dimension | Score (1-10) | Assessment |
|-----------|--------------|------------|
| **System Prompt Depth** | 9 | Rich identity with 12+ years experience; includes Keller Brand Equity Model, Brand Identity Prism, JTBD framework; decision framework with quality gates |
| **Domain Knowledge Density** | 9 | Deep brand frameworks (positioning statement, message hierarchy, brand essence); quantified metrics (NPS benchmarks by industry); real scenarios |
| **Workflow Actionability** | 8 | 4-phase workflow with templates; creative brief template detailed; has done/fail criteria but some generic sections (§8-21 appear template-filler) |
| **Risk Documentation** | 8 | 4+ risks with severity and mitigation; brand dilution, messaging inconsistency, cultural misstep, trademark, brand crisis |
| **Example Quality** | 8 | 4 scenario examples; 5 anti-patterns with wrong/correct contrasts; good coverage but some scenarios generic |
| **Metadata Completeness** | 9 | All 9 fields present; version history; comprehensive tags |

---

## Weighted Score Calculation

```
Score = (9×0.20) + (9×0.25) + (8×0.15) + (8×0.10) + (8×0.20) + (9×0.10)
      = 1.8 + 2.25 + 1.2 + 0.8 + 1.6 + 0.9
      = 8.55 → Expert ⭐
```

**Tier Classification**: Expert (7.0-8.9)

---

## Strengths

1. **Deep Domain Frameworks**: Keller CBBE, Brand Identity Prism, JTBD - all properly integrated
2. **Quantified Metrics**: NPS benchmarks (SaaS 30-50, FMCG 20-40, etc.), SOV/SOM correlation
3. **Creative Brief Template**: Comprehensive with done/fail criteria per field
4. **Anti-Patterns**: 5 well-crafted brand-specific pitfalls with solutions
5. **No Fabrications**: Explicit commitment to not fabricating competitive data

---

## Areas for Improvement

1. **Token Bloat**: Sections §8-21 appear to be template filler (generic "Phase 1-4" content repeated across skills); should move to references/
2. **Missing Platform Support**: No §5 with platform-specific install instructions
3. **Scenario Depth**: Some scenarios (§9-21) are generic template content, not brand-specific examples

---

## Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| High | Move sections §8-21 to references/; reduce SKILL.md to ~400 lines | -200 tokens/invoke |
| Medium | Add §5 Platform Support per standards.md §7.11 | +0.5 metadata score |
| Low | Replace generic §8-21 scenarios with brand-specific examples | +0.5 example score |

---

## Overall Assessment

**Expert ⭐** - This skill demonstrates deep brand management expertise with proper frameworks, quantified metrics, and anti-patterns. The main issue is token bloat from template filler content that should be moved to references/. Once trimmed, this will be Exemplary quality.

---
*Evaluation Date: 2026-03-24*
