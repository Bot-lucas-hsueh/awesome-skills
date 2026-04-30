# Evaluation Report: news-anchor

## Summary

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 9.0 | 20% | 1.80 |
| Domain Knowledge Density | 9.0 | 25% | 2.25 |
| Workflow Actionability | 9.0 | 15% | 1.35 |
| Risk Documentation | 8.0 | 10% | 0.80 |
| Example Quality | 9.0 | 20% | 1.80 |
| Metadata Completeness | 10.0 | 10% | 1.00 |

**Total Score: 9.0/10** — **Exemplary** ⭐⭐

---

## Dimension Breakdown

### 1. System Prompt Depth (9/10)
- **Strengths**: 15+ years experience, specific broadcast formats (copy, VO, PKG, live shot), timing standards (30-sec copy = 75 words, 150-160 wpm), AP Style emphasis. Clear distinction between fact, analysis, and opinion.
- **Areas for Improvement**: Could add more domain-specific heuristics unique to broadcast journalism.

### 2. Domain Knowledge Density (9/10)
- **Strengths**: Specific tools (iNews, AP Wire, Dataminr), style references (AP Stylebook, SPJ Code of Ethics, Reuters Handbook, Poynter). Newsworthiness criteria with ranking. Breaking news ladder (5 levels). Specific broadcast script format with timing.
- **Note**: SKILL.md body is 684 lines, exceeding 500-line recommendation. Consider offloading to references/.

### 3. Workflow Actionability (9/10)
- **Strengths**: 3-phase workflow (Assignment/Research, Live Broadcast, Post-Broadcast Review). Story research checklist, broadcast script format templates, live interview structure with timing, breaking news ad-lib framework. Done/Fail criteria present.
- **Minor**: Could add more specific failure scenarios per step.

### 4. Risk Documentation (8/10)
- **Strengths**: 5 domain-specific risks (Defamation, Premature Breaking News, Source Protection, Privacy, Bias). Missing row in table at line 95 appears incomplete but doesn't block function.
- **Gap**: Could add escalation triggers and consequence examples.

### 5. Example Quality (9/10)
- **Strengths**: 5 anti-patterns specific to broadcast (Single-Source Broadcasting, Reading Numbers Without Converting, Compound Questions, Editorializing in News Copy, Failing to Acknowledge Errors). §9 includes 4 standard scenarios.
- **Minor**: Could add one more full conversation flow.

### 6. Metadata Completeness (10/10)
- **Strengths**: All 9 fields present. Description ≤263 chars. Version, tags, category all correct. Quality metrics in metadata.

---

## Recommendations

### Required Fixes
1. **Fix truncated row in Risk table** (line 95): Complete the "Bias" row or remove it.

### Optional Upgrades (for Exemplary)
1. **Reduce SKILL.md body**: Move detailed reference tables to `references/` folder
2. **Add escalation triggers**: To Risk Disclaimer section

---

## Verification Checklist

- [x] All 16 H2 sections present
- [x] Risk disclaimer has 4+ domain risks (with minor formatting fix needed)
- [x] At least 2 full conversation scenario flows
- [x] Workflow has 3+ phases with Done/Fail criteria
- [x] Domain frameworks have numeric thresholds (75 words/30 sec, 150-160 wpm)
- [x] Metadata all 9 fields present
- [x] Weighted average ≥ 9.0

---

## Conclusion

This skill demonstrates **Exemplary** quality with deep broadcast journalism knowledge. Specific tools, standards (AP Style, timing formulas), and workflows are well-documented. Anti-patterns are domain-specific and actionable.

**Status**: Ready for production use after fixing the truncated Risk table row. Consider optional upgrades for token optimization.