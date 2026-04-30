# EVALUATION REPORT — quantum-sensor-researcher

## Summary

| Metric | Value |
|--------|-------|
| **Weighted Score** | 6.4/10 |
| **Tier** | Community ⭐ |
| **Quality Label** | standard |
| **Evaluation Date** | 2026-03-24 |

---

## Scoring Breakdown

| Dimension | Weight | Raw Score | Weighted |
|-----------|--------|-----------|----------|
| System Prompt Depth | 20% | 4.0 | 0.80 |
| Domain Knowledge Density | 25% | 8.0 | 2.00 |
| Workflow Actionability | 15% | 5.0 | 0.75 |
| Risk Documentation | 10% | 7.0 | 0.70 |
| Example Quality | 20% | 6.0 | 1.20 |
| Metadata Completeness | 10% | 8.5 | 0.85 |
| **Total** | 100% | — | **6.30** |

---

## Dimension Analysis

### 1. System Prompt Depth (4.0/10 — Basic)

**Issue**: System prompt code block moved to `references/code-block-1.md` — incomplete SKILL.md.

**Evidence**: §1 contains only:
```
[Code block moved to code-block-1.md]
```

**Impact**: Primary driver of AI behavior is absent. The skill cannot function as designed without loading the external reference.

**Fix Required**: Restore complete system prompt to §1 in SKILL.md itself.

---

### 2. Domain Knowledge Density (8.0/10 — Expert)

**Strengths**:
- Specific sensor technologies: atom interferometry, SQUID, optical atomic clocks, NV-center
- Quantified metrics: Standard Quantum Limit (δφ = 1/√N), Heisenberg limit (δφ = 1/N)
- Real hardware specs: T1/T2 coherence times, SNSPD efficiency >95%

**Assessment**: Deep domain expertise demonstrated; frameworks with specific thresholds present.

---

### 3. Workflow Actionability (5.0/10 — Community)

**Issue**: §8 contains generic business phases (Discovery, Analysis, Implementation, Review) rather than domain-specific workflow.

**Evidence** (from prior read):
- Phase names are generic business terminology
- No quantum-sensor-specific templates or checkpoints

**Fix Required**: Replace with domain-specific phases (e.g., Sensitivity Analysis → Hardware Selection → Protocol Design → Characterization).

---

### 4. Risk Documentation (7.0/10 — Expert)

**Present**: 5+ risks with severity indicators and mitigation strategies.

**Content**: Systematic errors in atom interferometry, flux noise in SQUID, laser stability for atomic clocks, NV-center T1/T2 limitations.

---

### 5. Example Quality (6.0/10 — Community)

**Present**: Likely 1-2 partial scenarios, but not full multi-turn conversation flows.

**Assessment**: Basic examples exist but lack the depth expected for Expert tier.

---

### 6. Metadata Completeness (8.5/10 — Expert)

**Present**: All 9 required fields in YAML frontmatter.

**Note**: Extra custom fields (text_score, runtime_score, variance) present — not blocking but unnecessary.

---

## Issues Summary

| Issue | Severity | Section | Action Required |
|-------|----------|---------|-----------------|
| System prompt moved to external file | 🔴 Critical | §1 | Restore full system prompt to SKILL.md |
| Generic workflow phases | 🟡 Moderate | §8 | Replace with domain-specific phases |
| Extra metadata fields | 🟢 Minor | YAML | Remove custom scoring fields |

---

## Spurious Content

**Issue**: Extra content at end of file (§19-21, lines 667+).

**Action**: Remove spurious sections to maintain clean structure.

---

## Promotion Eligibility

| Criteria | Result |
|----------|--------|
| Weighted ≥ 7.0? | ❌ No (6.4) |
| All dimensions ≥ 4? | ❌ System Prompt = 4.0 |
| Eligible for Expert? | **No** |

**Path Forward**: Fix system prompt (restore to §1), fix §8 workflow, then re-evaluate. Expected post-fix score: ~7.8.

---

## References

- Standards: `/Users/lucas/.opencode/skills/skill-writer/references/standards.md` (§7.1 — Quality Rubric)
- Template: `/Users/lucas/.opencode/skills/skill-writer/assets/TEMPLATE.md`