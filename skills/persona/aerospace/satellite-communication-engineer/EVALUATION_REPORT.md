# EVALUATION REPORT: satellite-communication-engineer

## Summary
| Metric | Value |
|--------|-------|
| **Weighted Score** | 7.55/10 |
| **Tier** | Expert ⭐ |
| **Original Score** | 7.8/10 |
| **Variance** | 0.25 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| System Prompt Depth | 20% | 8 | 1.60 |
| Domain Knowledge Density | 25% | 8 | 2.00 |
| Workflow Actionability | 15% | 7 | 1.05 |
| Risk Documentation | 10% | 7 | 0.70 |
| Example Quality | 20% | 7 | 1.40 |
| Metadata Completeness | 10% | 8 | 0.80 |
| **Total** | 100% | — | **7.55** |

---

## Detailed Analysis

### Strengths ✅

1. **System Prompt (8/10)**: Strong identity - 18+ years, Starlink/OneWeb/SES/Iridium experience. 5-gate framework (Orbit, Frequency, Coverage, Throughput, Regulatory). Thinking patterns specific to satcom (link budget, margin, interference, LEO, regulatory).

2. **Domain Knowledge (8/10)**: Comprehensive - link budget (EIRP, G/T, Eb/N0), constellation design, DVB-S2X waveform, ground station, interference analysis, ITU/FCC coordination, TCP/IP optimization. References ITU-R P.618, DVB-S2X, 3GPP NTN.

3. **Example Quality (7/10)**: Better than other 3 skills - scenarios have more structure and satellite-specific content. Still uses some placeholders.

4. **Anti-Patterns**: Good anti-patterns covering GEO→LEO link budget error, ITU timing, interference types, TCP overhead.

5. **Risk Documentation (7/10)**: 6 risks - interference, rain fade, solar conjunction, Kessler, regulatory, cybersecurity.

### Issues ❌

1. **Missing §5 Platform Support**: No install instructions.

2. **References-First Violations**:
   - §7: "See references/07-standards.md" - empty
   - §10: "See references/10-pitfalls.md" - content in body

3. **Body Length**: 754 lines - exceeds 500-line limit significantly.

---

## Anti-Patterns Detected

| # | Anti-Pattern | Severity | Location |
|---|--------------|----------|----------|
| 1 | Missing §5 Platform | 🟡 Medium | Section absent |
| 2 | Body exceeds 500 lines | 🔴 High | 754 lines |
| 3 | Generic examples | 🟢 Low | §9 partial |
| 4 | References empty | 🟢 Low | §7, §10 |

---

## Upgrade Recommendations

### Priority 1: Reduce Body Length (Critical)
- Move §7 Standards to references/
- Move §10 Pitfalls to references/
- Target: ≤500 lines (current 754 is 50% over)

### Priority 2: Add §5 Platform Support

### Priority 3: Fix remaining generic examples

---

## Verdict

**Tier: Expert ⭐** (7.55 ≥ 7.0)

Best of the 4 skills - higher example quality (7 vs 6). Critical issue: body length 754 lines far exceeds 500-line limit. Must offload content to references/ to meet token budget.

---
*Generated: 2026-03-24 | Skill Writer v12+*