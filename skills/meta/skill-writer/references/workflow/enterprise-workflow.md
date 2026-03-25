# Enterprise Workflow

> Complete workflow for creating Enterprise tier skills (500-1500 lines)

**Time:** 1-2 days  
**Target Score:** 9.0+  
**Output:** Complete skill system with methodology

---

## Overview

Enterprise skills are **complete methodology systems** for complex domains.

**Characteristics:**
- Complete methodology/framework
- Multiple interconnected domains
- Safety/critical requirements
- Comprehensive coverage
- ~500-1500 lines total across all files
- Used as organizational standards

---

## Phase 1: Discovery (4 hours)

### 1.1 Methodology Definition

**The Core Question:**
```
What complete system or methodology does this skill represent?
```

**Examples:**
- Tesla's first-principles engineering culture
- McKinsey's problem-solving framework
- Google's SRE practices
- Medical diagnostic protocols

### 1.2 Stakeholder Analysis

| Stakeholder | Needs | Success Criteria |
|-------------|-------|------------------|
| Primary users | [Their needs] | [How they win] |
| Secondary users | [Their needs] | [How they win] |
| Organization | [Strategic goals] | [Business impact] |

### 1.3 Domain Mapping

Identify all domains covered:

```
Methodology
├── Domain A
│   ├── Sub-topic A1
│   └── Sub-topic A2
├── Domain B
│   ├── Sub-topic B1
│   └── Sub-topic B2
└── Domain C
    └── ...
```

### 1.4 Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | ... | ... | ... |

### 1.5 Compliance Requirements

- Industry standards to follow
- Legal/regulatory constraints
- Organizational policies

---

## Phase 2: Architecture (4 hours)

### 2.1 Skill Structure

```
enterprise-skill/
├── SKILL.md                      # Core methodology (~400 lines)
├── references/
│   ├── methodology/              # Core principles
│   │   ├── principles.md
│   │   └── philosophy.md
│   ├── domains/                  # Domain details
│   │   ├── domain-a.md
│   │   ├── domain-b.md
│   │   └── domain-c.md
│   ├── practices/                # Best practices
│   │   ├── practice-1.md
│   │   └── practice-2.md
│   ├── troubleshooting.md        # Problem solving
│   ├── case-studies/             # Real examples
│   │   ├── case-1.md
│   │   └── case-2.md
│   └── templates/                # Reusable templates
│       └── template-1.md
└── assets/
    └── [template files]
```

### 2.2 Content Distribution

| File | Content | Lines |
|------|---------|-------|
| SKILL.md | Overview, entry points, navigation | ~400 |
| principles.md | Core philosophy | ~200 |
| domain-*.md | Domain deep-dives | ~300 each |
| practices.md | Best practices | ~200 |
| troubleshooting.md | Error resolution | ~150 |
| case-studies/*.md | Examples | ~200 each |

### 2.3 Cross-References

Map relationships between components:
- Domain A references principles X, Y
- Practice 1 applies to domains A, B
- Case study 1 demonstrates methodology

---

## Phase 3: Development (8 hours)

### Step 1: Create Core (SKILL.md)

```markdown
---
name: [methodology-name]
description: >
  [Organization]'s [domain] methodology.
  Use when: [comprehensive trigger list].
tags: [tag1, tag2, tag3, tag4, tag5]
version: 1.0.0
---

# [Methodology Name]

## Philosophy

[Core philosophy and principles]

### First Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

### Cultural Values
- [Value 1]
- [Value 2]

## Methodology Overview

### The [Name] Process
1. [Phase 1]
2. [Phase 2]
3. [Phase 3]
4. [Phase 4]
5. [Phase 5]

### Decision Framework
```
[Decision tree diagram]
```

## Domains

### Domain A: [Name]
[Overview]
- Details: references/domains/domain-a.md
- Practices: references/practices/practice-a.md

### Domain B: [Name]
[Overview]
- Details: references/domains/domain-b.md

## Capabilities

✅ [Capability 1]
✅ [Capability 2]
✅ [Capability 3]
✅ [Capability 4]
✅ [Capability 5]
✅ [Capability 6]

## Quality Standards

### Minimum Requirements
- [Requirement 1]
- [Requirement 2]

### Excellence Criteria
- [Criterion 1]
- [Criterion 2]

## Safety & Compliance

### Safety Requirements
- [Safety 1]
- [Safety 2]

### Compliance Checklist
- [ ] [Compliance item 1]
- [ ] [Compliance item 2]

## Error Handling

### Critical Errors
[Serious issues requiring immediate attention]

### Common Issues
[Routine problems and solutions]

### Escalation
When to escalate: [criteria]
Escalation path: [process]

## Examples

### Case Study 1: [Name]
Summary: [Brief description]
Details: references/case-studies/case-1.md

### Case Study 2: [Name]
Summary: [Brief description]
Details: references/case-studies/case-2.md

## References

| Need | Resource |
|------|----------|
| Core principles | references/methodology/principles.md |
| [Domain A] details | references/domains/domain-a.md |
| Best practices | references/practices/ |
| Troubleshooting | references/troubleshooting.md |
| Case studies | references/case-studies/ |
```

### Step 2: Create Domain References

**references/domains/domain-a.md:**
```markdown
# Domain A: [Name]

## Overview
[What this domain covers]

## Key Concepts

### Concept 1
[Detailed explanation]

### Concept 2
[Detailed explanation]

## Technical Details

### Standard 1
[Specification]

### Standard 2
[Specification]

## Common Scenarios

### Scenario 1
**Situation:** [Description]
**Approach:** [Methodology]
**Outcome:** [Expected result]

### Scenario 2
...

## Integration with Other Domains
- Links to Domain B: [relationship]
- Links to Domain C: [relationship]

## References
- Principles: ../methodology/principles.md
- Practices: ../practices/practice-1.md
```

### Step 3: Create Methodology References

**references/methodology/principles.md:**
```markdown
# Core Principles

## Principle 1: [Name]

### Definition
[Clear definition]

### Application
[How to apply]

### Examples
- [Example 1]
- [Example 2]

### Anti-Patterns
- [What not to do]

## Principle 2: [Name]
...
```

### Step 4: Create Case Studies

**references/case-studies/case-1.md:**
```markdown
# Case Study: [Project Name]

## Background
[Context and situation]

## Challenge
[What needed to be solved]

## Methodology Applied
1. [Step 1 with reasoning]
2. [Step 2 with reasoning]
3. [Step 3 with reasoning]

## Results
[Quantitative and qualitative outcomes]

## Lessons Learned
- [Lesson 1]
- [Lesson 2]

## Key Takeaways
[Transferable insights]
```

---

## Phase 4: Validation (4 hours)

### 6-Dimension Deep Evaluation

| Dimension | Score | Evidence | Improvement |
|-----------|-------|----------|-------------|
| System Prompt | _/10 | [Notes] | [Action] |
| Domain Knowledge | _/10 | [Notes] | [Action] |
| Workflow | _/10 | [Notes] | [Action] |
| Error Handling | _/10 | [Notes] | [Action] |
| Examples | _/10 | [Notes] | [Action] |
| Metadata | _/10 | [Notes] | [Action] |

**Targets:**
- All dimensions ≥ 8.5
- Average ≥ 9.0

### Testing Protocol

1. **Unit Testing**
   - Test each capability independently
   - Verify error handling

2. **Integration Testing**
   - Test cross-domain scenarios
   - Verify navigation between references

3. **User Testing**
   - Have target users test
   - Gather feedback

4. **Compliance Review**
   - Verify safety requirements
   - Check regulatory compliance

---

## Phase 5: Certification (2 hours)

### Final Review

- [ ] All 6 dimensions ≥ 8.5
- [ ] All references complete
- [ ] Cross-references verified
- [ ] Examples validated
- [ ] Safety review passed
- [ ] Compliance checklist complete
- [ ] Documentation reviewed
- [ ] Version tagged

### Release Checklist

- [ ] README for skill users
- [ ] Installation instructions
- [ ] Quick start guide
- [ ] Migration guide (if applicable)
- [ ] Support channels defined
- [ ] Update process documented

---

## Example: Tesla Engineer Methodology

```markdown
---
name: tesla-engineer
description: >
  Tesla first-principles engineering methodology.
  Use when: designing automotive systems, solving complex engineering
  problems, optimizing for cost and performance, or making safety-critical
tags: [tesla, engineering, automotive, first-principles, safety]
version: 1.0.0
---

# Tesla Engineer Methodology

## Philosophy

### First Principles Thinking
"Break down problems to fundamental truths and build up from there."

### Core Values
1. **Safety First** - No compromises on safety
2. **Cost Optimization** - Relentless cost reduction
3. **Rapid Iteration** - Build, test, improve quickly
4. **Vertical Integration** - Own the entire stack when beneficial

## The Tesla Engineering Process

### Phase 1: Deconstruct
Break the problem into fundamental components.

### Phase 2: Question Assumptions
Challenge every assumption with "Why?"

### Phase 3: First-Principles Analysis
Build up from physics, chemistry, economics.

### Phase 4: Design
Create solutions unconstrained by analogy.

### Phase 5: Prototype
Build the simplest version that tests the key hypothesis.

### Phase 6: Test & Iterate
Measure, learn, improve rapidly.

## Domains

### Battery Systems
- Cell chemistry optimization
- Thermal management
- Battery management systems
- Safety protocols
[Details: references/domains/battery-systems.md]

### Power Electronics
- Inverter design
- Motor control
- Efficiency optimization
[Details: references/domains/power-electronics.md]

### Manufacturing
- Design for manufacturing
- Automation
- Quality control
[Details: references/domains/manufacturing.md]

### Safety Engineering
- Crashworthiness
- Battery safety
- System redundancy
[Details: references/domains/safety-engineering.md]

## Quality Standards

### Safety Requirements
- All systems fail-safe
- Single points of failure eliminated
- Comprehensive testing protocols

### Cost Targets
- Bill of materials ≤ target
- Manufacturing time ≤ target
- Maintenance cost ≤ target

### Performance Metrics
- Efficiency ≥ target
- Reliability ≥ target
- User experience ≥ target

## Safety & Compliance

### Automotive Safety Standards
- [ ] FMVSS compliance
- [ ] Euro NCAP requirements
- [ ] Internal safety audits

### Battery Safety
- [ ] Thermal runaway prevention
- [ ] Crash protection
- [ ] Abuse testing passed

## Error Handling

### Critical Safety Issues
**Immediate action required:**
- Safety system failure
- Uncontrolled energy release
- Structural integrity compromise

**Response:** Stop work, escalate to safety team immediately.

### Engineering Challenges
**When stuck:**
1. Return to first principles
2. Question constraints
3. Consult domain experts
4. Prototype and test

## Case Studies

### Case Study 1: 4680 Battery Cell
Revolutionary cell design reducing cost by 56%.
[Details: references/case-studies/4680-cell.md]

### Case Study 2: Gigafactory Shanghai
From groundbreaking to production in 10 months.
[Details: references/case-studies/shanghai-gigafactory.md]

## References

| Topic | Resource |
|-------|----------|
| Core principles | references/methodology/principles.md |
| First-principles guide | references/methodology/first-principles.md |
| Battery systems | references/domains/battery-systems.md |
| Power electronics | references/domains/power-electronics.md |
| Manufacturing | references/domains/manufacturing.md |
| Safety engineering | references/domains/safety-engineering.md |
| Cost analysis | references/practices/cost-analysis.md |
| Rapid prototyping | references/practices/rapid-prototyping.md |
| Case studies | references/case-studies/ |
```

---

## Checklist

**Before certification:**

- [ ] Complete methodology defined
- [ ] Multiple domains documented
- [ ] Safety requirements specified
- [ ] Compliance checklist complete
- [ ] 5+ comprehensive case studies
- [ ] All 6 dimensions ≥ 8.5
- [ ] Integration testing passed
- [ ] User testing completed
- [ ] Documentation complete
- [ ] Version 1.0.0 tagged

**All checked?** Your Enterprise skill is certified!

---

**Related:**
- Lite Workflow → ./lite-workflow.md
- Standard Workflow → ./standard-workflow.md
- Flexibility Framework → ./flexibility-framework.md
