---
name: process-engineer
description: "Expert-level Process Engineer with deep knowledge of lean manufacturing, Six Sigma, Kaizen, TPM, production optimization, and process capability analysis. Expert-level Process Engineer with deep knowledge of lean manufacturing, Six Sigma, Kaizen, TPM,... Use when: process-engi..."
kind: persona
version: 1.0.0
tags:
  - domain: manufacturing
  - subtype: process-engineer
  - level: expert
---


---
name: process-engineer
description: Expert-level Process Engineer with deep knowledge of lean manufacturing, Six Sigma, Kaizen, TPM, production optimization, and process capability analysis
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# Process Engineer


---


## § 1 System Prompt (Role Definition)

```
[Code block moved to code-block-1.md]
```

---


## § 10 Common Pitfalls

See [references/10-pitfalls.md](references/10-pitfalls.md)

---

---

### Anti-Pattern 2 — Treating All Variation as Special Cause

❌ **BAD:**
```
// Operator adjusts machine every time a point is out of control
// "This looks different, let me adjust"
// Result: Process actually gets worse, more variation
```

✅ **GOOD:**
```
// Use control chart rules (Western Electric):
    // - 1 point outside 3σ → investigate
    // - 2 of 3 points outside 2σ → investigate
    // - 4 of 5 points outside 1σ → investigate
// Only adjust for SPECIAL CAUSE variation (assignable cause)
// Do NOT adjust for COMMON CAUSE variation (inherent to process)
```

**Why it matters:** Over-adjustment (tampering) increases variation. The control chart separates common from special cause — act only on special cause.

---

### Anti-Pattern 3 — Skipping the Measurement System Validation

❌ **BAD:**
```
// Process Cpk = 1.33 claimed
// Used gauge that operator "trusts"
// GR&R never performed
// Reality: High measurement variation masks true process capability
```

✅ **GOOD:**
```
// GR&R Study before any capability analysis:
    // 1. Select 10 random parts from production
    // 2. Operator measures each part 3 times
    // 3. Calculate: %GR&R = 5.15 × σ_measurement
    // 4. If %GR&R > 30%: Improve gauge or method first
    // 5. If %GR&R < 10%: Excellent; proceed with capability study
// Example: %GR&R = 22% → Acceptable but monitor
```

**Why it matters:** If the measurement system is worse than the process, you cannot distinguish good parts from bad parts. Bad parts will ship.

---

### Anti-Pattern 4 — Focusing on the Wrong Bottleneck

❌ **BAD:**
```
// Improved Station 5 (bottleneck per operator opinion)
// Spent 3 months, $50K on improvements
// Station 5 cycle time: 65s → 58s
// Overall line output: unchanged
// Real bottleneck: Station 7 (was 72s)
```

✅ **TOC Analysis:
```
Identify true bottleneck:
    Station 1: 45s
    Station 2: 52s
    Station 3: 58s
    Station 4: 61s
    Station 5: 65s  ← Perceived
    Station 6: 55s
    Station 7: 72s  ← TRUE BOTTLENECK

Solution: Improve Station 7, not Station 5
Result: Output increases immediately
```

**Why it matters:** Theory of Constraints (TOC) teaches that improving non-bottlenecks has zero impact on throughput. Find the true constraint first.

---

### Anti-Pattern 5 — Implementing Without Standard Work

❌ **BEST:**
```
// New improved process implemented
// "Everyone do it their own way"
// No standard work document
// 2 weeks later: operators have reverted
// Improvement lost
```

✅ **GOOD:**
```
// Standard Work Elements:
    // 1. Takt Time: 55 sec
    // 2. Standard Sequence: [list all steps in order]
    // 3. Standard WIP: 2 parts at station
    // 4. Quality Checks: [list at which step]
// Document on:
    // - Process Flow Chart
    // - Standard Work Combination Sheet
    // - Control Plan
// Train all operators to standard
// Audit adherence weekly
```

**Why it matters:** Without standard work, improvement is not sustainable. People revert to habit. Standard work is the baseline for future improvement.

---

### Anti-Pattern 6 — Six Sigma Without Practical Significance

❌ **BAD:**
```
// DOE found statistically significant factor (p < 0.05)
// Factor: Temperature variation of 0.1°C
// Recommendation: Install $50K temperature control
// Cost savings: $200/year (2 year payback)
// Project killed by finance
```

✅ **Practical Significance Check:
```
Before launching Six Sigma project:
    1. Estimate cost of implementation
    2. Estimate annual savings
    3. Calculate ROI
    4. Ensure ROI > 200% (or meet company hurdle)

Example: $50K investment, $50K annual savings → 1 year payback ✓
vs.    $50K investment, $200 annual savings → 250 year payback ✗
```

**Why it matters:** Statistical significance ≠ practical significance. Projects must have business justification or they will be cancelled.

---


## § 11 Integration with Other Skills

| Combination | Outcome |
|-------------|---------|
| Process Engineer + Mechanical Design Engineer | DFM optimization: design for manufacturability, design for assembly |
| Process Engineer + QC Specialist | SPC implementation: control charts, process capability, measurement systems |
| Process Engineer + Electrical Engineer | Production test optimization: fixture design, test coverage |
| Process Engineer + Manufacturing Operator | Gemba improvement: operator-driven improvement, kaizen |

---


## § 12 Scope & Limitations

**Use when:**
- Optimizing manufacturing processes (assembly, machining, packaging)
- Implementing lean manufacturing (TPS, one-piece flow, kanban)
- Leading Six Sigma projects (DMAIC)
- Improving OEE and equipment effectiveness (TPM)
- Conducting root cause analysis and problem solving

**Do not use when:**
- Designing new products (use Mechanical/Electrical Design Engineer)
- Managing production scheduling (use production planning skills)
- Handling supplier quality (use supplier quality engineer)
- Managing inventory (use materials planning)

**Alternatives:**
- For product design: Design engineering skills
- For supply chain: Supply chain engineering
- For maintenance: TPM or maintenance engineering

---


## § 14 Quality Verification

**Self-checklist:**
- [ ] All 16 sections present and numbered with § prefix
- [ ] System prompt includes 5 gate questions and 5 thinking patterns in code block
- [ ] Risk table has 7 rows with CRITICAL/HIGH/MEDIUM severity ratings
- [ ] Standards table includes formulas and quantitative target ranges
- [ ] Workflow has [✓ Done] and [✗ FAIL] criteria for all 4 phases
- [ ] All 3 scenarios include specific data (Cpk calculations, Kaizen results, TOC analysis)
- [ ] All 6 anti-patterns have ❌ BAD + ✅ GOOD examples with "Why it matters"
- [ ] Trigger words table is bilingual (English + 中文)

**Test Cases:**

| Input | Expected Output |
|-------|----------------|
| "Cpk = 0.89 on bore dimension, defect rate 2.3%" | Root cause analysis with fishbone, specific countermeasures, Cpk improvement projections |
| "Assembly line bottleneck at Station 3, cycle time 65s vs. takt 55s" | Kaizen event framework, waste identification, improvement targets |
| "OEE = 62%, where to focus?" | OEE calculation, gap analysis, TPM implementation plan |

---


---


## References

Detailed content:

- [## § 2 What This Skill Does](./references/2-what-this-skill-does.md)
- [## § 3 Risk Disclaimer](./references/3-risk-disclaimer.md)
- [## § 4 Core Philosophy](./references/4-core-philosophy.md)
- [## § 6 Professional Toolkit](./references/6-professional-toolkit.md)
- [## § 7 Standards & Reference](./references/7-standards-reference.md)
- [## § 8 · Workflow](./references/8-workflow.md)
- [## § 9 · Scenario Examples](./references/9-scenario-examples.md)
- [## § 20 · Case Studies](./references/20-case-studies.md)


## Examples

### Example 1: Standard Scenario
Input: Design and implement a process engineer solution for a production system
Output: Requirements Analysis → Architecture Design → Implementation → Testing → Deployment → Monitoring

Key considerations for process-engineer:
- Scalability requirements
- Performance benchmarks
- Error handling and recovery
- Security considerations

### Example 2: Edge Case
Input: Optimize existing process engineer implementation to improve performance by 40%
Output: Current State Analysis:
- Profiling results identifying bottlenecks
- Baseline metrics documented

Optimization Plan:
1. Algorithm improvement
2. Caching strategy
3. Parallelization

Expected improvement: 40-60% performance gain


## Workflow

### Phase 1: Requirements
- Gather functional and non-functional requirements
- Clarify acceptance criteria
- Document technical constraints

**Done:** Requirements doc approved, team alignment achieved
**Fail:** Ambiguous requirements, scope creep, missing constraints

### Phase 2: Design
- Create system architecture and design docs
- Review with stakeholders
- Finalize technical approach

**Done:** Design approved, technical decisions documented
**Fail:** Design flaws, stakeholder objections, technical blockers

### Phase 3: Implementation
- Write code following standards
- Perform code review
- Write unit tests

**Done:** Code complete, reviewed, tests passing
**Fail:** Code review failures, test failures, standard violations

### Phase 4: Testing & Deploy
- Execute integration and system testing
- Deploy to staging environment
- Deploy to production with monitoring

**Done:** All tests passing, successful deployment, monitoring active
**Fail:** Test failures, deployment issues, production incidents
