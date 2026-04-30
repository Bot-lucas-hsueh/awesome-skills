# Evaluation Report: interventional-tech

## Overall Assessment
| Metric | Score |
|--------|-------|
| **Weighted Score** | **8.2/10** |
| **Tier** | Expert ⭐ |
| **Line Count** | 642 (exceeds 500) |

---

## Dimension Scores

| Dimension | Score (1-10) | Weight | Weighted |
|-----------|--------------|--------|----------|
| **System Prompt Depth** | 8 | 20% | 1.60 |
| **Domain Knowledge Density** | 9 | 25% | 2.25 |
| **Workflow Actionability** | 8 | 15% | 1.20 |
| **Risk Documentation** | 8 | 10% | 0.80 |
| **Example Quality** | 8 | 20% | 1.60 |
| **Metadata Completeness** | 7 | 10% | 0.70 |
| **Total** | | | **8.15** |

---

## Strengths

1. **Domain Knowledge**: Excellent radiation safety metrics (ALARA, DAP, fluoroscopy time), procedure frameworks with specific thresholds. Equipment-specific knowledge (GE, Siemens, Philips, Toshiba).
2. **System Prompt**: 4-gate decision framework, thinking patterns emphasizing workflow efficiency and sterility.
3. **Workflows**: Detailed cath lab setup (3 phases), emergency response for contrast reactions.
4. **Examples**: Practical STEMI PCI setup, high-dose radiation safety scenario.

---

## Issues Identified

### 🔴 Critical Issues

1. **Token Budget Exceeded**: 642 lines exceeds 500-line limit — highest among these 5 skills.
   - Sections §16-21 contain ~180 lines of generic content

2. **Example Quality**: Mix of real interventional scenarios (9.1-9.2) with generic template Scenarios 1-4

### 🟡 Medium Issues

3. **Non-Standard Metadata**: YAML includes extra score fields.
4. **Risk Documentation**: Only 5 risks; interventional procedures have more specific risks (e.g., radiation-induced skin injury, arterial spasm, air embolism).

---

## Recommendations

1. **Move to references/**:
   - Create `references/domain-deep-dive.md` for §16-21 content
   - Remove generic Scenarios 1-4 from §9

2. **Enhance Risk Section**: Add more procedure-specific risks (air embolism, thrombosis, device entrapment).

---

## Test Case Verification

| Test | Expected Behavior | Status |
|------|-------------------|--------|
| STEMI Setup | Equipment list, workflow | ✅ PASS |
| Radiation Emergency | ALARA actions, documentation | ✅ PASS |

---

## Final Verdict

**Expert ⭐ Recommended** — Strong interventional radiology content with radiation safety emphasis. Requires token budget cleanup.
