# Scenario Examples

## 9.1 Service Level Objectives (SLO) Monitoring

**User:** "How do we track SLOs for our API with Prometheus?"

**Expert:**
> **Solution with Recording Rules:**
>
> 1. Define SLI metrics (requests, errors, latency)
> 2. Create recording rules for SLO calculations
> 3. Create alerting rules for budget burn
>
> ```yaml
> groups:
>   - name: slo-api-availability
>     interval: 60s
>     rules:
>       # Availability SLI (99.9% = 0.001 error budget)
>       - record: slo:requests_total:rate5m
>         expr: |
>           sum(rate(http_requests_total{service="api"}[5m]))
>
>       - record: slo:errors_total:rate5m
>         expr: |
>           sum(rate(http_requests_total{service="api",status=~"5.."}[5m]))
>
>       - record: slo:error_ratio:5m
>         expr: |
>           slo:errors_total:rate5m / slo:requests_total:rate5m
>
>       - record: slo:error_budget_remaining:5m
>         expr: |
>           1 - (slo:errors_total:rate5m / (slo:requests_total:rate5m * 0.001))
>
>       # Latency SLI (P99 < 500ms)
>       - record: slo:http_request_duration_seconds:p99:5m
>         expr: |
>           histogram_quantile(0.99,
>             sum(rate(http_request_duration_seconds_bucket{service="api"}[5m])) by (le)
>           )
>
>       - record: slo:latency_budget_remaining:5m
>         expr: |
>           1 - (slo:http_request_duration_seconds:p99:5m / 0.5)
>
>   - name: slo-alerts
>     interval: 60s
>     rules:
>       - alert: SLOErrorBudgetBurnFast
>         expr: |
>           (
>             sum(rate(http_requests_total{service="api",status=~"5.."}[1h]))
>             / sum(rate(http_requests_total{service="api"}[1h]))
>           ) / 0.001 > 1
>         for: 5m
>         labels:
>           severity: warning
>           slo: availability
>         annotations:
>           summary: "API availability error budget burning at >1x"
>           description: "Error budget is depleting faster than sustainable. Budget will be exhausted in {{ $value | printf \"%.0f\" }} hours."
>
>       - alert: SLOErrorBudgetExhausted
>         expr: slo:error_budget_remaining:5m < 0
>         for: 0m
>         labels:
>           severity: critical
>           slo: availability
>         annotations:
>           summary: "API availability SLO breached"
>           description: "30-day error budget has been exhausted. Immediate action required."
> ```

## 9.2 Multi-Instance Load Balancer Monitoring

**User:** "How do I monitor 20 instances of my service and identify which one is misbehaving?"

**Expert:**
> **Solution with Topk/Grouping:**
>
> ```promql
> # Overall service health
> sum(rate(http_requests_total{service="api"}[5m]))

> # Requests per instance
> sum by (instance) (rate(http_requests_total{service="api"}[5m]))

> # Error rate per instance
> sum by (instance) (rate(http_requests_total{service="api",status=~"5.."}[5m]))
>   / sum by (instance) (rate(http_requests_total{service="api"}[5m]))

> # P99 latency per instance
> histogram_quantile(0.99,
>   sum by (instance, le) (rate(http_request_duration_seconds_bucket{service="api"}[5m]))
> )

> # Find outliers (instances with >2x average error rate)
> (
>   sum by (instance) (rate(http_requests_total{service="api",status=~"5.."}[5m}))
>   / sum by (instance) (rate(http_requests_total{service="api"}[5m]))
> )
> > 2 * (
>     sum(rate(http_requests_total{service="api",status=~"5.."}[5m]))
>     / sum(rate(http_requests_total{service="api"}[5m]))
>   )

> # Top 5 slowest instances by P99
> topk(5,
>   histogram_quantile(0.99,
>     sum by (instance, le) (rate(http_request_duration_seconds_bucket{service="api"}[5m]))
>   )
> )
> ```

## 9.3 Kubernetes Resource Utilization

**User:** "How do we track CPU/memory requests vs actual usage in Kubernetes?"

**Expert:**
> **Solution:**
>
> ```promql
> # CPU: Request vs Actual
> (
>   sum by (namespace, pod) (rate(container_cpu_usage_seconds_total[5m]))
>   / on(namespace, pod) group_left
>   sum by (namespace, pod) (kube_pod_container_resource_requests{resource="cpu"})
> ) * 100

> # Memory: Request vs Actual
> (
>   sum by (namespace, pod) (container_memory_usage_bytes)
>   / on(namespace, pod) group_left
>   sum by (namespace, pod) (kube_pod_container_resource_requests{resource="memory"})
> ) * 100

> # Pods at risk (>90% of request)
> (
>   sum by (namespace, pod) (rate(container_cpu_usage_seconds_total[5m]))
>   / on(namespace, pod) group_left
>   sum by (namespace, pod) (kube_pod_container_resource_requests{resource="cpu"})
> ) > 0.9

> # Namespace-level utilization
> sum by (namespace) (container_memory_usage_bytes)
>   / on(namespace) group_left
> sum by (namespace) (kube_namespace_resource_limits{resource="memory"})

> # HPA readiness based on CPU
> sum by (namespace, deployment) (rate(container_cpu_usage_seconds_total[5m]))
>   / on(namespace, deployment) group_left
> sum by (namespace, deployment) (kube_pod_container_resource_requests{resource="cpu"})
> ```
>
> **Grafana dashboard panels:**
> - CPU Utilization % (requests vs actual)
> - Memory Utilization % (limits vs actual)
> - Top consumers by namespace
> - Pods approaching limits

## 9.4 Canary Deployment Analysis

**User:** "How do we compare metrics between stable and canary versions?"

**Expert:**
> **Solution with Relabeling:**
>
> ```yaml
> # prometheus.yml
> scrape_configs:
>   - job_name: 'kubernetes-pods'
>     kubernetes_sd_configs:
>       - role: pod
>     relabel_configs:
>       - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
>         target_label: service
>       - source_labels: [__meta_kubernetes_pod_label_version]
>         target_label: version
>       - source_labels: [__meta_kubernetes_pod_label_track]
>         target_label: track
>         regex: (.+)
>         replacement: ${1}
> ```
>
> ```promql
> # Compare request rates
> sum by (track) (rate(http_requests_total[5m]))

> # Compare error rates
> sum by (track) (rate(http_requests_total{status=~"5.."}[5m]))
>   / sum by (track) (rate(http_requests_total[5m]))

> # Compare P99 latency
> histogram_quantile(0.99,
>   sum by (track, le) (rate(http_request_duration_seconds_bucket[5m])) by (track, le)
> )

> # Alert if canary error rate is higher than stable by 5%
> (
>   sum(rate(http_requests_total{track="canary",status=~"5.."}[5m]))
>   / sum(rate(http_requests_total{track="canary"}[5m]))
> )
> > 1.05 * (
>     sum(rate(http_requests_total{track="stable",status=~"5.."}[5m]))
>     / sum(rate(http_requests_total{track="stable"}[5m]))
>   )
> ```

## 9.5 Continuous Profiling Integration

**User:** "How do we correlate Prometheus metrics with Pyroscope profiles?"

**Expert:**
> **Solution:**
>
> 1. Deploy Pyroscope server alongside Prometheus
> 2. Instrument applications with Pyroscope SDK
> 3. Configure Grafana datasources for both
>
> ```yaml
> # Prometheus scrape config for Pyroscope
> scrape_configs:
>   - job_name: 'pyroscope'
>     static_configs:
>       - targets: ['pyroscope:4040']
> ```
>
> **Correlation query:**
> ```promql
> # Find pods with high CPU
> topk(5,
>   sum by (pod) (rate(container_cpu_usage_seconds_total[5m]))
> )
>
> # Use instance label to link to Pyroscope profile
> # Grafana Explore: Select Pyroscope, filter by pod name
> ```
>
> **Grafana linking:**
> ```json
> {
>   "links": [
>     {
>       "title": "Pyroscope Profile",
>       "type": "link",
>       "url": "https://pyroscope.example/explore?query=${__field.name}&from=${__from}&until=${__to}",
>       "internal": false
>     }
>   ]
> }
> ```

## 9.6 Troubleshooting: High Cardinality

**User:** "Our Prometheus is running out of memory. How do we diagnose high cardinality?"

**Expert:**
> **Diagnosis:**
>
> ```bash
> # Check cardinality by metric name
> curl -s 'localhost:9090/api/v1/label/__name__/values' | jq '.data | length'

> # Get cardinality estimates via TSDB
> curl -s localhost:9090/api/v1/status/tsdb | jq '.data.seriesCountByMetricName'

> # Check top metrics by cardinality
> curl -s localhost:9090/api/v1/status/tsdb | jq '.data.labelValueCountByLabelName | sort_by(.value) | reverse | .[:20]'
> ```
>
> **Common causes:**
> - High-cardinality labels (user_id, session_id, request_id)
> - Unbounded label values (URLs with IDs)
> - Missing label grouping
> - Too many unique metric names
>
> **Solutions:**
> ```yaml
> # Use recording rules to pre-aggregate
> - record: service:request_count:sum
>   expr: sum by (service, status) (rate(http_requests_total[5m]))

> # Use relabeling to drop high-cardinality labels
> relabel_configs:
>   - source_labels: [request_id]
>     action: labeldrop

> # Use metric_relabel_configs to drop expensive metrics
> metric_relabel_configs:
>   - source_labels: [__name__]
>     regex: 'expensive_debug_metric'
>     action: drop
> ```
