---
name: jobs-to-be-done
display_name: Jobs-to-be-Done (JTBD)
author: wdavidturner
version: 1.0.0
quality: expert
difficulty: intermediate
category: product
tags: [product-management, customer-research, discovery, jtbd, user-interviews]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Apply Jobs-to-be-Done framework for customer discovery and product strategy. Triggers: "JTBD",
  "jobs to be done", "customer interviews", "why customers churn", "hire and fire products",
  "find real competitors". Returns: job statements, four-forces analysis, true competitive set.
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Jobs-to-be-Done (JTBD)

## What It Is

Jobs-to-be-Done is a framework for understanding customer motivation. The core insight: **people don't buy products, they hire them to make progress in their lives.**

When someone buys a product, they're not buying features or benefits—they're hiring that product to do a job. Understanding that job unlocks everything: positioning, messaging, feature prioritization, and competitive strategy.

The key shift: Move from asking "What do customers want?" to asking "What progress are customers trying to make?"

## When to Use It

Use JTBD when you need to:

- **Understand why customers buy** (not just what they buy)
- **Discover your true competitive set** (often not who you think)
- **Find product-market fit** for a new product or feature
- **Improve positioning and messaging** that resonates
- **Reduce churn** by understanding why customers leave
- **Prioritize your roadmap** based on real customer progress
- **Identify new market opportunities** through struggling moments

## When Not to Use It

- There's no real customer choice (e.g., employer-mandated software)
- The purchase is pure habit with no conscious decision
- You want to validate a hypothesis you've already decided on

## Patterns

Common mistakes and the correct approach. Full pattern files: [source repo](https://github.com/wdavidturner/product-skills/tree/main/skills/jobs-to-be-done/patterns).

### Critical (get these wrong and you've wasted your time)

| Pattern | What It Teaches |
|---------|-----------------|
| interview-asking-why | Don't ask "why did you buy" — ask "walk me through what happened" |
| job-statement-too-broad | "Save time" is useless — needs context + motivation + outcome |
| missing-forces | Analyze all four forces, not just Push and Pull |
| interviewing-prospects | Only interview people who already switched |
| conference-room-jtbd | You can't hypothesize jobs without talking to customers |

### High Impact

| Pattern | What It Teaches |
|---------|-----------------|
| wrong-competitors | Your real competitors are what customers do *instead* |
| clustering-vs-segmenting | Find pathways, don't segment by demographics |
| complaints-arent-jobs | "Bitching ain't switching" — complaints don't predict action |
| reducing-friction | Sometimes lowering anxiety beats adding features |
| context-changes-everything | Same person, different context = different job |
| getting-past-pablum | First answers are generic — push 2-3 questions deeper |
| milkshake-story | The classic example: same product, multiple jobs |

### Medium Impact

| Pattern | What It Teaches |
|---------|-----------------|
| three-energies | Address Functional, Emotional, and Social — all three matter |
| following-power-users | Power users will lead you away from what scales |

## Core Framework

**The Four Forces of Progress:**

| Force | Direction | Definition |
|-------|-----------|------------|
| **Push** | Away from old | Dissatisfaction with current situation |
| **Pull** | Toward new | Attraction to the new solution |
| **Anxiety** | Against switch | Fear and uncertainty about the new solution |
| **Habit** | Against switch | Attachment to the current way of doing things |

A customer switches when Push + Pull > Anxiety + Habit.

**Job Statement Format:**
```
When [situation/context],
I want to [motivation / make progress],
So I can [desired outcome / avoid consequence].
```

Bad: "Save time managing tasks"
Good: "When I'm leading a sprint with 4 engineers and things are slipping, I want to know exactly what's blocked and who owns it, so I can run a 15-minute standup without surprises."

**True Competitors:**
Your real competitors are everything a customer considers doing instead — including spreadsheets, hiring someone, doing nothing, or a completely different category of product.

## Resources

**Books:**
- *Demand-Side Sales* by Bob Moesta — the tactical method
- *Competing Against Luck* by Clayton Christensen — the theory
- *When Coffee and Kale Compete* by Alan Klement — accessible introduction

**Other:**
- *Never Split the Difference* by Chris Voss — interview techniques that complement JTBD research
- *The End of Average* by Todd Rose — why demographic segmentation fails

---

## Attribution

**Original Author:** David Turner ([@wdavidturner](https://github.com/wdavidturner))
**Source Repository:** https://github.com/wdavidturner/product-skills
**License:** MIT License — Copyright (c) 2025 David Turner
**Imported:** 2026-03-19

Special thanks to David Turner for open-sourcing this collection of product management frameworks inspired by Lenny's Podcast guests. The full pattern files with worked examples are available in the source repository.
