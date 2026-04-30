# Scenario Examples

## 9.1 Multi-Environment Dashboard

**User:** "How do I create a dashboard that works across dev, staging, and production environments?"

**Expert:**
> **Solution with Variables:**
>
> 1. Create a datasource variable filtered by environment prefix
> 2. Create environment constant variable
> 3. Use mixed datasource for cross-environment comparisons
>
> ```json
> {
>   "templating": {
>     "list": [
>       {
>         "name": "env",
>         "type": "custom",
>         "query": "dev,staging,production",
>         "multi": false,
>         "current": { "value": "production", "text": "Production" }
>       },
>       {
>         "name": "ds",
>         "type": "datasource",
>         "query": "prometheus",
>         "filtered": false
>       }
>     ]
>   },
>   "panels": [
>     {
>       "title": "Request Rate - $env",
>       "targets": [
>         {
>           "expr": "sum(rate(http_requests_total{env=\"$env\"}[5m]))",
>           "datasource": "Prometheus"
>         }
>       ]
>     }
>   ]
> }
> ```

## 9.2 Correlating Logs and Metrics

**User:** "I need to see the exact logs when a metric threshold is breached. How do I correlate?"

**Expert:**
> **Solution with Loki and Derived Fields:**
>
> 1. Configure Loki datasource with derived fields
> 2. Add regex pattern to extract TraceID
> 3. Link to Tempo for distributed tracing
>
> ```yaml
> # datasource.yml
> datasources:
>   - name: Loki
>     type: loki
>     jsonData:
>       maxLines: 5000
>       derivedFields:
>         - name: trace_id
>           matcherRegex: "trace_id=(\\w+)"
>           url: "http://tempo:3200/api/traces/$${1}"
>           datasourceUid: tempo
>         - name: pod_name
>           matcherRegex: "pod=([^\\s]+)"
>           url: "$${__value.text}"
> ```
>
> **In Explore:**
> 1. Run metric alert query to find time of breach
> 2. Click "Logs" to switch to Loki with pre-filled time range
> 3. Filter by `trace_id` from the metric label
> 4. Use "Trace" button to jump to Tempo

## 9.3 Service Level Objectives (SLO) Dashboard

**User:** "How do I build an SLO dashboard showing error budget burn rate?"

**Expert:**
> **Solution with SLO Panel:**
>
> ```json
> {
>   "panels": [
>     {
>       "title": "Request Success Rate (SLO: 99.9%)",
>       "type": "stat",
>       "datasource": "Prometheus",
>       "targets": [
>         {
>           "expr": "1 - (sum(rate(http_requests_total{status=~\"5..\"}[1h])) / sum(rate(http_requests_total[1h])))",
>           "refId": "A",
>           "format": "percentunit",
>           "thresholds": {
>             "mode": "absolute",
>             "steps": [
>               { "color": "red", "value": null },
>               { "color": "yellow", "value": 0.999 },
>               { "color": "green", "value": 0.9999 }
>             ]
>           }
>         }
>       ]
>     },
>     {
>       "title": "Error Budget Burn Rate (24h window)",
>       "type": "timeseries",
>       "datasource": "Prometheus",
>       "targets": [
>         {
>           "expr": "slo_burn_rate:http_requests:error_rate30d{job=\"$job\"}",
>           "legendFormat": "{{job}}"
>         }
>       ],
>       "fieldConfig": {
>         "defaults": {
>           "thresholds": {
>             "mode": "absolute",
>             "steps": [
>               { "color": "green", "value": null },
>               { "color": "yellow", "value": 1 },
>               { "color": "red", "value": 2 }
>             ]
>           }
>         }
>       }
>     }
>   ]
> }
> ```
>
> **SLO burn rate formula:** `burn_rate = (error_rate_actual / error_rate_allowed) * time_factor`

## 9.4 Templating with Dependent Variables

**User:** "How do I create cascading dropdowns where service choices depend on the selected environment?"

**Expert:**
> **Solution:**
>
> 1. Create `env` variable (datasource or custom)
> 2. Create `region` variable that depends on `env`
> 3. Create `service` variable that depends on both `env` and `region`
>
> ```json
> {
>   "templating": {
>     "list": [
>       {
>         "name": "env",
>         "type": "query",
>         "query": "label_values(up, env)",
>         "refresh": 1
>       },
>       {
>         "name": "region",
>         "type": "query",
>         "query": "label_values(up{env=\"$env\"}, region)",
>         "dependsOn": ["env"],
>         "refresh": 1
>       },
>       {
>         "name": "service",
>         "type": "query",
>         "query": "label_values(up{env=\"$env\", region=\"$region\"}, service)",
>         "dependsOn": ["env", "region"],
>         "refresh": 1,
>         "includeAll": true,
>         "multi": true
>       }
>     ]
>   }
> }
> ```

## 9.5 Incident Response: Alert to On-Call

**User:** "A critical alert fired. How do I use Grafana to investigate and respond?"

**Expert:**
> **Investigation Flow:**
>
> 1. **Alert notification** arrives via PagerDuty/Slack
> 2. **Click alert link** to open Grafana alert detail view
> 3. **Check alert state** - firing, pending, or recovered
> 4. **View query results** at time of firing
> 5. **Jump to Explore** with same time range and filters
> 6. **Query related metrics** (dependency check)
> 7. **Check logs** in Loki with same labels
> 8. **Trace request** using TraceID from logs
> 9. **Create incident** in Grafana OnCall
> 10. **Add timeline annotation** to dashboard for post-mortem
>
> **Annotation via API:**
> ```bash
> curl -X POST -H "Authorization: Bearer $API_KEY" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "dashboardUid": "abc123",
>     "panelId": 1,
>     "time": 1700000000,
>     "text": "Incident INC-1234 started - investigating high latency",
>     "tags": ["incident", "investigating"]
>   }' \
>   http://localhost:3000/api/annotations
> ```

## 9.6 Provisioning Dashboards from Git

**User:** "How do I version-control dashboards and deploy them automatically?"

**Expert:**
> **GitOps with ArgoCD:**
>
> 1. Store dashboard JSON in Git repository
> 2. Use `jq` to split dashboard JSON into individual files
> 3. Configure ArgoCD to sync `/grafana/dashboards` directory
>
> ```bash
> # Extract dashboards from JSON export
> cat dashboards-export.json | jq -r '.[] | @json' > dashboard-1.json

> # Generate dashboard.yml
> cat > dashboards.yml <<EOF
> apiVersion: 1
> providers:
>   - name: 'GitOps Dashboards'
>     orgId: 1
>     folder: 'GitOps'
>     type: file
>     disableDeletion: true
>     updateIntervalSeconds: 0
>     options:
>       path: /var/lib/grafana/dashboards
> EOF
> ```
>
> ```yaml
> # argocd-app.yaml
> spec:
>   syncPolicy:
>     automated:
>       prune: true
>       selfHeal: false
>     syncOptions:
>       - Replace=true
> ```
