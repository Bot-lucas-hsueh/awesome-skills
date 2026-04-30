# yaml Example

```
groups:
  - name: application-alerts
    rules:
      # High Error Rate
      - alert: ApplicationHighErrorRate
        expr: |
          100 * (
            sum by (service, namespace) (
              rate(http_requests_total{status=~"5.."}[5m])
            )
            /
            sum by (service, namespace) (
              rate(http_requests_total[5m])
            )
          ) > 5
        for: 5m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "High error rate on {{ $labels.service }}"
          description: "Error rate is {{ $value | printf \"%.2f\" }}% on {{ $labels.service }} in {{ $labels.namespace }}"
          runbook_url: "https://wiki.example.com/runbooks/high-error-rate"

      # High Latency
      - alert: ApplicationHighLatency
        expr: |
          histogram_quantile(0.99,
            sum by (le, service, namespace) (
              rate(http_request_duration_seconds_bucket[5m])
            )
          ) > 2
        for: 5m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High latency on {{ $labels.service }}"
          description: "p99 latency is {{ $value | printf \"%.3f\" }}s"

      # Service Down
      - alert: ServiceDown
        expr: up{job=~".*app.*"} == 0
        for: 1m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "{{ $labels.job }} is down"
          description: "{{ $labels.job }} has been down for more than 1 minute"

      # Pod Not Ready
      - alert: K8sPodNotReady
        expr: |
          kube_pod_status_ready{namespace="production", condition="true"} == 0
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "Pod {{ $labels.pod }} not ready"
          description: "Pod has been NotReady for more than 10 minutes"

      # Pod OOMKilled
      - alert: K8sPodOOMKilled
        expr: |
          increase(kube_pod_container_status_last_terminated_reason{
            reason="OOMKilled",
            namespace="production"
          }[5m]) > 0
        labels:
          severity: warning
        annotations:
          summary: "Pod {{ $labels.pod }} was OOMKilled"

      # Disk Space Low
      - alert: DiskSpaceLow
        expr: |
          (
            node_filesystem_avail_bytes{fstype!~"tmpfs|fuse.lxcfs", mountpoint="/"}
            /
            node_filesystem_size_bytes{fstype!~"tmpfs|fuse.lxcfs", mountpoint="/"}
          ) < 0.15
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Disk space is low on {{ $labels.instance }}"
          description: "Only {{ $value | humanize1024 }}B remaining on {{ $labels.instance }}"

  - name: recording-rules
    rules:
      # Pre-compute SLO metrics
      - record: service:request_success:rate5m
        expr: |
          sum by (service, namespace) (
            rate(http_requests_total[5m])
          )
          -
          sum by (service, namespace) (
            rate(http_requests_total{status=~"5.."}[5m])
          )

      - record: service:error_rate:rate5m
        expr: |
          100 * (
            sum by (service, namespace) (
              rate(http_requests_total{status=~"5.."}[5m])
            )
            /
            sum by (service, namespace) (
              rate(http_requests_total[5m])
            )
          )

      - record: service:request_latency_p99:rate5m
        expr: |
          histogram_quantile(0.99,
            sum by (le, service, namespace) (
              rate(http_request_duration_seconds_bucket[5m])
            )
          )
```
