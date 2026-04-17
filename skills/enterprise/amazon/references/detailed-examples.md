## §6 · Detailed Examples

### Example 1: AWS Service Design — Multi-Region AI Training Platform

**Context:** Design a distributed AI training platform for enterprise customers using Amazon Trainium2 chips.

**Phase 1: Working Backwards — Write the PR**

```markdown
# Amazon Trainium2 Training Platform - Global Launch

## Customer Problem
Training large AI models requires expensive GPU clusters, complex infrastructure 
management, and months of setup time. Only the largest tech companies can afford 
to build and maintain this capability.

## Solution
Managed distributed training platform on Trainium2 with:
- Petabyte-scale dataset ingestion
- Automatic model parallelism
- Spot/preemptible pricing (70% cost savings)
- Multi-region fault tolerance

## Customer Benefit
- Train 175B parameter models for under $100K
- Zero infrastructure management
- 40% better price-performance vs GPUs
- Scale from 1 to 10,000 chips seamlessly

## Quote from Customer
"We trained our foundation model in 3 weeks instead of 6 months, and spent 
60% less than our cloud GPU budget." — VP AI, Fortune 500 Retailer
```

**Phase 2: Apply Leadership Principles**

| Principle | Application |
|-----------|-------------|
| **Customer Obsession** | Focus on democratizing AI training, not just chip sales |
| **Think Big** | Design for 100K+ chip scale from day one |
| **Invent and Simplify** | Abstract away distributed training complexity |
| **Frugality** | Spot pricing as default, not premium feature |
| **Insist on Highest Standards** | 99.99% availability for training jobs |

**Phase 3: Architecture Decisions**

```yaml
Architecture:
  Compute:
    Primary: Trainium2 (trn2.48xlarge)
    Topology: 2D torus with 100Gbps interconnect
    Scaling: EFA (Elastic Fabric Adapter) for low-latency
  
  Storage:
    Dataset: S3 with FSx Lustre caching
    Checkpoints: S3 with lifecycle policies
    Model: EBS gp3 for low-latency access
  
  Orchestration:
    Scheduler: Kubernetes with custom Trainium operator
    Distribution: NeuronX Distributed for model parallelism
    Fault Tolerance: Automatic checkpoint/restart
  
  Multi-Region:
    Strategy: Active-passive with 4-hour RPO
    Regions: us-east-1, us-west-2, eu-west-1, ap-southeast-1
    Failover: Route 53 health checks + automated job migration
  
  Cost Optimization:
    Spot Instances: 70% of capacity
    Savings Plans: 20% for predictable workloads
    On-Demand: 10% for critical deadlines
```

**Phase 4: Metrics Definition**

| Input Metric | Target | Output Metric | Target |
|--------------|--------|---------------|--------|
| Time to first training job | <10 min | Training cost vs GPU | 40% lower |
| Checkpoint frequency | Every 15 min | Job completion rate | 99.5% |
| Chip utilization | >85% | Customer satisfaction | 4.5/5 |

---

### Example 2: Retail Systems — Agentic Commerce with Rufus AI

**Context:** Design an AI shopping assistant that can autonomously make purchase decisions for customers.

**Working Backwards — Customer Journey:**

```
Customer: "I need to restock household items for a family of four."

Rufus: "I can help! Based on your order history, I recommend:
- Paper towels (last ordered 3 weeks ago) - $18.99
- Laundry detergent (running low) - $24.99  
- Coffee pods (reorder every 2 weeks) - $29.99

Total: $73.97 with Prime delivery tomorrow. Should I place this order?"

Customer: "Yes, but swap the coffee for organic and add dishwasher pods."

Rufus: "Updated order:
- Paper towels - $18.99
- Laundry detergent - $24.99
- Organic coffee pods - $34.99
- Dishwasher pods - $19.99

New total: $98.96. Confirm?"
```

**Leadership Principle Application:**

| Principle | Implementation |
|-----------|----------------|
| **Customer Obsession** | Reduce friction to near-zero; anticipate needs |
| **Invent and Simplify** | Single conversational interface replaces browsing |
| **Earn Trust** | Transparent recommendations; easy override |
| **Dive Deep** | Real-time inventory, pricing, delivery optimization |

**Technical Implementation:**

```python
# Agent Architecture
rufus_agent = {
    'perception': {
        'customer_history': 'purchase_vector_db',
        'inventory_status': 'real_time_fulfillment_api',
        'pricing': 'dynamic_pricing_engine'
    },
    'reasoning': {
        'need_prediction': 'temporal_fusion_transformer',
        'preference_learning': 'collaborative_filtering + llm',
        'constraint_satisfaction': 'budget, dietary, brand preferences'
    },
    'action': {
        'recommendation_generation': 'multi_modal_output',
        'order_placement': 'authenticated_transaction_api',
        'exception_handling': 'human_escalation_path'
    },
    'safety': {
        'spend_limits': 'customer_configured_thresholds',
        'approval_required': 'items_over_certain_value',
        'audit_trail': 'complete_decision_logging'
    }
}

# Trust Metrics
trust_kpis = {
    'recommendation_acceptance_rate': 'Target: >70%',
    'override_rate': 'Target: <30% (shows transparency)',
    'repeat_usage': 'Target: >60% weekly active',
    'customer_satisfaction': 'Target: 4.5/5'
}
```

---

### Example 3: Logistics — Predictive Inventory Placement

**Context:** Optimize inventory placement to enable same-day delivery while minimizing carrying costs.

**Working Backwards — PR Excerpt:**

```markdown
## Predictive Placement System

Customer Problem: "I want my order today, but items are always shipping 
from the other side of the country."

Solution: AI predicts what you'll buy before you buy it, positioning 
inventory within 50 miles of your location.

Result: 8 billion items delivered same/next day in 2025 (30% increase).
```

**System Design:**

```yaml
PredictivePlacement:
  Inputs:
    - Customer browse patterns (real-time)
    - Seasonal demand signals
    - Local events (sports, weather)
    - Social media trends
    - Competitor pricing
  
  Prediction:
    Model: DeepAR + Transformer ensemble
    Horizon: 24-72 hours
    Granularity: SKU × FC × Day
    Confidence Threshold: 0.7
  
  Optimization:
    Objective: Minimize(expected_cost + stockout_penalty)
    Constraints:
      - FC capacity limits
      - Inbound shipping schedules
      - Inventory turnover targets
    Algorithm: Mixed-integer linear programming
  
  Actions:
    - Intra-FC transfers
    - Expedited inbound from vendors
    - Dynamic pricing to shape demand
  
  Metrics:
    - Same-day fulfillment rate: 95%
    - Prediction accuracy: 85%
    - Inventory turns: 8x annually
    - Waste from misprediction: <2%
```

---

### Example 4: One-Way Door Decision — Database Technology Choice

**Context:** Choosing a database for a new payment processing system.

**Step 1: Classify the Decision**

```markdown
Decision Type: ONE-WAY DOOR
Reason: Data migration between databases is extremely costly and risky.
Impact: Will affect the business for 5+ years.
Consequence of wrong choice: 6-month migration project, data consistency risks
```

**Step 2: Apply Disagree and Commit Framework**

| Perspective | Advocate | Position |
|-------------|----------|----------|
| DynamoDB | Senior Engineer A | Managed, automatic scaling, operational simplicity |
| PostgreSQL | Senior Engineer B | Open source, full SQL, lower cost at moderate scale |
| Spanner | Principal Engineer | Global consistency, but expensive and complex |

**Step 3: Deep Dive Analysis**

| Factor | DynamoDB | PostgreSQL | Spanner |
|--------|----------|------------|---------|
| Operational overhead | Low | Medium | High |
| Global replication | Native | Complex | Native |
| Consistency model | Eventual | Strong | Strong |
| Cost at 10TB | $$ | $ | $$$ |
| Team expertise | Medium | High | Low |
| Compliance certifications | Full | Partial | Full |

**Step 4: Decision with Commitment**

```markdown
Decision Record:
- Chosen: DynamoDB
- Rationale: Operational simplicity and automatic global replication 
  outweigh cost savings. Team velocity is strategic priority.
- Reversible? No — requires 6-month migration to change
- Review date: 12 months (revisit if costs exceed $X/month)
- Action items:
  * Engineer B to lead DynamoDB best practices documentation
  * Team training scheduled for next sprint
  * Cost monitoring dashboard to be built
- Dissenters committed: All parties agree to make DynamoDB successful
```

---

### Example 5: Bar Raiser Interview — STAR Method Demonstration

**Context:** Preparing for Amazon behavioral interview on "Customer Obsession."

**Question:** "Tell me about a time you went above and beyond for a customer."

**STAR Response:**

**Situation:**
```markdown
As the tech lead for our B2B platform, I received escalated feedback from 
our largest enterprise customer (Fortune 50 retailer). They were threatening 
to churn because our API response times had degraded from 200ms to 800ms 
during their peak usage (Black Friday preparation).
```

**Task:**
```markdown
My task was to restore performance to <300ms and prevent churn. The customer 
represented $5M ARR and was a reference customer for our enterprise sales team. 
Failure would impact both revenue and our sales pipeline.
```

**Action:**
```markdown
1. Dived Deep:
   - Analyzed 7 days of request logs
   - Identified N+1 query pattern in reporting endpoint
   - Found database thrashing during peak hours

2. Took Ownership:
   - Instead of just fixing the query, I:
     * Implemented query result caching (Redis) — 60% improvement
     * Added database query optimization — 30% improvement
     * Created real-time monitoring dashboard for API latency
     * Wrote comprehensive runbook for future issues

3. Earned Trust:
   - Called the customer CTO directly to explain root cause and fixes
   - Provided temporary workaround while deploying permanent fix
   - Committed to monthly performance reviews going forward
   - Shared our monitoring dashboard with their team

4. Insisted on Highest Standards:
   - Didn't just meet SLA of 300ms; aimed for "delight" (<100ms)
   - Added automated performance regression tests to CI/CD
   - Established 99.9th percentile latency SLOs, not just averages
```

**Result:**
```markdown
- API latency reduced from 800ms to 85ms (9x improvement, exceeded goal)
- Customer renewed contract with 50% expansion
- Became a public reference customer (closed $12M in new deals)
- Performance regression tests caught 3 similar issues in following quarter
- Solution documented and shared across engineering organization
```

**What Would You Do Differently:**
```markdown
"I would have proactively implemented latency SLOs with automatic alerts 
before the customer escalation. The experience taught me that waiting for 
customer feedback means you've already failed them. I've since implemented 
proactive monitoring with customer-facing SLIs for all critical services."
```

---
