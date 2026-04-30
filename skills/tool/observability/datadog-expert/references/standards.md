# Standards & Reference

## Official Documentation

| Resource | URL |
|----------|-----|
| Datadog Docs | https://docs.datadoghq.com/ |
| API Reference | https://docs.datadoghq.com/api/latest/ |
| Integrations | https://docs.datadoghq.com/integrations/ |
| APM Tracing | https://docs.datadoghq.com/tracing/ |
| OpenTelemetry | https://docs.datadoghq.com/opentelemetry/ |
| Universal Service Monitoring | https://docs.datadoghq.com/universal_service_monitoring/ |
| Security Platform | https://docs.datadoghq.com/security/ |

## Datadog Company Facts (2026)

| Metric | Value |
|--------|-------|
| Founded | 2010 |
| CEO | Olivier Pomel (Co-founder) |
| Headquarters | New York, NY |
| Employees | 8,100+ (35+ countries) |
| Customers | 32,700+ |
| Fortune 500 | 48% are customers |
| FY2026 Revenue Guidance | $4.06-4.10B |
| Q4 2025 Revenue | $953M (+29% YoY) |
| Integrations | 1,000+ |

## Configuration Reference

### datadog.yaml (Agent Configuration)

```yaml
# API Configuration
api_key: ${DD_API_KEY}
site: datadoghq.com
hostname: my-host

# Tags
tags:
  - env:production
  - service:myapp
  - team:platform
  - region:us-east-1

# APM Configuration
apm_config:
  enabled: true
  env: production
  analyzed_spans:
    web|http.request: 1
    db|postgres.query: 0.1

# Log Collection
logs_enabled: true
logs_config:
  container_collect_all: true
  processing_rules:
    - type: exclude_at_match
      name: exclude_health_checks
      pattern: /health

# System Probe (eBPF)
system_probe_config:
  enabled: true
  enable_usm: true
  enable_oom_kill: true

# Process Monitoring
process_config:
  enabled: true
  process_collection:
    enabled: true
```

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DD_API_KEY` | API authentication | `abc123...` |
| `DD_APP_KEY` | App authentication | `def456...` |
| `DD_SITE` | Datadog site | `datadoghq.com` |
| `DD_TAGS` | Global tags | `env:prod,team:platform` |
| `DD_ENV` | Default environment | `production` |
| `DD_SERVICE` | Default service name | `payment-api` |
| `DD_VERSION` | Service version | `v2.3.1` |
| `DD_TRACE_ENABLED` | Enable APM tracing | `true` |
| `DD_TRACE_SAMPLE_RATE` | Global sample rate | `0.1` |
| `DD_LOGS_ENABLED` | Enable log collection | `true` |
| `DD_PROCESS_AGENT_ENABLED` | Enable process monitoring | `true` |

## Metrics Reference

### Custom Metric Types

| Type | Use Case | Example |
|------|----------|---------|
| `gauge` | Point-in-time value | Current queue depth |
| `count` | Event counter | Total requests |
| `histogram` | Distribution with percentiles | Request latency |
| `distribution` | Global percentiles | Cross-host aggregation |
| `rate` | Events per second | Error rate |

### Reserved Metric Prefixes

| Prefix | Purpose |
|--------|---------|
| `datadog.*` | Internal Datadog metrics |
| `system.*` | System-level metrics |
| `docker.*` | Container metrics |
| `kubernetes.*` | K8s metrics |
| `trace.*` | APM trace metrics |
| `usm.*` | Universal Service Monitoring |

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/v1/validate` | GET | Validate API key |
| `/api/v1/series` | POST | Submit metrics |
| `/api/v1/check_run` | POST | Submit service checks |
| `/api/v1/events` | POST | Submit events |
| `/api/v1/log` | POST | Submit logs |
| `/api/v1/apm/traces` | POST | Submit traces |
| `/api/v1/monitor` | POST/PUT | Create/update monitors |
| `/api/v1/dashboard` | POST/PUT | Create/update dashboards |
| `/api/v2/slo` | POST/PUT | Create/update SLOs |

## Version Compatibility

| Component | Current | Supported | EOL |
|-----------|---------|-----------|-----|
| Datadog Agent | 7.63+ | 7.x | - |
| ddtrace (Python) | 2.x | 1.x, 2.x | 0.x |
| ddtrace (Java) | 1.x+ | 1.x | 0.x |
| Helm Chart | 3.x | 3.x | 2.x |
