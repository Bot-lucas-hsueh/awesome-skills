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
2. Follow the [Skill Development Guide](#skill-development-guide)
3. Submit a Pull Request

### 2. Improve Existing Skills

Help fix bugs, typos, or outdated information:
- Correcting factual errors
- Updating outdated information
- Adding missing best practices
- Improving clarity and readability

### 3. Report Issues

Open an issue with a clear title, detailed description, and suggested solution.

## Skill Development Guide

### Directory Structure

Skills are organised by **kind** first, then by domain:

```
skills/
├── persona/              ← Role-based professional personas
│   └── [domain]/
│       └── [skill-name]/
│           ├── SKILL.md           # Main skill file (required)
│           └── references/        # Deep-dive reference docs (optional)
│
├── tool/                 ← Technology-specific expert skills
│   └── [technology-area]/
│       └── [skill-name]/
│           └── SKILL.md
│
└── workflow/             ← Process-driven action skills
    └── [workflow-area]/
        └── [skill-name]/
            └── SKILL.md
```

**Which `kind` should I use?**

| Kind | Use when the skill… | Example |
|------|---------------------|---------|
| `persona` | Gives the agent a professional identity and methodology | `ceo`, `backend-developer` |
| `tool` | Teaches expert operation of a specific technology | `kubernetes-expert`, `aws-expert` |
| `workflow` | Defines a step-by-step process the agent executes | `tdd-workflow`, `debug-diagnose` |

### YAML Frontmatter

```yaml
---
name: skill-name           # Required. Must match directory name. Lowercase, hyphens only.
kind: persona              # Required. One of: persona | tool | workflow | template | composite
version: 1.0.0             # Required. SemVer.
description: >             # Required. Max 400 chars. State capability + "Use when: ..." triggers.
  A world-class expert in [domain]. Use when [triggers].
license: MIT
tags:
  - domain: [domain]
  - subtype: [skill-name]
  - level: expert
---
```

**Key rules for `name`:**
- Lowercase letters, numbers, and hyphens only
- Must match the parent directory name
- No consecutive hyphens (`--`), no leading/trailing hyphens

**`description` is the most important field.** It is the agent's only signal for deciding whether to load this skill. A vague description means the skill never loads. Use the `write-skill` workflow skill for guidance:

```
Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/workflow/meta/write-skill/SKILL.md and install write-skill
```

### Quality Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Accuracy** | Content is factually correct |
| **Description** | Specific triggers using "Use when:" language |
| **Clarity** | Easy to understand; tables over prose |
| **Practicality** | Actionable advice with frameworks and examples |
| **Safety** | Domain-specific risk warnings where appropriate |

## Pull Request Process

### 1. Fork and Branch

```bash
git clone https://github.com/YOUR-USERNAME/awesome-skills.git
cd awesome-skills
git checkout -b add-skill-name
```

### 2. Add Your Skill

```bash
# For a persona skill:
mkdir -p skills/persona/[domain]/[skill-name]
# Edit skills/persona/[domain]/[skill-name]/SKILL.md

# For a tool skill:
mkdir -p skills/tool/[technology]/[skill-name]
# Edit skills/tool/[technology]/[skill-name]/SKILL.md

# For a workflow skill:
mkdir -p skills/workflow/[area]/[skill-name]
# Edit skills/workflow/[area]/[skill-name]/SKILL.md
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
python3 .github/scripts/validate_skills.py skills/persona/software/backend-developer/SKILL.md

# Strict mode (16 sections required for Expert Verified skills)
python3 .github/scripts/validate_skills.py --strict skills/persona/executive/
```

### What the Validator Checks

| Check | Required For | Blocks Merge |
|-------|-------------|-------------|
| YAML frontmatter present | All skills | Yes |
| Required fields: `name`, `version`, `description` | All skills | Yes |
| `name` matches directory name | All skills | Yes |
| `kind` is a valid enum value | All skills | Yes |

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
