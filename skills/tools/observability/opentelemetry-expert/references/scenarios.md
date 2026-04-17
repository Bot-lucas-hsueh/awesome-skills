# Scenario Examples

## 9.1 Multi-Service Distributed Tracing

**User:** "We have 5 microservices (API Gateway, Auth, Users, Orders, Payments). How do we trace requests across all of them?"

**Expert:**
> **Solution:**
>
> 1. Deploy OTel Collector as sidecar for each service
> 2. Instrument with W3C TraceContext propagators
> 3. Configure batch exporters with retries
> 4. Enable k8sattributes processor for pod metadata
>
> ```yaml
> # api-gateway sidecar
> receivers:
>   otlp:
>     protocols:
>       grpc:
>         endpoint: localhost:4317
>
> exporters:
>   otlp/tempo:
>     endpoint: tempo:4317
>     tls:
>       insecure: false
>     sending_queue:
>       num_consumers: 10
>       queue_size: 10000
>
> processors:
>   batch:
>     timeout: 1s
>     send_batch_size: 100
>
> service:
>   pipelines:
>     traces:
>       receivers: [otlp]
>       exporters: [otlp/tempo]
> ```
>
> **Code propagation:**
> ```go
> // Inject trace context into downstream calls
> func callDownstream(ctx context.Context, url string) (*http.Request, error) {
>     req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
>     // W3C TraceContext injected automatically by OTel SDK
>     return req, nil
> }
> ```

## 9.2 Tail-Based Sampling

**User:** "We have 10,000 requests/second and can't afford to store all traces. How do we sample intelligently?"

**Expert:**
> **Solution: OTel Collector with tail sampling:**
>
> 1. First stage: Head-based sampling (1% of traffic)
> 2. Second stage: Tail sampling for errors and slow traces
>
> ```yaml
> receivers:
>   otlp:
>     protocols:
>       grpc:
>         endpoint: 0.0.0.0:4317

> processors:
>   tail_sampling:
>     decision_wait: 10s
>     num_traces: 100000
>     expected_new_traces_per_sec: 1000
>     policies:
>       # Always sample errors
>       - name: errors-policy
>         type: status_code
>         status_code: {status_codes: [ERROR]}
>       # Always sample slow traces
>       - name: slow-traces-policy
>         type: latency
>         latency: {threshold_ms: 1000}
>       # Sample 10% of everything else
>       - name: otherwise-10-percent
>         type: probabilistic
>         probabilistic: {sampling_percentage: 10}
>       # Keep traces with specific service
>       - name: payments-policy
>         type: string_attribute
>         string_attribute:
>           key: service.name
>           values: [payments, billing]

> exporters:
>   otlp/tempo:
>     endpoint: tempo:4317

> service:
>   pipelines:
>     traces:
>       receivers: [otlp]
>       processors: [tail_sampling, batch]
>       exporters: [otlp/tempo]
> ```

## 9.3 Correlating Traces with Logs

**User:** "How do I link traces to application logs?"

**Expert:**
> **Solution with OTel:**
>
> 1. Inject trace context into logs (TraceID, SpanID)
> 2. Configure log processor to extract context
> 3. Use Grafana Loki with derived fields
>
> **Go example:**
> ```go
> import (
>     "go.opentelemetry.io/otel/trace"
>     "go.opentelemetry.io/otel/log"
> )
>
> func processOrder(ctx context.Context) {
>     span := trace.SpanFromContext(ctx)
>     traceID := span.SpanContext().TraceID().String()
>     spanID := span.SpanContext().SpanID().String()
>
>     logger.Info("Processing order",
>         "trace_id", traceID,
>         "span_id", spanID,
>         "order_id", orderID,
>     )
> }
> ```
>
> **Log format (JSON with trace context):**
> ```json
> {
>   "timestamp": "2024-01-15T10:30:00Z",
>   "level": "info",
>   "message": "Processing order",
>   "service": "order-service",
>   "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
>   "span_id": "00f067aa0ba902b7",
>   "order_id": "ORD-12345"
> }
> ```
>
> **Loki derived field config:**
> ```yaml
> derivedFields:
>   - name: trace_id
>     matcherRegex: '"trace_id":"([a-f0-9]+)"'
>     url: "http://tempo:3200/api/traces/$${1}"
>     datasourceUid: tempo
> ```

## 9.4 Business Metrics from Traces

**User:** "How do I extract business KPIs from trace data?"

**Expert:**
> **Solution with Span Metrics connector:**
>
> ```yaml
> receivers:
>   otlp:
>     protocols:
>       grpc:
>         endpoint: 0.0.0.0:4317

> processors:
>   spanmetrics:
>     metrics_exporter: prometheus
>     latency_histogram_buckets: [10ms, 25ms, 50ms, 100ms, 250ms, 500ms, 1s, 2.5s, 5s, 10s]
>     dimensions:
>       - name: http.method
>         default: ""
>       - name: http.status_code
>         default: ""
>       - name: service.name
>         default: ""
>       - name: operation.name
>         default: ""

> exporters:
>   prometheus:
>     endpoint: "0.0.0.0:8889"

> service:
>   pipelines:
>     traces:
>       receivers: [otlp]
>       processors: [spanmetrics, batch]
>       exporters: [prometheus]
> ```
>
> **Resulting metrics:**
> - `traces_span_metrics_duration_milliseconds_bucket{operation_name="POST /orders"}`
> - `traces_span_metrics_calls_total{service_name="order-service", status_code="200"}`

## 9.5 Kubernetes Workload Telemetry

**User:** "How do we automatically add Kubernetes metadata to all telemetry data?"

**Expert:**
> **Solution:**
>
> ```yaml
> receivers:
>   otlp:
>     protocols:
>       grpc:
>         endpoint: 0.0.0.0:4317

> processors:
>   k8sattributes:
>     # Connect to Kubernetes API
>     auth_type: serviceAccount
>     passthrough: false
>
>     # Filter by namespace
>     filter:
>       node_from_env_var: KUBE_NODE_NAME
>
>     # Extract metadata from pod/namespace
>     extract:
>       metadata:
>         # Pod metadata
>         - k8s.pod.name
>         - k8s.pod.uid
>         - k8s.deployment.name
>         - k8s.namespace.name
>         - k8s.node.name
>         - k8s.pod.start_time
>         # Container metadata
>         - container.name
>         - container.id
>         - container.image.name
>         - container.image.tag
>         - container.runtime
>       # Extract from pod labels
>       labels:
>         - from: pod
>           key: app.kubernetes.io/name
>         - from: pod
>           key: app.kubernetes.io/version
>         - from: pod
>           key: version
>
>     # Associate containers with pods
>     pod_association:
>       - sources:
>           - from: resource_attribute
>             name: k8s.pod.uid
>       - sources:
>           - from: resource_attribute
>             name: k8s.pod.name
>           - from: resource_attribute
>             name: k8s.namespace.name

> exporters:
>   prometheusremotewrite:
>     endpoint: http://mimir:8080/api/v1/write

> service:
>   pipelines:
>     traces:
>       receivers: [otlp]
>       processors: [k8sattributes, batch]
>       exporters: [prometheusremotewrite]
>     metrics:
>       receivers: [otlp]
>       processors: [k8sattributes]
>       exporters: [prometheusremotewrite]
>     logs:
>       receivers: [otlp]
>       processors: [k8sattributes]
>       exporters: [prometheusremotewrite]
> ```

## 9.6 Troubleshooting: Missing Spans

**User:** "Some of our traces are missing spans. How do we diagnose?"

**Expert:**
> **Diagnosis Steps:**
>
> 1. **Check OTel SDK export errors:**
> ```bash
> curl localhost:8888/metrics | grep otel
> # Look for exporter_error_count, export_errors
> ```
>
> 2. **Check collector logs:**
> ```bash
> kubectl logs -n otel -l app=collector --tail=100 | grep -i error
> ```
>
> 3. **Common causes:**
>    - **Network issues**: Collector unreachable from app
>    - **Buffer overflow**: Send queue full, increase `sending_queue.queue_size`
>    - **Sampling**: Tail sampling dropping traces
>    - **Exporter errors**: Wrong endpoint, TLS issues
>    - **Memory pressure**: `memory_limiter` dropping data
>
> 4. **Fix configuration:**
> ```yaml
> exporters:
>   otlp:
>     endpoint: collector:4317
>     timeout: 30s
>     retry_on_failure:
>       enabled: true
>       initial_interval: 1s
>       max_interval: 30s
>       max_elapsed_time: 5m
>     sending_queue:
>       enabled: true
>       num_consumers: 10
>       queue_size: 10000
>       storage: file_storage
> ```
>
> 5. **Test connectivity:**
> ```bash
> # From app pod
> grpcurl -plaintext collector:4317 list
> # Should show grpc.health.v1.Health
> ```
