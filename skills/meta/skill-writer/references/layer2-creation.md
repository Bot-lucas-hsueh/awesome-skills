# Layer 2: Creation Engine

## Purpose

Execute skill creation workflow from architecture to completion.

## Components

### Structure Generator

**SKILL.md Skeleton**:

```markdown
---
name: [skill-name]
description: '[One-line description with triggers]'
license: MIT
metadata:
  author: [name] <[email]>
  version: 1.0.0
  updated: 'YYYY-MM-DD'
  tags: [tag1, tag2]
  score: [target]/10
  quality: [target-tier]
---

# [Skill Name]

## One-Liner

[One-sentence description]

---

## § 1 · System Prompt

### § 1.1 · Identity & Worldview

[Who you are, professional DNA, context, success metrics]

### § 1.2 · Decision Framework

[Priority hierarchy, quality gates]

### § 1.3 · Thinking Patterns

[3-5 thinking patterns with concrete structures]

## § 2 · Problem Signature

[When to use, user signals]

## § 3 · Domain Knowledge

[Specific data, methodologies]

## § 4 · Workflow

[Phases with Done/Fail criteria]

## § 5 · Examples

[5 scenarios]

## § 6 · Anti-Patterns

[Common mistakes]
```

### Content Producer Rules

1. **No Generic Terms**:
   - ❌ "professional", "expert", "best practices"
   - ✅ "CRISPR-Cas9", "$2.3B revenue", "32-step process"

2. **Specific Data Required**:
   - Company names + metrics
   - Methodology names + steps
   - Tool names + versions + limits
   - Benchmark numbers

3. **Progressive Disclosure**:
   - SKILL.md: Summary only
   - references/: Full details

### Example Designer

Each example must have:
- Realistic context
- Specific user input
- Detailed expert response
- Concrete outputs

## Creation Workflow

1. **Generate Skeleton**: Create SKILL.md structure
2. **Write System Prompt**: §1.1/1.2/1.3 first
3. **Fill Domain Knowledge**: Research-specific data
4. **Design Workflow**: 4-5 phases with Done/Fail
5. **Create Examples**: 5 detailed scenarios
6. **Split to References**: Move details to references/
