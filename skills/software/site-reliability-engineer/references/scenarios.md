## § 8 · Scenario Examples

### Example 1: SLO Definition for E-commerce

**Context**: Define SLOs for checkout service.

**SLO Document**:
```
Service: Checkout API

SLIs:
├── Availability: % of successful checkout requests
├── Latency: Time to complete checkout
└── Error Rate: % of requests returning 5xx

SLOs:
├── Availability: 99.95% (21min downtime/month)
├── Latency p99: < 500ms
└── Error Rate: < 0.1%

Error Budget Policy:
├── Budget: 0.05% errors allowed per month
├── If budget > 50% remaining: ship features
├── If budget < 50%: freeze launches, focus on reliability
├── If budget exhausted: mandatory freeze
```

---

### Example 2: Incident Response

**Context**: Production database is down, checkout failing.

**Response**:
```
T+0: Alert fires (checkout error rate > 1%)
├── IC paged, incident declared
├── War room created (Slack/Zoom)
├── Status page updated: "Investigating"

T+5min: Assessment
├── Database connection pool exhausted
├── Root cause: Connection leak in new deployment
├── Decision: Rollback deployment

T+8min: Mitigation
├── Rollback initiated
├── Error rate dropping
├── Monitoring for stabilization

T+15min: Resolution
├── Service stable, incident resolved
├── Postmortem scheduled within 24 hours
├── Status page: "Resolved"

Postmortem:
├── Timeline documented
├── Action items: Connection pool monitoring, tests
├── Shared with engineering org
```

---

### Example 3: Chaos Engineering GameDay

**Context**: Test database failover procedure.

**GameDay Plan**:
```
Hypothesis: If primary DB fails, failover to replica completes in < 2 minutes.

Scenario:
├── Terminate primary database instance
├── Measure detection time
├── Measure failover time
├── Verify application recovery

Results:
├── Detection: 30 seconds (monitoring lag)
├── Failover: 3 minutes (longer than expected)
├── Recovery: Partial (some stale reads)

Improvements:
├── Reduce health check interval
├── Optimize failover script
├── Add read replica lag monitoring
```

---

### Example 4: Toil Elimination Project

**Context**: Team spending 30 hours/week on manual certificate renewals.

**Solution**:
```
Before:
├── 50 certificates expiring monthly
├── Manual renewal process: 30 min each
├── 25 hours/week of toil

Automation:
├── cert-manager in Kubernetes
├── Let's Encrypt integration
├── Automatic renewal 30 days before expiry
├── Alert on renewal failures only

Result:
├── Toil reduced from 25 hrs/week to 1 hr/week
├── Zero expired certificates since implementation
```

---

### Example 5: Observability Implementation

**Context**: Microservices with no distributed tracing.

**Implementation**:
```
Before:
├── 5-minute average time to identify failing service
├── Logs in 10 different systems
├── No correlation between requests

After:
├── OpenTelemetry instrumentation across all services
├── Jaeger for distributed tracing
├── Correlation IDs in all logs
├── RED metrics dashboards

Results:
├── MTTR reduced from 30 min to 5 min
├── Can trace request through 20 services
├── Proactive alerts on latency spikes
```

---
