# Scenario Examples

## 9.1 Production Web Application Deployment

**User:** "How do I deploy a production-ready web application with Helm?"

**Expert:**
> **Solution:**
>
> 1. Create chart with proper structure
> 2. Configure security contexts and probes
> 3. Set up HPA for scaling
> 4. Configure ingress with TLS
>
> ```yaml
> # values-production.yaml
> replicaCount: 3
>
> image:
>   repository: myregistry.io/webapp
>   tag: "1.2.3"
>   pullPolicy: IfNotPresent
>
> service:
>   type: ClusterIP
>   port: 80
>   targetPort: 8080
>
> ingress:
>   enabled: true
>   className: nginx
>   annotations:
>     cert-manager.io/cluster-issuer: letsencrypt-prod
>     nginx.ingress.kubernetes.io/proxy-body-size: "50m"
>   hosts:
>     - host: app.example.com
>       paths:
>         - path: /
>           pathType: Prefix
>   tls:
>     - secretName: app-tls
>       hosts:
>         - app.example.com
>
> resources:
>   limits:
>     cpu: 1000m
>     memory: 512Mi
>   requests:
>     cpu: 200m
>     memory: 256Mi
>
> autoscaling:
>   enabled: true
>   minReplicas: 2
>   maxReplicas: 10
>   targetCPUUtilizationPercentage: 70
>   targetMemoryUtilizationPercentage: 80
>
> podSecurityContext:
>   runAsNonRoot: true
>   runAsUser: 1000
>   fsGroup: 2000
>   seccompProfile:
>     type: RuntimeDefault
>
> securityContext:
>   allowPrivilegeEscalation: false
>   readOnlyRootFilesystem: true
>   capabilities:
>     drop:
>       - ALL
>
> livenessProbe:
>   httpGet:
>     path: /health/live
>     port: 8080
>   initialDelaySeconds: 30
>   periodSeconds: 10
>   failureThreshold: 3
>
> readinessProbe:
>   httpGet:
>     path: /health/ready
>     port: 8080
>   initialDelaySeconds: 5
>   periodSeconds: 5
>   failureThreshold: 2
>
> startupProbe:
>   httpGet:
>     path: /health/start
>     port: 8080
>   failureThreshold: 30
>   periodSeconds: 10
> ```
>
> **Deploy:**
> ```bash
> helm upgrade --install webapp ./chart \
>   --namespace production \
>   --values values-production.yaml \
>   --atomic \
>   --cleanup-on-fail \
>   --wait
> ```

## 9.2 Database Deployment with Bitnami Charts

**User:** "How do I deploy PostgreSQL with persistent storage and backups?"

**Expert:**
> **Solution with Bitnami PostgreSQL:**
>
> ```yaml
> # Chart.yaml dependencies
> dependencies:
>   - name: postgresql
>     version: "12.x.x"
>     repository: "https://charts.bitnami.com"
>
> # values.yaml for production
> postgresql:
>   enabled: true
>   architecture: replication
>   
>   auth:
>     username: myapp
>     database: myappdb
>     existingSecret: myapp-db-secret
>   
>   primary:
>     persistence:
>       enabled: true
>       size: 20Gi
>       storageClass: standard-ssd
>     configuration: |
>       max_connections = 200
>       shared_buffers = 256MB
>       effective_cache_size = 1GB
>       maintenance_work_mem = 64MB
>       checkpoint_completion_target = 0.9
>       wal_buffers = 16MB
>       default_statistics_target = 100
>       random_page_cost = 1.1
>       effective_io_concurrency = 200
>       work_mem = 4MB
>       min_wal_size = 1GB
>       max_wal_size = 4GB
>
>   readReplicas:
>     replicaCount: 2
>     persistence:
>       enabled: true
>       size: 20Gi
>
>   metrics:
>     enabled: true
>     serviceMonitor:
>       enabled: true
> ```
>
> **Deploy:**
> ```bash
> helm dependency update
> helm upgrade --install postgresql ./chart \
>   --namespace database \
>   --create-namespace \
>   --values values-postgres.yaml
> ```

## 9.3 Multi-Environment Configuration

**User:** "How do I manage Helm values across dev, staging, and production?"

**Expert:**
> **Solution with Kustomize and Helm:**
>
> **Base values (values.yaml):**
> ```yaml
> replicaCount: 1
> image:
>   tag: "latest"
> resources:
>   limits:
>     cpu: 500m
>     memory: 256Mi
> ```
>
> **Dev overlay (values-dev.yaml):**
> ```yaml
> replicaCount: 1
> image:
>   tag: "dev-$(git rev-parse --short HEAD)"
> autoscaling:
>   enabled: false
> ingress:
>   enabled: false
> ```
>
> **Production overlay (values-prod.yaml):**
> ```yaml
> replicaCount: 3
> image:
>   tag: "v1.2.3"
> resources:
>   limits:
>     cpu: 2000m
>     memory: 1Gi
> autoscaling:
>   enabled: true
>   minReplicas: 3
>   maxReplicas: 20
> ingress:
>   enabled: true
>   className: nginx
>   annotations:
>     cert-manager.io/cluster-issuer: letsencrypt-prod
> ```
>
> **Deploy script:**
> ```bash
> #!/bin/bash
> ENV=${1:-dev}
> helm upgrade --install myapp ./chart \
>   --namespace $ENV \
>   --values values.yaml \
>   --values values-$ENV.yaml \
>   --set git.sha=$(git rev-parse --short HEAD)
> ```

## 9.4 Helmfile for Complex Deployments

**User:** "How do I manage multiple Helm releases with dependencies?"

**Expert:**
> **Solution with Helmfile:**
>
> ```yaml
> # helmfile.yaml
> bases:
>   - environments.yaml.gotmpl
>
> releases:
>   - name: monitoring
>     chart: prometheus-community/kube-prometheus-stack
>     namespace: monitoring
>     values:
>       - values/monitoring.yaml
>     installed: {{ .Values | getOrNil "monitoring.enabled" | default true }}
>
>   - name: postgresql
>     chart: bitnami/postgresql
>     namespace: database
>     needs:
>       - monitoring/prometheus-operator
>     values:
>       - values/postgresql.yaml
>
>   - name: myapp
>     chart: ./charts/myapp
>     namespace: production
>     needs:
>       - database/postgresql
>       - monitoring
>     values:
>       - values/myapp.yaml
>     secrets:
>       - secrets/myapp-secrets.yaml.gotpl
> ```
>
> **Helmfile commands:**
> ```bash
> # Sync all releases
> helmfile sync
>
> # Diff before sync
> helmfile diff
>
> # Deploy specific release
> helmfile -l name=myapp sync
>
> # Rollback
> helmfile rollback myapp
> ```

## 9.5 Progressive Delivery with Helm

**User:** "How do I implement canary deployments with Helm?"

**Expert:**
> **Solution:**
>
> ```yaml
> # canary-values.yaml
> replicaCount: 4  # Stable version
>
> canary:
>   enabled: true
>   replicas: 1  # Canary version
>
> image:
>   tag: "v2.0.0"  # New version
>
> service:
>   port: 80
>
> # Deployment with weight routing
> # Use Argo Rollouts or Flagger for automated canary
> ```
>
> **With Flagger:**
> ```yaml
> # Canary resource
> apiVersion: flagger.app/v1beta1
> kind: Canary
> metadata:
>   name: myapp
> spec:
>   targetRef:
>     apiVersion: apps/v1
>     kind: Deployment
>     name: myapp
>   service:
>     port: 80
>   analysis:
>     interval: 1m
>     threshold: 5
>     maxWeight: 50
>     stepWeight: 10
>     metrics:
>       - name: request-success-rate
>         thresholdRange:
>           min: 99
>       - name: request-duration
>         thresholdRange:
>           max: 500
> ```
>
> **Deploy canary:**
> ```bash
> # Upgrade stable version
> helm upgrade myapp ./chart --set image.tag=v2.0.0
>
> # Flagger automatically manages canary weight
> # Monitor progression
> kubectl get canary --watch
> ```

## 9.6 Helm Hooks for Lifecycle Management

**User:** "How do I run jobs before/after Helm operations?"

**Expert:**
> **Solution with Hooks:**
>
> ```yaml
> # templates/job-db-migration.yaml
> apiVersion: batch/v1
> kind: Job
> metadata:
>   name: {{ .Release.Name }}-db-migration
>   labels:
>     app.kubernetes.io/managed-by: Helm
>   annotations:
>     helm.sh/hook: pre-upgrade,pre-rollback
>     helm.sh/hook-weight: "-1"
>     helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
> spec:
>   template:
>     spec:
>       restartPolicy: Never
>       containers:
>         - name: migrate
>           image: myapp/migrate:latest
>           env:
>             - name: DATABASE_URL
>               valueFrom:
>                 secretKeyRef:
>                   name: myapp-db-secret
>                   key: url
>           command: ["python", "manage.py", "migrate"]
> ```
>
> **Other hook types:**
> ```yaml
> annotations:
>   # Lifecycle hooks
>   helm.sh/hook: post-install,post-upgrade,post-rollback,post-delete
>   
>   # Test hooks
>   helm.sh/hook: test
>   
>   # Cleanup hooks
>   helm.sh/hook-delete-policy: hook-succeeded,hook-failed,before-hook-creation
> ```

## 9.7 Library Charts for Reusable Components

**User:** "How do I create reusable Helm patterns?"

**Expert:**
> **Solution with Library Chart:**
>
> ```yaml
> # Library chart structure
> # mychart-library/
> # ├── Chart.yaml (type: library)
> # ├── templates/
> # │   ├── _deployment.yaml
> # │   ├── _service.yaml
> # │   └── _helpers.tpl
>
> # Chart.yaml
> apiVersion: v2
> name: mychart-library
> type: library
> version: 0.1.0
>
> # templates/_deployment.yaml
> {{/*
> Generic deployment template
> */}}
> {{- define "mylib.deployment" -}}
> {{- $ := . }}
> {{- $fullName := include "mylib.fullname" $ -}}
> apiVersion: apps/v1
> kind: Deployment
> metadata:
>   name: {{ $fullName }}
>   labels:
>     {{- include "mylib.labels" $ | nindent 4 }}
> spec:
>   replicas: {{ $.Values.replicaCount | default 1 }}
>   selector:
>     matchLabels:
>       {{- include "mylib.selectorLabels" $ | nindent 6 }}
>   template:
>     metadata:
>       labels:
>         {{- include "mylib.labels" $ | nindent 8 }}
>     spec:
>       containers:
>         - name: {{ $.Chart.Name }}
>           image: "{{ $.Values.image.repository }}:{{ $.Values.image.tag }}"
>           imagePullPolicy: {{ $.Values.image.pullPolicy }}
>           ports:
>             - name: http
>               containerPort: 8080
> {{- end }}
> ```
>
> **Usage in app chart:**
> ```yaml
> # Chart.yaml
> dependencies:
>   - name: mychart-library
>     version: "0.1.x"
>     repository: "https://charts.example.com"
>
> # templates/deployment.yaml
> {{- include "mylib.deployment" . -}}
> ```
