## §4 · The DevOps Toolchain

### §4.1 · Jira: The Work Management Platform

**Market Position:**
- 65%+ market share in issue tracking
- 62% of agile teams use Jira (State of Agile Report)
- 83% of Fortune 500 companies
- 100M+ monthly active users

**Core Concepts:**

```yaml
Jira_Fundamentals:
  Issue: The basic unit of work (Story, Bug, Task, Epic)
  Project: Collection of issues with shared configuration
  Workflow: Status transitions (To Do → In Progress → Done)
  Board: Visual representation (Scrum or Kanban)
  Sprint: Time-boxed iteration (1-4 weeks)
  Epic: Large body of work spanning multiple sprints
```

**Agile Workflow:**
```
Product Backlog → Sprint Planning → Active Sprint → Review → Retro
      ↑                                                    |
      └──────────────── Backlog Refinement ←───────────────┘
```

### §4.2 · Confluence: The Team Workspace

**Purpose:** Knowledge management, documentation, and team collaboration.

**Key Features:**

| Feature | Function | Use Case |
|---------|----------|----------|
| **Pages** | Document creation | Requirements, runbooks, retrospectives |
| **Spaces** | Organized content areas | Team spaces, project spaces, personal |
| **Templates** | Pre-structured pages | Meeting notes, decisions, retros |
| **Macros** | Dynamic content | Jira issues, roadmaps, diagrams |
| **Page Tree** | Hierarchical organization | Product documentation, wikis |

**Documentation-First Culture:**
```markdown
# Decision Log Template

## Status: PROPOSED | APPROVED | REJECTED | SUPERSEDED

## Context
What is the issue we're seeing?

## Decision
What are we doing about it?

## Consequences
What becomes easier/harder?

## Alternatives Considered
- Option A: ...
- Option B: ...
```

### §4.3 · Bitbucket: Code Collaboration

**Overview:** Git-based source control with native Jira integration.

**Differentiation:**
| Feature | Bitbucket | GitHub | GitLab |
|---------|-----------|--------|--------|
| Jira Integration | Native, bidirectional | Via apps | Via apps |
| Pipelines CI/CD | Built-in | GitHub Actions | Built-in |
| Best For | Atlassian ecosystem | Open source | Single DevOps app |
| Market Position | 12M+ users, #2 behind GitHub | 100M+ developers | 5M+ users |

**Bitbucket Pipelines (CI/CD):**
```yaml
# bitbucket-pipelines.yml
image: node:18

pipelines:
  default:
    - step:
        name: Build and Test
        script:
          - npm ci
          - npm run lint
          - npm run test:coverage
          - npm run build
        artifacts:
          - dist/**
    
    - step:
        name: Deploy to Staging
        deployment: staging
        trigger: manual
        script:
          - npm run deploy:staging
    
    - step:
        name: Security Scan
        script:
          - pipe: atlassian/snyk-scan:0.5.0
          - pipe: atlassian/git-secrets-scan:0.5.1
```

### §4.4 · The Integrated DevOps Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                    PLAN (Jira Software)                         │
│  Backlog → Sprint Planning → Story Estimation → Roadmap         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    CODE (Bitbucket)                             │
│  Branch → Commit → Pull Request → Code Review → Merge           │
│  ↓ Issue keys in commits auto-link to Jira                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    BUILD (Bitbucket Pipelines)                  │
│  Compile → Unit Tests → Integration Tests → Security Scan       │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    DEPLOY (Jira Service Management)             │
│  Change Request → Approval → Deployment → Verification          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    OPERATE & LEARN                              │
│  Monitoring → Incidents (JSM) → Post-mortems (Confluence)       │
└─────────────────────────────────────────────────────────────────┘
```

---
