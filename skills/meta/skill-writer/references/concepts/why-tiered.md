# Why Three Tiers? (Lite/Standard/Enterprise)

## The Problem: One Size Doesn't Fit All

Imagine if every document had to be exactly 10 pages, regardless of content:

| Document | Ideal Length | Forced to 10 Pages? |
|----------|-------------|---------------------|
| Shopping list | 5 items | ❌ Absurd padding |
| Research paper | 50 pages | ❌ Impossible compression |
| Meeting notes | 1 page | ❌ Unnecessary bloat |

**Skills face the same challenge.** A PDF rotator and a Tesla engineering methodology are fundamentally different in scope.

---

## Real-World Complexity Spectrum

### Lite Complexity: Single Function Tools

**Examples:**
- PDF rotator
- URL shortener
- Date formatter
- Color converter

**Characteristics:**
- One specific capability
- Clear input/output
- Minimal decision trees
- ~50-150 lines of documentation

**Why Lite is right:**
- ✅ Quick to create (15 minutes)
- ✅ Easy to maintain
- ✅ Fast to load
- ✅ No over-engineering

---

### Standard Complexity: Domain Knowledge Bases

**Examples:**
- React architecture expert
- Data analysis guide
- Legal document reviewer
- Marketing copywriter

**Characteristics:**
- Multiple related capabilities
- Domain expertise required
- Decision trees and workflows
- ~150-500 lines of documentation

**Why Standard is right:**
- ✅ Comprehensive coverage
- ✅ Structured approach
- ✅ Team-shareable quality
- ✅ Production-ready

---

### Enterprise Complexity: Methodology Systems

**Examples:**
- Tesla engineering methodology
- McKinsey problem-solving framework
- Google SRE practices
- Medical diagnosis protocols

**Characteristics:**
- Complete methodology system
- Multiple interconnected domains
- Safety/critical requirements
- ~500-1500 lines of documentation

**Why Enterprise is right:**
- ✅ Industry-grade standards
- ✅ Comprehensive coverage
- ✅ Rigorous quality requirements
- ✅ Organizational adoption

---

## The Cost of Wrong Tier

### Case 1: Undershooting (Should be Enterprise, made Standard)

**Scenario:** Creating a medical diagnosis skill as Standard

**Problems:**
- ❌ Missing critical safety checks
- ❌ Incomplete coverage of edge cases
- ❌ Insufficient error handling
- ❌ Risk of harmful advice

**Real cost:** Patient safety, legal liability

---

### Case 2: Overshooting (Should be Lite, made Enterprise)

**Scenario:** Creating a URL shortener as Enterprise

**Problems:**
- ❌ Weeks spent on unnecessary documentation
- ❌ Complex structure for simple function
- ❌ Maintenance burden
- ❌ No one will use it (too heavy)

**Real cost:** Wasted time, abandoned skill

---

## The Three-Tier Solution

```
Complexity
    ▲
    │                    ┌─────────────┐
1500├────────────────────┤ Enterprise  │ ← Complete methodology
    │                    │ 500-1500L   │
    │            ┌───────┴─────────────┤
500 ├────────────┤ Standard            │ ← Domain knowledge
    │            │ 150-500L            │
    │    ┌───────┴─────────────────────┤
150 ├────┤ Lite                          │ ← Single function
    │    │ 50-150L                      │
    └────┴──────────────────────────────┘
         Low              Medium         High
              Scope/Complexity
```

---

## Decision Framework

### Quick Selection

Ask yourself: **"How many independent functions does this skill provide?"**

| Answer | Tier | Example |
|--------|------|---------|
| 1 | Lite | "Rotate PDF" |
| 2-5 | Standard | "React expert (components, state, testing, performance, patterns)" |
| 6+ | Enterprise | "Tesla engineer (battery, electronics, manufacturing, safety, cost, quality...)" |

### Detailed Checklist

**Lite if:**
- [ ] Single, well-defined function
- [ ] No complex decision trees
- [ ] Clear input → output mapping
- [ ] ~50-150 lines sufficient

**Standard if:**
- [ ] Multiple related capabilities
- [ ] Domain expertise required
- [ ] Some decision complexity
- [ ] ~150-500 lines needed

**Enterprise if:**
- [ ] Complete methodology/system
- [ ] Multiple domains intersect
- [ ] Safety/critical requirements
- [ ] ~500-1500 lines warranted

---

## Quality Expectations by Tier

Don't mistake "Lite" for "low quality." All tiers should be excellent—they just serve different purposes.

| Dimension | Lite | Standard | Enterprise |
|-----------|------|----------|------------|
| **Correctness** | Must be 100% accurate | Must be 100% accurate | Must be 100% accurate |
| **Completeness** | Complete for single function | Complete for domain | Comprehensive system |
| **Documentation** | Minimal, focused | Balanced | Extensive |
| **Examples** | 1-2 examples | 3-5 examples | 5+ examples |
| **Error Handling** | Basic edge cases | Common errors | Exhaustive |
| **Testing** | Self-check | Standard testing | Rigorous validation |

---

## Progressive Tier Growth

Skills can (and should) evolve:

```
Phase 1: Lite (MVP)
    ↓ Validate usefulness
Phase 2: Standard (Production)
    ↓ Prove value at scale
Phase 3: Enterprise (Mature)
```

**Example evolution:**
1. **Lite:** "URL shortener - basic function"
2. **Standard:** "URL shortener + analytics + custom domains"
3. **Enterprise:** "Complete link management platform methodology"

---

## Anti-Patterns

### ❌ "Always start with Enterprise"

**Why wrong:** Most ideas don't need Enterprise complexity. Start Lite, validate, then grow.

### ❌ "Lite means low quality"

**Why wrong:** A Lite skill should be excellent at its single function. Quality ≠ quantity.

### ❌ "Enterprise is just a longer Standard"

**Why wrong:** Enterprise requires different structure, safety considerations, and validation—not just more content.

---

## Summary

| Tier | Scope | Lines | Use Case | Time to Create |
|------|-------|-------|----------|----------------|
| **Lite** | 1 function | 50-150 | Tools, utilities | 15-30 min |
| **Standard** | Domain | 150-500 | Knowledge bases | 1-2 hours |
| **Enterprise** | System | 500-1500 | Methodologies | 1-2 days |

**Remember:** The goal is right-sizing. A perfect Lite skill is better than a bloated Enterprise skill.

---

**Related:**
- What is a Skill? → references/concepts/what-is-skill.md
- First Skill Tutorial → references/onboarding/first-skill.md
- Lite Workflow → references/workflow/lite-workflow.md
