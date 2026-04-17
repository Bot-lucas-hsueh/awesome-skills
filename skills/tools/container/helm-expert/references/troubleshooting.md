# Troubleshooting

## 8.1 Chart Development Issues

### Template Rendering Errors

**Error:** `Error: template: chart/templates/deployment.yaml:1:3: executing "deployment.yaml" at <...>: invalid function`

**Diagnosis:**
```bash
# Dry-run to see rendered template
helm template ./mychart --debug

# Check syntax
helm lint ./mychart
```

**Common Solutions:**

| Error | Cause | Fix |
|-------|-------|-----|
| `unexpected .` | Wrong variable reference | Use `.Values.key.path` |
| `not defined` | Missing template | Add to `_helpers.tpl` |
| `cannot evaluate` | Type mismatch | Use `| toString` or `| quote` |

### Dependency Issues

**Error:** `Error: chart not found in expected location`

**Diagnosis:**
```bash
# Check if dependencies are present
ls mychart/charts/

# Update dependencies
helm dependency update ./mychart
```

**Solutions:**
```bash
# Update all dependencies
helm dependency update ./mychart

# Build dependencies
helm dependency build ./mychart

# Check requirements.lock
cat mychart/requirements.lock
```

## 8.2 Installation Issues

### Release Already Exists

**Error:** `Error: release myrelease already exists`

**Solutions:**
```bash
# Upgrade instead of install
helm upgrade myrelease ./mychart --install

# Or uninstall first
helm uninstall myrelease
helm install myrelease ./mychart
```

### Values Not Applied

**Error:** Custom values are not being used

**Diagnosis:**
```bash
# Check current values
helm get values myrelease

# Template with values
helm template ./mychart -f myvalues.yaml
```

**Solutions:**
```bash
# Install with values file
helm install myrelease ./mychart -f myvalues.yaml

# Install with set
helm install myrelease ./mychart --set replicaCount=5

# Override with precedence
helm install myrelease ./mychart -f values.yaml --set replicaCount=3
```

### Hooks Not Working

**Symptoms:** Pre-install/upgrade hooks not executing

**Diagnosis:**
```yaml
# Check hook definition
apiVersion: v1
kind: ConfigMap
metadata:
  annotations:
    "helm.sh/hook": pre-install
```

**Solutions:**
```yaml
# Ensure correct hook annotations
metadata:
  annotations:
    "helm.sh/hook": pre-install,pre-upgrade
    "helm.sh/hook-delete-policy": hook-succeeded,before-hook-creation
```

## 8.3 Runtime Issues

### Pod Not Starting After Helm Install

**Diagnosis:**
```bash
# Check release status
helm status myrelease

# Get manifest
helm get manifest myrelease

# Check pods
kubectl get pods -n <namespace>

# Get events
kubectl get events -n <namespace> --sort-by='.lastTimestamp'
```

**Common Causes:**

| Issue | Command | Solution |
|-------|---------|----------|
| Image pull error | `kubectl describe pod` | Check image tag/registry |
| Config error | `kubectl logs` | Check ConfigMap references |
| RBAC issue | `kubectl auth can-i` | Add RBAC rules |

### Upgrade Fails

**Error:** `Error: failed to upgrade release`

**Diagnosis:**
```bash
# Get last release info
helm get manifest myrelease

# Check history
helm history myrelease

# Template new version
helm template ./mychart -f values.yaml
```

**Solutions:**
```bash
# Dry-run first
helm upgrade myrelease ./mychart --dry-run

# Force upgrade (use carefully)
helm upgrade myrelease ./mychart --force

# Rollback first
helm rollback myrelease
helm upgrade myrelease ./mychart
```

## 8.4 Values Schema Issues

### Schema Validation Error

**Error:** `Error: values don't meet the schema`

**Diagnosis:**
```bash
# Check schema validation
helm template ./mychart -f values.yaml --validate

# Check schema
cat values.schema.json
```

**Solutions:**
```json
// Add to values.schema.json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "replicaCount": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10
    }
  }
}
```

## 8.5 Secrets and Sensitive Data

### Secrets in Values

**Problem:** Sensitive data in values.yaml

**Solutions:**
```bash
# Use --set-file for large values
helm install myrelease ./mychart --set-file certs.tls.crt=./cert.pem

# Use external secrets operator
# Reference: https://external-secrets.io/

# Use sealed secrets
# Reference: https://github.com/bitnami-labs/sealed-secrets
```

## 8.6 Testing Issues

### Test Failures

**Error:** `Test failed: pod connection failed`

**Diagnosis:**
```bash
# Run tests
helm test myrelease

# Check test pod logs
kubectl logs -n <namespace> myrelease-test-connection
```

**Solutions:**
```yaml
# Ensure test is correct
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "mychart.fullname" . }}-test-connection"
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['{{ include "mychart.fullname" . }}:{{ .Values.service.port }}']
  restartPolicy: Never
```

## 8.7 Performance Issues

### Slow Template Rendering

**Diagnosis:**
```bash
# Profile template
time helm template ./mychart
```

**Solutions:**
```yaml
# Simplify templates
# Use named templates instead of inline
# Cache values in ConfigMap
# Use --show-only for specific templates
```

### Large Charts

**Diagnosis:**
```bash
# Check chart size
helm package ./mychart --sign

# List dependencies
helm dependency list ./mychart
```

**Solutions:**
```bash
# Remove unnecessary dependencies
# Use subcharts instead of inlining
# Enable repository caching
```