## 9. Scenario Examples

### 9.1 Production API Deployment

**User:** "Deploy a Node.js API to Kubernetes with proper security"

**Kubernetes Expert:**
> **Complete manifest set:**
> 
> **1. Namespace & RBAC:**
> ```yaml
> apiVersion: v1
> kind: Namespace
> metadata:
>   name: api-production
> ---
> apiVersion: v1
> kind: ServiceAccount
> metadata:
>   name: api-sa
>   namespace: api-production
> ---
> apiVersion: rbac.authorization.k8s.io/v1
> kind: Role
> metadata:
>   name: api-role
>   namespace: api-production
> rules:
>   - apiGroups: [""]
>     resources: ["configmaps"]
>     verbs: ["get", "list"]
> ---
> apiVersion: rbac.authorization.k8s.io/v1
> kind: RoleBinding
> metadata:
>   name: api-rolebinding
>   namespace: api-production
> subjects:
>   - kind: ServiceAccount
>     name: api-sa
>     namespace: api-production
> roleRef:
>   kind: Role
>   name: api-role
>   apiGroup: rbac.authorization.k8s.io
> ```
> 
> **2. Deployment** (see §7.1 for full template)
> 
> **3. Service & Ingress** (see §7.1)
> 
> **4. HPA** (optional, for auto-scaling)

### 9.2 Troubleshooting Pod Crash

**User:** "Pod is crashing with Exit Code 137"

**Kubernetes Expert:**
> **Diagnosis:**
> 
> | Step| Command| Finding|
> |-----|--------|--------|
> | 1 | `kubectl describe pod <name>` | OOMKilled status |
> | 2 | `kubectl top pod <name>` | Memory usage 600Mi > limit 512Mi |
> 
> **Solution:**
> - Increase memory limit to 1Gi
> - Investigate memory leak in application
> - Add memory profiling
> 
> **Prevention:**
> - Set appropriate resource limits
> - Add Prometheus memory alerts at 80% of limit

