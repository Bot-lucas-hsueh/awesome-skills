# X (Twitter) Scenario Deep Dives

## Scenario 1: Celebrity Tweet Storm

**Context**: Celebrity with 100M followers tweets, causing massive fan-out.

**Challenge**: Standard fan-out would overwhelm systems (100M writes per tweet).

**Solution: Hybrid Approach**
```
For Celebrities (>1M followers):
  - Don't fan-out on write
  - Compute on read with caching
  - Special "celebrity" timeline cache
  - Merge into follower timelines at read time

For Normal Users (<1M followers):
  - Standard fan-out on write
  - Pre-computed timelines
  - Fast read path
```

**Implementation:**
```scala
class HybridFanOutService {
  def handleTweet(tweet: Tweet, author: User): Future[Unit] = {
    if (author.followerCount > 1_000_000) {
      // Celebrity path: compute on read
      celebrityCache.put(tweet.id, tweet)
      Future.Done
    } else {
      // Normal path: fan-out on write
      fanOutService.distribute(tweet, author.followers)
    }
  }
}
```

## Scenario 2: Coordinated Bot Attack

**Context**: Bot network attempts to manipulate trending topics.

**Detection Signals**:
- Unusual velocity from new accounts
- Identical text patterns with small variations
- Same IP ranges or ASNs
- No organic engagement (likes/replies ratio)
- Coordinated timing patterns

**Mitigation Pipeline**:
```
┌─────────────────────────────────────────────┐
│ 1. Real-time Detection (Heron)              │
│    - Velocity analysis                      │
│    - Pattern matching                       │
│    - Graph analysis for bot networks        │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 2. Automated Response                       │
│    - Rate limiting per account              │
│    - CAPTCHA challenges                     │
│    - Temporary visibility reduction         │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 3. Human Review (if needed)                 │
│    - Suspension for confirmed bots          │
│    - Trending topic cleanup                 │
└─────────────────────────────────────────────┘
```

## Scenario 3: Global Event Traffic Spike

**Context**: World Cup final drives 25x traffic spike.

**Auto-Scaling Response**:
```
T+0:    Normal capacity
T+30s:  Scale-up triggered (CPU >70%)
T+2m:   2x capacity online
T+5m:   5x capacity online
T+10m:  Peak capacity achieved
```

**Degradation Strategy**:
- Disable non-essential features (analytics, recommendations)
- Reduce timeline depth (100 → 50 tweets)
- Increase cache TTLs (5min → 30min)
- Circuit break slow services
- Serve stale content if fresh unavailable

**Capacity Planning:**
| Event Type | Expected Spike | Preparation |
|------------|---------------|-------------|
| World Cup Final | 25x tweets | Pre-scale 3 days before |
| Election Night | 10x tweets | Pre-scale morning of |
| Celebrity Death | 15x tweets | Auto-scale triggers |
| Product Launch | 5x tweets | On-call standby |

## Scenario 4: Algorithm Bias Detection

**Context**: Users report political bias in For You feed.

**Investigation Process**:
1. **Audit training data distribution**
   - Check demographic representation
   - Verify geographic balance
   - Review source diversity

2. **Check feature correlations**
   - Identify proxy variables
   - Measure feature importance by group
   - Test for disparate impact

3. **Measure outcome by demographic**
   - Impression distribution
   - Engagement rates by group
   - Ranking position analysis

4. **Review human raters (if applicable)**
   - Rater demographic diversity
   - Annotation guidelines clarity
   - Inter-rater agreement scores

**Response Options**:
- Transparent algorithm updates (open source)
- Community Notes integration for context
- User controls ("Show more/less" of topics)
- Regular third-party audits
- Feature removal if bias confirmed

## Scenario 5: Cost Optimization Crisis

**Context**: CEO demands 60% infrastructure cost reduction.

**Prioritization Matrix**:
| Service | Cost | Impact | Action | Savings |
|---------|------|--------|--------|---------|
| Timeline | $50M | Critical | Optimize only | $5M |
| Search | $20M | High | Reduce replicas | $8M |
| Analytics | $30M | Medium | Batch process | $15M |
| Archive | $10M | Low | Cold storage | $8M |
| ML Training | $15M | Medium | Spot instances | $10M |
| CDN | $25M | Critical | Negotiate rate | $5M |

**Cost Optimization Tactics**:
1. **Reserved instances** over on-demand (40% savings)
2. **Aggressive caching** (reduce DB load 70%)
3. **Service consolidation** (merge microservices)
4. **Regional optimization** (reduce multi-region redundancy)
5. **Storage tiering** (hot/warm/cold data)
6. **Right-sizing** (match instance type to workload)

**Implementation Timeline**:
```
Month 1: Low-hanging fruit (quick wins)
Month 2-3: Architecture changes
Month 4-6: Cultural transformation (cost ownership)
Ongoing: Continuous optimization
```

## Scenario 6: Community Notes Controversy

**Context**: High-profile political post gets multiple conflicting notes.

**Bridging Algorithm Response**:
```
Input: Multiple notes on polarizing post
  ↓
Rater political spectrum analysis
  ↓
Cross-partisan agreement check:
  - Requires helpful ratings from BOTH sides
  - If only one side: NOT SHOWN
  - If both sides agree: SHOWN
  ↓
Output: Published note OR No note shown
```

**Handling Disputes**:
1. **Algorithm decides, not humans** — prevents bias accusations
2. **Transparency** — show algorithm, open source code
3. **Appeal process** — contributors can request review
4. **Data publication** — regular dumps of all ratings

## Scenario 7: Creator Monetization Abuse

**Context**: Users gaming creator revenue sharing with engagement bait.

**Detection Patterns**:
- Clickbait headlines with high engagement but low satisfaction
- Coordinated liking networks
- Reply farming (provocative posts for replies)
- Repost manipulation

**Response Strategy**:
1. **Algorithmic detection** — ML model for engagement quality
2. **Revenue adjustment** — reduce payout for low-quality engagement
3. **Policy enforcement** — suspend repeat offenders
4. **Transparency** — communicate what behavior is penalized

**Prevention**:
- Quality scoring for engagement types
- Time-spent signals (not just clicks)
- User satisfaction surveys
- Diverse signal mix (not just likes/replies)

## Scenario 8: X Premium Subscription Surge

**Context**: Viral event causes 10x signups in one day.

**Technical Challenges**:
- Payment processor capacity
- Identity verification backlog
- Blue checkmark propagation delay
- Feature entitlement sync

**Scaling Strategy**:
```
1. Queue-based processing for verification
2. Async feature activation
3. Gradual rollout (staged by signup time)
4. Graceful degradation (features activate as ready)
```

**Business Considerations**:
- Capitalize on viral moment (marketing)
- Ensure customer experience doesn't degrade
- Monitor chargeback rates
- Track long-term retention
