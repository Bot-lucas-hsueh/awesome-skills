# Atlassian Marketplace Ecosystem

## Overview

The Atlassian Marketplace extends Atlassian products with 5,000+ apps and integrations, creating a vibrant ecosystem of partners and developers.

## Ecosystem Scale

| Metric | Value |
|--------|-------|
| Apps | 5,000+ |
| Partners | 50,000+ |
| Partner Revenue | $1B+ |
| Cloud Apps | 4,200+ |
| Data Center Apps | 2,500+ |
| Countries | 150+ |

## Top App Categories

### Reporting & Analytics
| App | Vendor | Purpose |
|-----|--------|---------|
| eazyBI | eazyBI | Advanced reporting, custom charts |
| Structure | ALM Works | Hierarchical issue organization |
| BigPicture | SoftwarePlant | Portfolio management, Gantt |
| Custom Charts | Old Street Solutions | Simple custom dashboards |

### Diagramming & Visualization
| App | Vendor | Purpose |
|-----|--------|---------|
| draw.io | JGraph | Diagrams, flowcharts |
| Gliffy | Perforce | Technical diagrams |
| SmartDraw | SmartDraw | Business diagrams |

### Automation & Scripting
| App | Vendor | Purpose |
|-----|--------|---------|
| Automation for Jira | Atlassian | Built-in automation rules |
| ScriptRunner | Adaptavist | Groovy scripting, listeners |
| Power Scripts | cPrime | Simplified scripting |

### Time Tracking
| App | Vendor | Purpose |
|-----|--------|---------|
| Tempo | Tempo | Timesheets, resource planning |
| Clockwork | HeroCoders | Automated time tracking |
| WorklogPRO | Everit | Advanced worklog features |

### Test Management
| App | Vendor | Purpose |
|-----|--------|---------|
| Zephyr | SmartBear | Test case management |
| Xray | Xpand IT | Advanced test management |
| TestRail | Gurock | Test case organization |
| qTest | Tricentis | Enterprise test management |

### ITSM & Assets
| App | Vendor | Purpose |
|-----|--------|---------|
| Insight | Atlassian | Asset and CMDB |
| Device42 | Device42 | Discovery and asset management |
| Lansweeper | Lansweeper | IT asset discovery |

### Security & Compliance
| App | Vendor | Purpose |
|-----|--------|---------|
| Snyk | Snyk | Vulnerability scanning |
| Git Secrets | Atlassian | Secret detection |
| Compliance | Various | Audit, GDPR, SOX |

## Forge Platform

Atlassian's cloud app development platform for building native extensions.

### Key Features
- Serverless functions
- UI kit components
- Custom UI support
- Storage and properties API
- Async events
- Scheduled triggers

### Example: Basic Forge App
```javascript
// manifest.yml
modules:
  jira:issuePanel:
    - key: issue-panel
      function: main
      title: My App
      icon: https://...
  
function:
  - key: main
    handler: index.run

app:
  id: ari:cloud:ecosystem::app/...
  name: my-forge-app
```

```javascript
// src/index.jsx
import ForgeUI, { render, IssuePanel, Text } from '@forge/ui';

const App = () => {
  return (
    <IssuePanel>
      <Text>Hello from Atlassian Forge!</Text>
    </IssuePanel>
  );
};

export const run = render(<App />);
```

## REST APIs

### Jira REST API v3
```
Base URL: https://your-domain.atlassian.net/rest/api/3/
```

**Common Endpoints:**
| Endpoint | Purpose |
|----------|---------|
| GET /issue/{id} | Get issue details |
| POST /issue | Create issue |
| PUT /issue/{id} | Update issue |
| GET /search | Search with JQL |
| GET /project | List projects |
| POST /issue/{id}/transitions | Transition issue |

**Example: Create Issue**
```python
import requests

JIRA_URL = "https://your-domain.atlassian.net"
AUTH = ("email@company.com", "API_TOKEN")

issue_data = {
    "fields": {
        "project": {"key": "PROJ"},
        "summary": "Implement OAuth2 authentication",
        "description": "Add OAuth2 support for API access",
        "issuetype": {"name": "Story"},
        "priority": {"name": "High"},
        "customfield_10016": 8  # Story points
    }
}

response = requests.post(
    f"{JIRA_URL}/rest/api/3/issue",
    json=issue_data,
    auth=AUTH
)
```

### Confluence REST API
```
Base URL: https://your-domain.atlassian.net/wiki/rest/api/
```

**Common Endpoints:**
| Endpoint | Purpose |
|----------|---------|
| GET /content | List pages |
| GET /content/{id} | Get page content |
| POST /content | Create page |
| PUT /content/{id} | Update page |
| GET /space | List spaces |

### Bitbucket REST API
```
Base URL: https://api.bitbucket.org/2.0/
```

**Common Endpoints:**
| Endpoint | Purpose |
|----------|---------|
| GET /repositories/{workspace}/{repo} | Get repo info |
| GET /repositories/{workspace}/{repo}/pullrequests | List PRs |
| POST /repositories/{workspace}/{repo}/pullrequests | Create PR |
| GET /repositories/{workspace}/{repo}/commits | List commits |

## Webhooks

### Jira Webhooks
Register webhooks to receive real-time events:

**Event Types:**
- jira:issue_created
- jira:issue_updated
- jira:issue_deleted
- jira:worklog_updated
- comment_created

**Configuration:**
```json
{
  "name": "My Webhook",
  "url": "https://my-app.com/webhook",
  "events": ["jira:issue_created", "jira:issue_updated"],
  "filters": {
    "issue-related-events-section": {
      "issue-event-types": [],
      "project": ["PROJ"]
    }
  }
}
```

## Atlassian Ventures

$50M fund investing in the Atlassian ecosystem.

### Investment Areas
1. Early-stage startups building cloud apps
2. Established ecosystem partners scaling
3. Channel partners expanding cloud services

### Portfolio Companies
- Zoom, Slack, InVision
- process.st, Split.io
- Marketplace partners

### Benefits for Investees
- Funding ($50K-$500K typical)
- Mentorship from Atlassian
- Global exposure at events
- Go-to-market support

## Partner Program

### Tiers
| Tier | Requirements | Benefits |
|------|--------------|----------|
| Silver | Active Marketplace presence | Basic support, listing |
| Gold | Revenue thresholds, certifications | Priority support, marketing |
| Platinum | Significant revenue, multiple certifications | Strategic partnership, co-selling |

### Certifications
- Atlassian Certified Developer
- Atlassian Cloud Certification
- Atlassian Data Center Certification

## App Development Best Practices

### Security
- Follow security guidelines
- Regular penetration testing
- Bug bounty participation
- Data encryption at rest/transit

### Performance
- Optimize API calls
- Use caching
- Async processing for long operations
- Rate limiting compliance

### User Experience
- Follow Atlassian Design Guidelines (ADG)
- Consistent with product UI
- Responsive design
- Accessibility compliance

### Support
- Clear documentation
- Responsive support channels
- Regular updates
- Deprecation policies

## Marketplace Analytics

### Metrics to Track
- Installations
- Active users
- Revenue
- Churn rate
- Reviews and ratings
- Support tickets

### Success Factors
1. Solve real problems
2. Easy to set up
3. Great documentation
4. Responsive support
5. Regular updates
6. Fair pricing
