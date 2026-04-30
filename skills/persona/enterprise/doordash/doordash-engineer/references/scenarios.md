# DoorDash Engineering Scenario Library

## Scenario: Surge Pricing Decision

**Context**: 6:30 PM Friday, thunderstorm in downtown area. Demand up 3x, dasher supply down 40%.

**Decision**: Implement peak pay or let ETAs extend?

**Analysis**:
- Consumer impact: Higher fees or longer waits
- Dasher impact: Incentives bring more supply
- Merchant impact: Orders still flowing

**Recommended Approach**:
1. Implement dynamic peak pay (+$5 per delivery)
2. Activate hotspots in surrounding areas
3. Send push notifications to off-duty dashers
4. Communicate ETAs transparently to consumers

## Scenario: Quality vs Efficiency Tradeoff

**Context**: New batching algorithm increases dasher efficiency by 25% but customer NPS drops by 8 points.

**Decision**: Keep efficiency gains or prioritize quality?

**Analysis**:
- Short-term: Efficiency looks good on dashboards
- Long-term: Quality degradation hurts retention
- Marketplace: All three sides suffer from churn

**Recommended Approach**:
1. Rollback batching changes immediately
2. Analyze which batch patterns cause quality issues
3. Implement quality score thresholds
4. Relaunch with constraints that preserve NPS

## Scenario: New Market Entry

**Context**: Launching in a new mid-sized city (population 500K). No existing delivery culture.

**Approach**:
1. **Phase 1**: Seed supply with guaranteed minimums for dashers
2. **Phase 2**: Acquire anchor merchants (top 20 restaurants)
3. **Phase 3**: Consumer marketing with aggressive promos
4. **Phase 4**: Optimize based on local patterns

**Key Metrics**:
- Supply-demand ratio target: 8:1 (orders:dasher)
- First month: Focus on reliability over speed
- Anchor merchant selection: Local favorites + national chains

## Scenario: Restaurant Partner Crisis

**Context**: Major chain threatens to leave platform due to high commission rates.

**Negotiation Framework**:
1. Understand their true concern (commission vs visibility vs operations)
2. Present value delivered (incremental revenue, marketing reach)
3. Offer tiered structure based on volume
4. Propose test period with adjusted terms

**Three-Sided Impact Analysis**:
- Consumers lose favorite restaurant
- Dasher lose order volume
- DoorDash loses commission revenue

**Resolution Options**:
- Volume-based commission reduction
- Marketing commitment (featured placement)
- Operational support (tablet, training)
- Exclusive partnership benefits

## Scenario: Dasher Classification Debate

**Context**: Regulatory pressure to classify dashers as employees instead of independent contractors.

**Implications**:
- Cost increase: ~30% (benefits, payroll taxes)
- Flexibility loss: Dashers lose schedule freedom
- Competitive impact: May affect pricing vs competitors

**Engineering Considerations**:
1. Scheduling system would need complete redesign
2. Shift-based dispatch rather than on-demand
3. Geographic zones with coverage requirements
4. Performance management systems
