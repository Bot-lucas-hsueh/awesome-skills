# Standards & Reference

## 7.1 Official Documentation

- [Linear Documentation](https://linear.app/docs)
- [Linear API Reference](https://developers.linear.app/docs)
- [Linear GraphQL API](https://api.linear.app/graphql)
- [Linear Integrations](https://linear.app/integrations)
- [Linear Webhooks](https://developers.linear.app/docs/webhooks)
- [Linear SDK](https://developers.linear.app/docs/sdk)
- [Linear GitHub Integration](https://linear.app/docs/github)
- [Linear GitLab Integration](https://linear.app/docs/gitlab)

## 7.2 Configuration Reference

### Linear SDK Setup

```javascript
import { LinearClient } from '@linear/sdk';

const linear = new LinearClient({
  apiKey: process.env.LINEAR_API_KEY
});

// Query issues
const issues = await linear.issues({
  filter: {
    team: { id: { eq: 'team-id' } },
    state: { name: { eq: 'In Progress' } }
  }
});
```

### GraphQL API Configuration

```bash
# GraphQL Endpoint
POST https://api.linear.app/graphql

# Headers
Authorization: Bearer <your-api-key>
Content-Type: application/json
```

### API Key Setup

```yaml
# Environment
LINEAR_API_KEY=lin_api_xxxxxxxxxxxxxxxxxxxx

# Create API key
# Settings → API → Personal API Keys → Create new
# Scopes: read, write, comments, etc.
```

### Issue Properties

```json
{
  "id": "issue-id-123",
  "identifier": "ENG-456",
  "title": "Implement user authentication",
  "description": "## Details\n\nAdd OAuth2 support",
  "priority": 1,
  "priorityLabel": "Urgent",
  "state": {
    "name": "In Progress",
    "type": "started"
  },
  "team": {
    "key": "ENG",
    "name": "Engineering"
  },
  "assignee": {
    "id": "user-id",
    "name": "Alice",
    "email": "alice@example.com"
  },
  "labels": [
    { "name": "backend", "color": "#ef4444" }
  ],
  "dueDate": "2024-02-15",
  "estimate": 5,
  "startedAt": "2024-02-01T10:00:00Z",
  "completedAt": null
}
```

### Webhook Configuration

```json
{
  "webhook": {
    "url": "https://api.example.com/webhooks/linear",
    "secret": "whsec_xxxxxxxx",
    "events": [
      "Issue",
      "Comment",
      "Project",
      "Cycle"
    ]
  }
}
```

## 7.3 Common Commands & Operations

### Linear CLI

```bash
# Install Linear CLI
npm install -g @linear/cli

# Login
linear login

# View issues
linear issue list --team ENG

# Create issue
linear issue create --team ENG --title "New feature"

# Update issue
linear issue update ENG-123 --state "In Progress"

# Comment on issue
linear comment ENG-123 "Looking good!"

# Search
linear search "authentication"
```

### GraphQL Queries

| Query | Purpose |
|-------|---------|
| `viewer` | Get current user |
| `teams` | List all teams |
| `issues` | Query issues with filters |
| `cycles` | List sprint cycles |
| `projects` | List projects |
| `users` | List workspace users |

### Common Filters

```graphql
# Active sprint issues
query {
  issues(filter: {
    cycle: { id: { eq: "cycle-id" } }
    state: { type: { notEq: "completed" } }
  }) {
    nodes {
      id
      identifier
      title
      assignee {
        name
      }
    }
  }
}

# My assigned issues
query {
  issues(filter: {
    assignee: { id: { eq: "me" } }
    state: { type: { notEq: "cancelled" } }
  }) {
    nodes {
      identifier
      title
      priority
      dueDate
    }
  }
}
```

## 7.4 Version & Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| Linear Web | Current | Full functionality |
| Linear Desktop | Current | macOS/Windows |
| Linear Mobile | Current | iOS/Android |
| Linear API | Current | GraphQL, v1 |
| Linear SDK | v19.x | NPM package |

| Plan | Members | Issues | Cycles | Storage |
|------|--------|--------|--------|---------|
| Free | 250 | Unlimited | Unlimited | 10GB |
| Standard | Unlimited | Unlimited | Unlimited | 100GB |
| Pro | Unlimited | Unlimited | Unlimited | 1TB |
| Enterprise | Unlimited | Unlimited | Unlimited | Unlimited |

### Rate Limits

```
API:
- 200 requests per minute (authenticated)
- 50 requests per minute (unauthenticated)
- 5000 requests per day

Webhook delivery:
- Max 3 retries
- 30 second timeout
- 72 hour retry window
```
