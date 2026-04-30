# Agile Practices at Atlassian

## Scrum Framework

### Roles

**Product Owner**
- Accountable for maximizing product value
- Manages and prioritizes product backlog
- Defines acceptance criteria
- Makes go/no-go decisions
- Available to development team

**Scrum Master**
- Facilitates Scrum events
- Removes impediments
- Coaches team on Scrum
- Protects team from interruptions
- Tracks and improves team metrics

**Developers**
- Self-organizing, cross-functional
- Accountable for creating increment
- Estimate and commit to work
- Own quality (test, code review)
- Participate in all ceremonies

### Ceremonies

**Sprint Planning**
- Duration: 2-4 hours (2-week sprint)
- Inputs: Product backlog, team capacity, past velocity
- Outputs: Sprint backlog, sprint goal
- Agenda:
  1. Product Owner presents priority items
  2. Team asks clarifying questions
  3. Team estimates stories
  4. Team commits to sprint goal
  5. Team creates sprint backlog

**Daily Scrum (Standup)**
- Duration: 15 minutes
- Format: What did I do? What will I do? Any blockers?
- Focus: Coordination, not status reporting
- Tool: Jira board, Slack async updates

**Sprint Review**
- Duration: 1-2 hours
- Audience: Stakeholders, product team
- Format: Demo working software
- Goal: Gather feedback, adapt backlog
- Not: A status meeting or presentation

**Retrospective**
- Duration: 1 hour
- Format: What went well? What to improve? Actions?
- Focus: Process improvement, not blame
- Output: Action items with owners
- Tool: Confluence retrospective template

### Artifacts

**Product Backlog**
- Ordered list of everything needed
- Constantly evolving
- Refined by Product Owner
- Contains stories, bugs, tech debt

**Sprint Backlog**
- Stories committed for sprint
- Owned by development team
- Visible to all (Jira board)
- Updated daily

**Increment**
- Sum of all completed backlog items
- Must meet Definition of Done
- Potentially releasable
- Demonstrated in Sprint Review

### Metrics

**Velocity**
- Story points completed per sprint
- Used for capacity planning
- Look for trends, not absolutes
- Averages over 3-5 sprints

**Burndown Chart**
- Work remaining vs. time
- Ideal vs. actual line
- Early warning for risks

**Sprint Health**
```yaml
Commitment_Reliability: (Committed / Completed) * 100  # Target: 80-90%
Velocity_Trend: Story points per sprint  # Look for consistency
Escaped_Defects: Bugs found post-release  # Target: decreasing
Happiness_Index: Team survey  # Target: > 7/10
```

## Kanban

### Principles
- Visualize workflow
- Limit Work in Progress (WIP)
- Manage flow
- Make policies explicit
- Implement feedback loops
- Improve collaboratively

### WIP Limits
- Set per column/status
- Start with 2-3 items per person
- Adjust based on flow
- Enforce to improve cycle time

### Flow Metrics
| Metric | Formula | Target |
|--------|---------|--------|
| Cycle Time | Start → Done | < 5 days |
| Lead Time | Created → Done | < 10 days |
| Throughput | Items completed/period | Team dependent |
| Flow Efficiency | Work time / Total time | > 40% |

### Cumulative Flow Diagram
- Visualizes work distribution
- Identifies bottlenecks
- Shows trends over time

## SAFe (Scaled Agile Framework)

### Levels

**Portfolio**
- Strategic themes
- Epics (large initiatives)
- Lean budgeting

**Large Solution**
- Multiple ARTs
- Solution trains
- Complex systems

**Program (ART)**
- Agile Release Train
- 5-12 teams
- 8-12 week Program Increments

**Team**
- Scrum or Kanban
- 5-11 people
- 2-week sprints

### Program Increment (PI)
- 8-12 weeks
- Includes:
  - PI Planning (2 days)
  - System demos
  - Inspect and Adapt
  - Innovation and planning

### Jira Align Concepts

| Term | Definition |
|------|------------|
| Theme | Strategic area of investment |
| Epic | Large initiative spanning sprints |
| Feature | Deliverable value |
| Story | User-facing functionality |
| Capability | Large feature spanning ARTs |
| Enabler | Technical foundation work |

## Estimation

### Story Points
Relative sizing of effort, complexity, and uncertainty.

**Scale Options:**
- Fibonacci: 1, 2, 3, 5, 8, 13, 21
- Powers of 2: 1, 2, 4, 8, 16, 32
- T-shirt: XS, S, M, L, XL, XXL

**Planning Poker Process:**
1. Product Owner explains story
2. Team asks questions
3. Each person privately selects estimate
4. Reveal simultaneously
5. Discuss discrepancies
6. Re-estimate if needed

### Velocity
- Sum of points completed in sprint
- Used for forecasting
- Averages 3-5 sprints
- Not for comparing teams

## Definition of Done

### Standard Criteria
- [ ] Code written and reviewed
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Acceptance criteria met
- [ ] Documentation updated
- [ ] Code merged to main
- [ ] Deployed to staging
- [ ] Product Owner accepted

### Enabling Constraints
- Must be achievable every sprint
- Same for all stories
- Team owns and evolves it
- Visible to all

## Anti-Patterns

### Scrum Anti-Patterns
- **Death march:** Committing to unrealistic scope
- **Water-Scrum-fall:** Scrum in name only
- **ScrumBut:** Picking and choosing practices
- **Proxy Product Owner:** PO not empowered
- **Scrum Master as PM:** SM managing not facilitating

### Kanban Anti-Patterns
- **No WIP limits:** Just visualizing without constraining
- **Status quo:** Not improving flow
- **Ignored policies:** Rules not followed
- **Frozen board:** Stale items not addressed

## Tools in Jira

### Boards
- Scrum boards with sprints
- Kanban boards with WIP limits
- Customizable columns
- Quick filters

### Reports
- Burndown/burnup charts
- Velocity chart
- Cumulative flow diagram
- Control chart (cycle time)
- Epic burndown
- Release burndown

### Automation
- Auto-assign issues
- Transition on events
- Slack notifications
- SLA tracking
