# Common Pitfalls & Anti-Patterns

## 10.1 Statistical Pitfalls

| # | Pitfall | Severity | Prevention |
|---|---------|----------|------------|
| 1 | **P-hacking** | 🔴 High | Pre-register hypotheses |
| 2 | **Cherry-picking results** | 🔴 High | Report all analyses |
| 3 | **Ignoring weighting** | 🔴 High | Apply weights correctly |
| 4 | **Wrong inference** | 🟡 Medium | Understand test assumptions |
| 5 | **Missing context** | 🟡 Medium | Provide full picture |

## 10.2 Documentation Failures

⚠️ **Methodology Issues:**
- No sampling methodology documented
- Missing weighting variables
- Undocumented exclusions
- No variance estimation
- Unclear suppression rules

## 10.3 Communication Errors

⚠️ **Stakeholder Misunderstandings:**
- Presenting estimates without margins of error
- Claiming causation from correlation
- Overstating precision
- Using technical jargon inappropriately

## 10.4 Quality Checklist

- [ ] Sample design documented
- [ ] Weighting methodology explained
- [ ] Variance estimation included
- [ ] Disclosure review completed
- [ ] All results reported (not selective)
- [ ] Limitations acknowledged
- [ ] Code/reproducibility materials
- [ ] Peer review conducted