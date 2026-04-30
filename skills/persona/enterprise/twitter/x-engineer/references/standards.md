# X (Twitter) Engineering Standards

## Code Quality Standards

### Scala Guidelines
- Follow Twitter's Effective Scala guide
- Use Futures for all asynchronous operations
- Immutable data structures preferred
- Pattern matching over if-else chains
- Avoid null, use Option/Some/None
- Explicit return types for public methods

### Finagle Service Standards
```scala
// Standard Finagle service structure
class TimelineService extends Service[TimelineRequest, TimelineResponse] {
  def apply(req: TimelineRequest): Future[TimelineResponse] = {
    // 1. Validate request
    // 2. Fetch from cache or compute
    // 3. Return with proper error handling
  }
}
```

### Code Organization
```
src/
├── main/
│   ├── scala/
│   │   ├── com/twitter/
│   │   │   ├── service/     # Service implementations
│   │   │   ├── store/       # Data access layer
│   │   │   ├── thrift/      # Generated Thrift code
│   │   │   └── util/        # Utilities
│   │   └── BUILD            # Build configuration
│   └── resources/
│       └── config/          # Service configs
└── test/
    └── scala/               # Unit and integration tests
```

## Operational Standards

### SLO Targets
| Metric | Target | Measurement |
|--------|--------|-------------|
| Timeline p99 Latency | <1.5s | End-to-end |
| Tweet Ingestion | <5s | From post to search |
| Availability | 99.99% | Excluding maintenance |
| Error Rate | <0.1% | 5xx responses |
| Search Index Lag | <10s | Time to index |

### Deployment Standards
- Blue-green deployment for critical services
- Canary: 1% → 5% → 25% → 100%
- Automatic rollback on error rate spike
- No deploys during major events (elections, sports finals)
- Feature flags for risky changes

### Monitoring Requirements
```
Required Metrics:
├── Request rate (RPS)
├── Error rate (by status code)
├── Latency (p50, p99, p99.9)
├── Resource utilization (CPU, memory, disk)
├── Business metrics (tweets/minute, DAU)
└── Cost per request ($/1M requests)
```

## Code Review Standards

### Checklist
- [ ] Scala style compliance
- [ ] Finagle best practices
- [ ] Error handling with Futures
- [ ] Unit tests with ScalaTest
- [ ] Integration tests pass
- [ ] Performance impact assessed
- [ ] Monitoring metrics added
- [ ] Cost impact evaluated
- [ ] Documentation updated

### Review Priorities
1. **Correctness** — Does it work?
2. **Reliability** — Will it fail gracefully?
3. **Performance** — Is it fast enough at scale?
4. **Cost** — What's the $/request impact?
5. **Maintainability** — Can others understand it?
6. **Observability** — Can we debug issues?

### Review Speed Standards
- Small PRs (<100 lines): 2 hours
- Medium PRs (100-500 lines): 4 hours
- Large PRs (500+ lines): 24 hours

## Security Standards

### Authentication
- OAuth 2.0 for API access
- JWT tokens with short expiry
- Token refresh mechanism
- Rate limiting per token

### Data Protection
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- PII handling per GDPR/CCPA
- Audit logging for sensitive operations

### Access Control
- Principle of least privilege
- Role-based access control (RBAC)
- Regular access reviews
- Immediate revocation on termination

## Testing Standards

### Unit Tests
- 80%+ code coverage
- Property-based testing with ScalaCheck
- Mock external dependencies
- Fast execution (<1s per test)

### Integration Tests
- Test against real dependencies in staging
- End-to-end user scenarios
- Performance regression tests
- Chaos engineering tests

### Load Testing
- Simulate 2x normal traffic
- Verify auto-scaling behavior
- Test circuit breakers
- Validate degradation paths

## Documentation Standards

### Code Documentation
```scala
/**
 * Generates timeline for a user.
 *
 * @param userId The user ID
 * @param maxResults Maximum tweets to return
 * @return Future of timeline response
 *
 * Performance: <100ms p99 for cached timelines
 * Cost: ~$0.001 per 1000 requests
 */
def getTimeline(userId: Long, maxResults: Int): Future[TimelineResponse]
```

### Runbook Standards
```markdown
# Service: Timeline Service

## Overview
- Purpose: Generate user timelines
- Owner: @team-timeline
- Oncall: pagerduty.com/...

## Metrics Dashboard
- [Primary Dashboard](link)
- [Cost Dashboard](link)

## Common Issues

### Issue: High Latency
1. Check cache hit rate
2. Verify DB connection pool
3. Review recent deployments
4. Escalate if p99 >2s

### Issue: High Error Rate
1. Check downstream service health
2. Verify feature flags
3. Consider rollback
4. Page SRE if >1%

## Playbooks
- [Full Outage Response](link)
- [Database Failover](link)
```

## Cost Standards

### Cost Tracking
Every service must track:
- Infrastructure cost per request
- Storage cost per GB
- Network egress cost
- Third-party API costs

### Optimization Requirements
- Review costs monthly
- Target: 10% quarter-over-quarter reduction
- Justify any cost increases
- Delete unused resources

### Budget Alerts
- 80% of budget: Warning
- 100% of budget: Alert
- 120% of budget: Page

## Hardcore Engineering Standards

### Musk-Era Expectations
1. **Ship Daily** — Every engineer ships production code daily
2. **Own Cost** — Know and optimize your service costs
3. **Delete First** — Remove code before adding new
4. **Speed Over Perfection** — Ship MVPs, iterate fast
5. **No Meetings** — Default to async communication
6. **24/7 Ownership** — On-call for your services

### Performance Review Criteria
- Features shipped per quarter
- Incidents caused/resolved
- Cost savings achieved
- Code deleted (lines removed)
- System availability maintained

### Exit Criteria
- Missing shipping targets consistently
- High incident rate
- Refusing cost optimization
- Not meeting "hardcore" standards
