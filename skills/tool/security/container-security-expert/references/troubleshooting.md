# Troubleshooting Guide

## 8.1 Image Scanning

### No Vulnerabilities Found

**Problem:** Trivy scan returns no vulnerabilities but you expected to find some.

**Diagnosis:**
```bash
# Check if vulnerability database is current
trivy image --download-db-only

# Verify image was actually scanned
trivy image --security-checks vuln,config,secret myimage

# Check DB version
trivy db --download
trivy image --vuln-type os myimage
```

**Fix:**
- Run `trivy image --download-db-only` before scanning
- Use `--security-checks vuln,config,secret` for full scan
- Update Trivy to latest version

### False Positives

**Problem:** Trivy reports vulnerabilities that don't apply.

**Fix:**
```bash
# Create .trivyignore file
cat > .trivyignore << EOF
CVE-2023-12345
CVE-2023-*
EOF

# Run with ignore file
trivy image --ignorefile .trivyignore myimage

# Filter by fixable only
trivy image --fixed myimage
```

## 8.2 Registry Issues

### Authentication Failed

**Problem:** Cannot pull images from private registry.

**Diagnosis:**
```bash
# Test registry connectivity
curl https://registry.example.com/v2/

# Check Docker login
docker login registry.example.com

# Test with full image path
docker pull registry.example.com/project/myimage:tag
```

**Fix:**
- Configure Docker credentials: `docker login registry.example.com`
- Use `--registry-auth-tlscontext` for TLS issues
- Check IAM/permissions for cloud registries (ECR, GCR, ACR)

### Rate Limiting

**Problem:** Registry returns 429 Too Many Requests.

**Fix:**
```bash
# Use caching proxy
# For Docker Hub: upgrade to paid plan or use mirror

# Cache images locally
docker pull myimage
docker save myimage > myimage.tar
```

## 8.3 Runtime Security

### Alerts Not Firing (Falco)

**Problem:** Falco running but not detecting events.

**Diagnosis:**
```bash
# Check Falco status
falco

# Check Falco logs
journalctl -u falco -f

# Verify rules loaded
falco --list-rules

# Test rule manually
falco -r /path/to/rules.yaml
```

**Fix:**
- Ensure Falco kernel module is loaded: `lsmod | grep falco`
- Check rule syntax: `falco -r /etc/falco/falco_rules.yaml`
- Verify event generation: enable debug logging

### Container Escape Detection

**Problem:** Need to detect container escape attempts.

**Fix:**
```yaml
# falco_rules.yaml
- rule: Container Escape Attempt
  desc: Detect container escape attempts
  condition: >
    evt.type = execve and 
    (container.id != host) and 
    (proc.name = "chroot" or 
     proc.name = "nsenter" or 
     proc.name = "unshare")
  output: "Container escape attempt detected"
  priority: CRITICAL
```

## 8.4 Kubernetes Issues

### Admission Controller Blocking Deployments

**Problem:** Valid pods being rejected by admission controller.

**Diagnosis:**
```bash
# Check admission controller logs
kubectl logs -n kube-system <admission-pod>

# Test manually
kubectl apply -f pod.yaml --dry-run=server

# Check validation webhooks
kubectl get validatingwebhookconfigurations
```

**Fix:**
- Update policy to allow specific configurations
- Use `kubectl explain` to understand required fields
- Temporarily disable webhook for testing

### Trivy K8s Scan Errors

**Problem:** Trivy Kubernetes scan fails.

**Fix:**
```bash
# Install proper kubeconfig
export KUBECONFIG=/path/to/config

# Scan specific cluster context
trivy k8s --cluster-context kind-mycluster cluster

# Scan specific namespace
trivy k8s --namespace default cluster
```

## 8.5 CI/CD Integration

### Exit Codes

**Problem:** Pipeline failing unexpectedly.

**Fix:**
```bash
# Understand exit codes
# 0 = success, vulnerabilities found
# 1 = failure, no vulnerabilities or error
# 10 = vulnerabilities found (with --exit-code 1)
# 11 = error + vulnerabilities found

# Use proper flags
trivy image --exit-code 1 --severity HIGH,CRITICAL myimage
```

### Cache Issues

**Problem:** Scans taking too long.

**Fix:**
```bash
# Use cache
trivy image --cache-dir /path/to/cache myimage

# Download DB once, use offline
trivy image --download-db-only
trivy image --offline myimage
```
