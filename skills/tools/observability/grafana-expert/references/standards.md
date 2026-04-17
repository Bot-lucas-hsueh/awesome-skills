# Standards & Reference

## 7.1 Official Documentation

- [Grafana Documentation](https://grafana.com/docs/grafana/latest/)
- [Grafana Loki Documentation](https://grafana.com/docs/loki/latest/)
- [Grafana Tempo Documentation](https://grafana.com/docs/tempo/latest/)
- [Grafana Mimir Documentation](https://grafana.com/docs/mimir/latest/)
- [Grafana OnCall Documentation](https://grafana.com/docs/oncall/latest/)
- [Grafana Cloud Docs](https://grafana.com/docs/grafana-cloud/)
- [Grafana Alerting Docs](https://grafana.com/docs/grafana/latest/alerting/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/http_api/dashboard/)
- [Grafana Provisioning](https://grafana.com/docs/grafana/latest/administration/provisioning/)

## 7.2 Configuration Reference

### Grafana Server (grafana.ini)

```ini
[server]
protocol = http
http_addr = 0.0.0.0
http_port = 3000
domain = grafana.example.com
root_url = %(protocol)s://%(domain)s/grafana
enable_gzip = true

[database]
type = postgres
host = db:5432
name = grafana
user = grafana
password = ${GF_DATABASE_PASSWORD}
ssl_mode = require

[security]
admin_user = admin
admin_password = ${GF_ADMIN_PASSWORD}
secret_key = ${GF_SECRET_KEY}
disable_gravatar = true
cookie_secure = true
cookie_samesite = strict

[auth]
disable_login_form = false
disable_signout_menu = false
auth.anonymous.enabled = false

[users]
allow_sign_up = false
allow_org_create = false
auto_assign_org = true
auto_assign_org_role = Viewer

[alerting]
enabled = true
execute_alerts = true
evaluation_timeout = 30s
notification_timeout = 30s
max_annotations_keep = 0

[unified_alerting]
enabled = true
min_interval = 10s

[paths]
provisioning = /etc/grafana/provisioning
```

### Provisioning (datasources.yml)

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    uid: prometheus-main
    access: proxy
    url: http://prometheus:9090
    isDefault: true
    jsonData:
      timeInterval: 15s
      httpMethod: POST
    editable: false

  - name: Loki
    type: loki
    uid: loki-main
    access: proxy
    url: http://loki:3100
    jsonData:
      maxLines: 5000
      derivedFields:
        - name: TraceID
          matcherRegex: "trace_id=(\\w+)"
          url: "http://tempo:3200/api/traces/$${1}"
          datasourceUid: tempo-main

  - name: Tempo
    type: tempo
    uid: tempo-main
    access: proxy
    url: http://tempo:3200
    jsonData:
      serviceMap:
        datasourceUid: prometheus-main
      lokiSearch:
        datasourceUid: loki-main

  - name: MySQL
    type: mysql
    uid: mysql-app
    access: proxy
    url: mysql:3306
    database: app_metrics
    user: grafana_ro
    secureJsonData:
      password: ${MYSQL_PASSWORD}
```

### Provisioning (dashboards.yml)

```yaml
apiVersion: 1

providers:
  - name: 'Default'
    orgId: 1
    folder: ''
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    allowUiUpdates: true
    options:
      path: /var/lib/grafana/dashboards

  - name: 'Team Dashboards'
    orgId: 1
    folder: 'Platform Team'
    type: file
    disableDeletion: false
    updateIntervalSeconds: 30
    options:
      path: /var/lib/grafana/dashboards/team
```

### Alerting Rules (alert-rules.yml)

```yaml
apiVersion: 1

groups:
  - orgId: 1
    name: platform_alerts
    folder: Platform
    interval: 1m
    rules:
      - uid: high_cpu_alert
        title: High CPU Usage
        condition: C
        data:
          - refId: A
            relativeTimeRange:
              from: 300
              to: 0
            datasourceUid: prometheus-main
            model:
              expr: avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100 < 20
              refId: A
          - refId: B
            relativeTimeRange:
              from: 300
              to: 0
            datasourceUid: __expr__
            model:
              conditions:
                - evaluator:
                    params: []
                    type: gt
                  operator:
                    type: and
                  query:
                    params:
                      - B
                  reducer:
                    params: []
                    type: avg
                  type: query
              refId: B
              type: reduce
              reducer: last
          - refId: C
            relativeTimeRange:
              from: 300
              to: 0
            datasourceUid: __expr__
            model:
              conditions:
                - evaluator:
                    params:
                      - 0
                    type: gt
              expression: B
              refId: C
              type: threshold
        noDataState: NoData
        execErrState: Error
        for: 5m
        annotations:
          summary: 'High CPU usage detected on {{ $labels.instance }}'
          description: 'CPU idle time has been below 20% for more than 5 minutes'
        labels:
          severity: warning
          team: platform
        isPaused: false
```

## 7.3 Common Commands

### Grafana CLI

| Command | Description |
|---------|-------------|
| `grafana-cli admin reset-admin-password <new_password>` | Reset admin password |
| `grafana-cli plugins install <plugin_id>` | Install plugin |
| `grafana-cli plugins list-remote` | List available plugins |
| `grafana-cli plugins update <plugin_id>` | Update plugin |
| `grafana-cli admin manage-ldap-sync` | Sync LDAP users |

### HTTP API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/dashboards/uid/:uid` | GET | Get dashboard by UID |
| `/api/dashboards/db` | POST | Create/update dashboard |
| `/api/datasources` | GET | List datasources |
| `/api/ds/query` | POST | Query datasources |
| `/api/annotations` | GET/POST | Manage annotations |
| `/api/folders` | GET/POST | Manage folders |
| `/api/org` | GET | Get current org |
| `/api/auth/keys` | GET/POST | Manage API keys |
| `/api/v1/provisioning/alert-rules` | GET/POST | Manage alerting rules |

### Provisioning with curl

```bash
# Create datasource via API
curl -X POST -H "Authorization: Bearer $GRAFANA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test DS","type":"prometheus","url":"http://prom:9090"}' \
  http://localhost:3000/api/datasources

# Import dashboard
curl -X POST -H "Authorization: Bearer $GRAFANA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @dashboard.json \
  http://localhost:3000/api/dashboards/db

# Force datasource health check
curl -X POST -H "Authorization: Bearer $GRAFANA_TOKEN" \
  http://localhost:3000/api/datasources/1/health
```

## 7.4 Version Compatibility

| Grafana Version | Status | Notes |
|-----------------|--------|-------|
| 11.x | Current | New navigation, alerting changes |
| 10.x | Supported | Scene graphs, RBAC improvements |
| 9.x | Supported | Alerting onGVL, unified storage |
| 8.x | Security only | Deprecated, upgrade recommended |

### Plugin Compatibility

- Plugins must be rebuilt for each major Grafana version
- Check plugin compatibility at grafana.com/plugins
- Use `grafana-cli plugins list-versions <plugin>` for version history

## 7.5 Variables and Templating

### Dashboard Variables

```json
{
  "templating": {
    "list": [
      {
        "name": "datasource",
        "type": "datasource",
        "query": "prometheus",
        "current": { "value": "prometheus-main", "text": "Prometheus" }
      },
      {
        "name": "job",
        "type": "query",
        "datasource": "prometheus-main",
        "query": "label_values(node_cpu_seconds_total, job)",
        "refresh": 2,
        "includeAll": true,
        "multi": true
      },
      {
        "name": "instance",
        "type": "query",
        "datasource": "prometheus-main",
        "query": "label_values(node_cpu_seconds_total{job=\"$job\"}, instance)",
        "dependsOn": ["job"]
      },
      {
        "name": "environment",
        "type": "constant",
        "query": "production",
        "hide": "label"
      },
      {
        "name": "timeRange",
        "type": "interval",
        "query": "1m,5m,15m,30m,1h,6h,1d",
        "current": { "value": "$__auto_interval_interval" }
      }
    ]
  }
}
```

### Nested Variables

```json
{
  "name": "service",
  "type": "query",
  "query": "label_values(sum by (service) (rate(http_requests_total[$__range])), service)",
  "dependsOn": ["datasource"]
}
```

## 7.6 RBAC Permissions

```yaml
# provisioning/access-control.yml
apiVersion: 1

roles:
  - name: 'managed:editor:read:all'
    uid: 'managed_editor_read_all'
    description: 'Read all dashboards and folders'
    version: 1
    permissions:
      - action: 'dashboards:read'
        scope: 'dashboards:*'
      - action: 'folders:read'
        scope: 'folders:*'
      - action: 'datasources:read'
        scope: 'datasources:*'

role_assignments:
  managed:editor:read:all:
    - uid: 'team-platform'
```
