# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | **Creating issues without team/project** | High | Always assign to team |
| 2 | **Setting unrealistic estimates** | Medium | Use historical velocity |
| 3 | **Not using cycles properly** | Medium | Define sprint cadence |
| 4 | **Overusing labels** | Low | Keep to 10-15 labels max |
| 5 | **Skipping issue descriptions** | Medium | Use templates |
| 6 | **Not linking PRs to issues** | Medium | Use branch naming |
| 7 | **Ignoring inbox** | High | Set daily inbox review |
| 8 | **Creating too many priorities** | Low | Use 0-4 scale only |

### Anti-Pattern: Unscoped Issues

```markdown
# BAD
Title: "Fix bug"
Description: "Something is broken"

# GOOD
Title: "Login fails for users with special characters in email"
Description:
- Team: Engineering
- Priority: P2
- Labels: backend, authentication
- Estimate: 3
- Acceptance criteria:
  - [ ] Users can login with email containing +
  - [ ] Error message displayed correctly
```

## 10.2 Anti-Patterns

### 1. Over-Customizing Workflow

```
Anti-Pattern:
- 15+ custom states
- Complex workflow rules
- Multiple teams for similar work

Problem: Cognitive overload, inconsistent processes

Solution:
- Use default states (Backlog, Todo, In Progress, In Review, Done)
- Limit to 6-8 states max
- Consolidate similar teams
```

### 2. Issue Sprawl

```
Anti-Pattern:
- Creating separate issue for every tiny task
- No epic/initiative grouping
- Hard to see big picture

Problem: Too many issues to track

Solution:
- Use epics for features
- Group related tasks
- Use checklists in issue description for small items
```

### 3. Neglecting Inbox

```
Anti-Pattern:
- Ignoring inbox for days
- Comments unanswered
- Issues stacking up

Problem: Missed feedback, lost context

Solution:
- Set inbox zero goal daily
- Use filters to prioritize
- Batch process comments
```

### 4. Not Using Cycles

```
Anti-Pattern:
- No sprint planning
- Issues added随时随地
- No velocity tracking

Solution:
- Define sprint cadence (1 or 2 weeks)
- Plan cycle in advance
- Track velocity over time
```

### 5. Poor Estimation

```
Anti-Pattern:
- No estimates
- Story points inconsistent
- Estimates don't reflect reality

Solution:
- Use Fibonacci sequence (1, 2, 3, 5, 8, 13)
- Calibrate against historical data
- Refine estimates during sprint
```

## 10.3 Integration Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| No webhook verification | Security | Verify webhook signatures |
| Syncing everything | Performance | Filter events |
| Ignoring webhook failures | Data loss | Implement retry logic |
| Hardcoded team IDs | Fragile | Use environment variables |
| No rate limit handling | API blocks | Implement backoff |

## 10.4 Performance Anti-Patterns

```graphql
# BAD: N+1 queries
query {
  issues {
    nodes {
      assignee {
        name
        email
        avatarUrl
        teams {
          nodes {
            name
          }
        }
      }
      comments {
        nodes {
          author {
            name
          }
        }
      }
    }
  }
}

# GOOD: Specific fields
query {
  issues {
    nodes {
      identifier
      title
      assignee {
        name
      }
    }
  }
}

# BAD: Large page size
issues(first: 1000)  // May timeout

# GOOD: Pagination
issues(first: 50) {
  pageInfo {
    hasNextPage
    endCursor
  }
  nodes {
    ...
  }
}
```

## 10.5 API Anti-Patterns

```javascript
// BAD: Polling for updates
setInterval(async () => {
  const issues = await linear.issues();
  updateUI(issues);
}, 5000);

// GOOD: Webhooks
app.post('/webhooks/linear', async (req, res) => {
  const { type, action, data } = req.body;
  
  if (type === 'Issue' && action === 'update') {
    await handleIssueUpdate(data);
  }
  
  res.sendStatus(200);
});

// BAD: No error handling
const issue = await linear.issues.create({ title: 'Test' });
await updateUI(issue);

// GOOD: Proper error handling
try {
  const issue = await linear.issues.create({ title: 'Test' });
  await updateUI(issue);
} catch (error) {
  if (error.code === 'PAYLOAD_TOO_LARGE') {
    // Handle size limit
  } else if (error.code === 'UNAUTHORIZED') {
    // Re-authenticate
  } else {
    throw error;
  }
}
```
