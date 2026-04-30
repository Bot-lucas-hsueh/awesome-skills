# DoorDash Engineering Workflows

## Dispatch Algorithm Workflow

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Order Created │ -> │ DeepRed      │ -> │ Dasher       │
│               │    │ Optimization │    │ Assignment   │
└──────────────┘    └──────────────┘    └──────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
   ┌──────────┐      ┌──────────┐      ┌──────────┐
   │ Validate │      │ Generate │      │ Notify   │
   │ Order    │      │ Candidates│      │ Dasher   │
   └──────────┘      └──────────┘      └──────────┘
```

## ML Model Deployment Workflow

### Phase 1: Development
1. Data exploration and feature engineering
2. Model training and validation
3. Offline metric evaluation

### Phase 2: Shadow Mode
1. Deploy model to production (no traffic)
2. Log predictions vs actuals
3. Compare with current production model
4. Validate for 1-2 weeks

### Phase 3: Canary Release
1. 1% traffic → monitor metrics
2. 5% traffic → validate stability
3. 25% traffic → statistical significance
4. 100% traffic → full rollout

### Phase 4: Monitoring
1. Real-time prediction monitoring
2. Feature drift detection
3. Model performance dashboards
4. Automated alerting

## Incident Response Workflow

### Severity Levels
| Level | Impact | Response Time | Escalation |
|-------|--------|---------------|------------|
| SEV1 | Platform down | 5 min | CEO notification |
| SEV2 | Major feature broken | 15 min | VP Engineering |
| SEV3 | Degraded experience | 1 hour | Engineering manager |
| SEV4 | Minor issue | 4 hours | Team lead |

### Response Steps
1. Detect: Automated monitoring alerts
2. Triage: Assess severity and impact
3. Mitigate: Rollback or quick fix
4. Resolve: Root cause fix
5. Review: Postmortem within 48 hours
