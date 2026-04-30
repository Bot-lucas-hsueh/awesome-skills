# Stripe Engineering Culture

## Overview

Stripe's engineering culture is renowned in Silicon Valley for its thoughtfulness, rigor, and developer-first principles. With 8,550+ employees globally and one of the world's largest Ruby codebases (20M+ lines), Stripe has maintained its culture of meticulous craft while scaling dramatically.

## Operating Principles

Stripe's culture is defined by three groups of operating principles:

### How We Work

**1. Users First**
> "There's a weighty obligation to businesses built on Stripe and the customers they serve. Because we're so critical to our users' success, we must keep their needs front and center in everything we do."

- Deeply understand user needs before building
- Work backwards from customer problems
- Surprisingly great solutions, not just functional ones

**2. Move with Urgency and Focus**
> "A bias for action speeds up our learning and delights users. Focus on what matters most, make fast initial progress, and iterate toward the best outcome."

- Focus on what matters most
- Make fast initial progress, iterate toward best outcome
- Learning speed > being right initially

**3. Be Meticulous in Your Craft**
> Excellence in every detail — from API design to error messages

- APIs are UI — design them like user interfaces
- Seven lines of code philosophy
- Every pixel, every word matters

**4. Seek Feedback**
> "Intellectual honesty, challenge assumptions."

- Prefer investigating to being right
- Lead with genuine curiosity
- Stripe sees itself as "probably wrong about lots"

**5. Deliver Outstanding Results**
> End-to-end accountability for outcomes

- High hiring bar maintains quality
- Help unblock fellow engineers
- Operate reliably (99.99%+ uptime)

### Who We Are

**Curious**
> "We lead with a genuine interest in people, ideas, and the unknown. We work hard to understand other points of view, and prefer investigating to being right."

**Resilient**
> "We view setbacks as opportunities to sharpen our skills and broaden our impact."

**Humble**
> "Stripes are humble, not arrogant or complacent, and create an inclusive environment for all. We aren't wedded to how we currently do things – lots about our current practices will turn out to be wrong."

**Macro-Optimistic**
> "All problems can be solved with understanding."

**Exothermic**
> "We generate infectious energy and warmth."

### And Leaders

**Elevate Ambitions**
> Know where your team is headed next year/in 4 years/10 years

**Set the Pace and Energy**
> Sign your team up for bold goals, articulate a plan to achieve them faster than expected

**Obsess Over Talent**
> Maintain high hiring bar, invest in team growth

**Help Others Succeed**
> When folks don't feel they have a stake in each other's success, this leads to bad outcomes

## Engineering Structure

### Team Organization

**Product Development Teams:**
- Built around major products (Billing, Terminal, Fraud, etc.)
- Large products have several engineering teams
- Full-stack by default (most engineers work across backend/frontend)

**Infrastructure and Operations:**
- Build internal infrastructure to enable engineering productivity
- Global Payments and Treasury Network (core money movement)
- Platform teams that other teams build on

**Specialized Engineering Roles:**
- ML Engineering (Radar, fraud models)
- Security (paramount in fintech)
- Native Mobile (iOS/Android)
- Infrastructure/Platform

### Remote Work Philosophy

**Remote Hub Coequal:**
- Remote Engineering Hub established 2019 (before pandemic)
- ~30% of engineers fully remote
- ~70% hybrid
- Remote staff are coequal part of culture
- Writing-heavy culture supports async work

**Global Engineering Centers:**
- San Francisco (HQ)
- Dublin (International HQ)
- Singapore
- Seattle
- New York
- Remote (distributed)

### Career Ladder

**Levels (L1-L7):**
- L1: Entry-level engineer
- L2: Engineer
- L3: Senior Engineer (equivalent to senior at most Big Tech)
- L4: Staff Engineer
- L5-L7: Senior Staff, Principal, Distinguished

**Dual Track:**
- IC track (individual contributor)
- Management track (EM)
- Lateral transfers possible at L3+
- Many senior leaders have switched tracks

**"Tech Staff" Descriptor:**
- Higher-level ICs evaluated by breadth and depth of impact
- Definition of impact varies by role and level

**"Engineer-ication":**
- Managers spend time writing code with their teams
- Recommended, not required, but culturally encouraged
- Keeps managers connected to technical reality

## Key Cultural Practices

### Writing Culture

Stripe operates with a writing-heavy, async-first culture:

**Why Writing:**
- Supports remote work
- Forces clarity of thought
- Creates persistent record of decisions
- Scales better than meetings

**Key Documents:**
- RFCs (Request for Comments) for technical decisions
- Product specs before building
- "Crazy Ideas" document — surface unconventional thinking

**Code Review:**
- Help unblock fellow engineers is a cultural value
- Encoded in code review expectations
- Cross-team help expected and valued

### API Review Discipline

**Every API Change is Reviewed:**
- Goes beyond normal code review
- Strict review process for all API modifications
- Documentation-driven design
- If it's hard to explain, it's wrong

**API Design Principles:**
- Consistency across all endpoints
- Predictable behavior
- Idempotency by default
- Graceful degradation

### "Engineer-ication"

Managers are encouraged to spend time writing code:

**Benefits:**
- Stay connected to technical reality
- Understand team challenges
- Maintain credibility with ICs
- Better technical decision-making

### First-Principles Thinking

**Approach:**
- Solve problems from fundamentals
- Don't just copy what others do
- "Crazy Ideas" document for unconventional thinking
- Willing to make farsighted bets

**Example — Global Expansion:**
- Stripe should work as well in Nigeria/Brazil as US
- Built infrastructure for emerging markets, not just Western countries
- Long-term infrastructure over short-term gains

### Full-Stack by Default

**Philosophy:**
- Most engineers work across backend and frontend
- Not siloed by specialty
- Rare to do only backend, frontend, or data
- New joiners take on what their team needs

**Flexibility:**
- Can specialize over time
- Movement between roles supported
- Many engineers started general, then specialized

## Technical Stack

### Core Technologies

| Layer | Technologies |
|-------|--------------|
| Backend | Ruby (20M+ LOC), Java, Go, Python |
| Frontend | React, TypeScript |
| Infrastructure | AWS, Kubernetes, Terraform |
| Data | Kafka, Flink, Spark, PostgreSQL |
| ML | PyTorch, custom fraud models |
| Mobile | iOS (Swift), Android (Kotlin) |

### Notable Facts

**Ruby Codebase:**
- World's largest Ruby codebase (20M+ lines)
- Heavy investment in Ruby tooling
- No requirement for new hires to know Ruby — learn on the job

**Language Flexibility:**
- Heavy investment in Java and Go on backend
- ML/AI tools increasingly important
- Engineers can pick up languages as they go

## Internal Tools

| Tool | Purpose |
|------|---------|
| **Sail** | Internal engineering platform |
| **Amp** | Internal deployment tooling |
| **Trailhead** | Internal learning/documentation |
| **Compass** | Navigation/discovery |
| **Intranet Home** | Central hub |
| **Go** | Custom tool for common tasks |

## Hiring Philosophy

**High Bar:**
- Hiring bar is a key cultural protection
- "Obsess over talent" is a leadership principle
- Prefer generalists who can specialize

**Interview Process:**
- Technical screens
- System design
- Cultural fit (operating principles)
- Coding exercises

**What They Look For:**
- Intellectual curiosity
- First-principles thinking
- User empathy
- Humble confidence
- Macro-optimism

## Product Development Culture

### Team Sport

**Cross-Functional:**
- Product development involves many disciplines
- Engineers expected to wear "product hat"
- Engineers talk directly with customers
- Not just "implement what PMs say"

### Customer Interaction

**Engineers with Customers:**
- Engineers encouraged to put on "product hat"
- Talk directly with customers
- Understand real problems before building
- Public chat rooms for user support (historically)

### Iteration Speed

**Historical Example (Early Stripe):**
- Public chat room for user support
- Every API request emailed to founders
- High-priority alerts on user errors
- Dashboard changed 3x, API 2-3x in first year

## Operational Excellence

### Reliability Focus

**Requirements:**
- 99.99%+ uptime for critical systems
- Graceful degradation
- Never lose track of money in flight
- Commercial contracts require reliability

### Deployment Practices

**Gradual Rollout:**
- Feature flags for everything
- Gradual rollout to reduce risk
- Custom deployment tooling (Amp)
- Hundreds of deploys per day

### Monitoring

**Everything Measured:**
- Stripe unapologetically measures everything
- Developer productivity metrics
- System health metrics
- Business metrics

## Unique Cultural Elements

### "Crazy Ideas" Document

**Purpose:**
- Annual exercise
- Everyone contributes ideas that are "probably bad but might be great"
- Separates idea generation from vetting
- Prevents self-censorship
- Surfaces unconventional thinking

### Long-Term Thinking

**Examples:**
- Global infrastructure for emerging markets
- Frontier ($925M carbon removal commitment)
- Atlas (50K+ companies, long-term bet)
- Climate (years before mainstream interest)

### Craft Obsession

**Details Matter:**
- API consistency obsessively maintained
- Documentation as product
- Error messages designed thoughtfully
- "Meticulous in your craft" principle

## Cultural Challenges

### Scaling Culture

**Risks:**
- Maintaining quality at scale
- Avoiding hierarchy ossification
- Keeping remote/hybrid cohesion
- Hiring fast enough while maintaining bar

**Mitigations:**
- Iterated operating principles to drive change
- Remote-first culture
- Writing-heavy async practices
- Explicit cultural investment from leadership

---

*Last Updated: March 2026*
*Sources: Pragmatic Engineer newsletter, Stripe blog, public interviews*
