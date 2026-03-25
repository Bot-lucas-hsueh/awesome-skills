# Skill Quality Standards

> Minimum requirements and best practices for all tiers

---

## Universal Requirements

Every skill must have:

### 1. Complete Metadata
```yaml
---
name: [specific-name]
description: "[Clear description]. Use when: [triggers]."
version: x.y.z
---
```

### 2. System Prompt
Clear definition of:
- Role
- Capabilities
- Boundaries

### 3. Usage Instructions
How to use the skill

### 4. Examples
At least one working example

---

## Tier-Specific Standards

### Lite Standards (50-150 lines)

| Aspect | Minimum |
|--------|---------|
| Lines | 50-150 |
| Capabilities | 1-2 |
| Examples | 1-2 |
| Error handling | Basic |
| References | Optional |
| Target score | 6.0+ |

**Quality Check:**
- [ ] Single clear capability
- [ ] Concise documentation
- [ ] Basic error handling
- [ ] Working example

---

### Standard Standards (150-500 lines)

| Aspect | Minimum |
|--------|---------|
| Lines | 150-500 |
| Capabilities | 2-5 |
| Examples | 3-5 |
| Error handling | Comprehensive |
| References | Required |
| Target score | 7.0+ |

**Quality Check:**
- [ ] Multiple related capabilities
- [ ] Deep domain knowledge
- [ ] Clear workflow
- [ ] Comprehensive error handling
- [ ] Diverse examples
- [ ] references/ directory

---

### Enterprise Standards (500-1500 lines)

| Aspect | Minimum |
|--------|---------|
| Lines | 500-1500 |
| Capabilities | 5+ |
| Examples | 5+ |
| Error handling | Exhaustive |
| References | Extensive |
| Target score | 8.0+ |

**Quality Check:**
- [ ] Complete methodology
- [ ] Multiple domains
- [ ] Safety/compliance (if applicable)
- [ ] Case studies
- [ ] Comprehensive references
- [ ] All 6 dimensions ≥ 8.0

---

## Progressive Disclosure Standards

### SKILL.md
- Maximum 300 lines
- Essential information only
- Clear reference triggers

### references/
- 2-10 files typical
- 100-500 lines per file
- Logical organization

### Loading Strategy
- Default: SKILL.md only
- On demand: Specific references based on need
- Never: Load everything upfront

---

## Documentation Standards

### Writing Style
- Clear and concise
- Active voice
- Specific examples
- No ambiguity

### Format
- Consistent markdown
- Proper headings
- Tables for structured data
- Code blocks for examples

### Completeness
- All capabilities documented
- All error cases handled
- All examples tested

---

## Review Checklist

Before releasing a skill, verify:

### Content
- [ ] Metadata complete
- [ ] System prompt clear
- [ ] Capabilities defined
- [ ] Workflow documented
- [ ] Error handling included
- [ ] Examples provided

### Quality
- [ ] All 6 dimensions scored
- [ ] Meets tier target score
- [ ] No anti-patterns
- [ ] Progressive disclosure followed

### Testing
- [ ] Examples work
- [ ] Error handling tested
- [ ] Edge cases covered
- [ ] Real inputs validated

---

**Related:**
- Quality Rubric → ./scoring/rubric.md
- Anti-Patterns → ./anti-patterns.md
