# SOP 4: Live Operations Crisis Response

## Purpose

Respond to live issues quickly while maintaining player trust.

## Input

Live issue detected (crash, exploit, revenue drop)

## Output

Resolved issue, player trust maintained

## Process

### Severity Assessment (5 minutes)

**P0 (Critical)**:
- Game unplayable
- Data loss
- Security breach
- Major exploit affecting economy

**Response**: All hands, immediate action

**P1 (High)**:
- Major feature broken
- Significant player impact
- Revenue impact

**Response**: Dedicated team, fix within hours

**P2 (Medium)**:
- Minor issues
- Workarounds exist

**Response**: Scheduled fix, next deployment

**P3 (Low)**:
- Cosmetic issues
- No player impact

**Response**: Backlog for next sprint

### P0 Response Workflow

| Time | Action | Owner |
|------|--------|-------|
| T+0 min | Issue detected via monitoring | On-call engineer |
| T+5 min | Page on-call engineer | Automated |
| T+10 min | Assess scope and impact | Game Lead + Engineer |
| T+15 min | Decision: Disable feature or emergency fix | Game Lead |
| T+30 min | Player communication (in-game, social) | Community Manager |
| T+1 hour | Hotfix deployed OR feature disabled | Engineering |
| T+2 hours | Verify fix effectiveness | QA + Engineering |
| T+4 hours | Post-mortem scheduled | Game Lead |

### Communication Templates

**In-Game Message**:
```
"We're aware of [issue] and working on a fix. 
Thank you for your patience."
```

**Social Media**:
```
"We've identified an issue with [feature]. 
We're working on a fix and will update you within [timeframe]. 
Thank you for your patience."
```

**Support Scripts**:
```
"We're aware of the [issue] and working on a fix. 
Expected resolution: [timeframe]. 
We'll update you when it's resolved."
```

**Internal Updates**:
- Regular updates to company Slack
- Status page updates
- Leadership briefings

### Post-Incident Process

**Root Cause Analysis** (within 24 hours):
- What happened?
- Why did it happen?
- How did we detect it?
- How could we have prevented it?

**Fix Verification**:
- Test fix thoroughly
- Monitor for recurrence
- Verify no side effects

**Player Compensation** (if warranted):
- Assess impact on players
- Determine appropriate compensation
- Deliver quickly

**Process Improvements**:
- What can we do better next time?
- Monitoring improvements?
- Process changes?

**Retrospective with Cell**:
- What went well?
- What could improve?
- Action items?

## Deliverables

- Incident report
- Root cause analysis
- Preventive measures
- Communication logs
- Post-mortem document
