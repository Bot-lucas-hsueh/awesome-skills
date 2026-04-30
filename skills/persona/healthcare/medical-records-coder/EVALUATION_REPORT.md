# Skill Evaluation Report: medical-records-coder

## Summary
| Attribute | Value |
|-----------|-------|
| **Score** | 8.7/10 |
| **Tier** | Expert ⭐ |
| **File** | `skills/healthcare/medical-records-coder/SKILL.md` |
| **Lines** | 636 (exceeds 500 limit) |

---

## Dimension Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 9/10 | 20% | 1.80 |
| Domain Knowledge Density | 9/10 | 25% | 2.25 |
| Workflow Actionability | 9/10 | 15% | 1.35 |
| Risk Documentation | 9/10 | 10% | 0.90 |
| Example Quality | 8/10 | 20% | 1.60 |
| Metadata Completeness | 10/10 | 10% | 1.00 |

---

## Rubric Analysis

### System Prompt Depth: 9/10 ✅
- Role definition with certifications (CCS, CPC, RHIA)
- 4 decision gates (coding scope, documentation support, inpatient/outpatient, CC/MCC)
- 4 thinking patterns (Documentation First, Sequencing Logic, DRG Impact, Compliance)
- Communication style: Code-First, Query-Ready, DRG-Aware

### Domain Knowledge Density: 9/10 ✅
- ICD-10-CM/PCS coding frameworks
- DRG assignment flow with ASCII diagram
- Coding metrics with targets (accuracy >95%, query rate 3-5%)
- Professional toolkit (Coding Clinic, DRG Grouper, Encoder Pro)

### Workflow Actionability: 9/10 ✅
- 4-phase inpatient coding process with sub-steps
- Physician query process (Identify Need → Compose Query → Send and Track)
- Each step has clear done criteria

### Risk Documentation: 9/10 ✅
- 4 high-severity risks: Upcoding, Undercoding, Query misuse, Copy-paste errors
- Severity ratings with specific mitigation
- Important warnings section

### Example Quality: 8/10 ⚠️
- 2 detailed domain-specific examples: DRG Assignment with CC impact, Query for Documentation
- §9 scenarios are generic (not medical coding specific)
- Full conversation flows present for domain examples

### Metadata Completeness: 10/10 ✅
- All 9 required fields present
- Description: 262 chars (within 263 limit)
- Version, author, difficulty, category, tags all present

---

## Issues Identified

| Issue | Severity | Action |
|-------|----------|--------|
| File length 636 lines | 🔴 High | Exceeds 500 line limit; move §16-21 to references/ |
| Generic §9 scenarios | 🟡 Medium | Replace with domain-specific coding scenarios |
| Section duplication | 🟡 Medium | §16-21 are generic filler; remove or reference |

---

## Recommendations

1. **Move to references/**: §16 (Domain Deep Dive), §17 (Risk Management), §18 (Excellence Framework), §19 (Best Practices), §20 (Case Studies), §21 (Resources)
2. **Add domain-specific §9 scenarios**: Add coding error identification, audit preparation scenarios
3. **Reduce total lines**: Target 480 lines for SKILL.md body

---

## Verdict

**Expert ⭐** — This skill demonstrates comprehensive medical coding expertise with strong frameworks, workflows, and risk awareness. The primary issue is file length exceeding the token budget. After moving generic sections to references/, this will be Exemplary tier.

**Recommendation**: Accept with required file length fixes.
