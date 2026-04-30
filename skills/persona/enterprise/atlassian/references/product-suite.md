# Atlassian Product Suite Reference

## Core Products Overview

### Jira Software
**Purpose:** Agile project management and issue tracking

**Key Features:**
- Scrum and Kanban boards
- Roadmaps and timeline views
- Customizable workflows
- Advanced search (JQL)
- Sprint planning and reporting
- Backlog management
- Integration with 3,000+ apps

**Editions:**
| Edition | Users | Price | Features |
|---------|-------|-------|----------|
| Free | Up to 10 | $0 | Basic features |
| Standard | Up to 10,000 | $8.15/user | Advanced permissions |
| Premium | Unlimited | $16/user | Advanced roadmaps, sandbox |
| Enterprise | Unlimited | Custom | Atlassian Analytics, data residency |

### Confluence
**Purpose:** Team workspace and knowledge management

**Key Features:**
- Page trees and hierarchies
- Real-time collaborative editing
- Templates and blueprints
- Macros (Jira issues, roadmaps, diagrams)
- Page versioning and history
- Comments and inline feedback
- Spaces for teams and projects

**Best Practices:**
1. Create a space per team or major project
2. Use templates for consistency
3. Maintain a clear page hierarchy
4. Link related content
5. Review and archive outdated content quarterly

### Bitbucket
**Purpose:** Git code hosting and CI/CD

**Key Features:**
- Unlimited private repositories
- Pull requests with code review
- Branch permissions and merge checks
- Bitbucket Pipelines (CI/CD)
- Jira integration (smart commits)
- Deployment permissions
- Large file support (LFS)

**Bitbucket Pipelines Features:**
- YAML configuration
- Docker support
- Caching for faster builds
- Deployment environments
- Parallel steps
- Conditional execution
- Pipe integrations (Snyk, AWS, etc.)

### Jira Service Management
**Purpose:** IT service management and help desk

**Key Features:**
- Service request management
- Incident and problem management
- Change management
- Asset and configuration management
- Knowledge base integration
- SLA management
- Self-service portal

**Use Cases:**
- IT help desk
- HR service delivery
- Facilities management
- Legal service requests
- Customer service

### Trello
**Purpose:** Visual project management

**Key Features:**
- Kanban boards
- Cards with checklists
- Labels and filters
- Power-Ups (integrations)
- Butler automation
- Calendar and timeline views
- Mobile apps

**Best For:**
- Simple projects
- Personal task management
- Small teams
- Visual workflows
- Marketing campaigns
- Content calendars

---

## Cloud vs Data Center

### Atlassian Cloud
**Best for:** Most teams, especially those wanting:
- Automatic updates
- Reduced maintenance
- AI features (Atlassian Intelligence)
- Mobile and web access
- Predictable costs

### Data Center
**Best for:** Organizations requiring:
- Self-hosting for compliance
- Custom infrastructure
- Specific data residency
- High availability clustering
- Advanced customization

**Migration Timeline:**
- Server support ended: February 2024
- Data Center EOL: March 2029
- 99% of customers are cloud or migrating

---

## Integration Ecosystem

### Key Integrations

| Category | Popular Integrations |
|----------|---------------------|
| Communication | Slack, Microsoft Teams, Zoom |
| Development | GitHub, GitLab, Azure DevOps |
| Design | Figma, InVision, Adobe Creative Cloud |
| Analytics | Tableau, Power BI, Google Analytics |
| CRM | Salesforce, HubSpot, Zendesk |
| Cloud | AWS, Azure, GCP |

### Smart Commits
Format: `<ISSUE_KEY> #<action> #<action>`

**Actions:**
- `#comment` - Add comment
- `#time` - Log work time
- `#close` or `#resolve` - Transition to done
- `#in-progress` - Transition to in progress
- `#review` - Request review

**Examples:**
```
PROJ-123 Add login feature #time 4h #comment Implemented OAuth
PROJ-456 Fix null pointer #close
PROJ-789 Update documentation #in-progress
```
