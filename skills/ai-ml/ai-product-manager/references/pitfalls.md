## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: "AI Feature for AI's Sake"

```
❌ BAD: Product roadmap item: "Add AI to the dashboard."
Motivation: competitor launched AI features; executive wants AI in quarterly demo.
Outcome: team spends 3 months building an AI insight widget that 8% of users click,
generates generic observations users already know, and is removed after 2 quarters.

✅ GOOD: Start with the user problem. "Users spend 20 minutes every Monday manually
identifying which accounts to prioritize for outreach."
THEN evaluate: can AI solve this better than a simple sort + filter? (Often yes.)
AI feature with a real job to do: adoption >40% in month 1.
```

### Anti-Pattern 2: "The 95% Accuracy Fallacy"

```
❌ BAD: PM declares AI feature ready after model hits 95% accuracy on test set.
Ships to production. 5% error rate on medical dosage recommendations causes
pharmacist to administer wrong dose — user trust collapses, product pulled.

✅ GOOD: Define accuracy threshold relative to error severity tier BEFORE training:
- Error tier: annoying (wrong song recommendation) → 80% accuracy acceptable
- Error tier: trust-damaging (wrong product spec) → 95%+ required with explanation
- Error tier: harmful (medical, legal, financial) → 99.5%+ AND human review for all outputs

95% accuracy is excellent for some use cases and catastrophically insufficient for others.
The use case defines the threshold, not a universal standard.
```

### Anti-Pattern 3: "Ignoring Error UX"

```
❌ BAD: Team designs 47 screens for the AI success path.
Zero screens for what happens when AI returns low confidence or wrong output.
In production: AI shows a confident-looking wrong answer with no indication of uncertainty.
User makes a business decision based on wrong AI output; blames the product.

✅ GOOD: Design the error states FIRST:
- Low confidence (below threshold): "I'm not sure about this — here are similar cases"
- Wrong domain: "This is outside my knowledge — here's how to reach a human expert"
- System failure: "AI is temporarily unavailable — here's the manual workflow"
Every AI output state must have a designed user experience, not just the happy path.
```

### Anti-Pattern 4: "Misleading AI Transparency"

```
❌ BAD: Show users a confidence score of "0.73" or a percentage bar next to AI output.
Users in research: "What does 73% mean? Is that good? Should I trust it?"
Most users interpret any confidence display as binary (confident
without understanding calibration, without context, and without knowing what 73% means
for this specific task.

✅ GOOD: Translate confidence into plain language calibrated to the task:
- High confidence: Show AI output prominently; no extra friction
- Medium confidence: "Based on limited information — you may want to verify this"
- Low confidence: Route to human review; do not show uncertain output to user at all
Show explanations ("Because you previously purchased X") not probabilities.
```

### Anti-Pattern 5: "Binary Launch Thinking"

```
❌ BAD: "AI is ready, let's ship to all users."
Team disables all feature flags, deploys to 100% of production traffic.
Model has a subtle bias against mobile users (trained mostly on desktop sessions).
Mobile user NPS drops 12 points over 2 weeks before anyone notices.
Rollback requires coordinated deploy during business hours; 4-hour window of degraded UX.

✅ GOOD: Progressive rollout with automated guardrails:
1% → 10% → 50% → 100%, with:
- Automated rollback trigger if harmful output rate >0.5% or latency P99 >2× baseline
- Segment-aware rollout: test mobile users explicitly at 10% before expanding
- Kill switch that any on-call engineer can activate in <5 minutes
- "Blast radius" planning: what % of users are affected if we rollback at each stage?
```

---

