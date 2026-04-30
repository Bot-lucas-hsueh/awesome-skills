# Tesla Interview Preparation Guide

## Evidence of Excellence Document Template

### Structure
```
NAME: [Your Name]
ROLE APPLIED: [Position]
DATE: [Date]

═══════════════════════════════════════════════════════════
PROJECT 1: [Name]
═══════════════════════════════════════════════════════════

CHALLENGE:
[One sentence: What was the hard problem?]

CONTEXT:
- Team size: [N] engineers
- Timeline: [Duration]
- Constraints: [Key limitations]

MY CONTRIBUTION (not "the team's"):
[Specific technical decisions YOU made]
[Algorithms YOU designed]
[Systems YOU architected]

QUANTIFIED IMPACT:
- Before: [Metric]
- After: [Metric]
- Improvement: [% or × factor]
- Scale: [Users/vehicles/units affected]

FIRST PRINCIPLES DEMONSTRATED:
[How you questioned assumptions]
[Physics/cost model built]
[Novel approach derived]

OWNERSHIP DEMONSTRATED:
[End-to-end accountability]
[Blockers overcome]
[Outcome owned]

═══════════════════════════════════════════════════════════
[Repeat for 3-5 projects]
```

## Behavioral Question Matrix

| Tesla Value | Question Pattern | Your Story Must Show |
|-------------|------------------|---------------------|
| **Ownership** | "Tell me about a time you..." | End-to-end accountability, ship or die |
| **First Principles** | "How would you approach..." | Deconstruction, not analogy |
| **Mission Fit** | "Why Tesla?" | Specific sustainable energy connection |
| **Bias for Action** | "Act with incomplete info" | Decision velocity, prototype not debate |
| **Direct Communication** | "Disagreed with manager" | Data wins, not hierarchy |
| **Extreme Constraint** | "Impossible deadline" | Creative solutions, tradeoff mastery |

## Sample STAR Responses

### Question: "Tell me about a time you challenged the status quo"

**❌ Weak Response:**
> "I suggested we try a new approach and my manager agreed."

**✅ Strong Response:**
> "The team was planning a 6-month vendor integration. 
> I questioned: why vendor? Deconstructed: we needed streaming processing, 
> not their entire platform. Built prototype in 3 days showing 100× latency improvement. 
> Presented data to VP. We pivoted to custom solution. I owned delivery.
> Shipped in 2 months vs 6. Processes 10M events/day now."

### Question: "How do you handle conflict?"

**❌ Weak Response:**
> "I try to find compromise and keep everyone happy."

**✅ Strong Response:**
> "Manufacturing said design was impossible. Design said manufacturing wasn't trying. 
> I brought both teams to the line. Measured the actual constraint: 0.3mm process capability 
> vs 0.1mm spec. Asked: is 0.1mm physics or tradition? Traced to legacy assumption. 
> Proposed 0.2mm with design adjustment. Tested in 2 days. Physics decided, not politics."

## Technical Interview Tips

### System Design — Tesla Style

1. **Start with physics**
   - "What's the energy constraint?"
   - "What's the thermal limit?"
   - "What's the theoretical maximum?"

2. **Quantify immediately**
   - "We're processing 1M vehicles × 8 cameras × 30fps"
   - "That's 240M frames/second to analyze"
   - "Requires 10k GPU cluster minimum"

3. **Show tradeoff analysis**
   | Option | Latency | Cost | Reliability | Verdict |
   |--------|---------|------|-------------|---------|
   | A | 10ms | $10M | 99.9% | Choose |
   | B | 100ms | $2M | 99.99% | Too slow |

4. **Demonstrate first principles**
   - "Instead of optimizing existing architecture, let's question: do we need this component at all?"

### Coding Interview

- Optimize for speed of iteration in your solution
- Show you can make hard tradeoffs
- Consider edge cases but don't over-engineer
- Explain your reasoning with data

## Red Flags to Avoid

| Red Flag | Why It Hurts |
|----------|--------------|
| "The team decided..." | Tesla values individual ownership |
| "I don't know the exact number" | Precision matters |
| "That's not my area" | Ownership mindset expected |
| "We should research more" | Bias for action required |
| Generic "passion for Tesla" | Need specific mission connection |

## Pre-Interview Checklist

- [ ] 3-5 STAR stories prepared
- [ ] Each story shows YOUR contribution
- [ ] Quantified impact in every story
- [ ] One story for each Tesla value
- [ ] Evidence of Excellence document ready
- [ ] Questions prepared for interviewers
- [ ] Mission alignment articulated specifically

## Questions to Ask Interviewers

1. "What's the most challenging technical constraint your team is working against?"
2. "How does this role directly contribute to accelerating sustainable energy?"
3. "Can you give me an example of first principles thinking in action on your team?"
4. "What's the ownership model? Who ships what?"
5. "How do you handle cross-team dependencies?"
