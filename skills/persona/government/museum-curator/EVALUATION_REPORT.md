# Skill Evaluation Report: museum-curator

**Date:** 2026-03-24  
**Evaluator:** skill-writer  
**Version:** 3.0.0

---

## Summary

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 8.5 | 20% | 1.70 |
| Domain Knowledge Density | 7.5 | 25% | 1.88 |
| Workflow Actionability | 7.0 | 15% | 1.05 |
| Risk Documentation | 9.0 | 10% | 0.90 |
| Example Quality | 7.0 | 20% | 1.40 |
| Metadata Completeness | 8.0 | 10% | 0.80 |
| **TOTAL** | | | **7.73** |

**Tier: Expert ⭐**

---

## Dimension Analysis

### 1. System Prompt Depth (8.5/10)
- ✅ §1.1 Role definition with 15+ years experience
- ✅ §1.2 Decision Framework with 3 gates table
- ✅ §1.3 Thinking Patterns with 4 dimensions
- ✅ §1.4 Communication Style defined
- ⚠️ System prompt ~25 lines, good but could be more dense

### 2. Domain Knowledge Density (7.5/10)
- ✅ Visitor-Centered Exhibition Framework (visual)
- ✅ Conservation metrics table (light, RH, temperature)
- ✅ Exhibition design frameworks table (3 frameworks)
- ⚠️ Missing quantified decision thresholds in frameworks

### 3. Workflow Actionability (7.0/15)
- ✅ Exhibition Development (3 phases with sub-steps)
- ✅ Artifact Interpretation (5 steps)
- ⚠️ No explicit "deliverables" per phase
- ⚠️ No measurable output tests

### 4. Risk Documentation (9.0/10)
- ✅ 5 risks with severity ratings
- ✅ Each risk has description AND mitigation
- ✅ Important disclaimer box
- **Signal**: Domain-specific mitigations for provenance, cultural offense, conservation

### 5. Example Quality (7.0/10)
- ✅ 2 real museum scenarios (Silk Road exhibition, culturally sensitive material)
- ✅ Edge case covered (sacred indigenous artifacts)
- ❌ Sections 9.1-9.4 contain generic placeholder content ("Initial Consultation", "Problem Resolution", "Strategic Planning", "Quality Assurance") - NOT museum-specific
- **Anti-Pattern**: Generic consultant scenarios are filler content

### 6. Metadata Completeness (8.0/10)
- ✅ 9 fields present (author, version, difficulty, category, tags)
- ⚠️ Description: 156 chars - short, could be more descriptive
- ⚠️ No platforms field
- ⚠️ Score discrepancy: metadata shows 8.5 but self-score claims 9.5

---

## Critical Issues

| Issue | Severity | Fix |
|-------|----------|-----|
| Sections 9.1-9.4 are generic consultant filler | 🔴 High | Remove or replace with museum-specific scenarios |
| Line count 583, exceeds domain limit of 600 but borderline | 🟡 Medium | Minor concern |
| Self-score (9.5) does not match actual quality (~7.7) | 🟡 Medium | Update metadata to reflect actual score |

---

## Anti-Patterns Detected

| Anti-Pattern | Location | Severity |
|--------------|----------|----------|
| Generic placeholder content | §9 Scenario Examples (lines 295-424) | 🔴 High |
| Knowledge maturity model (irrelevant) | §16 (lines 470-488) | 🟡 Medium |
| Risk register (generic template) | §17 (lines 493-518) | 🟡 Medium |
| Excellence framework (generic template) | §18-21 (lines 522-587) | 🟡 Medium |

**Total filler content: ~130 lines** (22% of file)

---

## Signal-to-Token Efficiency
```
= (3×3) + (2×5) + (5×2) = 9 + 10 + 10 = 29
÷ 5.83 = 4.97 → Exemplary
```
**Status: ✅ PASS** (efficiency high despite quality issues)

---

## Conclusion

**museum-curator** is an Expert-level skill with significant quality issues:
1. ~130 lines of generic filler content (sections 16-21) should be removed
2. Self-score (9.5) significantly overestimates actual quality (7.73)
3. Scenario examples section mixes real museum content with generic filler

**Recommendation**: 
- Remove sections 16-21 (generic template content)
- Update self-score to 7.5-8.0
- Expand §9 scenario examples with 2-3 more museum-specific flows

After fixes: Potential for Exemplary tier (8.5+)

---

*Evaluation complete. Next: rescue-worker*
