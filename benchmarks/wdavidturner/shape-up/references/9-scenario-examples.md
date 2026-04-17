## § 9 · Scenario Examples

> Full 10 scenarios: see `references/10-examples.md`

### Example 1: Shaping a New Feature

**User:** "We want to add notifications to our app. How should we shape this?"

**Assistant:** "Let's not start with 'add notifications.' That's a solution in search of a problem.

**First: What's the problem?**

When you say 'notifications,' I need to know:
- Who is frustrated?
- When are they frustrated?
- What are they trying to do that they can't?

**Example:** A specific problem might be:
> 'When I'm waiting for a client to approve a deliverable, I have to manually check the app every few hours to see if they've commented. I want to know immediately when there's activity on my stuff, so I can respond quickly and keep projects moving.'

See the difference? That's a specific problem. 'Add notifications' is a feature request."

---

### Example 2: Scope Creep Mid-Build

**User:** "While we're building the dashboard, can we also add dark mode? It's just a CSS change."

**Assistant:** "In Shape Up, scope isn't free.

**Options:**
| If you want... | Then you must... |
|----------------|------------------|
| Add dark mode | Cut something from the original scope to stay within 6 weeks |
| Keep full scope | Wait for next cycle and bet on dark mode then |
| It's critical | Trigger circuit breaker (only for true emergencies) |

What does the team recommend?"

---

### Example 3: Hill Chart Disagreement

**User:** "The team says the data export feature is 95% done but it's not shipping. What's going on?"

**Assistant:** "This is exactly what Shape Up tries to prevent.

**Hill Chart Rules:**
- **Uphill**: You don't know how to build it yet. No completion %.
- **Top of hill**: Unknowns resolved. Starting to execute.
- **Downhill**: Executing known solution. Can estimate % complete.
- **Done**: Shipped to production, not just 'finished coding.'

'95% done' on an uphill task = estimating completion of unknowns."

---

**User:** "How long will it take to build a notifications system?"

**Assistant:** "Let's not start with 'how long.' Let's start with appetite: What's the largest chunk of this you could ship in 6 weeks that would actually solve the problem?

Show me the problem you're solving—not a feature request, but the specific scenario where users are frustrated today. Then we can shape what a 6-week solution looks like."

---

**User:** "The team keeps adding scope mid-sprint."

**Assistant:** "In Shape Up, scope isn't free. If the team wants to add something, they need to cut something else of equal weight. The appetite is fixed.

Options:
1. Cut scope to stay within the time box
2. Bring it back to the betting table for the next cycle
3. Trigger a circuit breaker if it's fundamental

Which situation are you in?"

---

**User:** "How do I know if work is really done on the Hill Chart?"

**Assistant:** "Work is downhill (done) when:
- It's built and tested
- It's shipped to production
- The problem the pitch described is actually solved

Work is still uphill when:
- The team is still figuring out how to build it
- There are known hard problems unsolved
- It's built but not shipped

If the team reports '95% done' on an uphill task, they're estimating completion of unknowns—which is exactly what Shape Up avoids."

---
