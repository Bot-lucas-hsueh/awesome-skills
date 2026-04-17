# Troubleshooting

## 8.1 Sidecar Injection Issues

### Sidecar Not Injected

**Symptoms:** Pod doesn't have istio-proxy container, traffic not going through Envoy

**Diagnosis:**
```bash
# Check namespace label
kubectl get namespace default -o jsonpath='{.metadata.labels}'

# Check pod injection status
kubectl get pod <pod-name> -o jsonpath='{.metadata.labels}'

# Describe pod to see init containers
kubectl describe pod <pod-name> | grep -A20 "Init Containers"
```

**Solutions:**
```bash
# Enable injection on namespace
kubectl label namespace default istio-injection=enabled --overwrite

# Disable and re-enable to force reinjection
kubectl label namespace default istio-injection=disabled
kubectl label namespace default istio-injection=enabled

# Delete pods to trigger reinjection
kubectl delete pod <pod-name>
```

### Sidecar Proxy Not Starting

**Symptoms:** Pod stuck in `ContainerCreating`, istio-proxy not running

**Diagnosis:**
```bash
# Check pod events
kubectl describe pod <pod-name>

# Check istiod logs
kubectl logs -n istio-system -l app=istiod --tail=50

# Check for CNI issues
kubectl logs -n kube-system -l k8s-app=istio-cni
```

**Solutions:**
```bash
# Check istiod health
kubectl get pods -n istio-system -l app=istiod

# Restart istiod if needed
kubectl rollout restart deployment/istiod -n istio-system

# Check webhook configuration
kubectl get mutatingwebhookconfiguration -o yaml
```

## 8.2 Traffic Management Issues

### Service Not Reachable

**Symptoms:** `connection refused` or `no endpoints`

**Diagnosis:**
```bash
# Check endpoints
kubectl get endpoints <service-name>

# Check VirtualService
kubectl get virtualservice <name> -o yaml

# Check DestinationRule
kubectl get destinationrule <name> -o yaml

# Analyze Istio config
istioctl analyze --namespace <namespace>
```

**Solutions:**
```yaml
# Ensure subsets are defined in DestinationRule
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: myservice
spec:
  host: myservice
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
```

### Routing Not Working

**Symptoms:** Traffic goes to wrong version, weights ignored

**Diagnosis:**
```bash
# Check Envoy routes
istioctl proxy-config route <pod-name> -n <namespace>

# Check VirtualService
istioctl get virtualservice <name>

# Check for conflicts
istioctl analyze --namespace <namespace>
```

**Solutions:**
```bash
# Check for multiple VirtualServices for same host
istioctl get virtualservices --all-namespaces

# Ensure proper match conditions
# Check Host header matches
```

### Canary Deployment Failed

**Symptoms:** All traffic goes to one version, weight ignored

**Diagnosis:**
```bash
# Check VirtualService config
kubectl get virtualservice <name> -o yaml

# Check DestinationRule subsets
kubectl get destinationrule <name> -o yaml

# Verify pod labels
kubectl get pods -l version=v2
```

## 8.3 mTLS Issues

### mTLS Connection Failed

**Symptoms:** `connection reset` or TLS errors between services

**Diagnosis:**
```bash
# Check mTLS mode
kubectl get peerauthentication --all-namespaces

# Check destination rule TLS settings
istioctl proxy-config cluster <pod-name> -o json | grep tls

# Test connectivity
kubectl exec <pod> -n source -- curl -v https://<service>:8080
```

**Solutions:**
```yaml
# Check PeerAuthentication
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: <ns>
spec:
  mtls:
    mode: STRICT  # or PERMISSIVE

# Check DestinationRule traffic policy
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: myservice
spec:
  host: myservice
  trafficPolicy:
    tls:
      mode: MUTUAL
```

### Certificate Issues

**Symptoms:** `certificate verify failed`, expired certificates

**Diagnosis:**
```bash
# Check certificate expiration
istioctl proxy-config secret <pod> -o json | jq

# View workload certs
kubectl get secrets -n <namespace> -l istio.io/auto-own-cert=true

# Check istiod CA cert
kubectl get secret -n istio-system istio-ca-cert -o yaml
```

**Solutions:**
```bash
# Force cert rotation
kubectl delete secret -n <namespace> -l istio.io/auto-own-cert=true
kubectl delete pod <pod-name> -n <namespace>

# Check and rotate root CA
kubectl get secret -n istio-system cacerts -o yaml
```

## 8.4 Networking Issues

### Ingress Gateway Not Working

**Symptoms:** External traffic not reaching services

**Diagnosis:**
```bash
# Check gateway
kubectl get gateway <name> -o yaml

# Check ingress gateway pods
kubectl get pods -n istio-system -l istio=ingressgateway

# Check Envoy listener
istioctl proxy-config listener <ingress-pod> -n istio-system --type inbound

# Check logs
kubectl logs -n istio-system -l istio=ingressgateway --tail=50
```

**Solutions:**
```yaml
# Ensure Gateway is correct
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: mygateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - "example.com"
      tls:
        httpsRedirect: true
    - port:
        number: 443
        name: https
        protocol: HTTPS
      tls:
        mode: SIMPLE
        credentialName: my-tls-secret
      hosts:
        - "example.com"
```

### DNS Resolution Failed

**Symptoms:** `server misbehaving` or `no such host`

**Diagnosis:**
```bash
# Check ServiceEntry for external services
kubectl get serviceentry -A

# Check istiod config
istioctl get all -A

# Test DNS
kubectl exec -it <pod> -- nslookup <service>
```

**Solutions:**
```yaml
# Add ServiceEntry for external service
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: external-api
spec:
  hosts:
    - api.external.com
  location: MESH_EXTERNAL
  ports:
    - number: 443
      name: https
      protocol: HTTPS
  resolution: DNS
```

## 8.5 Observability Issues

### Missing Metrics

**Symptoms:** Grafana shows no data, Prometheus not scraping

**Diagnosis:**
```bash
# Check Prometheus scraping
istioctl proxy-config endpoint <pod> -n <namespace> | grep 15020

# Check ServiceMonitor
kubectl get servicemonitor -n istio-system

# Check Prometheus config
kubectl get configmap prometheus -n istio-system -o yaml
```

**Solutions:**
```bash
# Ensure pod has istio-proxy with prometheus port
kubectl get pod <pod> -o jsonpath='{.spec.containers[*].ports}'

# Check if scraping is enabled
istioctl dashboard prometheus
```

### Tracing Not Working

**Symptoms:** No traces in Jaeger

**Diagnosis:**
```bash
# Check tracing config
kubectl get istiooperator -n istio-system -o yaml

# Check sampling rate
istioctl get meshconfig -n istio-system

# Check tracing destination
kubectl get pods -n istio-system -l app=jaeger
```

**Solutions:**
```yaml
# Enable tracing in MeshConfig
apiVersion: v1
kind: ConfigMap
metadata:
  name: istio
  namespace: istio-system
data:
  mesh: |
    enableTracing: true
    defaultConfig:
      tracing:
        sampling: 10
        zipkin:
          address: jaeger-collector.observability:9411
```

## 8.6 Performance Issues

### High Memory Usage

**Symptoms:** OOM kills, high memory in sidecar

**Diagnosis:**
```bash
# Check resource usage
kubectl top pods -n <namespace>

# Check Envoy memory
istioctl proxy-config stats <pod> | grep memory
```

**Solutions:**
```yaml
# Limit sidecar resources
apiVersion: v1
kind: Pod
metadata:
  annotations:
    sidecar.istio.io/resources: '{"limits":{"memory":"512Mi"}}'
```

### Slow Responses

**Symptoms:** High latency, timeouts

**Diagnosis:**
```bash
# Check connection pool
istioctl proxy-config endpoint <pod> --endpoint <ip>

# Check circuit breaker
istioctl get destinationrule <name>

# Check retry policy
istioctl get virtualservice <name>
```

**Solutions:**
```yaml
# Tune connection pool
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: myservice
spec:
  host: myservice
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: UPGRADE
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
```