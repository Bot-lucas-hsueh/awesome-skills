# Evaluation Report — ai-chip-architect

## Skill Summary
| Field | Value |
|-------|-------|
| **Name** | ai-chip-architect |
| **Version** | 3.0.0 |
| **Quality Tier** | Expert ⭐ |
| **Rubric Score** | 7.6/10 |
| **Line Count** | 596 |

---

## 6-Dimension Rubric Scores

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 8.0 | 20% | 1.60 | Expert |
| Domain Knowledge Density | 8.5 | 25% | 2.125 | Expert |
| Workflow Actionability | 7.0 | 15% | 1.05 | Expert |
| Risk Documentation | 8.0 | 10% | 0.80 | Expert |
| Example Quality | 8.0 | 20% | 1.60 | Expert |
| Metadata Completeness | 6.0 | 10% | 0.60 | Community |

---

## Strengths

### §1 System Prompt — Excellent
- Specific identity: 7nm NPU, 312 TFLOPS BF16 with 900 GB/s HBM3, MLPerf benchmarks
- "Bandwidth-Compute Wall" mental model
- Roofline-First gate with specific thresholds
- Decision Framework with 5 gates (Arithmetic Intensity → Memory Hierarchy → Dataflow → PPA Budget → Technology Readiness)
- **5 Thinking Patterns**: Compute vs Memory, Precision Trade-off, Sparsity Exploitation, Thermal Envelope, Compiler-Hardware Co-design
- Roofline Model with ASCII diagram and specific ridge point calculation
- PPA discipline mindset
- **Verdict**: Deep chip-architecture domain knowledge

### §3 Risk Disclaimer
- 4 risks (Process Node Risk, Bandwidth Underestimation, Compiler Gap, Thermal Throttling)
- Specific mitigations
- TFLOPS specification disclaimer

### §6 Professional Toolkit
- Specific EDA tools (Synopsys Design Compiler, Cadence Innovus, Ansys RedHawk, gem5, CACTI)
- MLPerf and Roofline Toolkit

### §9.2 Scenario: Systolic Array vs Vector Engine
- PPA trade-off table with specific area/power/performance numbers
- Hybrid recommendation with specific PPA impact

### §9.3 Scenario: Low MAC Utilization in MLPerf
- Roofline analysis with specific FLOPs/byte calculation
- Diagnostic table with expected loss and tools

---

## Weaknesses

### ❌ Missing §7 Standard Workflow (Severity: High)
- Section §7 exists but: `See [references/07-standards.md](references/07-standards.md)`
- No actual workflow

### ❌ Missing §8 Standard Workflow (Severity: High)
- Section §8: `See [references/08-workflow.md](references/08-workflow.md)`
- No actual workflow

### ❌ Missing §10 Common Pitfalls (Severity: High)
- Section §10: `See [references/10-pitfalls.md](references/10-pitfalls.md)`
- No actual anti-patterns

### ❌ Missing §5 Platform Support (Severity: High)

### ❌ Duplicate Generic Scenarios
- §9 lines 316-413: identical generic templates

### ❌ Duplicate Boilerplate Sections (Severity: High)
- §16-21 (~120 lines)

### ❌ Metadata Below Standard (Severity: Medium)
- Non-standard format (10-field block with tags)

### ❌ References Point to Non-Existent Files

### ❌ Token Budget Exceeded (Severity: High)
- **596 lines** — exceeds 500-line limit by 96 lines

---

## Token Budget Analysis

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| SKILL.md lines | 596 | ≤500 | ❌ Over by 96 lines |
| Post-cleanup estimate | ~470 lines | ≤500 | ✅ Within budget |

---

## Recommendation

**Tier: Expert ⭐** (7.6/10)

Same structural issue as ai-compute-platform-engineer. §1 is deep and specific (Roofline Model, PPA analysis, chip microarchitecture). But 3 empty sections pointing to missing files. Either create the reference files or inline the workflow content.

**Immediate actions required:**
1. Create/inline §7, §8, §10 content
2. Strip boilerplate and generic scenarios
3. Add §5 Platform Support
4. Fix metadata

After fixes: Estimated score → 8.5/10 Expert ⭐
