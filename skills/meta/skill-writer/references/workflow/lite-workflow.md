# Lite Workflow

> Complete workflow for creating Lite tier skills (50-150 lines)

**Time:** 15-30 minutes  
**Target Score:** 7.0+  
**Output:** Single SKILL.md file (~100 lines)

---

## Overview

Lite skills are **single-function tools** with focused scope.

**Characteristics:**
- One specific capability
- Clear input/output
- Minimal decision trees
- No references/ directory needed
- No scripts/ directory needed

---

## Phase 1: Define (5 minutes)

### 1.1 The One-Sentence Test

Define your skill in one sentence:

```
This skill [does X] for [Y purpose].
```

**Examples:**
- "This skill rotates PDF pages for document orientation fixes."
- "This skill shortens URLs for easy sharing."
- "This skill converts CSV to JSON for data processing."

**If you can't say it in one sentence → Scope too broad.**

### 1.2 Identify the Single Capability

List what your skill does:

| Capability | Include? |
|------------|----------|
| Rotate PDF pages | ✅ Yes |
| Merge PDFs | ❌ No (different function) |
| Compress PDFs | ❌ No (different function) |

**Rule:** Only the core capability. Everything else is out of scope.

### 1.3 List Inputs and Outputs

**Inputs:**
- PDF file path
- Rotation angle (90, 180, 270)

**Outputs:**
- Rotated PDF file

### 1.4 Identify Edge Cases

- File doesn't exist
- File is corrupted
- Invalid rotation angle
- File is password-protected

---

## Phase 2: Design (5 minutes)

### 2.1 Choose Pattern

For Lite skills, use **Tool Wrapper** pattern:

```
Setup → Usage → Examples
```

### 2.2 Outline Structure

```markdown
SKILL.md:
1. Metadata (name, description)
2. System Prompt (role)
3. Capabilities (what it does)
4. Usage (how to use it)
5. Error Handling (edge cases)
6. Examples (demonstrations)
```

### 2.3 Estimate Lines

Target: 50-150 lines

| Section | Lines |
|---------|-------|
| Metadata | 5 |
| System Prompt | 10 |
| Capabilities | 10 |
| Usage | 15 |
| Error Handling | 20 |
| Examples | 30 |
| **Total** | **~90** ✅ |

---

## Phase 3: Create (10 minutes)

### Step 1: Metadata Block

```yaml
---
name: [skill-name]
description: "[What it does]. Use when: [trigger situations]."
version: 1.0.0
---
```

**Naming:**
- Use kebab-case: `pdf-rotator`, `url-shortener`
- Be specific: `csv-to-json` not `data-converter`

**Description:**
- Start with action: "Rotate PDFs...", "Shorten URLs..."
- Include trigger: "Use when: ..."

### Step 2: System Prompt

```markdown
## System Prompt

You are a [role description].
You [primary function].
You are [key characteristics].

## Capabilities
✅ [Capability 1]
✅ [Capability 2]

## Limitations
❌ [What you don't do]
❌ [What you don't do]
```

**Example:**
```markdown
## System Prompt

You are a PDF rotation assistant.
You help users rotate PDF pages to change orientation.
You are precise, helpful, and handle errors gracefully.

## Capabilities
✅ Rotate all pages in a PDF
✅ Rotate specific page ranges
✅ Support 90°, 180°, 270° rotations

## Limitations
❌ Edit PDF content
❌ Merge or split PDFs
❌ Convert to other formats
```

### Step 3: Usage

```markdown
## Usage

### [Use Case 1]
**Input:** "[Example command]"
**Process:**
1. [Step 1]
2. [Step 2]
3. [Step 3]
**Output:** [Expected result]

### [Use Case 2]
...
```

### Step 4: Error Handling

```markdown
## Error Handling

### [Error 1]
**Symptom:** [What happens]
**Solution:** [How to fix]

### [Error 2]
...
```

Cover:
- Invalid input
- Missing files
- Permission issues
- Unsupported formats

### Step 5: Examples

```markdown
## Examples

### Example 1: [Scenario]
**User:** "[Input]"
**Response:** [Expected output]

### Example 2: [Error Scenario]
**User:** "[Problematic input]"
**Response:** [Error handling]
```

Provide 2-3 examples covering:
- Happy path
- Edge case
- Error case

---

## Phase 4: Validate (5 minutes)

### Quick Quality Check

| Dimension | Check | Score |
|-----------|-------|-------|
| System Prompt | Role clear? | _/10 |
| Domain Knowledge | Accurate? | _/10 |
| Workflow | Steps clear? | _/10 |
| Error Handling | Cases covered? | _/10 |
| Examples | Concrete? | _/10 |
| Metadata | Complete? | _/10 |

**Target:** Average ≥ 7.0

### Self-Test

Mentally trace:
1. User says: "[Example usage]"
2. Skill responds: [Expected behavior]
3. Edge case: "[Bad input]"
4. Skill handles: [Error response]

**If flow works → Done!**

---

## Example: Complete Lite Skill

```markdown
---
name: csv-to-json
description: "Convert CSV files to JSON. Use when: user needs CSV to JSON conversion."
version: 1.0.0
---

# CSV to JSON Converter

## System Prompt

You are a CSV to JSON conversion tool.
You convert CSV files to JSON format accurately.
You handle headers, data types, and edge cases.

## Capabilities
✅ Convert CSV to JSON
✅ Handle headers automatically
✅ Detect data types (number, boolean, string)

## Limitations
❌ JSON to CSV conversion
❌ Complex nested structures
❌ Formula evaluation

## Usage

### Basic Conversion
**Input:** "Convert data.csv to JSON"
**Process:**
1. Read CSV file
2. Parse headers as keys
3. Convert rows to objects
4. Output JSON array

### With Options
**Input:** "Convert data.csv, use first column as ID"
**Process:** Convert to JSON with specified ID field

## Error Handling

### File Not Found
**Symptom:** "Cannot find file"
**Solution:** Check file path and permissions

### Malformed CSV
**Symptom:** "Parse error at line X"
**Solution:** Check for unescaped quotes or inconsistent columns

### Empty File
**Symptom:** "No data found"
**Solution:** Verify file contains data

## Examples

### Example 1: Basic Conversion
**User:** "Convert users.csv to JSON"
**Response:** 
```json
[
  {"name": "Alice", "age": 30},
  {"name": "Bob", "age": 25}
]
```

### Example 2: Type Detection
**User:** "Convert products.csv"
**Response:** 
```json
[
  {"id": 1, "price": 19.99, "in_stock": true},
  {"id": 2, "price": 29.99, "in_stock": false}
]
```

### Example 3: Error Case
**User:** "Convert missing.csv"
**Response:** "Error: File 'missing.csv' not found. Please check the path."
```

**Lines:** ~85  
**Score:** 7.5/10  
**Status:** ✅ Production ready

---

## Checklist

**Before declaring done:**

- [ ] Single, clear capability
- [ ] 50-150 lines total
- [ ] Metadata complete
- [ ] System prompt clear
- [ ] Capabilities and limitations listed
- [ ] Usage instructions provided
- [ ] Error handling included
- [ ] 2-3 examples provided
- [ ] Self-test passes
- [ ] Score ≥ 7.0

**All checked?** Your Lite skill is ready!

---

**Related:**
- Standard Workflow → ./standard-workflow.md
- Quick Mode → ./quick-mode.md
- What is a Skill? → ../../concepts/what-is-skill.md
