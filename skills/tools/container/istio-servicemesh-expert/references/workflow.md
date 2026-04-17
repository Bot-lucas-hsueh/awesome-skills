# Standard Workflow

## 8.1 Traffic Management Workflow

```
Istio Traffic Management Flow
══════════════════════════════════════════════════════════════

[Client] → [Ingress Gateway] → [Sidecar Proxy] → [Application]
              │                        │
              ▼                        ▼
         [Gateway]              [VirtualService]
              │                        │
              ▼                        ▼
         [DestinationRule] ←── [Service Discovery]
              │
              ▼
         [Envoy LB Pool]
```

### Canary Deployment Workflow

```bash
# 1. Deploy new version alongside existing
kubectl apply -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: reviews
spec:
  ports:
    - port: 9080
      name: http
  selector:
    app: reviews
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reviews-v2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: reviews
      version: v2
  template:
    metadata:
      labels:
        app: reviews
        version: v2
    spec:
      containers:
        - image: gcr.io/istio-samples/bookinfo-reviews:v2
          name: reviews
          ports:
            - containerPort: 9080
EOF

# 2. Create DestinationRule for subsets
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews
spec:
  host: reviews
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
EOF

# 3. Route 10% to v2
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews
  http:
    - route:
        - destination:
            host: reviews
            subset: v1
          weight: 90
        - destination:
            host: reviews
            subset: v2
          weight: 10
EOF

# 4. Monitor metrics
istioctl dashboard grafana

# 5. Gradual rollout
kubectl patch virtualservice reviews --type merge -p '{
  "spec":{"http":[{"route":[{"destination":{"subset":"v1"},"weight":50},
                              {"destination":{"subset":"v2"},"weight":50}]}]}
}'

# 6. Full cutover
kubectl patch virtualservice reviews --type merge -p '{
  "spec":{"http":[{"route":[{"destination":{"subset":"v2"},"weight":100}]}]}
}'
```

### Traffic Mirroring

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: httpbin-mirror
spec:
  hosts:
    - httpbin
  http:
    - route:
        - destination:
            host: httpbin
            subset: v1
          weight: 100
        - destination:
            host: httpbin
            subset: v2
          weight: 0
      mirror:
        host: httpbin
        subset: v2
      mirrorPercentage:
        value: 100
```

## 8.2 Integration Workflow

### Prometheus Integration

```bash
# Enable metrics collection
kubectl apply -f - <<EOF
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: istio-components
  namespace: istio-system
  labels:
    release: prometheus
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  endpoints:
    - port: http-monitoring
      path: /stats/prometheus
---
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: istio-sidecars
  namespace: istio-system
spec:
  selector:
    matchLabels:
      security.istio.io/injection: enabled
  podMetricsEndpoints:
    - port: http-envoy-prom
      path: /stats/prometheus
```

### Grafana Dashboard Setup

```bash
# Import Istio dashboards
istioctl dash grafana

# Common dashboards:
# - Istio Mesh Dashboard
# - Istio Service Dashboard
# - Istio Workload Dashboard
# - Istio Control Plane Dashboard
```

### ServiceEntry for External Services

```yaml
# Allow controlled external access with mTLS
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: external-api
spec:
  hosts:
    - api.stripe.com
  ports:
    - number: 443
      name: https
      protocol: HTTPS
  location: MESH_EXTERNAL
  resolution: DNS
  workloadEntry:
    - address: 10.0.0.1
      locality: us-east-1
      weight: 100
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: stripe-mtls
spec:
  host: api.stripe.com
  trafficPolicy:
    tls:
      mode: MUTUAL
      clientCertificate: /etc/certs/cert-chain.pem
      privateKey: /etc/certs/key.pem
      caCertificates: /etc/certs/root-cert.pem
```

## 8.3 Observability Workflow

### Distributed Tracing Setup

```yaml
# Enable tracing in Istio
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: istio-with-tracing
  namespace: istio-system
spec:
  profile: default
  components:
    pilot:
      k8s:
        env:
          - name: PILOT_TRACE_SAMPLING
            value: "1.0"
  values:
    meshConfig:
      enableTracing: true
      defaultConfig:
        tracing:
          sampling: 1.0
          zipkin:
            address: jaeger-collector.observability:9411
```

### Kiali Dashboard

```bash
# Access Kiali
istioctl dash kiali

# Common queries:
# - Service graph topology
# - Request flow visualization
# - Traffic rates and latencies
# - mTLS status across services

# Validate mesh configuration
istioctl x analyze --namespace default
```

### Logging Configuration

```yaml
apiVersion: networking.istio.io/v1beta1
kind: EnvoyFilter
metadata:
  name: access-log-format
  namespace: istio-system
spec:
  workloadSelector:
    labels:
      istio: ingressgateway
  configPatches:
    - applyTo: NETWORK_FILTER
      match:
        context: SIDECAR_INBOUND
        listener:
          filterChain:
            filter:
              name: envoy.filters.network.http_connection_manager
      patch:
        operation: MERGE
        value:
          typed_config:
            "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
            access_log:
              - name: envoy.access_loggers.file
                typed_config:
                  "@type": type.googleapis.com/envoy.extensions.access_loggers.file.v3.FileAccessLog
                  path: /dev/stdout
                  format:
                    string_format: "[%START_TIME%] %REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL% %RESPONSE_CODE% %RESPONSE_FLAGS% %BYTES_RECEIVED% %BYTES_SENT% %DURATION% %REQ(X-REQUEST-ID)% %REQ(X-B3-TRACEID)% %REQ(x-envoy-peer-metadata)% %RESPONSE_CODE_DETAILS% %CONNECTION_TERMINATION_DETAILS% %UPSTREAM_TRANSPORT_FAILURE_REASON% %PATH% %UPSTREAM_HOST%"
```

### Health Check Configuration

```yaml
# Configure proper health checks through Envoy
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews-health-check
spec:
  host: reviews
  trafficPolicy:
    healthCheck:
      interval: 10s
      path: /healthz/ready
      timeout: 3s
      healthyThreshold: 2
      unhealthyThreshold: 3
```
