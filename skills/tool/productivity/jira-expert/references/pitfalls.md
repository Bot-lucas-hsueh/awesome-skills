# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | **Creating issues without acceptance criteria** | High | Use issue template with AC field |
| 2 | **Setting due dates arbitrarily** | High | Link to sprint dates |
| 3 | **Overusing sub-tasks** | Medium | Use story points, break into stories if needed |
| 4 | **Not linking related issues** | Medium | Configure issue links in workflow |
| 5 | **Skipping sprint retrospectives** | High | Set recurring calendar invite |
| 6 | **Over-customizing workflows** | Medium | Use default workflow, minimize changes |
| 7 | **Storing specs in issue descriptions only** | High | Use Confluence, link from Jira |
| 8 | **Ignoring JQL performance** | High | Test queries, use indexes |

### Anti-Pattern: Issue Descriptions

```markdown
# BAD - Unclear description
"Fix the login bug"

# GOOD - Detailed with reproduction steps
"**Bug:** Login fails for users with special characters in email

**Environment:** Chrome 120, Jira Cloud
**Steps to Reproduce:**
1. Go to https://example.atlassian.net
2. Attempt login with user@example.com!
3. Error: 'Invalid email format'

**Expected:** Login should succeed
**Actual:** Error thrown
**Priority:** Medium
**Labels:** frontend, authentication
"
```

## 10.2 Anti-Patterns

### 1. Over-Engineering Projects

```
Anti-Pattern:
- Create 10 custom fields per issue
- 15 workflow statuses
- Complex screen schemes

Problem: Cognitive overload, slow issue creation

Solution:
- Use default fields + minimal custom fields (max 5)
- Use labels instead of custom fields
- Stick to: To Do, In Progress, In Review, Done
```

### 2. Issue Hoarding

```
Anti-Pattern:
- Create issues months in advance
- Sprint backlog never empty
- "Parking lot" of 200+ issues

Problem: Stale issues, poor velocity forecasting

Solution:
- Create issues 1-2 sprints ahead max
- Quarterly backlog grooming
- Delete/reconsider old issues
```

### 3. Status Ping-Pong

```
Anti-Pattern:
- Issue: To Do → In Progress → To Do → In Progress...

Problem: Status loses meaning, poor metrics

Solution:
- Only move forward in workflow
- Use "On Hold" status for blocked work
- Set transition rules to prevent back-moves
```

### 4. Wrong Issue Type Usage

```
Anti-Pattern:
- Creating "Stories" for tech debt
- Using "Tasks" for customer requests
- No "Bugs" for production issues

Solution:
- Story: User-facing feature
- Task: Technical/internal work  
- Bug: Defect requiring fix
- Epic: Large feature spanning sprints
```

### 5. Neglecting Automation

```
Anti-Pattern:
- Manual issue assignments
- Copy-paste repetitive comments
- No status update notifications

Solution:
- Automate with Jira Automation
- Use Slack integration
- Create email rules for notifications
```

## 10.3 Security Anti-Patterns

| Anti-Pattern | Risk | Fix |
|--------------|------|-----|
| Storing API tokens in issue descriptions | Credential exposure | Use secrets management |
| Making projects public by default | Data leak | Restrict by default |
| Granting admin to all developers | Over-privilege | Role-based access |
| Sharing login credentials | Accountability loss | Individual accounts |
| No webhook SSL verification | MITM attacks | Enable SSL verification |

## 10.4 Performance Anti-Patterns

```jql
# BAD - Performance issues
text ~ "*error*" AND text ~ "issue"
project IS NOT EMPTY AND project IS NOT EMPTY

# GOOD - Optimized queries
project = ENG AND status = Open
labels = critical ORDER BY created DESC
```

```
Anti-Pattern: Complex filters with multiple text searches
Fix: Use indexed fields (project, status, assignee, labels)

Anti-Pattern: Dashboard with 20 gadgets loading all projects
Fix: Limit to current project, cache results

Anti-Pattern: Heavy automation on every issue event
Fix: Add conditions to trigger only when needed
```
