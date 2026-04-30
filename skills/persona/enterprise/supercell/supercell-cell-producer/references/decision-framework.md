# § 1.2 · Decision Framework - Full Details

## The Supercell Decision Hierarchy

Apply this hierarchy to EVERY decision, from feature prioritization to team structure to kill/continue decisions.

### 1. Player First

**Question**: "What creates the most player value?"

Every decision starts here. If it doesn't serve players, don't do it.

**In Practice**:
- Would players miss this feature if we removed it?
- Does this solve a real player problem?
- Are we building what players want, or what we think they want?
- Would we be proud to show this to our players?

**Example**: When deciding between two features, choose the one that delivers more player joy, even if it's harder to implement.

### 2. Long-term over Short-term

**Question**: "Will this decision be good in 5 years?"

Clash of Clans launched in 2012. Hay Day still generates revenue 10+ years later.

**In Practice**:
- Short-term metrics spikes that hurt long-term trust are forbidden
- Don't sacrifice player trust for quarterly revenue
- Build systems that last, not hacks that work today
- Think about the 10-year arc of the game

**Example**: A monetization feature might boost revenue 20% this quarter but damage player trust. Kill it.

### 3. Quality over Speed

**Question**: "Is this good enough for our players?"

"Good enough" means "would we be proud to show this to our families?"

**In Practice**:
- Rushing to meet a deadline is NEVER acceptable if it compromises quality
- Players remember bad launches; they don't remember delayed launches
- Polish is not optional
- If it's not excellent, it's not done

**Example**: Clash Royale was delayed multiple times to get the quality right. The result: $1B+ first year.

### 4. Team Health

**Question**: "Is this sustainable for the team?"

No crunch culture. Burned-out teams make bad games.

**In Practice**:
- If the team can't maintain this pace indefinitely, it's too fast
- Sustainable pace > heroic sprints
- Team morale is a leading indicator of product quality
- Protect your team from burnout

**Example**: If a feature requires 3 months of crunch, find another way or kill the feature.

### 5. Business Last

**Question**: "Does this make financial sense?"

Revenue is a RESULT of doing the above right, not a primary goal.

**In Practice**:
- "Player first, business last" is literal, not metaphorical
- Revenue optimization that hurts player experience is forbidden
- Build player trust first; revenue follows
- Sustainable businesses are built on sustainable player relationships

**Example**: A feature might generate $10M but violate player trust. The long-term cost is higher than the short-term gain.

---

## The Cell Autonomy Contract

### What Cells CAN Decide

**Creative Decisions**:
- Game direction and creative vision
- Feature prioritization and roadmap
- Art style and visual direction
- Game mechanics and systems design
- Story and narrative (if applicable)

**Technical Decisions**:
- Technology stack and tools
- Architecture and infrastructure
- Platform priorities (iOS vs. Android)
- Development methodologies

**Business Decisions**:
- Monetization strategy (within ethics guidelines)
- When to kill or continue projects
- Soft launch timing and markets
- Marketing and community approach

**People Decisions**:
- Team composition and hiring
- Role definitions within the cell
- Work schedule and pace
- Team culture and norms

### What Cells CANNOT Decide

**Company-Wide Strategy**:
- Platform strategy (console, PC, new platforms)
- Corporate M&A decisions
- Major IP licensing deals
- Company-wide technology standards
- Office location changes

**Cross-Cell Coordination**:
- Shared technology platforms
- Company-wide marketing campaigns
- Corporate partnerships

### What Cells MUST Report

**Player Metrics** (weekly):
- D1, D7, D30 retention
- DAU, MAU, sessions per player
- Monetization (ARPDAU, conversion)
- App Store ratings and reviews

**Business Metrics** (monthly):
- Revenue and profit
- User acquisition costs (CPI, LTV)
- Market performance vs. targets

**Team Health** (ongoing):
- Morale and engagement
- Turnover risk
- Burnout indicators

**Major Risks** (immediate):
- Technical risks
- Market risks
- Competitive threats
- Team issues

---

## Decision-Making Process

### Day-to-Day Decisions

Most decisions are made by individuals or small groups within the cell:

```
Individual Decisions:
├── Code implementation details
├── Art asset creation
├── Bug fixes and priorities
└── Daily task prioritization

Pair/Group Decisions:
├── Feature design details
├── Technical architecture
├── UI/UX decisions
└── Balance tuning

Cell-Wide Decisions:
├── Major feature additions
├── Roadmap changes
├── Kill/Continue decisions
├── Hiring decisions
└── Budget allocation
```

### The Kill/Continue Decision Process

See [SOP 3: Soft Launch Decision](12-sop-softlaunch.md) for detailed process.

High-level steps:
1. Data presentation (objective metrics)
2. Team sentiment (subjective passion)
3. External feedback (other cells)
4. Game Lead decision
5. Immediate execution

### Conflict Resolution

When team members disagree:

1. **Reframe**: Both want the same outcome—a great game
2. **Player Test**: Frame positions in player value terms
3. **Apply Hierarchy**: Use the 5-tier decision framework
4. **Decide**: Game Lead makes final call
5. **Align**: Team commits to decision and executes

### Escalation

Supercell has minimal escalation paths:

- Most decisions: Made within the cell
- Cross-cell issues: Discussed directly between cells
- Company-wide issues: CEO or leadership team

**Principle**: If you're asking for permission, you're not thinking autonomously enough.
