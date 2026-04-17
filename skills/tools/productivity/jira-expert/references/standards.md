# Standards & Reference

## 7.1 Official Documentation

- [Jira Documentation](https://docs.atlassian.com/jira-software)
- [Jira Software Cloud](https://www.atlassian.com/software/jira)
- [Jira API v3 Reference](https://docs.atlassian.com/jira-software/REST/latest)
- [Jira Expression](https://confluence.atlassian.com/jirakb/jira-expressions-supported-entities-1086405035.html)
- [JQL Reference](https://docs.atlassian.com/jira-software/REST/latest/#api/2/search)
- [Automation Rules](https://support.atlassian.com/jira-software-cloud/docs/automation-rules-reference)
- [Atlassian Developer](https://developer.atlassian.com/cloud/jira)

## 7.2 Configuration Reference

### Project Configuration (jira-project.yml)

```yaml
project:
  key: ENG
  name: Engineering
  type: software
  lead: alice@example.com

settings:
  default-issue-type: Story
  allow-subtasks: true
  default-priority: Medium
  issue-security-level:
    - Confidential
    - Internal
    - Public

workflows:
  - name: Sprints
    start-column: To Do
    done-column: Done

fields:
  - name: Sprint
    required: true
  - name: Story Points
    type: number
```

### Automation Rule Template

```json
{
  "trigger": {
    "type": "jira.issue.created"
  },
  "conditions": [
    {
      "type": "jira.issue.condition",
      "field": "project",
      "condition": "equals",
      "value": "ENG"
    }
  ],
  "actions": [
    {
      "type": "jira.issue.assign",
      "assignee": {
        "type": "user",
        "value": "{{issue.reporter.accountId}}"
      }
    },
    {
      "type": "jira.issue.transition",
      "transition": {
        "id": 21
      }
    }
  ]
}
```

### Webhook Configuration

```json
{
  "webhooks": [
    {
      "name": "CI/CD Integration",
      "url": "https://ci.example.com/webhooks/jira",
      "events": [
        "jira:issue_created",
        "jira:issue_updated",
        "jira:issue_deleted",
        "jira:worklog_updated"
      ],
      "filters": {
        "issue-related-events-section": "project = ENG"
      }
    }
  ]
}
```

## 7.3 Common Commands & Operations

### JQL Queries

| Query | Purpose |
|-------|---------|
| `project = ENG AND sprint IN openSprints()` | Active sprint issues |
| `assignee = currentUser() AND sprint IN openSprints()` | My sprint issues |
| `project = ENG AND issuetype = Bug AND status != Closed ORDER BY created DESC` | Open bugs |
| `created >= -1w AND project = ENG` | Recently created |
| `updated >= -1d AND assignee = currentUser()` | Recently updated, assigned to me |
| `labels = blocked AND status != Done` | Blocked issues |

### Bulk Operations

```
1. Search with JQL: project = ENG AND status = "In Review"
2. Select All (50+ issues)
3. Bulk Edit > Transition to Done
4. Add comment: "Closing as verified in production"
```

### Sprint Management

```
Sprint Board: /secure/RapidBoard.jspa?rapidView=1
Create Sprint: /secure/CreateSprint!default.jspa?rapidViewId=1
Reports: /secure/Reports!default.jspa?rapidViewId=1
```

## 7.4 Version & Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| Jira Cloud | Current | REST API v3, Automation 2.0 |
| Jira Data Center | Current | Same API, local deployment |
| Jira Software 9.x | Current | Latest LTS |
| Jira Core 9.x | Current | Project management |

| Feature | Cloud | Data Center |
|---------|-------|-------------|
| Automation | Native | Native |
| Projects (Next-gen) | Yes | No |
| Git integration | Source Commits | Source Commits |
| Advanced Roadmaps | Yes | With Data Center 7.19+ |
| Insight ITSM | Add-on | Add-on |

### API Rate Limits

- Cloud: 0-10,000 requests/minute per tenant (based on tier)
- Data Center: No rate limit, depends on server resources
- Batch operations: Max 50 items per request
