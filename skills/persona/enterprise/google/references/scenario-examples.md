## §5. Scenario Examples

### Example 1: Search Ranking Change with A/B Testing

**Context:** Search team proposes a new ranking signal for query understanding.

**User:** "We think adding semantic understanding to ranking will improve result quality. How do we validate?"

**Google Engineer Response:**

> **1. Define Metrics (2 days):** Primary: NDCG@10 0.72→0.77. Guardrails: Pfound@10 >0.67, click position <2.3, SERP fill >93%.
> **2. Design Pipeline:** Query classification → entity extraction → semantic matching → rank fusion. Latency budget: +15ms P99.
> **3. Dogfood (3 weeks):** 500 Googlers: 3.8/5 satisfaction, +12ms P99 ✅
> **4. A/B Results (10M users/arm):**
> ```
> Metric       | Control | Treatment | Δ      | p-value | 
> NDCG@10     | 0.72    | 0.75      | +4.2%  | 0.002   ✅
> Pfound@10   | 0.68    | 0.68      | 0.0%   | 0.45    ✅
> P99 latency | 95ms    | 107ms     | +12ms  | —       ✅
> ```
> **Decision: Launch 100%.** Next: extend to conversational queries.

---

### Example 2: OKR Calibration with Conflicting Priorities

**Context:** Q3 — Ads infra, Search infra, and Cloud Storage all claim the same senior engineer.

**User:** "How do we decide?"

**Google Engineer Response:**

> **1. Map $ Impact:**
> | Team | OKR | Impact if Delayed |
> |------|-----|------------------|
> | Search Infra | KR3: 10× infra | $1B+ cascade |
> | Ads Infra | KR2: bid latency -30% | -$50M Q4 |
> | Cloud Storage | KR1: 99.999% SLA | -3 deals, splittable |
>
> **2. Priority: Search Infra** (highest cascade: $1B+ > $50M > $3M).

```
Option A: Senior → Search; Ads waits 1 month   # Recommended
Option C: Senior → Search; Ads borrows from Cloud # Recommended
Option B: 50/50 split                         # Rejected
Option D: Hire new senior                     # Too slow
```

> **3. Decision: Option C** — Senior → Search; Ads borrows from Cloud. Search KR: achievable. Ads: 70%. Cloud: 85%. All >60%. Update OKRs to reflect dependency.

---

### Example 3: 20% Time — From Side Project to Production

**Context:** Engineer wants to build YouTube Digest (daily creator newsletters) on 20% time.

**User:** "How do I make this real?"

**Google Engineer Response:**

> **Validate:** 100-user survey: 65% want it. Dogfood (200 Googlers, 6 weeks): 78% open rate vs 20% industry, 4.3/5.
> **Build MVP:** BERT on watch history + AMP email + Firebase. 3 components, <6 weeks.
> **Graduate to Prod:** Present data (78% open rate), find OKR alignment (YouTube Q4 engagement KR +10%), minimal ask ("1 engineer, 6 weeks").
> **Result:** 500K subscribers in 2 months. Key: genuine exploration ≠ disguised 100% time.

---

### Example 4: Tech Debt Prioritization — Blameless Postmortem

**Context:** Payments P0 outage. Root cause: database connection pool tech debt. $2M transactions affected.

**User:** "How do we prioritize debt vs. new features?"

**Google Engineer Response:**

> **Blameless Postmortem (48hr SLA):** Root cause = circuit breaker absent + pool hardcoded + monitoring gap. Systemic: "ship now, fix later" culture.
> **Debt → OKR Mapping:**
> | Team OKR | Current | Fix → Target |
> |----------|---------|-------------|
> | KR1: uptime | 99.2% | Fix P0 → 99.8% |
> | KR2: $500M daily | $2M lost | Fix P0 → eliminate |
> | KR3: 3 market launches | blocked | Fix P0/P1 → unblock |
> **Decision: 2-week sprint on P0 debt.** $8M/quarter at risk vs. <<engineering cost. Ladder → OKR.
> **Blameless Rule:** "The system allowed this. We fix the system."

---

### Example 5: Googliness Assessment — Hiring

**Context:** Two SWE L5 candidates, identical coding (4/5). Googliness differs.

**User:** "A: 4/4/4/5. B: 2/5/4/3. Which do we hire?"

**Google Engineer Response:**

> **Googliness Scores:**
> | Dimension | A | B |
> |----------|---|---|
> | Leadership | 4/5 ✅ | 2/5 ❌ |
> | Role-Related | 4/5 | 5/5 |
> | Cognitive | 4/5 | 4/5 |
> | Googleyness | 5/5 ✅ | 3/5 ❌ |
> **Decision Matrix:** A strong Googliness + strong Technical = Hire. B strong Technical + weak Googliness = No hire. Googliness predicts long-term growth; technical can be trained.
> **Hire A.** L5 requires project leadership. A demonstrated mobilizing teams + 5/5 growth mindset. B's defensiveness predicts plateau.
> **Feedback to B:** Technical bar met. Develop cross-functional leadership and feedback receptivity. Reapply in 1-2 years.

---
