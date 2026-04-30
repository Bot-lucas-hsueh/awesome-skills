---
name: to-prd
kind: workflow
version: 1.0.0
tags:
  - domain: engineering
  - subtype: to-prd
  - methodology: product-requirements-document
description: "Converts conversation context into a structured Product Requirements Document (PRD) and publishes it to the project issue tracker. Do NOT interview the user — synthesize what is already known. Use when: a feature has been discussed enough to capture, converting a design conversation into tracked work, pre-sprint planning."
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
  inspired_by: mattpocock/skills
---

# To PRD

## One-Liner

Synthesize what has already been discussed into a structured Product Requirements Document — without interviewing the user again.

---

## § 1 · Core Constraint

**Do NOT interview the user.** This skill runs after a design conversation has already happened. Its job is to organize and commit that knowledge — not to gather more. If key information is missing, note the gap in the PRD's "Open Questions" section rather than pausing to ask.

---

## § 2 · Workflow

### Step 1 — Codebase Exploration

Before writing anything:

1. Read `CONTEXT.md` if present — use its canonical terms throughout the PRD
2. Read relevant ADRs — the PRD must not contradict past decisions without noting it
3. Identify the major modules the feature will touch or create
4. Note any existing patterns the new code should follow (naming, error handling, testing)

### Step 2 — Module Sketch

Before drafting the PRD body, sketch the major modules:

- What new modules will be created?
- What existing modules will be modified?
- Prefer **deep modules**: encapsulate significant behavior behind a simple, testable interface

This sketch goes into the PRD's Implementation Decisions section.

### Step 3 — Write the PRD

Use this template:

---

**PRD: [Feature Name]**

**Problem Statement**
[One paragraph: what user problem does this solve? What is the cost of not building it?]

**Solution**
[One paragraph: what does the feature do at a high level?]

**User Stories**
1. As a [role], I want to [action] so that [benefit]
2. ...

**Implementation Decisions**
- Module: `<name>` — owns [behavior]; interface: [description]
- Module: `<name>` — modified to [change]; seam used: [description]
- [Pattern to follow]: [rationale]

**Testing Decisions**
- [Behavior to test]: [test type and approach]
- [Edge case]: [how it will be covered]

**Out of Scope**
- [Explicitly excluded functionality]

**Open Questions**
- [Anything that needs a human decision before implementation starts]

**Further Notes**
- [Performance considerations, security notes, rollout strategy, etc.]

---

**Important:** Do not include specific file paths or implementation code in the PRD. File paths rot rapidly; behavior descriptions survive. Implementation will determine exact paths.

### Step 4 — Publish

Post the PRD to the project issue tracker with:
- Label: `needs-triage` (so the issue enters the triage workflow)
- Title format: `feat: [feature name]`
- Link back to the conversation or design session if available

---

## § 3 · PRD Quality Checklist

| Check | Pass Condition |
|-------|---------------|
| Uses canonical terms | All entity/action names match `CONTEXT.md` |
| No file paths | Implementation details left to implementation phase |
| Explicit out-of-scope | At least one item listed |
| Module sketch present | Major modules identified and their interfaces described |
| Open questions captured | Missing info noted, not blocking the PRD |
| Testable user stories | Each story has an implied acceptance test |

---

## § 4 · When to Use This Skill

**Use when:**
- A feature has been fully or mostly designed in conversation
- Preparing for a sprint and need to create issues
- An enhancement issue was promoted from `issue-triage` to `ready-for-human` and needs a full spec

**Do NOT use when:**
- The feature has not been discussed at all (nothing to synthesize)
- The goal is just a small bug fix (overkill — use `debug-diagnose`)

---

## § 5 · Relationship to Other Skills

| Skill | When to reach for it |
|-------|---------------------|
| `zoom-out` | Run first to map what modules the feature will touch |
| `issue-triage` | After publishing — triage the created issue |
| `tdd-workflow` | When implementation begins — start from the user stories as behaviors |
| `architecture-review` | If the PRD reveals a need for significant structural changes |
