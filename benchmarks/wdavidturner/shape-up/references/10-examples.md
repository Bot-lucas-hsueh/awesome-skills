# Shape Up — Real-World Scenarios

---

## Scenario 1: Shaping a New Feature

**Context:**
A SaaS company wants to add "notifications" to their product. Currently vague, no specifics.

### User Input
> "We want to add notifications to our app. How should we shape this?"

### Expert Response
> "Let's not start with 'add notifications.' That's a solution in search of a problem.

**First: What's the problem?**

When you say 'notifications,' I need to know:
- Who is frustrated?
- When are they frustrated?
- What are they trying to do that they can't?

**Example:** Let's say your app is a project management tool. A specific problem might be:
> 'When I'm waiting for a client to approve a deliverable, I have to manually check the app every few hours to see if they've commented. I want to know immediately when there's activity on my stuff, so I can respond quickly and keep projects moving.'

See the difference? That's a specific problem. 'Add notifications' is a feature request.

**Now let's shape it:**

### Step 1: Set Appetite
Is this a small batch (1-2 weeks, 1 person) or big batch (6 weeks, 1-3 people)?

Given 6 weeks for a new notification system (infrastructure + UI + preferences), this is likely a **big batch**.

### Step 2: Narrow the Problem
A 6-week notification feature could include:
- In-app notifications
- Email notifications
- Push notifications
- Notification preferences
- Notification history

Too much. **Narrow it down:**

> For this cycle, we'll solve: "Notify users when something they own or are watching gets updated."

Email + in-app. Push deferred. Preferences: just on/off. History: deferred.

### Step 3: Fat Marker Sketch
```
[Screen: Notification Bell]
[Dropdown: "3 new notifications"]
  - "Sarah commented on 'Q1 Report'"
  - "Client approved 'Logo Final'"
  - "Task 'Banners' marked complete"
[Click takes to notification details]
```

No full wireframes. Just enough to show:
1. Where notifications appear
2. What's in the dropdown
3. What happens when clicked

### Step 4: Rabbit Holes
- **Email deliverability** — Don't build an email system from scratch. Use SendGrid/Postmark.
- **Real-time websockets** — Don't build live updates. Poll every X minutes.
- **Notification preferences** — Skip granular settings. Just on/off.

### Step 5: No-Gos
- Push notifications (deferred)
- Notification history/dismissal (deferred)
- Email digests/summaries (deferred)
- @mentions in notifications (deferred)

---

## Scenario 2: Scope Creep Mid-Build

**Context:**
Team is 3 weeks into a 6-week build. PM wants to add "one small thing."

### User Input
> "While we're building the dashboard, can we also add dark mode? It's just a CSS change."

### Expert Response
> "In Shape Up, scope isn't free.

**Let me ask:**
1. What's the current appetite? [6 weeks, 2 people]
2. What's already committed in the pitch?
3. What will you cut to add dark mode?

You can't 'also add' without 'also subtract.'

**Options:**

| If you want... | Then you must... |
|----------------|------------------|
| Add dark mode | Cut something from the original scope to stay within 6 weeks |
| Keep full scope | Wait for next cycle and bet on dark mode then |
| It's critical | Trigger circuit breaker (only for true emergencies) |

**Let's look at the original pitch:**
> "Dashboard v2 includes: new layout, filter persistence, bulk actions, export"

**So:**
- Cut "bulk actions"? → Add dark mode
- Cut "export"? → Add dark mode
- Keep everything? → Dark mode waits

**What does the team recommend?**

---

## Scenario 3: Hill Chart Disagreement

**Context:**
Team reports "95% done" on a task, but it's been at "95%" for a week.

### User Input
> "The team says the data export feature is 95% done but it's not shipping. What's going on?"

### Expert Response
> "This is exactly what Shape Up tries to prevent.

**Common causes:**

1. **The task was never really defined** — "Build export" is a project, not a task. Team is still figuring out scope.

2. **"95% done" = "we're still on the hill"** — If they're still figuring out how to solve something, they're uphill. Don't report percentage.

**Hill Chart Rules:**
- **Uphill (0-50%)**: You don't know how to build it yet. No completion %.
- **Top of hill (50%)**: Unknowns resolved. Starting to execute.
- **Downhill (50-100%)**: Executing known solution. Can estimate % complete.
- **Done**: Shipped to production, not just "finished coding."

**Diagnosis Questions:**

| Question | What It Reveals |
|----------|-----------------|
| What's left? | Scope still unclear? |
| Can you ship today? | If no, not 95% done |
| What's blocking? | Real blockers vs. estimates |

**Fix:**
Move the dot back to where it actually is. If they're still figuring out how to handle large file exports, they're at 0% or 10% on the hill.

**Rule:** You can't be 95% done on something you're still figuring out.

---

## Scenario 4: Betting Table Dysfunction

**Context:**
Betting table is just a status update meeting. Nothing gets rejected. Everyone bets on everything.

### User Input
> "Our betting table is more like a sprint planning meeting. Everyone just takes work. No one says no. What's wrong?"

### Expert Response
> "That's not a betting table — that's a backlog shuffle.

**The betting table has one job:**

**THREE outcomes per pitch:**
1. **Bet** — "Yes, we're committing to this this cycle"
2. **Pass** — "Not this cycle, maybe next"  
3. **Shelf** — "Interesting, but not a priority right now"

**If everyone bets on everything, you don't have a betting table.**

**Root causes:**

| Cause | Fix |
|-------|-----|
| Too many pitches | Only bring 2-3 shaped pitches per cycle |
| Pitches are too vague | Fat marker sketches + rabbit holes required |
| No rejection culture | PM needs to say "not this cycle" |
| Leadership pressure | Exec support needed to protect no |

**The rule:**

> A pitch that gets bet on locks the team for 6 weeks. If you're not willing to say "no" to it, you're not using the appetite constraint.

**Better process:**

1. Present 2-3 pitches
2. For each pitch, team discusses: appetite fit, risks, unknowns
3. Vote: bet / pass / shelf
4. Sum bets ≤ available capacity
5. Announce who's building what

---

## Scenario 5: Team Too Small for Shape Up

**Context:**
Team of 2 developers wonders if Shape Up is worth the overhead.

### User Input
> "We're just a 2-person team. Is Shape Up overkill for us?"

### Expert Response
> "For 3 or fewer people: yes, formal Shape Up is probably overkill.

**When NOT to formalize:**
- Just talk to each other instead of meetings
- Skip the betting table ceremony
- Skip the pitch template
- But keep the core ideas:

| Keep | Skip |
|------|------|
| Fixed time cycles (work in 2-week chunks) | Betting table ceremony |
| Appetite over estimates | Formal pitch template |
| No scope creep | Hill Chart (for 2 people) |
| Kickoff clarity | Multiple hats/shaped work |

**The principles still apply even at small scale:**
- Don't estimate "how long" — decide "how much time"
- No adding scope mid-project
- Ship in chunks, not continuous trickles

**Once you hit 3 people, consider formalizing.**

---

## Scenario 6: Circuit Breaker Emergency

**Context:**
Critical bug found in production. Team is mid-cycle on a bet. What do?

### User Input
> "We found a critical security vulnerability mid-cycle. The team wants to stop everything and fix it. Is that allowed?"

### Expert Response
> "Yes — this is exactly what the circuit breaker is for.

**Key question:** Is this a true emergency?

| Emergency (Circuit Breaker) | Not Emergency |
|------------------------------|---------------|
| Security vulnerability | Feature not arriving fast enough |
| Data loss/corruption | Customer complaint |
| Service downtime | Scope creep request |
| Legal/compliance issue | PM changed their mind |

**The Rule:**
The circuit breaker is the ONLY exception to "no interruptions during the cycle."

**Process:**
1. Identify the circuit breaker event
2. Pause current bet work
3. Address the emergency (shortest path to safe)
4. Decide: Resume bet OR re-bet

**After:**
- Document what happened
- Review: Could this have been caught in shaping?
- If it's a pattern, revisit how work enters build

---

## Scenario 7: Unfinished Work Doesn't Roll Over

**Context:**
Cycle ends. The team didn't finish everything they bet on.

### User Input
> "We have half a feature incomplete at the end of the cycle. What do we do?"

### Expert Response
> "In Shape Up, unfinished work goes back to the betting table — it doesn't automatically roll over.

**The Rule:**
What doesn't ship stays in the queue. You re-bet on it next cycle.

**What happened:**
- Was the appetite wrong? (6 weeks wasn't enough)
- Were rabbit holes accurate? (were there unknowns you didn't flag?)
- Was there scope creep? (did something get added during build?)
- Did the team scope too much? (9 tasks was too many)

**Next cycle options:**

| Option | When |
|--------|------|
| Re-bet same scope | Scope is still valid, just not done |
| Rescope smaller | The original appetite was wrong |
| Abandon | Problem is no longer relevant |
| Split | Some shipped, some continues |

**Key:** No shame in unfinished work. It teaches you about sizing.

---

## Scenario 8: Shaping Without Engineering

**Context:**
PM shaped a feature solo. Engineering jumps in at build and finds major issues.

### User Input
> "Our PM does all the shaping work, then hands it off to us to build. We keep discovering problems mid-build."

### Expert Response
> "Shaping without engineering is the #1 mistake in Shape Up.

**Why does this fail?**

PMs don't know:
- What's technically hard vs. easy
- What dependencies exist
- What edge cases will surface
- How the system actually works

**The Fix:**

> Shaping requires: PM + Senior Engineer together.

**Shaping Sessions should have:**
- PM: problem focus, user context
- Senior Eng: technical reality, unknowns

**How to fix your process:**

1. No more PM-only shaping
2. Engineering joins at problem definition
3. Rabbit holes are identified WITH engineering
4. Appetite is set WITH engineering validation

**If engineering can't join:**
- At minimum, get engineering review before betting
- Better: dedicated shaping time with both
- Best: PM+Eng co-located during shaping

---

## Scenario 9: Pitch Too Abstract

**Context:**
Pitch says "Improve onboarding flow."

### User Input
> "The pitch just says 'improve onboarding.' We have no idea what to build."

### Expert Response
> "That's not a shaped pitch — that's a ticket.

**Bad Pitch Example:**
```
## Pitch: Improve onboarding

### Problem
Users aren't finishing onboarding.

### Solution
Make it better.
```

**Good Pitch Example:**
```
## Pitch: Reduce onboarding drop-off at step 3

### Problem
When users get to the "API key configuration" step (step 3 of 5), 
40% abandon. User interviews show: they don't understand what an 
API key is or why they need one.

### Appetite
Big batch: 6 weeks, 2 people

### Solution
[Fat marker sketch: simplified step 3 - "Connect your data" language]
- Replace "API key" with "Connect your database"
- Show visual of where to find key in their dashboard
- Skip optional for now, can configure later
- Add "Need help?" link to docs

### Rabbit Holes
- Don't build new database connection UI (use existing)
- Don't add OAuth (too complex for v1)
- Don't redesign steps 1-2 (scope creep)

### No-Gos
- Video tutorials
- Account wizard
- Email sequence
```

**Exercise:** Throw back any pitch where you can't draw a fat marker sketch of the solution.

---

## Scenario 10: Post-Mortem: What Didn't Ship?

**Context:**
Review phase. 2 of 3 bets didn't ship.

### User Input
> "We bet on 3 things this cycle. Only 1 shipped. What do we learn?"

### Expert Response
> "This is the most valuable data Shape Up gives you.

**Review Questions:**

| What didn't ship? | Why? | What does this teach? |
|-------------------|------|------------------------|
| Feature A | Underestimated complexity | Rabbit holes missed |
| Feature B | Scope creep | Need to renegotiate more |
| Feature C | Team distraction | Need to protect build time |

**Calibration:**

| Pattern | Teaching |
|---------|----------|
| 3 bets, 3 shipped | Appetite may be too conservative |
| 3 bets, 1 shipped | Appetite too aggressive OR too much scope creep |
| Same features never ship | Problem may have shifted |
| Different features miss | Team may struggle with unknowns |

**The learning:**
- Don't estimate better
- Size the appetite better
- Call rabbit holes more honestly
- Enforce scope discipline

**Key insight:**
> Unfinished work isn't failure — it's information about your sizing.