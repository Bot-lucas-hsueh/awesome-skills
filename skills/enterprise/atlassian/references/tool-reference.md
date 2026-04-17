## §8 · Tool Reference

### §8.1 · Atlassian Product Equivalents

| Atlassian | Competitor/Open Source | Use Case |
|-----------|------------------------|----------|
| Jira Software | Linear, Asana, Azure DevOps | Agile project management |
| Jira Service Management | ServiceNow, Zendesk | ITSM, service desk |
| Confluence | Notion, SharePoint | Knowledge management |
| Bitbucket | GitHub, GitLab | Git hosting, CI/CD |
| Trello | Monday.com, Asana boards | Simple kanban boards |
| Jira Align | Planview, Clarity | Enterprise agile |
| Loom | Vidyard, CloudApp | Async video |

### §8.2 · Key Integrations

**Development Workflow:**
```
Bitbucket ←→ Jira (issue linking, smart commits)
Bitbucket ←→ Confluence (documentation in PRs)
Jira ←→ Confluence (roadmaps, requirements)
Jira ←→ Slack (notifications, slash commands)
Bitbucket Pipelines ←→ AWS/Azure/GCP (deployments)
```

**Smart Commits Reference:**
```bash
# Link commit to issue
PROJ-123 Add authentication middleware

# Link and transition
PROJ-123 #close #comment Fixed the login bug

# Link and time log
PROJ-123 #time 4h 30m Implemented OAuth flow

# Multiple actions
PROJ-123 #in-progress #time 2h #comment Starting implementation
```

---
