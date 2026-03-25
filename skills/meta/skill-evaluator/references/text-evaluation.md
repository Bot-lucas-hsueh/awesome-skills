# Text Quality Evaluation

> 6-dimension rubric for assessing skill file craftsmanship

---

## Overview

Text quality evaluation measures the **craftsmanship** of skill files:
- Structure and organization
- Content depth and accuracy
- Polish and completeness

---

## Dimension 1: System Prompt (20%)

### 10/10 - Exemplary
- Crystal clear role definition
- Specific behavior guidelines
- Appropriate boundaries (what NOT to do)
- Tone/persona well-defined
- Self-consistent throughout

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

---

## Dimension 2: Domain Knowledge (20%)

### 10/10 - Exemplary
- Deep, accurate expertise
- Comprehensive coverage
- Current best practices
- Appropriate depth for tier
- No factual errors

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

---

## Dimension 3: Workflow (20%)

### 10/10 - Exemplary
- Clear step-by-step process
- Well-defined entry/exit points
- Decision trees for variations
- Validation checkpoints
- Handles all capabilities

### 8/10 - Good
- Clear steps
- Most variations covered
- Minor gaps

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

---

## Dimension 4: Error Handling (15%)

### 10/10 - Exemplary
- Comprehensive edge cases
- Graceful degradation
- Clear error messages
- Recovery suggestions
- Fail-safe behavior

### 8/10 - Good
- Common errors covered
- Helpful messages
- Most edge cases handled

### 6/10 - Acceptable
- Basic errors handled
- Some edge cases missing

### 4/10 - Poor
- Few errors covered
- Unhelpful messages

### 2/10 - Critical
- No error handling
- Crashes on bad input

---

## Dimension 5: Examples (15%)

### 10/10 - Exemplary
- Multiple diverse examples
- Simple and complex cases
- Clear input/output pairs
- Error cases included
- Realistic scenarios

### 8/10 - Good
- 3-4 examples
- Good variety
- Clear demonstrations

### 6/10 - Acceptable
- 2-3 examples
- Basic coverage

### 4/10 - Poor
- 1-2 examples
- Limited variety

### 2/10 - Critical
- No examples
- Or examples don't work

---

## Dimension 6: Metadata (10%)

### 10/10 - Exemplary
- Clear, specific name
- Comprehensive description
- Specific trigger phrases
- Appropriate tags
- Version specified

### 8/10 - Good
- Clear name
- Good description
- Some triggers

### 6/10 - Acceptable
- Name ok
- Basic description

### 4/10 - Poor
- Unclear name
- Vague description

### 2/10 - Critical
- Missing or broken metadata

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

---

## Tier Targets

| Tier | Minimum | Target |
|------|---------|--------|
| Lite | 6.0 | 7.0+ |
| Standard | 7.0 | 8.0+ |
| Enterprise | 8.0 | 9.0+ |

---

**Lines:** ~150 | Load for text quality evaluation
