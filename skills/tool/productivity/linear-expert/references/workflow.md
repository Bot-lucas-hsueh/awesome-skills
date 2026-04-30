# Standard Workflow

## 8.1 Issue Management Workflow

```
Issue Lifecycle
├── Creation
│   ├── Submit via Linear UI or API
│   ├── Assign team and project
│   ├── Set priority (0-4)
│   ├── Add labels and estimate
│   └── Link to milestone/cycle
│
├── In Progress
│   ├── Assign to team member
│   ├── Move to "In Progress" state
│   ├── Link PR (GitHub integration)
│   ├── Update progress
│   └── Log time if tracking
│
├── Review
│   ├── Move to "In Review" state
│   ├── Request review
│   ├── Address feedback
│   └── Squash/merge PR
│
└── Completion
    ├── Move to "Done" state
    ├── Verify all checklist items
    └── Close/resolve
```

## 8.2 Integration Workflow

### GitHub Integration

```
Linear ↔ GitHub:
1. Connect GitHub account in Linear
2. Install Linear GitHub app
3. Link repositories to teams
4. Link PRs to issues

Branch Naming Convention:
- linear-123-add-authentication
- ENG-123-feature-login

Commit Messages:
- Fixes ENG-123: Resolve login timeout
- Closes ENG-123

PR Description:
Resolves ENG-123

### Changes Made
- Added OAuth2 support
- Updated login flow

### Testing
- [x] Unit tests
- [x] E2E tests
```

### GitLab Integration

```
Linear ↔ GitLab:
1. Configure GitLab integration in Linear
2. Link GitLab projects
3. Reference issues in commits

Merge Request Reference:
- !123 → Links MR to current issue
- Closes linear:ENG-123 → Closes on merge
```

### Slack Integration

```
Linear → Slack Notifications:
1. Install Linear Slack app
2. Configure channel notifications
3. Set up notification rules

Commands:
/linear issue ENG-123 → Shows issue details
/linear create "New task" → Create issue
/linear assign ENG-123 @user → Assign issue

Notification Events:
- New issue assigned
- Issue status changed
- PR linked
- Comment added
- Cycle started/ended
```

### Zapier/Make Integration

```
Trigger: Linear Issue Created
├─ Filter by team/project
├─ Create card in Trello
├─ Add to Notion database
├─ Send Slack DM to assignee

Trigger: Linear Issue Completed
├─ Update external task system
├─ Send completion notification
├─ Archive related items
└─ Trigger next workflow step
```

## 8.3 Automation Workflow

### Issue Auto-Assignment

```javascript
// Auto-assign based on labels
const rules = {
  'frontend': 'alice@example.com',
  'backend': 'bob@example.com',
  'devops': 'carol@example.com',
  'urgent': 'lead@example.com'
};

async function autoAssign(issue) {
  for (const [label, assignee] of Object.entries(rules)) {
    if (issue.labels.includes(label)) {
      await linear.issues.update(issue.id, {
        assigneeId: await getUserId(assignee)
      });
      break;
    }
  }
}
```

### Sprint Automation

```
Weekly Sprint Workflow:
1. Cycle Created (Sunday night)
   ├─ Create cycle with dates
   ├─ Import backlog items
   └─ Notify team

2. Daily Updates
   ├─ Bot posts daily summary
   ├─ Show: Done, In Progress, Blocked
   └─ Remind of upcoming deadlines

3. Cycle Completed (Friday)
   ├─ Move incomplete to next cycle
   ├─ Generate velocity report
   └─ Start retrospective
```

### PR Auto-Linking

```javascript
// GitHub webhook handler
app.post('/webhooks/github', async (req, res) => {
  const { action, pull_request, repository } = req.body;
  
  if (action === 'opened' || action === ' synchronize') {
    // Extract Linear issue key from branch
    const match = pull_request.head.ref.match(/linear-(\w+-\d+)/);
    if (match) {
      const issueId = await getIssueId(match[1]);
      await linear.issues.update(issueId, {
        labelIds: [getLabelId('has-pr')]
      });
      
      // Post comment
      await linear.comments.create({
        issueId,
        body: `PR opened: ${pull_request.html_url}`
      });
    }
  }
  
  res.sendStatus(200);
});
```

### Milestone Progress Tracking

```
Milestone: v2.0 Release
├─ Progress auto-calculated
│   ├─ Total issues: 50
│   ├─ Completed: 35
│   └─ Progress: 70%
│
├─ Blocking Issues: highlighted
│
└─ Auto-updates:
   ├─ Slack notification at 25%, 50%, 75%
   └─ Email at 100% (release ready)
```
