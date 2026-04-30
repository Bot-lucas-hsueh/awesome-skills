# Scenario Examples

## 9.1 Team Workflows

### Scenario: Sprint Planning

**User:** "How do I run effective sprint planning in Jira?"

**Expert:**
> **Sprint Planning Workflow:**
>
> 1. **Before Meeting:**
>    - Product Owner prioritizes backlog (use ranking)
>    - Run JQL: `project = ENG AND sprint IS EMPTY ORDER BY rank ASC`
>    - Pre-estimate top 20 issues
>
> 2. **During Meeting:**
>    - Pull issues into sprint backlog
>    - Refine acceptance criteria in issue description
>    - Adjust story points via backlog view
>
> 3. **Jira Setup:**
>    ```jql
>    / sprints upcoming
>    / backlog
>    ```
>    Drag issues from backlog to sprint

### Scenario: Bug Triage

**User:** "How should we handle bug triage?"

**Expert:**
> **Bug Triage Process:**
>
> 1. **Incoming Bugs Query:**
>    ```jql
>    project = ENG AND issuetype = Bug AND labels IS EMPTY 
>    ORDER BY created DESC
>    ```
>
> 2. **Triage Actions:**
>    - Set priority (P1-P4)
>    - Add labels: "triaged", "regression", "frontend"
>    - Assign to appropriate team
>    - Link to related issues
>
> 3. **Weekly Triage Meeting:**
>    - Review untriaged bugs (JQL filter)
>    - Update bug dashboard
>    - Review bug escape rate

## 9.2 Automation Scenarios

### JQL Queries for Dashboards

```jql
# Velocity Tracking
project = ENG AND issuetype IN (Story, Bug, Task) 
AND sprint IN closedSprints() 
AND status = Done

# Scope Creep Detection
project = ENG AND sprint IN openSprints() 
AND created > sprintStartDate(sprint)

# Review Cycle Time
project = ENG AND status CHANGED TO "In Review" 
AFTER -7d AND issuetype = Story

# Blocker Aging
project = ENG AND labels = blocked 
AND status != Done 
ORDER BY updated ASC
```

### Automation Rules

**Rule: Epic Progress Sync**
```
Trigger: Subtask status changed
Conditions:
  - Parent issue type = Epic
  - Project = ENG
Actions:
  - Calculate completion percentage
  - Update Epic description with progress
  - Notify epic owner if >50% complete
```

**Rule: Cross-Project Dependencies**
```
Trigger: Issue linked to another project
Condition: Link type = "blocks" OR "is blocked by"
Actions:
  - Sync status changes
  - Notify linked project team
  - Create dependency ticket if missing
```

### Service Desk Workflow

```
Customer Request → Auto-assign → SLA Timer Starts
                        ↓
              [First Response < 4h]
                        ↓
              Technical Assessment
                        ↓
              ┌─────────┴─────────┐
         Resolved         Escalated
              ↓                  ↓
       Closed (8h)       Assigned to Team
              ↓                  ↓
       Customer Survey    In Progress
              ↓                  ↓
         (Feedback)       Resolution
```

## 9.3 DevOps Workflows

### Release Management

```
Version 2.1.0 Release Flow:
├─ Create fix versions: "2.1.0-beta", "2.1.0"
├─ Bulk assign issues to version
│
├─ Pre-release:
│  ├─ Run JQL: `project = ENG AND fixVersion = "2.1.0-beta"`
│  ├─ QA sign-off checklist
│  └─ Deploy to staging
│
├─ Release:
│  ├─ Transition all issues to Done
│  ├─ Bulk edit fixVersion
│  ├─ Create release notes (auto-generate)
│  └─ Deploy to production
│
└─ Post-release:
   ├─ Close sprint
   ├─ Generate release report
   └─ Archive old issues
```

### Deployment Integration

```yaml
# GitHub Actions .github/workflows/jira.yml
name: Jira Integration

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Extract Jira ticket
        run: |
          JIRA_KEY=$(echo "${{ github.head_ref }}" | grep -oE 'ENG-[0-9]+')
          echo "JIRA_KEY=$JIRA_KEY" >> $GITHUB_ENV
      
      - name: Update Jira
        uses: atlassian/gajira-transition@v3
        with:
          transition: "In Review"
          issue: ${{ env.JIRA_KEY }}
```

### Environment Promotion

```
Dev Branch → PR Created → Jira: "In Review"
                                    ↓
PR Approved → Merge → Auto-transition to "Ready for Deploy"
                                    ↓
Deploy Staging → Jira: "Staging Testing"
                                    ↓
Smoke Tests Pass → Manual Approval
                                    ↓
Deploy Production → Jira: "Done"
```

### Incident Response

```
P1 Incident Workflow:
1. Create incident issue (issuetype = Incident)
2. Set priority: Critical (P1)
3. Link to affected Jira projects
4. Assign to incident commander
5. Create dedicated Slack channel: #incident-YYYY-MM-DD
6. Update issue hourly until resolved
7. Post-mortem within 48h
8. Create action items from post-mortem
```
