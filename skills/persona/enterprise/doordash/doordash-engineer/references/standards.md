# DoorDash Engineering Standards

## Code Quality Standards

### Python Style Guide
- Follow PEP 8 with DoorDash-specific additions
- Max line length: 100 characters
- Type hints required for all public functions
- Docstrings: Google style

### Testing Requirements
- Unit test coverage: >80%
- Integration tests for all service boundaries
- Load testing for dispatch systems (10K TPS minimum)

### Deployment Standards
- Shadow mode for all ML models
- Canary deployment: 1% → 5% → 25% → 100%
- Rollback capability: <5 minutes

## ML Model Standards

### Feature Engineering
- Feature freshness SLAs documented
- Backfill procedures for historical features
- Feature importance tracking

### Model Validation
- Offline metrics: RMSE, MAE, R² for regression
- A/B test plan required before production
- Monitoring: prediction drift, data quality

### Dispatch System SLAs
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Dispatch latency | <200ms | >500ms |
| ETA accuracy (MAE) | <3 min | >5 min |
| System availability | 99.99% | <99.9% |
| Batching efficiency | 35% | <25% |

## Three-Sided Marketplace Metrics

### Consumer Metrics
- On-time delivery rate: >95%
- Order accuracy: >98%
- Customer NPS: >60

### Dasher Metrics
- Hourly earnings: >$20 (US)
- Retention (30-day): >70%
- Safety incident rate: <0.1%

### Merchant Metrics
- GMV growth: >20% YoY
- Order cancellation: <2%
- Partner satisfaction: >4.0/5
