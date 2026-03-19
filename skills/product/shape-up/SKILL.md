---
name: shape-up
display_name: Shape Up
author: wdavidturner
version: 1.0.0
quality: expert
difficulty: intermediate
category: product
tags: [product-management, development-methodology, planning, agile, basecamp]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Apply Shape Up methodology to escape estimate-driven development. Triggers: "shape up",
  "shaping session", "set an appetite", "scope without estimates", "betting table",
  "ship in fixed cycles". Returns: shaped pitches, appetite settings, scoped work.
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Shape Up

## What It Is

Shape Up is a product development methodology built on one core insight: **you cannot estimate your way to shipping—you must shape your way there.**

Traditional approaches ask "How long will this take?" and then try to hit that estimate. Shape Up flips this: decide upfront how much time you're willing to spend (the *appetite*), then shape a version of the solution that fits within that constraint.

The methodology emerged from 17 years of building Basecamp, where the founding team faced an unusual constraint: their only engineer (DHH) worked just 10 hours per week. This forced extreme clarity about what to build and ruthless scoping to ensure every hour counted.

**The key shift:** Move from "What's the estimate for this?" to "What version of this can we confidently ship in the time we're willing to spend?"

## When to Use It

Use Shape Up when you need to:

- **Stop projects from dragging** — work that should take weeks is taking months
- **Escape the estimate trap** — you're tired of estimates that are always wrong
- **Give teams real autonomy** — not just ticket execution
- **Reduce meeting overhead** — Scrum rituals are consuming your time
- **Ship meaningful chunks** — not just incremental tickets that don't add up to anything
- **Align product and engineering** — there's a wall between them today
- **Maintain startup speed** — as you scale past 30-50 people

## When Not to Use It

- **You're 3 people or fewer** — just talk to each other, formalization isn't needed yet
- **There's no real complexity** — simple tasks don't need shaping
- **You can't get engineering into shaping** — without technical input, shaping fails
- **Leadership isn't bought in** — you need exec support to protect build time
- **You're doing pure maintenance** — bug fixes don't need the full process

## Patterns

Common mistakes and the correct approach. Full pattern files: [source repo](https://github.com/wdavidturner/product-skills/tree/main/skills/shape-up/patterns).

### Critical (get these wrong and you've wasted your time)

| Pattern | What It Teaches |
|---------|-----------------|
| estimates-vs-appetite | Don't ask "how long?" — decide how much time you're willing to spend |
| unshaped-work | A Figma file or PRD is not shaped work — you need collaborative clarity |
| shaping-without-engineering | Shaping without a senior engineer is a recipe for blowups |
| ten-pound-bag | You can't put 10 pounds of scope in a 5 pound time box |
| fuzzy-problem | "Build a calendar" is not a problem — narrow it down first |

### High Impact

| Pattern | What It Teaches |
|---------|-----------------|
| too-abstract-shaping | Fat marker sketches must communicate the idea, not just be blurry wireframes |
| scope-hammering | Cut scope before you start, not when you're out of time |
| tickets-not-projects | Give teams whole projects, not shredded tickets |
| hill-chart-theater | Hill charts show real progress, not status theater |
| missing-kickoff | Builders must translate shaped work into 9 or fewer implementation scopes |
| cool-down-skipping | Teams need breathing room between cycles to reset |

### Medium Impact

| Pattern | What It Teaches |
|---------|-----------------|
| betting-table-dysfunction | Betting is a real commitment, not a backlog shuffle |
| junior-detail-dial | Adjust shaping detail based on who's building |
| circuit-breaker-fear | If it's not working, stop building and return to shaping |

## Core Concepts

**The Shape Up Cycle:**

```
6-week cycle:
├── Shaping (parallel, by senior PM+eng)
│   ├── Problem: narrow it down to a specific case
│   ├── Appetite: how much time are we willing to spend? (S/M/L)
│   ├── Solution: rough, not detailed; fat marker sketches
│   └── Rabbit holes: call out the unknowns and hard parts
├── Betting Table
│   ├── Bets are REAL commitments — not backlog reshuffling
│   ├── No interruptions during cycle (circuit breaker is the only exception)
│   └── Unfinished work doesn't automatically roll over
└── Building (by autonomous team)
    ├── Team scopes their own tasks from the shaped work
    ├── Progress tracked on Hill Charts (uphill = uncertainty, downhill = execution)
    └── No scope creep without renegotiating appetite
2-week cool-down:
└── No scheduled work — bugs, exploration, personal projects
```

**Appetite Sizes:**
| Appetite | Definition | Typical Use |
|---------|-----------|------------|
| **Small batch** | 1-2 weeks for 1 person | Bug fixes, small improvements |
| **Big batch** | 6 weeks for 1-3 people | New features, significant changes |

**A Pitch (shaped work) contains:**
1. **Problem** — specific scenario, not abstract statement
2. **Appetite** — S/M/L; this is the constraint, not an estimate
3. **Solution** — rough fat marker sketches; not full wireframes
4. **Rabbit holes** — what to avoid; hard parts to call out
5. **No-gos** — what is explicitly out of scope

## Resources

**Books:**
- *Shape Up* by Ryan Singer — the original free book at basecamp.com/shapeup
- *Competing Against Luck* by Clayton Christensen — Jobs-to-be-Done theory (for the discovery phase)

**Courses:**
- *Shaping in Real Life* — Ryan Singer's course on practical shaping

**Other:**
- Ryan Singer's website: ryansinger.co
- 37signals blog for ongoing insights

---

## Attribution

**Original Author:** David Turner ([@wdavidturner](https://github.com/wdavidturner))
**Source Repository:** https://github.com/wdavidturner/product-skills
**License:** MIT License — Copyright (c) 2025 David Turner
**Imported:** 2026-03-19
**Framework Credit:** Shape Up was created by Ryan Singer during his 17 years at Basecamp/37signals.

Special thanks to David Turner for open-sourcing this collection of product management frameworks inspired by Lenny's Podcast guests. The full pattern files with worked examples are available in the source repository.
