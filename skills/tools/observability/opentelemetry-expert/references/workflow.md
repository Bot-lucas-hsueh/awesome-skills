# Standard Workflow

## 8.1 Getting Started

```
Phase 1: Choose Your Path
├── Option A: Managed Collector (SigNoz, Jaeger, Grafana Tempo)
├── Option B: Self-hosted OTel Collector
└── Option C: Vendor-specific agents (Datadog, New Relic)

Phase 2: Instrumentation
├── Auto-instrumentation for supported languages
├── Manual SDK for custom spans and metrics
├── Add propagators (W3C TraceContext, B3)
└── Configure sampling strategy

Phase 3: Backend Setup
├── Deploy OTel Collector (Kubernetes/Docker)
├── Configure exporters (Jaeger, Prometheus, Loki)
├── Set up trace/metrics correlation
└── Verify data flow with test spans

Phase 4: Production
├── Enable TLS between components
├── Configure resource attributes
├── Set up tail-based sampling
└── Add business metrics
```

## 8.2 Common Workflows

### Manual Instrumentation (Go)

```go
package main

import (
    "context"
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/sdk/resource"
    "go.opentelemetry.io/otel/trace"
)

func initTracer(ctx context.Context) (func(context.Context), error) {
    exporter, err := otlptracegrpc.New(ctx,
        otlptracegrpc.WithEndpoint("otel-collector:4317"),
        otlptracegrpc.WithInsecure(),
    )
    if err != nil {
        return nil, err
    }

    res, _ := resource.Merge(
        resource.Default(),
        resource.NewWithAttributes(
            "https://opentelemetry.io/schemas/1.20.0",
            attribute.String("service.name", "my-service"),
            attribute.String("deployment.environment", "production"),
        ),
    )

    tp := trace.NewTracerProvider(
        trace.WithBatcher(exporter),
        trace.WithResource(res),
        trace.WithSampler(trace.ParentBased(trace.TraceIDRatioBased(0.1))),
    )

    otel.SetTracerProvider(tp)

    return func(ctx context.Context) {
        tp.Shutdown(ctx)
    }, nil
}

func handleRequest(ctx context.Context) {
    tracer := otel.Tracer("my-service")

    ctx, span := tracer.Start(ctx, "handleRequest",
        trace.WithAttributes(
            attribute.String("http.method", "GET"),
            attribute.String("http.route", "/api/users"),
        ),
    )
    defer span.End()

    ctx, childSpan := tracer.Start(ctx, "fetchUser")
    user, err := db.Query(ctx, "SELECT * FROM users WHERE id = ?", userID)
    if err != nil {
        childSpan.RecordError(err)
        childSpan.SetStatus(codes.Error, err.Error())
    }
    childSpan.End()

    span.SetAttributes(attribute.Int("user.count", len(user)))
}
```

### Auto-Instrumentation Setup (Python)

```python
# requirements.txt
opentelemetry-api
opentelemetry-sdk
opentelemetry-instrumentation-flask
opentelemetry-instrumentation-requests
opentelemetry-exporter-otlp

# app.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Configure tracing
resource = Resource(attributes={
    SERVICE_NAME: "my-flask-app",
    "deployment.environment": "production"
})
trace.set_tracer_provider(TracerProvider(resource=resource))

# Export to collector
exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(exporter))

# Instrument Flask
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
```

### Kubernetes Deployment

```yaml
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
  name: cluster-collector
spec:
  mode: daemonset
  config: |
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
      memory_limiter:
        check_interval: 1s
        limit_mib: 512
      k8sattributes:
        extract:
          metadata:
            - k8s.namespace.name
            - k8s.pod.name
            - k8s.deployment.name
    exporters:
      otlp:
        endpoint: "tempo:4317"
        tls:
          insecure: false
    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [memory_limiter, k8sattributes, batch]
          exporters: [otlp]
```

## 8.3 Auto-Instrumentation Agents

### Java Agent Setup

```bash
# Download latest agent
curl -L -O https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar

# Configure via environment
export OTEL_SERVICE_NAME=my-app
export OTEL_EXPORTER_OTLP_ENDPOINT=http://collector:4317
export OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=grpc
export OTEL_METRICS_EXPORTER=none
export OTEL_LOGS_EXPORTER=none
export OTEL_TRACES_SAMPLER=parentbased_traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.1
export OTEL_PROPAGATORS=tracecontext,baggage

# Start application
java -javaagent:opentelemetry-javaagent.jar \
     -jar my-app.jar
```

### Node.js Auto-Instrumentation

```javascript
// instrumentation.js
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-grpc');

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: 'http://collector:4317',
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-http': {
        ignoreIncomingPaths: ['/health', '/metrics'],
      },
      '@opentelemetry/instrumentation-express': {
        enabled: true,
      },
    }),
  ],
});

sdk.start();
process.on('SIGTERM', () => sdk.shutdown());
```

## 8.4 Testing Workflow

```bash
# Validate collector config
otelcol validate-config --config=otelcol-config.yml

# Test with ephemeral collector
docker run --rm \
  -v $(pwd)/config.yml:/etc/otelcol/config.yml \
  otel/opentelemetry-collector-contrib:0.110.0 \
  otelcol --config=/etc/otelcol/config.yml

# Send test trace
curl -X POST http://localhost:4318/v1/traces \
  -H "Content-Type: application/json" \
  -d '[{
    "resourceSpans": [{
      "resource": {
        "attributes": [
          {"key": "service.name", "value": {"stringValue": "test-service"}}
        ]
      },
      "scopeSpans": [{
        "spans": [{
          "traceId": "00000000000000000000000000000001",
          "spanId": "0000000000000001",
          "name": "test-span",
          "kind": 1,
          "startTimeUnixNano": "1700000000000000000",
          "endTimeUnixNano": "1700000001000000000"
        }]
      }]
    }]
  }]'
```

## 8.5 Migration from Legacy Agents

### Jaeger to OTel Collector

```yaml
# Old: Direct Jaeger agent
jaeger:
  agent:
    endpoint: localhost:6831

# New: OTel Collector with Jaeger receiver
receivers:
  jaeger:
    protocols:
      thrift_http:
        endpoint: localhost:14268
      grpc:
        endpoint: localhost:14250

processors:
  transform:
    traces:
      statements:
        - replace_pattern(attributes["db.statement"], pattern="\\?([0-9]+)", replacement="?$1")

exporters:
  otlp/tempo:
    endpoint: tempo:4317

service:
  pipelines:
    traces:
      receivers: [jaeger]
      processors: [transform, batch]
      exporters: [otlp/tempo]
```
