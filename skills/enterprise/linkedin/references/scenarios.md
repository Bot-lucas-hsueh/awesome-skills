## § 8 · Scenario Examples

### Example 1: Social Graph — Connection Recommendations (People You May Know)

**User**: "Design a 'People You May Know' recommendation system for LinkedIn's 1.3B members."

**Expected Response**:
```
LinkedIn's PYMK Architecture:

1. GRAPH CONSTRUCTION
   Nodes: 1.3B members, 67M companies, 41K skills
   Edges: Connections, co-worker relationships, school ties, 
          shared interactions, skill overlaps
   
   Edge Types (in order of predictive power):
   ├── 1st-degree connections (strongest signal)
   ├── Co-workers (same company, overlapping dates)
   ├── School connections (same institution, overlapping years)
   ├── Shared connections (friend-of-friend)
   ├── Interaction edges (profile views, post engagements)
   └── Skill similarities (vector similarity)

2. CANDIDATE GENERATION
   Approach: Multi-hop graph traversal with early stopping
   
   Algorithm:
   - Start from member node
   - BFS to 2nd-degree (friends-of-friends): ~10K candidates
   - Filter: Remove existing connections, pending invites
   - Apply geographic and industry heuristics
   - Downsample to ~500 candidates for ranking

3. RANKING MODEL
   Features (50+ signals):
   ├── Graph features: Common connections, connection paths
   ├── Profile similarity: Industry, location, skills overlap
   ├── Behavioral features: Mutual profile views, post engagement
   ├── Temporal features: Recent job changes, active status
   └── Social proof: Endorsements, recommendations

   Model: Gradient Boosted Decision Trees (historically)
          → Transitioning to Graph Neural Networks (GNNs)

4. REAL-TIME SERVING
   Latency requirements:
   - Candidate generation: <20ms
   - Feature fetching: <30ms
   - Model inference: <10ms
   - Total: <100ms p99

5. EVALUATION
   Online metrics:
   - Connection acceptance rate (target: >15%)
   - Invitation send rate
   - Post-connection engagement
   
   Offline metrics:
   - AUC-ROC for connection likelihood
   - Precision@K for recommendations

Key Insight: The strongest predictor is "shared connections with 
high interaction strength" — not just count, but quality of 
intermediate relationships.
```

---

### Example 2: Recommendation Systems — Feed Ranking

**User**: "How does LinkedIn rank content in the professional feed?"

**Expected Response**:
```
LinkedIn Feed Ranking System:

1. PROBLEM FRAMING
   Multi-objective optimization:
   - Maximize member engagement (clicks, reactions, comments)
   - Maintain professional quality (reduce clickbait)
   - Ensure diversity (variety of sources, topics)
   - Support creator ecosystem (fair distribution)

2. CANDIDATE GENERATION
   Sources:
   ├── Followed connections (organic content)
   ├── Followed companies (corporate updates)
   ├── Joined groups (community content)
   ├── Recommended accounts (ML-based)
   ├── Sponsored content (ads)
   └── News/influencer content
   
   Volume: ~1,500 candidates per user per session

3. LIGHT RANKER (First Pass)
   Purpose: Fast filtering to ~150 candidates
   Model: Lightweight logistic regression or small NN
   Features: Basic profile match, recency, author authority
   Latency: <5ms per candidate

4. HEAVY RANKER (Second Pass)
   Purpose: Precise ranking of ~150 candidates
   Model: Deep Neural Network with attention
   
   Architecture:
   ├── Member embedding (learned from activity history)
   ├── Content embedding (text + media understanding)
   ├── Author embedding (reputation, expertise)
   ├── Context features (time, device, location)
   └── Interaction features (historical engagement patterns)
   
   Output: Engagement probability scores
   Latency: <50ms for full ranking

5. DIVERSITY AND FAIRNESS
   Post-processing:
   ├── Author diversity: Cap from single author
   ├── Content type mix: Articles, posts, videos, polls
   ├── Temporal diversity: Mix of fresh and evergreen
   └── Sponsored content: Blend naturally with organic

6. REAL-TIME PERSONALIZATION
   Dynamic adjustments:
   - Recent engagement boosts similar content
   - Dwell time signals (reading without clicking)
   - Instant feedback: "Not interested" downweights features
   - Trending content boosts for active topics

7. EVALUATION
   Online A/B tests:
   ├── Session length (target: +5% improvement)
   ├── Engagement rate (clicks, reactions, comments)
   ├── Diversity metrics (author entropy)
   └── Creator satisfaction (distribution fairness)

Key Insight: "Dwell time" — how long a member spends viewing 
content without explicit engagement — is a stronger signal than 
clicks for professional content quality.
```

---

### Example 3: Real-Time Analytics — Job Market Trends

**User**: "Design a system to track and report real-time job market trends (hiring rates, in-demand skills, salary trends)."

**Expected Response**:
```
LinkedIn Economic Graph Insights Platform:

1. DATA SOURCES
   Raw events:
   ├── Job postings (67M companies post jobs)
   ├── Job applications (140/second)
   ├── Profile updates (job changes, skill additions)
   ├── Hiring announcements (public posts)
   └── Recruiter activities (sourcing, InMails)

2. EVENT STREAMING PIPELINE
   
   Producer Layer:
   ├── Job posting service → Kafka
   ├── Profile service → Kafka
   ├── Recruiter tools → Kafka
   └── External data (layoff announcements, funding news)
   
   Kafka Configuration:
   - Topics: job-postings, profile-updates, hiring-events
   - Partitions: By geography + industry for parallel processing
   - Retention: 7 days for real-time, archived to HDFS

3. STREAM PROCESSING (Samza)
   
   Real-Time Aggregations:
   ├── Job posting rate by: city, industry, company size
   ├── Application-to-hire conversion rates
   ├── Skill demand trends (emerging, declining)
   ├── Salary range distributions
   └── Talent migration patterns (where people move)
   
   Windowing:
   - 1-minute windows for real-time dashboards
   - 1-hour windows for trend detection
   - 1-day windows for official reports

4. STORAGE LAYER (Apache Pinot)
   
   Schema Design:
   ├── Time column: Event timestamp
   ├── Dimensions: Geography, industry, company, job title
   ├── Metrics: Postings, applications, hires, salary
   └── Derived: YoY growth, MoM change, percentile ranks
   
   Pinot Features:
   - Real-time ingestion from Kafka
   - Sub-second query latency
   - Aggregation queries on billions of rows
   - Star-tree index for fast filtering

5. INSIGHTS PRODUCTS
   
   Consumer Products:
   ├── LinkedIn Workforce Reports (monthly publications)
   ├── Job seeker insights: "Top skills for this role"
   ├── Recruiter insights: "Competitive salary ranges"
   ├── Economic dashboards: City-level hiring trends
   └── API for journalists, policymakers, researchers

6. SAMPLE QUERY PATTERNS
   
   "Software Engineer hiring in San Francisco, last 90 days":
   ```sql
   SELECT 
     dateTrunc('DAY', event_time) as day,
     COUNT(DISTINCT job_id) as job_postings,
     AVG(salary_max) as avg_salary,
     PERCENTILE(salary_max, 90) as p90_salary
   FROM job_postings
   WHERE job_title = 'Software Engineer'
     AND location = 'San Francisco Bay Area'
     AND event_time > now() - 90 DAYS
   GROUP BY day
   ORDER BY day
   ```

Key Insight: Real-time insights enable proactive career decisions. 
When AI engineer hiring spikes in a city, members get notified 
before the trend is widely known.
```

---

### Example 4: Talent Marketplace — Skills-Based Job Matching

**User**: "How does LinkedIn match candidates to jobs using a skills-first approach?"

**Expected Response**:
```
LinkedIn Skills-First Matching System:

1. THE SKILLS TAXONOMY
   Structure:
   ├── 41,000+ standardized skills
   ├── Hierarchical: "Machine Learning" → "Deep Learning" → "PyTorch"
   ├── Relationships: Related skills, prerequisites, adjacent skills
   └── Emerging skills: Continuously added (e.g., "Generative AI", "LLM Engineering")

2. SKILL EXTRACTION & STANDARDIZATION
   
   Sources:
   ├── Profile: Self-reported skills with endorsements
   ├── Job descriptions: Extracted requirements
   ├── Course completions: LinkedIn Learning
   ├── Assessments: Verified skill badges
   └── Implicit: Inferred from job titles, descriptions
   
   NLP Pipeline:
   - Named Entity Recognition (NER) for skill mentions
   - Disambiguation: "Java" (island vs. language vs. coffee)
   - Normalization: Map synonyms to canonical skill
   - Confidence scoring for implicit extraction

3. SKILL GRAPH CONSTRUCTION
   
   Nodes: Skills
   Edges: 
   ├── Co-occurrence: Skills appearing together on profiles
   ├── Career paths: Skills leading to other skills (transitions)
   ├── Job requirements: Skills required for specific roles
   └── Similarity: Vector embedding similarity

4. MATCHING ALGORITHM
   
   Input:
   - Candidate: Skill set S_c with proficiency levels
   - Job: Required skills S_j with importance weights
   
   Scoring:
   ```
   match_score = Σ [importance_j × similarity(S_c, S_j)]
   
   Where similarity considers:
   - Exact match (skill in both sets)
   - Adjacent skills (related in skill graph)
   - Transferable skills (career path proven)
   - Proficiency level (self-reported or assessed)
   ```
   
   Gap Analysis:
   - Missing skills for the role
     - Time to acquire (based on learning path data)
   - Alternative skills that satisfy requirements

5. PERSONALIZED RECOMMENDATIONS
   
   For Job Seekers:
   ├── "Top job picks for you" (skills match ranking)
   ├── "Skill gaps to address" for target roles
   ├── "Career path" visualization (skills → roles → salaries)
   └── Learning recommendations (courses to close gaps)
   
   For Recruiters:
   ├── "Best matches" for their open roles
   ├── "Talent pool insights" (supply of specific skills)
   ├── "Diversity insights" (skill-based vs. credential-based)
   └── "Skills growth trends" in their industry

6. AI-POWERED ENHANCEMENTS
   
   Hiring Assistant (2024+):
   - Natural language job description → skill extraction
   - Automated candidate sourcing based on skills
   - Personalized outreach messages mentioning skill matches
   - Interview question suggestions based on skill requirements

Key Insight: Skills-based matching increases opportunity 
accessibility — candidates without traditional credentials but 
with demonstrated skills surface for roles they might otherwise 
be filtered out of.
```

---

### Example 5: Architecture — Real-Time Notification System

**User**: "Design LinkedIn's notification system that handles billions of events daily."

**Expected Response**:
```
LinkedIn Real-Time Notification System:

1. NOTIFICATION TYPES
   
   User-Triggered:
   ├── Connection requests and acceptances
   ├── Messages and InMails
   ├── Profile views
   ├── Post reactions and comments
   └── Mentions and tags
   
   System-Generated:
   ├── Job recommendations
   ├── Birthday reminders
   ├── Work anniversaries
   ├── Network updates (job changes, posts)
   └── Marketing and re-engagement

2. EVENT PRODUCERS
   
   Services publish to Kafka topics:
   ├── ConnectionService → connection-events
   ├── MessagingService → message-events
   ├── ProfileService → profile-view-events
   ├── FeedService → engagement-events
   └── RecommendationService → job-match-events

3. NOTIFICATION PROCESSOR (Samza)
   
   Stream Processing Steps:
   
   Step 1: Event Enrichment
   ├── Fetch sender profile
   ├── Fetch recipient preferences
   ├── Check notification settings
   └── Determine notification type
   
   Step 2: Rate Limiting & Throttling
   ├── Per-user daily limits (prevent spam)
   ├── Batching: Group similar notifications
   ├── Cool-down periods (don't over-notify)
   └── Priority scoring
   
   Step 3: Channel Selection
   ├── Real-time: Push notification (iOS/Android/Web)
   ├── Delayed: Email digest (batched)
   ├── In-app: Notification bell icon
   ├── SMS: High-priority only
   └── Third-party: Browser push, smart watches
   
   Step 4: Personalization
   ├── Time zone optimization (send at optimal time)
   ├── Device preference (mobile vs. desktop)
   ├── Historical engagement (which notifications opened)
   └── ML model: Will this user engage with this notification?

4. DELIVERY PIPELINES
   
   Real-Time Path:
   Kafka → Samza → Push Notification Service → APNs/FCM → Device
   Latency: <2 seconds end-to-end
   
   Email Path:
   Kafka → Samza → Email Queue → Email Service → SendGrid/AWS SES
   Latency: Batched, sent at optimal open times
   
   In-App Path:
   Kafka → Samza → Notification Store → Real-time API → Web/App
   Latency: <500ms for badge update

5. STORAGE & STATE
   
   Notification Store (Espresso):
   - User's notification inbox (last 90 days)
   - Read/unread status
   - Interaction tracking (clicked, dismissed)
   
   Aggregation Store (Voldemort):
   - Daily notification counts per user
   - Rate limit tracking
   - A/B test cohort assignments

6. SCALING CONSIDERATIONS
   
   Peak Load Handling:
   - Black Friday job posting spikes
   - Product launches (new features)
   - Viral content (posts getting millions of views)
   
   Strategies:
   ├── Partition by user_id for parallel processing
   ├── Backpressure: Queue overflow protection
   ├── Circuit breakers: Degrade gracefully under load
   └── Multi-region: Notifications served from nearest DC

7. MONITORING & ALERTING
   
   Key Metrics:
   ├── Delivery rate (target: >99.9%)
   ├── Latency p99 (target: <2s)
   ├── Open rate by notification type
   ├── Opt-out rate (target: <0.1%)
   └── False positive rate (notifications sent to wrong user)

Key Insight: The hardest problem is not sending notifications — 
it's not sending too many. Aggressive rate limiting and ML-based 
engagement prediction prevent notification fatigue.
```

---
