# Common Pitfalls & Anti-Patterns

## 🔴 Critical Pitfalls

### 1. Metric Cardinality Explosion

**Problem:** Using high-cardinality values as metric tags

```python
# BAD: Creates millions of unique time series
for user_id in user_ids:
    statsd.increment("api.request", tags=[f"user_id:{user_id}"])
    # If 1M users = 1M unique time series!

# GOOD: Aggregate or use low-cardinality alternatives
statsd.increment("api.request", tags=[
    f"user_tier:{user.tier}",  # free, basic, premium
    f"user_region:{user.region}"  # us-east, eu-west, apac
])
```

**Impact:** 
- 10x-100x cost increase
- Query performance degradation
- Dashboard timeouts

**Mitigation:**
- Cardinality limit: < 100 values per tag
- Use logs for high-cardinality data
- Pre-aggregate where possible

### 2. Alert Fatigue

**Problem:** Too many alerts with poor signal-to-noise ratio

```yaml
# BAD: Alert on every threshold breach
name: "CPU High"
query: avg(last_1m):system.cpu.user{*} > 80
# Will trigger constantly during normal operation

# GOOD: Sustained threshold with context
name: "[P2] Sustained High CPU"
query: |
  avg(last_15m):system.cpu.user{env:production} > 80 
  AND 
  avg(last_5m):system.cpu.user{env:production} > 85
message: |
  CPU has been elevated for 15+ minutes.
  Current load: {{value}}%
  Top processes: {{top_processes}}
  Runbook: https://wiki/runbooks/high-cpu
  @slack-alerts
```

**Mitigation:**
- Use composite alerts
- Add hysteresis (different alert/recovery thresholds)
- Include context and runbook links
- Regular alert review (monthly)

### 3. Missing Error Budget Policies

**Problem:** SLOs defined without error budget policies

```yaml
# BAD: SLO without action plan
slo:
  target: 99.9%
  # No guidance on what to do when budget is at risk

# GOOD: SLO with explicit policies
slo:
  target: 99.9%
  error_budget_policy:
    - threshold: 50%
      action: "monitor, no alert"
    - threshold: 25%
      action: "review recent deployments"
    - threshold: 10%
      action: "halt feature releases"
    - threshold: 1%
      action: "all hands incident response"
```

## 🟡 High Severity Pitfalls

### 4. Inconsistent Tagging

**Problem:** Different teams use different tag conventions

```yaml
# Team A
tags: [env:prod, service:payment-api]

# Team B  
tags: [environment:production, app:payments]

# Team C
tags: [e:prd, svc:pay]
```

**Impact:**
- Cannot aggregate across services
- Dashboards show incomplete data
- Alerting gaps

**Solution:** Implement tag governance
```yaml
required_tags:
  - env: [prod, staging, dev]
  - service: "lowercase-hyphenated"
  - team: "from-service-catalog"
  
validation:
  - reject_missing_tags: true
  - auto_apply_defaults: true
```

### 5. Over-Reliance on Defaults

**Problem:** Using default sampling rates without consideration

```yaml
# BAD: 100% sampling in high-throughput service
apm_config:
  enabled: true
  # Default 100% sampling - will overwhelm backend

# GOOD: Configured sampling based on traffic
apm_config:
  enabled: true
  sample_rate: 0.01  # 1% for high-volume
  sample_rate_by_service:
    payment-api: 0.1  # 10% for critical
    health-check: 0.0  # 0% for noise
```

### 6. Log Cost Surprises

**Problem:** Debug logs in production causing bill shock

```yaml
# Agent Configuration - Log Filtering
logs_config:
  processing_rules:
    - type: exclude_at_match
      name: exclude_debug
      pattern: "\\[DEBUG\\]"
      
    - type: exclude_at_match  
      name: exclude_health_checks
      pattern: "/health|/ready|/alive"
      
    - type: include_at_match
      name: include_errors_only_in_prod
      pattern: "\\[ERROR\\]|\\[FATAL\\]"
      # Only send errors from specific services
```

## 🟢 Medium Severity Pitfalls

### 7. Dashboard Sprawl

**Problem:** Hundreds of unmaintained dashboards

**Solution:**
- Dashboard ownership tagging
- Quarterly deprecation reviews
- Template-based standardization
- Usage analytics to identify stale dashboards

### 8. Monitor Drift

**Problem:** Alerts don't reflect current architecture

**Solution:**
- Infrastructure-as-code for monitors (Terraform)
- Automated monitor validation
- Service catalog integration
- Regular monitor audits

### 9. Missing Correlation

**Problem:** Traces, metrics, and logs not linked

```python
# BAD: No correlation between telemetry types
def handle_request(request):
    logger.info("Processing request")  # No trace_id
    statsd.increment("request.count")  # No tags
    with tracer.trace("handler"):
        process(request)  # No log correlation

# GOOD: Full correlation
def handle_request(request):
    span = tracer.current_span()
    trace_id = span.trace_id if span else None
    
    logger.info("Processing request", extra={
        "trace_id": trace_id,
        "request_id": request.id,
        "user_id": request.user_id
    })
    
    statsd.increment("request.count", tags=[
        f"service:{SERVICE_NAME}",
        f"endpoint:{request.endpoint}",
        f"trace_id:{trace_id}"
    ])
```

## Anti-Pattern Reference

| Anti-Pattern | Why It's Bad | Better Approach |
|--------------|--------------|-----------------|
| Alerting on symptoms | False positives | Alert on user-impacting metrics |
| One-size-fits-all SLOs | Unachievable targets | Team-specific, realistic targets |
| Ignoring cost | Budget overruns | Cost attribution and budgets |
| Manual configuration | Drift, inconsistency | Infrastructure as code |
| Siloed observability | Missing context | Unified platform approach |
| Over-monitoring | Alert fatigue | Focus on critical paths |
| Under-monitoring | Missed incidents | Complete coverage of dependencies |
