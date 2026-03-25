# Quick Mode Workflow

> Fast path to working skills. Perfect for prototypes and personal tools.

**Time:** ~15 minutes  
**Target Score:** 6.0-6.5  
**Use for:** Personal use, prototypes, low-risk scenarios

---

## Overview

```
Define (2 min) → Create (10 min) → Check (3 min) = Done! ✅
```

---

## Phase 1: Define (2 minutes)

### The One-Sentence Test

Can you describe your skill in one sentence?

**Template:**
```
This skill [does what] for [who] to [achieve what].
```

**Examples:**
- "This skill rotates PDFs for anyone who needs to change page orientation."
- "This skill generates marketing copy for marketers creating ad campaigns."
- "This skill analyzes CSV data for analysts exploring datasets."

**If you can't say it in one sentence → Scope is unclear. Narrow it down.**

---

### Identify ONE Core Capability

**Not:** "PDF rotator, merger, splitter, compressor, and editor"  
**Yes:** "PDF rotator - changes page orientation"

**Why:** Quick mode = one thing done well.

---

## Phase 2: Create (10 minutes)

### Step 1: Create SKILL.md (7 minutes)

Use this template:

```markdown
---
name: [skill-name]
description: "[What it does]. Use when: [trigger situations]."
---

# [Skill Name]

## What I Do
[One paragraph describing the single capability]

## Usage
- "[Example command 1]"
- "[Example command 2]"

## How It Works
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Common Issues
- **[Issue 1]:** [Quick solution]
- **[Issue 2]:** [Quick solution]
```

**Example - PDF Rotator:**

```markdown
---
name: pdf-rotator
description: "Rotate PDF pages. Use when: user needs to change PDF orientation."
---

# PDF Rotator

## What I Do
I rotate PDF pages to change their orientation (portrait ↔ landscape).

## Usage
- "Rotate this PDF 90 degrees"
- "Make this PDF landscape"

## How It Works
1. Read the PDF file
2. Rotate specified pages
3. Save with "_rotated" suffix

## Common Issues
- **File not found:** Check the file path
- **Wrong rotation:** Specify clockwise or counter-clockwise
```

---

### Step 2: Quick Self-Review (3 minutes)

**The 4-Point Check:**

| Check | Question | Action if No |
|-------|----------|--------------|
| ✅ Clear | Can I explain this to a friend in 30 seconds? | Simplify description |
| ✅ Complete | Does it have metadata, usage, and workflow? | Add missing section |
| ✅ Testable | Can I imagine a test case? | Add example |
| ✅ Safe | Could this cause harm if wrong? | Add basic error handling |

---

## Phase 3: Check (3 minutes)

### The 60-Second Test

**Mental simulation:**

1. **User says:** "[Example usage]"
2. **Skill should:** [Expected behavior]
3. **Edge case:** "What if [bad input]?"
4. **Should respond:** [Error handling]

**Example:**

1. User: "Rotate report.pdf 90 degrees"
2. Skill: Rotates all pages, saves as report_rotated.pdf
3. Edge case: File doesn't exist
4. Response: "File not found. Please check the path."

**If you can trace through this → Good enough for Quick mode!**

---

### Quality Estimate

Give yourself a rough score:

| Dimension | Score | Check |
|-----------|-------|-------|
| System Prompt | 6/10 | Role defined? |
| Domain Knowledge | 6/10 | Basic accuracy? |
| Workflow | 6/10 | Steps clear? |
| Error Handling | 5/10 | Basic cases covered? |
| Examples | 6/10 | 1-2 examples? |
| Metadata | 6/10 | Name + description clear? |
| **Average** | **5.8** | **→ 6.0 target** ✅ |

---

## Done! Next Steps

### Option 1: Use It Now

Your skill is ready for personal use. Test it!

### Option 2: Upgrade Later

If it proves useful, upgrade to Standard:
```
Quick skill → Test in real use → Gather feedback → Standard upgrade
```

---

## Quick Mode Examples

### Example 1: URL Shortener

```markdown
---
name: url-shortener
description: "Create short URLs. Use when: user wants to shorten a link."
---

# URL Shortener

## What I Do
I generate short, shareable URLs from long links.

## Usage
- "Shorten https://example.com/very/long/url"
- "Create short link for this URL"

## How It Works
1. Validate the URL
2. Generate short code
3. Return short URL

## Common Issues
- **Invalid URL:** Must start with http:// or https://
- **Already short:** No benefit for URLs < 30 chars
```

**Time to create:** 12 minutes  
**Score:** 6.2/10  
**Status:** ✅ Ready for personal use

---

### Example 2: Date Formatter

```markdown
---
name: date-formatter  
description: "Format dates. Use when: user needs to convert date formats."
---

# Date Formatter

## What I Do
I convert dates between formats (e.g., US → ISO, relative → absolute).

## Usage
- "Convert 12/31/2024 to ISO format"
- "What date is 'next Friday'?"

## How It Works
1. Parse input date
2. Identify target format
3. Convert and return

## Common Issues
- **Ambiguous date:** "01/02/2024" → Ask: US (Jan 2) or EU (Feb 1)?
- **Invalid date:** "February 30" → Error: Date doesn't exist
```

**Time to create:** 10 minutes  
**Score:** 6.5/10  
**Status:** ✅ Ready for personal use

---

## When to NOT Use Quick Mode

Don't use Quick mode if:

- ❌ Other people will depend on this
- ❌ Failure has serious consequences
- ❌ Handling sensitive data
- ❌ Required to be 100% accurate (medical, legal, financial)
- ❌ You have time for proper development

**If any checked → Use Standard or Strict mode**

---

## Quick Mode Checklist

**Before declaring "done":**

- [ ] Can explain skill in one sentence
- [ ] SKILL.md exists with metadata
- [ ] One clear capability defined
- [ ] At least one usage example
- [ ] Basic workflow described
- [ ] Common errors acknowledged
- [ ] Mental test passes

**All checked?** → Your Quick mode skill is ready! 🚀

---

## Summary

```
┌─────────────────────────────────────────────┐
│           QUICK MODE IN NUMBERS             │
├─────────────────────────────────────────────┤
│ Time: 15 minutes                            │
│ Target Score: 6.0-6.5                       │
│ Files: 1 (SKILL.md)                         │
│ Examples: 1-2                               │
│ Error Handling: Basic                       │
│ Testing: Mental simulation                  │
│ Review: Self-check only                     │
└─────────────────────────────────────────────┘
```

**Remember:** Quick mode isn't "low quality" — it's "right-sized for the context." A perfect Quick mode skill is better than an unfinished Strict mode skill.

---

**Related:**
- Flexibility Framework → ./flexibility-framework.md
- Standard Workflow → ./standard-workflow.md
- First Skill Tutorial → ../onboarding/first-skill.md
