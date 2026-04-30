# Skill Evaluation Report: rescue-worker

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
- ✅ §1.1 Role definition with 12+ years experience
- ✅ §1.2 Decision Framework with 4 gates table
- ✅ §1.3 Thinking Patterns with 4 dimensions
- ✅ §1.4 Communication Style (action-oriented, calm under pressure)
- ⚠️ System prompt ~25 lines

### 2. Domain Knowledge Density (7.5/10)
- ✅ RESCUE Incident Command Framework (visual)
- ✅ Response metrics table (response time, triage accuracy)
- ✅ Emergency response frameworks table (ICS, START, Size-Up)
- ⚠️ Missing specific quantified thresholds (e.g., exact response time targets per scenario)

### 3. Workflow Actionability (7.0/10)
- ✅ Emergency Response Protocol (3 phases with sub-steps)
- ✅ Shelter Operations (5 steps)
- ⚠️ No explicit "deliverables" per phase
- ⚠️ No measurable output tests or failure criteria

### 4. Risk Documentation (9.0/10)
- ✅ 5 risks with severity ratings (🔴 High, 🟡 Medium)
- ✅ Each risk has description AND mitigation
- ✅ Important disclaimer box
- **Signal**: Domain-specific mitigations (secondary incidents, vicarious trauma)

### 5. Example Quality (7.0/10)
- ✅ 2 real rescue scenarios (natural disaster response, vulnerable population evacuation)
- ✅ Edge case covered (elderly resident refusing evacuation)
- ❌ Sections 9.1-9.4 contain generic placeholder content
- **Anti-Pattern**: Generic consultant scenarios are filler

### 6. Metadata Completeness (8.0/10)
- ✅ 9 fields present
- ⚠️ Description: 192 chars - short
- ⚠️ No platforms field
- ⚠️ Score discrepancy: metadata shows 8.5 but self-score claims 9.5

---

## Critical Issues

| Issue | Severity | Fix |
|-------|----------|-----|
| Sections 9.1-9.4 are generic consultant filler | 🔴 High | Remove or replace with rescue-specific scenarios |
| Self-score (9.5) does not match actual quality (~7.7) | 🟡 Medium | Update metadata to reflect actual score |
| Line count 601, exceeds domain limit | 🟡 Medium | Remove filler |

---

## Anti-Patterns Detected

| Anti-Pattern | Location | Severity |
|--------------|----------|----------|
| Generic placeholder content | §9 Scenario Examples (lines 327-424) | 🔴 High |
| Knowledge maturity model | §16 (lines 486-505) | 🟡 Medium |
| Risk register (generic) | §17 (lines 509-532) | 🟡 Medium |
| Excellence framework | §18-21 (lines 536-601) | 🟡 Medium |

**Total filler content: ~120 lines** (20% of file)

---

## Signal-to-Token Efficiency
```
= (3×3) + (2×5) + (5×2) = 9 + 10 + 10 = 29
÷ 6.01 = 4.83 → Exemplary
```
**Status: ✅ PASS**

---

## Conclusion

**rescue-worker** is an Expert-level skill with similar issues to museum-curator:
1. ~120 lines of generic filler content (sections 16-21)
2. Self-score overestimates actual quality
3. Real scenarios are good but mixed with generic content

**Recommendation**: 
- Remove sections 16-21 (generic template content)
- Update self-score to 7.5-8.0
- Add 1-2 more rescue-specific scenario flows

After fixes: Potential for Exemplary tier (8.5+)

---

*Evaluation complete. Next: customs-officer*
