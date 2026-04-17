# Standard Workflow

## 8.1 Getting Started

```
Phase 1: Installation
├── Download binary or use Docker
├── Configure prometheus.yml
├── Set up data directory
├── Configure retention policies
└── Start Prometheus

Phase 2: Target Discovery
├── Static configs for known targets
├── Service discovery (Kubernetes, Consul, DNS)
├── Configure relabeling for labels
└── Verify targets in /targets

Phase 3: Metrics Pipeline
├── Deploy exporters (Node, Blackbox, custom)
├── Define recording rules for expensive queries
├── Configure alerting rules with SLIs
└── Set up alertmanager integration

Phase 4: Long-Term Storage
├── Configure remote_write to Mimir/Thanos
├── Set up write relabeling
├── Configure query federation
└── Verify data in long-term store
```

## 8.2 Common Workflows

### Adding a New Service

1. **Instrument the service** with Prometheus client library
2. **Configure scrape target** in prometheus.yml
3. **Add relabel rules** for service-specific labels
4. **Verify metrics** in Prometheus UI
5. **Create recording rules** for dashboard queries
6. **Add alerting rules** based on SLIs

### Creating Effective Dashboards

1. **Start with SLIs** (request rate, error rate, latency)
2. **Add infrastructure metrics** (CPU, memory, disk, network)
3. **Create recording rules** for complex queries
4. **Build panels with `rate()`** over appropriate windows
5. **Use `histogram_quantile()`** for latency percentiles
6. **Add context** with annotations for deployments

### Alert Tuning

1. **Set `for` duration** to avoid flapping alerts
2. **Use `avg_over_time()`** to smooth volatile metrics
3. **Add runbook links** in annotations
4. **Group by severity** and team for routing
5. **Test in staging** before production
6. **Iterate based on false positives**

## 8.3 Kubernetes Deployment

### Prometheus Operator

```yaml
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: prometheus
spec:
  replicas: 2
  retention: 15d
  retentionSize: 50GiB
  resources:
    requests:
      cpu: 500m
      memory: 1Gi
    limits:
      cpu: 2
      memory: 4Gi
  serviceAccountName: prometheus
  serviceMonitorSelector:
    matchLabels:
      team: platform
  ruleSelector:
    matchLabels:
      role: alert-rules
  alerting:
    alertmanagers:
      - namespace: monitoring
        name: alertmanager-main
        port: web
  remoteWrite:
    - url: http://mimir-distributed-query-frontend.monitoring:8080/prometheus
      tlsConfig:
        insecure: false
      queueConfig:
        capacity: 10000
        maxShards: 30
```

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: myapp
  labels:
    team: platform
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
    - port: metrics
      interval: 15s
      path: /metrics
      scheme: http
      tlsConfig:
        insecureSkipVerify: true
  namespaceSelector:
    matchNames:
      - production
```

## 8.4 Docker Compose Setup

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:v2.49.1
    container_name: prometheus
    restart: unless-stopped
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - ./prometheus/rules:/etc/prometheus/rules
      - ./prometheus/certs:/certs
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=15d'
      - '--storage.tsdb.wal-compression'
      - '--web.enable-lifecycle'
      - '--web.console.libraries=/usr/share/prometheus/console_libraries'
      - '--web.console.templates=/usr/share/prometheus/consoles'
    extra_hosts:
      - "host.docker.internal:host-gateway"
    networks:
      - monitoring

  alertmanager:
    image: prom/alertmanager:v0.27.0
    container_name: alertmanager
    restart: unless-stopped
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager/alertmanager.yml:/etc/alertmanager/alertmanager.yml
      - alertmanager-data:/alertmanager
    command:
      - '--config.file=/etc/alertmanager/alertmanager.yml'
      - '--storage.path=/alertmanager'
    networks:
      - monitoring

  node-exporter:
    image: prom/node-exporter:v1.7.0
    container_name: node-exporter
    restart: unless-stopped
    ports:
      - "9100:9100"
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--path.rootfs=/rootfs'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:11.0.0
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    volumes:
      - ./grafana/provisioning:/etc/grafana/provisioning
      - grafana-data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    networks:
      - monitoring

volumes:
  prometheus-data:
  alertmanager-data:
  grafana-data:

networks:
  monitoring:
    driver: bridge
```

## 8.5 Migration to Mimir (Horizontal Scaling)

```yaml
# prometheus.yml remote_write to Mimir
remote_write:
  - name: mimir
    url: https://mimir.example.com/api/v1/push
    bearer_token: ${MIMIR_API_KEY}
    tls_config:
      ca_file: /certs/ca.crt
    queue_config:
      capacity: 100000
      max_shards: 50
      max_samples_per_send: 5000
      batch_send_deadline: 30s
      min_shards: 10
    metadata_config:
      send: true
      send_interval: 1m

# Migration steps:
# 1. Deploy Mimir with Thanos/Mimir operator
# 2. Configure remote_write in Prometheus
# 3. Query via Grafana with Mimir datasource
# 4. Backfill historical data with thanos-backfill
# 5. Enable compactor for storage optimization
```

## 8.6 Alertmanager Configuration

```yaml
global:
  resolve_timeout: 5m
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alerts@example.com'
  smtp_auth_username: 'alerts'
  smtp_auth_password_file: '/secrets/smtp_password'
  slack_api_url: 'https://hooks.slack.com/services/XXX/YYY/ZZZ'
  pagerduty_url: 'https://events.pagerduty.com/v2/enqueue'

route:
  group_by: ['alertname', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: default
  routes:
    - match:
        severity: critical
      receiver: critical-alerts
      group_wait: 10s
      repeat_interval: 1h
    - match:
        team: platform
      receiver: platform-team
      continue: true
    - match:
        service: payments
      receiver: payments-oncall
      routes:
        - match:
            severity: critical
          receiver: payments-pagerduty

receivers:
  - name: 'default'
    email_configs:
      - to: 'alerts@example.com'
        headers:
          subject: '{% raw %}{{ .GroupLabels.alertname }}{% endraw %} - {% raw %}{{ .Status }}{% endraw %}'

  - name: 'critical-alerts'
    slack_configs:
      - channel: '#critical-alerts'
        send_resolved: true
        color: '{% raw %}{{ if eq .Status "firing" }}danger{{ else }}good{{ end }}{% endraw %}'
        title: '{% raw %}{{ .GroupLabels.alertname }}{% endraw %}'
        text: '{% raw %}{{ range .Alerts }}{% endraw %}{{ .Annotations.summary }}\n{{ .Annotations.description }}{% raw %}{{ end }}{% endraw %}'

  - name: 'platform-team'
    slack_configs:
      - channel: '#platform-alerts'
        send_resolved: true
    email_configs:
      - to: 'platform@example.com'

  - name: 'payments-oncall'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_SERVICE_KEY}'
        severity: '{% raw %}{{ if eq .Labels.severity "critical" }}critical{{ else }}warning{{ end }}{% endraw %}'
        component: Prometheus
        group: '{% raw %}{{ .GroupLabels.alertname }}{% endraw %}'
        class: 'Monitoring'
        send_resolved: true

inhibit_rules:
  - source_match:
      severity: critical
    target_match_re:
      severity: warning|info
    equal: ['alertname', 'instance']
```
