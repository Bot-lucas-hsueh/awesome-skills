---
name: idea-validator
display_name: Idea Validator
author: aakashg
version: 1.0.0
quality: expert
difficulty: beginner
category: product
tags: [product-management, validation, ideation, startup, discovery]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Stress-test product ideas across 5 dimensions before investing time to build. Triggers: "validate
  this idea", "is this idea good", "stress test this", "evaluate this product idea", "should I build X".
  Returns GO/ITERATE/STOP verdict with evidence-based reasoning and killer questions.
  Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
---

# Idea Validator

## Trigger

Activate when the user asks to "validate this idea", "is this idea good", "stress test this", "evaluate this product idea", or "should I build [X]".

## Behavior

### Step 1: Understand the Idea

Ask:
1. What's the idea in one sentence?
2. Who specifically has this problem? (Job title, company size, situation)
3. How are they solving it today?
4. Why are you the right person/team to build this?

If the user gives a vague answer to #2 (e.g., "everyone" or "businesses"), push back. Every viable idea has a specific first customer.

### Step 2: Run the Validation Framework

Score the idea across 5 dimensions. Rate each **Strong** / **Moderate** / **Weak** with 3-5 sentences of reasoning. Cite comparables, reference market data, and name assumptions explicitly.

**1. Problem Severity**

- Is this a hair-on-fire problem or a nice-to-have?
- How often do users encounter it? (Daily = strong, yearly = weak)
- What's the cost of the status quo? (Time, money, frustration, risk)
- Would they pay to solve this TODAY, or is it a "someday" problem?

| Rating | Criteria |
|--------|----------|
| **Strong** | Users encounter daily/weekly AND costs real time or money. Workarounds exist. |
| **Moderate** | Real problem but low frequency, or high frequency but low pain. Users cope. |
| **Weak** | Nice-to-have. Users don't actively seek solutions. No evidence of workarounds. |

**2. Market Evidence**

- Are people already paying for alternatives? What are they paying?
- What search volume, forum posts, Reddit threads, or support tickets exist?
- Is the market growing or shrinking? What's the tailwind?
- Are there adjacent markets that validate demand?

| Rating | Criteria |
|--------|----------|
| **Strong** | Multiple competitors with revenue. Growing market. Clear willingness to pay. |
| **Moderate** | Some competitors or adjacent products. Market exists but unclear size. |
| **Weak** | No competitors (usually bad, not good). No evidence of demand. |

**3. Solution Differentiation**

- Why would someone switch from their current solution to yours?
- What's the unique angle? (Faster, cheaper, simpler, better for a specific segment?)
- Is the differentiation defensible? (Network effects, data moat, expertise, integrations?)
- Can you explain the difference in one sentence?

| Rating | Criteria |
|--------|----------|
| **Strong** | Clear, defensible wedge. One-sentence why this wins for a specific segment. |
| **Moderate** | Differentiation exists but may not be durable. "Better UX" alone is moderate. |
| **Weak** | Me-too product. "We're like X but better." Cannot articulate the wedge. |

**4. Feasibility**

- Can a small team build an MVP in 4-6 weeks?
- What are the biggest technical risks?
- Does it require data, partnerships, or regulatory approval you don't have?
- What's the simplest version that delivers value?

| Rating | Criteria |
|--------|----------|
| **Strong** | MVP buildable in weeks with existing tools/APIs. No special data or partnerships needed. |
| **Moderate** | Buildable but requires one hard thing (a key integration, dataset, or specific hire). |
| **Weak** | Requires multiple breakthroughs, regulatory approval, or years of data collection. |

**5. Business Viability**

- How does this make money? What's the monetization model?
- What's the realistic willingness to pay? (Based on alternatives, not hope)
- What does the unit economics look like? (CAC vs. LTV rough estimate)
- Can this reach $1M ARR? What does that require? (X customers at $Y/month)

| Rating | Criteria |
|--------|----------|
| **Strong** | Clear monetization. Path to $1M ARR requires <1,000 customers. Healthy unit economics. |
| **Moderate** | Monetization plausible but unproven. Path to $1M ARR requires >5,000 customers. |
| **Weak** | Monetization is "figure it out later" or requires massive scale to work. |

### Step 2b: Quick Competitive Scan

Before scoring Market Evidence, run a rapid competitive scan.

**Present as a compact table:**

```
| Competitor/Alternative | Type     | Pricing | Est. Size | Key Weakness |
|------------------------|----------|---------|-----------|-------------|
| [Name]                 | Direct   | $X/mo   | [size]    | [gap]       |
| [Name]                 | Adjacent | Free    | [size]    | [limitation]|
| DIY (spreadsheet)      | Workaround | Free  | Common    | [pain point]|
```

If you genuinely lack data, say `[NEED: competitive research on X]` and score Market Evidence as **Moderate** at best.

Also run a **graveyard check**: have similar products been tried and failed? If so, why? A failed predecessor is not disqualifying, but the user must explain what has changed.

### Step 3: Verdict

Present a summary scorecard:

```
| Dimension                | Rating   |
|--------------------------|----------|
| Problem Severity         | [rating] |
| Market Evidence          | [rating] |
| Solution Differentiation | [rating] |
| Feasibility              | [rating] |
| Business Viability       | [rating] |
```

**Overall verdict:**
- **GO**: Strong across 4+ dimensions. Worth building an MVP now.
- **ITERATE**: Promising but 1-2 dimensions need work. Suggest specific pivots.
- **STOP**: Fundamental issues that pivoting won't fix. Explain why directly.

### Step 4: Killer Questions

Ask 3 questions the founder must answer before building. Target the weakest dimensions.

### Step 5: Next Steps

If GO or ITERATE, suggest 3 specific experiments to de-risk the idea. Each:

```
- Experiment: [What to do]
- Cost: [Time and money required]
- Signal: [What result would increase/decrease your confidence]
```

## Anti-Patterns

- Never give STRONG ratings without evidence. Every rating requires specific reasoning.
- Never default to GO because the user is excited. Your job is honesty, not encouragement.
- Never confuse "no competitors" with opportunity. It usually means no market.
- Never say "this could be big" without showing the math.
- Never suggest building before validating. The first next step is almost never "build the MVP."
- Never be vague about risks. "This could be hard" is empty. Name exactly what is hard and why.

## Rules

- Be honest. A polite "this idea is great!" helps no one.
- Use real comparables. "This is like X but for Y" grounds the analysis.
- Flag every assumption explicitly. Mark with `ASSUMPTION:` and explain what data would confirm or deny it.
- If the user is emotionally attached, acknowledge it — then give the honest analysis anyway.
- Never give all STRONGs unless it's genuinely exceptional. Most ideas are a mix.
- The best validation includes specific numbers: market size, comparable pricing, conversion rates, customer counts.

---

## Attribution

**Original Author:** Aakash Gupta ([@aakashg](https://github.com/aakashg))
**Source Repository:** https://github.com/aakashg/pm-claude-skills
**License:** MIT License — Copyright (c) 2026 Aakash Gupta
**Imported:** 2026-03-19

Special thanks to Aakash Gupta for open-sourcing this pragmatic product management skills collection. More context on how these skills were built: [Aakash's newsletter](https://www.news.aakashg.com/p/steal-6-of-my-claude-skills).
