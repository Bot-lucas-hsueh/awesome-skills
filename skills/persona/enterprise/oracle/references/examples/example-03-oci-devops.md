# Example 3: OCI DevOps CI/CD Pipeline

## Context

Enterprise development team deploying microservices to OCI Kubernetes Engine (OKE)
with requirements for automated testing, security scanning, and blue-green deployments.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Developer Workflow                           │
│  Code Commit → Build → Test → Security Scan → Deploy → Monitor      │
└───────────────────────┬─────────────────────────────────────────────┘
                        │
┌───────────────────────┼─────────────────────────────────────────────┐
│                       ▼                                             │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              OCI DevOps Service (CI/CD)                      │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │   │
│  │  │  Build   │→│   Test   │→│  Security│→│  Deploy  │    │   │
│  │  │  Pipeline│  │ Pipeline │  │  Scan    │  │ Pipeline │    │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    OKE Cluster                               │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │   │
│  │  │  Blue Env   │  │  Green Env  │  │   Ingress   │         │   │
│  │  │  (Current)  │  │  (Staging)  │  │  Controller │         │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘         │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## OCI DevOps Project Structure

```yaml
# devops-project-structure
project/
├── build-pipeline.yaml
├── deployment-pipeline.yaml
├── terraform/
│   ├── main.tf
│   ├── oke.tf
│   └── network.tf
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── configmap.yaml
├── tests/
│   ├── unit/
│   ├── integration/
│   └── security/
└── build_spec.yaml
```

## Build Pipeline

### build_spec.yaml

```yaml
version: 0.1
component: build
timeoutInSeconds: 6000
runAs: root
shell: bash
env:
  vaultVariables:
    OCIR_AUTH_TOKEN: ocid1.vaultsecret.oc1..xxx
    DB_PASSWORD: ocid1.vaultsecret.oc1..yyy
  exportedVariables:
    - BUILD_ID
    - IMAGE_TAG
    - APP_VERSION

steps:
  - type: Command
    name: "Define Build Variables"
    command: |
      export BUILD_ID=${OCI_BUILD_RUN_ID}
      export IMAGE_TAG=${OCI_BUILD_RUN_ID:0:8}
      export APP_VERSION=$(cat package.json | grep version | head -1 | awk -F: '{ print $2 }' | sed 's/[",]//g' | tr -d '[[:space:]]')
      echo "Building version ${APP_VERSION} with tag ${IMAGE_TAG}"

  - type: Command
    name: "Install Dependencies"
    command: |
      npm ci

  - type: Command
    name: "Run Unit Tests"
    command: |
      npm run test:unit -- --coverage --coverageReporters=text-summary
    onFailure:
      - type: Command
        command: |
          echo "Unit tests failed. Stopping build."
          exit 1

  - type: Command
    name: "Run Integration Tests"
    command: |
      npm run test:integration
    onFailure:
      - type: Command
        command: |
          echo "Integration tests failed. Stopping build."
          exit 1

  - type: Command
    name: "Security Scan - Dependency Check"
    command: |
      npm audit --audit-level=high
      if [ $? -ne 0 ]; then
        echo "High severity vulnerabilities found."
        exit 1
      fi

  - type: Command
    name: "Security Scan - Code Analysis"
    command: |
      sonar-scanner \
        -Dsonar.projectKey=${OCI_PROJECT_NAME} \
        -Dsonar.sources=. \
        -Dsonar.host.url=${SONAR_HOST} \
        -Dsonar.login=${SONAR_TOKEN}

  - type: Command
    name: "Build Docker Image"
    command: |
      docker build \
        --build-arg APP_VERSION=${APP_VERSION} \
        --build-arg BUILD_ID=${BUILD_ID} \
        -t ${OCIR_HOST}/${OCIR_NAMESPACE}/${IMAGE_NAME}:${IMAGE_TAG} \
        -t ${OCIR_HOST}/${OCIR_NAMESPACE}/${IMAGE_NAME}:latest \
        .

  - type: Command
    name: "Scan Docker Image"
    command: |
      docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
        aquasec/trivy image \
        --exit-code 1 \
        --severity HIGH,CRITICAL \
        ${OCIR_HOST}/${OCIR_NAMESPACE}/${IMAGE_NAME}:${IMAGE_TAG}

  - type: Command
    name: "Push to OCIR"
    command: |
      echo ${OCIR_AUTH_TOKEN} | docker login ${OCIR_HOST} -u ${OCIR_NAMESPACE} --password-stdin
      docker push ${OCIR_HOST}/${OCIR_NAMESPACE}/${IMAGE_NAME}:${IMAGE_TAG}
      docker push ${OCIR_HOST}/${OCIR_NAMESPACE}/${IMAGE_NAME}:latest

outputArtifacts:
  - name: deployment_manifest
    type: BINARY
    location: kubernetes/
  - name: terraform_config
    type: BINARY
    location: terraform/
```

### Dockerfile

```dockerfile
# Multi-stage build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

WORKDIR /app
COPY --from=builder --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs . .

USER nextjs
EXPOSE 3000
ENV NODE_ENV=production

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

CMD ["npm", "start"]
```

## Deployment Pipeline

### deployment-pipeline.yaml (Terraform)

```hcl
resource "oci_devops_deploy_pipeline" "main" {
  compartment_id = var.compartment_id
  project_id     = oci_devops_project.main.id
  display_name   = "${var.app_name}-deploy-pipeline"
  
  description = "Blue-green deployment pipeline"
}

# Deploy to Blue Environment
resource "oci_devops_deploy_stage" "deploy_blue" {
  deploy_pipeline_id = oci_devops_deploy_pipeline.main.id
  display_name       = "Deploy to Blue"
  deploy_stage_type  = "OKE_DEPLOY"
  
  oke_deploy_stage {
    cluster_id        = oci_containerengine_cluster.main.id
    namespace         = "blue"
    deployment_spec   = file("${path.module}/kubernetes/deployment-blue.yaml")
    
    kubernetes_manifest_deploy_artifact_id = oci_devops_deploy_artifact.manifest.id
  }
}

# Run Smoke Tests
resource "oci_devops_deploy_stage" "smoke_tests" {
  deploy_pipeline_id = oci_devops_deploy_pipeline.main.id
  display_name       = "Smoke Tests"
  deploy_stage_type  = "SHELL"
  
  shell_deploy_stage {
    command = <<-EOT
      #!/bin/bash
      set -e
      
      BLUE_URL="https://blue.${var.domain}/health"
      
      # Wait for deployment
      sleep 30
      
      # Health check
      for i in {1..10}; do
        if curl -sf ${BLUE_URL}; then
          echo "Health check passed"
          exit 0
        fi
        sleep 10
      done
      
      echo "Health check failed"
      exit 1
    EOT
  }
}

# Switch Traffic (Blue-Green)
resource "oci_devops_deploy_stage" "switch_traffic" {
  deploy_pipeline_id = oci_devops_deploy_pipeline.main.id
  display_name       = "Switch Traffic to Blue"
  deploy_stage_type  = "SHELL"
  
  shell_deploy_stage {
    command = <<-EOT
      #!/bin/bash
      kubectl patch service app-service -p '{"spec":{"selector":{"version":"blue"}}}'
    EOT
  }
}

# Cleanup Green Environment
resource "oci_devops_deploy_stage" "cleanup_green" {
  deploy_pipeline_id = oci_devops_deploy_pipeline.main.id
  display_name       = "Cleanup Green"
  deploy_stage_type  = "SHELL"
  
  shell_deploy_stage {
    command = <<-EOT
      #!/bin/bash
      kubectl delete deployment app-green -n green --ignore-not-found=true
    EOT
  }
}
```

## Kubernetes Manifests

### deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-blue
  namespace: blue
  labels:
    app: microservice
    version: blue
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: microservice
      version: blue
  template:
    metadata:
      labels:
        app: microservice
        version: blue
    spec:
      containers:
      - name: app
        image: ${OCIR_HOST}/${OCIR_NAMESPACE}/${IMAGE_NAME}:${IMAGE_TAG}
        ports:
        - containerPort: 3000
          protocol: TCP
        env:
        - name: NODE_ENV
          value: "production"
        - name: DB_HOST
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: host
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: password
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
        securityContext:
          runAsNonRoot: true
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
---
apiVersion: v1
kind: Service
metadata:
  name: app-service
  namespace: blue
spec:
  type: ClusterIP
  selector:
    app: microservice
  ports:
  - port: 80
    targetPort: 3000
    protocol: TCP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  namespace: blue
  annotations:
    kubernetes.io/ingress.class: "nginx"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  tls:
  - hosts:
    - api.example.com
    secretName: app-tls
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
```

## Infrastructure as Code

### oke.tf

```hcl
# OKE Cluster
resource "oci_containerengine_cluster" "main" {
  compartment_id     = var.compartment_id
  kubernetes_version = "v1.28.2"
  name               = "${var.app_name}-cluster"
  vcn_id             = oci_core_vcn.main.id
  
  options {
    add_ons {
      is_kubernetes_dashboard_enabled = false
      is_tiller_enabled               = false
    }
    
    admission_controller_options {
      is_pod_security_policy_enabled = true
    }
    
    kubernetes_network_config {
      pods_cidr     = "10.244.0.0/16"
      services_cidr = "10.96.0.0/16"
    }
    
    service_lb_subnet_ids = [oci_core_subnet.lb.id]
  }
  
  endpoint_config {
    is_public_ip_enabled = false
    subnet_id            = oci_core_subnet.endpoint.id
  }
}

# Node Pool
resource "oci_containerengine_node_pool" "main" {
  cluster_id         = oci_containerengine_cluster.main.id
  compartment_id     = var.compartment_id
  kubernetes_version = "v1.28.2"
  name               = "${var.app_name}-nodes"
  node_shape         = "VM.Standard.E4.Flex"
  
  node_shape_config {
    ocpus         = 2
    memory_in_gbs = 16
  }
  
  node_config_details {
    placement_configs {
      availability_domain = data.oci_identity_availability_domains.ads.availability_domains[0].name
      subnet_id           = oci_core_subnet.nodes.id
    }
    
    size = 3
    
    node_pool_pod_network_option_details {
      cidr_type   = "FLANNEL_OVERLAY"
      max_pods    = 110
    }
  }
  
  initial_node_labels {
    key   = "environment"
    value = var.environment
  }
  
  node_eviction_node_pool_settings {
    eviction_grace_duration = "PT1H"
  }
}
```

## Deployment Commands

```bash
# Trigger build pipeline
oci devops build-run create \
    --build-pipeline-id $BUILD_PIPELINE_ID \
    --display-name "Release v1.2.3"

# Monitor build
oci devops build-run get \
    --build-run-id $BUILD_RUN_ID \
    --query "data.progress"

# Trigger deployment
oci devops deployment create \
    --deploy-pipeline-id $DEPLOY_PIPELINE_ID \
    --display-name "Deploy v1.2.3 to Production" \
    --deployment-arguments file://deployment-args.json

# Rollback
kubectl rollout undo deployment/app-blue -n blue
```

## Monitoring Integration

```yaml
# ServiceMonitor for Prometheus
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: app-metrics
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: microservice
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
---
# OCI Monitoring Alarm
resource "oci_monitoring_alarm" "high_error_rate" {
  compartment_id        = var.compartment_id
  display_name          = "High Error Rate"
  metric_compartment_id = var.compartment_id
  namespace             = "oci_oke"
  query                 = "ErrorRate[5m].mean() > 5"
  severity              = "CRITICAL"
  destinations          = [oci_ons_notification_topic.alerts.id]
  message_format        = "ONS_OPTIMIZED"
  
  body = <<-EOT
    High error rate detected in application.
    Current value: ${metric.value}
    Please investigate immediately.
  EOT
}
```

## Key Learnings

1. **Security First**: Scan at multiple stages (dependencies, code, container)
2. **Blue-Green Deployments**: Zero-downtime releases with instant rollback
3. **Health Checks**: Comprehensive liveness, readiness, and smoke tests
4. **Resource Limits**: Prevent resource exhaustion with proper limits
5. **Observability**: Metrics, logs, and traces for full visibility

---

*Example Version: 5.0.0*
