# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Prevention |
|---|---------|----------|--------|------------|
| 1 | **Alert fatigue from duplicate alerts** | 🔴 High | Engineers ignore critical alerts | Configure aggregation/suppression rules |
| 2 | **Noisy services with hundreds of triggers** | 🔴 High | Buries real incidents | Set up event orchestration |
| 3 | **Missing escalation policy** | 🔴 Critical | Incidents go unhandled | Always define escalation chain |
| 4 | **Test alerts sent to production** | 🟠 Medium | Accidental incident creation | Use separate test services |
| 5 | **Ignored acknowledgements** | 🔴 High | Engineer marked "acknowledged" but didn't act | Audit acknowledgment patterns |
| 6 | **No maintenance windows during deploys** | 🟡 Medium | Alert storm during rollout | Schedule maintenance windows |
| 7 | **Single point of contact** | 🟠 Medium | One person unavailable = unhandled incident | Always have backup |
| 8 | **Inconsistent priority levels** | 🟡 Medium | Misaligned expectations | Document priority definitions |

### Anti-Pattern: Alert Fatigue

**Bad Practice:**
```yaml
# Every single monitoring check fires independently
# 50 CPU alerts for 50 servers = chaos
alerts:
  - name: high-cpu
    expr: cpu_usage > 80
    for: 0m  # Immediate trigger
    
# Alertmanager sends each as separate PagerDuty event
receivers:
  - pagerduty_configs:
      - service_key: 'xxx'
```

**Good Practice:**
```yaml
# Group alerts by service, aggregate
alerts:
  - name: high-cpu
    expr: avg(cpu_usage) by (service) > 80
    for: 5m  # Wait 5 minutes
    labels:
      severity: warning
      service: '{{ $labels.service }}'

# Alertmanager groups by service
route:
  group_by: ['service', 'severity']
  group_wait: 60s  # Wait to see if more alerts come in
  group_interval: 5m
  repeat_interval: 1h
```

### Anti-Pattern: Missing Context

**Bad Practice:**
```json
{
  "routing_key": "xxx",
  "event_action": "trigger",
  "payload": {
    "summary": "Error",
    "severity": "critical"
  }
}
```

**Good Practice:**
```json
{
  "routing_key": "xxx",
  "event_action": "trigger",
  "payload": {
    "summary": "[PROD] Payment service: Error rate spike - 15% of transactions failing (threshold: 1%)",
    "source": "prometheus/payment-monitoring",
    "severity": "critical",
    "component": "stripe-integration",
    "group": "payments",
    "class": "error-rate-spike",
    "custom_details": {
      "service": "payment-api",
      "environment": "production",
      "error_rate": "15.2%",
      "threshold": "1%",
      "affected_users": "~2,400 in last 5 minutes",
      "primary_error": "Stripe API timeout (code: 500)",
      "grafana_dashboard": "https://grafana.company.com/d/payments",
      "logs": "https://logs.company.com/payments?q=error"
    },
    "links": [
      {
        "href": "https://runbooks.company.com/payment-errors",
        "text": "Payment Errors Runbook"
      }
    ]
  }
}
```

## 10.2 Anti-Patterns

### Anti-Pattern 1: "Catch-All" Service

**Problem:** One PagerDuty service receives all alerts regardless of team or type.

**Why It's Bad:**
- No clear ownership
- Everyone gets paged for everything
- Impossible to set proper escalation paths
- Alert noise is unbearable

**Solution:**
```yaml
# Create service-per-team structure
resource "pagerduty_service" "api_platform" {
  name = "API Platform"
  # ...
}

resource "pagerduty_service" "data_pipeline" {
  name = "Data Pipeline"
  # ...
}

resource "pagerduty_service" "authentication" {
  name = "Authentication"
  # ...
}
```

### Anti-Pattern 2: Infinite Escalation Loops

**Problem:** Alert triggers -> engineer acknowledges but doesn't fix -> alert re-fires -> escalates again

**Why It's Bad:**
- Wastes engineer time
- Causes alert fatigue
- Can page executives unnecessarily

**Solution:**
```yaml
# Set auto-resolution for self-healing systems
resource "pagerduty_service" "api" {
  name                 = "API Platform"
  auto_resolve_timeout = 14400  # 4 hours - auto-resolve if no update
  acknowledgement_timeout = 1800  # 30 min warning
}

# Configure alert to auto-resolve when condition clears
alert: HighLatency
expr: http_request_duration_seconds > 5
for: 10m
labels:
  severity: warning

# Alertmanager: resolve event when alert clears
receivers:
  - name: 'pagerduty'
    pagerduty_configs:
      - send_resolved: true  # CRITICAL: send resolution events
```

### Anti-Pattern 3: Manual Incident Creation

**Problem:** Engineers manually create incidents instead of using automated monitoring.

**Why It's Bad:**
- Human error (forgot to create incident)
- No correlation with other alerts
- Breaks analytics and reporting

**Solution:**
```bash
# Always prefer automated creation through monitoring
# If manual creation is needed, use standardized format:

pd-cli incidents create \
  --title "[MANUAL] Investigating customer report of checkout failures" \
  --service payment-service \
  --priority P2 \
  --assignee ONCALL_ENGINEER_ID \
  --body "Customer reported via support: Unable to complete purchase at 14:30 PST. Investigating correlation with recent Stripe API changes."
```

### Anti-Pattern 4: No On-Call Rotation Policy

**Problem:** Informal "whoever sees it first" approach to on-call.

**Why It's Bad:**
- No accountability
- Burnout for conscientious engineers
- No clear handoff

**Solution:**
```yaml
# Clear, documented rotation
resource "pagerduty_schedule" "backend_oncall" {
  name      = "Backend On-Call Schedule"
  time_zone = "America/Los_Angeles"
  
  layer {
    name             = "Weekly Rotation"
    start            = "2024-01-01T09:00:00-08:00"
    rotation_length  = 1
    rotation_turns   = 1
    users            = [
      pagerduty_user.engineer1.id,
      pagerduty_user.engineer2.id,
      pagerduty_user.engineer3.id,
      pagerduty_user.engineer4.id
    ]
  }
}

# Document rules:
# - Primary on-call: Must acknowledge within 15 minutes
# - Secondary on-call: Escalation target after 15 minutes
# - Manager: Escalation target after 30 minutes
# - CTO: Final escalation for P1 after 1 hour
```

### Anti-Pattern 5: Ignoring Post-Mortems

**Problem:** Incidents are resolved but never analyzed for root cause.

**Why It's Bad:**
- Same incidents recur
- No process improvement
- Missed opportunities for automation

**Solution:**
```yaml
# Require post-mortem for all P1 and P2 incidents
resource "pagerduty_business_rule" "postmortem_required" {
  name        = "Post-Mortem Requirement"
  description = "Auto-create post-mortem task for high-severity incidents"
  
  conditions {
    expr = "incident.priority in ['P1', 'P2']"
  }
  
  actions {
    create_task {
      title       = "Post-Mortem: {{ incident.title }}"
      description = "Complete post-mortem within 5 business days"
      assignee    = incident.last_acknowledged_by
      due_in      = "5d"
    }
    
    notify {
      channel   = "#postmortems"
      template  = "new-postmortem-required"
    }
  }
}
```
