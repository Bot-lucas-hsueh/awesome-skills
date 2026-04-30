# Grafana Expert — Example Interactions

This file contains detailed example interactions referenced from SKILL.md §10.

---

## Example 1: Build Multi-Environment SLO Dashboard

**User:** "Create a dashboard template that shows SLO metrics for our services across all environments"

**Grafana Expert:**
> **Dashboard Design:**
>
> **1. Template Variables:**
> ```json
> // Variable: environment
> {
>   "name": "environment",
>   "type": "query",
>   "query": "label_values(up, environment)",
>   "multi": false,
>   "includeAll": false,
>   "allValue": ".*"
> }
>
> // Variable: service
> {
>   "name": "service",
>   "type": "query",
>   "query": "label_values(up{environment=\"$environment\"}, job)",
>   "multi": true,
>   "includeAll": true,
>   "allValue": ".*"
> }
>
> // Variable: slo_window (for error budget calculation)
> {
>   "name": "slo_window",
>   "type": "custom",
>   "options": ["1h", "6h", "24h", "7d"],
>   "current": {"value": "24h", "text": "24h"}
> }
> ```
>
> **2. SLO Overview Panel (Stat):**
> ```promql
> // Error rate
> 100 * (
>   sum(rate(http_requests_total{service=~"$service", status=~"5..", environment="$environment"}[$__rate_interval]))
>   /
>   sum(rate(http_requests_total{service=~"$service", environment="$environment"}[$__rate_interval]))
> )
>
> // Display: percentage with color thresholds
> // Thresholds: < 0.1% = green, 0.1-1% = yellow, > 1% = red
> ```
>
> **3. Error Budget Panel (Gauge):**
> ```promql
> // Calculate remaining error budget
> // SLO target: 99.9% (0.1% error budget)
> 100 * (
>   (1 - 0.001) - (
>     sum(rate(http_requests_total{service=~"$service", status=~"5..", environment="$environment"}[${slo_window}]))
>     /
>     sum(rate(http_requests_total{service=~"$service", environment="$environment"}[${slo_window}]))
>   )
> ) / 0.1
>
> // Display: gauge 0-100% remaining budget
> // Thresholds: < 10% = red, < 50% = yellow, > 50% = green
> ```
>
> **4. Availability Trend (Time Series):**
> ```promql
> // 7-day rolling availability
> 100 * (
>   1 - (
>     sum(rate(http_requests_total{service=~"$service", status=~"5..", environment="$environment"}[1h]))
>     /
>     sum(rate(http_requests_total{service=~"$service", environment="$environment"}[1h]))
>   )
> )
>
> // Compare to SLO target line
> 99.9
> ```
>
> **5. Multi-Environment Comparison (Table):**
> ```promql
> // Rows per environment
> by (environment) (
>   100 * (
>     1 - (
>       sum(rate(http_requests_total{service=~"$service", status=~"5..", environment=~".*"}[1h]))
>       /
>       sum(rate(http_requests_total{service=~"$service", environment=~".*"}[1h]))
>     )
>   )
> )
> ```

---

## Example 2: Set Up Grafana Alerting with PagerDuty Integration

**User:** "Configure a Grafana alert for checkout service error rate that pages PagerDuty on-call"

**Grafana Expert:**
> **Step-by-Step Configuration:**
>
> **1. Create Contact Point (PagerDuty):**
> ```
> Alerting → Contact Points → New Contact Point
>
> Name: pagerduty-checkout
> Integration Type: PagerDuty
> Integration Key: (from PagerDuty Service → Integrations)
> Severity: critical
>
> Test: Send test notification
> ```
>
> **2. Create Notification Policy:**
> ```
> Alerting → Notification Policies → New Policy
>
> Matching Labels: service=checkout, severity=critical
> Contact Point: pagerduty-checkout
> Group By: service, alertname
>
> Timing:
>   Group wait: 30s
>   Group interval: 5m
>   Repeat interval: 4h
> ```
>
> **3. Create Alert Rule:**
> ```
> Alerting → Alert Rules → New Alert Rule
>
> Name: Checkout Error Rate Critical
> Folder: checkout-alerts
>
> Define query:
>   Metrics: B
>   expr: 100 * (sum(rate(http_requests_total{service="checkout", status=~"5.."}[$__rate_interval])) / sum(rate(http_requests_total{service="checkout"}[$__rate_interval])))
>   Conditions:
>     WHEN: B > 5 FOR: 5m
>
> Annotations:
>   summary: "Checkout error rate is {{ $values.B }}%"
>   description: "Error rate has exceeded 5% for 5 minutes. Current: {{ $values.B }}%"
>   runbook_url: "https://wiki.example.com/runbooks/checkout-error"
>
> Labels:
>   severity: critical
>   service: checkout
>   team: platform
> ```
>
> **4. Grafonnet Definition:**
> ```jsonnet
> local prometheus = grafonnet.prometheus;
>
> prometheus.alertGroup.new(
>   name='checkout-alerts',
>   rules=[
>     prometheus.alert.new(
>       name='CheckoutErrorRateCritical',
>       message='Checkout error rate exceeds 5%',
>       conditions=[
>         prometheus.query.threshold(
>           expr='100 * (sum(rate(http_requests_total{service="checkout", status=~"5.."}[$__rate_interval])) / sum(rate(http_requests_total{service="checkout"}[$__rate_interval]))) > 5',
>           refID='A',
>           operator=prometheus.query.operators.greater_than,
>           for='5m',
>         ),
>       ],
>       labels={
>         severity: 'critical',
>         service: 'checkout',
>       },
>       annotations={
>         summary: 'Checkout error rate is {{ $values.A }}%',
>         runbook_url: 'https://wiki.example.com/runbooks/checkout-error',
>       },
>     ),
>   ],
> )
> ```

---

## Example 3: Provision Dashboards with GitOps

**User:** "Help me set up Grafana provisioning so dashboards are managed in Git"

**Grafana Expert:**
> **Directory Structure:**
> ```
> grafana-provisioning/
> ├── dashboards/
> │   ├── dashboards.yml          # Dashboard provider config
> │   ├── checkout/
> │   │   ├── overview.json
> │   │   ├── slo.json
> │   │   └── infrastructure.json
> │   └── platform/
> │       └── kubernetes.json
> ├── datasources/
> │   └── datasources.yml        # Datasource provisioning
> └── alerting/
>     ├── alert-rules.yml         # Alert rules
>     └── contact-points.yml     # Notification configs
> ```
>
> **1. Datasource Provisioning (`datasources/datasources.yml`):**
> ```yaml
> apiVersion: 1
>
> datasources:
>   - name: Prometheus
>     type: prometheus
>     uid: prometheus-main
>     access: proxy
>     url: http://prometheus:9090
>     isDefault: true
>     jsonData:
>       httpMethod: POST
>       manageAlerts: true
>       prometheusType: Prometheus
>       timeInterval: 15s
>
>   - name: Loki
>     type: loki
>     uid: loki-main
>     access: proxy
>     url: http://loki:3100
>     jsonData:
>       derivedFields:
>         - name: TraceID
>           matcherRegex: "trace_id=(\\w+)"
>           url: $${__value.raw}
>           datasourceUid: tempo-main
> ```
>
> **2. Dashboard Provisioning (`dashboards/dashboards.yml`):**
> ```yaml
> apiVersion: 1
>
> providers:
>   - name: 'Checkout Dashboards'
>     orgId: 1
>     folder: 'Checkout'
>     folderUid: 'checkout'
>     type: file
>     disableDeletion: false
>     updateIntervalSeconds: 30
>     allowUiUpdates: false  # All changes via Git
>     options:
>       path: /var/lib/grafana/dashboards/checkout
>
>   - name: 'Platform Dashboards'
>     orgId: 1
>     folder: 'Platform'
>     folderUid: 'platform'
>     type: file
>     disableDeletion: false
>     updateIntervalSeconds: 30
>     allowUiUpdates: false
>     options:
>       path: /var/lib/grafana/dashboards/platform
> ```
>
> **3. Kubernetes Deployment:**
> ```yaml
> # ConfigMap for datasources
> apiVersion: v1
> kind: ConfigMap
> metadata:
>   name: grafana-datasources
> data:
>   datasources.yml: |
>     apiVersion: 1
>     datasources:
>       - name: Prometheus
>         type: prometheus
>         url: http://prometheus:9090
> ---
> # ConfigMap for dashboards
> apiVersion: v1
> kind: ConfigMap
> metadata:
>   name: grafana-dashboards
> data:
>   dashboards.yml: |
>     apiVersion: 1
>     providers:
>       - name: default
>         orgId: 1
>         folder: ''
>         type: file
>         options:
>           path: /var/lib/grafboard/dashboards
> ---
> # Deployment volume mounts
> volumeMounts:
>   - name: grafana-datasources
>     mountPath: /etc/grafana/provisioning/datasources
>   - name: grafana-dashboards
>     mountPath: /var/lib/grafana/dashboards
> ```
>
> **4. GitOps Workflow:**
> ```bash
> # 1. Update dashboard in UI, export JSON
> # 2. Copy to git repo
> cp /tmp/checkout-overview.json dashboards/checkout/
>
> # 3. Commit and push
> git add dashboards/checkout/overview.json
> git commit -m "Update checkout SLO dashboard"
> git push
>
> # 4. CI/CD deploys to Kubernetes
> # ArgoCD/GitOps syncs ConfigMap updates
> # Grafana reloads dashboard from volume
> ```

---

## Edge Cases (from §11)

### Dynamic Dashboard for Many Services
```promql
sum by (service) (rate(http_requests_total{service=~"$service"}[$__rate_interval]))
```

### Alert When Metric Doesn't Exist (No Data)
```promql
absent(up{service="checkout", environment="production"})
```

### Correlated Metrics (Traces + Metrics)
```json
// Mixed panel with Prometheus + Tempo
"datasource": {
  "type": "datasource",
  "uid": "-- Mixed --"
},
"targets": [
  { "datasource": "Prometheus", "expr": "error_rate" },
  { "datasource": "Tempo", "expr": "traces{error=true}" }
]
```

### Dashboard with Multiple Row Groups
```json
{
  "type": "row",
  "title": "SLO Metrics",
  "collapsed": false,
  "repeat": "$service"
}
```

### Percentage Calculations Across Multiple Series
```promql
// Manual calculation
100 * (
  sum(rate(http_requests_total{status="500"}[$__rate_interval]))
  /
  sum(rate(http_requests_total[$__rate_interval]))
)
```

### Sensitive Data in Annotations
```yaml
annotations:
  summary: "High error rate on {{ $labels.service }}"
labels:
  service: checkout
  # sensitive_metric: "..."
```

### Dashboard Variables from Multiple Datasources
```jsonnet
// Grafonnet with combined variable
local var = grafonnet.variable;

var.query.new(
  name='service',
  datasource='Prometheus',
  query='label_values(up, job)',
)
```

### Long-Running Queries
```yaml
# Prometheus recording rule
groups:
  - name: checkout:recording_rules
    interval: 30s
    rules:
      - record: checkout:error_rate:5m
        expr: |
          100 * (
            sum(rate(http_requests_total{service="checkout", status=~"5.."}[5m]))
            /
            sum(rate(http_requests_total{service="checkout"}[5m]))
          )
```
