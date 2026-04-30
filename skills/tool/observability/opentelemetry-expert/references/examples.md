# OpenTelemetry Expert — Example Interactions

This file contains detailed example interactions referenced from SKILL.md §10.

---

## Example 1: Instrument a Python FastAPI Service

**User:** "Help me instrument a FastAPI application with OpenTelemetry for traces and metrics"

**OTel Expert:**
> **Step-by-Step Setup:**
>
> **1. Install Dependencies:**
> ```bash
> pip install opentelemetry-api \
>     opentelemetry-sdk \
>     opentelemetry-exporter-otlp-proto-grpc \
>     opentelemetry-instrumentation-fastapi \
>     opentelemetry-instrumentation-requests \
>     opentelemetry-instrumentation-psycopg2 \
>     opentelemetry-instrumentation-logging
> ```
>
> **2. Create OpenTelemetry setup module (`otel.py`):**
> ```python
> from opentelemetry import trace, metrics
> from opentelemetry.sdk.trace import TracerProvider
> from opentelemetry.sdk.metrics import MeterProvider
> from opentelemetry.sdk.trace.export import BatchSpanProcessor
> from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
> from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
> from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
> from opentelemetry.sdk.resources import Resource, SERVICE_NAME, DEPLOYMENT_ENVIRONMENT
> from opentelemetry.sdk.propagate import set_global_textmap
> from opentelemetry.propagators.b3 import B3MultiFormat
> from opentelemetry.semconv.resource import ResourceAttributes
>
> def setup_otel():
>     resource = Resource.create({
>         SERVICE_NAME: "checkout-api",
>         SERVICE_VERSION: "1.0.0",
>         DEPLOYMENT_ENVIRONMENT: "production",
>         ResourceAttributes.HOST_NAME: gethostname(),
>     })
>
>     # Configure tracing
>     trace_provider = TracerProvider(resource=resource)
>     trace.set_tracer_provider(trace_provider)
>
>     # Export to Collector
>     trace_provider.add_span_processor(
>         BatchSpanProcessor(
>             OTLPSpanExporter(
>                 endpoint="http://otel-collector:4317",
>                 insecure=True,
>             )
>         )
>     )
>
>     # Configure metrics
>     meter_provider = MeterProvider(
>         resource=resource,
>         metric_readers=[
>             PeriodicExportingMetricReader(
>                 OTLPMetricExporter(
>                     endpoint="http://otel-collector:4317",
>                     insecure=True,
>                 ),
>                 export_interval_millis=60000,
>             )
>         ],
>     )
>     metrics.set_meter_provider(meter_provider)
>
>     # Configure propagator (B3 for Zipkin compatibility)
>     set_global_textmap(B3MultiFormat())
>
>     return trace.get_tracer(__name__), metrics.get_meter(__name__)
> ```
>
> **3. Instrument FastAPI (`main.py`):**
> ```python
> from fastapi import FastAPI
> from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
> from opentelemetry.instrumentation.requests import RequestsInstrumentor
>
> app = FastAPI()
>
> # Import and setup
> from otel import setup_otel
> tracer, meter = setup_otel()
>
> # Auto-instrument FastAPI
> FastAPIInstrumentor.instrument_app(app)
> RequestsInstrumentor().instrument()
>
> # Create custom metrics
> request_counter = meter.create_counter(
>     name="checkout.requests",
>     description="Number of checkout requests",
> )
>
> @app.post("/checkout")
> def checkout(cart_id: str):
>     request_counter.add(1, {"cart_id": cart_id})
>
>     with tracer.start_as_current_span("checkout.process") as span:
>         span.set_attribute("cart.id", cart_id)
>         # Process checkout...
>         return {"status": "success"}
> ```
>
> **4. Environment Variables (alternative to code):**
> ```bash
> export OTEL_SERVICE_NAME=checkout-api
> export OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
> export OTEL_EXPORTER_OTLP_INSECURE=true
> export OTEL_PROPAGATORS=b3
> export OTEL_TRACES_SAMPLER=parentbased_traceidratio
> export OTEL_TRACES_SAMPLER_ARG=0.1
> ```

---

## Example 2: Configure Tail-Based Sampling for Errors

**User:** "I want to capture 100% of error traces but only 1% of successful traces to save cost"

**OTel Expert:**
> **Collector Tail Sampling Configuration:**
>
> ```yaml
> receivers:
>   otlp:
>     protocols:
>       grpc:
>         endpoint: 0.0.0.0:4317
>       http:
>         endpoint: 0.0.0.0:4318
>
> processors:
>   # Memory limiter to prevent OOM
>   memory_limiter:
>     check_interval: 1s
>     limit_mib: 512
>     spike_limit_mib: 64
>
>   # Batch before sampling
>   batch:
>     timeout: 10s
>     send_batch_size: 8192
>
>   # Tail-based sampling
>   tail_sampling:
>     decision_wait: 30s
>     num_traces: 100000
>     expected_new_traces_per_sec: 1000
>     policies:
>       # Policy 1: Always sample errors
>       - name: errors-policy
>         type: status_code
>         status_code: { status_codes: [ERROR] }
>
>       # Policy 2: Always sample slow traces (>2s)
>       - name: slow-traces-policy
>         type: latency
>         latency: { threshold_ms: 2000 }
>
>       # Policy 3: Sample by trace ID (1% of successful traces)
>       - name: probabilistic-policy
>         type: probabilistic
>         probabilistic: { sampling_percentage: 1 }
>
>       # Policy 4: Keep traces with specific service name
>       - name: critical-service-policy
>         type: string_attribute
>         string_attribute:
>           key: service.name
>           values: [checkout-api, payment-service]
>
> exporters:
>   otlp/tempo:
>     endpoint: tempo:4317
>
> service:
>   pipelines:
>     traces:
>       receivers: [otlp]
>       processors: [memory_limiter, batch, tail_sampling]
>       exporters: [otlp/tempo]
> ```

---

## Example 3: Multi-Service Distributed Tracing with Context Propagation

**User:** "I have a frontend React app calling a backend API which calls a database. How do I trace this end-to-end?"

**OTel Expert:**
> **Architecture:**
> ```
> React (Browser)
>   → Backend API (Node.js)
>     → Database Service (Python)
> ```
>
> **Step 1: Configure Context Propagation**
>
> Frontend (React + OTel JS Browser SDK):
> ```javascript
> import { WebTracerProvider } from '@opentelemetry/sdk-trace-web';
> import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
> import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base';
> import { W3CTraceContextPropagator } from '@opentelemetry/core';
>
> const provider = new WebTracerProvider();
> provider.addSpanProcessor(new BatchSpanProcessor(
>   new OTLPTraceExporter({ url: 'http://otel-collector:4318/v1/traces' })
> ));
>
> provider.register({ propagator: new W3CTraceContextPropagator() });
> ```
>
> Backend (Node.js):
> ```javascript
> import { NodeSDK } from '@opentelemetry/sdk-node';
> import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';
>
> const sdk = new NodeSDK({
>   traceExporter: new OTLPTraceExporter({ url: 'http://otel-collector:4317' }),
> });
> sdk.start();
> ```
>
> **Result in Trace Viewer:**
> ```
> trace_id: abc123
> spans:
>   [browser] GET / → 10ms
>     [backend] /api/checkout → 50ms
>       [db-service] db.checkout → 30ms
> ```

---

## Edge Cases (from §11)

### Baggage for Cross-Service Business Context
```python
from opentelemetry import baggage
baggage.set_baggage("user.id", user_id)
```

### gRPC vs HTTP Context Propagation
```python
from opentelemetry.propagators.composite import CompositePropagator
set_global_textmap(CompositePropagator([
    W3CTraceContextPropagator(),
    JaegerPropagator(),
]))
```

### Database Connection Pool Instrumentation
```yaml
processors:
  filter/spans:
    traces:
      exclude:
        match_type: strict
        attributes:
          - key: db.system
            value: connection_pool
```

### Kubernetes Auto-Detection
```yaml
processors:
  k8sattributes:
    passthrough: true
    extract:
      metadata:
        - k8s.namespace.name
        - k8s.deployment.name
        - k8s.pod.name
```

### Log Correlation to Traces
```python
from opentelemetry.sdk._logs import LoggingHandler
handler = LoggingHandler(trace.get_tracer_provider())
logging.root.addHandler(handler)
```

### High-Volume Services (Aggressive Sampling)
```bash
OTEL_TRACES_SAMPLER: parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG: "0.01"
```

### SDK Version Mismatches
```yaml
processors:
  transform:
    trace_statements:
      - context: span
        statements:
          - replace_pattern(attributes["http.target"], "pattern", "replacement")
```

### Collector High Availability
```yaml
exporters:
  otlp:
    endpoint: "http://collector-lb:4317"
    reconnection_delay: 10s
```
