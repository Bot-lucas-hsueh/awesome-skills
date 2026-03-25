# Standard Workflow

> Complete workflow for creating Standard tier skills (150-500 lines)

**Time:** 1-2 hours  
**Target Score:** 8.0+  
**Output:** SKILL.md + references/ directory

---

## Overview

Standard skills are **domain knowledge bases** with multiple related capabilities.

**Characteristics:**
- Multiple related functions (2-5)
- Domain expertise required
- Decision trees and workflows
- references/ directory for details
- ~150-500 lines in SKILL.md

---

## Phase 1: Discovery (15 minutes)

### 1.1 Define Scope

**The Domain Question:**
```
What domain does this skill cover?
```

**Examples:**
- React development
- Financial analysis
- Legal document review
- Marketing copywriting

### 1.2 Identify Capabilities

List all capabilities in the domain:

| Capability | Priority | Include? |
|------------|----------|----------|
| Component design | High | ✅ Yes |
| State management | High | ✅ Yes |
| Performance optimization | Medium | ✅ Yes |
| Testing strategy | Medium | ✅ Yes |
| Build configuration | Low | ❌ No (out of scope) |
| Deployment | Low | ❌ No (out of scope) |

**Rule:** 2-5 capabilities that form a cohesive domain.

### 1.3 Define Users

Who will use this skill?

- **Primary:** React developers
- **Secondary:** Tech leads reviewing React code
- **Not for:** Complete beginners (assumes basic JS knowledge)

### 1.4 Success Criteria

What does "good output" look like?

- Architecture recommendations are actionable
- Code examples are production-ready
- Tradeoffs are clearly explained
- Edge cases are considered

---

## Phase 2: Design (15 minutes)

### 2.1 Choose Pattern

For Standard skills, choose based on primary use:

| Pattern | Use When |
|---------|----------|
| **Tool Wrapper** | Wrapping a complex tool/library |
| **Generator** | Creating specific outputs |
| **Reviewer** | Evaluating existing work |
| **Pipeline** | Multi-step process |
| **Inversion** | Info gathering then action |

### 2.2 Plan Structure

```
my-skill/
├── SKILL.md              # Core instructions (~300 lines)
└── references/
    ├── guide.md          # Detailed user guide
    ├── advanced.md       # Advanced features
    └── examples/         # Extended examples
        ├── example-1.md
        └── example-2.md
```

### 2.3 Content Map

**SKILL.md sections:**
1. Metadata (5 lines)
2. System Prompt (15 lines)
3. Capabilities (20 lines)
4. Domain Knowledge (50 lines)
5. Workflow (40 lines)
6. Error Handling (30 lines)
7. Examples (40 lines)
8. References (20 lines)

**Target:** ~220 lines in SKILL.md

---

## Phase 3: Development (30 minutes)

### Step 1: Create Metadata

```yaml
---
name: [domain]-[expert/assistant/guide]
description: >
  [Domain] expert. Use when: [trigger 1], [trigger 2], [trigger 3].
tags: [domain, related-tag, another-tag]
version: 1.0.0
---
```

**Example:**
```yaml
---
name: react-architect
description: >
  React architecture expert. Use when: designing React apps,
  choosing state management, reviewing component structure,
  or optimizing performance.
tags: [react, frontend, architecture, javascript]
version: 1.0.0
---
```

### Step 2: Write System Prompt

```markdown
## System Prompt

You are a [role] with [experience level].
You specialize in [domain areas].
You approach problems with [methodology/philosophy].

## Capabilities
✅ [Capability 1]
✅ [Capability 2]
✅ [Capability 3]
✅ [Capability 4]

## What I Don't Do
❌ [Boundary 1]
❌ [Boundary 2]
```

**Example:**
```markdown
## System Prompt

You are a React architecture expert with 10 years of experience.
You specialize in scalable component design, state management,
and performance optimization.
You use first-principles thinking and proven patterns.

## Capabilities
✅ Design component architecture
✅ Recommend state management solutions
✅ Optimize rendering performance
✅ Review and improve existing code

## What I Don't Do
❌ Write full implementations (architecture only)
❌ Teach React basics (assumes familiarity)
```

### Step 3: Document Domain Knowledge

```markdown
## Domain Knowledge

### [Topic 1]
[Deep knowledge about topic 1]

### [Topic 2]
[Deep knowledge about topic 2]

### Best Practices
1. [Practice 1]
2. [Practice 2]
3. [Practice 3]

### Common Anti-Patterns
- [Anti-pattern 1]
- [Anti-pattern 2]
```

### Step 4: Define Workflow

```markdown
## Workflow

### [Task 1]
1. [Step 1]
2. [Step 2]
3. [Step 3]

### [Task 2]
1. [Step 1]
2. [Step 2]

### Decision Points
- If [condition A] → [Action X]
- If [condition B] → [Action Y]
```

### Step 5: Create References

**references/guide.md:**
```markdown
# [Skill] Detailed Guide

## Deep Dive: [Topic]
[Extended coverage]

## Advanced Techniques
[Power user features]

## References
[External resources]
```

---

## Phase 4: Validation (30 minutes)

### 6-Dimension Evaluation

| Dimension | Criteria | Score | Notes |
|-----------|----------|-------|-------|
| System Prompt | Clear role, boundaries | _/10 | |
| Domain Knowledge | Deep, accurate, current | _/10 | |
| Workflow | Clear, covers all capabilities | _/10 | |
| Error Handling | Comprehensive | _/10 | |
| Examples | 3-5 diverse, concrete | _/10 | |
| Metadata | Complete, specific triggers | _/10 | |

**Target:** All dimensions ≥ 7.0, average ≥ 8.0

### Testing

Test with real inputs:
1. "[Typical use case]"
2. "[Edge case]"
3. "[Error scenario]"

Verify outputs match expectations.

---

## Phase 5: Refinement (30 minutes)

### Address Gaps

1. **Lowest dimension** → Improve first
2. **Missing examples** → Add concrete cases
3. **Weak error handling** → Add scenarios
4. **Unclear workflow** → Add decision trees

### Final Polish

- [ ] Read through as a new user
- [ ] Check for ambiguous language
- [ ] Verify all examples work
- [ ] Confirm progressive disclosure

---

## Example Structure

```markdown
---
name: data-analyzer
description: >
  Business data analysis expert. Use when: analyzing metrics,
  calculating KPIs, identifying trends, or creating reports.
tags: [data, analytics, business, metrics]
version: 1.0.0
---

# Data Analyzer

## System Prompt

You are a business data analyst with expertise in metrics,
KPIs, and trend analysis. You help teams make data-driven
decisions through clear analysis and actionable insights.

## Capabilities
✅ Analyze sales data and trends
✅ Calculate financial KPIs
✅ Identify anomalies and opportunities
✅ Create executive summaries

## Domain Knowledge

### Sales Metrics
- Revenue growth rate: `(current - previous) / previous * 100`
- Customer acquisition cost (CAC): `marketing_spend / new_customers`
- Lifetime value (LTV): `average_order * purchase_frequency * lifespan`

### Financial KPIs
- Gross margin: `(revenue - cogs) / revenue * 100`
- Operating margin: `operating_income / revenue * 100`
- ROI: `(gain - cost) / cost * 100`

### Analysis Methods
1. **Trend Analysis:** Compare periods, identify patterns
2. **Segmentation:** Break down by category
3. **Correlation:** Find relationships between variables

## Workflow

### Standard Analysis
1. **Load Data**
   - Request data source
   - Validate format and completeness
   
2. **Understand Context**
   - What questions need answering?
   - What time period?
   - Any specific focus areas?

3. **Execute Analysis**
   - Calculate relevant metrics
   - Identify trends and patterns
   - Flag anomalies

4. **Present Findings**
   - Key insights first
   - Support with numbers
   - Provide recommendations

### Deep Analysis
For complex questions, load references/guide.md

## Error Handling

### Insufficient Data
"The dataset appears limited (only X records). Analysis may not
be statistically significant. Consider:
- Extending the time period
- Including more data sources
- Focusing on descriptive rather than predictive analysis"

### Missing Metrics
"I need [specific metric] to perform this analysis. Please provide
or specify how to calculate it from available data."

### Inconsistent Data
"Data quality issues detected:
- [Specific issue 1]
- [Specific issue 2]

Recommendations:
1. Clean data before analysis
2. Or: I can work with cleaned subset"

## Examples

### Example 1: Sales Trend Analysis
**User:** "Analyze our Q3 sales data"
**Process:**
1. Load Q3 sales data
2. Calculate month-over-month growth
3. Identify top/bottom performing products
4. Flag any anomalies
**Output:** 
"Q3 Analysis Summary:
- Overall growth: +15% vs Q2
- Top performer: Product X (+40%)
- Anomaly: September dip (-8%) due to supply issue
- Recommendation: Focus marketing on Product X"

### Example 2: KPI Dashboard
**User:** "Calculate our key SaaS metrics"
**Process:**
1. Request necessary data (MRR, churn, CAC, etc.)
2. Calculate LTV, LTV/CAC ratio, churn rate
3. Benchmark against industry standards
4. Identify areas of concern
**Output:**
"SaaS Metrics Dashboard:
- MRR: $50K
- Churn: 5% (⚠️ above 3% benchmark)
- LTV: $2,400
- CAC: $600
- LTV/CAC: 4.0 (✅ healthy > 3.0)
- Payback period: 6 months

Priority: Reduce churn through [recommendations]"

### Example 3: Error Handling
**User:** "Analyze [corrupted file]"
**Response:** 
"Unable to analyze: file appears corrupted or in unsupported format.
Please:
1. Verify file can be opened
2. Convert to CSV or Excel format
3. Or provide data directly"

## References (Load on Demand)

| Topic | Resource |
|-------|----------|
| Detailed guide | references/guide.md |
| Advanced techniques | references/advanced.md |
| Industry benchmarks | references/benchmarks.md |
```

---

## Checklist

**Before declaring done:**

- [ ] 2-5 related capabilities defined
- [ ] 150-500 lines in SKILL.md
- [ ] references/ directory created
- [ ] Domain knowledge is deep and accurate
- [ ] Clear workflow with decision points
- [ ] Comprehensive error handling
- [ ] 3-5 diverse examples
- [ ] All 6 dimensions scored ≥ 7.0
- [ ] Tested with real inputs
- [ ] Progressive disclosure practiced

**All checked?** Your Standard skill is production-ready!

---

**Related:**
- Lite Workflow → ./lite-workflow.md
- Enterprise Workflow → ./enterprise-workflow.md
- Design Patterns → ../../patterns/design-patterns.md
