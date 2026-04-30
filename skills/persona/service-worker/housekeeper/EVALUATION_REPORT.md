# Evaluation Report: housekeeper

## Overall Score: 7.2/10 — Expert ⭐

### 6-Dimension Scoring

| Dimension | Score | Assessment |
|-----------|-------|------------|
| **System Prompt Depth** | 8/10 | Strong role definition (24 lines) with 3 gates, thinking patterns, professional communication style |
| **Domain Knowledge Density** | 8/10 | Cleaning Workflow Matrix with specific sequence; room-by-room checklist; stain removal guide (7 stains); surface guide |
| **Workflow Actionability** | 7/10 | 3 phases with detailed sub-steps; weekly routine references external file |
| **Risk Documentation** | 7/10 | 5 risks with severity ratings; chemical mixing explicit warnings |
| **Example Quality** | 6/10 | 2 real housekeeping scenarios + 4 generic placeholder scenarios |
| **Metadata Completeness** | 6/10 | Has YAML but uses non-standard fields; missing platforms field |

### Strengths

1. **Cleaning Workflow Matrix** — visual top-to-bottom, left-to-right sequence
2. **Room-by-Room Checklist** — specifies must-clean areas and frequency
3. **Stain Removal Guide** — 7 common stains with treatment and timing
4. **Surface Compatibility Guide** — what to use/avoid for wood, marble, stainless, etc.
5. **Realistic Scenarios** — pantry organization, post-illness cleaning

### Critical Issues

1. **Generic placeholder scenarios** (§9 scenarios 1-4) are template text
2. **Non-standard metadata** — score, text_score, runtime_score, variance
3. **Sections 16-21** generic filler (same content as other skills)
4. **External reference** §8.2 references code-block-1.md
5. **SKILL.md body exceeds 500 lines** (675 lines)

### Recommendations

1. Replace placeholder scenarios with housekeeper-specific examples
2. Standardize metadata fields
3. Remove sections 16-21 or move to references/
4. Inline or verify code-block-1.md
5. Trim to ≤500 lines

### Token Budget Issues

- Description: 239 chars (within budget)
- Body: 675 lines (exceeds 500 limit)
- ~150 lines generic content

---

## Quality Verification Checklist

| Check | Status |
|-------|--------|
| All 9 metadata fields present | ⚠️ Partial |
| System Prompt defines role + framework | ✅ Yes |
| All 16 H2 sections present | ✅ Yes |
| Risk disclaimer 4+ domain risks | ✅ Yes |
| 2+ full conversation scenarios | ⚠️ 2 real + 4 placeholders |
| Workflow 3+ phases | ✅ Yes |
| Domain frameworks with thresholds | ✅ Yes |
| SKILL.md ≤500 lines | ❌ No (675) |
| Description ≤263 chars | ✅ Yes |

---

## Scoring Formula

```
Score = (8 × 0.20) + (8 × 0.25) + (7 × 0.15) + (7 × 0.10) + (6 × 0.20) + (6 × 0.10)
      = 1.6 + 2.0 + 1.05 + 0.7 + 1.2 + 0.6
      = 7.15 → 7.2
```

---

*Generated: 2026-03-24 | skill-writer v12+*
