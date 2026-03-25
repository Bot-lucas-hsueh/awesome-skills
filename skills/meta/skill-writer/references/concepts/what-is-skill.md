# What is a Skill?

## Core Definition

A **Skill** is a specialized training manual for AI that transforms a general-purpose agent into a domain expert.

---

## Analogy: Education System

| Level | Analogy | Capability |
|-------|---------|------------|
| Base AI | High school graduate | General knowledge, can learn anything |
| + 1 Skill | Bachelor's degree | Specialized in one domain |
| + Multiple Skills | PhD + cross-training | Deep expertise + interdisciplinary |

---

## What Skills Actually Do

### Not: Teaching New Functions

❌ Wrong: "Skills teach AI how to call APIs"  
❌ Wrong: "Skills add new capabilities to AI"

### Yes: Providing Expert Perspective

✅ Correct: "Skills give AI a professional mindset"  
✅ Correct: "Skills are onboarding guides for specific domains"

### Example Comparison

**Without "Tesla Engineer" Skill:**
```
User: "Design an EV battery cooling system"
AI: "Here are some general principles of thermal management..."
     [Generic explanation, might miss critical constraints]
```

**With "Tesla Engineer" Skill:**
```
User: "Design an EV battery cooling system"
AI: "First, let's establish our constraints per Tesla standards:
     - Cell-to-cell temperature variance < 2°C
     - Coolant flow rate optimization for range
     - Safety cutoff at 60°C absolute max
     - Manufacturing cost targets...
     [Immediately applies Tesla's specific methodology]
```

---

## Skill vs. Other Concepts

| Concept | What It Is | Skill Equivalent |
|---------|-----------|------------------|
| **Library** | Reusable code | Scripts/ + Usage patterns |
| **Framework** | Development structure | Workflow patterns |
| **API Docs** | Interface reference | references/ directory |
| **Tutorial** | Learning material | Onboarding examples |
| **Template** | Starting point | assets/ directory |
| **Best Practices** | Guidelines | Domain knowledge in SKILL.md |

---

## Anatomy of a Skill

```
my-skill/
├── SKILL.md              # The "brain" - instructions for AI
│   ├── Metadata          # Name, description, triggers
│   ├── System Prompt     # Role definition
│   ├── Capabilities      # What it can do
│   ├── Workflow          # How to do it
│   └── Examples          # Show correct usage
│
├── scripts/              # Executable tools (optional)
│   └── helper.py         # Scripts the AI can run
│
├── references/           # Detailed docs (optional)
│   ├── guide.md          # Extended documentation
│   └── api-reference.md  # Technical details
│
└── assets/               # Templates/resources (optional)
    └── template.docx     # Files used in outputs
```

### SKILL.md = The Brain

This is the only required file. It contains everything the AI needs to know.

**Key insight:** AI reads SKILL.md like a human reads a job description. It learns:
- What is my role?
- What should I do?
- How should I behave?
- What are the examples of good work?

### scripts/ = The Hands

Optional scripts that the AI can execute. These are tools, not instructions.

**When to use:**
- Complex calculations
- File processing
- External API calls
- Anything better done with code than LLM reasoning

### references/ = The Library

Extended documentation loaded on demand. Keeps SKILL.md lean.

**When to use:**
- Detailed API documentation
- Long lists of options/parameters
- Domain-specific reference material
- Content only needed in specific scenarios

### assets/ = The Materials

Files used in the final output (templates, images, etc.).

**When to use:**
- Document templates
- Logo/image assets
- Data files
- Anything that becomes part of the deliverable

---

## Real-World Examples

### Example 1: PDF Rotator (Lite)

**What it does:** Rotates PDF pages

**Structure:**
```yaml
# SKILL.md
name: pdf-rotator
description: "Rotate PDF pages. Use when user needs to change PDF orientation."
---

Rotate PDF pages using PyPDF2 or similar.

## Usage
"Rotate this PDF 90 degrees clockwise"
"Rotate pages 2-5 of this PDF"
```

**Why it's Lite:**
- Single function
- Simple usage pattern
- No complex domain knowledge
- ~50 lines total

---

### Example 2: React Architecture Expert (Standard)

**What it does:** Guides React application architecture decisions

**Structure:**
```yaml
# SKILL.md
name: react-architect
description: "React architecture expert. Use when: designing React apps, choosing patterns."
---

You are a React architecture expert with 10 years experience.

## Capabilities
- Component architecture design
- State management selection
- Performance optimization
- Testing strategy

## Workflow
1. Understand requirements
2. Analyze tradeoffs
3. Recommend architecture
4. Provide implementation guidance

## References
- Component patterns: references/component-patterns.md
- State management: references/state-management-guide.md
- Performance: references/performance-optimization.md
```

**Why it's Standard:**
- Multiple related capabilities
- Domain expertise required
- Complex decision trees
- ~300 lines in SKILL.md + references

---

### Example 3: Tesla Engineer Methodology (Enterprise)

**What it does:** Complete engineering methodology for automotive design

**Structure:**
```yaml
# SKILL.md  
name: tesla-engineer
description: "Tesla engineering methodology. Use when: automotive design, safety-critical systems."
---

You embody Tesla's first-principles engineering culture.

## Philosophy
- First principles thinking
- Rapid iteration
- Safety above all
- Cost optimization

## Domains
- Battery systems
- Power electronics
- Manufacturing
- Safety engineering

## Methodology
[Detailed 10-step process]

## References (10+ files)
- references/battery-design.md
- references/safety-standards.md
- references/cost-analysis.md
...
```

**Why it's Enterprise:**
- Complete methodology system
- Multiple interconnected domains
- Safety-critical requirements
- ~1000+ lines across all files

---

## Key Insights

### 1. Skills are about Mindset, Not Functions

A "PDF Rotator" skill isn't about teaching AI the rotate_pdf() function. It's about:
- When to rotate (use case understanding)
- How to handle errors (robustness)
- What options to offer (user experience)
- Edge cases to consider (thoroughness)

### 2. Progressive Disclosure is Critical

Just like you don't read an entire textbook to answer one question, AI shouldn't load entire skill documentation for every interaction.

**Good:** Load overview → Load specific section when needed  
**Bad:** Load everything upfront → Waste tokens → Slow responses

### 3. Skills Compose Together

Multiple skills can work together:

```
User: "Design a React dashboard for EV battery monitoring"

Skills activated:
├── react-architect (component structure)
├── data-viz-expert (chart selection)
├── tesla-engineer (battery domain knowledge)
└── ux-designer (dashboard patterns)
```

### 4. Quality Over Quantity

Better to have 3 excellent skills than 10 mediocre ones.

A great skill:
- Solves one problem exceptionally well
- Is immediately usable
- Handles edge cases gracefully
- Provides clear examples

---

## Common Misconceptions

### ❌ "Skills are just prompt templates"

**Truth:** Skills are comprehensive packages including:
- System prompts (role definition)
- Domain knowledge (expertise)
- Workflows (processes)
- Scripts (tools)
- References (documentation)
- Examples (demonstrations)

### ❌ "More content = better skill"

**Truth:** Concise, well-organized content is better. Progressive disclosure means:
- SKILL.md: Essential information only
- references/: Detailed content loaded on demand
- Result: Fast, focused interactions

### ❌ "Skills replace thinking"

**Truth:** Skills guide thinking. A "Tesla Engineer" skill doesn't replace engineering judgment—it provides Tesla's specific methodology and constraints for making those judgments.

---

## Next Steps

Now that you understand what skills are:

1. **See it in action:** Read references/onboarding/first-skill.md
2. **Understand the system:** Read references/concepts/why-tiered.md
3. **Create your first:** Follow the 30-second tutorial in SKILL.md

---

**Related:**
- Why 3 Tiers? → references/concepts/why-tiered.md
- Why 6 Dimensions? → references/concepts/why-6-dimensions.md
- First Skill Tutorial → references/onboarding/first-skill.md
