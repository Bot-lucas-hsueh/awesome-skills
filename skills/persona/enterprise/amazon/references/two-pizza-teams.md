# Two-Pizza Teams & Single-Threaded Leadership

> Sources: *Working Backwards* by Colin Bryar & Bill Carr; Amazon re:Invent talks

---

## The Two-Pizza Rule

**Definition:**
> Any team should be small enough to be fed with two pizzas (8-10 people).

**Origin:**
Jeff Bezos introduced this rule in the early 2000s as Amazon scaled rapidly. The goal was to maintain startup-like agility as the company grew beyond thousands of employees.

---

## Key Characteristics

### 1. Small Size
- **8-10 people maximum**
- Cross-functional when possible (engineering, product, design)
- Small enough for high-bandwidth communication

### 2. Autonomous
- Minimal dependencies on other teams
- Can make decisions without extensive coordination
- "You build it, you run it" ownership

### 3. Single-Threaded
- One clear mission or goal
- Not pulled in multiple directions
- Clear definition of success

### 4. API-Driven Communication
- Interact with other teams through documented interfaces
- No ad-hoc requests or side channels
- Service-oriented architecture enables team autonomy

### 5. End-to-End Ownership
- Own the complete lifecycle: design → build → deploy → operate
- Direct pager duty for production issues
- No handoffs to "operations teams"

---

## Single-Threaded Leadership (STL)

**The Evolution:**
While two-pizza teams were the starting point, Amazon evolved to emphasize **single-threaded leadership** as the more fundamental concept.

**Definition:**
> A Single-Threaded Leader (STL) is a leader who owns one major initiative and has no other responsibilities.

**Jeff Bezos:**
> "The best way to fail at inventing something is by making it somebody's part-time job."

**Characteristics of an STL:**
- Has no other competing priorities
- Wakes up every day thinking about ONE initiative
- Is fully accountable for success or failure
- Leads a separable, autonomous team
- Can be any level (not just senior leaders)

### Examples of Single-Threaded Leadership

| Initiative | STL Responsibility |
|------------|-------------------|
| AWS EC2 | One leader owned compute services from concept to scale |
| Kindle | One leader owned e-reader business end-to-end |
| Amazon Prime | One leader owned membership program creation |
| Fulfillment by Amazon | One leader owned seller fulfillment service |
| Alexa | One leader owned voice assistant platform |

---

## Separable, Single-Threaded Teams

**Separable:**
> Almost as separable organizationally as APIs are for software.

**Key Requirements:**
1. **Clear ownership boundaries** — What this team owns vs. others
2. **Minimal organizational dependencies** — Can build/deploy without extensive coordination
3. **Self-contained mission** — Doesn't require other teams to succeed

**Benefits:**

| Benefit | Mechanism | Outcome |
|---------|-----------|---------|
| **Speed** | Fewer coordination costs | Faster decision making |
| **Ownership** | Clear accountability | Higher quality |
| **Innovation** | Autonomy to experiment | More creative solutions |
| **Scale** | Replicable structure | Organic growth capability |
| **Agility** | Small teams pivot faster | Better market responsiveness |

---

## The API Mandate (2002)

**Jeff Bezos's Famous Email:**

> 1. All teams will expose their data and functionality through service interfaces.
> 2. Teams must communicate with each other through these interfaces.
> 3. No other interprocess communication allowed: no direct linking, no direct reads of another team's data store, no shared-memory model, no back-doors. The only communication allowed is via service interface calls over the network.
> 4. It doesn't matter what technology they use.
> 5. All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers outside the company. No exceptions.
> 6. Anyone who doesn't do this will be fired. Thank you; have a nice day!

**Impact:**
- Enabled AWS (APIs were already built to be externalized)
- Created team autonomy through clear interfaces
- Reduced coordination overhead
- Forced clear thinking about service boundaries

---

## Organizational Evolution

### Phase 1: Early Two-Pizza Teams (2000s)
- Teams evaluated by "fitness functions"
- Required multidisciplinary leaders (rare)
- Strict 8-10 person limit

### Phase 2: Matrix Model
- Product managers + engineering managers
- More scalable leadership model
- Still small, autonomous teams

### Phase 3: Single-Threaded Leadership
- Focus on one leader, one goal
- Team size flexible based on need
- Separability more important than size

### Current State (2025)
- STL model is primary organizing principle
- Two-pizza size is guidance, not rule
- Emphasis on reducing dependencies
- Bureaucracy reduction initiatives ongoing

---

## Team Mitosis

**The Problem:**
Teams tend to grow over time. When they exceed effective size, they slow down.

**The Solution:**
> Team mitosis — When a team gets too large, split it into two teams with clear separation.

**How It Works:**
1. Identify natural fault lines in the team's responsibilities
2. Create two separable missions
3. Assign Single-Threaded Leaders to each
4. Split the team based on skills/interests
5. Define clear interfaces between the new teams

**Example:**
- Original: "Search Team" (20 people)
- Mitosis: "Product Search Team" + "Query Understanding Team"
- Interface: Query classification API

---

## Away Team Model

**The Problem:**
Team A needs a feature from Team B, but Team B has other priorities.

**The Solution:**
> Away team — Team A embeds engineers in Team B temporarily to build what they need.

**Rules:**
1. Away team members follow host team's processes
2. Code must meet host team's quality bar
3. Away team maintains their feature after launch
4. Time-boxed engagement (usually 3-6 months)

**Benefits:**
- Unblocks dependencies
- Builds cross-team relationships
- No permanent organizational changes

---

## Tolerate, Then Eliminate Duplication

**Amazon Principle:**
> "Prefer two solutions than none, one is better than two."

**The Idea:**
- When teams need similar capabilities, let them build independently first
- Don't force premature standardization
- Over time, best solution emerges
- Then consolidate on the winner

**Example:**
- Multiple teams built internal caching solutions
- Eventually ElastiCache (managed Redis/Memcached) emerged as standard
- Teams migrated to shared service

---

## "Communication is Terrible"

**Amazon Principle:**
> Communication is a sign of organizational dysfunction. Teams should communicate through well-defined APIs, not meetings and status updates.

**What This Means:**
- Well-designed interfaces reduce need for coordination
- Documentation replaces meetings
- Self-service tools replace human processes
- Teams should be autonomous, not interdependent

---

## Decision Rights

**Type 1 vs Type 2 Decisions:**

| Type | Definition | Who Decides |
|------|------------|-------------|
| **Type 1 (One-Way Door)** | Irreversible or costly to reverse | Senior leadership |
| **Type 2 (Two-Way Door)** | Easily reversible | Team decides |

**Amazon's Rule:**
- 90% of decisions are Type 2
- Teams should have authority over Type 2 decisions
- Don't let the 10% slow down the 90%

---

## Measuring Team Health

### Input Metrics (Controllable)
- Deployment frequency
- Lead time for changes
- Change failure rate
- Mean time to recovery
- Customer contact rate

### Output Metrics (Results)
- Customer satisfaction
- Feature adoption
- System availability
- Revenue impact

### Team Health Indicators
- On-call burden distribution
- Documentation completeness
- Cross-team dependency count
- Employee engagement scores

---

## Challenges and Adaptations

### Challenge: Coordination Complexity
**Problem:** With hundreds of teams, coordination becomes difficult.
**Solution:** Bar Raiser program; clear interfaces; well-defined ownership boundaries.

### Challenge: Inconsistent Customer Experience
**Problem:** Autonomous teams create inconsistent UX across Amazon.
**Solution:** Design systems; customer experience principles; centralized UX review for customer-facing changes.

### Challenge: Career Path Ambiguity
**Problem:** Flat team structure creates unclear advancement paths.
**Solution:** Dual ladder (engineering vs management); clear level expectations (L4-L10+).

### Challenge: Bureaucracy Creep
**Problem:** As Amazon grew, process accumulated.
**Solution:** Andy Jassy's "bureaucracy mailbox" — 1,000+ employee submissions, 375+ changes made (2024-2025).

---

## Leadership Principles Connection

| Principle | How Two-Pizza Teams Enable It |
|-----------|------------------------------|
| **Ownership** | Clear end-to-end accountability |
| **Bias for Action** | Fewer dependencies = faster decisions |
| **Invent and Simplify** | Autonomy to experiment |
| **Dive Deep** | Small teams know their domain intimately |
| **Deliver Results** | Clear metrics and accountability |
| **Frugality** | Small teams accomplish more with less |

---

## Summary

**Two-Pizza Teams + Single-Threaded Leadership =**
- High-velocity innovation at scale
- Clear ownership and accountability
- Reduced coordination overhead
- Entrepreneurial culture in large organization

**Key Takeaway:**
> It's not about the pizza. It's about separability, autonomy, and single-threaded focus.

---

*Last Updated: 2026-03-21*
