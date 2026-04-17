# Workflow & Best Practices

## Observability Implementation Lifecycle

### Phase 1: Assessment & Planning

**Discovery Checklist:**
- [ ] Inventory all services and dependencies
- [ ] Identify critical user journeys
- [ ] Document existing monitoring gaps
- [ ] Define SLO targets with stakeholders
- [ ] Establish tagging standards

**Tagging Strategy:**
```yaml
Required Tags:
  - env: [prod, staging, dev]
  - service: [service-name]
  - team: [owning-team]
  
Recommended Tags:
  - version: [git-sha or semver]
  - region: [aws-region]
  - tier: [critical, standard, internal]
```

### Phase 2: Infrastructure Deployment

**Kubernetes Installation:**
```bash
# Add repository
helm repo add datadog https://helm.datadoghq.com
helm repo update

# Install with best practices
helm install datadog datadog/datadog \
  --set datadog.apiKey=$DD_API_KEY \
  --set datadog.appKey=$DD_APP_KEY \
  --set datadog.site=datadoghq.com \
  --set datadog.tags={env:production} \
  --set datadog.apm.enabled=true \
  --set datadog.apm.instrumentation.enabled=true \
  --set datadog.logs.enabled=true \
  --set datadog.logs.containerCollectAll=true \
  --set datadog.processAgent.enabled=true \
  --set datadog.networkMonitoring.enabled=true \
  --set datadog.securityAgent.runtime.enabled=true \
  --set datadog.systemProbe.enabled=true \
  --set datadog.systemProbe.enableUSM=true
```

**Validation Steps:**
1. Check Agent status: `datadog-agent status`
2. Verify APM: Send test trace
3. Test log collection: `datadog-agent stream-logs`
4. Confirm system probe: `datadog-agent system-probe status`

### Phase 3: Application Instrumentation

**Auto-Instrumentation (Recommended):**
```yaml
# Kubernetes Admission Controller
podAnnotations:
  admission.datadoghq.com/enabled: "true"
  admission.datadoghq.com/config.mode: "socket"
  
env:
  - name: DD_ENV
    value: "production"
  - name: DD_SERVICE
    valueFrom:
      fieldRef:
        fieldPath: metadata.labels['app']
```

**Manual Instrumentation (Python Example):**
```python
from ddtrace import tracer, patch_all
from ddtrace.propagation.http import HTTPPropagator

patch_all()

# Custom spans
@tracer.wrap(service="payment-api", resource="/charge")
def process_payment(request):
    with tracer.trace("validate_card") as span:
        span.set_tag("card.type", request.card_type)
        result = validate_card(request)
        span.set_metric("validation.ms", result.duration)
        return result
```

### Phase 4: Alerting Configuration

**Alert Hierarchy:**
```
SLO Alerts (Highest Priority)
├── Burn rate > 14.4x (1h window) → P1
├── Burn rate > 6x (6h window) → P2
└── Budget exhaustion < 10% → P1

Symptom-Based Alerts
├── Error rate > threshold → P2
├── Latency p99 > threshold → P2
└── Availability drops → P1

Infrastructure Alerts
├── Resource utilization → P3
├── Anomaly detection → P4
└── Capacity planning → P4
```

### Phase 5: Runbook Development

**Runbook Template:**
```markdown
# Alert: [Alert Name]

## Overview
- **Severity**: P1/P2/P3/P4
- **Service**: [Service Name]
- **SLO Impact**: Yes/No

## Symptoms
[List observable symptoms]

## Diagnostic Steps
1. [Step 1 with Datadog links]
2. [Step 2 with queries]
3. [Step 3]

## Resolution
1. [Immediate mitigation]
2. [Root cause fix]
3. [Verification steps]

## Escalation
- Contact: @team-oncall
- Secondary: @engineering-manager
- War room: #incidents-channel
```

### Phase 6: Ongoing Optimization

**Weekly Tasks:**
- Review triggered alerts for false positives
- Check dashboard usage and deprecate unused
- Monitor custom metric cardinality

**Monthly Tasks:**
- SLO review with stakeholders
- Cost analysis and optimization
- Runbook updates based on incidents

**Quarterly Tasks:**
- Full SLO reassessment
- Architecture review for new services
- Tool consolidation evaluation
