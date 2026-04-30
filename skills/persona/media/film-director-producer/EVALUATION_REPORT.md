# Evaluation Report: film-director-producer

## Summary

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 9.0 | 20% | 1.80 |
| Domain Knowledge Density | 9.0 | 25% | 2.25 |
| Workflow Actionability | 8.0 | 15% | 1.20 |
| Risk Documentation | 9.0 | 10% | 0.90 |
| Example Quality | 8.0 | 20% | 1.60 |
| Metadata Completeness | 10.0 | 10% | 1.00 |

**Total Score: 8.75/10** — **Expert** ⭐

---

## Dimension Breakdown

### 1. System Prompt Depth (9/10)
- **Strengths**: Comprehensive role definition with 15+ years experience, award-winning director/producer. Has 1.1 role definition, 1.2 decision framework with 4 gates, 1.3 thinking patterns, 1.4 communication style. Distinguishes between director (creative) and producer (business) authority.
- **Areas for Improvement**: Very strong, near Exemplary level.

### 2. Domain Knowledge Density (9/10)
- **Strengths**: Specific tools (MovieMagic Budgeting, Final Draft, Celtx, Mimeo, Frame.io, DaVinci Resolve, Pro Tools). Production phase framework (Development → Pre-Production → Production → Post-Production). Budget ranges for indie ($50K-$50M). Specific deliverables (DCP, QTPF, streaming masters).
- **Note**: Body is 536 lines, slightly over 500-line recommendation.

### 3. Workflow Actionability (8/10)
- **Strengths**: Has §8 workflow section, references external files (08-workflow.md). Scenario examples in §9 cover 4 standard types.
- **Gap**: §7 and §8 reference external files (`references/07-standards.md`, `references/08-workflow.md`) — need to verify they contain actionable content, not just placeholders.

### 4. Risk Documentation (9/10)
- **Strengths**: 6 risks with severity ratings (Budget Overrun, Schedule Overrun, Talent Dropout, Legal/Union Issues, IP/Chain of Title, Safety Incidents). Includes ⚠️ important warnings. Better than most skills in this dimension.
- **Areas for Improvement**: Could add escalation triggers.

### 5. Example Quality (8/10)
- **Strengths**: 4 scenarios (Initial Consultation, Problem Resolution, Strategic Planning, Quality Review). Test cases in §14 with specific input/expected output. §10 references external pitfalls file.
- **Gap**: Scenarios somewhat generic compared to podcast-producer and news-anchor. Could be more film-specific with actual script analysis examples, budget breakdown examples.

### 6. Metadata Completeness (10/10)
- **Strengths**: All 9 fields present. Description ≤263 chars. Version, tags, category all correct. Self-score of 9.5/10 documented in metadata.

---

## Recommendations

### Required Fixes
1. **Verify external references**: Confirm `references/07-standards.md` and `references/08-workflow.md` contain substantive content, not placeholders.

### Optional Upgrades (for Exemplary)
1. **Make scenarios more film-specific**: Add examples like script analysis, budget breakdown, shot list creation
2. **Reduce SKILL.md body**: Move detailed reference tables to `references/`
3. **Add escalation triggers**: To Risk Disclaimer section

---

## Verification Checklist

- [x] All 16 H2 sections present
- [x] Risk disclaimer has 4+ domain risks (6 total)
- [x] At least 2 full conversation scenario flows (4 present)
- [x] Workflow has 3+ phases (4 phases in production framework)
- [x] Domain frameworks have numeric thresholds (budget ranges, delivery specs)
- [x] Metadata all 9 fields present
- [x] Weighted average ≥ 7.0 (8.75 = Expert)

---

## Conclusion

This skill demonstrates **Expert** quality with strong system prompt, domain knowledge, and risk documentation. The reference to external files is appropriate (follows References-First principle) but requires verification. Scenarios could be more film-specific.

**Status**: Ready for production use. Verify external references contain actionable content. Consider scenario upgrades for Exemplary tier.