# promql Example

```
# Rate with correct interval (prevents gaps)
rate(http_requests_total{service="checkout"}[$__rate_interval])

# Availability (success rate)
1 - (
  rate(http_requests_total{service="checkout", status=~"5.."}[$__rate_interval])
  /
  rate(http_requests_total{service="checkout"}[$__rate_interval])
)

# Latency percentiles (p50, p95, p99)
histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{service="checkout"}[$__rate_interval]))
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{service="checkout"}[$__rate_interval]))
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{service="checkout"}[$__rate_interval]))

# Current vs 7-day comparison
# Legend: {{instance}}
current: rate(http_requests_total{service="checkout"}[5m])
7d_ago: rate(http_requests_total{service="checkout"}[5m] offset 7d)
ratio: current / (rate(http_requests_total{service="checkout"}[5m] offset 7d))

# CPU usage percentage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle", instance="$instance"}[$__rate_interval])) * 100)

# Memory usage percentage
100 * (1 - (
  avg by (instance) (node_memory_MemAvailable_bytes{instance="$instance"})
  /
  avg by (instance) (node_memory_MemTotal_bytes{instance="$instance"})
))

# Active connections
sum(tcp_heap_size{instance="$instance"})

# Error rate with labels
sum by (service, status) (rate(http_requests_total{status=~"5.."}[$__rate_interval]))
```
