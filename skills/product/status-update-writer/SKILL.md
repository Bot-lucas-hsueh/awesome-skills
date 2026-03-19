---
name: status-update-writer
display_name: Status Update Writer
author: aakashg
version: 1.0.0
quality: expert
difficulty: beginner
category: product
tags: [product-management, communication, stakeholders, writing, reporting]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Convert messy notes into precise stakeholder status updates. Triggers: "write a status update",
  "weekly update", "stakeholder update", "project update", "status report", "write a QBR".
  Calibrates for audience (CEO/VP/board) and cadence (daily/weekly/monthly/QBR).
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Status Update Writer

## Trigger

Activate when the user asks to "write a status update", "weekly update", "stakeholder update", "write a project update", or "status report".

## Behavior

### Step 1: Gather Context

Ask:
1. What project or initiative is this for?
2. What happened this week? (Paste notes, Slack messages, whatever you have — the messier the better)
3. Who is the audience? (CEO, VP Eng, cross-functional team, skip-level, board)
4. Is there bad news? (If so, I'll help you frame it with a mitigation plan)

If the user pastes raw notes, Slack threads, or bullet points, extract and structure the information directly. Never ask the user to organize it first.

### Step 2: Write the Update

Follow this exact structure:

---

**TL;DR** (2 sentences max)
The entire update if they read nothing else. Lead with the single most important thing. Bad news goes here, not buried below.

**Status: [pick one]**
- **On Track** — shipping on schedule, no blockers
- **At Risk** — potential issues that need visibility, with mitigation plan
- **Blocked** — cannot proceed without a decision or action from someone specific

**Progress This Week**
- What actually shipped or completed — never what was "worked on"
- Be specific: "Shipped new onboarding flow to 10% of users" not "Made progress on onboarding"
- Include links to PRs, docs, demos, or dashboards when provided
- Call out milestones explicitly

**Next Week**
- What's planned, with owners where known
- Highlight dependencies on other teams or decisions
- If something needs to happen by a specific date, make the deadline visible

**Risks & Blockers**
- Every risk gets: description, likelihood, impact, mitigation plan
- Every blocker gets: what's blocked, who can unblock it, by when
- If there are none, write "None currently." Never fabricate risks to fill the section

**Decisions Needed** (include only if applicable)
- State exactly what needs to be decided
- Who needs to decide it
- By when
- Enough context for the reader to decide without scheduling a meeting
- Always include a recommendation: "I recommend Option A because..."

**Metrics** (include only if applicable and the user provides data)
- Key metric: current value vs. target, trend, brief interpretation
- Only include metrics that tell a story

---

### Step 3: Tone Calibration

Adjust content and depth based on audience:

| Audience | Focus On | Leave Out |
|----------|----------|-----------|
| **CEO / C-suite** | Outcomes, metrics, strategic implications | Implementation details, technical decisions |
| **VP / Director** | Progress against milestones, risks, resource needs | Code-level details, day-to-day tasks |
| **Cross-functional** | Dependencies, timeline impacts, what they need to know | Internal team dynamics, technical debt |
| **Engineering lead** | Technical blockers, architecture decisions, velocity | Business context they already know |
| **Skip-level** | Your team's impact, growth, wins | Minutiae that your direct manager handles |
| **Board** | Metrics, trajectory, market context | Everything operational |

### Formatting Rules

- Total update: under 200 words. Longer means too much detail for the audience.
- No filler. "We continued to make progress on..." — state what was done.
- Bad news goes above the fold, not buried at the bottom. Always pair bad news with a mitigation plan.
- Active voice. "Team shipped the migration" not "The migration was completed."
- Use parallel structure in bullet points. Start each with a verb.

## Adapting by Cadence

**Daily Standup / Async Daily** — 3 lines max:
```
Yesterday: [what shipped]
Today: [what's happening]
Blocked: [any blockers, or "None"]
```

**Weekly Update** — default format above. Target 150-200 words.

**Monthly Update** — same structure but zoom out: progress against monthly goals, not daily tasks. Add metric trends ("WAU grew from 130K to 142K, +9%"). Target 300-500 words.

**QBR (Quarterly Business Review)**:
- Lead with OKR scorecard: each KR with target vs. actual and red/yellow/green status
- Add "Key Decisions Made" section — what big bets were placed and early results
- Add "Lessons Learned" — 2-3 things that would change if you could rerun the quarter
- Forward-looking: next quarter's top 3 priorities with success criteria
- Target: 500-800 words. Use tables for OKR scorecards and metric summaries.

When the user doesn't specify cadence, default to weekly.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Hiding bad news at the bottom | Stakeholders lose trust when they discover you buried the lead | Bad news is in the TL;DR, always |
| Confusing activity with progress | "Had 6 meetings" is activity; "Migrated 40% of users" is progress | Report outcomes, not effort |
| Weasel words ("roughly on track") | Signal uncertainty and hide facts | Be precise; if unknown, say "investigating, update by [date]" |
| Including everything | VP does not need to know about a refactored utility function | Match depth to audience |
| No action items | Reader doesn't know what to do | Every update makes clear what you need from the reader |
| Passive voice to avoid ownership | "The deadline was missed" dodges accountability | "We missed the deadline because X. Recovery plan: Y" |

## Rules

- Never fabricate progress or inflate status. If behind, say so with a plan.
- Never hide bad news. Surface it early, pair it with mitigation.
- Every item must pass the "so what?" test. If it does not matter to this audience, cut it.
- Always include a recommendation with decisions. Never make the reader do the analysis.
- Match depth to audience. Board updates have no technical details. Eng lead updates have no business platitudes.

---

## Attribution

**Original Author:** Aakash Gupta ([@aakashg](https://github.com/aakashg))
**Source Repository:** https://github.com/aakashg/pm-claude-skills
**License:** MIT License — Copyright (c) 2026 Aakash Gupta
**Imported:** 2026-03-19

Special thanks to Aakash Gupta for open-sourcing this pragmatic product management skills collection. More context on how these skills were built: [Aakash's newsletter](https://www.news.aakashg.com/p/steal-6-of-my-claude-skills).
