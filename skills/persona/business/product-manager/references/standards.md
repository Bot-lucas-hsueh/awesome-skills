## § 6 · Standards & Reference

### Product Requirements Document (PRD) Template

```
PRODUCT REQUIREMENTS DOCUMENT
Product: [Name] | Feature: [Name] | Version: [X.Y]
Author: [PM Name] | Date: [YYYY-MM-DD]

1. PROBLEM STATEMENT
   - Current user pain point
   - Impact of not solving
   - Evidence (quotes, data, observations)

2. HYPOTHESIS
   We believe that [solution]
   For [target users]
   Will achieve [outcome]

3. SUCCESS METRICS
   | Metric | Baseline | Target | Measurement |
   |--------|----------|--------|-------------|
   | [Metric 1] | [X] | [Y] | [Method] |

4. TARGET USERS
   - Primary persona: [Description]
   - JTBD: When I [situation], I want to [motivation], so I can [expected outcome]

5. USER STORIES
   As a [user], I want [goal], so that [benefit]
   Acceptance Criteria:
   - Given [context], when [action], then [result]

6. FUNCTIONAL REQUIREMENTS
   | ID | Requirement | Priority |
   |----|-------------|----------|
   | FR-001 | [Description] | P0/P1/P2 |

7. NON-FUNCTIONAL REQUIREMENTS
   - Performance: [Criteria]
   - Security: [Criteria]
   - Scalability: [Criteria]

8. OUT OF SCOPE
   - Explicit exclusions
   - Future phase items

9. RISK ANALYSIS
   | Risk | Mitigation |
   |------|------------|

10. RELEASE CRITERIA
    - [ ] All P0 bugs resolved
    - [ ] Performance targets met
    - [ ] Documentation complete
```

### Product Roadmap Template

```
PRODUCT ROADMAP — [Product Name]
Horizon: 4 quarters | Last Updated: [Date]

THEME-BASED ROADMAP:

NOW (Current Quarter)
Theme: [Strategic focus, e.g., "Activation Improvement"]
| Feature | Goal | Owner | Status |
|---------|------|-------|--------|
| [Feature 1] | [Metric impact] | [Name] | In Progress |
| [Feature 2] | [Metric impact] | [Name] | In Progress |

NEXT (Next Quarter)
Theme: [Strategic focus]
| Feature | Goal | Confidence |
|---------|------|------------|
| [Feature 3] | [Metric impact] | High/Med/Low |

LATER (2-4 Quarters)
Theme: [Strategic focus]
| Feature | Hypothesis |
|---------|------------|
| [Feature 4] | [Learning goal] |

DEPENDENCIES:
- [Dependency 1]: [Impact, mitigation]

KEY METRICS:
- North Star: [Metric]
- Current: [Value] | Target: [Value]
```

### User Persona Template

```
USER PERSONA — [Persona Name]

Demographics:
- Role: [Job title]
- Company: [Size, industry]
- Experience: [Years in role]
- Tools: [Current tools used]

Quote:
"[Direct quote capturing their motivation]"

Jobs-to-be-Done:
When I [situation/context],
I want to [motivation/goal],
So I can [expected outcome]

Pain Points:
1. [Specific frustration with current solution]
2. [Specific frustration with current solution]
3. [Specific frustration with current solution]

Current Behavior:
- How they currently solve the problem
- Workarounds and hacks they use
- Frequency and context of the job

Success Looks Like:
- [Desired outcome 1]
- [Desired outcome 2]

Segment Size:
- % of user base: [X%]
- Strategic importance: [High/Med/Low]
```

### Experiment Log Template

```
EXPERIMENT — [Experiment Name]
Status: [Planned/Running/Complete]

Hypothesis:
We believe that [change]
Will result in [outcome]
As measured by [metric]

Experiment Design:
- Type: [A/B test, prototype test, etc.]
- Duration: [X days/weeks]
- Sample size: [N users]
- Confidence level: [95%]

Variants:
| Variant | Description | Allocation |
|---------|-------------|------------|
| Control | [Current state] | 50% |
| Treatment | [New version] | 50% |

Success Criteria:
- Win: [Metric] improves by [X%] with statistical significance
- Lose: [Metric] decreases or no significant change
- Inconclusive: Insufficient data or conflicting signals

Results:
| Metric | Control | Treatment | Delta | Significant? |
|--------|---------|-----------|-------|--------------|
| [Metric 1] | [X] | [Y] | [Z%] | Yes/No |

Learnings:
- [Key insight 1]
- [Key insight 2]

Decision: [Ship/Learn more/Abandon]
```

---
