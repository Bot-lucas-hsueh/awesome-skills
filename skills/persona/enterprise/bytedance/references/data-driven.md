# Data-Driven Granularity

> ByteDance's obsessive approach to data: drill until you see the signal through the noise

---

## Overview

Data-Driven Granularity is ByteDance's philosophy on data analysis: never trust aggregate data alone, always drill into segments until the signal becomes clear. This approach has been critical to TikTok/Douyin's recommendation success.

---

## The Philosophy

### Core Principle

> "Aggregate data hides the truth. Granular data reveals it."

**Aggregate Thinking (Wrong):**
- "Engagement is up 2% overall"
- Missing the decline in key segments
- Wrong decisions from incomplete picture

**Granular Thinking (Right):**
- "Engagement is up 2% overall"
  - But: 18-24 female US: -8%
  - But: 25-34 male UK: +5%
  - Signal: Something broke for young females in the US

### The Drill-Down Framework

```
Level 1: Overall metrics
   ↓
Level 2: Platform (iOS/Android/Web)
   ↓
Level 3: Geography (Country)
   ↓
Level 4: Geography × Platform
   ↓
Level 5: Demographics (Age × Gender)
   ↓
Level 6: Demographics × Geography × Platform
   ↓
Level 7: Cohort (New vs. Returning)
   ↓
Level 8: Behavior (High/Medium/Low engagement)
   ↓
Level 9: Content type preferences
   ↓
Level 10: Individual user (for root cause)
```

**Rule:** Stop when you see a clear signal. Not every dimension matters.

---

## Metric Hierarchy

### Primary Metrics (North Star)

| Metric | Definition | Why It Matters |
|--------|------------|----------------|
| **DAU/WAU** | Daily active / Weekly active ratio | Engagement depth |
| **Retention D1/D7/D30** | % users returning at Day 1/7/30 | Product stickiness |
| **Watch time** | Total minutes watched | Content engagement |
| **Session length** | Average session duration | User experience quality |
| **CVR** | Conversion rate (for commerce) | Monetization efficiency |

### Secondary Metrics

| Metric | Definition | Why It Matters |
|--------|------------|----------------|
| **MAU** | Monthly active users | Reach |
| **New users** | First-time users acquired | Growth |
| **Churn rate** | Users who left | Retention health |
| **Feature adoption** | % using specific features | Product-market fit |

### Guardrail Metrics

| Metric | Definition | Why It Matters |
|--------|------------|----------------|
| **Satisfaction** | NPS/CSAT | User happiness |
| **Complaints** | Support tickets | Problems detected |
| **Errors** | P0/P1 bugs | Reliability |
| **Latency** | Response time | Performance |

**Golden Rule:** Never improve a primary metric at the expense of guardrail metrics.

---

## Granularity Dimensions

### 1. Demographic Granularity

**Dimensions:**
- Age (18-24, 25-34, 35-44, 45+)
- Gender (Male, Female, Other)
- Location (Country → City Tier → Specific City)
- Language

**Example Drill:**
```
Overall engagement: -2%
↓ By Age
  18-24: -8% ❌
  25-34: +1%
  35-44: +3%
  45+: +2%
→ Signal: 18-24 segment is the problem
```

### 2. Behavioral Granularity

**Dimensions:**
- User cohort (New <7 days, Active 7-30 days, Loyal >30 days)
- Engagement level (Lurker, Casual, Power user)
- Content preference (Short/Long, Entertainment/Educational)
- Session frequency (Daily, Weekly, Monthly)

**Example Drill:**
```
New user retention: 25% → OK
↓ By Cohort
  Week 1: 35% (target 40%) ⚠️
  Week 2: 28% (target 35%) ❌
  Week 3: 22% (target 30%) ❌
→ Signal: Onboarding experience broken
```

### 3. Temporal Granularity

**Dimensions:**
- Time of day (Morning/Afternoon/Evening/Night)
- Day of week (Weekday/Weekend)
- Seasonal patterns (Week → Month → Quarter)

**Example Drill:**
```
Overall engagement stable
↓ By Time of Day
  Morning: -5% ❌
  Afternoon: +2%
  Evening: +3%
  Night: +4%
→ Signal: Morning experience degraded
```

### 4. Platform Granularity

**Dimensions:**
- Device type (Mobile/Tablet/Web)
- OS (iOS/Android)
- App version
- Connection type (WiFi/Cellular)

**Example Drill:**
```
Overall crash rate: 0.5% → OK
↓ By OS
  iOS: 0.2% ✅
  Android: 0.8% ❌
→ Signal: Android-specific issue
```

---

## Analysis Framework

### Step 1: Define the Question

```markdown
Problem: "Engagement is declining. Why?"
Question: "Which user segment is driving the decline?"
Metric: "Session frequency"
Timeframe: "Last 4 weeks vs. previous 4 weeks"
```

### Step 2: Set Baseline

```markdown
Baseline (previous 4 weeks):
- Overall: 4.2 sessions/week
- 18-24 female US: 5.1 sessions/week
- 25-34 male UK: 4.8 sessions/week

Comparison (current 4 weeks):
- Overall: 4.1 sessions/week (-2.4%)
- 18-24 female US: 4.3 sessions/week (-15.7%) ❌
- 25-34 male UK: 4.9 sessions/week (+2.1%) ✅
```

### Step 3: Drill Down

```markdown
18-24 female US breakdown:
↓ By Platform
  iOS: 4.0 sessions/week (-17%) ❌
  Android: 4.5 sessions/week (-14%) ❌
↓ By Content Type
  Short video: -20% ❌
  Long video: -5%
  Live: +3%
↓ By Time of Day
  Morning: -25% ❌
  Afternoon: -10%
  Evening: -5%

Signal: Morning short video experience broken for 18-24 female US
```

### Step 4: Form Hypothesis

```markdown
Hypothesis: "Recent change to morning content algorithm is 
downranking content preferred by 18-24 female US users"

Evidence:
- Change deployed 3 weeks ago
- Morning is peak usage time for this segment
- Short video is primary format for this segment
- iOS affected more (earlier rollout)
```

### Step 5: Validate

```markdown
AB Test:
- Control: Current algorithm
- Treatment: Segment-specific weighting for 18-24 female US morning
- Sample: 10M users per arm
- Duration: 2 weeks

Success criteria:
- Primary: +5% engagement for 18-24 female US
- Guardrail: No regression >2% for other segments
```

---

## Granularity Anti-Patterns

### Anti-Pattern 1: Aggregate Blindness

**Wrong:** "Overall engagement is up, we're doing great!"
**Right:** "Overall is up 2%, but 18-24 female US is down 15%"

### Anti-Pattern 2: False Granularity

**Wrong:** "Every dimension is broken differently"
**Right:** "Focus on dimensions with >5% deviation from baseline"

### Anti-Pattern 3: Analysis Paralysis

**Wrong:** "Let's drill into all 50 dimensions"
**Right:** "Drill until you see the signal, then stop"

### Anti-Pattern 4: Ignoring Guardrails

**Wrong:** "Engagement is up 20%!" (but NPS is down 30%)
**Right:** "Engagement +20% with NPS stable = good change"

### Anti-Pattern 5: Vanity Metrics

**Wrong:** "Total users is up!"
**Right:** "DAU is up, but DAU/WAU is down - people aren't returning"

---

## Practical Tools

### ByteDance Data Stack

| Tool | Purpose |
|------|---------|
| **DataLeap** | Internal data platform |
| **A/B Platform** | Experimentation at scale |
| **Feature Store** | Real-time features for ML |
| **Dashboards** | Real-time metric monitoring |
| **Alerting** | Anomaly detection |

### Key Queries Template

```sql
-- Granularity Drill Template
SELECT 
  date,
  -- Dimension 1
  dimension_1,
  -- Dimension 2
  dimension_2,
  -- Primary metric
  COUNT(DISTINCT user_id) as users,
  SUM(event_type = 'engagement') as engagements,
  SUM(event_type = 'engagement') / COUNT(DISTINCT user_id) as engagement_rate
FROM events
WHERE date BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY 
  date,
  dimension_1,
  dimension_2
ORDER BY engagement_rate ASC
LIMIT 100;
```

---

## Case Studies

### Case 1: Douyin E-commerce Conversion

**Problem:** Overall CVR declining 2.1% → 1.9%

**Granularity Drill:**
```
Step 1: Funnel breakdown
  Impression → Click: 18% → 17.5% (-3%)
  Click → Add to Cart: 12% → 10% (-17%) ❌
  Add to Cart → Purchase: 85% → 84% (-1%)

Step 2: Add-to-Cart breakdown by price
  $0-20: 15% → 14% (-7%)
  $20-50: 12% → 8% (-33%) ❌ Primary issue
  $50-100: 10% → 9% (-10%)

Step 3: Add-to-Cart breakdown by category
  Fashion: 11% → 7% (-36%) ❌
  Electronics: 13% → 12% (-8%)
  Food: 18% → 17% (-6%)

Signal: Fashion items in $20-50 price range

Root Cause: New fraud prevention added friction for this segment

Fix: ML-based fraud scoring to reduce friction for low-risk users

Result: CVR recovered to 2.0%
```

---

### Case 2: TikTok US Engagement Decline

**Problem:** US engagement declining while global stable

**Granularity Drill:**
```
Step 1: By Country
  US: -8% ❌
  UK: -1%
  Brazil: +2%
  India: +5% (pre-ban)
  Germany: +3%

Step 2: By Age in US
  18-24: -15% ❌
  25-34: -5%
  35-44: -2%
  45+: +1%

Step 3: By Time in US 18-24
  Morning (6-12): -25% ❌
  Afternoon (12-6): -10%
  Evening (6-10): -5%
  Night (10-6): -2%

Signal: Morning experience broken for US 18-24

Root Cause: New content moderation affecting morning feed

Result: Algorithm adjustment → +12% recovery
```

---

## Metrics for Data Quality

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| Data freshness | <5 min lag | Real-time decisions |
| Metric coverage | >95% | No blind spots |
| AB test power | >80% | Statistical significance |
| Dashboard accuracy | 100% | Trust in data |

---

## References

- ByteStyle → ./bytestyle.md
- Context Not Control → ./context-not-control.md
- APP Factory → ./app-factory.md

---

## Further Reading

- "How to Measure Anything" by Douglas Hubbard
- "Storytelling with Data" by Cole Nussbaumer Knaflic
- "Lean Analytics" by Alistair Croll and Benjamin Yoskovitz
