# Risk Documentation

## Common Creation Pitfalls

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Wrong Tier Selection** | Medium | High | Use tier selection matrix |
| **Missing System Prompt** | High | High | Check §1.1/1.2/1.3 checklist |
| **Generic Content** | High | High | Data validation checklist |
| **Flat Structure** | Medium | Medium | Enforce progressive disclosure |
| **Insufficient Examples** | Medium | Medium | Require 5+ scenarios |
| **No Done/Fail Criteria** | Medium | High | Add to all workflow phases |
| **Scope Creep** | Medium | Medium | Define boundaries upfront |

## Quality Checkpoints

### Checkpoint 1: Before Writing

- [ ] Tier selected based on scope
- [ ] System Prompt architecture designed
- [ ] 5 examples planned
- [ ] Progressive disclosure mapped

### Checkpoint 2: During Writing

- [ ] §1.1/1.2/1.3 complete
- [ ] No generic terms remaining
- [ ] Specific data verified
- [ ] Progressive disclosure correct

### Checkpoint 3: Before Delivery

- [ ] Evaluator score ≥ 9.0
- [ ] All thresholds met
- [ ] Variance < 1.0
- [ ] EVALUATION_REPORT.md saved

## Crisis Playbooks

### Generic Content Detected

**Symptoms**: "professional", "expert", "best practices" found

**Response**:
1. Identify all generic terms (grep)
2. Research specific replacements
3. Update with real data
4. Re-validate

### Missing System Prompt Sections

**Symptoms**: Score < 7.0, missing §1.1/1.2/1.3

**Response**:
1. Add §1.1 Identity & Worldview
2. Add §1.2 Decision Framework
3. Add §1.3 Thinking Patterns
4. Re-score

### Score Below Target

**Symptoms**: Evaluator score < 9.0

**Response**:
1. Check System Prompt completeness
2. Verify domain data specificity
3. Add more detailed examples
4. Strengthen Done/Fail criteria
5. Re-run evaluator
