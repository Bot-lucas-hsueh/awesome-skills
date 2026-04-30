# Evaluation Report: journalist-editor

## Summary

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 9.0 | 20% | 1.80 |
| Domain Knowledge Density | 9.0 | 25% | 2.25 |
| Workflow Actionability | 9.0 | 15% | 1.35 |
| Risk Documentation | 9.0 | 10% | 0.90 |
| Example Quality | 9.0 | 20% | 1.80 |
| Metadata Completeness | 10.0 | 10% | 1.00 |

**Total Score: 9.1/10** — **Exemplary** ⭐⭐

---

## Dimension Breakdown

### 1. System Prompt Depth (9/10)
- **Strengths**: 15+ years at major publications (NYT, WaPo, Reuters, AP). Has 1.1 role definition, 1.2 decision framework with 4 gates, 1.3 thinking patterns (Sourcing, News Value, Legal/Ethical, Clarity), 1.4 communication style. Clear on attribution-first, active voice, no editorializing.
- **Areas for Improvement**: Could add more domain-specific heuristics unique to investigative journalism.

### 2. Domain Knowledge Density (9/10)
- **Strengths**: Specific tools (AP Stylebook, iNews, FOIA.gov, LexisNexis, MuckRack, Poynter, DocumentCloud). Inverted pyramid framework with visual diagram. AP Style quick reference table. Story types table. Metrics defined.
- **Note**: SKILL.md body is 669 lines, exceeding 500-line recommendation. Consider offloading to references/.

### 3. Workflow Actionability (9/10)
- **Strengths**: 3 detailed workflows: Investigative Story Workflow (4 phases), Copy Editing Workflow (7 steps), Breaking News Workflow. All have specific steps and criteria. This is one of the strongest workflow sections among the 4 skills.
- **Areas for Improvement**: Could add more failure criteria per step.

### 4. Risk Documentation (9/10)
- **Strengths**: 5 risks with severity (Defamation, Confidential Source Exposure, Premature Publication, Privacy Violation, Plagiarism). Includes ⚠️ important warnings section. Better than most skills.
- **Areas for Improvement**: Could add escalation triggers.

### 5. Example Quality (9/10)
- **Strengths**: 3 detailed scenarios (Investigative Story Development, Breaking News — Mass Shooting, Copy Editing a Political Press Release) — these are highly specific and actionable! Anti-patterns in §10 with 5 patterns and ❌/✅ fixes.
- **Note**: This skill has the best example scenarios among the 4 skills reviewed.

### 6. Metadata Completeness (10/10)
- **Strengths**: All 9 fields present. Description ≤263 chars. Version, tags, category all correct. Self-score documented.

---

## Recommendations

### Required Fixes
None required for Exemplary tier.

### Optional Upgrades (for Token Optimization)
1. **Reduce SKILL.md body**: Move detailed AP Style reference table to `references/` folder to stay under 500 lines

---

## Verification Checklist

- [x] All 16 H2 sections present
- [x] Risk disclaimer has 4+ domain risks (5 total)
- [x] At least 2 full conversation scenario flows (4 present, plus 3 detailed domain-specific scenarios in §9.1-9.3)
- [x] Workflow has 3+ phases with specific steps (3 workflows with 4-7 steps each)
- [x] Domain frameworks have numeric thresholds (metrics table, Flesch-Kincaid targets)
- [x] Metadata all 9 fields present
- [x] Weighted average ≥ 9.0

---

## Conclusion

This skill demonstrates **Exemplary** quality with particularly strong example scenarios and workflow sections. The 3 detailed scenarios in §9.1-9.3 are highly specific to journalism (investigative development, breaking news, copy editing) and set a high bar. The inverted pyramid framework with visual diagram, AP Style quick reference, and 3 distinct workflows make this one of the best-structured skills in the media category.

**Status**: Ready for production use. Consider optional upgrade for token optimization.