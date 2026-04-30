# Datadog Example Interactions

## Example 1: Investigate High Latency in Checkout Service

**Step 3: Analyze database spans**
```sql
-- In Trace Search, filter:
service:checkout-api AND resource:db.query AND duration:>100ms
-- Identify which queries are slow
```

**Step 6: Create latency monitor**
```
Query: avg:trace.checkout.duration{service:checkout-api}.as_count() by {resource}
Alert when: p99 > 1s for 5 minutes
```

## Example 2: Set Up SLO Alert for Payment Service

**1. Define the SLO:**
```
Setup → Services → Payment Service → SLOs → New SLO
Name: Payment Success Rate
Target: 99.5%
Window: 30-day rolling
Metric:
  good: sum:trace.payment.request{status:200,service:payment-api}.as_count()
  total: sum:trace.payment.request{service:payment-api}.as_count()
```

**2. Create burn rate alerts:**
```
Monitor → New Monitor → SLO Alert
SLO: Payment Success Rate

Alert thresholds:
  Critical (1h window): burn_rate > 14.4  → Page immediately
  Warning (6h window):  burn_rate > 6     → Slack alert
  Warning (3d window):   burn_rate > 2      → Slack alert
```

**3. Alert message template:**
```
Payment SLO (99.5%) error budget at risk.
Burn rate: {{burnRate}}x over {{window}}
Remaining budget: {{budgetRemaining}}%
{{#is_alert}} Escalate to payment-team immediately. {{/is_alert}}
Runbook: https://wiki.example.com/payment-slo-runbook
```

## Example 3: Create Production Log Pipeline

**Step 1: Create Pipeline:**
```
Logs → Pipelines → New Pipeline
Name: Application Logs - Production
Filter: service:our-app AND env:prod
```

**Step 2: Add Grok Parser:**
```
Processor: Grok Parser
Log Message: %{timestamp:timestamp} %{word:level} %{notSpace:logger} - %{data:message}

Advanced:
  timestamp: parse date using format "yyyy-MM-dd HH:mm:ss.SSS"
```

**Step 3: Add Category Processor:**
```
Processor: Category Processor
Name: Log Level Normalization
Target: level
Mappings:
  error, err, fatal, EXCEPTION → ERROR
  warn, WARNING                → WARN
  info, INFO                   → INFO
  debug, DEBUG, TRACE          → DEBUG
```

**Step 4: Add Exclusion Filter:**
```
Filter: Exclude logs where:
  level:DEBUG OR message matches /health.?check/i
```

**Step 5: Add Remapper (for trace correlation):**
```
Processor: Trace Remapper
Trace ID attribute: dd.trace_id
```
