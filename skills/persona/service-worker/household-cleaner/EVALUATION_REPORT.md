# Evaluation Report: household-cleaner

## Overall Score: 7.2/10 — Expert ⭐

### 6-Dimension Scoring

| Dimension | Score | Assessment |
|-----------|-------|------------|
| **System Prompt Depth** | 8/10 | Strong role definition (24 lines) with decision framework (4 gates), thinking patterns, and communication style |
| **Domain Knowledge Density** | 8/10 | DEEP-CLEAN framework with specific thresholds; appliance-specific protocols with timing; quality metrics |
| **Workflow Actionability** | 7/10 | 4 phases with sub-steps; has templates but some sections reference external files |
| **Risk Documentation** | 7/10 | 5 risks with severity ratings; chemical mixing warnings explicit |
| **Example Quality** | 6/10 | 2 real appliance scenarios + 4 generic placeholder scenarios that don't match skill domain |
| **Metadata Completeness** | 6/10 | Has YAML but uses non-standard fields (score, text_score, runtime_score, variance); missing platforms field |

### Strengths

1. **Strong system prompt** with clear role identity and decision framework
2. **DEEP-CLEAN framework** (9-step) provides actionable structure
3. **Appliance-specific protocols** with detailed step-by-step instructions
4. **Quality metrics** for bacterial reduction, cleaning time, re-clean rate
5. **Comprehensive risk matrix** with severity and explicit chemical warnings

### Critical Issues

1. **Generic placeholder scenarios** (§9 scenarios 1-4) are template text, not household cleaner specific
2. **Non-standard metadata fields** — uses score/text_score/runtime_score/variance instead of standard fields
3. **Sections 16-21** appear copied from another skill (generic "Domain Deep Dive", "Risk Management", "Excellence Framework")
4. **SKILL.md body exceeds 500 lines** (602 lines) — should offload to references/

### Recommendations

1. **Replace placeholder scenarios** with real household cleaner scenarios (e.g., organizing after move, post-renovation clean)
2. **Standardize metadata** — remove non-standard fields, add platforms, quality, difficulty standard fields
3. **Remove sections 16-21** or move to references/ — these are generic filler
4. **Trim body to ≤500 lines** by moving appliance protocols to references/

### Token Budget Issues

- Description: 263 chars (within budget but verbose)
- Body: 602 lines (exceeds 500 line limit)
- Sections 16-21 (~150 lines) should be moved to references/

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
| SKILL.md ≤500 lines | ❌ No (602) |
| Description ≤263 chars | ✅ Yes |

---

## Scoring Formula

```
Score = (System Prompt × 0.20) + (Domain Knowledge × 0.25) + (Workflow × 0.15)
      + (Risk × 0.10) + (Examples × 0.20) + (Metadata × 0.10)

Score = (8 × 0.20) + (8 × 0.25) + (7 × 0.15) + (7 × 0.10) + (6 × 0.20) + (6 × 0.10)
      = 1.6 + 2.0 + 1.05 + 0.7 + 1.2 + 0.6
      = 7.15 → 7.2
```

---

*Generated: 2026-03-24 | skill-writer v12+*
