# Evaluation Report: rehabilitation-engineer

## Overall Assessment
| Metric | Score |
|--------|-------|
| **Weighted Score** | **8.3/10** |
| **Tier** | Expert ⭐ |
| **Line Count** | 603 (exceeds 500) |

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

1. **Domain Knowledge**: Excellent K-level framework for prosthetic selection, FDA Class device awareness, ISO 16982 usability engineering reference.
2. **System Prompt**: Clear 3-gate decision framework, thinking patterns on function-driven design.
3. **Workflows**: Good prosthetic design workflow (4 phases), assistive technology assessment steps.
4. **Examples**: Practical transfemoral prosthetic selection and wheelchair seating scenarios.

---

## Issues Identified

### 🔴 Critical Issues

1. **Token Budget Exceeded**: 603 lines exceeds 500-line limit.
   - Sections §16-21 contain ~170 lines of generic content

2. **Example Quality**: Mix of real content (9.1-9.2 rehab-specific) with generic template Scenarios 1-4

### 🟡 Medium Issues

3. **Non-Standard Metadata**: YAML includes extra score fields.
4. **Risk Documentation**: Only 5 risks listed; could benefit from more rehabilitation-specific risks (e.g., improper device fitting causing falls, electrical failures in powered wheelchairs).

---

## Recommendations

1. **Move to references/**:
   - Create `references/domain-deep-dive.md` for §16-21 content
   - Remove generic Scenarios 1-4 from §9

2. **Enhance Risk Section**: Add domain-specific rehabilitation risks.

---

## Test Case Verification

| Test | Expected Behavior | Status |
|------|-------------------|--------|
| Prosthetic Component Selection | K-level based selection | ✅ PASS |
| Assistive Technology Assessment | User capability analysis | ✅ PASS |

---

## Final Verdict

**Expert ⭐ Recommended** — Strong rehabilitation engineering content with practical K-level framework. Requires token budget cleanup.
