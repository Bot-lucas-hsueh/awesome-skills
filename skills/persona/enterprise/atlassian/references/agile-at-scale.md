## §5 · Agile at Scale

### §5.1 · Scrum Framework

**Roles:**
| Role | Responsibility | Atlassian Tool |
|------|----------------|----------------|
| **Product Owner** | Backlog prioritization, value maximization | Jira Roadmap |
| **Scrum Master** | Facilitation, impediment removal | Jira Board, Reports |
| **Developers** | Building increment, self-organization | Jira issues, Bitbucket |

**Ceremonies:**
```yaml
Sprint_Cycle:
  Sprint_Planning: 
    duration: 2-4 hours (2-week sprint)
    output: Sprint backlog, sprint goal
    tool: Jira Sprint creation
    
  Daily_Scrum:
    duration: 15 minutes
    format: What did I do? What will I do? Blockers?
    tool: Jira board, Slack async updates
    
  Sprint_Review:
    duration: 1-2 hours
    focus: Demo working software, gather feedback
    tool: Confluence demo notes
    
  Retrospective:
    duration: 1 hour
    format: What went well? What to improve? Actions?
    tool: Confluence retrospective template
```

### §5.2 · SAFe with Jira Align

**Enterprise Agile Framework:**

```
Portfolio Level (Strategic Themes)
    ↓
Program Level (ART - Agile Release Trains)
    ↓
Team Level (Scrum/Kanban Teams)
```

**Jira Align Concepts:**
| Term | Definition | Jira Mapping |
|------|------------|--------------|
| **Theme** | Strategic area of investment | Epic category |
| **Epic** | Large initiative | Epic issue type |
| **Feature** | Deliverable value | Story with feature flag |
| **Story** | User-facing functionality | Standard story |
| **Enabler** | Technical foundation | Technical story |

### §5.3 · Metrics That Matter

**Flow Metrics (Kanban):**
| Metric | Formula | Target |
|--------|---------|--------|
| **Cycle Time** | Start → Done duration | < 5 days |
| **Lead Time** | Created → Done duration | < 10 days |
| **Throughput** | Items completed per sprint | Team velocity |
| **WIP Limits** | Max items per status | 2-3 per developer |

**Agile Health Metrics:**
```yaml
Sprint_Health:
  Commitment_Reliability: (Committed / Completed) * 100  # Target: 80-90%
  Velocity_Trend: Story points per sprint  # Look for consistency
  Escaped_Defects: Bugs found post-release  # Target: decreasing
  Happiness_Index: Team survey  # Target: > 7/10
```

---
