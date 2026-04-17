# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Scanning :latest tag only** | :red_circle: High | Miss vulnerabilities in older tags | Scan all tags, use SHA references |
| 2 | **Not updating vulnerability database** | :red_circle: High | False negatives | `trivy image --download-db-only` before scan |
| 3 | **Running containers as root** | :red_circle: High | Container escape risk | `RUN useradd`, `USER appuser` |
| 4 | **Using --privileged unnecessarily** | :red_circle: High | Full host access | Use specific capabilities |
| 5 | **Embedding secrets in images** | :red_circle: High | Secret exposure | Use secrets management, env vars at runtime |
| 6 | **Not scanning base images** | :yellow_circle: Medium | Unknown inherited vulns | Scan FROM image explicitly |
| 7 | **Ignoring OS packages vs apps** | :yellow_circle: Medium | Miss application vulns | Use `--security-checks vuln,config,secret` |
| 8 | **Scanning without --ignore-unfixed** | :yellow_circle: Medium | Noise for unpatched vulns | Filter based on fix availability |
| 9 | **Not setting scan thresholds in CI** | :yellow_circle: Medium | Security gates ineffective | `--exit-code 1 --severity CRITICAL` |
| 10 | **Skipping runtime security** | :yellow_circle: Medium | Only scanning at build time | Add Falco/runtime monitoring |

### Image Scanning Anti-Patterns

```markdown
:x: WRONG - Common scanning errors:

# Error 1: Not updating DB
trivy image myimage  # Using old cached DB
# Fix: trivy image --download-db-only

# Error 2: Only scanning :latest
trivy image myrepo/myapp
# Should also scan:
# trivy image myrepo/myapp:v1.2.3
# trivy image myrepo/myapp@sha256:abc...

# Error 3: Ignoring application vulns
trivy image --security-checks vuln myimage
# Should add:
# --security-checks vuln,config,secret

# Error 4: No fail threshold in CI
trivy image myimage  # Always exits 0
# Fix:
# trivy image --exit-code 1 --severity CRITICAL myimage

:white_check_mark: CORRECT:

# 1. Update DB
trivy image --download-db-only

# 2. Scan specific version
trivy image --input ./myimage.tar
trivy image myrepo/myapp:v1.2.3

# 3. Full security checks
trivy image --security-checks vuln,config,secret myimage

# 4. CI/CD blocking
trivy image \
  --exit-code 1 \
  --severity HIGH,CRITICAL \
  --ignore-unfixed \
  myimage
```

## 10.2 Anti-Patterns

### Dockerfile Security Anti-Patterns

| Anti-Pattern | Why Dangerous | Secure Alternative |
|-------------|---------------|---------------------|
| `USER root` at end | Container runs as root | `USER appuser` |
| `ADD . .` | Copies entire repo including secrets | `COPY requirements.txt .` then `COPY app app/` |
| `apt-get upgrade` | Large image, unpredictable | Pin base image versions |
| `:latest` tag | Unpredictable versions | `:1.21.0` specific version |
| `RUN pip install -r requirements.txt` | Unverified packages | Pin hashes: `pip install --require-hashes` |
| `EXPOSE 0-65535` | Over-exposed ports | Only expose needed ports |
| `--privileged` | Full host access | Specific capabilities only |
| Host network mode | No isolation | Default bridge or custom network |

### Runtime Anti-Patterns

```markdown
:x: WRONG - Dangerous container run options:

# Full host access
docker run --rm \
  --network host \
  --privileged \
  --pid=host \
  --ipc=host \
  myimage

# Dangerous volume mounts
docker run --rm \
  -v /:/host \
  -v /var/run/docker.sock:/var/run/docker.sock \
  myimage

# Running as root by default
docker run --rm myimage

:white_check_mark: CORRECT - Secure run options:

# Minimal capabilities
docker run --rm \
  --read-only \
  --no-new-privileges \
  --cap-drop=ALL \
  --security-opt=no-new-privileges:true \
  myimage

# Read-only filesystem
docker run --rm \
  --read-only \
  --tmpfs /tmp \
  myimage

# Non-root user
docker run --rm \
  --user 1000:1000 \
  myimage

# Resource limits
docker run --rm \
  --memory=256m \
  --cpus=0.5 \
  --pids-limit=100 \
  myimage

# Network isolation
docker run --rm \
  --network=none \
  myimage
```

### Kubernetes Anti-Patterns

```yaml
:x: WRONG - Insecure pod spec:

apiVersion: v1
kind: Pod
metadata:
  name: insecure-pod
spec:
  hostNetwork: true      # Danger: Host network
  hostPID: true          # Danger: Host PID namespace
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      privileged: true  # Danger: Privileged
      runAsUser: 0       # Danger: Running as root
    volumeMounts:
    - name: docker-socket
      mountPath: /var/run/docker.sock  # Danger
```

```yaml
:white_check_mark: CORRECT - Hardened pod spec:

apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 10000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
```

## 10.3 False Positive/Negative Management

### Reducing False Positives

```bash
# Ignore specific CVEs (if acceptable risk)
trivy image --ignorefile .trivyignore myimage

# .trivyignore format:
# CVE-2023-12345
# CVE-2023-*
# CVE-2023-12345 # Expired

# Filter by fix available
trivy image --ignore-unfixed myimage

# Exclude specific packages
trivy image --exclude-images "registry.example.com/internal/*" myimage

# Custom policy to suppress known-acceptable vulns
trivy image --policy ./policy.rego myimage
```

### Verification Checklist

```markdown
:clipboard: Before reporting container vulnerabilities:

1. Is the base image up-to-date?
   - Check FROM line, scan the base image
   
2. Is the vulnerable package actually used?
   - Some vulns only affect specific code paths
   
3. Is the vulnerability in a production path?
   - Test dependencies vs runtime dependencies
   
4. Is there a compensating control?
   - Network policies, WAF, runtime protection
   
5. Can the image be rebuilt?
   - Pin base image, rebuild with updated packages
   
6. Is it a dev-only dependency?
   - Multi-stage build to exclude from production
```

### Common False Positive Sources

| Source | Issue | Solution |
|--------|-------|----------|
| OS packages in multi-stage build | Build-only deps in final image | Use multi-stage builds |
| Development tools | Not needed in prod | Multi-stage or distroless |
| Test frameworks | Excluded from prod | Multi-stage builds |
| Debug symbols | Not needed | Strip in build |
| Outdated base image | Already fixed upstream | Pin and rebuild |

## 10.4 Legal & Compliance Issues

### Supply Chain Security Requirements

```markdown
:warning: Legal/Compliance considerations:

1. Open Source Licenses
   - Scan with FOSSA or similar
   - Track: GPL, LGPL, AGPL usage
   
2. Data Privacy
   - Don't scan images with PII
   - Use isolated scan environment
   
3. Regulatory Compliance
   - HIPAA: Audit trail for container access
   - PCI-DSS: Image signing, vulnerability management
   - SOC 2: Change management, monitoring
   
4. Export Controls
   - Some CVEs may have legal implications
   - Check OFAC/EAR requirements
```

### Compliance Audit Checklist

```markdown
:clipboard: Container Security Compliance:

- [ ] Images signed with Cosign/Syft
- [ ] SBOM generated and stored
- [ ] Vulnerability scan in CI/CD
- [ ] No secrets in images
- [ ] Non-root user in Dockerfile
- [ ] Read-only root filesystem
- [ ] No privileged containers
- [ ] Capability drops configured
- [ ] Network policies defined
- [ ] Resource limits set
- [ ] Audit logging enabled
- [ ] Runtime security monitoring
```

## 10.5 Performance & Scalability

| Issue | Cause | Solution |
|-------|-------|----------|
| Slow scan times | Large images, slow network | Use local cache, `--offline` |
| DB download timeout | Large vulnerability DB | Increase timeout, use mirror |
| Memory issues | Large Kubernetes cluster | Scan namespace by namespace |
| Registry rate limits | Too many scans | Use caching proxy |
| CI timeout | Full scan too long | Incremental scanning |

### Scaling Container Scanning

```bash
# Parallel image scanning
parallel trivy image {} ::: image1 image2 image3

# Use image cache for registries
# Harbor, Artifactory have built-in scanning

# Incremental scanning
# Only scan layers that changed
trivy image --cache-dir /path/to/cache myimage

# Lightweight scanning for large deployments
trivy image --security-checks vuln myimage
# Skip config/secret for speed
```
