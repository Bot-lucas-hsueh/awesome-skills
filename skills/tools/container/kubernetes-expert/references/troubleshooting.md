# Troubleshooting

## 8.1 Pod Failures

### Pod Stuck in Pending

**Symptoms:** Pod shows `Pending` status, not scheduling

**Diagnosis:**
```bash
kubectl describe pod <pod-name>
kubectl get events --sort-by='.lastTimestamp'
kubectl get nodes
```

**Common Causes:**

| Cause | Check | Solution |
|-------|-------|----------|
| No matching nodes | `kubectl get nodes` | Add nodes or adjust constraints |
| Insufficient resources | `kubectl describe node` | Free resources or add nodes |
| PVC not bound | `kubectl get pvc` | Check storage class |
| taints/tolerations | `kubectl describe node` | Add matching toleration |
| PDB blocking | `kubectl get pdb` | Allow disruption |

**Solutions:**
```bash
# Check why node can't be used
kubectl describe node <node-name> | grep -A10 "Taints"

# Check PVC status
kubectl get pvc <pvc-name> -o yaml

# Check storage class
kubectl get storageclass
```

### Pod Stuck in ContainerCreating

**Symptoms:** Pod stuck, no containers started

**Diagnosis:**
```bash
kubectl describe pod <pod-name>
kubectl get events --sort-by='.lastTimestamp'
```

**Common Causes:**

| Cause | Check | Solution |
|-------|-------|----------|
| Image pull failure | Events show "Failed to pull image" | Check image name, registry auth |
| CNI plugin error | Events show network errors | Check CNI configuration |
| Init container failed | Show in describe | Debug init container |
| Volume mount error | Show in events | Check PVC, configmap |

### Pod Crashing (CrashLoopBackOff)

**Symptoms:** Pod starts, then crashes, repeats

**Diagnosis:**
```bash
kubectl logs <pod-name> --previous
kubectl describe pod <pod-name>
```

**Common Causes:**

| Exit Code | Meaning | Debug |
|-----------|---------|-------|
| 1 | Application error | Check logs |
| 137 | OOMKilled | Increase memory limit |
| 139 | Segmentation fault | Application bug |
| 143 | SIGTERM (graceful) | Check termination |

**Solutions:**
```bash
# Increase memory limit
kubectl patch deployment <name> -p '{"spec":{"template":{"spec":{"containers":[{"name":"app","resources":{"limits":{"memory":"1Gi"}}}]}}}}'

# Debug application
kubectl exec -it <pod> -- /bin/sh
```

## 8.2 Networking Issues

### Service Not Reaching Pods

**Symptoms:** `Connection refused` or `No endpoints`

**Diagnosis:**
```bash
kubectl get endpoints <service-name>
kubectl get pods -l app=<selector>
kubectl describe service <service-name>
```

**Solutions:**
```bash
# Ensure selector matches pods
kubectl get pods --show-labels

# Check endpoint creation
kubectl get endpoints <service-name>

# Test connectivity
kubectl run test --rm -it --image=busybox --restart=Never -- sh
# wget <service-name>
```

### DNS Not Working

**Symptoms:** `server misbehaving`, `no such host`

**Diagnosis:**
```bash
kubectl exec -it <pod> -- nslookup <service>
kubectl exec -it <pod> -- cat /etc/resolv.conf
```

**Solutions:**
```yaml
# Check CoreDNS running
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
        }
        forward . /etc/resolv.conf
        cache 30
    }
```

### Pod Can't Reach External Services

**Symptoms:** `connection timeout`, `no route to host`

**Diagnosis:**
```bash
kubectl exec -it <pod> -- curl -v <external-ip>
kubectl get networkpolicy -A
```

**Solutions:**
```yaml
# Add egress network policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-egress
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
    - Egress
  egress:
    - to:
        - namespaceSelector: {}
    - to:
        - podSelector: {}
```

## 8.3 RBAC Issues

### Permission Denied

**Symptoms:** `Forbidden`, `Unauthorized` errors

**Diagnosis:**
```bash
kubectl auth can-i <verb> <resource> --as=<user>
kubectl describe role <role-name> -n <namespace>
kubectl describe rolebinding <name> -n <namespace>
```

**Solutions:**
```yaml
# Create role
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["pods", "services"]
    verbs: ["get", "list", "watch"]

# Bind role
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-reader-binding
  namespace: production
subjects:
  - kind: User
    name: john@example.com
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: app-reader
  apiGroup: rbac.authorization.k8s.io
```

### ServiceAccount Issues

**Symptoms:** Pod can't access API server

**Diagnosis:**
```bash
kubectl describe pod <pod> | grep "Service Account"
kubectl get serviceaccount <sa-name> -o yaml
```

**Solutions:**
```yaml
# Add service account to pod
spec:
  serviceAccountName: my-sa
  containers:
    - name: app
      image: myapp:latest
```

## 8.4 Resource Issues

### OOMKilled

**Symptoms:** Pod terminated with OOMKilled

**Diagnosis:**
```bash
kubectl describe pod <pod-name> | grep -A5 "Last State"
kubectl top pod <pod-name>
```

**Solutions:**
```yaml
# Increase memory limit
resources:
  requests:
    memory: "256Mi"
  limits:
    memory: "512Mi"
```

### CPU Throttling

**Symptoms:** High latency, throttling warnings

**Diagnosis:**
```bash
kubectl top pod <pod-name>
kubectl describe pod <pod-name> | grep -A10 "CPU"
```

**Solutions:**
```yaml
# Increase CPU limit
resources:
  requests:
    cpu: "100m"
  limits:
    cpu: "500m"
```

## 8.5 Scheduling Issues

### Pod Unschedulable

**Symptoms:** No nodes available

**Diagnosis:**
```bash
kubectl describe pod <pod-name>
kubectl get nodes
kubectl top nodes
```

**Solutions:**
```bash
# Add more nodes
# Or adjust resource requests
# Or remove taints
kubectl taint node <node> key:NoSchedule-
```

## 8.6 Volume Issues

### PVC Not Bound

**Symptoms:** PVC stuck in Pending

**Diagnosis:**
```bash
kubectl describe pvc <pvc-name>
kubectl get storageclass
```

**Solutions:**
```bash
# Check storage class exists
kubectl get storageclass

# Check provisioner
kubectl get pvc <pvc-name> -o jsonpath='{.spec.storageClassName}'
```