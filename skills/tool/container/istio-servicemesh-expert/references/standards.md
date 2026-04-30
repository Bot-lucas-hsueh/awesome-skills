# Standards & Reference

## 7.1 Official Documentation

- [Istio Documentation](https://istio.io/latest/docs/)
- [Istio API Reference](https://istio.io/latest/docs/reference/config/)
- [Istio Operator API](https://istio.io/latest/docs/reference/config/istio.operator.v1alpha1/)
- [Envoy Proxy Documentation](https://www.envoyproxy.io/docs/envoy/latest/)
- [Istio Bookinfo Sample](https://istio.io/latest/docs/examples/bookinfo/)
- [Istio Certificate Management](https://istio.io/latest/docs/ops/basic-traffic-management/certificates/)
- [Ambient Mesh Documentation](https://istio.io/latest/docs/ops/ambient/)

## 7.2 Configuration Reference

### Gateway Configuration

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: production-gateway
  namespace: istio-system
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      tls:
        mode: SIMPLE
        credentialName: wildcard-tls-secret
      hosts:
        - "*.example.com"
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - "example.com"
      tls:
        httpsRedirect: true
```

### VirtualService Configuration

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews-route
  namespace: default
spec:
  hosts:
    - reviews
  http:
    - match:
        - headers:
            x-canary:
              exact: "true"
      route:
        - destination:
            host: reviews
            subset: v2
          weight: 100
    - route:
        - destination:
            host: reviews
            subset: v1
          weight: 100
```

### DestinationRule Configuration

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews-destination
  namespace: default
spec:
  host: reviews
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: UPGRADE
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
    loadBalancer:
      simple: LEAST_CONN
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
```

### PeerAuthentication (mTLS)

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
---
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: permissive-namespace
  namespace: legacy-apps
spec:
  mtls:
    mode: PERMISSIVE
```

### AuthorizationPolicy

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: frontend-access
  namespace: default
spec:
  selector:
    matchLabels:
      app: reviews
  action: ALLOW
  rules:
    - from:
        - source:
            principals: ["cluster.local/ns/default/sa/frontend"]
      to:
        - operation:
            methods: ["GET"]
            paths: ["/reviews/*"]
    - from:
        - source:
            namespaces: ["istio-system"]
      to:
        - operation:
            ports: ["15020"]
```

## 7.3 Common Commands & Operations

### Istioctl Commands

```bash
# Check Istio installation status
istioctl x precheck
istioctl verify-install -f manifests/profiles/default.yaml

# Analyze running configuration
istioctl analyze --namespace default
istioctl analyze --allNamespaces

# View Envoy configuration
istioctl proxy-config cluster <pod-name> -n default
istioctl proxy-config route <pod-name> -n default
istioctl proxy-config endpoint <pod-name> -n default
istioctl proxy-config listener <pod-name> -n default

# Debugging
istioctl proxy-config log <pod-name> --level debug
istioctl proxy-config bootstrap <pod-name> -o json

# Traffic management
istioctl experimental wait -n default virtualservice reviews 30s
istioctl x describe pod <pod-name>

# Revision management
istioctl revision list
istioctl revision tag set canary --revision 1-20
```

### Sidecar Injection

```bash
# Enable injection on namespace
kubectl label namespace default istio-injection=enabled

# Disable injection on namespace
kubectl label namespace default istio-injection=disabled --overwrite

# Inject manually (if not automatic)
istioctl kube-inject -f deployment.yaml | kubectl apply -f -

# Check sidecar status
kubectl get pod -l security.istio.io/injection=enabled -n default
```

### mTLS Debugging

```bash
# Check if mTLS is enabled
istioctl authz tls-check <pod-name> -n default

# View mTLS mode per namespace
kubectl get peerauthentication --all-namespaces

# Test mTLS connectivity
kubectl exec <source-pod> -n default -- curl -v https://<target-service>:8080

# Check DestinationRule TLS settings
istioctl proxy-config cluster <pod-name> -n default --export | grep -i tls
```

## 7.4 Version Compatibility

| Istio Version | Kubernetes | Ambient Mode | Major Features |
|--------------|------------|--------------|----------------|
| 1.22.x | 1.27-1.30 | Beta | Gateway API GA, ztunnel improvements |
| 1.21.x | 1.26-1.29 | Alpha | Waypoint proxies, Enterprise features |
| 1.20.x | 1.25-1.28 | - | CPU optimization, health probes |
| 1.19.x | 1.24-1.27 | - | ExternalName support |
| 1.18.x | 1.23-1.26 | - | WASM extensibility |

### Upgrade Path

```bash
# Check upgrade prerequisites
istioctl x precheck --revision 1-22

# Supported upgrade paths:
# 1.17 -> 1.18 -> 1.19 -> 1.20 -> 1.21 -> 1.22

# Canary upgrade
istioctl operator init --revision 1-22 --set values.defaultRevision=default

# Migrate workloads
kubectl label namespace default istio.io/rev=1-22 --overwrite
kubectl rollout restart deployment -n default
```

### Component Support Matrix

| Component | Status | Min Version |
|-----------|--------|-------------|
| Ingress Gateway | Stable | 1.4 |
| Egress Gateway | Stable | 1.4 |
| Sidecar Proxy | Stable | 1.4 |
| ztunnel | Beta | 1.20 |
| Waypoint Proxy | Beta | 1.21 |
| CNI Plugin | Stable | 1.6 |
| Ambient Mesh | Beta | 1.20 |
