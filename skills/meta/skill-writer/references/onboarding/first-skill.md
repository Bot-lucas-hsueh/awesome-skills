# Your First Real Skill

> Complete walkthrough: Create a PDF Rotator skill in 30 minutes

---

## What We're Building

**Skill:** PDF Rotator  
**What it does:** Rotates PDF pages  
**Complexity:** Lite tier  
**Time:** 30 minutes

---

## Phase 1: Understand the Skill (5 min)

### 1.1 Define the Problem

**What problem does this solve?**
Users need to change the orientation of PDF pages (portrait ↔ landscape).

**When would someone use this?**
- Scanned documents in wrong orientation
- Combining PDFs with different orientations
- Preparing documents for printing

### 1.2 List Capabilities

What can this skill do?

| Capability | Priority |
|------------|----------|
| Rotate all pages | Must have |
| Rotate specific page range | Nice to have |
| 90° clockwise/counter-clockwise | Must have |
| 180° flip | Nice to have |

**Decision:** Start with "Must have" only. Keep it simple.

### 1.3 Identify Edge Cases

What could go wrong?
- File doesn't exist
- File is corrupted
- File is password-protected
- User wants to rotate non-existent pages

---

## Phase 2: Plan the Structure (5 min)

### 2.1 Choose Tier

- Single function? ✅ Yes → **Lite**
- Lines estimate: ~100 lines → **Lite** confirmed

### 2.2 Design Files

```
pdf-rotator/
└── SKILL.md          # Only file needed for Lite
```

**Decision:** No scripts/, no references/. Keep it minimal.

### 2.3 Outline Content

```markdown
SKILL.md structure:
1. Metadata (name, description)
2. System Prompt (who am I)
3. Capabilities (what I can do)
4. Usage (how to use me)
5. Error Handling (what if it breaks)
6. Examples (show correct usage)
```

---

## Phase 3: Create the Skill (15 min)

### Step 1: Create Directory

```bash
mkdir pdf-rotator
cd pdf-rotator
```

### Step 2: Create SKILL.md

```markdown
---
name: pdf-rotator
description: "Rotate PDF pages. Use when: user needs to change PDF page orientation."
version: 1.0.0
---

# PDF Rotator

## System Prompt
You are a PDF rotation assistant. Your job is to help users rotate PDF pages.
You use Python with PyPDF2 library to perform rotations.
You are helpful, clear, and handle errors gracefully.

## Capabilities
✅ Rotate all pages in a PDF
✅ Rotate specific page ranges
✅ Support 90°, 180°, 270° rotations
✅ Preserve original file (create copy)

## What I Cannot Do
❌ Edit PDF content (text/images)
❌ Merge or split PDFs
❌ Convert PDF to other formats

## Usage

### Rotate All Pages
User: "Rotate this PDF 90 degrees clockwise"
Action: Rotate every page 90° clockwise

### Rotate Specific Pages
User: "Rotate pages 2-5 of document.pdf 90° counter-clockwise"
Action: Rotate only pages 2, 3, 4, 5

## Workflow

1. **Verify Input**
   - Confirm PDF file path exists
   - Validate rotation angle (90, 180, 270)
   - Identify target pages (all or specific range)

2. **Execute Rotation**
   - Use PyPDF2 to rotate specified pages
   - Create new file with "_rotated" suffix
   - Preserve original file

3. **Confirm Success**
   - Report pages rotated
   - Provide output file path
   - Note any issues

## Error Handling

### File Not Found
"I couldn't find the file at [path]. Please check:
- The file path is correct
- The file exists
- You have permission to access it"

### Corrupted PDF
"This PDF appears to be corrupted. Try:
1. Opening it in a PDF reader to verify
2. Re-downloading if from internet
3. Checking if it's password-protected"

### Invalid Page Range
"Invalid page range [range]. Please use:
- Single page: '5'
- Range: '2-5' (pages 2,3,4,5)
- All pages: leave unspecified"

### Password Protected
"This PDF is password-protected. I cannot rotate it.
Please remove the password first or provide an unprotected copy."

## Examples

### Example 1: Basic Rotation
**User:** "Rotate report.pdf 90 degrees"
**Process:**
1. Verify report.pdf exists
2. Rotate all pages 90° clockwise
3. Save as report_rotated.pdf
**Result:** "✅ Rotated all pages. Saved to report_rotated.pdf"

### Example 2: Selective Rotation
**User:** "Rotate pages 1-3 of scan.pdf 180 degrees"
**Process:**
1. Verify scan.pdf exists and has ≥3 pages
2. Rotate pages 1, 2, 3 by 180°
3. Save as scan_rotated.pdf
**Result:** "✅ Rotated pages 1-3. Saved to scan_rotated.pdf"

### Example 3: Error Case
**User:** "Rotate missing.pdf"
**Response:** "❌ File not found: missing.pdf. Please check the file path."

## Technical Details

**Library:** PyPDF2  
**Method:** `page.rotate_clockwise(angle)` or `page.rotate_counter_clockwise(angle)`  
**Output naming:** Original filename + "_rotated" suffix

## Best Practices
- Always preserve original file
- Validate inputs before processing
- Report specific error messages
- Confirm success with details
```

### Step 3: Save File

```bash
# Save as SKILL.md in pdf-rotator/ directory
```

---

## Phase 4: Validate (5 min)

### 4.1 Self-Review Checklist

| Check | Status |
|-------|--------|
| Clear metadata | ✅ |
| System prompt defines role | ✅ |
| Capabilities listed | ✅ |
| Limitations stated | ✅ |
| Workflow defined | ✅ |
| Error handling included | ✅ |
| Examples provided | ✅ |

### 4.2 Quality Score Estimate

| Dimension | Score | Notes |
|-----------|-------|-------|
| System Prompt | 8/10 | Clear role, good boundaries |
| Domain Knowledge | 8/10 | Accurate PyPDF2 usage |
| Workflow | 8/10 | Clear 3-step process |
| Error Handling | 8/10 | 4 common errors covered |
| Examples | 8/10 | 3 examples (success + error) |
| Metadata | 7/10 | Good, could add more tags |
| **Average** | **7.8/10** | **Production ready** ✅ |

---

## Phase 5: Test (Optional but Recommended)

### Test Case 1: Happy Path
```
Input: "Rotate my document.pdf 90 degrees"

Expected behavior:
1. Acknowledge request
2. Verify file exists
3. Explain rotation plan
4. Execute rotation (simulated)
5. Report success with output path
```

### Test Case 2: Error Path
```
Input: "Rotate nonexistent.pdf"

Expected behavior:
1. Attempt to locate file
2. Report file not found
3. Provide helpful suggestions
4. Ask for correct path
```

---

## Congratulations! 🎉

You just created a **production-quality Lite skill**!

### What You Learned

1. **Skill structure** - Metadata + instructions
2. **Lite tier** - Single function, ~100 lines
3. **6 dimensions** - All covered in your skill
4. **Error handling** - Anticipate problems
5. **Examples** - Show, don't just tell

### Your Skill Stats

| Metric | Value |
|--------|-------|
| Lines of code/docs | ~120 |
| Files created | 1 |
| Time spent | ~30 min |
| Quality score | 7.8/10 |
| Production ready | ✅ Yes |

---

## Next Steps

### Level Up This Skill

Add these to make it Standard tier:
- [ ] `references/` with PyPDF2 API details
- [ ] Script for actual PDF rotation
- [ ] More examples (batch processing, etc.)

### Create Another Skill

Try these ideas:
- **Image resizer** - Resize images to specific dimensions
- **URL shortener** - Generate short links
- **Date formatter** - Convert between date formats

### Go Deeper

- **Progressive disclosure** → ../progressive-guide.md
- **Standard workflow** → ../workflow/standard-workflow.md
- **Design patterns** → ../../patterns/design-patterns.md

---

**Related:**
- 30-Second Quick Start → ./quickstart.md
- Why Skills Work → ../../concepts/what-is-skill.md
- Progressive Disclosure → ./progressive-guide.md
