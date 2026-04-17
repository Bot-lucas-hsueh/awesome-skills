# Prometheus Expert — Example Interactions

This file contains detailed example interactions referenced from SKILL.md §10.

---

## Example 1: Calculate SLO Error Budget

**User:** "Help me calculate the error budget for our checkout service with a 99.9% availability SLO over 30 days"

**Prometheus Expert:**
> **Error Budget Calculation:**
>
> **1. Query Current Error Rate:**
> ```promql
> # 30-day average error rate
> 100 * (
>   1 - (
>     sum(
>       increase(http_requests_total{
>         service="checkout",
>         namespace="production",
>         status=~"2.."
>       }[30d])
>     )
>     /
>     sum(
>       increase(http_requests_total{
>         service="checkout",
>         namespace="production"
>       }[30d])
>     )
>   )
> )
> ```
>
> **2. Calculate Total Allowed Errors:**
> ```promql
> # Total allowed 5xx errors for 99.9% SLO
> # Budget = (1 - 0.999) * total_requests
> # In last 30 days:
> sum(increase(http_requests_total{
>   service="checkout",
>   namespace="production"
> }[30d])) * 0.001
> ```
>
> **3. Calculate Remaining Budget:**
> ```promql
> # Total budget - consumed budget = remaining
> (
>   sum(increase(http_requests_total{
>     service="checkout",
>     namespace="production"
>   }[30d])) * 0.001
> )
> -
> (
>   sum(
>     increase(http_requests_total{
>       service="checkout",
>       namespace="production",
>       status=~"5.."
>     }[30d])
>   )
> )
> ```
>
> **4. Burn Rate Alert (1h window):**
> ```promql
> # Alert when burning 14.4x normal rate (4.86% errors)
> # Over 1h: 14.4 * (0.1% / 30d * 1h) = 0.0000048% threshold
> (
>   sum(rate(http_requests_total{
>     service="checkout",
>     namespace="production",
>     status=~"5.."
>   }[1h]))
>   /
>   sum(rate(http_requests_total{
>     service="checkout",
>     namespace="production"
>   }[1h]))
> ) > 0.000000048
>
> # More readable: > 4.8e-8 = 0.0000048%
> ```
>
> **5. Dashboard Panels:**
> ```
> Panel 1: Error Rate (%)
>   Query: error_rate:rate30d
>
> Panel 2: Error Budget Consumed (%)
>   Query: 100 * (
>     errors / (total_requests * 0.001)
>   )
>
> Panel 3: Remaining Good Requests
>   Query: total_requests * 0.001 - errors
>
> Panel 4: Burn Rate (multiplier)
>   Query: current_error_rate / acceptable_error_rate
> ```

---

## Example 2: Set Up Blackbox Monitoring for API Endpoints

**User:** "Configure blackbox monitoring for our public API endpoints to detect downtime"

**Prometheus Expert:**
> **Architecture:**
> ```
> Prometheus
>   → blackbox_exporter (HTTP probe)
>     → https://api.example.com/health
>       → Success / HTTP status codes
> ```
>
> **1. Configure blackbox_exporter (`config.yml`):**
> ```yaml
> modules:
>   http_2xx:
>     prober: http
>     http:
>       valid_http_versions: ["HTTP/1.1", "HTTP/2"]
>       valid_status_codes: [200]
>       method: GET
>       headers:
>         User-Agent: Prometheus/blackbox-exporter
>       fail_if_ssl: false
>       fail_if_not_ssl: false
>
>   http_post_2xx:
>     prober: http
>     http:
>       method: POST
>       valid_status_codes: [200, 201, 202]
>       headers:
>         Content-Type: application/json
>       body: '{"endpoint":"health"}'
> ```
>
> **2. Prometheus scrape config:**
> ```yaml
> - job_name: 'blackbox-http'
>   metrics_path: /probe
>   params:
>     module: [http_2xx]
>   static_configs:
>     - targets:
>       - https://api.example.com/health
>       - https://api.example.com/api/v1/users/health
>       - https://checkout.example.com/health
>       - https://payment.example.com/api/health
>   relabel_configs:
>     - source_labels: [__address__]
>       target_label: __param_target
>     - source_labels: [__param_target]
>       regex: '(https?://)?([^/]+)(/.*)?'
>       replacement: '${2}'
>       target_label: instance
>     - target_label: __address__
>       replacement: 'blackbox-exporter:9115'
> ```
>
> **3. Alert rules:**
> ```yaml
> - alert: EndpointDown
>   expr: probe_success == 0
>   for: 2m
>   labels:
>     severity: critical
>   annotations:
>     summary: "Endpoint {{ $labels.instance }} is down"
>     description: "Blackbox probe failed for {{ $labels.instance }}"
>
> - alert: EndpointSlow
>   expr: probe_duration_seconds > 5
>   for: 5m
>   labels:
>     severity: warning
>   annotations:
>     summary: "Endpoint {{ $labels.instance }} is slow"
>     description: "Response time > 5s for {{ $labels.instance }}"
>
> - alert: SSLCertExpiring
>   expr: probe_ssl_earliest_cert_expiry - time() < 86400 * 30
>   labels:
>     severity: warning
>   annotations:
>     summary: "SSL certificate for {{ $labels.instance }} expires soon"
>     description: "Certificate expires in {{ $value | humanizeDuration }}"
> ```
>
> **4. Key metrics from blackbox_exporter:**
> ```promql
> # Is the endpoint up?
> probe_success{instance="api.example.com"}
>
> # HTTP response code
> probe_http_status_code{instance="api.example.com"}
>
> # Response time
> probe_duration_seconds{instance="api.example.com"}
>
> # SSL certificate expiry (days)
> probe_ssl_earliest_cert_expiry{instance="api.example.com"} - time()
>
> # DNS resolution time
> probe_dns_lookup_time_seconds{instance="api.example.com"}
> ```

---

## Example 3: Kubernetes Monitoring with Prometheus Operator

**User:** "Show me how to set up comprehensive Kubernetes monitoring using Prometheus Operator"

**Prometheus Expert:**
> **1. Install kube-prometheus-stack (Helm):**
> ```bash
> helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
> helm repo update
>
> helm install prometheus prometheus-community/kube-prometheus-stack \
>   --namespace monitoring \
>   --create-namespace \
>   --set prometheus.prometheusSpec.retention=30d \
>   --set prometheus.prometheusSpec.replicas=2 \
>   --set prometheus.prometheusSpec.replicaExternalLabelName="" \
>   --set alertmanager.alertmanagerSpec.replicas=2 \
>   --set grafana.enabled=true \
>   --set prometheus-node-exporter.prometheusMonitor.enabled=true
> ```
>
> **2. Create ServiceMonitor for your application:**
> ```yaml
> apiVersion: monitoring.coreos.com/v1
> kind: ServiceMonitor
> metadata:
>   name: checkout-app
>   namespace: production
>   labels:
>     release: prometheus  # Must match Prometheus selector
> spec:
>   jobLabel: checkout
>   selector:
>     matchLabels:
>       app: checkout
>   namespaceSelector:
>     matchNames:
>       - production
>   endpoints:
>     - port: metrics
>       path: /metrics
>       interval: 15s
>       scrapeTimeout: 10s
>       metricRelabelings:
>         # Remove sensitive labels
>         - sourceLabels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
>           action: keep
>           regex: 'true'
>       relabelings:
>         # Override metrics path from annotation
>         - sourceLabels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
>           action: replace
>           target_label: __metrics_path__
>           regex: (.+)
> ```
>
> **3. Create PrometheusRule for alerts:**
> ```yaml
> apiVersion: monitoring.coreos.com/v1
> kind: PrometheusRule
> metadata:
>   name: checkout-alerts
>   namespace: production
>   labels:
>     app: prometheus
> spec:
>   groups:
>     - name: checkout.rules
>       rules:
>         - alert: CheckoutHighErrorRate
>           expr: |
>             100 * (
>               sum(rate(http_requests_total{
>                 service="checkout",
>                 status=~"5.."
>               }[5m]))
>               /
>               sum(rate(http_requests_total{
>                 service="checkout"
>               }[5m]))
>             ) > 5
>           for: 5m
>           labels:
>             severity: critical
>           annotations:
>             summary: "Checkout error rate exceeds 5%"
>             runbook_url: "https://wiki.example.com/runbooks/checkout"
>
>         - alert: CheckoutPodNotReady
>           expr: |
>             kube_pod_status_ready{
>               namespace="production",
>               pod=~"checkout-.*",
>               condition="true"
>             } == 0
>           for: 10m
>           labels:
>             severity: critical
>           annotations:
>             summary: "Checkout pod not ready"
> ```
>
> **4. Configure additionalScrapeTargets in Prometheus:**
> ```yaml
> apiVersion: monitoring.coreos.com/v1
> kind: Prometheus
> metadata:
>   name: prometheus
> spec:
>   # ... other config
>   additionalScrapeConfigs:
>     - job_name: 'custom-metrics'
>       kubernetes_sd_configs:
>         - role: endpoints
>           namespaces:
>             names:
>               - custom-metrics
>       relabel_configs:
>         - source_labels: [__meta_kubernetes_service_name]
>           action: keep
>           regex: custom-metrics-api
>         - source_labels: [__meta_kubernetes_endpoint_port_name]
>           action: keep
>           regex: metrics
> ```
>
> **5. Key Kubernetes metrics from kube-state-metrics:**
> ```promql
> # Deployment replicas
> kube_deployment_spec_replicas{deployment="checkout", namespace="production"}
> kube_deployment_status_replicas_available{deployment="checkout", namespace="production"}
>
> # Pod status
> kube_pod_status_phase{namespace="production", pod=~"checkout-.*"}
> kube_pod_container_status_restarts_total{namespace="production", pod=~"checkout-.*"}
>
> # Resource usage (from cadvisor)
> container_cpu_usage_seconds_total{namespace="production", pod=~"checkout-.*"}
> container_memory_working_set_bytes{namespace="production", pod=~"checkout-.*"}
>
> # HPA status
> kube_horizontalpodautoscaler_status_current_replicas{namespace="production", hpa="checkout-hpa"}
> ```

---

## Edge Cases (from §11)

### High Cardinality from Dynamic Pod Names
```yaml
relabel_configs:
  - source_labels: [__meta_kubernetes_pod_label_pod_template_hash]
    action: keep
```

### Metrics with Duplicate Time Series
```yaml
relabel_configs:
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
    action: replace
    target_label: metrics_path
```

### Missing Metrics from Batch Jobs
```yaml
- job_name: 'batch-jobs'
  static_configs:
    - targets: ['pushgateway:9091']
  metrics_path: /metrics
  relabel_configs:
    - source_labels: [job]
      action: replace
      target_label: batch_job
```

### Querying Data Across Federations
```yaml
- job_name: 'federate'
  honor_labels: true
  params:
    match[]:
      - '{job="kubernetes-nodes"}'
  static_configs:
    - targets: ['thanos-query:9090']
```

### Slow Query with Subqueries
```promql
# Instead of subquery
max_over_time(
  rate(http_requests[5m])[1h:5m]
)

# Use recording rule
record: job:http_requests_max:max5m
expr: max_over_time(rate(http_requests[5m])[5m])

# Then query
max_over_time(job:http_requests_max:max5m[1h])
```

### Alert When Metric Disappears
```promql
alert: ServiceNotReporting
  expr: absent(up{job="checkout"})
  for: 5m
```

### Scrape Config for Sidecar Containers
```yaml
scrape_configs:
  - job_name: 'app-with-sidecar'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        target_label: __param_target
```

### Handling Metric Name Conflicts
```yaml
relabel_configs:
  - source_labels: [job]
    regex: '(.+)'
    replacement: '${1}_exporter'
    target_label: exporter
```
