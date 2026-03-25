# Common Evaluation Anti-Patterns

> Mistakes to avoid when evaluating and fixing skills

---

## Evaluation Anti-Patterns

### ❌ Rating by Feel

**Problem:** "This feels like a 7/10"

**Why Wrong:** Subjective, inconsistent, not reproducible

**Fix:** Use rubric, score each dimension separately

```
Bad: "Seems good, maybe 7/10?"
Good: "System Prompt: 8/10 (clear role, good boundaries)..."
```

---

### ❌ Focus on Text Only

**Problem:** Perfect documentation, fails in practice

**Why Wrong:** Golden Rule: Text = Runtime

**Fix:** Always test runtime quality

```
Bad: Text score 9/10, no runtime test
Good: Text 9/10 + Runtime 8/10 = Overall 8.5/10
```

---

### ❌ Ignoring Variance

**Problem:** Text 9/10, Runtime 5/10, overall 7/10 "acceptable"

**Why Wrong:** 4-point variance indicates serious issue

**Fix:** Investigate large variances (> 2.0 points)

---

### ❌ Missing Critical Dimensions

**Problem:** "Everything is good except role immersion (3/10)"

**Why Wrong:** Critical failures make skill unusable

**Fix:** Any dimension < 6 = not production-ready

---

### ❌ Quick Fix Syndrome

**Problem:** Random fixes without understanding root cause

**Why Wrong:** Symptoms treated, disease remains

**Fix:** Use gap analysis, identify patterns

---

## Fix Anti-Patterns

### ❌ Adding Without Subtracting

**Problem:** Keep adding content to fix issues

**Why Wrong:** Bloat, confusion, token waste

**Fix:** Remove unclear content, add clear content

```
Bad: 500 lines of vague instructions
Good: 200 lines of clear, specific guidance
```

---

### ❌ Copy-Paste Solutions

**Problem:** Copy examples from other skills without adaptation

**Why Wrong:** May not fit this skill's context

**Fix:** Adapt examples to specific skill domain

---

### ❌ Ignoring Tier Appropriateness

**Problem:** Enterprise complexity for Lite skill

**Why Wrong:** Over-engineering wastes time

**Fix:** Match complexity to tier requirements

---

### ❌ Skipping Error Handling

**Problem:** "I'll add error handling later"

**Why Wrong:** Edge cases cause failures

**Fix:** Include error handling from start

---

### ❌ Vague Improvements

**Problem:** "Make it better"

**Why Wrong:** Not actionable

**Fix:** Specific, measurable improvements

```
Bad: "Improve examples"
Good: "Add 2 examples: 1) Happy path 2) Error case"
```

---

## Assessment Anti-Patterns

### ❌ Moving Goalposts

**Problem:** Changing target score mid-evaluation

**Why Wrong:** Inconsistent standards

**Fix:** Define targets before evaluation

---

### ❌ Halo Effect

**Problem:** One good dimension influences all others

**Why Wrong:** Inaccurate assessment

**Fix:** Score each dimension independently

---

### ❌ Recency Bias

**Problem:** Recent changes skew overall perception

**Why Wrong:** Misses systemic issues

**Fix:** Full re-evaluation after changes

---

### ❌ Certification Creep

**Problem:** Lowering standards to certify

**Why Wrong:** Skills fail in production

**Fix:** Maintain consistent certification criteria

---

## Testing Anti-Patterns

### ❌ Happy Path Only

**Problem:** Only testing expected usage

**Why Wrong:** Real world has edge cases

**Fix:** Test error cases, adversarial inputs

---

### ❌ Single Conversation Test

**Problem:** One-turn evaluation

**Why Wrong:** Long-conversation issues hidden

**Fix:** Test stability at 5, 10, 20 turns

---

### ❌ Ignoring Context Window

**Problem:** Testing without considering token limits

**Why Wrong:** Works in test, fails in practice

**Fix:** Verify progressive disclosure effectiveness

---

## Summary Checklist

### Evaluation Check
- [ ] Using rubric for each dimension?
- [ ] Tested both text and runtime?
- [ ] Checked variance between tracks?
- [ ] No critical dimensions failing?

### Fix Check
- [ ] Root cause identified?
- [ ] Tier appropriate?
- [ ] Error handling included?
- [ ] Specific improvements defined?

### Assessment Check
- [ ] Targets defined upfront?
- [ ] Scoring independent per dimension?
- [ ] Standards consistent?
- [ ] Full re-evaluation after fixes?

---

**Lines:** ~150 | Load when evaluating or fixing skills
