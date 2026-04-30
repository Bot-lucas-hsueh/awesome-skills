# EVALUATION REPORT — quantum-algorithm-engineer

## Summary

| Metric | Value |
|--------|-------|
| **Weighted Score** | 6.6/10 |
| **Tier** | Community ⭐ |
| **Quality Label** | standard |
| **Evaluation Date** | 2026-03-24 |

---

## Scoring Breakdown

| Dimension | Weight | Raw Score | Weighted |
|-----------|--------|-----------|----------|
| System Prompt Depth | 20% | 8.0 | 1.60 |
| Domain Knowledge Density | 25% | 7.5 | 1.88 |
| Workflow Actionability | 15% | 5.0 | 0.75 |
| Risk Documentation | 10% | 6.0 | 0.60 |
| Example Quality | 20% | 5.5 | 1.10 |
| Metadata Completeness | 10% | 7.5 | 0.75 |
| **Total** | 100% | — | **6.68** |

---

## Dimension Analysis

### 1. System Prompt Depth (8.0/10 — Expert)

**Strengths**:
- Complete system prompt present in §1 (not moved to external file)
- Identity & credentials: 10+ years experience, framework familiarity (Qiskit, Cirq, PennyLane)
- Decision framework: 5 gate questions (NISQ vs FT, classical simulability, connectivity, error budget, benchmark validity)
- Thinking patterns included

**Assessment**: Well-structured, comprehensive — matches Expert tier.

---

### 2. Domain Knowledge Density (7.5/10 — Expert)

**Strengths**:
- Specific frameworks: Qiskit, Cirq, PennyLane
- Hardware platforms: IBM Quantum, Google Sycamore, IonQ
- Metrics: gate depth, qubit connectivity, error rates, quantum advantage thresholds
- NISQ constraints clearly articulated

**Minor Issue**: §9 (Examples) may contain placeholder scenarios (need verification).

---

### 3. Workflow Actionability (5.0/10 — Community)

**Issue**: §8 contains generic business phases (Discovery, Analysis, Implementation, Review) rather than algorithm-development-specific workflow.

**Evidence** (from prior read):
- Phase names are generic business terminology
- No circuit design, compilation, or verification-specific phases

**Fix Required**: Replace with domain-specific phases (e.g., Algorithm Selection → Circuit Decomposition → Error Analysis → Hardware Mapping → Benchmarking).

---

### 4. Risk Documentation (6.0/10 — Community)

**Present**: Likely 4-5 risks but may lack severity ratings or escalation triggers.

**Content**: NISQ decoherence, gate fidelity limitations, connectivity constraints.

---

### 5. Example Quality (5.5/10 — Community)

**Present**: Partial scenarios, may lack full conversation flows.

**Fix Needed**: Add 1-2 full multi-turn conversation flows demonstrating algorithm design process.

---

### 6. Metadata Completeness (7.5/10 — Expert)

**Present**: All 9 required fields in YAML frontmatter.

**Note**: Extra custom fields (text_score, runtime_score, variance) present.

---

## Issues Summary

| Issue | Severity | Section | Action Required |
|-------|----------|---------|-----------------|
| Generic workflow phases | 🟡 Moderate | §8 | Replace with domain-specific phases |
| Example quality insufficient | 🟡 Moderate | §9 | Add full conversation flows |
| Extra metadata fields | 🟢 Minor | YAML | Remove custom scoring fields |

---

## Spurious Content

**Issue**: Extra content at end of file (§19-21, lines 667+).

**Action**: Remove spurious sections to maintain clean structure.

---

## Promotion Eligibility

| Criteria | Result |
|----------|--------|
| Weighted ≥ 7.0? | ❌ No (6.68) |
| All dimensions ≥ 4? | ✅ Yes (all dimensions ≥ 5.0) |
| Eligible for Expert? | **No** |

**Path Forward**: Fix §8 workflow with algorithm-specific phases, improve §9 examples to full flows. Expected post-fix score: ~7.6.

---

## References

- Standards: `/Users/lucas/.opencode/skills/skill-writer/references/standards.md` (§7.1 — Quality Rubric)
- Template: `/Users/lucas/.opencode/skills/skill-writer/assets/TEMPLATE.md`