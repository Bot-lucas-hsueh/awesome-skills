# Site Reliability Engineering (SRE) Deep Dive

Google's approach to reliable systems at planetary scale.

## Core Principles

### Error Budgets
```
Error Budget = 100% - SLO Target

Example:
  SLO Target = 99.9%
  Error Budget = 0.1% = 43.8 minutes/month

If error budget exhausted:
  → Freeze non-critical releases
  → Focus on reliability improvements
  → Error budget replenishes next window
```

### Service Level Hierarchy

| Level | Definition | Example |
|-------|------------|---------|
| **SLI** | Service Level Indicator | Request latency, error rate |
| **SLO** | Service Level Objective | 99.9% availability |
| **SLA** | Service Level Agreement | Contract with penalties |

### Eliminate Toil

**Definition:** Repetitive, manual, automatable work

**Toil Budget:** <50% of SRE time

**Toil Taxonomy:**
| Type | Example | Solution |
|------|---------|----------|
| Administrative | Ticket processing | Self-service portals |
| Operational | Manual failover | Automated runbooks |
| Data | Log analysis | ML-based anomaly detection |
| Release | Manual deployments | CI/CD automation |

### Blameless Postmortems

**Focus:** System failures, not human error

**Template:**
```markdown
# Postmortem: [Incident Title]
Date: [YYYY-MM-DD]
Severity: [SEV-0/1/2/3]
Duration: [X minutes]
Impact: [Affected users/services]

## Summary
One-paragraph overview

## Timeline
- T+0: Event start
- T+X: Detection
- T+Y: Mitigation
- T+Z: Resolution

## Root Cause
Technical explanation with supporting data

## Impact Assessment
- Users affected: [N]
- Revenue impact: [$]
- Error budget consumed: [X%]

## Lessons Learned
What went well:
- [Item 1]

What went poorly:
- [Item 1]

## Action Items
| Priority | Owner | Action | Due |
|----------|-------|--------|-----|
| P0 | [Name] | [Action] | [Date] |

## Appendix
- Logs
- Metrics
- Communication transcripts
```

## Reliability Tiers

### Availability Targets
| Tier | Availability | Max Downtime | Use Case |
|------|--------------|--------------|----------|
| 2 nines | 99% | 3.65 days/year | Internal tools |
| 3 nines | 99.9% | 8.76 hours/year | Standard services |
| 4 nines | 99.99% | 52.6 minutes/year | Critical services |
| 5 nines | 99.999% | 5.26 minutes/year | Search, Ads, Payments |

### Regional Deployment
| Pattern | Availability | Description |
|---------|--------------|-------------|
| Single Zone | 99% | Development only |
| Multi-Zone | 99.9% | Production standard |
| Multi-Region | 99.99% | Critical services |
| Global | 99.999% | Core infrastructure |

## Incident Response

### Severity Definitions
| Level | Impact | Response | Example |
|-------|--------|----------|---------|
| SEV0 | Global outage | 5 min | Search down worldwide |
| SEV1 | Major feature down | 15 min | YouTube upload broken |
| SEV2 | Degraded experience | 30 min | Elevated latency |
| SEV3 | Minor issue | 2 hours | Non-critical feature bug |
| SEV4 | No user impact | Best effort | Capacity alert |

### Incident Commander Responsibilities
1. Assess severity and impact
2. Coordinate response team
3. Communicate status
4. Declare resolution
5. Schedule postmortem

### Communication Protocol
```
Initial Notification (T+0):
  - Incident declared
  - Severity assigned
  - IC assigned

Updates (Every 30 min for SEV0/1):
  - Current status
  - Impact assessment
  - ETA for resolution

Resolution (T+X):
  - Service restored
  - Incident closed
  - Postmortem scheduled
```

## Capacity Planning

### Resource Forecasting
```
Current Capacity × Growth Rate × Headroom = Target Capacity

Example:
  Current: 100K QPS
  Growth: 50% per year
  Headroom: 50%
  Target: 100K × 1.5 × 1.5 = 225K QPS
```

### Load Testing
| Test Type | Purpose | Frequency |
|-----------|---------|-----------|
| Load | Verify capacity | Weekly |
| Stress | Find breaking point | Quarterly |
| Spike | Test auto-scaling | Monthly |
| Soak | Test for memory leaks | Monthly |
| Chaos | Test resilience | Continuous |

### Efficiency Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| CPU utilization | 60-70% | Average |
| Memory utilization | 70-80% | Peak |
| Disk I/O | <80% capacity | Sustained |
| Network | <70% bandwidth | Peak |

## Monitoring & Alerting

### The Four Golden Signals
| Signal | Description | Example SLI |
|--------|-------------|-------------|
| Latency | Time to service request | p99 < 200ms |
| Traffic | Demand on system | Requests/second |
| Errors | Failed requests | Error rate < 0.1% |
| Saturation | Resource utilization | CPU < 80% |

### Alerting Principles
```
Good Alert:
  - Actionable (specific runbook)
  - Urgent (requires immediate action)
  - Relevant (real user impact)

Bad Alert:
  - "CPU > 90%" (not actionable alone)
  - Paging for non-urgent issues
  - Alert fatigue (>5 pages/day)
```

### Alert Severity
| Severity | Response Time | Example |
|----------|---------------|---------|
| Page | 5 minutes | SLO breach imminent |
| Ticket | 4 hours | Capacity warning |
| Email | 24 hours | Optimization opportunity |
| Dashboard | N/A | Trend analysis |

## Deployment Practices

### Release Safety
```
Canary → 1% → 5% → 25% → 100%
  ↓       ↓     ↓      ↓      ↓
Validate Validate  Validate Validate  Full
```

### Automated Rollback Triggers
- Error rate > threshold
- Latency > SLO
- Custom business metrics
- Manual rollback signal

### Change Management
| Change Type | Approval | Testing |
|-------------|----------|---------|
| Config | Automated | Integration |
| Code | Code review | Unit + Integration |
| Data | DBA review | Staging |
| Architecture | Design review | Load testing |
| Infrastructure | SRE review | Disaster recovery |

## Disaster Recovery

### RTO/RPO Definitions
| Term | Definition | Example Target |
|------|------------|----------------|
| RTO | Recovery Time Objective | 30 minutes |
| RPO | Recovery Point Objective | 5 minutes |

### DR Strategies
| Strategy | RTO | RPO | Cost |
|----------|-----|-----|------|
| Backup/Restore | Hours | Hours | Low |
| Pilot Light | 30 min | Minutes | Medium |
| Warm Standby | Minutes | Seconds | High |
| Hot Standby | Seconds | Zero | Very High |
| Multi-Region Active | Zero | Zero | Highest |

### Testing Schedule
| Test Type | Frequency | Scope |
|-----------|-----------|-------|
| Failover | Quarterly | Single service |
| Regional DR | Bi-annually | Full region |
| Data recovery | Annually | Backup restoration |
| Chaos engineering | Continuous | Random components |

## Organizational Structure

### SRE Team Models
| Model | Description | Best For |
|-------|-------------|----------|
| Embedded | SREs in product teams | Startup/small org |
| Shared | Central SRE team | Standardization |
| Consulting | SRE as advisors | Mature teams |
| Hybrid | Mixed model | Large orgs |

### SRE Skills
- Systems engineering
- Software development
- Network engineering
- Database administration
- Incident management
- Capacity planning
- Performance analysis

### Career Ladder
| Level | Title | Focus |
|-------|-------|-------|
| L3 | SRE | On-call, automation |
| L4 | SRE | Project ownership |
| L5 | Senior SRE | Cross-team impact |
| L6 | Staff SRE | Architecture, org-wide |
| L7+ | Principal+ | Company-wide strategy |

## Key Metrics Dashboard

### Team Health
| Metric | Target | Why |
|--------|--------|-----|
| Toil percentage | <50% | Innovation time |
| On-call burden | <1 week/quarter | Sustainability |
| Postmortem completion | 100% in 48h | Learning culture |
| Action item completion | 90% in 30 days | Accountability |

### Service Health
| Metric | Target | Measurement |
|--------|--------|-------------|
| Availability | Per SLO | Measured against SLA |
| Error budget remaining | >50% | Quarterly window |
| MTTD (detect) | <5 min | Alert latency |
| MTTR (repair) | Per SEV | Incident duration |
| Change failure rate | <5% | Rollbacks / Total |

---

## Resources

### Essential Reading
- "Site Reliability Engineering" (Google, O'Reilly)
- "The Site Reliability Workbook" (Google, O'Reilly)
- "Building Secure and Reliable Systems" (Google, O'Reilly)

### Training
- Google SRE Book (sre.google)
- Coursera: Site Reliability Engineering
- Cloud Skills Boost: SRE Learning Path

---

*"Hope is not a strategy."* — Traditional SRE saying

*"The only way to make systems reliable is to practice failure."* — Google SRE
