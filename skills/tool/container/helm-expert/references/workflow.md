# Standard Workflow

## 8.1 Helm Chart Development Workflow

```
Phase 1: Chart Creation
├── helm create mychart (scaffold)
├── Edit Chart.yaml with metadata
├── Configure values.yaml with defaults
├── Create templates with helpers
└── Add tests in templates/tests/

Phase 2: Template Development
├── Define _helpers.tpl for labels/selectors
├── Create deployment.yaml with security
├── Add service.yaml, ingress.yaml
├── Configure probes and resources
└── Add ConfigMaps/Secrets templates

Phase 3: Testing
├── helm lint ./mychart
├── helm template ./mychart --debug
├── helm install --dry-run --debug
├── kind create cluster for e2e
└── helm test myrelease

Phase 4: Publishing
├── helm package ./mychart
├── helm push to OCI registry (v3)
├── Push to Artifact Hub
└── Document in README.md
```

## 8.2 Release Management Workflow

### Development Release
```bash
# Create development release
helm upgrade --install myapp ./mychart \
  --namespace dev \
  --create-namespace \
  --set image.tag=dev-$(git rev-parse --short HEAD) \
  --wait --timeout 5m
```

### Staging Release
```bash
# Blue-green style deployment to staging
helm upgrade --install myapp-staging ./mychart \
  --namespace staging \
  --values ./values-staging.yaml \
  --set replicaCount=2 \
  --wait
```

### Production Release
```bash
# Production with atomic rollback
helm upgrade --install myapp ./mychart \
  --namespace production \
  --values ./values-prod.yaml \
  --atomic \
  --cleanup-on-fail \
  --wait \
  --timeout 10m

# Monitor rollout
kubectl rollout status deployment/myapp -n production
```

## 8.3 Helm Testing Workflow

### Lint Check
```bash
# Basic lint
helm lint ./mychart

# Strict mode
helm lint ./mychart --strict

# Check template rendering
helm template myapp ./mychart --debug
```

### Dry-Run Installation
```bash
# Test without cluster
helm template myapp ./mychart

# Test with cluster
helm upgrade --install myapp ./mychart \
  --dry-run \
  --debug \
  --namespace test

# Diff before upgrade
helm diff upgrade myapp ./mychart -n production
```

### Automated Testing
```bash
# Run test hooks
helm test myapp --logs

# Test with Kind
kind create cluster
helm upgrade --install myapp ./mychart --wait
helm test myapp
kind delete cluster
```

## 8.4 Dependency Management Workflow

### Chart Dependencies
```yaml
# Chart.yaml
dependencies:
  - name: postgresql
    version: "12.x.x"
    repository: "https://charts.bitnami.com"
  - name: redis
    version: "17.x.x"
    repository: "https://charts.bitnami.com"
```

### Dependency Operations
```bash
# Update dependencies
helm dependency update ./mychart

# List dependencies
helm dependency list ./mychart

# Build lock file
helm dependency build ./mychart

# Repair corrupted lock
helm dependency update --verify ./mychart
```

### OCI Registry Dependencies
```bash
# Login to registry
helm registry login ghcr.io

# Pull dependency
helm pull oci://ghcr.io/org/chart --version 1.0.0

# Push chart
helm chart save ./mychart ghcr.io/org/mychart:1.0.0
helm chart push ghcr.io/org/mychart:1.0.0
```

## 8.5 Rollback Workflow

### List Release History
```bash
helm history myapp -n production

# Output:
# REVISION    STATUS         DESCRIPTION
# 1           superseded     Install complete
# 2           superseded     Upgrade complete
# 3           deployed       Upgrade complete
```

### Rollback to Previous
```bash
# Rollback one revision
helm rollback myapp -n production

# Rollback to specific revision
helm rollback myapp 1 -n production

# Rollback with wait
helm rollback myapp 1 -n production --wait --timeout 5m
```

### Emergency Rollback
```bash
# Quick rollback if deployment fails
helm rollback myapp 0 -n production --wait

# Force rollback ignoring failures
helm rollback myapp --force -n production
```

## 8.6 Repository Management

### Add Repositories
```bash
# Add common repositories
helm repo add bitnami https://charts.bitnami.com
helm repo add prometheus https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo add elastic https://helm.elastic.co

# Update all repos
helm repo update

# List repositories
helm repo list
```

### Search Charts
```bash
# Search Artifact Hub
helm search hub nginx

# Search local repos
helm search repo nginx

# Search with version
helm search repo nginx --versions | head -5
```

### Manage Local Cache
```bash
# Update specific repo
helm repo update bitnami

# Remove repo
helm repo remove bitnami

# Clean up old charts
helm repo prune
```

## 8.7 CI/CD Integration

### GitHub Actions
```yaml
# .github/workflows/helm.yml
- name: Lint and Test Chart
  run: |
    helm lint ./chart
    helm template myapp ./chart

- name: Package and Push
  if: github.ref == 'refs/heads/main'
  run: |
    helm package ./chart
    helm push mychart-*.tgz oci://${{ env.REGISTRY }}/charts
```

### ArgoCD Integration
```yaml
# application.yaml for Helm
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
spec:
  chart:
    chart: myapp
    repoURL: oci://ghcr.io/org/charts
    targetRevision: 1.0.0
  destination:
    server: https://kubernetes.default.svc
    namespace: production
```

## 8.8 Plugin Workflow

### Essential Plugins
```bash
# Install plugins
helm plugin install https://github.com/databus23/helm-diff
helm plugin install https://github.com/hypnoglow/helm-s3
helm plugin install https://github.com/aslafy-z/helm-git

# Use diff plugin
helm diff upgrade myapp ./chart -n production

# Use S3 plugin
helm repo add s3 s3://my-bucket/charts
```
