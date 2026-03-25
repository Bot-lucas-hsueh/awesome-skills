# Flexibility Framework

> Choose the right rigor for your context. Not every skill needs enterprise-grade process.

---

## The Core Insight

**One size doesn't fit all workflows.**

A personal prototype doesn't need the same rigor as a safety-critical medical skill.

---

## Three Flexibility Levels

```
Speed ◄─────────────────────────────────────► Quality

🚀 Quick          ⚖️ Standard          🔒 Strict
15 min            1-2 hours            1+ days
Personal          Team                 Public
Good enough       High quality         Certified
```

---

## 🚀 Quick Mode

### When to Use

- [ ] Personal use only
- [ ] Prototype/validation
- [ ] Internal tool
- [ ] Time constraint (< 30 min)
- [ ] Low consequence of failure

### Process

```
1. Define (2 min)
   └── What does this skill do?

2. Create (10 min)
   └── Write SKILL.md with essentials

3. Check (3 min)
   └── Quick sanity check

Done! ✅
```

### Quality Threshold

| Dimension | Minimum | Target |
|-----------|---------|--------|
| System Prompt | Clear role | Clear role + boundaries |
| Domain Knowledge | Basic accuracy | Good accuracy |
| Workflow | Exists | Clear steps |
| Error Handling | Basic | Common cases |
| Examples | 1 | 2 |
| Metadata | Filled | Good description |
| **Target Score** | **5.5** | **6.5** |

### Checklist

- [ ] I can explain what this skill does in one sentence
- [ ] SKILL.md has metadata block
- [ ] System prompt is clear
- [ ] At least one example works
- [ ] Basic error handling included

**If all checked → Ready to use**

---

## ⚖️ Standard Mode

### When to Use

- [ ] Team shared
- [ ] Production use
- [ ] Moderate consequence of failure
- [ ] Expected to evolve
- [ ] Time available (1-2 hours)

### Process

```
1. Discover (15 min)
   ├── Understand requirements
   ├── Identify users
   └── Define success criteria

2. Design (15 min)
   ├── Choose tier (Lite/Standard/Enterprise)
   ├── Select pattern
   └── Plan structure

3. Create (30 min)
   ├── Write SKILL.md
   ├── Add references if needed
   └── Create scripts if needed

4. Validate (30 min)
   ├── Self-review against rubric
   ├── Test with examples
   └── Score all 6 dimensions

5. Refine (30 min)
   └── Address gaps identified

Done! ✅
```

### Quality Threshold

| Dimension | Minimum | Target |
|-----------|---------|--------|
| System Prompt | Clear role + boundaries | Excellent definition |
| Domain Knowledge | Good accuracy | Deep expertise |
| Workflow | Clear steps | Optimized flow |
| Error Handling | Common cases | Comprehensive |
| Examples | 2 | 3-5 varied |
| Metadata | Good description | Excellent + tags |
| **Target Score** | **7.0** | **8.0** |

### Checklist

- [ ] All 6 dimensions ≥ 7.0
- [ ] 3+ diverse examples
- [ ] Comprehensive error handling
- [ ] Tested with real inputs
- [ ] Clear documentation

**If all checked → Production ready**

---

## 🔒 Strict Mode

### When to Use

- [ ] Open source/public release
- [ ] Safety-critical (medical, financial, legal)
- [ ] High consequence of failure
- [ ] Organizational standard
- [ ] Time available (1+ days)

### Process

```
1. Discovery (2 hours)
   ├── Deep requirements analysis
   ├── Stakeholder interviews
   ├── Risk assessment
   └── Success metrics definition

2. Design (2 hours)
   ├── Architecture design
   ├── Security review
   ├── Compliance check
   └── Pattern selection

3. Development (4 hours)
   ├── Write comprehensive SKILL.md
   ├── Create all references
   ├── Build test scripts
   └── Documentation

4. Validation (4 hours)
   ├── Full 6-dimension scoring
   ├── Runtime testing
   ├── Edge case testing
   ├── Adversarial testing
   └── Peer review

5. Certification (2 hours)
   ├── Final quality score
   ├── Documentation review
   ├── Version tagging
   └── Release checklist

Done! ✅
```

### Quality Threshold

| Dimension | Minimum | Target |
|-----------|---------|--------|
| System Prompt | Excellent definition | Exemplary |
| Domain Knowledge | Deep expertise | Authoritative |
| Workflow | Optimized flow | Best practice |
| Error Handling | Comprehensive | Exhaustive |
| Examples | 5 varied | 5+ comprehensive |
| Metadata | Excellent + tags | Perfect |
| **Target Score** | **8.5** | **9.0+** |

### Checklist

- [ ] All 6 dimensions ≥ 8.5
- [ ] 5+ comprehensive examples
- [ ] Exhaustive error handling
- [ ] Runtime tested
- [ ] Adversarial tested
- [ ] Peer reviewed
- [ ] Documentation complete
- [ ] Security reviewed (if applicable)

**If all checked → Certified for release**

---

## Auto-Selection Guide

Not sure which mode? Answer these questions:

### Q1: Who will use this skill?

| Answer | Suggested Mode |
|--------|---------------|
| Just me | Quick |
| My team | Standard |
| Public/Company-wide | Strict |

### Q2: What happens if it fails?

| Answer | Suggested Mode |
|--------|---------------|
| No big deal, try again | Quick |
| Minor inconvenience | Standard |
| Serious consequences | Strict |

### Q3: How much time can you invest?

| Answer | Suggested Mode |
|--------|---------------|
| < 30 minutes | Quick |
| 1-2 hours | Standard |
| 1+ days | Strict |

### Q4: What's the expected lifespan?

| Answer | Suggested Mode |
|--------|---------------|
| One-time use | Quick |
| Months of use | Standard |
| Years as standard | Strict |

### Q5: Will it handle sensitive data?

| Answer | Suggested Mode |
|--------|---------------|
| No | Quick/Standard |
| Yes | Strict |

---

## Mode Switching

Skills can (and should) evolve through modes:

```
Quick (prototype)
    ↓ Validate concept
Standard (production)
    ↓ Prove value
Strict (certified)
```

**Example:**
1. **Quick:** "PDF rotator that sort of works" (30 min)
2. **Standard:** "PDF rotator that works reliably" (2 hours)
3. **Strict:** "PDF processor suite, battle-tested" (2 days)

---

## Common Anti-Patterns

### ❌ Always Strict Mode

**Problem:** Spending 2 days on a one-time utility

**Cost:** Wasted time, over-engineering

**Fix:** Start with Quick, upgrade if needed

---

### ❌ Never Strict Mode

**Problem:** Releasing safety-critical skills with Quick mode quality

**Cost:** Errors, liability, user harm

**Fix:** Assess risk honestly. When in doubt, be stricter.

---

### ❌ Mode Confusion

**Problem:** Mixing requirements ("Quick mode but also do full adversarial testing")

**Cost:** Inconsistent quality, undefined done-ness

**Fix:** Pick one mode. Follow its process. Don't cherry-pick.

---

## Summary Matrix

| Aspect | Quick | Standard | Strict |
|--------|-------|----------|--------|
| **Time** | 15 min | 1-2 hrs | 1+ days |
| **Users** | Personal | Team | Public |
| **Quality Target** | 6.5 | 8.0 | 9.0+ |
| **Examples** | 1-2 | 3-5 | 5+ |
| **Error Handling** | Basic | Comprehensive | Exhaustive |
| **Testing** | Self-check | Standard tests | Full suite |
| **Documentation** | Minimal | Complete | Exemplary |
| **Review** | None | Self | Peer + adversarial |

---

## Decision Tree

```
Start
│
├─ Personal use only?
│  ├─ Yes → Quick Mode
│  └─ No → Continue
│
├─ High consequence if fails?
│  ├─ Yes → Strict Mode
│  └─ No → Continue
│
├─ < 30 minutes available?
│  ├─ Yes → Quick Mode
│  └─ No → Continue
│
├─ Public release?
│  ├─ Yes → Strict Mode
│  └─ No → Standard Mode
```

---

**Remember:** The right mode is the one that matches your context. Don't over-engineer, don't under-engineer.

---

**Related:**
- Quick Mode → ./quick-mode.md
- Standard Workflow → ./standard-workflow.md
- Strict Mode → ./strict-mode.md
