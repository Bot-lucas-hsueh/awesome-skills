# Scenario Examples

## 9.1 Team Workflows

### Scenario: Sprint Planning

**User:** "How do we run sprint planning with Linear?"

**Expert:**
> **Sprint Planning Workflow:**
>
> 1. **Prepare Backlog**
>    - Create cycle: "Sprint 24"
>    - Set dates: Feb 5-16, 2024
>    - Set scope capacity
>
> 2. **Select Issues**
>    ```graphql
>    query {
>      issues(filter: {
>        cycle: { id: { eq: null } }
>        team: { key: { eq: "ENG" } }
        state: { name: { eq: "Backlog" } }
      }) {
>        nodes {
>          identifier
>          title
>          estimate
          priority
>        }
>      }
>    }
>    ```
>
> 3. **Drag Issues to Cycle**
>    - Prioritize by business value
>    - Check total estimate vs capacity
>    - Move to cycle
>
> 4. **Assign & Kick Off**
>    - Assign issues to team members
>    - Set sprint goal in cycle description
>    - Announce to team

### Scenario: Bug Triage

**User:** "How should we handle incoming bugs?"

**Expert:**
> **Bug Triage Process:**
>
> 1. **Inbox Triage**
>    ```graphql
>    query {
>      issues(filter: {
>        inbox: { id: { eq: "inbox-id" } }
>        state: { name: { eq: "Triage" } }
>      }) {
>        nodes {
>          identifier
>          title
>          priority
>          assignee {
>            name
>          }
>        }
>      }
>    }
>    ```
>
> 2. **Triage Checklist**
>    - [ ] Reproduced and confirmed?
>    - [ ] Priority assigned (P1-P4)?
>    - [ ] Team assigned?
>    - [ ] Labels added (frontend/backend)?
>    - [ ] Related issues linked?
>    - [ ] Estimate added?
>
> 3. **Quick Actions**
>    - `/linear triage ENG-123 --priority 2 --team backend`

## 9.2 Automation Scenarios

### Linear API Queries

```graphql
# Velocity calculation
query Velocity($teamId: String!, $cycleCount: Int!) {
  team(id: $teamId) {
    name
    issues( filter: {
      completedAt: { gte: "2024-01-01" }
    }) {
      nodes {
        estimate
        completedAt
        cycle {
          name
        }
      }
    }
  }
}

# Blockers report
query Blockers {
  issues(filter: {
    state: { name: { in: ["In Progress", "In Review"] } }
    label: { name: { eq: "blocked" } }
  }) {
    nodes {
      identifier
      title
      assignee {
        name
        email
      }
      updatedAt
    }
  }
}
```

### Workflow Automations

```javascript
// Auto-close stale issues
async function closeStaleIssues() {
  const thirtyDaysAgo = new Date();
  thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);
  
  const staleIssues = await linear.issues({
    filter: {
      updatedAt: { lt: thirtyDaysAgo.toISOString() }
      state: { name: { eq: "In Progress" } }
    }
  });
  
  for (const issue of staleIssues.nodes) {
    await linear.issues.update(issue.id, {
      stateId: getStateId("Backlog"),
      comment: "Moved to backlog due to inactivity"
    });
  }
}

// Auto-escalate urgent issues
async function escalateUrgentIssues() {
  const urgentIssues = await linear.issues({
    filter: {
      priority: { eq: 0 }
      state: { name: { notIn: ["In Progress", "In Review"] } }
    }
  });
  
  for (const issue of urgentIssues.nodes) {
    // Notify Slack
    await slack.chat.postMessage({
      channel: '#engineering',
      text: `🔴 Urgent: ${issue.identifier} not started`
    });
  }
}
```

### Custom Issue Templates

```javascript
// Create issue with template
async function createBugIssue(data) {
  return await linear.issues.create({
    teamId: 'eng-team-id',
    title: data.title,
    description: `
## Bug Description
${data.description}

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior


## Actual Behavior


## Environment
- OS: 
- Browser: 
- Version: 

## Screenshots


## Priority
- [ ] P1 - Critical
- [ ] P2 - High
- [ ] P3 - Medium
- [ ] P4 - Low
    `,
    labelIds: [getLabelId('bug')],
    priority: data.priority || 2
  });
}
```

## 9.3 DevOps Workflows

### Release Management

```
Release v2.1.0:
├─ Create Milestone
│   ├─ Name: v2.1.0
│   ├─ Target date: 2024-02-15
│   └─ Linked issues
│
├─ Track Progress
│   ├─ Total: 25 issues
│   ├─ Completed: 18
│   ├─ Remaining: 7
│   └─ Progress: 72%
│
├─ Release Checklist
│   ├─ All P0 issues closed
│   ├─ QA sign-off
│   ├─ Release notes generated
│   └─ Deployment scheduled
│
└─ Post-Release
    ├─ Move remaining to next release
    ├─ Archive milestone
    └─ Send release announcement
```

### CI/CD Integration

```yaml
# GitHub Actions .github/workflows/linear.yml
name: Linear Integration

on:
  pull_request:
    types: [opened, synchronize, closed]

jobs:
  linear:
    runs-on: ubuntu-latest
    steps:
      - name: Link PR to Linear
        uses: linear/github-action/create Linear issue
        with:
          linear_token: ${{ secrets.LINEAR_API_KEY }}
          title: ${{ github.head_ref }}
        
      - name: Update Linear on merge
        if: github.event.pull_request.merged
        uses: linear/github-action/done Linear issue
        with:
          linear_token: ${{ secrets.LINEAR_API_KEY }}
```

### Incident Response

```
Incident Issue Template:
├─ Severity (P1-P4)
├─ Status (Investigating, Identified, Resolved)
├─ Impact (users affected, revenue impact)
├─ Timeline
│   ├─ Detected: timestamp
│   ├─ Investigating: timestamp
│   ├─ Identified: timestamp
│   └─ Resolved: timestamp
│
├─ Root Cause
│
├─ Resolution
│
└─ Action Items
    └─ Linked follow-up issues

Automation:
P1 Created:
├─ Create dedicated issue
├─ Set status: Investigating
├─ DM on-call engineer
├─ Create #incident Slack channel
└─ Start timer

Status Changed to Resolved:
├─ Prompt for post-mortem
├─ Create follow-up issues
└─ Archive incident tracking
```

### Deployment Tracking

```javascript
// Track deployments in Linear
async function trackDeployment(deployment) {
  const { version, environment, status, commits } = deployment;
  
  // Create deployment issue
  const issue = await linear.issues.create({
    teamId: 'devops-team-id',
    title: `Deploy ${version} to ${environment}`,
    stateId: status === 'success' ? getStateId('Done') : getStateId('In Progress'),
    labelIds: [
      getLabelId('deployment'),
      getLabelId(environment)
    ]
  });
  
  // Link commits
  for (const commit of commits) {
    await linear.issues.update(issue.id, {
      linkedIssues: {
        create: {
          issueId: issue.id,
          comment: `Deployed commit: ${commit.sha.slice(0, 7)}`
        }
      }
    });
  }
  
  return issue;
}
```
