# Standards & Reference

## 7.1 Official Documentation

- [Prometheus Docs](https://prometheus.io/docs/introduction/overview/)
- [Querying PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- [Storage](https://prometheus.io/docs/prometheus/latest/storage/)
- [Alerting](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
- [Exporters](https://prometheus.io/docs/instrumenting/exporters/)
- [Operator](https://prometheus-operator.dev/)
- [Node Exporter](https://github.com/prometheus/node_exporter)
- [Blackbox Exporter](https://github.com/prometheus/blackbox_exporter)

## 7.2 Configuration Reference

### prometheus.yml

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: production
    env: prod
  scrape_protocols:
    - PrometheusProto
    - OpenMetricsText1.0.0
    - PrometheusText0.0.4

alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - alertmanager:9093
          scheme: https
          tls_config:
            ca_file: /certs/ca.crt
          basic_auth:
            username: alertmanager
            password_file: /secrets/alertmanager_password

rule_files:
  - "/etc/prometheus/rules/*.yml"
  - "/etc/prometheus/rules/*.yaml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
    metrics_path: /metrics
    scheme: http
    scrape_interval: 30s

  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
      - role: node
    relabel_configs:
      - source_labels: [__meta_kubernetes_node_name]
        target_label: instance
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)

  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)

  - job_name: 'blackbox-http'
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
          - https://api.example.com/health
          - https://app.example.com/health
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
      - source_labels: [__param_target]
        target_label: target

  - job_name: 'prometheus-rate-slow'
    static_configs:
      - targets: ['localhost:9090']
    metrics_path: /metrics
    scrape_interval: 5s
    scheme: http
```

### Alerting Rules

```yaml
groups:
  - name: general
    interval: 30s
    rules:
      - alert: HighMemoryUsage
        expr: |
          (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes)
          / node_memory_MemTotal_bytes * 100 > 90
        for: 5m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"
          description: "Memory usage is above 90% for more than 5 minutes (current: {{ $value | printf \"%.2f\" }}%)"
          runbook_url: "https://wiki.example.com/runbooks/high-memory"

      - alert: HighCPUUsage
        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "CPU usage high on {{ $labels.instance }}"
          description: "CPU usage is above 80% for more than 5 minutes"

      - alert: DiskSpaceLow
        expr: |
          (node_filesystem_avail_bytes{mountpoint="/",fstype!="tmpfs"}
           / node_filesystem_size_bytes{mountpoint="/",fstype!="tmpfs"}) < 0.1
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "Disk space low on {{ $labels.instance }}"
          description: "Less than 10% disk space remaining"

      - alert: PrometheusTargetMissing
        expr: up == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Target {{ $labels.job }} is down"
          description: "{{ $labels.job }} has been down for more than 2 minutes"

      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m]))
          / sum(rate(http_requests_total[5m])) > 0.05
        for: 3m
        labels:
          severity: critical
        annotations:
          summary: "High error rate for {{ $labels.service }}"
          description: "Error rate is above 5% for more than 3 minutes"

  - name: sli
    interval: 60s
    rules:
      - alert: SLOErrorBudgetBurn
        expr: |
          (
            sum(rate(http_requests_total{status=~"5.."}[1h]))
            / sum(rate(http_requests_total[1h]))
          ) / 0.001 > 1
        for: 5m
        labels:
          severity: warning
          slo: availability
        annotations:
          summary: "SLO error budget burning fast"
          description: "Error budget is burning at 1x rate. Budget will be exhausted in {{ $value | printf \"%.0f\" }} hours."

      - alert: SLOErrorBudgetExhausted
        expr: |
          (
            sum(rate(http_requests_total{status=~"5.."}[1h]))
            / sum(rate(http_requests_total[1h]))
          ) / 0.001 > 1
        for: 15m
        labels:
          severity: critical
          slo: availability
        annotations:
          summary: "SLO error budget exhausted"
          description: "Error budget has been exhausted. Immediate attention required."

  - name: recording_rules
    interval: 30s
    rules:
      - record: job:http_requests_total:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job, service)

      - record: job:http_request_duration_seconds_bucket:histogram_quantile_99
        expr: |
          histogram_quantile(0.99,
            sum(rate(http_request_duration_seconds_bucket[5m])) by (job, le)
          )

      - record: job:http_request_duration_seconds_mean:rate5m
        expr: |
          sum(rate(http_request_duration_seconds_sum[5m])) by (job)
          / sum(rate(http_request_duration_seconds_count[5m])) by (job)
```

### Remote Write Configuration

```yaml
remote_write:
  - name: long-term-storage
    url: https://mimir.example.com/api/v1/push
    bearer_token_file: /var/run/secrets/mimir-token
    tls_config:
      ca_file: /certs/ca.crt
      cert_file: /certs/client.crt
      key_file: /certs/client.key
    queue_config:
      capacity: 10000
      max_shards: 30
      min_shards: 1
      max_samples_per_send: 2000
      batch_send_deadline: 30s
      retry_on_http_429: true
      min_backoff: 100ms
      max_backoff: 100s
    metadata_config:
      send: true
      send_interval: 1m
    write_relabel_configs:
      - source_labels: [__name__]
        regex: 'expensive_metric.*'
        action: drop
```

## 7.3 Common Commands

### Querying

| Command | Description |
|---------|-------------|
| `up{job="prometheus"}` | Check if targets are up |
| `rate(http_requests_total[5m])` | Request rate over 5m |
| `histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))` | P99 latency |
| `topk(10, sum by (job) (rate(cpu_seconds_total[5m])))` | Top 10 CPU consumers |
| `count by (service) (rate(http_requests_total[5m]))` | Services by request count |
| `avg_over_time(node_load1[5m])` | Average load over 5 minutes |
| `changes(node_cpu_seconds_total[1h])` | CPU mode changes in last hour |
| `vector(1)` | Constant vector for instant alerts |

### Administration

| Command | Description |
|---------|-------------|
| `curl localhost:9090/-/healthy` | Health check |
| `curl localhost:9090/api/v1/status/tsdb` | TSDB status |
| `curl localhost:9090/api/v1/label/__name__/values` | All metric names |
| `curl -X POST localhost:9090/-/reload` | Reload config |
| `curl -X POST localhost:9090/api/v1/admin/tsdb/snapshot` | Create snapshot |

### PromQL Functions

| Function | Usage |
|----------|-------|
| `rate()` | Per-second average rate of increase |
| `irate()` | Instantaneous rate of increase |
| `increase()` | Total increase over time |
| `histogram_quantile()` | Percentile from histogram |
| `label_replace()` | Replace label values |
| `label_join()` | Join multiple labels |
| `group_left()` | Many-to-one matching |
| `absent()` | Detect missing metrics |
| `vector()` | Convert scalar to vector |
| `clamp_max()` | Cap values at maximum |
| `predict_linear()` | Linear prediction |
