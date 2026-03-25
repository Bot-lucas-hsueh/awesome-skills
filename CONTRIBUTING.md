# Contributing to Awesome Skills

Thank you for considering contributing to Awesome Skills!

## Quick Links

- [Skill Development Guide](#skill-development-guide)
- [Pull Request Process](#pull-request-process)
- [Validation & CI](#validation--ci)
- [Style Guidelines](#style-guidelines)

## How to Contribute

### 1. Submit a New Skill

Create a new skill for a domain not yet covered:

1. Check existing skills to avoid duplication
2. Use the [TEMPLATE.md](./skills/meta/skill-writer/assets/TEMPLATE.md)
3. Follow the [Skill Development Guide](#skill-development-guide)
4. Submit a Pull Request

### 2. Improve Existing Skills

Help fix bugs, typos, or outdated information:
- Correcting factual errors
- Updating outdated information
- Adding missing best practices
- Improving clarity and readability

### 3. Report Issues

Open an issue with a clear title, detailed description, and suggested solution.

## Skill Development Guide

### Skill Structure

```
skills/
└── [category]/
    └── [skill-name]/
        ├── SKILL.md           # Main skill file
        └── references/        # Reference docs (optional)
            ├── frameworks.md
            ├── workflows.md
            └── examples.md
```

### Required Sections

Every skill must include all 16 standard H2 sections in the correct order. See [TEMPLATE.md](./skills/meta/skill-writer/assets/TEMPLATE.md).

### YAML Frontmatter

Skills follow the [agentskills open format specification](https://github.com/agentskills/agentskills):

```yaml
---
name: skill-name           # Required. Must match directory name. Lowercase, hyphens only.
description: >             # Required. Max 1024 chars. What it does and when to use it.
  A world-class expert in [domain]. Use when [triggers].
license: MIT               # Optional.
compatibility: ...         # Optional. Environment requirements.
metadata:                  # Optional. Arbitrary key-value pairs.
  author: neo.ai
  version: 1.0.0
  tags: tag1, tag2, tag3
  category: category-name
  difficulty: expert|intermediate|beginner
  quality: exemplary
---
```

**Key rules for `name`:**
- Lowercase letters, numbers, and hyphens only
- Must match the parent directory name
- No consecutive hyphens (`--`), no leading/trailing hyphens

### Quality Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Accuracy** | Content is factually correct |
| **Completeness** | All 16 H2 sections in correct order |
| **Clarity** | Easy to understand; tables over prose |
| **Practicality** | Actionable advice with frameworks and examples |
| **Safety** | Domain-specific risk warnings with severity ratings |

## Pull Request Process

### 1. Fork and Branch

```bash
git clone https://github.com/YOUR-USERNAME/awesome-skills.git
cd awesome-skills
git checkout -b add-skill-name
```

### 2. Add Your Skill

```bash
mkdir -p skills/[category]/[skill-name]
# Edit skills/[category]/[skill-name]/SKILL.md
```

### 3. Test Your Skill

- [ ] Read through the entire skill
- [ ] Check for typos and formatting issues
- [ ] Verify all links work
- [ ] Run validator: `python3 .github/scripts/validate_skills.py <file>`

### 4. Submit PR

```bash
git add .
git commit -m "feat: add [skill-name] skill"
git push origin add-skill-name
```

## Validation & CI

### Run Validator Locally

```bash
# Validate all skill files
python3 .github/scripts/validate_skills.py skills/

# Validate a single file
python3 .github/scripts/validate_skills.py skills/software/backend-developer/SKILL.md

# Strict mode (16 sections required)
python3 .github/scripts/validate_skills.py --strict skills/executive/
```

### What the Validator Checks

| Check | Required For | Blocks Merge |
|-------|-------------|-------------|
| YAML frontmatter present | All skills | Yes |
| Required fields: `name`, `description` | All skills | Yes |
| `name` matches directory name | All skills | Yes |
| ≥16 H2 sections | Expert skills (strict mode) | Yes |

## Style Guidelines

- **Be concise**: Clear and to the point
- **Be specific**: Concrete examples over abstract concepts
- **Be actionable**: Tell users exactly what to do
- **Be consistent**: Follow established patterns

## Questions?

- **General**: [GitHub Discussions](https://github.com/theneoai/awesome-skills/discussions)
- **Bug reports**: [GitHub Issues](https://github.com/theneoai/awesome-skills/issues)
- **Skill ideas**: [GitHub Discussions](https://github.com/theneoai/awesome-skills/discussions) with "Idea" label

---

Thank you for contributing to Awesome Skills!
