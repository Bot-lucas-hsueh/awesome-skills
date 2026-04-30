# Common Pitfalls & Anti-Patterns

## 10.1 Helm Anti-Patterns

| # | Anti-Pattern | Severity | Impact | Prevention |
|---|--------------|----------|--------|------------|
| 1 | **No values schema validation** | 🔴 High | Runtime validation failures | Add values.schema.json |
| 2 | **Using latest tag** | 🔴 High | Unpredictable deployments | Always pin versions |
| 3 | **No resource limits** | 🔴 High | Resource exhaustion | Set requests/limits |
| 4 | **Secrets in values** | 🔴 High | Secret exposure | Use external secrets |
| 5 | **No readiness probes** | 🟠 Medium | Traffic to unhealthy pods | Add readinessProbe |
| 6 | **Ignoring hook weights** | 🟡 Medium | Race conditions | Set proper hook weights |
| 7 | **Hardcoded values** | 🟡 Medium | Inflexibility | Use values.yaml |
| 8 | **No tests** | 🟡 Medium | Broken templates | Add test hooks |

## 10.2 Chart Development Anti-Patterns

### Anti-Pattern: No Schema Validation

**Bad Practice:**
```yaml
# values.yaml - No validation
replicaCount: "three"  # Should be integer!
imageTag: null  # Required but no validation
```

**Good Practice:**
```yaml
# values.schema.json
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "replicaCount": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10
    },
    "image": {
      "type": "object",
      "required": ["repository", "tag"],
      "properties": {
        "repository": {"type": "string"},
        "tag": {"type": "string", "minLength": 1}
      }
    }
  }
}
```

### Anti-Pattern: Secret in Values

**Bad Practice:**
```yaml
# values.yaml - EXPOSED!
database:
  password: "my-secret-password"
```

**Good Practice:**
```yaml
# values.yaml - Reference only
database:
  existingSecret: myapp-secrets
  passwordKey: db-password
```

```yaml
# external-secrets.yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: myapp-secrets
spec:
  secretStoreRef:
    name: vault-backend
  target:
    name: myapp-secrets
  data:
    - secretKey: db-password
      remoteRef:
        key: production/myapp/db
```

### Anti-Pattern: No Health Checks

**Bad Practice:**
```yaml
# Deployment without probes
containers:
  - name: app
    image: myapp:latest
    ports:
      - containerPort: 8080
    # No livenessProbe or readinessProbe!
```

**Good Practice:**
```yaml
containers:
  - name: app
    image: myapp:latest
    ports:
      - containerPort: 8080
    livenessProbe:
      httpGet:
        path: /health/live
        port: 8080
      initialDelaySeconds: 30
      periodSeconds: 10
      failureThreshold: 3
    readinessProbe:
      httpGet:
        path: /health/ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
      failureThreshold: 2
    startupProbe:
      httpGet:
        path: /health/start
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
```

## 10.3 Template Anti-Patterns

### Anti-Pattern: Overly Complex Templates

**Bad Practice:**
```yaml
# _helpers.tpl - Too complex
{{- define "myapp.labels" -}}
{{- $ := . -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{ .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
app: {{ $name }}
version: {{ .Chart.Version | quote }}
{{- end -}}
```

**Good Practice:**
```yaml
# Split into smaller functions
{{- define "myapp.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "myapp.fullname" -}}
{{- $name := include "myapp.name" . -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end -}}
{{- end -}}

{{- define "myapp.labels" -}}
app.kubernetes.io/name: {{ include "myapp.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
```

### Anti-Pattern: Not Using Required Function

**Bad Practice:**
```yaml
# Template assumes value exists
image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
# Fails silently if image.repository is empty
```

**Good Practice:**
```yaml
# Template with required validation
image: {{ required "image.repository is required" .Values.image.repository }}:{{ .Values.image.tag | default "latest" }}
```

## 10.4 Release Management Anti-Patterns

### Anti-Pattern: No Atomic Operations

**Bad Practice:**
```bash
# No rollback on failure
helm upgrade myapp ./chart -n production

# If this fails, cluster is left in broken state
```

**Good Practice:**
```bash
# Atomic operation with rollback
helm upgrade --install myapp ./chart -n production \
  --atomic \
  --cleanup-on-fail \
  --wait \
  --timeout 5m

# Or use explicit rollback
helm upgrade --install myapp ./chart -n production \
  --wait --timeout 5m \
  || helm rollback myapp -n production
```

### Anti-Pattern: Not Using Dry-Run

**Bad Practice:**
```bash
# Blind upgrade
helm upgrade myapp ./chart -n production
```

**Good Practice:**
```bash
# Always diff first
helm diff upgrade myapp ./chart -n production

# Then dry-run
helm upgrade myapp ./chart -n production \
  --dry-run \
  --debug

# Finally actual upgrade
helm upgrade --install myapp ./chart -n production
```

## 10.5 Dependency Anti-Patterns

### Anti-Pattern: No Version Constraints

**Bad Practice:**
```yaml
# Chart.yaml
dependencies:
  - name: postgresql
    version: "*"  # Latest always!
    repository: https://charts.bitnami.com
```

**Good Practice:**
```yaml
# Chart.yaml with version constraints
dependencies:
  - name: postgresql
    version: ">=12.0.0 <13.0.0"  # Constrained
    repository: https://charts.bitnami.com
```

### Anti-Pattern: Not Updating Dependencies

**Bad Practice:**
```bash
# No dependency update
helm package ./chart
# Push outdated dependencies to registry
```

**Good Practice:**
```bash
# Always update before release
helm dependency update ./chart
helm dependency build ./chart

# Verify dependencies
helm dependency list ./chart
helm dependency verify ./chart
```

## 10.6 Security Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Running as root | Privilege escalation | Set `runAsNonRoot: true` |
| No readOnlyRootFilesystem | Container breakout | Set `readOnlyRootFilesystem: true` |
| Privileged containers | Full host access | Remove `privileged: true` |
| Host network/pid | Container isolation | Use default namespace/network |
| No AppArmor/SELinux | Host exploits | Configure pod SecurityContext |

### Secure Deployment Template

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 1000
  fsGroup: 1000
  seccompProfile:
    type: RuntimeDefault

podSecurityContext:
  seccompProfile:
    type: RuntimeDefault

securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop:
      - ALL

podSecurityContext:
  sysctls:
    - name: net.ipv4.ip_local_port_range
      value: "49152 65535"
```

## 10.7 Best Practices Summary

### Chart Development
- Use semantic versioning for chart versions
- Add JSON schema validation (values.schema.json)
- Include meaningful NOTES.txt for post-install
- Add tests in templates/tests/
- Document all values in README.md

### Template Writing
- Keep templates simple and readable
- Use named templates for reusability
- Use `required` for mandatory values
- Use `default` with sensible fallbacks
- Test templates with `helm template`

### Release Management
- Always use `--atomic` for production
- Use `--dry-run` before upgrades
- Use `helm diff` plugin for changes
- Keep release history with `helm history`
- Use descriptive release names

### Security
- Never store secrets in values
- Use external secrets operators
- Configure proper security contexts
- Run as non-root user
- Drop all capabilities
- Use read-only root filesystem

### Dependencies
- Pin chart versions
- Use semantic version ranges
- Update before release
- Verify dependencies

### Documentation
- Document all values in README
- Include example values files
- Add troubleshooting section
- Document upgrade procedures
