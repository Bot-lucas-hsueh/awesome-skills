# Anti-Patterns

> Common mistakes to avoid when creating skills

---

## Structure Anti-Patterns

### ❌ README.md

**Problem:** Creating separate README.md files

**Why:** Skills don't need READMEs. SKILL.md serves as documentation.

**Fix:** Put all documentation in SKILL.md or references/

---

### ❌ Over-Documentation

**Problem:** SKILL.md with 2000+ lines

**Why:** Wastes tokens, slow loading, most content never used

**Fix:** Use progressive disclosure. Keep SKILL.md < 300 lines, details in references/

---

### ❌ Under-Documentation

**Problem:** SKILL.md with only metadata and one line of instruction

**Why:** AI doesn't know what to do

**Fix:** Provide clear system prompt, capabilities, workflow, examples

---

### ❌ Missing references/

**Problem:** All content in SKILL.md, no references

**Why:** When skill grows, SKILL.md becomes unwieldy

**Fix:** Plan for growth. Put detailed content in references/ from the start

---

## Content Anti-Patterns

### ❌ Vague Descriptions

**Problem:**
```yaml
description: "Helps with stuff"
```

**Why:** Triggers don't activate, users don't know when to use

**Fix:**
```yaml
description: "PDF rotation tool. Use when: changing PDF orientation."
```

---

### ❌ Missing Error Handling

**Problem:** No error scenarios documented

**Why:** Skill fails unpredictably on bad input

**Fix:** Add Error Handling section with common errors and solutions

---

### ❌ No Examples

**Problem:** Instructions without demonstrations

**Why:** Users (and AI) don't know what "good" looks like

**Fix:** Include 2-5 concrete examples

---

### ❌ Over-Promising

**Problem:**
```markdown
## Capabilities
✅ Do everything related to X
```

**Why:** Unrealistic scope, poor performance

**Fix:** Be specific and limited:
```markdown
## Capabilities
✅ Specific capability 1
✅ Specific capability 2

## Limitations
❌ Out of scope: [thing it doesn't do]
```

---

### ❌ Ambiguous Workflow

**Problem:**
```markdown
## How to Use
Just analyze the data and provide insights.
```

**Why:** No clear process, inconsistent results

**Fix:**
```markdown
## Workflow
1. Load data
2. Validate format
3. Analyze trends
4. Present findings
```

---

## Tier Anti-Patterns

### ❌ Lite Over-Engineering

**Problem:** Creating Enterprise-tier documentation for a simple tool

**Why:** Wasted effort, maintenance burden

**Fix:** Match tier to complexity. PDF rotator → Lite, not Enterprise

---

### ❌ Enterprise Under-Engineering

**Problem:** Critical methodology with Lite-tier documentation

**Why:** Safety risks, incomplete coverage

**Fix:** Safety-critical skills need Enterprise rigor

---

### ❌ Wrong Tier Growth

**Problem:** Upgrading tier without adding real value

**Why:** Bloat without benefit

**Fix:** When upgrading:
- Lite → Standard: Add depth, references, more examples
- Standard → Enterprise: Add methodology, safety, compliance

---

## Metadata Anti-Patterns

### ❌ Generic Names

**Problem:** `helper`, `assistant`, `tool`

**Why:** Hard to discover, vague purpose

**Fix:** Specific names: `pdf-rotator`, `react-architect`

---

### ❌ No Triggers

**Problem:** Description without "Use when"

**Why:** AI doesn't know when to activate

**Fix:** Always include trigger phrases:
```yaml
description: "... Use when: [specific situations]"
```

---

### ❌ Missing Version

**Problem:** No version in metadata

**Why:** Can't track updates, compatibility issues

**Fix:** Always include:
```yaml
version: 1.0.0
```

---

## Progressive Disclosure Anti-Patterns

### ❌ Load Everything

**Problem:** All references loaded upfront

**Why:** Defeats purpose of progressive disclosure

**Fix:** Load on demand based on user needs

---

### ❌ Buried References

**Problem:** References exist but never mentioned in SKILL.md

**Why:** AI never loads them

**Fix:** Explicitly reference when to load:
```markdown
## References (Load on Demand)
- Advanced features → references/advanced.md
```

---

### ❌ Over-Splitting

**Problem:** 50 files in references/, each 20 lines

**Why:** Fragmented context, hard to navigate

**Fix:** Combine related content. Aim for 100+ lines per file.

---

## Safety Anti-Patterns

### ❌ No Safety Warnings

**Problem:** Safety-critical skill without warnings

**Why:** Potential harm to users

**Fix:** Add Safety section with clear warnings

---

### ❌ Insufficient Validation

**Problem:** No input validation before critical operations

**Why:** Dangerous operations on bad data

**Fix:** Validate inputs, add confirmation steps for critical actions

---

### ❌ Missing Escalation

**Problem:** No guidance on when to escalate

**Why:** Critical issues not properly handled

**Fix:** Define escalation criteria and process

---

## Summary Checklist

**Avoid these:**

- [ ] README.md (not needed)
- [ ] Over/under-documentation
- [ ] Vague descriptions
- [ ] Missing error handling
- [ ] No examples
- [ ] Over-promising capabilities
- [ ] Ambiguous workflow
- [ ] Wrong tier selection
- [ ] Generic names
- [ ] No version
- [ ] Loading everything upfront
- [ ] Buried references
- [ ] Safety issues (for critical skills)

---

**Related:**
- Standards → ./standards.md
- Quality Rubric → ./scoring/rubric.md
