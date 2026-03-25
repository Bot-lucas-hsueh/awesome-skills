# SOP 3: Progressive Disclosure

## Purpose

Structure skill content for optimal token usage: navigation in SKILL.md, details in references/.

## Architecture

```
skill-name/
├── SKILL.md (< 300 lines, navigation)
│   ├── Overview
│   ├── Key frameworks (summarized)
│   └── Links to references/
│
└── references/ (3000+ lines, details)
    ├── Detailed explanations
    ├── Deep dives
    └── Full examples
```

## Navigation Ratio

Target 1:10 ratio:
- SKILL.md: ~300 lines
- references/: ~3000 lines
- Total: ~3300 lines professional content

## What Goes Where

### SKILL.md Content

**Include**:
- One-liner description
- System Prompt §1.1/1.2/1.3 (essential structure)
- Problem signature (when to use)
- Architecture overview
- Tier specifications (summary)
- Mode descriptions
- SOP index
- Risk matrix (summary)
- Workflow phases (summary)
- Example index
- Anti-patterns (summary)

**Exclude**:
- Detailed explanations
- Long examples
- Deep methodology dives
- Full SOP procedures
- Complete risk documentation

### references/ Content

**Create files for**:
- Detailed SOPs
- Full examples (5 scenarios)
- Deep domain knowledge
- Complete risk documentation
- Thinking pattern details
- Quality gate details

## Linking Convention

Use relative links:
```markdown
📄 **Details**: [references/filename.md](references/filename.md)
| Link | [references/filename.md](references/filename.md) |
```

## Verification

```bash
# Line count check
wc -l SKILL.md  # Should be < 300

# Reference link count
grep -c "references/" SKILL.md  # Should be 15+
```
