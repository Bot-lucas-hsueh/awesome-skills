## § 6 · Standards & Reference

### Business Requirements Document (BRD) Template

```
BUSINESS REQUIREMENTS DOCUMENT
Project: [Name] | Version: [X.Y] | Date: [YYYY-MM-DD]
Author: [BA Name] | Approver: [Sponsor]

1. EXECUTIVE SUMMARY
   - Business opportunity
   - Expected benefits
   - Investment required
   - Success metrics

2. BUSINESS OBJECTIVES
   | Objective | Target | Measurement |
   |-----------|--------|-------------|
   | [Obj 1]   | [X]    | [Metric]    |

3. STAKEHOLDERS
   | Role | Name | Responsibility | Influence |
   |------|------|----------------|-----------|
   | Sponsor | [Name] | Accountable | High |

4. CURRENT STATE (AS-IS)
   - Process overview
   - Pain points
   - Metrics baseline

5. FUTURE STATE (TO-BE)
   - Process description
   - Key changes
   - Expected outcomes

6. FUNCTIONAL REQUIREMENTS
   | ID | Requirement | Priority | Acceptance Criteria |
   |----|-------------|----------|---------------------|
   | FR-001 | [Description] | Must Have | [Criteria] |

7. NON-FUNCTIONAL REQUIREMENTS
   - Performance: [e.g., <2s response time]
   - Security: [e.g., SSO, encryption]
   - Availability: [e.g., 99.9% uptime]
   - Scalability: [e.g., 10x growth capacity]

8. CONSTRAINTS & ASSUMPTIONS
   - Budget: $[X]
   - Timeline: [Y months]
   - Technical constraints

9. RISK ANALYSIS
   | Risk | Probability | Impact | Mitigation |
   |------|-------------|--------|------------|

10. APPENDICES
    - Glossary
    - Process models
    - Data models
```

### User Story Template

```
USER STORY

Story ID: US-[XXX]
Title: [Clear, active verb phrase]
Epic: [Parent epic]
Sprint: [Sprint number]

User Story:
As a [user type]
I want [functionality]
So that [business value/value proposition]

Acceptance Criteria:
1. Given [context], when [action], then [expected result]
2. Given [context], when [action], then [expected result]
3. Given [context], when [action], then [expected result]

Definition of Done:
- [ ] Code developed and reviewed
- [ ] Unit tests passing (>80% coverage)
- [ ] Acceptance criteria validated
- [ ] Documentation updated
- [ ] PO sign-off

Additional Notes:
- UI mockup: [Link]
- Data requirements: [Description]
- Dependencies: [List]

Estimation: [Story points]
Priority: [Must/Should/Could/Won't]
```

### BPMN Process Model Standards

```
PROCESS MODEL: [Process Name]
Version: [X.Y] | Date: [YYYY-MM-DD] | Author: [Name]

Pool/Lane Structure:
- Pool: [Organization/Process boundary]
  - Lane: [Role 1]
  - Lane: [Role 2]
  - Lane: [System/Automated]

Element Usage:
- Start Event: Circle (green)
- End Event: Circle (red)
- Task: Rectangle (activity)
- Gateway: Diamond (decision/merge)
- Sequence Flow: Arrow (solid)
- Message Flow: Arrow (dashed)

Annotations:
- Each task: [Task name, avg duration, system used]
- Each gateway: [Decision criteria]
- Data objects: [Inputs/outputs]

Metrics Captured:
- Cycle time: [X minutes/hours/days]
- Touch time: [Y minutes/hours]
- Wait time: [Z minutes/hours]
- Error rate: [W%]
```

### Stakeholder Analysis Matrix

```
STAKEHOLDER ANALYSIS

| Stakeholder | Role | Power | Interest | Engagement Strategy | Communication |
|-------------|------|-------|----------|---------------------|---------------|
| [Name/Role] | [Sponsor] | High | High | Manage closely | Weekly 1:1 |
| [Name/Role] | [End User] | Low | High | Keep informed | Bi-weekly demo |
| [Name/Role] | [IT Lead] | High | Medium | Keep satisfied | Monthly review |
| [Name/Role] | [Finance] | Medium | Low | Monitor | Monthly report |

RACI Matrix:
| Activity | Sponsor | BA | PM | Dev Lead | End Users |
|----------|---------|-----|-----|----------|-----------|
| Requirements | A | R | C | C | I |
| Design | I | C | C | R | C |
| Testing | A | R | C | C | R |
| Deployment | A | C | R | C | I |

Legend: R=Responsible, A=Accountable, C=Consulted, I=Informed
```

---
