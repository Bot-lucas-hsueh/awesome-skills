# Scenario Examples

## 9.1 CTF & Training Scenarios

### Container Security Lab Setup

**User:** "How do I practice container security?"

**Expert:**
> **Training Lab Setup:**
>
> **Docker Security Playground:**
> ```bash
> # Vulnerable container image
> git clone https://github.com/MyrtleSoftware/test-vuln-container.git
> cd test-vuln-container
> docker build -t vuln-app:latest .
>
> # Scan it with Trivy
> trivy image vuln-app:latest
>
> # Analyze layers
> docker history vuln-app:latest
> ```
>
> **Kubernetes Security Playground:**
> ```bash
> # Minikube with security plugins
> minikube start --kubernetes-version=v1.28.0 \
>   --extra-config=apiserver.enable-admission-plugins=\
>   PodSecurityPolicy,NamespaceLifecycle,LimitRanger
>
> # Deploy vulnerable workload
> kubectl apply -f vulnerable-app.yaml
>
> # Scan with Trivy
> trivy k8s cluster --report summary
> ```
>
> **Hands-on Resources:**
> - Katacoda Container Security courses
> - Play with Docker (playwithdocker.com)
> - Docker Security Playgrounds on GitHub

### Practice Exercises

**User:** "What should I practice?"

**Expert:**
> **Exercise Set:**
>
> **1. Image Scanning**
> ```bash
> # Find vulnerabilities in official images
> trivy image ubuntu:22.04
> trivy image python:3.11-slim
> trivy image node:18-alpine
> ```
>
> **2. Dockerfile Hardening**
> ```bash
> # Given this Dockerfile, find issues
> hadolint Dockerfile.broken
> # Fix all reported issues
> ```
>
> **3. Runtime Security**
> ```bash
> # Try breaking out of container
> docker run --rm -v /:/host myimage chroot /host
> docker run --rm --privileged myimage
> docker run --rm -v /var/run/docker.sock:/var/run/docker.sock myimage
> ```
>
> **4. Kubernetes Hardening**
> ```bash
> # Audit YAML against security policies
> kubectl apply --dry-run=server -f pod.yaml
> trivy k8s k8s://default/deployments/myapp
> ```

## 9.2 Bug Bounty & Pentest Workflows

### Container Attack Scenarios

**User:** "How do I assess container security in a pentest?"

**Expert:**
> **Container Penetration Test Workflow:**
>
> **Step 1: Image Discovery**
> ```bash
> # Find exposed container registries
> nmap -p 5000,443 10.0.0.0/24
>
> # Check for public Docker registries
> curl https://registry.example.com/v2/_catalog
> curl https://registry.example.com/v2/myapp/tags/list
> ```
>
> **Step 2: Image Pull & Analysis**
> ```bash
> # Pull if accessible
> docker pull registry.example.com/myapp:v1
>
> # Scan for vulnerabilities
> trivy image registry.example.com/myapp:v1
>
> # Analyze for secrets
> docker run --rm -v $(pwd):/workspace \
>    aquasec/trivy-config:latest /workspace
>
> # Check for malware
> trivy image --security-checks vuln,misconfig,secret myapp
> ```
>
> **Step 3: Runtime Container Testing**
> ```bash
> # If you have container access:
> docker ps
> docker exec -it container_id /bin/sh
>
> # Inside container - escape attempts
> # Try: mounting host filesystem
> cat /proc/1/cgroup
> ls -la /var/run/docker.sock 2>/dev/null
> ```
>
> **Step 4: Kubernetes Assessment**
> ```bash
> # Check RBAC
> kubectl auth can-i --list
> kubectl get secrets
>
> # Check pod security
> trivy k8s cluster
>
> # Network policies
> kubectl get networkpolicies -A
> ```

### Cloud Container Security Assessment

**User:** "How do I assess EKS/ECS/GKE security?"

**Expert:**
> **Cloud Container Assessment:**
>
> **AWS EKS:**
> ```bash
> # List clusters
> aws eks list-clusters --region us-east-1
>
> # Update kubeconfig
> aws eks update-kubeconfig --name my-cluster
>
> # Scan cluster
> trivy k8s --cluster-context my-cluster cluster
>
> # Check IAM roles attached to pods
> kubectl get pod -A -o json | jq '.items[].spec.serviceAccountName'
> ```
>
> **Google GKE:**
> ```bash
> # List clusters
> gcloud container clusters list
>
> # Get credentials
> gcloud container clusters get-credentials my-cluster
>
> # Scan
> trivy k8s cluster
> ```
>
> **Azure AKS:**
> ```bash
> # List clusters
> az aks list -o table
>
> # Get credentials
> az aks get-credentials --name my-cluster --resource-group my-rg
>
> # Scan
> trivy k8s cluster
> ```

## 9.3 Compliance Scanning

### PCI-DSS Container Requirements

**User:** "How do I meet PCI-DSS container security requirements?"

**Expert:**
> **PCI-DSS Container Security Checklist:**
>
> **Req 2.2.1: Minimal functionality**
> ```dockerfile
> # Use minimal base images
> FROM gcr.io/distroless/static:nonroot
> COPY --from=builder /app /app
> CMD ["/app"]
> ```
>
> **Req 2.2: Unique passwords**
> ```bash
> # Scan for default credentials
> trivy image --security-checks vuln,config myapp
> ```
>
> **Req 3.4: Encryption at rest**
> ```yaml
> # Kubernetes secret encryption
> apiVersion: apiserver.config.k8s.io/v1
> kind: EncryptionConfiguration
> resources:
>   - resources:
>     - secrets
>     providers:
>     - aescbc:
>         keys:
>         - name: key1
>           secret: <base64-encoded-key>
> ```
>
> **Req 6.3.3: Security patches**
> ```bash
> # Regular vulnerability scanning
> trivy image --severity HIGH,CRITICAL \
>     --exit-code 1 \
>     --ignore-unfixed \
>     myrepo/myimage
>
> # Block images older than 30 days
> trivy image --ignore-file .trivyignore \
>     myrepo/myimage
> ```
>
> **Compliance Report:**
> ```bash
> trivy image --compliance myapp \
>     --compliance-boundary pci-dss \
>     -f table
> ```

### CIS Docker Benchmark Compliance

```bash
# Run CIS benchmark checks manually
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
     aquasec/docker-bench-test

# Using Trivy for misconfiguration
trivy config --severity ERROR,DANGER,WARN \
    ./kubernetes/

# Specific CIS checks
# CIS 5.2: Containers should not run as root
docker run --rm --user 0 myimage  # Should fail audit

# CIS 5.9: Container's root filesystem should be read-only
docker run --rm --read-only myimage

# CIS 5.15: Privileged containers should not be used
docker run --rm --privileged myimage  # Should fail audit
```

### Kubernetes Security Audit (CIS Benchmarks)

```bash
# kube-bench for Kubernetes CIS compliance
kubectl apply -f job.yaml  # kube-bench job

# Or run directly
docker run --rm -v $(pwd):/root/.kube \
     aquasec/kube-bench:latest run

# Trivy Kubernetes scan
trivy k8s --report full cluster

# Check specific controls
trivy k8s k8s://kube-system/deployments
trivy k8s k8s://default/pods
```

### SOC 2 Container Controls

```markdown
| CC6.1 | Logical access controls |
| - Run containers as non-root
| - Use RBAC in Kubernetes
| - Implement network policies
|
| CC7.2 | System monitoring |
| - Enable audit logging
| - Monitor container runtime
| - Deploy Falco for runtime security
|
| CC7.4 | Change management |
| - Image signing (Cosign)
| - SBOM generation
| - CI/CD security gates
```

### Ongoing Compliance Monitoring

```bash
# Scheduled vulnerability scanning
trivy image --severity HIGH,CRITICAL \
    --exit-code 1 \
    --ignore-unfixed \
    --refresh \
    myrepo/myimage:latest

# Kubernetes drift detection
trivy k8s --report drift cluster

# Supply chain verification
cosign verify \
    --certificate-identity myrepo/myimage:latest \
    myrepo/myimage:latest

# Export for compliance reporting
trivy image -f json myimage > monthly_scan.json
trivy k8s cluster -f json > cluster_audit.json
```
