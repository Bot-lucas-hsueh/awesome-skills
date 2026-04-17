## § 7 · Standards & Reference

### 7.1 Branch Naming Convention

| Type| Pattern| Example|
|-----|---------|---------|
| Feature | `feature/[skill-name]` | `feature/aws-cloud-expert` |
| Fix | `fix/[skill-name]-[issue]` | `fix/ceo-score-fix-42` |
| Docs | `docs/[topic]` | `docs/workflow-update` |
| Upgrade | `upgrade/[skill-name]` | `upgrade/backend-developer-to-exemplary` |

### 7.2 Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

| Type| Scope| Subject|
|-----|------|--------|
| `feat` | skill name | Brief description |
| `fix` | skill name | What was fixed |
| `docs` | - | Documentation changes |
| `refactor` | skill name | Structure change |
| `quality` | skill name | Score improvement |

**Example:**
```
feat(aws-cloud-expert): add EC2 spot instance decision framework

- Implements §7.1 decision matrix for spot vs on-demand
- Adds §9.2 cost optimization scenario
- Score: 9.2/10

Closes #123
```

### 7.3 PR Description Template

```markdown
## Summary

## Quality Checklist
- [ ] 16 sections present in order
- [ ] YAML valid (yamllint passed)
- [ ] Score calculated: __/10
- [ ] Test cases added
- [ ] References verified

## Changes

## Testing

```

### 7.4 Quality Gate Thresholds

| Gate| Threshold| Action|
|-----|----------|-------|
| Sections | 16 present, ordered | Block if missing |
| YAML | Valid syntax | Block if invalid |
| Score | ≥9.0 for Exemplary | Block if below |
| Score | ≥7.0 for Expert | Block if below |
| Lines | ≤500 SKILL.md | Warn if exceeded |
| Links | All valid | Block if broken |

---
