# 6-Dimension Quality Rubric

> Detailed scoring criteria for skill evaluation

---

## Scoring Scale

| Score | Meaning | Action |
|-------|---------|--------|
| 1-3 | Critical issues | Major revision required |
| 4-5 | Below acceptable | Significant improvements needed |
| 6-6.5 | Minimum viable | OK for personal/internal use |
| 7-8 | Good | Suitable for team sharing |
| 9-10 | Excellent | Production-ready, exemplary |

---

## Dimension 1: System Prompt

### 10/10 - Exemplary
- Crystal clear role definition
- Specific behavior guidelines
- Appropriate boundaries (what NOT to do)
- Tone/persona well-defined
- Self-consistent throughout

**Example:**
```markdown
You are a React architecture expert with 10 years experience.
You help teams design scalable React applications.
You ask clarifying questions before recommendations.
You do NOT write full implementations—only architecture guidance.
You prefer functional components and modern hooks patterns.
```

### 8/10 - Good
- Clear role
- Some boundaries defined
- Minor ambiguities

### 6/10 - Acceptable
- Basic role stated
- Few boundaries
- Some confusion possible

### 4/10 - Poor
- Vague role
- Missing boundaries
- Conflicting guidance

### 2/10 - Critical
- No clear role
- Cannot understand purpose
- Confusing or missing

### Evaluation Questions
- [ ] Is the role immediately clear?
- [ ] Are boundaries defined?
- [ ] Is the tone appropriate?
- [ ] Is it self-consistent?

---

## Dimension 2: Domain Knowledge

### 10/10 - Exemplary
- Deep, accurate expertise
- Comprehensive coverage
- Current best practices
- Appropriate depth for tier
- No factual errors

**Example:**
```markdown
## React 18 Concurrent Features

React 18 introduced automatic batching which groups state updates
to reduce re-renders. This differs from React 17 where updates were
batched only in React event handlers...

[Deep technical detail showing expertise]
```

### 8/10 - Good
- Accurate knowledge
- Good coverage
- Minor gaps

### 6/10 - Acceptable
- Basic knowledge correct
- Some gaps
- Adequate for simple cases

### 4/10 - Poor
- Superficial knowledge
- Significant gaps
- May mislead users

### 2/10 - Critical
- Inaccurate information
- Outdated practices
- Potentially harmful

### Evaluation Questions
- [ ] Is information accurate?
- [ ] Is coverage appropriate?
- [ ] Is it current/up-to-date?
- [ ] Is depth appropriate for tier?

---

## Dimension 3: Workflow

### 10/10 - Exemplary
- Clear step-by-step process
- Well-defined entry/exit points
- Decision trees for variations
- Validation checkpoints
- Handles all capabilities

**Example:**
```markdown
## Architecture Design Workflow

1. **Gather Requirements**
   - Scale expectations? [small|medium|large]
   - Team expertise? [junior|mid|senior]
   - Performance needs? [standard|high|critical]

2. **Analyze Constraints**
   - If existing codebase → Review patterns used
   - If greenfield → Recommend modern stack
   - If integration required → Check compatibility

3. **Recommend Architecture**
   - Present 2-3 options
   - Tradeoff analysis for each
   - Default recommendation with reasoning
   
4. **Implementation Guidance**
   - Provide folder structure
   - Key libraries with versions
   - Migration steps if applicable
```

### 8/10 - Good
- Clear steps
- Most variations covered
- Minor gaps in edge cases

### 6/10 - Acceptable
- Basic workflow exists
- Main path clear
- Some edge cases missing

### 4/10 - Poor
- Unclear process
- Missing steps
- Confusing flow

### 2/10 - Critical
- No workflow defined
- Ad hoc approach
- Users can't follow

### Evaluation Questions
- [ ] Are steps clear?
- [ ] Are entry/exit points defined?
- [ ] Are variations handled?
- [ ] Is it complete for all capabilities?

---

## Dimension 4: Error Handling

### 10/10 - Exemplary
- Comprehensive edge cases
- Graceful degradation
- Clear error messages
- Recovery suggestions
- Fail-safe behavior

**Example:**
```markdown
## Error Handling

### Invalid Input
"Unable to process: input format not recognized.

Supported formats:
- CSV (.csv)
- Excel (.xlsx, .xls)
- JSON (.json)

Please convert your file or paste data directly."

### Missing Data
"Analysis requires [specific field] which is not present.

Options:
1. Provide data with this field
2. Use alternative analysis: [link]
3. Continue with limited scope (results may be incomplete)"

### System Errors
"An unexpected error occurred. [Error code: X]

Please try:
1. Retry the operation
2. Check input format
3. If persists, try with smaller dataset"
```

### 8/10 - Good
- Common errors covered
- Helpful messages
- Most edge cases handled

### 6/10 - Acceptable
- Basic errors handled
- Some edge cases missing
- Recovery suggestions basic

### 4/10 - Poor
- Few errors covered
- Unhelpful messages
- Poor recovery

### 2/10 - Critical
- No error handling
- Crashes on bad input
- Unpredictable behavior

### Evaluation Questions
- [ ] Are common errors covered?
- [ ] Are messages helpful?
- [ ] Is recovery suggested?
- [ ] Is it fail-safe?

---

## Dimension 5: Examples

### 10/10 - Exemplary
- Multiple diverse examples
- Simple and complex cases
- Clear input/output pairs
- Error cases included
- Realistic scenarios

**Example:**
```markdown
## Examples

### Example 1: Basic Usage
**Input:** "Rotate report.pdf 90 degrees"
**Process:**
1. Verify file exists
2. Rotate all pages 90° clockwise
3. Save as report_rotated.pdf
**Output:** "✅ Rotated all pages. Saved to report_rotated.pdf"

### Example 2: Selective Rotation
**Input:** "Rotate pages 2-5 of scan.pdf"
**Process:**
1. Verify scan.pdf exists (8 pages)
2. Rotate pages 2,3,4,5
3. Save as scan_rotated.pdf
**Output:** "✅ Rotated pages 2-5 of 8. Saved to scan_rotated.pdf"

### Example 3: Batch Processing (Advanced)
**Input:** "Rotate all PDFs in /reports folder"
**Process:**
1. Find all PDF files in directory
2. Rotate each 90°
3. Save with _rotated suffix
**Output:** "✅ Processed 12 files. Rotated versions saved with _rotated suffix."

### Example 4: Error Case
**Input:** "Rotate protected.pdf"
**Process:**
1. Attempt to open file
2. Detect password protection
**Output:** "❌ Cannot rotate: file is password protected.
Please remove password or provide unprotected copy."
```

### 8/10 - Good
- 3-4 examples
- Good variety
- Clear demonstrations

### 6/10 - Acceptable
- 2-3 examples
- Basic coverage
- Some variety

### 4/10 - Poor
- 1-2 examples
- Limited variety
- Unclear demonstrations

### 2/10 - Critical
- No examples
- Or examples don't work
- Or completely unclear

### Evaluation Questions
- [ ] Are there multiple examples?
- [ ] Do they cover main scenarios?
- [ ] Are error cases included?
- [ ] Are they realistic?

---

## Dimension 6: Metadata

### 10/10 - Exemplary
- Clear, specific name
- Comprehensive description
- Specific trigger phrases
- Appropriate tags
- Version specified

**Example:**
```yaml
---
name: react-architect
description: >
  React architecture expert for designing scalable applications.
  Use when: planning React projects, choosing state management,
  designing component hierarchies, optimizing performance,
  or reviewing React codebase architecture.
tags: [react, frontend, architecture, javascript, spa]
version: 2.1.0
---
```

### 8/10 - Good
- Clear name
- Good description
- Some triggers
- Minor improvements possible

### 6/10 - Acceptable
- Name ok
- Basic description
- Vague triggers
- Functional

### 4/10 - Poor
- Unclear name
- Vague description
- Missing triggers
- Hard to discover

### 2/10 - Critical
- Missing or broken metadata
- Cannot be triggered
- Unusable

### Evaluation Questions
- [ ] Is name clear and specific?
- [ ] Are trigger phrases specific?
- [ ] Is description informative?
- [ ] Are tags appropriate?

---

## Scoring Worksheet

| Dimension | Score | Evidence | Improvement |
|-----------|-------|----------|-------------|
| System Prompt | _/10 | | |
| Domain Knowledge | _/10 | | |
| Workflow | _/10 | | |
| Error Handling | _/10 | | |
| Examples | _/10 | | |
| Metadata | _/10 | | |
| **TOTAL** | **_/60** | **→ _/10** | |

---

## Priority Improvements

After scoring, prioritize fixes:

1. **Dimensions scoring < 6** → Fix first (critical)
2. **Lowest dimension** → Next priority
3. **Easy wins** → Quick improvements
4. **Nice to have** → If time permits

---

## Tier Targets

| Tier | Minimum | Target |
|------|---------|--------|
| Lite | 6.0 | 7.0+ |
| Standard | 7.0 | 8.0+ |
| Enterprise | 8.0 | 9.0+ |

---

**Related:**
- Why 6 Dimensions? → ../../concepts/why-6-dimensions.md
- Standards → ../standards.md
