# Standard Workflow

## 8.1 Getting Started

```
Phase 1: Installation
├── Binary installation or Docker
├── Configure database (PostgreSQL/MySQL/SQLite)
├── Set up reverse proxy (nginx/Caddy)
├── Configure security (TLS, auth)
└── Verify with grafana-cli

Phase 2: Data Source Setup
├── Add Prometheus as default datasource
├── Add Loki for logs, Tempo for traces
├── Configure Explore data sources
├── Set up alerting datasources
└── Test connectivity with query builder

Phase 3: First Dashboard
├── Create folder for team
├── Build CPU/Memory/Disk panels
├── Add row for custom application metrics
├── Configure templating variables
└── Share dashboard and set up notifications

Phase 4: Alerting
├── Define alert rules with conditions
├── Set up contact points (email/Slack/PagerDuty)
├── Configure notification policies
├── Test alert firing and recovery
└── Document on-call runbooks
```

## 8.2 Common Workflows

### Dashboard Creation Workflow

1. **Plan the dashboard layout** (metrics, logs, traces sections)
2. **Define variables** for reusability (datasources, environments, services)
3. **Add panels incrementally** starting with key metrics
4. **Use mixed datasources** for correlated views
5. **Add annotations** from alerting rules or manual
6. **Configure row collapsing** for organized sections
7. **Set up links** between dashboards (drill-down)
8. **Add to folder** with proper permissions

### Alerting Workflow

1. **Define SLIs/SLOs** before creating alerts
2. **Create alert rules** with clear naming convention
3. **Configure evaluation interval** (default 1m, reduce for critical)
4. **Set `for` duration** to prevent alert storms
5. **Add annotations** with runbook links and context
6. **Configure labels** for routing (severity, team, service)
7. **Set up contact points** with proper notification timing
8. **Test with `NoData` and `Error` states**

### Provisioning Workflow

1. **Structure config** with datasources, dashboards, alerting directories
2. **Use `options.path`** for file-based provisioning
3. **Enable `allowUiUpdates`** for dashboard-only changes
4. **Version control** all YAML/JSON provisioning files
5. **Use environment variables** for secrets
6. **Test with `--validate-items`** or dry-run
7. **Automate with CI/CD** (GitOps approach)

### Explore Workflow

1. **Select datasource** (Prometheus, Loki, Tempo, etc.)
2. **Build query** with query editor
3. **Add filters** with label matchers
4. **Switch between metrics/logs/traces**
5. **Correlate using TraceID** from logs to Tempo
6. **Share query** via deep links or copy link

## 8.3 Docker Compose Setup

```yaml
version: '3.8'

services:
  grafana:
    image: grafana/grafana:11.0.0
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    volumes:
      - ./grafana/data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
      - ./grafana/dashboards:/var/lib/grafana/dashboards
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD}
      - GF_DATABASE_TYPE=postgres
      - GF_DATABASE_HOST=postgres:5432
      - GF_DATABASE_NAME=grafana
      - GF_DATABASE_USER=grafana
      - GF_DATABASE_PASSWORD=${GRAFANA_DB_PASSWORD}
      - GF_FEATURE_TOGGLES_ENABLE=publicDashboards
    depends_on:
      - postgres
    networks:
      - monitoring

  prometheus:
    image: prom/prometheus:v2.49.1
    container_name: prometheus
    restart: unless-stopped
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - ./prometheus/rules:/etc/prometheus/rules
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.enable-lifecycle'
    networks:
      - monitoring

  loki:
    image: grafana/loki:3.0.0
    container_name: loki
    restart: unless-stopped
    ports:
      - "3100:3100"
    volumes:
      - ./loki/loki-config.yml:/etc/loki/local-config.yaml
      - loki-data:/loki
    networks:
      - monitoring

  tempo:
    image: grafana/tempo:2.4.1
    container_name: tempo
    restart: unless-stopped
    ports:
      - "3200:3200"
      - "4317:4317"  # OTLP gRPC
      - "4318:4318"  # OTLP HTTP
    volumes:
      - ./tempo/tempo-config.yml:/etc/tempo.yaml
      - tempo-data:/var/tempo
    networks:
      - monitoring

volumes:
  prometheus-data:
  loki-data:
  tempo-data:

networks:
  monitoring:
    driver: bridge
```

## 8.4 GitOps Workflow with Argo CD

```yaml
# argocd-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: grafana-provisioning
  namespace: argocd
spec:
  project: monitoring
  source:
    repoURL: https://github.com/org/grafana-config.git
    targetRevision: main
    path: grafana/provisioning
  destination:
    server: https://kubernetes.default.svc
    namespace: monitoring
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

## 8.5 Testing Workflow

```bash
# Validate provisioning files
grafana-server --verify-config grafana.ini

# Test datasource connectivity
curl -H "Authorization: Bearer $API_KEY" \
  http://localhost:3000/api/datasources/1/health

# Check alerting
curl -H "Authorization: Bearer $API_KEY" \
  http://localhost:3000/api/v1/provisioning/alert-rules

# Run e2e tests
make test-e2e

# Check explore queries
curl -X POST -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"queries":[{"datasourceId":1,"expr":"up","refId":"A"}]}' \
  http://localhost:3000/api/ds/query
```

## 8.6 Migration Workflow (v10 to v11)

1. **Backup all dashboards** using API
2. **Update plugins** to compatible versions
3. **Test in staging** with production-like data
4. **Check breaking changes** in release notes
5. **Update alerting rules** syntax if needed
6. **Migrate to new navigation** and panels
7. **Update alerting** from Grafana 8 alerting to Grafana 11 unified alerting
