# code Example

```
PHASE 1: PROBLEM DEFINITION (Day 1)
├── Define success metric: "Reduce interventions in construction zones by 50%"
├── Identify data gap: Query fleet for construction zone scenarios
├── Baseline: Current model performance on target scenario
└── Shadow mode setup: Deploy detector to measure current gap

PHASE 2: DATA COLLECTION (Week 1-2)
├── Trigger definition: When to capture construction zone data
├── Fleet deployment: Push trigger to 100K+ vehicles via OTA
├── Autolabeling: Generate initial ground truth automatically
└── Human verification: Label ambiguous cases

PHASE 3: MODEL DEVELOPMENT (Week 2-4)
├── Architecture: Extend occupancy network with construction query
├── Training: Distributed training on Dojo
├── Simulation validation: CARLA/nuPlan regression suite
└── Metrics: mAP, collision rate, comfort metrics

PHASE 4: VALIDATION (Week 4-6)
├── Shadow mode: Run new model alongside human driver
├── A/B fleet test: Deploy to 1% of fleet, measure intervention rate
├── Safety review: Analyze all disengagements and near-misses
└── Go/No-Go: Decision based on fleet metrics

PHASE 5: DEPLOYMENT (Week 6+)
├── Gradual rollout: 1% → 10% → 100% over 2 weeks
├── Monitoring: Real-time intervention tracking
├── Rollback ready: Automated detection of regression
└── Post-deployment: Continue data collection for next iteration
```
