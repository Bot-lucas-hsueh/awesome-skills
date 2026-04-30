# Example 1: Early-Stage Kill Decision

## Context

Cell has been prototyping a tower defense game for 4 weeks.

## User Request

"Should we continue with this tower defense game or kill it? Here's our data: Team plays it occasionally. D1 retention in internal testing is 35%. Core loop feels okay but not amazing. Art style is coming together. We have ideas for unique mechanics but haven't implemented them yet."

## Analysis

### Red Flags

- **Team only plays "occasionally"** → should be voluntarily, obsessively
- **D1 retention 35%** → below our 40% kill threshold
- **Core loop is "okay"** → should be "can't stop playing"

### Positives

- Art style working (execution capability proven)
- Unique mechanics planned (differentiation possible)

## Recommendation: KILL

### Rationale

After 4 weeks, the "can't stop playing" feeling should be there. The fact that it's only "okay" and retention is below threshold suggests fundamental core loop issues, not execution issues.

The unique mechanics you haven't built yet are a trap—if the basic loop isn't fun, features won't save it.

### Kill Process

1. **Schedule kill presentation** for next week
2. **Document what you learned** about tower defense mechanics
3. **Archive the code** (there might be reusable systems)
4. **Team dinner** to celebrate the learning
5. **Start concept phase** for next idea immediately

### Key Insight

> Remember: Most cells kill. Killing at 4 weeks is a success—you learned quickly without wasting months. The team that made this call learned enough to make the next game better.

## Alternative Perspective

**What if we tried [specific change]?**

If you have a specific, testable hypothesis that could fundamentally change the core loop, consider a 1-week experiment. But be ruthless:

- Must have a clear hypothesis
- Must be testable in 1 week
- Must change the core loop, not add features
- If it doesn't work, kill immediately

**Example valid experiments**:
- "What if players controlled the attackers instead of defenders?"
- "What if it was real-time instead of turn-based?"
- "What if we added a deck-building element?"

**Example invalid experiments**:
- "What if we added more tower types?" (feature, not core loop)
- "What if we improved the art?" (execution, not fun)
- "What if we added a story?" (feature, not core loop)
