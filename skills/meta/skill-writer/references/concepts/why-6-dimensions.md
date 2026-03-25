# Why Six Quality Dimensions?

## The Problem: What Makes a Skill "Good"?

Without clear criteria, quality becomes subjective:

- "It feels right"
- "It works for me"
- "I like the style"

**We need objective, measurable dimensions.**

---

## Why 6 Dimensions?

### Why Not 3?

Too few = miss critical aspects  
Example: "Works, Fast, Nice" misses safety, maintainability...

### Why Not 10?

Too many = too complex to evaluate  
Example: 10 dimensions = decision fatigue, inconsistent scoring

### 6 is the Sweet Spot

- ✅ Covers all critical aspects
- ✅ Manageable cognitive load
- ✅ Industry-proven frameworks use 5-7 dimensions
- ✅ Can be evaluated in reasonable time

---

## The 6 Dimensions Explained

### Dimension 1: System Prompt

**Question:** Does the AI clearly understand its role and behavior?

**What to check:**
- Clear role definition
- Specific behavior guidelines
- Appropriate tone/persona
- Scope boundaries (what NOT to do)

**Example (Good):**
```
You are a React architecture expert with 10 years of experience.
You help teams design scalable React applications.
You ask clarifying questions before making recommendations.
You do NOT write full implementations—only architecture guidance.
```

**Example (Bad):**
```
You are helpful assistant. Help with React.
```

**Why it matters:**
- Defines the AI's "personality" and approach
- Prevents scope creep
- Sets user expectations

---

### Dimension 2: Domain Knowledge

**Question:** Is the expertise accurate, deep, and comprehensive?

**What to check:**
- Technical accuracy
- Depth of knowledge
- Coverage of relevant topics
- Up-to-date information

**Example (Good):**
```
React 18 introduced automatic batching, which groups state updates
to reduce re-renders. This is different from React 17 where updates
were batched only in React event handlers...
```

**Example (Bad):**
```
React is a JavaScript library for building UIs. It uses components.
```

**Why it matters:**
- Users rely on skill for expert guidance
- Inaccurate knowledge → bad decisions
- Superficial knowledge → missed edge cases

---

### Dimension 3: Workflow

**Question:** Is there a clear process from input to output?

**What to check:**
- Step-by-step process defined
- Clear entry/exit points
- Decision trees for variations
- Validation checkpoints

**Example (Good):**
```
## Architecture Design Workflow

1. **Gather Requirements**
   - Ask about scale expectations
   - Identify team expertise level
   - Determine performance requirements

2. **Analyze Constraints**
   - Review existing codebase
   - Check integration requirements
   - Identify non-negotiables

3. **Recommend Architecture**
   - Present 2-3 options with tradeoffs
   - Default to proven patterns
   - Highlight risks of each approach

4. **Implementation Guidance**
   - Provide code structure
   - Suggest key libraries
   - Outline migration steps if applicable
```

**Example (Bad):**
```
Just ask what they need and suggest something.
```

**Why it matters:**
- Consistent quality across uses
- Reduces cognitive load for AI
- Users know what to expect

---

### Dimension 4: Error Handling

**Question:** Does it gracefully handle edge cases and failures?

**What to check:**
- Common error scenarios covered
- Graceful degradation
- Clear error messages
- Recovery suggestions

**Example (Good):**
```
## Error Handling

### Invalid Input
"The PDF file appears corrupted. Try:
1. Re-download the file
2. Use a different PDF reader to verify
3. If still failing, the file may be password-protected"

### Missing Dependencies
"PDF processing requires PyPDF2. Install with:
pip install PyPDF2

If using conda:
conda install -c conda-forge pypdf2"
```

**Example (Bad):**
```
If errors occur, try again or check the file.
```

**Why it matters:**
- Real-world usage involves failures
- Good error handling = user trust
- Bad error handling = abandoned skill

---

### Dimension 5: Examples

**Question:** Are there clear demonstrations of correct usage?

**What to check:**
- Multiple examples covering different scenarios
- Both simple and complex cases
- Input/output pairs
- Common mistake examples (what NOT to do)

**Example (Good):**
```
## Examples

### Example 1: Basic Rotation
**Input:** "Rotate this PDF 90 degrees clockwise"
**Process:** 
1. Confirm source file
2. Apply 90° rotation to all pages
3. Save with "_rotated" suffix

**Output:** Rotated PDF file

### Example 2: Selective Rotation
**Input:** "Rotate only pages 2-5 of report.pdf"
**Process:**
1. Parse page range
2. Rotate specified pages only
3. Preserve other pages

**Output:** PDF with only pages 2-5 rotated

### Example 3: Error Case
**Input:** "Rotate this corrupted file"
**Response:** "Unable to process - file appears corrupted. 
See Error Handling section for recovery options."
```

**Example (Bad):**
```
Example: "Rotate a PDF"
```

**Why it matters:**
- Examples are the best documentation
- Reduces ambiguity
- Shows expected behavior

---

### Dimension 6: Metadata

**Question:** Is the skill information complete and accurate?

**What to check:**
- Clear, specific name
- Accurate description with trigger phrases
- Correct version
- Appropriate tags/categories

**Example (Good):**
```yaml
---
name: react-architect
description: >
  React architecture expert for designing scalable applications.
  Use when: planning React projects, choosing state management,
  designing component hierarchies, or optimizing performance.
tags: [react, frontend, architecture, javascript]
version: 2.1.0
---
```

**Example (Bad):**
```yaml
---
name: react-helper
description: Helps with React
---
```

**Why it matters:**
- Users find the right skill
- Triggers activate correctly
- Version tracking for updates

---

## Scoring System

### 1-10 Scale

| Score | Meaning | Action |
|-------|---------|--------|
| 1-3 | Critical issues | Major revision needed |
| 4-5 | Below acceptable | Significant improvements needed |
| 6-6.5 | Minimum viable | OK for internal/personal use |
| 7-8 | Good quality | Suitable for team sharing |
| 9-10 | Excellent | Production-ready, exemplary |

### Tier Targets

| Tier | Minimum Score | Target Score |
|------|--------------|--------------|
| Lite | 6.0 | 7.0+ |
| Standard | 7.0 | 8.0+ |
| Enterprise | 8.0 | 9.0+ |

---

## Interdependencies

Dimensions don't exist in isolation:

```
System Prompt ──┐
Domain Knowledge ├─→ Enables → Workflow
                │
Examples ───────┘     ↓
                 Error Handling
                      ↓
                 Metadata (wraps all)
```

**Example:**
- Good System Prompt + Poor Domain Knowledge = "Confident but wrong"
- Good Workflow + Poor Error Handling = "Works until it doesn't"
- All good + Poor Examples = "Great but users don't understand how to use"

---

## Evaluation Process

### Quick Check (5 minutes)
- Skim each dimension
- Note obvious issues
- Calculate rough score

### Standard Evaluation (30 minutes)
- Review each dimension in detail
- Check against examples
- Verify accuracy
- Calculate detailed score

### Deep Evaluation (2 hours)
- Test with real inputs
- Verify all examples work
- Check edge cases
- Review against rubric
- Calculate precise score

---

## Common Weakness Patterns

| Pattern | Weak Dimensions | Fix Strategy |
|---------|-----------------|--------------|
| "Expert but vague" | System Prompt ✓, Domain Knowledge ✓, Examples ✗ | Add concrete examples |
| "Process-heavy" | Workflow ✓, System Prompt ✗ | Clarify role and boundaries |
| "Works on happy path" | All except Error Handling | Add comprehensive error scenarios |
| "Invisible" | Metadata ✗ | Improve name, description, triggers |

---

## Summary

```
┌─────────────────────────────────────────────────────┐
│              6-DIMENSION QUALITY MODEL              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. System Prompt     → "Who am I?"                │
│  2. Domain Knowledge  → "What do I know?"          │
│  3. Workflow          → "How do I work?"           │
│  4. Error Handling    → "What if things break?"    │
│  5. Examples          → "Show me how"              │
│  6. Metadata          → "How do users find me?"    │
│                                                     │
│  Target: ≥ 7.0 for production use                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Remember:** Quality is multidimensional. A skill can be strong in some areas and weak in others. The goal is balanced excellence.

---

**Related:**
- What is a Skill? → references/concepts/what-is-skill.md
- Why 3 Tiers? → references/concepts/why-tiered.md
- Scoring Guide → references/scoring/rubric.md
