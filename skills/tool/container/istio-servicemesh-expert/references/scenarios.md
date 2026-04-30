# Scenario Examples

## 9.1 Service Mesh Deployment Scenarios

### Scenario: Progressive mTLS Rollout

**User:** "We want to enable mTLS across our cluster but are worried about breaking existing services. How do we do this safely?"

**Expert:**
> **Phased mTLS Implementation:**
>
> **Phase 1: Permissive Mode (Week 1)**
> ```yaml
> # Set entire mesh to permissive
> apiVersion: security.istio.io/v1beta1
> kind: MeshPeerAuthentication
> metadata:
>   name: default
>   namespace: istio-system
> spec:
>   mtls:
>     mode: PERMISSIVE
> ```
>
> **Phase 2: Monitor & Identify Issues (Week 2)**
> ```bash
> # Check which services are not using mTLS
> istioctl authz tls-check <pod-name> -n <namespace>
>
> # Review Kiali graph for mTLS status
> istioctl dashboard kiali
> # Look for services showing lock icon (mTLS enabled)
> ```
>
> **Phase 3: Namespace-by-Namespace STRICT (Week 3)**
> ```yaml
> # Enable STRICT for individual namespaces
> apiVersion: security.istio.io/v1beta1
> kind: PeerAuthentication
> metadata:
>   name: default
>   namespace: platform
> spec:
>   mtls:
>     mode: STRICT
> ```
>
> **Phase 4: Full STRICT (Week 4)**
> ```yaml
> # Remove permissive global policy, set STRICT default
> apiVersion: security.istio.io/v1beta1
> kind: MeshPeerAuthentication
> metadata:
>   name: default
> spec:
>   mtls:
>     mode: STRICT
> ```

### Scenario: Blue-Green Deployment with Istio

**User:** "How do I implement blue-green deployment for zero-downtime releases?"

**Expert:**
> **Blue-Green Deployment Pattern:**
>
> ```bash
> # 1. Deploy blue (current production)
> kubectl apply -f deployment-blue.yaml
> # Labels: app: payment-service, version: blue, env: production
>
> # 2. Deploy green (new version)
> kubectl apply -f deployment-green.yaml
> # Labels: app: payment-service, version: green, env: production
>
> # 3. Configure routing
> kubectl apply -f - <<EOF
> apiVersion: networking.istio.io/v1beta1
> kind: DestinationRule
> metadata:
>   name: payment-service
> spec:
>   host: payment-service
>   subsets:
>     - name: blue
>       labels:
>         version: blue
>     - name: green
>       labels:
>         version: green
> ---
> apiVersion: networking.istio.io/v1beta1
> kind: VirtualService
> metadata:
>   name: payment-service
> spec:
>   hosts:
>     - payment-service
>   http:
>     - route:
>         - destination:
>             host: payment-service
>             subset: blue
>           weight: 100
> ---
> apiVersion: networking.istio.io/v1beta1
> kind: EnvoyFilter
> metadata:
>   name: payment-service-cookie-sticky
> spec:
>   workloadSelector:
>     labels:
>       app: payment-service
>   httpCookies:
>     headerName: "x-payment-version"
>     cookieName: "payment_version"
>     ttl: 0
>     path: "/"
> ```
>
> **4. Route traffic to green**
> ```bash
> kubectl patch virtualservice payment-service -p '{
>   "spec":{"http":[{"route":[{"destination":{"subset":"blue"},"weight":80},
>                               {"destination":{"subset":"green"},"weight":20}]}]}
> }'
> ```
>
> **5. Full cutover after validation**
> ```bash
> kubectl patch virtualservice payment-service -p '{
>   "spec":{"http":[{"route":[{"destination":{"subset":"green"},"weight":100}]}]}
> }'
>
> # Keep blue running for rollback
> kubectl scale deployment payment-service-blue --replicas=0
> ```

## 9.2 Multi-Environment Setups

### Scenario: Dev/Staging/Production Isolation

**User:** "We have dev, staging, and prod clusters. How do we configure Istio for environment isolation?"

**Expert:**
> **Multi-Cluster Configuration:**
>
> **Shared Control Plane (Simple)**
> ```yaml
> # IstioOperator for each cluster
> # staging:
> apiVersion: install.istio.io/v1alpha1
> kind: IstioOperator
> metadata:
>   name: staging-istio
>   namespace: istio-system
> spec:
>   profile: default
>   meshConfig:
>     clusterName: staging-us-east
>     defaultConfig:
>       proxyMetadata:
>         ISTIO_META_DNS_CAPTURE: "true"
>         ISTIO_META_DNS_AUTO_ALLOCATE: "true"
>   values:
>     global:
>       meshID: shared-mesh
>       multiCluster:
>         clusterName: staging-us-east
> ```
>
> **Network Isolation**
> ```yaml
> # Gateway for staging
> apiVersion: networking.istio.io/v1beta1
> kind: Gateway
> metadata:
>   name: staging-gateway
>   namespace: istio-system
> spec:
>   selector:
>     istio: ingressgateway
>   servers:
>     - port:
>         number: 443
        name: https
        protocol: HTTPS
      hosts:
        - "*.staging.example.com"
      tls:
        mode: SIMPLE
        credentialName: staging-tls-cert
```
>
> **Service Discovery Across Clusters**
> ```yaml
> # ServiceEntry for cross-cluster service
> apiVersion: networking.istio.io/v1beta1
> kind: ServiceEntry
> metadata:
>   name: prod-api-access
> spec:
>   hosts:
>     - api.prod.svc.cluster.local
>   location: MESH_INTERNAL
>   resolution: DNS
>   ports:
>     - number: 80
>       name: http
      protocol: HTTP
  endpoints:
    - address: prod-gateway.istio-system.svc.cluster.local
      ports:
        http: 15443
```

### Scenario: Multi-Cluster Federation

**User:** "How do I configure cross-cluster traffic between US and EU clusters?"

**Expert:**
> **Multi-Primary Multi-Network Setup:**
>
> **US Cluster (Primary)**
> ```yaml
> apiVersion: install.istio.io/v1alpha1
> kind: IstioOperator
> metadata:
>   name: us-cluster
>   namespace: istio-system
> spec:
>   meshConfig:
>     clusterName: us-east-1
>     defaultConfig:
>       proxyMetadata:
>         ISTIO_META_DNS_CAPTURE: "true"
>   values:
>     global:
>       meshNetwork: us-east-network
>       network: us-east-network
>     pilot:
>       configSource:
>         certified:
>           dnsName: istiod.us-east.example.com
>           secretName: istiod-us-cert
> ```
>
> **Configure cross-cluster endpoints**
> ```yaml
> apiVersion: networking.istio.io/v1beta1
> kind: ServiceEntry
> metadata:
>   name: eu-services
> spec:
>   hosts:
>     - user-service.eu-east.svc.cluster.local
>   location: MESH_INTERNAL
>   resolution: DNS
>   ports:
>     - number: 80
>       name: http
      protocol: HTTP
  endpoints:
    - address: eu-west-gateway.example.com
      locality: eu-west
      ports:
        https: 15443
```

## 9.3 Disaster Recovery

### Scenario: Sidecar Failure Recovery

**User:** "One of our pods has a broken sidecar and traffic isn't reaching the application. How do we fix this?"

**Expert:**
> **Diagnosis and Recovery:**
>
> **1. Identify the Issue**
> ```bash
> # Check pod status
> kubectl describe pod <problem-pod>
>
> # Check Envoy status
> istioctl proxy-config bootstrap <problem-pod> -n <namespace>
>
> # View Envoy logs
> kubectl logs <problem-pod> -c istio-proxy --previous
>
> # Check for init container errors
> kubectl logs <problem-pod> -c istio-init --previous
> ```
>
> **2. Common Fixes**
> ```bash
> # Fix 1: Restart the sidecar
> kubectl exec <problem-pod> -n <namespace> -- curl -X POST localhost:15000/quitquitquit
> kubectl delete pod <problem-pod> -n <namespace>  # Will reschedule
>
> # Fix 2: Re-inject sidecar
> kubectl delete pod <problem-pod> -n <namespace>
>
> # Fix 3: Check injection webhook
> kubectl get mutatingwebhookconfiguration istio-sidecar-injector -o yaml
> ```
>
> **3. If Istio System is Broken**
> ```bash
> # Restart istiod
> kubectl rollout restart deployment istiod -n istio-system
>
> # Check for resource exhaustion
> kubectl top pods -n istio-system
>
> # View istiod logs
> kubectl logs -n istio-system -l app=istiod --tail=100
> ```

### Scenario: Network Partition Recovery

**User:** "After a network partition, some services can't talk to each other. What should we check?"

**Expert:**
> **Recovery Procedure:**
>
> **1. Check Endpoint Status**
> ```bash
> istioctl proxy-config endpoint <pod-name> -n <namespace>
>
> # Look for UNHEALTHY endpoints
> # Look for missing endpoints
> ```
>
> **2. Verify DestinationRules**
> ```bash
> kubectl get destinationrule -A
> istioctl proxy-config cluster <pod-name> -n <namespace> --verbose
> ```
>
> **3. Check for Conflicting VirtualServices**
> ```bash
> istioctl analyze --namespace <namespace>
>
> # Look for errors like:
> # - Multiple VirtualServices for same host
> # - Conflicting subsets
> ```
>
> **4. Force Endpoint Refresh**
> ```bash
> # Trigger EDS push by updating istiod
> kubectl rollout restart deployment istiod -n istio-system
>
> # Or restart pilot
> kubectl delete pod -n istio-system -l app=pilot
> ```
>
> **5. Network Policy Check**
> ```bash
> # Ensure CNI isn't blocking
> kubectl get networkpolicies -A
>
> # Temporarily disable NetworkPolicy for testing
> kubectl label namespace <namespace> network-policy=disabled --overwrite
> ```

### Scenario: Certificate Expiration Recovery

**User:** "mTLS stopped working after certificates expired. How do we renew them?"

**Expert:**
> **Certificate Renewal Process:**
>
> **1. Check Certificate Status**
> ```bash
> # Check Envoy certificate
> istioctl proxy-config secret <pod-name> -n <namespace> --show-types | grep cert
>
> # Check istiod managed certificates
> kubectl get secret -n istio-system -l istio.io/auto-own-cert=true
>
> # View certificate expiration
> kubectl get secret -n istio-system istio-ca-cert -o jsonpath='{.data[\"ca-cert\.pem\]}' | base64 -d | openssl x509 -noout -dates
> ```
>
> **2. Automatic Rotation (Istiod)**
> ```bash
> # Istiod automatically rotates workload certs
> # Check rotation config
> kubectl get cm istio -n istio-system -o yaml | grep CERT_TTL
> # Default: 24h workload cert TTL, 10m rotation interval
> ```
>
> **3. Manual Force Rotation**
> ```bash
> # Delete workload certs to trigger immediate rotation
> kubectl delete secret -n <namespace> -l istio.io/auto-own-cert=true
>
> # Restart pods to get new certs
> kubectl rollout restart deployment -n <namespace>
> ```
>
> **4. Root Certificate Rotation**
> ```bash
> # Rotate CA root certificate
> kubectl create secret generic cacerts -n istio-system \
>   --from-file=ca-cert.pem=/path/to/new-ca-cert.pem \
>   --from-file=ca-key.pem=/path/to/new-ca-key.pem \
>   --dry-run=client -o yaml | kubectl apply -f -
>
> # Restart istiod
> kubectl rollout restart deployment istiod -n istio-system
>
> # Restart all workloads
> kubectl rollout restart deployment -A
> ```
