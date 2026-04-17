# Scenario Library

## Scenario 1: E-commerce Black Friday Preparation

**Context:** E-commerce platform expecting 10x traffic spike  
**Goal:** Ensure monitoring can handle scale and detect issues early

```yaml
Preparation Checklist:
  Infrastructure:
    - Scale Datadog Agents horizontally
    - Verify K8s HPA metrics collection
    - Enable cluster autoscaling monitoring
    
  APM:
    - Adjust sampling rates (0.1% → 0.01%)
    - Enable adaptive sampling
    - Pre-warm service maps
    
  Logs:
    - Increase log retention buffers
    - Enable aggressive filtering
    - Archive non-critical logs
    
  Alerts:
    - Tune thresholds for elevated baseline
    - Add capacity-based alerts
    - Create synthetic tests for critical flows

Key Metrics to Watch:
  - trace.web.request.errors (should be < 1%)
  - trace.web.request.duration.p99 (should be < 500ms)
  - kubernetes.cpu.usage.total (should be < 80%)
  - datadog.estimated_usage.metrics (watch for cardinality spikes)
```

## Scenario 2: Multi-Region Failover

**Context:** Primary region experiencing outages  
**Goal:** Monitor failover and validate recovery

```yaml
Monitoring Strategy:
  Synthetic Tests:
    - Multi-region API health checks
    - DNS resolution monitoring
    - CDN edge performance
    
  APM:
    - Cross-region trace correlation
    - Database replication lag
    - Cache hit rate changes
    
  Infrastructure:
    - Regional resource utilization
    - Network latency between regions
    - Load balancer traffic distribution

Failover Validation:
  1. Verify traffic shift in Service Map
  2. Check error rates remain stable
  3. Confirm latency within SLA
  4. Validate data consistency
```

## Scenario 3: Database Migration

**Context:** Migrating from PostgreSQL 12 to 15  
**Goal:** Monitor migration progress and catch issues

```yaml
Pre-Migration Baseline:
  metrics:
    - trace.db.query.duration (p50, p95, p99)
    - trace.db.query.errors
    - system.disk.io (database volumes)
    - postgresql.connections.active
    
During Migration:
  - Enable detailed query logging
  - Monitor replication lag
  - Track connection pool exhaustion
  - Watch for lock contention

Post-Migration Validation:
  - Compare query latency (should be same or better)
  - Verify all integrations functioning
  - Check backup job success
  - Validate monitoring data continuity
```

## Scenario 4: Security Incident Response

**Context:** Potential data breach detected  
**Goal:** Investigate and contain using observability data

```yaml
Investigation Steps:
  1. Log Analysis:
     query: "source:cloudtrail OR source:vpcflow @evt.name:*Delete* OR @evt.name:*Put*"
     timeframe: "last 4 hours"
     
  2. Trace Analysis:
     - Identify unusual API call patterns
     - Track authentication failures
     - Correlate with user sessions
     
  3. Infrastructure Audit:
     - Check for unauthorized instances
     - Review security group changes
     - Audit IAM policy modifications

Containment Actions:
  - Isolate affected resources
  - Rotate exposed credentials
  - Enable additional logging
  - Set up temporary high-frequency monitoring
```

## Scenario 5: Cost Optimization Initiative

**Context:** Datadog bill exceeded budget by 40%  
**Goal:** Reduce costs without losing visibility

```yaml
Analysis Phase:
  1. Identify Top Contributors:
     - Metrics by cardinality
     - Logs by volume per service
     - APM hosts and sampling rates
     - Custom metrics by team
     
  2. Optimization Actions:
     Metrics:
       - Replace histograms with distributions
       - Remove high-cardinality tags
       - Aggregate before sending
       
     Logs:
       - Filter debug logs at agent
       - Use FlexLogs for archived data
       - Reduce retention where possible
       
     APM:
       - Implement intelligent sampling
       - Use USM for non-critical services
       - Disable profiling in dev

Monitoring:
  - Set up cost anomaly alerts
  - Create team-level cost dashboards
  - Weekly cost review meetings
```

## Scenario 6: Microservices Decomposition

**Context:** Monolith being split into 10 microservices  
**Goal:** Maintain observability during transition

```yaml
Migration Strategy:
  Phase 1 - Shadow Mode:
    - Deploy new services alongside monolith
    - Mirror traffic to both paths
    - Compare latency/error rates
    - Use feature flags for routing
    
  Phase 2 - Gradual Cutover:
    - Shift 1% → 10% → 50% → 100% traffic
    - Monitor golden signals at each stage
    - Rollback triggers defined
    
  Phase 3 - Cleanup:
    - Remove monolith instrumentation
    - Update service maps
    - Consolidate dashboards

Observability Requirements:
  - Distributed tracing across old/new
  - Service dependency mapping
  - Database query attribution
  - Cross-service SLOs
```
