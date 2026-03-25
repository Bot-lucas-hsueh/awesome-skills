# Progressive Disclosure Deep Guide

> Master the art of "load what you need, when you need it"

---

## The Core Principle

**Progressive Disclosure** = Show essential information first, reveal details on demand.

### Why It Matters

| Metric | All-at-once | Progressive | Improvement |
|--------|-------------|-------------|-------------|
| Tokens loaded | 5,000 | 500 (avg) | **90% reduction** |
| Load time | 2-3s | 0.5s | **4x faster** |
| Relevant content | 20% | 95% | **5x better** |
| User confusion | High | Low | **Clearer** |

**Key insight:** Context window is shared, precious resource. Don't waste it.

---

## The Three-Level System

### Level 1: Metadata (Always Loaded)

**What:** Name + description + triggers  
**Size:** ~100 words  
**Purpose:** Decide IF to activate this skill

```yaml
---
name: data-analyzer
description: >
  Analyze business data. Use when: user mentions metrics, 
  KPIs, trends, sales data, or asks for data insights.
triggers: ["analyze data", "KPI", "metrics", "sales report"]
---
```

**When to use:** Always. This is the "front door" of your skill.

---

### Level 2: SKILL.md Body (Loaded When Triggered)

**What:** Core instructions, workflow, key examples  
**Size:** < 5,000 words  
**Purpose:** Tell AI HOW to execute

```markdown
# Data Analyzer

## System Prompt
You are a business data analyst...

## Capabilities
✅ Analyze sales trends
✅ Calculate KPIs
✅ Identify anomalies

## Workflow
1. Load data
2. Clean and validate
3. Analyze...

## Examples
[2-3 key examples]

## References
- Finance metrics: references/finance.md
- Sales metrics: references/sales.md
- Full guide: references/guide.md
```

**When to use:** When skill is activated. Keep it focused.

---

### Level 3: Bundled Resources (Loaded On Demand)

**What:** Detailed documentation, scripts, assets  
**Size:** Unlimited (loaded as needed)  
**Purpose:** Provide DEEP details for specific scenarios

```
references/
├── finance.md          # Loaded when user asks about finance
├── sales.md            # Loaded when user asks about sales
├── guide.md            # Loaded when user wants "more details"
└── api-reference.md    # Loaded for technical questions
```

**When to use:** Only when needed. Keeps main context lean.

---

## Three Disclosure Patterns

### Pattern 1: Main Guide + References

**Best for:** Skills with multiple, distinct capabilities

**Structure:**
```
SKILL.md:
  - Overview
  - Quick start
  - Capability summaries
  - "See references/X.md for details"

references/
  ├── capability-a.md   # Deep dive on A
  ├── capability-b.md   # Deep dive on B
  └── advanced.md       # Power user features
```

**Example:** Data Analyzer
- SKILL.md: "I can analyze sales, finance, and operations data"
- references/sales.md: All sales metrics and formulas
- references/finance.md: All financial KPIs and calculations

**Loading strategy:**
```
User: "Analyze sales data" → Load SKILL.md + references/sales.md
User: "Calculate ROI" → Load SKILL.md + references/finance.md
User: "Full guide" → Load SKILL.md + references/guide.md
```

---

### Pattern 2: Domain Separation

**Best for:** Cross-domain skills

**Structure:**
```
SKILL.md:
  - Domain-agnostic framework
  - "Choose domain: [sales|finance|ops]"

references/
  ├── domain-sales.md
  ├── domain-finance.md
  └── domain-ops.md
```

**Example:** Marketing Expert
- SKILL.md: Marketing framework (applies to all channels)
- references/seo.md: SEO-specific tactics
- references/social.md: Social media strategies
- references/email.md: Email marketing details

**Loading strategy:**
```
User: "SEO strategy" → Load SKILL.md + references/seo.md
User: "Email campaign" → Load SKILL.md + references/email.md
```

---

### Pattern 3: Conditional Details

**Best for:** Skills with basic vs. advanced usage

**Structure:**
```
SKILL.md:
  - Basic usage (covers 80% of cases)
  - "Advanced features in references/advanced.md"

references/
  ├── advanced.md       # Power user features
  ├── troubleshooting.md # Problem solving
  └── api-reference.md  # Technical details
```

**Example:** PDF Processor
- SKILL.md: Basic rotate, merge, split
- references/advanced.md: Batch processing, encryption, metadata editing

**Loading strategy:**
```
Default: Load only SKILL.md (basic features)
User: "Advanced options" → Load references/advanced.md
User: "It failed" → Load references/troubleshooting.md
User: "API details" → Load references/api-reference.md
```

---

## Decision Tree: When to Split

```
Start: Writing skill content
│
├─ Is this content ALWAYS needed?
│  ├─ Yes → Keep in SKILL.md
│  └─ No → Continue
│
├─ Is this content SPECIFIC to certain scenarios?
│  ├─ Yes → Split to references/[scenario].md
│  └─ No → Continue
│
├─ Is this content for BASIC vs ADVANCED users?
│  ├─ Basic → Keep in SKILL.md
│  └─ Advanced → Split to references/advanced.md
│
├─ Is this content a LONG list or REFERENCE?
│  ├─ Yes → Split to references/
│  └─ No → Continue
│
└─ Keep in SKILL.md with collapsible section
```

---

## File Organization Best Practices

### The Golden Rule

**SKILL.md = Table of Contents + Quick Reference**  
**references/ = Detailed Chapters**

### Directory Structure

```
my-skill/
├── SKILL.md              # Essential only (<300 lines ideal)
│
├── references/
│   ├── guide.md          # Full user guide
│   ├── advanced.md       # Advanced features
│   ├── troubleshooting.md # Error resolution
│   ├── api-reference.md  # Technical details
│   └── examples/         # Extended examples
│       ├── example-1.md
│       └── example-2.md
│
├── scripts/              # Executable tools
│   └── helper.py
│
└── assets/               # Templates/files
    └── template.docx
```

### Naming Conventions

| File | Purpose | Example |
|------|---------|---------|
| `guide.md` | Complete user guide | `references/guide.md` |
| `advanced.md` | Power user features | `references/advanced.md` |
| `troubleshooting.md` | Problem solving | `references/troubleshooting.md` |
| `api-reference.md` | Technical docs | `references/api-reference.md` |
| `[domain].md` | Domain-specific | `references/finance.md` |
| `[capability].md` | Capability deep-dive | `references/validation.md` |

---

## Common Mistakes

### ❌ Mistake 1: Everything in SKILL.md

**Problem:** 2000-line SKILL.md

**Why wrong:**
- Slow to load
- Most content never used
- Hard to maintain

**Fix:** Split by scenario into references/

---

### ❌ Mistake 2: Over-splitting

**Problem:** 50 files in references/, each 20 lines

**Why wrong:**
- Fragmented context
- Hard to navigate
- Overhead exceeds benefit

**Fix:** Combine related content. Aim for 100+ lines per reference file.

---

### ❌ Mistake 3: Vague References

**Problem:**
```markdown
For more info, see references/docs.md
```

**Why wrong:** AI doesn't know WHEN to load it.

**Fix:** Be specific:
```markdown
For finance metrics, load references/finance.md
For error resolution, load references/troubleshooting.md
```

---

### ❌ Mistake 4: No Loading Triggers

**Problem:** References exist but SKILL.md never mentions them

**Why wrong:** AI never loads them

**Fix:** Include explicit trigger conditions:
```markdown
## References (Load on Demand)
- Finance metrics → references/finance.md
- Sales metrics → references/sales.md
- Full guide → references/guide.md
```

---

## Metrics: Good vs Bad Disclosure

### Good Progressive Disclosure

| Metric | Target |
|--------|--------|
| SKILL.md length | 100-300 lines |
| References count | 2-10 files |
| Reference file size | 100-500 lines |
| Load efficiency | >80% content used |
| User requests "more info" | <20% of interactions |

### Bad Progressive Disclosure

| Metric | Red Flag |
|--------|----------|
| SKILL.md length | >1000 lines |
| References count | >20 files or 0 files |
| Reference file size | <50 lines each |
| Load efficiency | <50% content used |
| User confusion | "What can this do?" |

---

## Examples: Before & After

### Before (Poor Disclosure)

```markdown
# Data Analyzer

[2000 lines of content including:]
- All metrics definitions (500 lines)
- All formulas (300 lines)
- All examples (400 lines)
- Troubleshooting (300 lines)
- API reference (500 lines)
```

**Result:** Always loads 2000 lines, uses 200 lines average

---

### After (Good Disclosure)

```markdown
# Data Analyzer

## Capabilities
I analyze business data across sales, finance, and operations.

## Quick Start
1. Provide your data
2. Specify metrics you want
3. I'll analyze and report

## References (Load on Demand)
- Sales metrics → references/sales.md
- Finance metrics → references/finance.md
- Operations metrics → references/operations.md
- Full guide → references/guide.md
- Troubleshooting → references/troubleshooting.md
```

**Result:** Loads 100 lines, adds 200-500 lines on demand as needed

---

## Summary

```
┌─────────────────────────────────────────────────────────────┐
│              PROGRESSIVE DISCLOSURE CHECKLIST               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✅ SKILL.md < 300 lines (ideally < 200)                   │
│  ✅ Clear "when to load" triggers in SKILL.md              │
│  ✅ References organized by purpose                        │
│  ✅ Each reference file > 100 lines                        │
│  ✅ < 10 reference files total                             │
│  ✅ Examples in SKILL.md, details in references            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Remember:** The goal is "just enough, just in time." Not "everything, all at once."

---

**Related:**
- First Skill Tutorial → ./first-skill.md
- What is a Skill? → ../../concepts/what-is-skill.md
- Standard Workflow → ../workflow/standard-workflow.md
