# Datadog APM & Distributed Tracing Reference

> Complete guide to application performance monitoring and distributed tracing

---

## APM Setup by Language

### Java

**VM Arguments:**
```bash
-javaagent:/opt/dd-java-agent.jar \
-Ddd.service=my-service \
-Ddd.env=production \
-Ddd.version=1.0.0 \
-Ddd.tags=team:platform,tier:critical \
-Ddd.agent.host=localhost \
-Ddd.agent.port=8126
```

**Environment Variables:**
```bash
export DD_SERVICE=my-service
export DD_ENV=production
export DD_VERSION=1.0.0
export DD_AGENT_HOST=localhost
export DD_TRACE_SAMPLE_RATE=1.0
export DD_PROFILING_ENABLED=true
```

### Python

**Installation:**
```bash
pip install ddtrace
```

**Auto-Instrumentation:**
```bash
ddtrace-run python app.py
```

**Code Instrumentation:**
```python
from ddtrace import tracer, patch
from ddtrace.pin import Pin

# Enable integrations
patch(flask=True, requests=True, psycopg2=True)

# Custom span
@tracer.wrap(service="payment-api", resource="process_payment")
def process_payment(order_id):
    with tracer.trace("payment.process") as span:
        span.set_tag("order.id", order_id)
        span.set_metric("payment.amount", amount)
        # ...
```

### Node.js

**Installation:**
```bash
npm install dd-trace
```

**Initialization:**
```javascript
// Must be first import
tracer.init({
  service: 'my-service',
  env: 'production',
  version: '1.0.0',
  logInjection: true,
  profiling: true,
  runtimeMetrics: true
});

// Auto-instrument all integrations
tracer.use('express');
tracer.use('http');
tracer.use('mongodb');
tracer.use('redis');
```

### Go

**Installation:**
```bash
go get gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer
```

**Basic Setup:**
```go
package main

import (
    "gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer"
)

func main() {
    tracer.Start(
        tracer.WithService("my-service"),
        tracer.WithEnv("production"),
        tracer.WithServiceVersion("1.0.0"),
    )
    defer tracer.Stop()
    
    // Your application code
}
```

### .NET

**Installation:**
```bash
dotnet add package Datadog.Trace
```

**Environment Variables:**
```bash
export CORECLR_ENABLE_PROFILING=1
export CORECLR_PROFILER={846F5F1C-F9AE-4B07-969E-05C26BC060D8}
export CORECLR_PROFILER_PATH=/opt/datadog/Datadog.Trace.ClrProfiler.Native.so
export DD_DOTNET_TRACER_HOME=/opt/datadog
export DD_SERVICE=my-service
export DD_ENV=production
```

---

## OpenTelemetry Integration

### Collector Configuration
```yaml
# otel-collector.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 10s
    send_batch_size: 1024

exporters:
  datadog:
    api:
      key: ${DD_API_KEY}
      site: datadoghq.com
    tags:
      - env:production
      - team:platform

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [datadog]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [datadog]
```

### OTLP Ingest (Direct)
```yaml
# datadog-agent.yaml
datadog:
  otlp:
    receiver:
      protocols:
        grpc:
          enabled: true
          endpoint: 0.0.0.0:4317
        http:
          enabled: true
          endpoint: 0.0.0.0:4318
```

---

## Custom Instrumentation

### Span Creation
```python
from ddtrace import tracer

# Create a span
with tracer.trace("web.request", service="web-frontend") as span:
    span.set_tag("http.method", "GET")
    span.set_tag("http.url", "/api/users")
    span.set_metric("http.response_size", 1024)
    
    # Add error info
    try:
        process_request()
    except Exception as e:
        span.set_traceback()
        span.set_tag("error.msg", str(e))
```

### Span Links (Async Operations)
```python
# Start parent span
with tracer.trace("parent-operation") as parent_span:
    # Get context for async operation
    context = parent_span.context
    
    # Later, in async callback
    with tracer.trace("async-operation") as child_span:
        child_span.link_span(context)
```

### Resource Naming
Best practices for span resource names:
- `GET /api/users/{id}` — REST API endpoint
- `SELECT users` — Database query type
- `send_email` — Function/operation name
- `kafka.consume` — Message queue operation

---

## Sampling Configuration

### Head-Based Sampling
```yaml
# datadog.yaml
apm_config:
  enabled: true
  # Global sampling rate
  max_traces_per_second: 100
  
  # Service-specific sampling
  analyzed_spans:
    web|http.request: 1
    api|flask.request: 0.5
    worker|celery.run: 0.1
```

### Environment Variables
```bash
export DD_TRACE_SAMPLE_RATE=0.5
export DD_TRACE_RATE_LIMIT=100
```

### Remote Sampling (Agent Controlled)
```python
# Dynamic sampling via Datadog UI
# Navigate to: APM > Setup & Configuration > Retention Filters
```

---

## Continuous Profiler

### Enable Profiling
```bash
# Python
export DD_PROFILING_ENABLED=true
export DD_PROFILING_CPU_ENABLED=true
export DD_PROFILING_HEAP_ENABLED=true

# Java
-Ddd.profiling.enabled=true
-Ddd.profiling.allocation.enabled=true
```

### Profile Types
- **CPU** — Time spent in methods
- **Memory Allocation** — Object allocation tracking
- **Wall Time** — Real-time method duration
- **Exception** — Exception profiling
- **Lock** — Contention analysis

---

## Trace Analytics

### Trace Search & Analytics
```sql
-- Find slow database queries
@duration:>1s @db.system:postgresql resource_name:SELECT*

-- Error analysis
status:error service:payment-api @http.status_code:500

-- Custom business metrics
@order.value:>1000 @customer.tier:premium
```

### Retention Filters
```hcl
# Configure via UI or API
# Keep 100% of errors
resource "datadog_retention_filter" "errors" {
  query       = "status:error"
  sample_rate = 1.0
  name        = "Keep All Errors"
}

# Sample successful traces
resource "datadog_retention_filter" "success" {
  query       = "status:ok"
  sample_rate = 0.1
  name        = "Sample 10% Success"
}
```

---

## Service Catalog

### Service Definition (API)
```json
{
  "schema-version": "v2.1",
  "dd-service": "payment-api",
  "team": "payments",
  "application": "ecommerce-platform",
  "tier": "critical",
  "lifecycle": "production",
  "contacts": [
    {
      "type": "slack",
      "contact": "#payments-team"
    },
    {
      "type": "email",
      "contact": "payments-oncall@company.com"
    }
  ],
  "links": [
    {
      "type": "runbook",
      "url": "https://wiki.internal/payment-runbook"
    },
    {
      "type": "repo",
      "url": "https://github.com/company/payment-api"
    }
  ],
  "tags": ["language:python", "framework:fastapi"]
}
```

---

## APM Alerting

### Latency Alert
```hcl
resource "datadog_monitor" "high_latency" {
  name = "Payment API High Latency"
  type = "metric alert"
  
  query = <<-EOT
    avg(last_5m):avg:trace.payment-api.request.duration{env:production} by {resource_name} > 500
  EOT
  
  thresholds {
    critical = 500
    warning  = 300
  }
  
  message = <<-EOT
    High latency detected on {{resource_name.name}}
    Current p99: {{value}}ms
    
    @pagerduty-payments-oncall
  EOT
}
```

### Error Rate Alert
```hcl
resource "datadog_monitor" "error_rate" {
  name = "Payment API Error Rate"
  type = "metric alert"
  
  query = <<-EOT
    avg(last_5m):(
      sum:trace.payment-api.request.errors{env:production}.as_rate() /
      sum:trace.payment-api.request.hits{env:production}.as_rate()
    ) * 100 > 5
  EOT
  
  message = <<-EOT
    Error rate is {{value}}% on payment-api
    
    Check the Trace Search for details:
    https://app.datadoghq.com/apm/traces?query=service:payment-api%20status:error
    
    @pagerduty-payments-oncall
  EOT
}
```
