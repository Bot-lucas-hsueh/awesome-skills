# Skill-Writer User Guide

> Complete guide to using Skill-Writer v5

**Version:** 5.0.2  
*Author: neo.ai | Contact: lucas_hsueh@hotmail.com | License: MIT*

---

## Quick Reference

```
Create a skill → "write skill", "create skill", "start [level]"
Review a skill → "review this skill", "score my skill"
Upgrade a skill → "upgrade to [tier]", "make this enterprise"
```

---

## Getting Started

### For Complete Beginners

**Start here:** Type `start beginner`

You'll get:
- 30-minute guided tutorial
- Your first working skill
- Understanding of core concepts

**What you'll create:** A PDF rotator skill (Lite tier)

**Prerequisites:** None

---

### For Experienced Users

**Quick prototype:** Type `start quick`

You'll get:
- 15-minute minimal skill
- Working code immediately
- Good enough for personal use

**Production skill:** Type `start standard`

You'll get:
- 1-2 hour comprehensive process
- Team-ready quality
- Full documentation

---

## Core Concepts

### What is a Skill?

A skill is a specialized training manual for AI. It transforms a general-purpose AI into a domain expert.

**Analogy:**
- Without skill = General education graduate
- With skill = Domain expert (Tesla engineer, React architect, etc.)

**Example:**
```
Without Tesla skill: "Here are some general engineering principles..."
With Tesla skill: "Per Tesla first-principles methodology, we start with..."
```

---

## The Three Tiers

### Lite (50-150 lines)

**Use for:** Single-function tools

**Examples:**
- PDF rotator
- URL shortener
- Date formatter

**Characteristics:**
- One specific capability
- Clear input/output
- No references/ directory needed

**Time:** 15-30 minutes

---

### Standard (150-500 lines)

**Use for:** Domain knowledge bases

**Examples:**
- React architecture guide
- Data analysis assistant
- Marketing copywriter

**Characteristics:**
- 2-5 related capabilities
- Domain expertise required
- references/ directory for details

**Time:** 1-2 hours

---

### Enterprise (500-1500 lines)

**Use for:** Complete methodologies

**Examples:**
- Tesla engineering methodology
- Medical diagnosis protocols
- Enterprise security framework

**Characteristics:**
- Complete system
- Multiple domains
- Safety/compliance requirements

**Time:** 1-2 days

---

## Flexibility Levels

### Quick Mode (15 minutes)

**Use when:**
- Personal use only
- Prototype/validation
- Time constrained

**Process:**
1. Define capability (2 min)
2. Create SKILL.md (10 min)
3. Quick check (3 min)

**Quality target:** 6.0+

---

### Standard Mode (1-2 hours)

**Use when:**
- Team sharing
- Production use
- Quality matters

**Process:**
1. Discovery (15 min)
2. Design (15 min)
3. Development (30 min)
4. Validation (30 min)
5. Refinement (30 min)

**Quality target:** 8.0+

---

### Strict Mode (1+ days)

**Use when:**
- Public release
- Safety-critical
- High consequence

**Process:**
1. Requirements (2 hrs)
2. Design review (2 hrs)
3. Development (4 hrs)
4. Testing (4 hrs)
5. Review (2 hrs)
6. Certification (2 hrs)

**Quality target:** 9.0+

---

## Design Patterns

### Tool Wrapper

**Use when:** Wrapping a tool/library

**Structure:** Setup → Usage → Examples

**Example:** PDF processor, API client

---

### Generator

**Use when:** Creating specific outputs

**Structure:** Template → Variables → Output

**Example:** Report generator, email writer

---

### Reviewer

**Use when:** Evaluating existing content

**Structure:** Criteria → Assessment → Feedback

**Example:** Code reviewer, document editor

---

### Pipeline

**Use when:** Multi-step process

**Structure:** Input → Step 1 → Step 2 → Output

**Example:** Data processing, approval workflow

---

### Inversion

**Use when:** Need info before helping

**Structure:** Collection → Analysis → Execution

**Example:** Consultant, diagnostic tool

---

## Quality Standards

### The 6 Dimensions

Every skill is scored on:

1. **System Prompt** - Clear role and boundaries?
2. **Domain Knowledge** - Accurate and deep?
3. **Workflow** - Clear process?
4. **Error Handling** - Edge cases covered?
5. **Examples** - Good demonstrations?
6. **Metadata** - Complete and specific?

### Scoring Scale

| Score | Meaning |
|-------|---------|
| 1-3 | Critical issues |
| 4-5 | Below acceptable |
| 6-6.5 | Minimum viable |
| 7-8 | Good quality |
| 9-10 | Excellent |

### Tier Targets

| Tier | Minimum | Target |
|------|---------|--------|
| Lite | 6.0 | 7.0+ |
| Standard | 7.0 | 8.0+ |
| Enterprise | 8.0 | 9.0+ |

---

## Common Workflows

### Creating Your First Skill

```
1. Type: "start beginner"
2. Follow the tutorial
3. Create PDF rotator skill
4. Test it works
5. Done! (30 minutes)
```

---

### Reviewing a Skill

```
1. Type: "review this skill"
2. Paste your SKILL.md
3. Get 6-dimension scores
4. Receive improvement suggestions
5. Apply fixes
```

---

### Upgrading a Skill

```
1. Type: "upgrade to standard"
2. Current skill is assessed
3. Target template is loaded
4. Upgrade steps are guided
5. New tier achieved
```

---

## Anti-Patterns to Avoid

### ❌ Don't Create README.md
Skills don't need separate README files. SKILL.md is the documentation.

### ❌ Don't Over-Document
Keep SKILL.md under 300 lines. Details go in references/.

### ❌ Don't Under-Document
Include clear system prompt, capabilities, workflow, examples.

### ❌ Don't Use Vague Triggers
Bad: "Helps with stuff"  
Good: "PDF rotation tool. Use when: changing PDF orientation"

### ❌ Don't Skip Error Handling
Always anticipate and document error cases.

### ❌ Don't Pick Wrong Tier
PDF rotator → Lite (not Enterprise)  
Tesla methodology → Enterprise (not Lite)

---

## Resource Reference

### Getting Started
| Need | Resource |
|------|----------|
| First skill | references/onboarding/first-skill.md |
| Quick start | references/onboarding/quickstart.md |
| Progressive disclosure | references/onboarding/progressive-guide.md |

### Core Concepts
| Need | Resource |
|------|----------|
| What is skill? | references/concepts/what-is-skill.md |
| Why 3 tiers? | references/concepts/why-tiered.md |
| Why 6 dimensions? | references/concepts/why-6-dimensions.md |

### Workflows
| Need | Resource |
|------|----------|
| Lite workflow | references/workflow/lite-workflow.md |
| Standard workflow | references/workflow/standard-workflow.md |
| Enterprise workflow | references/workflow/enterprise-workflow.md |
| Quick mode | references/workflow/quick-mode.md |
| Strict mode | references/workflow/strict-mode.md |

### Patterns & Quality
| Need | Resource |
|------|----------|
| Design patterns | references/patterns/design-patterns.md |
| Pattern selector | references/patterns/pattern-selector.md |
| Quality rubric | references/scoring/rubric.md |

### Templates
| Need | Resource |
|------|----------|
| Lite template | references/templates/TEMPLATE-lite.md |
| Standard template | references/templates/TEMPLATE-standard.md |
| Enterprise template | references/templates/TEMPLATE-enterprise.md |

---

## Troubleshooting

### "I don't know where to start"
→ Type: `start beginner`

### "I need a skill quickly"
→ Type: `start quick`

### "What tier should I use?"
→ One function = Lite, Multiple = Standard, System = Enterprise

### "How do I know if my skill is good?"
→ Type: `score my skill` and paste your SKILL.md

### "Can I upgrade later?"
→ Yes! Skills can evolve: Lite → Standard → Enterprise

---

## Best Practices

### Do's ✅
- Start simple, upgrade later
- Use specific trigger phrases
- Include concrete examples
- Handle error cases
- Follow progressive disclosure
- Test with real inputs

### Don'ts ❌
- Over-engineer simple tools
- Skip error handling
- Use vague descriptions
- Load all references upfront
- Ignore quality scores
- Rush safety-critical skills

---

## Examples of Great Skills

### Lite Example: PDF Rotator
- 85 lines
- Single function
- Clear examples
- Basic error handling
- Score: 7.5/10

### Standard Example: React Architect
- 220 lines + references
- 4 capabilities
- Deep domain knowledge
- Comprehensive error handling
- Score: 8.2/10

### Enterprise Example: Tesla Engineer
- 400 lines + extensive references
- Complete methodology
- Multiple domains
- Safety requirements
- Score: 9.1/10

---

## FAQ

**Q: How long does it take to create a skill?**  
A: 15 minutes (Quick) to 2 days (Enterprise), depending on complexity.

**Q: Can I upgrade my skill later?**  
A: Yes! Start with Lite, upgrade to Standard or Enterprise as needed.

**Q: What's a good score?**  
A: 7.0+ for team use, 8.0+ for production, 9.0+ for public release.

**Q: Do I need programming skills?**  
A: No for basic skills. Helpful for complex ones.

**Q: Can skills work together?**  
A: Yes! Multiple skills can activate for complex tasks.

---

## Quick Command Cheat Sheet

| Goal | Command |
|------|---------|
| First skill | `start beginner` |
| Quick skill | `start quick` |
| Standard skill | `start standard` |
| Expert mode | `start expert` |
| Review skill | `review this skill` |
| Score skill | `score my skill` |
| Upgrade skill | `upgrade to [tier]` |
| Pattern help | `pattern help` |

---

## Support

**Questions?** Check the resources above.  
**Issues?** Review anti-patterns.md.  
**Improvements?** Follow upgrade workflows.

---

**Guide Version:** 1.0  
**Last Updated:** 2026-03-21
