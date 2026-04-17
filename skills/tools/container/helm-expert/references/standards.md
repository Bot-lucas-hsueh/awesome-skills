# Standards & Reference

## 7.1 Official Documentation

- [Helm Documentation](https://helm.sh/docs/)
- [Helm Chart Template Guide](https://helm.sh/docs/chart_template_guide/)
- [Helm Chart Best Practices](https://helm.sh/docs/chart_best_practices/)
- [Helm Repository](https://artifacthub.io/)
- [Kubernetes Helm](https://github.com/helm/helm)

## 7.2 Chart Structure

```
mychart/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default configuration values
├── values.schema.json  # JSON schema for values validation
├── charts/             # Dependency charts
├── crds/               # Custom Resource Definitions
├── templates/          # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── _helpers.tpl    # Named templates
│   └── NOTES.txt       # Post-install notes
└── templates/tests/    # Test files
    └── test-connection.yaml
```

## 7.3 Chart.yaml Reference

```yaml
apiVersion: v2
name: mychart
description: A Helm chart for Kubernetes
type: application
version: 1.0.0
appVersion: "1.0.0"
kubeVersion: ">=1.20.0"
keywords:
  - myapp
  - kubernetes
home: https://myapp.example.com
sources:
  - https://github.com/myorg/myapp
maintainers:
  - name: My Name
    email: myemail@example.com
    url: https://myapp.example.com
annotations:
  category: Application
```

## 7.4 Values.yaml Best Practices

```yaml
# Default values
replicaCount: 3

image:
  repository: myregistry.io/myapp
  pullPolicy: IfNotPresent
  tag: "v1.0.0"

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

serviceAccount:
  create: true
  annotations: {}
  name: ""

service:
  type: ClusterIP
  port: 80
  targetPort: 8080
  annotations: {}

ingress:
  enabled: true
  className: nginx
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
  hosts:
    - host: myapp.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: myapp-tls
      hosts:
        - myapp.example.com

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 100m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70

nodeSelector: {}

tolerations: []

affinity: {}

podSecurityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000

securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop:
      - ALL

livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

## 7.5 Template Functions

### Common Functions

```yaml
# Values access
name: {{ .Release.Name }}
namespace: {{ .Release.Namespace }}
version: {{ .Chart.Version }}

# Default value
imageTag: {{ .Values.image.tag | default "latest" }}

# Quote strings
name: {{ .Values.name | quote }}

# Upper/Lower
env: {{ .Values.env | upper }}

# Ternary
replicas: {{ .Values.reValues.replicaCount | default 3 | int }}

# Required value
image: {{ required "image repository is required" .Values.image.repository }}

# Include template
{{ include "mychart.labels" . }}

# Tpl - template from string
{{ .Values.someTemplate | tpl }}
```

### Flow Control

```yaml
{{- if .Values.enabled }}
apiVersion: v1
kind: Service
{{- end }}

{{- if eq .Values.environment "production" }}
replicas: 5
{{- else }}
replicas: 1
{{- end }}

{{- range $key, $value := .Values.labels }}
{{ $key }}: {{ $value }}
{{- end }}

{{- range .Values.service.ports }}
- name: {{ .name }}
  port: {{ .port }}
{{- end }}
```

## 7.6 Helpers Template (_helpers.tpl)

```yaml
{{/*
Expand the name of the chart.
*/}}
{{- define "mychart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "mychart.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "mychart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "mychart.labels" -}}
helm.sh/chart: {{ include "mychart.chart" . }}
{{ include "mychart.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "mychart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "mychart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "mychart.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- include "mychart.fullname" . }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
```

## 7.7 Common Commands

```bash
# Create new chart
helm create mychart

# Install release
helm install myrelease ./mychart

# Install with values
helm install myrelease ./mychart -f values-prod.yaml

# Upgrade release
helm upgrade myrelease ./mychart

# Rollback
helm rollback myrelease 1

# Template (dry-run)
helm template ./mychart --debug

# lint chart
helm lint ./mychart

# Package chart
helm package ./mychart

# Dependency update
helm dependency update ./mychart

# Get manifest
helm get manifest myrelease

# Get values
helm get values myrelease

# List releases
helm list --all-namespaces
```