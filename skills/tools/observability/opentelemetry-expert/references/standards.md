# Standards & Reference

## 7.1 Official Documentation

- [OpenTelemetry Docs](https://opentelemetry.io/docs/)
- [OTLP Protocol Specification](https://opentelemetry.io/docs/specs/otlp/)
- [Collector Configuration](https://opentelemetry.io/docs/collector/configuration/)
- [Semantic Conventions](https://opentelemetry.io/docs/specs/otel/trace/semantic_conventions/)
- [Metrics Data Model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/)
- [Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [Language SDKs](https://opentelemetry.io/docs/languages/)
- [Operator for Kubernetes](https://opentelemetry.io/docs/kubernetes/operator/)
- [Collector Exporter Matrix](https://opentelemetry.io/docs/collector/exporter/)

## 7.2 Configuration Reference

### OTel Collector (otelcol-config.yml)

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

  jaeger:
    protocols:
      thrift_http:
        endpoint: 0.0.0.0:14268
      grpc:
        endpoint: 0.0.0.0:14250

  prometheus:
    config:
      scrape_configs:
        - job_name: 'otel-collector'
          static_configs:
            - targets: ['localhost:8888']
        - job_name: 'app-metrics'
          static_configs:
            - targets: ['app:9090']

  hostmetrics:
    collection_interval: 30s
    scrapers:
      cpu: {}
      disk: {}
      filesystem: {}
      load: {}
      memory: {}
      network: {}
      process: {}

processors:
  batch:
    timeout: 10s
    send_batch_size: 1024

  memory_limiter:
    check_interval: 1s
    limit_mib: 512
    spike_limit_mib: 128

  k8sattributes:
    passthrough: false
    filter:
      node_from_env_var: KUBE_NODE_NAME
    extract:
      metadata:
        - deployment.name
        - k8s.deployment.uid
        - k8s.pod.name
        - k8s.pod.uid
        - k8s.namespace.name
        - container.name
        - container.image.name
        - container.image.tag
        - cloud.provider
        - cloud.region

  resource:
    attributes:
      - action: upsert
        key: service.namespace
        value: production
      - action: upsert
        key: deployment.environment
        value: ${DEPLOYMENT_ENV}

  resourcedetection:
    detectors: [gce, k8s, ec2, azure]

  transform:
    error_mode: ignore
    traces:
      statements:
        - replace_pattern(attributes["http.url"], pattern="api_key=[^&]+", replacement="api_key=REDACTED")
    metrics:
      statements:
        - set(attributes["metric.unit"], "1") where attributes["metric.unit"] == ""

exporters:
  otlp/tempo:
    endpoint: tempo:4317
    tls:
      insecure: false
      cert_file: /certs/client.crt
      key_file: /certs/client.key
      ca_file: /certs/ca.crt

  otlphttp/prometheus:
    endpoint: http://prometheus:9090
    tls:
      insecure: true

  prometheus:
    endpoint: "0.0.0.0:8889"
    namespace: otel
    const_labels:
      service: otel-collector

  logging:
    verbosity: detailed
    sampling_initial: 5
    sampling_thereafter: 200

extensions:
  zpages:
    endpoint: localhost:55679

  health_check:
    endpoint: 0.0.0.0:13133

  pprof:
    endpoint: localhost:1777

  file_storage:
    directory: /var/lib/otelcol/file_storage

service:
  extensions: [health_check, pprof, zpages, file_storage]
  pipelines:
    traces:
      receivers: [otlp, jaeger]
      processors: [memory_limiter, batch, resource, k8sattributes]
      exporters: [otlp/tempo, logging]
    metrics:
      receivers: [prometheus, hostmetrics, otlp]
      processors: [memory_limiter, batch, resourcedetection]
      exporters: [prometheus, otlphttp/prometheus, logging]
    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch, transform]
      exporters: [logging]
```

### Auto-Instrumentation (Java)

```bash
# With OpenTelemetry Java agent
java -javaagent:opentelemetry-javaagent.jar \
  -Dotel.service.name=my-service \
  -Dotel.exporter.otlp.endpoint=http://collector:4317 \
  -Dotel.metrics.exporter=otlp \
  -Dotel.logs.exporter=otlp \
  -Dotel.propagators=tracecontext,baggage \
  -Dotel.resource.attributes=deployment.environment=production \
  -Dotel.traces.sampler=parentbased_traceidratio \
  -Dotel.traces.sampler.param=0.1 \
  -Dotel.instrumentation.http.enabled=true \
  -Dotel.instrumentation.jdbc.enabled=true \
  -Dotel.instrumentation.redis.enabled=true \
  -Dotel.exporter.otlp.traces.protocol=grpc \
  -Dotel.exporter.otlp.metrics.protocol=http/protobuf \
  -Dotel.javaagent.debugging=true \
  -jar my-app.jar
```

### Collector with TLS (otelcol-tls.yml)

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
        tls:
          cert_file: /certs/server.crt
          key_file: /certs/server.key
          client_ca_file: /certs/ca.crt

exporters:
  otlp/secure:
    endpoint: collector.internal:5317
    tls:
      insecure: false
      cert_file: /certs/client.crt
      key_file: /certs/client.key
      ca_file: /certs/ca.crt

processors:
  batch:
    timeout: 5s
    send_batch_size: 512

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [otlp/secure]
```

## 7.3 Common Commands

### OTel Collector

| Command | Description |
|---------|-------------|
| `otelcol --config=config.yml` | Start collector with config |
| `otelcol --version` | Show version |
| `otelcol --health` | Check health |
| `otelcol components` | List available components |
| `otelcol validate-config --config=config.yml` | Validate config syntax |

### Kubernetes Operator

| Command | Description |
|---------|-------------|
| `kubectl apply -f otel-collector.yaml` | Deploy collector CR |
| `kubectl get otelcol` | List collectors |
| `kubectl describe otelcol` | Show collector status |
| `kubectl logs -l app=opentelemetry` | View collector logs |

### Auto-Instrumentation

| Command | Description |
|---------|-------------|
| `java -javaagent:agent.jar ...` | Start with Java agent |
| `DD_SERVICE=my-app ddtrace-run python app.py` | Python auto-instrumentation |
| `node --require ./instrumentation.js app.js` | Node.js instrumentation |

## 7.4 Semantic Conventions

### HTTP Trace Attributes

```
service.name              # Service identifier
service.version           # Service version
service.namespace         # Logical namespace
deployment.environment    # Environment (production, staging)

http.method               # HTTP method
http.url                  # Full URL (redact secrets)
http.target               # Request path
http.host                 # Host header
http.scheme               # http/https
http.status_code          # Response status
http.user_agent           # User-Agent header
http.request_content_length
http.response_content_length

http.route                # Route pattern (e.g., /users/:id)
http.client_ip            # Client IP address

db.system                 # Database type (postgresql, mysql, mongodb)
db.name                   # Database name
db.statement              # Query (redact params)
db.operation              # Operation (SELECT, INSERT)
db.sql.table              # Table name

messaging.system          # Queue system (kafka, rabbitmq)
messaging.destination      # Queue name
messaging.operation       # publish, receive
messaging.kafka.partition

rpc.system                # gRPC, thrift, etc.
rpc.method                # Method name
rpc.grpc.status_code

net.peer.name             # Peer hostname
net.peer.ip               # Peer IP
net.peer.port             # Peer port
net.host.ip               # Host IP
```

## 7.5 Version Compatibility

| OTel Version | Collector | SDK | Status |
|-------------|-----------|-----|--------|
| 2.x | 0.110+ | 2.x | Current (stable) |
| 1.x | 0.50-0.109 | 1.x | Maintenance |
| 0.x | 0.1-0.49 | 0.x | Deprecated |

### SigNoz OTel Config Example

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

exporters:
  otlp/sigNoz:
    endpoint: "ingest.signoz.io:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": "${SIGNOZ_TOKEN}"

  prometheus:
    endpoint: "0.0.0.0:8889"

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [otlp/sigNoz]
    metrics:
      receivers: [otlp]
      exporters: [otlp/sigNoz]
    logs:
      receivers: [otlp]
      exporters: [otlp/sigNoz]
```
