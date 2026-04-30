## §7 · Example Scenarios

### §7.1 · Project Management: Sprint Planning and Execution

**Context:** Lead a 2-week sprint for a feature delivery team using Jira Software.

**Atlassian Approach:**

**Phase 1: Backlog Refinement (Day -2)**
```yaml
Backlog_Health_Check:
  Ready_Criteria:
    - Clear acceptance criteria
    - Story points estimated
    - Dependencies identified
    - Designs attached
  
  Estimation:
    method: Planning Poker (Story Points: 1,2,3,5,8,13)
    baseline: 1 point = ~1/2 day of work
    velocity: Team averages 40 points/sprint
```

**Phase 2: Sprint Planning (Day 0)**
```markdown
# Sprint 23 Planning

## Sprint Goal
Enable customers to export reports in PDF format

## Capacity
- Team: 5 developers
- Days: 10 (minus 1 day for holiday)
- Total capacity: 45 person-days
- Buffer: 20% (9 days)
- Available: 36 days equivalent

## Committed Stories
| Key | Summary | Points | Owner |
|-----|---------|--------|-------|
| PROJ-145 | PDF export backend API | 8 | Sarah |
| PROJ-146 | PDF template engine | 5 | Mike |
| PROJ-147 | Frontend export button | 3 | Alex |
| PROJ-148 | PDF styling framework | 5 | Sarah |
| PROJ-149 | Export progress indicator | 3 | Mike |
| PROJ-150 | Error handling for exports | 3 | Alex |

**Total: 27 points** (Conservative for first sprint with new tech)
```

**Phase 3: Daily Execution**
```yaml
Daily_Flow:
  Morning:
    - Review Jira board (To Do → In Progress → Review → Done)
    - Update issue status
    - Flag blockers in Slack #dev-updates
    
  Development:
    - Branch naming: PROJ-145-pdf-export-api
    - Commit format: "PROJ-145 Add PDF generation service"
    - PR requires: 2 approvals, green build, no conflicts
    
  Tracking:
    - Burndown chart review in standup
    - Flag issues > 2 days in same status
    - Update remaining estimates daily
```

**Phase 4: Sprint Review**
```markdown
# Sprint 23 Review

## Demo
1. Navigate to Reports page
2. Click "Export as PDF"
3. Show progress indicator
4. Download and display generated PDF

## Feedback Captured
- Customer wants CSV export too (new backlog item)
- PDF formatting needs dark mode support
- Export should include charts

## Metrics
- Committed: 27 points
- Completed: 24 points (89% reliability)
- Escaped defects: 0
- Cycle time avg: 3.2 days
```

**Phase 5: Retrospective**
```markdown
# Retrospective: Sprint 23

## What Went Well 🟢
- PDF generation library worked smoothly
- API design reviews caught issues early
- QA involvement from day 1

## What to Improve 🟡
- Underestimated styling complexity by 2 points
- Need better test data for large reports
- Documentation lagged behind code

## Action Items
1. [ ] Create shared test data fixture (Alex)
2. [ ] Update DoD to include doc update (Team)
3. [ ] Research PDF dark mode options (Sarah)
```

---

### §7.2 · Documentation: Building a Team Knowledge Base

**Context:** Set up comprehensive documentation in Confluence for a microservices platform.

**Atlassian Approach:**

**Phase 1: Information Architecture**
```yaml
Confluence_Space_Structure:
  📁 Platform_Team_Space:
    
    📁 00-Getting-Started:
      - Onboarding Checklist
      - Local Development Setup
      - Team Charter
      
    📁 10-Architecture:
      - System Overview
      - Service Catalog
      - Data Flow Diagrams
      - Decision Records (ADRs)
      
    📁 20-Runbooks:
      - Deployment Procedures
      - Incident Response
      - Rollback Playbooks
      - Common Issues
      
    📁 30-APIs:
      - API Reference (OpenAPI)
      - Authentication Guide
      - Rate Limiting
      - Changelog
      
    📁 40-Operations:
      - Monitoring Dashboards
      - Alert Runbooks
      - Capacity Planning
      - Security Procedures
```

**Phase 2: Template Standardization**
```markdown
# Runbook Template

## Overview
One-sentence description of this procedure.

## Prerequisites
- [ ] Access to X system
- [ ] Required permissions
- [ ] Tools installed

## Procedure
### Step 1: Title
```bash
# Commands with expected output
kubectl get pods -n production
```

### Step 2: Title
Description and verification.

## Rollback
If something goes wrong:
1. Step to revert
2. Verification command

## Related
- Link to related runbook
- Link to monitoring dashboard
- Escalation contact

## Changelog
| Date | Author | Change |
|------|--------|--------|
| 2024-03-15 | J. Doe | Initial version |
```

**Phase 3: Living Documentation Workflow**
```yaml
Doc_as_Code:
  Creation:
    - New feature → Create design doc in Confluence
    - Architecture decision → Create ADR
    - Incident → Create/update runbook
    
  Review:
    - Technical docs: Peer review required
    - Runbooks: Test procedures before publishing
    - APIs: Auto-generate from OpenAPI specs
    
  Maintenance:
    - Quarterly doc health checks
    - Archive outdated pages
    - Update on-call handoff notes weekly
```

---

### §7.3 · CI/CD: Bitbucket Pipelines and Deployment Automation

**Context:** Design a complete CI/CD pipeline for a Node.js microservice deploying to Kubernetes.

**Atlassian Approach:**

**Pipeline Configuration:**
```yaml
# bitbucket-pipelines.yml
image: node:18

definitions:
  caches:
    node: ~/.npm
  
  services:
    docker:
      memory: 2048
  
  steps:
    - &build
      name: Build Application
      caches:
        - node
      script:
        - npm ci
        - npm run build
      artifacts:
        - dist/**
        - node_modules/**
    
    - &test-unit
      name: Unit Tests
      caches:
        - node
      script:
        - npm run test:unit -- --coverage
      artifacts:
        - coverage/**
    
    - &security-scan
      name: Security Scan
      script:
        - pipe: atlassian/snyk-scan:0.5.0
          variables:
            SNYK_TOKEN: $SNYK_TOKEN
            LANGUAGE: "npm"
        - pipe: atlassian/git-secrets-scan:0.5.1
    
    - &docker-build
      name: Build Docker Image
      script:
        - export IMAGE_TAG=$BITBUCKET_COMMIT
        - docker build -t $DOCKER_REGISTRY/service-api:$IMAGE_TAG .
        - docker push $DOCKER_REGISTRY/service-api:$IMAGE_TAG

pipelines:
  default:
    - <<: *build
    - <<: *test-unit
    - <<: *security-scan
    - <<: *docker-build
    - step:
        name: Deploy to Staging
        deployment: staging
        trigger: automatic
        script:
          - kubectl set image deployment/service-api 
              service-api=$DOCKER_REGISTRY/service-api:$BITBUCKET_COMMIT
          - kubectl rollout status deployment/service-api -n staging
  
  branches:
    main:
      - <<: *build
      - <<: *test-unit
      - <<: *security-scan
      - <<: *docker-build
      - step:
          name: Deploy to Production
          deployment: production
          trigger: manual
          script:
            - kubectl set image deployment/service-api 
                service-api=$DOCKER_REGISTRY/service-api:$BITBUCKET_COMMIT
            - kubectl rollout status deployment/service-api -n production
            - |
              curl -X POST $SLACK_WEBHOOK \
                -H 'Content-Type: application/json' \
                -d '{"text":"🚀 service-api deployed to production: '$BITBUCKET_COMMIT'"}'
```

**Change Management Integration:**
```yaml
Jira_Service_Management_Integration:
  Change_Request:
    - Pipeline creates CR for production deploys
    - Approval required from: Tech Lead, Product Owner
    - Risk assessment based on:
      - Files changed (config vs code)
      - Test coverage delta
      - Security scan results
  
  Deployment_Record:
    - Bitbucket deployment linked to Jira issue
    - Release notes auto-generated from commits
    - Rollback procedure attached
```

---

### §7.4 · Incident Management: Post-Mortem and Process Improvement

**Context:** A critical service experienced a 45-minute outage. Lead the post-mortem and process improvement.

**Atlassian Approach:**

**Phase 1: Immediate Response (T+0 to T+45min)**
```yaml
Incident_Response:
  Detection:
    - PagerDuty alert: "API latency > 2s"
    - Jira Service Management incident: INC-4521
  
  Assessment:
    - Severity: SEV-1 (Customer-facing outage)
    - Impact: 15% of requests failing
    - Blast radius: Payment processing service
  
  Mitigation:
    - 08:15 UTC: Rolled back deployment v2.4.1
    - 08:30 UTC: Service recovery confirmed
    - 08:45 UTC: Incident resolved
```

**Phase 2: Post-Mortem Preparation (T+1 to T+24h)**
```markdown
# Post-Mortem: Payment API Outage (INC-4521)

## Summary
On 2024-03-15, the payment processing API experienced a 45-minute outage
due to a database connection pool exhaustion following a deployment.

## Timeline (UTC)
| Time | Event |
|------|-------|
| 07:55 | Deployment v2.4.1 began |
| 08:00 | Deployment completed |
| 08:05 | Latency alerts began firing |
| 08:10 | Error rate exceeded 5% |
| 08:15 | Rollback initiated |
| 08:30 | Service recovery confirmed |
| 08:45 | Incident resolved |

## Root Cause
The new feature in v2.4.1 added a database query in the hot path without
proper connection pool sizing. Each request held connections longer,
exhausting the pool of 20 connections under production load.

## Contributing Factors
1. Load testing didn't simulate realistic concurrent load
2. Database metrics not included in deployment dashboard
3. Connection pool alerts threshold too high

## Impact
- 45 minutes of degraded service
- ~500 failed payment attempts
- No data loss or financial impact
```

**Phase 3: Action Items (Tracked in Jira)**
```yaml
Action_Items:
  Prevent_Recurrence:
    - key: INFRA-892
      summary: Increase DB connection pool to 50
      owner: platform-team
      priority: Critical
      due: 2024-03-18
    
    - key: INFRA-893
      summary: Add connection pool exhaustion alerts
      owner: sre-team
      priority: High
      due: 2024-03-22
    
  Detection:
    - key: MON-445
      summary: Include DB metrics in deploy dashboard
      owner: observability-team
      priority: Medium
      due: 2024-03-29
    
  Process:
    - key: ENG-201
      summary: Update load test scenarios for DB-heavy changes
      owner: qa-team
      priority: High
      due: 2024-03-25
```

---

### §7.5 · Team Collaboration: Async-First Workflow Design

**Context:** Design an async-first collaboration workflow for a distributed team spanning 4 time zones (Sydney, Bangalore, Berlin, San Francisco).

**Atlassian Approach:**

**Phase 1: Team Topology Design**
```yaml
Team_Structure:
  Sydney_Hub:
    timezone: AEST (UTC+10)
    hours: 09:00 - 17:00
    focus: APAC customers, morning handoffs
    
  Bangalore_Hub:
    timezone: IST (UTC+5:30)
    hours: 09:00 - 17:00
    focus: Development, code review
    
  Berlin_Hub:
    timezone: CET (UTC+1)
    hours: 09:00 - 17:00
    focus: EMEA customers, architecture decisions
    
  San_Francisco_Hub:
    timezone: PST (UTC-8)
    hours: 09:00 - 17:00
    focus: Americas customers, product decisions

Overlap_Strategy:
  - Sydney/Bangalore: 4 hours (best for handoffs)
  - Bangalore/Berlin: 3.5 hours
  - Berlin/SF: 0 hours (async only)
```

**Phase 2: Async Communication Protocol**
```markdown
# Team Communication Charter

## Response Time Expectations
| Channel | Urgent | Normal | FYI |
|---------|--------|--------|-----|
| PagerDuty | 15 min | - | - |
| Slack DM | 4 hours | 24 hours | - |
| Slack Channel | - | 24 hours | 48 hours |
| Confluence | - | - | 72 hours |
| Jira Comment | 24 hours | 48 hours | 72 hours |
| Email | 24 hours | 48 hours | - |
| Loom | - | 48 hours | 72 hours |

## Communication Guidelines

### Use Confluence For:
- Decisions that need to persist
- Documentation and runbooks
- Meeting notes and agendas
- Project status and roadmaps

### Use Jira For:
- Work tracking and assignments
- Technical discussions on issues
- Sprint planning and retrospectives
- Bug reports and feature requests

### Use Slack For:
- Quick questions (< 5 min answer)
- Real-time coordination during overlap
- Social connection and team bonding
- Incident response coordination

### Use Loom For:
- Demos and walkthroughs
- Complex explanations
- Weekly async standups
- Code review explanations
```

**Phase 3: Meeting Minimization**
```yaml
Meeting_Policy:
  Required_Synchronous:
    - Sprint Planning (2 hours, bi-weekly)
    - Retrospective (1 hour, bi-weekly)
    - 1:1s (30 min, weekly)
    - Quarterly ITG (Intentional Together Gathering)
  
  Async_Replacements:
    - Daily Standup: Loom updates in #standups
    - Code Review: Bitbucket with detailed comments
    - Design Reviews: Confluence with async feedback
    - Status Updates: Weekly Confluence page

Meeting_Free_Wednesdays:
  purpose: Deep work focus time
  exception: P1 incidents only
  communication: Async only
```

---
