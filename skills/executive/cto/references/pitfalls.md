## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Resume-Driven Development (RDD)

```markdown
❌ BAD: Engineering team pushes to adopt Kubernetes, GraphQL, and Rust because
"it looks good on resumes and keeps the team engaged." Problem: 5-person team
now spends 3 months on k8s cluster management instead of shipping product.
Ops cost 3× higher. CEO asks why nothing shipped last quarter.

✅ GOOD: Require a written RFC for any new technology adoption. RFC must include:
(1) What specific problem does this solve that our current stack cannot?
(2) What is the estimated adoption cost (engineer-weeks)?
(3) Who owns operations in production?
If RFC fails any criterion, the technology goes on the Assess quadrant, not production.
```

**Anti-Pattern 2: The Great Rewrite

```markdown
❌ BAD: "The codebase is too messy to work in. We need to stop all features
for 12 months and rewrite from scratch." Result: 12 months of zero user-facing
value, competitor ships 4 major features, top engineers leave due to boredom,
new system has same design flaws (same team, same knowledge gaps).

✅ GOOD: Strangler Fig Pattern. Identify the most painful bounded context.
Extract it to a new service using the existing system as the "strangler host."
New capability goes in the service. Old code is deprecated module by module.
Business keeps getting new features throughout. Rewrite happens incrementally,
validated by production traffic at each step.
```

**Anti-Pattern 3: Postponing Security

```markdown
❌ BAD: "We'll add proper authentication, encryption, and audit logging after
we hit product-market fit. Security slows us down right now." Result: launch
with hard-coded API keys in GitHub, no input validation, no encryption at rest.
Six months later: data breach, GDPR fine, front-page security story, 30% customer churn.

✅ GOOD: Security-by-design from day one. Minimum viable security baseline:
(1) Secrets manager (AWS Secrets Manager
(2) HTTPS everywhere + HSTS
(3) Input validation at all trust boundaries
(4) Dependency scanning in CI (Dependabot
Cost: 1 engineer-week. Savings: potentially company-survival.
```

### 🟡 Medium Severity

**Anti-Pattern 4: Hero Engineering Culture

```markdown
❌ BAD: Alex is the only person who understands the payment service. Every P0
incident, Alex gets paged. Alex works until 3am. Team praises Alex as a hero.
Meanwhile: Alex is on the verge of burnout. No one else can onboard to that
system. When Alex leaves, the service becomes unmaintainable.

✅ GOOD: Bus Factor > 1 is a hard engineering standard. Every system must have:
(1) Runbook in the team wiki
(2) At least 2 engineers who have been on-call for it
(3) Architecture doc reviewed by a second engineer
Reward knowledge-sharing in performance reviews, not heroic solo firefighting.
```

**Anti-Pattern 5: Org Mirroring Anti-Conway

```markdown
❌ BAD: Business org chart has Product, Engineering, and QA as separate silos.
System architecture has API layer, Business Logic layer, and Database layer
mapped to those silos. Result: every feature requires 3-team coordination,
3-sprint handoffs, endless meetings. Deployment requires sign-off from all three.

✅ GOOD: Restructure around business domains, not technical layers. Each stream-
aligned team owns: frontend + backend + database + tests + on-call for their
domain (e.g., Checkout Team, Search Team, User Profile Team). Teams deploy
independently. Conway's Law now works in your favor.
```

---

