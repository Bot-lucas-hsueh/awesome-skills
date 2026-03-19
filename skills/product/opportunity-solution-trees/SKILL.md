---
name: opportunity-solution-trees
display_name: Opportunity Solution Trees (OST)
author: wdavidturner
version: 1.0.0
quality: expert
difficulty: intermediate
category: product
tags: [product-management, discovery, teresa-torres, continuous-discovery, ost]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Apply Opportunity Solution Trees (OST) by Teresa Torres to connect outcomes to customer needs.
  Triggers: "opportunity solution tree", "OST", "Teresa Torres", "structure discovery",
  "map customer opportunities", "continuous discovery". Returns: outcome-opportunity-solution tree.
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Opportunity Solution Trees (OST)

## What It Is

Use the Opportunity Solution Tree (OST) to connect a business outcome to the customer opportunities that drive it, then compare solutions and tests. The tree forces you to separate needs from ideas and keeps discovery tied to delivery.

## When to Use It

- Structure discovery around customer opportunities
- Tie customer needs to measurable outcomes
- Compare multiple solutions for the same opportunity
- Keep continuous discovery aligned with the roadmap
- Create a shared view of priorities with stakeholders

## When Not to Use It

- You are not doing customer research
- The solution is already decided
- The work is a commodity requirement with no real options
- You only need a quick one-off decision

## Patterns

Common mistakes and the correct approach. Full pattern files: [source repo](https://github.com/wdavidturner/product-skills/tree/main/skills/opportunity-solution-trees/patterns).

### Critical (get these wrong and you've wasted your time)

| Pattern | What It Teaches |
|---------|-----------------|
| opportunities-are-solutions | "Add a search bar" is a solution — the opportunity is what's hard about finding things |
| starting-with-solutions | Work backward from outcomes, not forward from feature ideas |
| skipping-outcome | Without a clear outcome, you can't evaluate which opportunities matter most |
| interviewing-for-facts | Collect stories, not preferences — needs emerge from what happened |
| conference-room-opportunities | You can't hypothesize opportunities without customer research |

### High Impact

| Pattern | What It Teaches |
|---------|-----------------|
| single-solution-thinking | Always compare at least 3 solutions for any opportunity |
| opportunities-too-big | "Make it easier to use" is not actionable — decompose into specific moments |
| flat-tree-structure | Opportunities should nest hierarchically from broad to specific |
| missing-experience-map | Structure opportunities around the customer journey, not internal categories |
| output-not-outcome | "Launch feature X" is an output — "Increase activation by 10%" is an outcome |
| solution-testing-whole-idea | Break solutions into assumptions and test the riskiest ones first |

### Medium Impact

| Pattern | What It Teaches |
|---------|-----------------|
| tree-not-updated | The OST is a living document — update it weekly as you learn |
| needs-not-heard | Train your ear to hear opportunities customers don't explicitly state |
| too-many-branches | Limit top-level opportunities to 5-7 for cognitive manageability |

## Core Structure

```
Outcome (measurable business result you own)
└── Opportunity 1 (customer need / pain / desire — from research)
    ├── Sub-opportunity 1a (decomposed, specific moment)
    │   ├── Solution A (one of ≥3 ideas)
    │   ├── Solution B
    │   └── Solution C → Experiment (test riskiest assumption)
    └── Sub-opportunity 1b
└── Opportunity 2
└── Opportunity 3 (max 5-7 at each level)
```

**Four node types:**
| Node | What It Is | Common Mistake |
|------|------------|----------------|
| **Outcome** | Measurable business result | Using output ("ship feature X") instead of outcome |
| **Opportunity** | Unmet customer need, pain, or desire | Writing solutions ("add search bar") as opportunities |
| **Solution** | One of ≥3 ideas addressing an opportunity | Exploring only one solution and calling it done |
| **Experiment** | Test of the riskiest assumption in a solution | Testing the whole solution instead of one assumption |

## How to Apply It

```
Step 1: Define a measurable outcome.
        → Not "ship the dashboard" — "increase week-2 retention from 40% to 55%"

Step 2: Map the customer journey to frame opportunity areas.
        → Acquisition → Activation → Retention → Referral → Revenue moments

Step 3: Capture opportunities from real interviews (stories, not preferences).
        → "Walk me through the last time you [experienced this journey]"
        → Hear: what was hard, what was frustrating, what they wished existed

Step 4: Organize opportunities hierarchically (broad → specific).
        → Max 5-7 at each level; decompose "make it easier to use" into specific friction moments

Step 5: Generate ≥3 solutions per high-priority opportunity.
        → Never evaluate just one solution; compare explicitly

Step 6: Test the riskiest assumption of the most promising solution first.
        → Prototype, fake door, concierge test — not full build

Step 7: Review and update the tree weekly.
        → OST is a living document, not a one-time artifact
```

## Resources

**Books:**
- *Continuous Discovery Habits* by Teresa Torres
- *Nudge* by Richard Thaler

**Online:**
- Product Talk: producttalk.org
- learn.producttalk.org

**Related Skills:**
- `jobs-to-be-done` — framework for capturing opportunities from interviews
- `product-manager` — PRD writing and RICE prioritization after OST maps the landscape

---

## Attribution

**Original Author:** David Turner ([@wdavidturner](https://github.com/wdavidturner))
**Source Repository:** https://github.com/wdavidturner/product-skills
**License:** MIT License — Copyright (c) 2025 David Turner
**Imported:** 2026-03-19
**Framework Credit:** Opportunity Solution Trees were created by Teresa Torres (producttalk.org).

Special thanks to David Turner for open-sourcing this collection of product management frameworks inspired by Lenny's Podcast guests. The full pattern files with worked examples are available in the source repository.
