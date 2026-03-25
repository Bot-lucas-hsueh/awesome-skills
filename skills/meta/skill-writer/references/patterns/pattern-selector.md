# Pattern Selector

> Interactive guide to choose the right design pattern

---

## Quick Selector

Answer these questions to find your pattern:

### Question 1: What is the primary output?

| Answer | Pattern |
|--------|---------|
| Modified/transformed input | **Tool Wrapper** |
| Generated content | **Generator** |
| Assessment/feedback | **Reviewer** |
| Transformed data through stages | **Pipeline** |
| Depends on information gathered | **Inversion** |

---

## Detailed Scenarios

### Scenario A: Tool/Library Skills

**Indicators:**
- Users provide input to process
- Skill uses specific tool/library
- Clear input/output transformation

**Examples:**
- "Rotate this PDF"
- "Format this code"
- "Query this API"

**Pattern:** **Tool Wrapper**

**Next:** Read design-patterns.md#pattern-1-tool-wrapper

---

### Scenario B: Content Creation Skills

**Indicators:**
- Users need specific output type
- Template-based generation
- Variable inputs produce structured outputs

**Examples:**
- "Generate meeting notes"
- "Write a PR description"
- "Create a report"

**Pattern:** **Generator**

**Next:** Read design-patterns.md#pattern-2-generator

---

### Scenario C: Evaluation Skills

**Indicators:**
- Users provide existing content
- Skill assesses quality/correctness
- Output is feedback/recommendations

**Examples:**
- "Review this code"
- "Check this document"
- "Audit this for security"

**Pattern:** **Reviewer**

**Next:** Read design-patterns.md#pattern-3-reviewer

---

### Scenario D: Process Skills

**Indicators:**
- Multiple sequential steps
- Each step has specific purpose
- Clear stage progression

**Examples:**
- "Process this data"
- "Approve this content"
- "Handle this incident"

**Pattern:** **Pipeline**

**Next:** Read design-patterns.md#pattern-4-pipeline

---

### Scenario E: Consultative Skills

**Indicators:**
- Need information before helping
- Questions lead to recommendations
- Advice depends on context

**Examples:**
- "Design this system"
- "Debug this issue"
- "Plan this project"

**Pattern:** **Inversion**

**Next:** Read design-patterns.md#pattern-5-inversion

---

## Decision Tree

```
What does your skill do?
│
├─ Transforms input using tools?
│  └─ Tool Wrapper
│
├─ Creates new content?
│  └─ Generator
│
├─ Evaluates existing content?
│  └─ Reviewer
│
├─ Processes through multiple steps?
│  └─ Pipeline
│
└─ Requires gathering information first?
   └─ Inversion
```

---

## Pattern Comparison

| Pattern | Input | Output | Complexity | Examples |
|---------|-------|--------|------------|----------|
| **Tool Wrapper** | Raw data/tool params | Processed result | Low | PDF rotator, API client |
| **Generator** | Variables/template params | Generated content | Low-Med | Report generator, email writer |
| **Reviewer** | Existing content | Assessment/feedback | Med | Code reviewer, editor |
| **Pipeline** | Raw data | Transformed output | Med-High | ETL process, approval workflow |
| **Inversion** | User responses | Customized result | Med | Consultant, diagnostic tool |

---

## Still Unsure?

Describe your skill in this format:

```
My skill helps users [action] by [method].
Users provide [input] and receive [output].
An example interaction: [brief example]
```

**Example:**
```
My skill helps users create meeting notes by structuring their input.
Users provide discussion points and receive formatted notes.
Example: User says "Meeting with John about project X, discussed timeline and budget"
→ Skill generates structured meeting notes
```

**Analysis:** Creates output from input → **Generator** pattern

---

**Next:**
- Read about your selected pattern → ./design-patterns.md
- Learn tier selection → ../../concepts/why-tiered.md
- Start creating → ../../workflow/lite-workflow.md
