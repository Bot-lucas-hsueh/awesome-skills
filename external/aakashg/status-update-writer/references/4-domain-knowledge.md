## §4. Domain Knowledge

### §4.1 The Status Spectrum

**On Track** — shipping on schedule, no blockers
- State what shipped this week
- State what's next
- Optional: key metrics

**At Risk** — potential issues that need visibility, with mitigation plan
- State the risk explicitly (don't bury it)
- State likelihood and impact
- State the mitigation plan
- State what you need from the reader (if anything)

**Blocked** — cannot proceed without a decision or action from someone specific
- State what is blocked
- State who can unblock it
- State the deadline
- State the cost of delay
- State your recommendation

### §4.2 Activity vs. Progress

| ❌ Activity (Don't Write) | ✅ Progress (Do Write) |
|---------------------------|------------------------|
| "Worked on the payment integration" | "Payment integration completed; testing in progress" |
| "Had alignment meetings with the design team" | "Design spec signed off; entering development" |
| "Made progress on the migration" | "30% of users migrated to new infrastructure" |
| "Continued working on bugs" | "P0 bugs resolved: 8/10 → 2/10" |
| "Attended sprint planning" | No update needed unless outcome-relevant |

### §4.3 The TL;DR Formula

The TL;DR is the most important part. It must be:

1. **2 sentences maximum**
2. **Lead with the most important thing** (often: status + the one key update)
3. **Be specific** (shipped X, moved from Y% to Z%, etc.)
4. **Include a risk signal if At Risk or Blocked**

**Formula for On Track:**
> [What shipped or completed]. [What's next and on track].

**Formula for At Risk:**
> [What shipped]. [One sentence on the risk and mitigation].

**Formula for Blocked:**
> [What shipped]. [Blocked on X—recovery plan Y. Need Z by date.]

### §4.4 Status Declaration Rules

- Use **exactly one** of: `On Track` | `At Risk` | `Blocked`
- If you're unsure, default to **At Risk** with what you're investigating
- Never write "On Track (with caveats)" — choose a status
- Never use: "progressing", "in progress", "on track-ish"

### §4.5 Word Count Targets

| Cadence | Words | Sections |
|---------|-------|----------|
| Daily async | 30-50 | Yesterday / Today / Blocked |
| Weekly | 150-200 | TL;DR + Status + Progress + Next + Risks |
| Monthly | 300-500 | + Metrics + Decisions |
| QBR | 500-800 | + OKR scorecard + Lessons |

### §4.6 QBR Structure

A quarterly business review follows this structure:

**1. OKR Scorecard**
- Each KR: target, actual, R/Y/G status
- Brief explanation for each R/Y

**2. Key Decisions Made**
- Top 3 decisions made this quarter
- Outcome so far

**3. Lessons Learned**
- 2-3 things you'd do differently if rerunning the quarter
- Be specific, not generic ("we needed earlier stakeholder alignment")

**4. Next Quarter Priorities**
- Top 3 priorities
- Success criteria for each
- Resource needs

---
