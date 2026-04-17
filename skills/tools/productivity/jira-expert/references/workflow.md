# Standard Workflow

## 8.1 Agile Project Management Workflow

```
Sprint Lifecycle
├── Sprint Planning
│   ├── Select issues from backlog (JQL: project = ENG AND sprint IS EMPTY)
│   ├── Estimate story points
│   ├── Confirm sprint commitment
│   └── Set sprint goal
│
├── Daily Standups
│   ├── Update issue status on board
│   ├── Log blockers as labels: "blocked"
│   └── Update time tracking
│
├── Sprint Execution
│   ├── Move issues: To Do → In Progress → In Review → Done
│   ├── Link PRs using DevPanel
│   ├── Update sprint progress via board
│   └── Track velocity
│
└── Sprint Review
    ├── Demo completed features
    ├── Retrospective (team health metrics)
    ├── Update issue statuses
    └── Velocity calculation
```

## 8.2 Integration Workflow

### GitHub Integration

```
1. Install Jira GitHub app in organization
2. Connect Jira project to GitHub organization
3. Authorize repositories
4. Development panel shows PRs automatically

Branch Naming Convention:
- feature/ENG-123-add-auth
- bugfix/ENG-456-fix-login
- release/v2.1.0

Commit Messages:
- ENG-123: Add OAuth2 authentication
- [ENG-123] Fix session timeout
```

### CI/CD Pipeline Integration

```yaml
# .jira-workflow.yml
workflow:
  transitions:
    - name: Deploy to Staging
      trigger: pipeline.success
      environment: staging
      jira-transition: "In Review"
    
    - name: Deploy to Production  
      trigger: approval.manual
      environment: production
      jira-transition: "Done"
```

### Slack Integration

```
/jira search "project = ENG AND assignee = @me"
/jira create "Add user authentication module"
/jira assign ENG-123 @alice
/jira transition ENG-123 "In Review"
```

## 8.3 Automation Workflow

### Issue Lifecycle Automation

```
Trigger: Issue Created
├─ Condition: Project = ENG
├─ Action 1: Set labels ["needs-triage"]
├─ Action 2: Assign to project lead
├─ Action 3: Send Slack notification #engineering
└─ Action 4: Set due date (sprint end + 7 days)

Trigger: Issue Status Changed to "In Review"
├─ Condition: Assignee is not empty
├─ Action 1: Notify assignee via Slack
├─ Action 2: Request review (if PR linked)
└─ Action 3: Update parent issue progress

Trigger: Issue Completed
├─ Condition: Issue type = Bug
├─ Action 1: Log to analytics
├─ Action 2: Update team metrics
└─ Action 3: Close related subtasks
```

### SLA Automation

```
Service Desk Request:
├─ First Response: 4 hours
│  └─ Auto-escalate if overdue
│
├─ Resolution: 24 hours (Critical)
│  └─ P1 issues auto-prioritized
│
└─ Notifications:
   - 1 hour before SLA breach
   - At SLA breach
   - 1 hour after SLA breach
```

### Sprint Automation

```
Before Sprint Starts:
├─ Create sprint (if auto-sprint enabled)
├─ Notify team members
└─ Set sprint goal

After Sprint Ends:
├─ Archive completed issues
├─ Move incomplete issues to next sprint
└─ Generate velocity report
```
