# Restore Reference

> 7-step restoration methodology, diagnosis tools, research guides, and quality gates.

---

## When to Restore vs. When to Rewrite

| Situation | Action |
|-----------|--------|
| Score 7.5–9.0, structure intact | Restore — targeted fixes |
| Score 5.0–7.5, good domain content | Restore — structural surgery |
| Score < 5.0, mostly generic | Rewrite — use CREATE mode |
| Score < 5.0, wrong domain | Rewrite from scratch |

If more than 60% of the content is generic filler, rewriting is faster than restoring.

---

## Step 1 · Diagnose (15 min)

**Never assume you know the problem before fully reading the skill.**

Read SKILL.md and every reference file. Then fill out this checklist:

```
Structural Issues:
[ ] Missing §1.1 Identity
[ ] Missing §1.2 Decision Framework
[ ] Missing §1.3 Thinking Patterns
[ ] Flat structure (no references/)
[ ] SKILL.md > 400 lines

Content Issues:
[ ] Generic claims ("professional", "industry leader", "best practices")
[ ] No specific data (numbers, companies, frameworks)
[ ] Workflow lacks Done/Fail criteria
[ ] < 5 examples, or examples are shallow
[ ] Error handling is absent or vague

Quality Issues:
[ ] Current text score: ___
[ ] Current runtime score: ___
[ ] Variance: ___
[ ] Dimensions scoring < 6: ___
```

**Deliverable**: Diagnosis report — list every issue, categorize as P0/P1/P2.

**Fix order**: Structural → Content → Quality (always in this sequence).

---

## Step 2 · Research (30–60 min)

Generic content is the root cause of most low scores. Research is the cure.

**Research targets**:

| What to find | Where to find it | How to use it |
|--------------|-----------------|---------------|
| Company financials | Annual reports, Crunchbase | Replace "large company" with "$4.2B revenue, 2023" |
| Named methodologies | Wikipedia, official docs | Replace "proven framework" with "TOGAF 9.2 architecture framework" |
| Industry benchmarks | Gartner, McKinsey reports | Replace "significant improvement" with "34% reduction per Gartner 2024" |
| Domain terminology | Internal docs, textbooks | Replace "technical terms" with actual jargon users recognize |
| Case studies | Company blogs, case study sites | Replace generic scenarios with real outcomes |

**Minimum research time**: 30 minutes for Standard tier, 60 minutes for Enterprise. Skipping research produces a skill that looks restored but still feels generic at runtime.

---

## Step 3 · Architecture Design (20 min)

Before writing, design the structure. A skill written without a blueprint always needs restructuring.

```
Design checklist:
[ ] Tier confirmed (Lite / Standard / Enterprise)
[ ] §1.1 identity drafted (role + DNA + context)
[ ] §1.2 decision framework outlined (priority hierarchy)
[ ] §1.3 thinking patterns named (3–5 patterns)
[ ] Domain knowledge sections mapped
[ ] Workflow phases planned (4–6 phases, Done/Fail per phase)
[ ] 5 examples designed (context, input, expected output)
[ ] Progressive disclosure split planned:
    SKILL.md: navigation + key frameworks (≤ 300 lines)
    references/: deep dives + full examples
```

---

## Step 4 · Progressive Disclosure Setup (15 min)

Restructure the file layout before filling content.

**Target structure**:
```
skill-name/
├── SKILL.md              ← navigation hub (≤ 300 lines)
└── references/
    ├── [workflow].md     ← detailed phase descriptions
    ├── [domain].md       ← deep domain knowledge
    ├── [examples].md     ← full example transcripts
    └── [anti-patterns].md
```

**Migration rule**: For each section in SKILL.md, ask: "Does a user need this to navigate the skill, or to execute a specific step?" If execution → move to references/.

---

## Step 5 · Content Production (60–90 min)

Fill sections in priority order — highest-impact first:

1. **§1.1 Identity** — specific role, real DNA, concrete context
2. **§1.2 Decision Framework** — named priorities, tie-breaking rules
3. **§1.3 Thinking Patterns** — 3–5 named, illustrated patterns
4. **Domain Knowledge** — replace all generics with researched specifics
5. **Workflow** — add Done/Fail criteria to every phase
6. **Examples** — write 5 scenarios with realistic data
7. **Anti-Patterns** — named failures with specific fixes

**Self-check while writing**: If you can replace a phrase with "by a random skilled professional" and it still makes sense — it's generic. Find the specific data.

---

## Step 6 · Validate (15–30 min)

Score the restored skill before delivery using the dual-track rubric.

**Targets**:
- Text ≥ 8.0
- Runtime ≥ 8.0
- Variance < 1.0
- All dimensions ≥ 6.0

**If score < 8.0 after restoration**:
1. Check System Prompt completeness first (worth 20% — most common gap)
2. Find remaining generic content and replace with specific data
3. Add examples until you have 5 with realistic inputs and edge cases
4. Re-score

**If variance > 2.0**:
- High Text, Low Runtime: skill is well-documented but model doesn't execute as described — simplify or rewrite the instructions that describe the behavior
- High Runtime, Low Text: skill works but is poorly documented — improve structure and specificity

---

## Step 7 · Deliver (10 min)

```
Delivery checklist:
[ ] SKILL.md ≤ 300 lines
[ ] references/ directory exists with at least 1 file
[ ] EVALUATION_REPORT.md saved with before/after scores
[ ] File structure verified
[ ] Original version backed up (git history or snapshot)
```

**EVALUATION_REPORT.md template**:
```
## Restoration Report

**Before**: X.X/10 (Text: X.X, Runtime: X.X, Variance: X.X)
**After**:  X.X/10 (Text: X.X, Runtime: X.X, Variance: X.X)
**Improvement**: +X.X points

### Changes Made
1. [What changed and why]
2. [What changed and why]
...

### Remaining Gaps
- [Any dimensions still below 8.0 and why]
```

---

## Quality Gates Summary

| Step | Gate | Fail Action |
|------|------|-------------|
| 1 Diagnose | All issues identified and categorized | Re-read skill, be more thorough |
| 2 Research | Specific data found for every generic claim | Continue researching |
| 3 Architecture | Blueprint designed before writing | Stop and design first |
| 4 Disclosure | File structure set up | Restructure before filling content |
| 5 Content | No generic claims remain | Return to Step 2 |
| 6 Validate | Score ≥ 9.0, variance < 1.0 | Iterate on weakest dimension |
| 7 Deliver | All files present, report saved | Complete missing files |

---

## Common Restoration Patterns

### Pattern: The Generic Shell

**Symptom**: Skill has correct structure but all content is filler ("professional consultation", "strategic analysis", "industry expertise").

**Fix**: Step 2 (Research) before anything else. Every section needs real data before it gets better.

### Pattern: The Undisclosed Monolith

**Symptom**: SKILL.md is 800+ lines, no references/, everything in one file.

**Fix**: Step 4 (Progressive Disclosure). Move everything except navigation to references/. Usually cuts SKILL.md by 60–70%.

### Pattern: The Headless Skill

**Symptom**: Good domain content, but no System Prompt (§1.1/1.2/1.3). Score capped at ~7.0.

**Fix**: Add System Prompt sections first. They account for 20% — fixing them alone often raises score by 2+ points.

### Pattern: The Example Desert

**Symptom**: 0–2 examples, all generic.

**Fix**: Write 5 realistic scenarios. Each should have: specific context, real inputs, concrete expected outputs, and at least one edge case.
