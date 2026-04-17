# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Prevention |
|---|---------|----------|--------|------------|
| 1 | **Deploying without `istio-injection` label** | 🔴 Critical | No sidecar, no mesh features | Always label namespace first |
| 2 | **Conflicting VirtualServices** | 🔴 High | Unpredictable routing | Use `istioctl analyze` |
| 3 | **No health checks configured** | 🟠 Medium | Bad backends in rotation | Configure readiness/liveness |
| 4 | **Excessive retries causing cascading failures** | 🟠 Medium | Traffic amplification | Set retry budget limits |
| 5 | **Outlier detection too aggressive** | 🟡 Medium | False ejections | Tune consecutive errors |
| 6 | **Ignoring Envoy resource limits** | 🟠 Medium | OOM kills | Set memory/CPU limits |
| 7 | **Mixing mTLS modes incorrectly** | 🔴 High | Intermittent auth failures | Phase permissive → strict |
| 8 | **Not using managed certificates** | 🟡 Medium | Certificate expiration issues | Use cert-manager integration |

### Anti-Pattern: Missing Sidecar Injection

**Bad Practice:**
```yaml
# Deploying to namespace without injection
apiVersion: v1
kind: Namespace
metadata:
  name: production
  # No istio-injection label!
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: api
          image: api:v1.0
```

**Good Practice:**
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    istio-injection: enabled  # CRITICAL!
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: api
        version: v1
    spec:
      containers:
        - name: api
          image: api:v1.0
          readinessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
```

### Anti-Pattern: Overly Aggressive Retries

**Bad Practice:**
```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api
spec:
  hosts:
    - api
  http:
    - route:
        - destination:
            host: api
      retries:
        attempts: 100  # Dangerous!
        perTryTimeout: 1s
        retryOn: gateway-error,connect-failure,reset
```

**Good Practice:**
```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api
spec:
  hosts:
    - api
  http:
    - route:
        - destination:
            host: api
      retries:
        attempts: 3
        perTryTimeout: 3s
        retryOn: 5xx,connect-failure,reset
        retryRemoteLocalities: false
```

### Anti-Pattern: No Circuit Breaker Configuration

**Bad Practice:**
```yaml
# No traffic policy = no protection
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: backend
spec:
  host: backend
  subsets:
    - name: v1
      labels:
        version: v1
  # No trafficPolicy!
```

**Good Practice:**
```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: backend
spec:
  host: backend
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http2MaxRequests: 1000
        maxPendingRequests: 100
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
      minHealthPercent: 30
  subsets:
    - name: v1
      labels:
        version: v1
```

## 10.2 Anti-Patterns

### Anti-Pattern 1: Global mtls: PERMISSIVE Forever

**Problem:** Staying in permissive mode indefinitely leaves the mesh vulnerable.

**Why It's Bad:**
- No guarantee of service-to-service encryption
- Attackers can intercept traffic
- Compliance violations

**Solution:**
```bash
# Monitor permissive usage
istioctl authz tls-check <pod> -n <namespace>

# Gradually move to STRICT
# 1. Identify non-mTLS services
# 2. Update them to use mTLS
# 3. Switch namespace to STRICT
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: <namespace>
spec:
  mtls:
    mode: STRICT
EOF
```

### Anti-Pattern 2: Multiple VirtualServices for Same Host

**Problem:** Conflicting route rules cause unpredictable behavior.

**Bad Practice:**
```yaml
# virtualservice-1.yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api-routes
spec:
  hosts:
    - api.example.com
  http:
    - route:
        - destination:
            host: api-service
---
# virtualservice-2.yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api-mirror
spec:
  hosts:
    - api.example.com  # Same host!
  http:
    - route:
        - destination:
            host: api-service-v2  # Different destination
```

**Solution:**
```bash
# Detect with istioctl
istioctl analyze --namespace <namespace>

# Merge into single VirtualService
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api-combined
spec:
  hosts:
    - api.example.com
  http:
    - match:
        - uri:
            prefix: /v2
      route:
        - destination:
            host: api-service-v2
    - route:
        - destination:
            host: api-service
```

### Anti-Pattern 3: Ignoring Envoy Resource Limits

**Problem:** Sidecar containers consume excessive memory/CPU, causing OOM kills.

**Bad Practice:**
```yaml
apiVersion: v1
kind: Deployment
metadata:
  name: api
spec:
  template:
    spec:
      containers:
        - name: istio-proxy
          resources: {}  # No limits!
```

**Good Practice:**
```yaml
apiVersion: v1
kind: Deployment
metadata:
  name: api
spec:
  template:
    metadata:
      annotations:
        sidecar.istio.io/resources: |
          {"limits":{"cpu":"500m","memory":"512Mi"},"requests":{"cpu":"100m","memory":"128Mi"}}
```

### Anti-Pattern 4: Using Wrong Protocol in Service Port

**Problem:** Defining port protocol incorrectly breaks mTLS and routing.

**Bad Practice:**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  ports:
    - name: http
      port: 8080
      targetPort: 8080
      protocol: TCP  # Should be HTTP for Istio routing
```

**Good Practice:**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  ports:
    - name: http
      port: 8080
      targetPort: 8080
      protocol: TCP  # Let Istio auto-detect, or...
    - name: http-web
      port: 8080
      targetPort: 8080
      # For explicit protocol (if auto-detection fails):
      # appProtocol: http
```

### Anti-Pattern 5: Not Using DestinationRule Subsets

**Problem:** Referencing subsets in VirtualService without defining them.

**Bad Practice:**
```yaml
# VirtualService references subset "v2"
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api
spec:
  hosts:
    - api
  http:
    - route:
        - destination:
            host: api
            subset: v2  # Never defined!
```

**Solution:**
```bash
# Always define subsets in DestinationRule first
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: api
spec:
  host: api
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
EOF
```
