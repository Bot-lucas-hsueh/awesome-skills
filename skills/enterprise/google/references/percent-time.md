# 20% Time at Google

> How Google cultivates innovation through structured autonomy

## Philosophy

Google's 20% time policy — often credited to co-founder Larry Page — gives engineers **one day per week** to work on projects unrelated to their core responsibilities. The policy's purpose is not productivity recovery, but **genuine exploration**: time to build things that might not exist otherwise, driven by individual curiosity and user empathy.

The key tension: 20% time is **not** 100% time with extra steps. It's not a slush fund for personal productivity disguised as company work. It requires genuine user impact, honest reporting, and alignment with the company's mission — otherwise it becomes a distraction that hurts team velocity without generating value.

## Historical Impact

| Project | Origin | Revenue/Impact |
|---------|--------|---------------|
| **Gmail** | Paul Buchheit's 20% project (2004) | $80B+ annual Google Workspace revenue |
| **Google News** | Krishna Bharat's 20% project (2003) | 1B+ readers, news indexing standard |
| **AdSense** | Technology from 20% explorations | $20B+ annual revenue |
| **Google Suggest** | 20% autocomplete feature | Core to Search UX globally |
| **Google Transit** | Public transit directions | Integrated into Maps worldwide |
| **Material Design** | Cross-product design system | Adopted by millions of apps |

The common thread: every successful 20% project solved a **genuine user pain** that wasn't being addressed by core teams, and the creator had both the autonomy to build and the data to prove it worked.

## The "10× Test"

Before starting a 20% project, apply the **10× test**:

```
Is this project trying to improve something by 10×, not 10%?

Example: Gmail didn't improve email by 10%.
It introduced: 1GB storage (vs 2-4MB competitors),
search-native design, and threading — each a 10-100× improvement.
```

**Questions to answer before starting:**
1. Who is the user and what is their pain? (Specific persona, not "users")
2. What is the 10× improvement? (Quantitative, not "better experience")
3. How does this connect to Google's mission?
4. What is the smallest thing I can build to test the hypothesis?
5. How will I know if it's working? (Metrics defined upfront)

## Project Lifecycle

### Phase 1: Discovery (2-4 weeks)

**Activities:**
- User research: interviews, surveys, or data analysis
- Competitive landscape: what exists today?
- 10× framing: what would make this worth doing?
- Prototype: smallest viable thing to test the idea

**Output:** One-page proposal with:
- User problem and evidence
- 10× improvement hypothesis
- Prototype results (dogfood or small user test)
- Alignment to team/org OKR

**Done Criteria:** Data from at least 10 users (internal or external) showing interest

### Phase 2: Active Development (4-12 weeks)

**Time Budget:**
- Default: 1 day/week (20% of time)
- Sprint exception: With manager approval, can sprint full-time for 2-4 weeks
- Total exception: "120% projects" require evidence of prior impact

**Principles during development:**
- **Minimal viable ask**: Don't ask for a team; build it yourself first
- **Leverage existing infrastructure**: Reuse existing APIs, design systems, storage
- **Dogfood early**: Get it in front of internal users within 2 weeks of starting
- **Track metrics**: Log usage, engagement, satisfaction from day 1
- **Be honest about progress**: "Still exploring" is valid; "it's almost done" is not

**Common failure modes:**
- Building in secret for 3 months → no feedback loop
- Asking for resources before proving concept → denied
- Scope creep → never ships
- No metrics tracking → can't demonstrate impact

### Phase 3: Graduation (Ongoing)

**Path A: Product Integration**
- If metrics show clear user value → pitch to relevant product team
- Pitch must include: user evidence, alignment to their OKR, minimal eng ask
- Example: "I built this for 500 internal users. Here's the data. It ladders to your Q3 KR. I need one backend engineer for 6 weeks to productionize."

**Path B: Open Source**
- If product fit is unclear but technology is valuable → open source
- Example: Libraries, tools, infrastructure components
- Benefit: Builds external reputation, attracts talent

**Path C: Sunset**
- If data doesn't support continuation → document learnings, move on
- "I learned that X doesn't work because of Y" is a valid 20% outcome
- Abandoned projects are not failures if learnings are captured

## The Modern Evolution: 120% Time

As Google's scale grew, so did the scrutiny on 20% time. By the 2010s, the policy was informally rebranded as **"120% time"** in some teams — meaning you need a track record of **delivering on core OKRs before spending time on exploration**. This isn't a punishment; it's a recognition that:

1. **Core work creates the capacity for exploration.** A team that misses its OKRs can't afford 20% time.
2. **Impact at scale requires coordination.** A feature serving 1B users needs more than one engineer.
3. **The best 20% projects come from people who understand 100% work first.** You need to know the system's constraints to know where to push.

**120% time in practice:**
- Quarter 1: Deliver core OKR with high quality
- Quarter 2: With proven impact, spend 20% on adjacent exploration
- Quarter 3: If exploration shows promise, negotiate partial reallocation
- Quarter 4: Either integrate into core or sunset

## Proposal Template

```markdown
# 20% Project Proposal: [Name]

## User Problem
[1-2 sentences. Specific user, specific pain. Data or evidence supporting this.]

## 10× Hypothesis
[What is the 10× improvement over current state?
Quantitative if possible: "search time: 5 min → 30 sec"]
[What is the 10× improvement over alternatives?
"Other solutions cost $X; this is free/integrated"]

## Connection to Mission
[How does this accelerate "organize the world's information" or "make it universally accessible"?]

## Current Progress
[What have you built? Screenshots/data]
[Who has tested it? What did they say?]

## Metrics
| Metric | Current | Target | How Measured |
|--------|---------|--------|--------------|
| [Metric 1] | [Value] | [Value] | [Method] |

## Resource Ask
[What do you need to productionize?
Be specific: "1 backend engineer for 6 weeks" vs. "a team"]

## Timeline
- Week 1-2: [Deliverable]
- Week 3-4: [Deliverable]
- Week 5-6: [Productionize or pitch]

## Alignment to OKR
[Which team OKR does this ladder to? Which KR?]
```

## Anti-Patterns

| ❌ Wrong | ✅ Right |
|---------|---------|
| "I'll work on my side project 20% of the time" without telling anyone | Announce early; get feedback; align with team |
| Building for 3 months in secret | Ship something small within 2 weeks; iterate |
| "It's almost done" as status update | Share metrics: "30 users, 40% weekly retention" |
| Asking for a team before proving concept | Build alone first; prove it; then ask for resources |
| Pretending 20% is actually 100% | Be honest; managers can only help if they know the real allocation |
| Complaining about not having time | Either negotiate time explicitly or don't do it |
| No metrics tracking | Track everything from day 1; you need data to graduate |
| "This is for me" framing | Reframe: "This solves X for users Y" |

## References

- [How Google Works](https://www.amazon.com/How-Google-Works-Eric-Schmidt/dp/1455582344) — Eric Schmidt, Jonathan Rosenberg
- [In the Plex](https://www.amazon.com/In-Plex-Note-Eighteen-Looking/dp/1416596582) — Steven Levy
- Google's original 20% policy: [blog post on culture](https://abc.xyz/investor/other/annual-reports.html)
