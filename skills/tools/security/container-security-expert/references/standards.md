# Standards & Reference

## 7.1 Official Documentation

- [Docker Security Documentation](https://docs.docker.com/engine/security/)
- [Kubernetes Security Documentation](https://kubernetes.io/docs/concepts/security/)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [Trivy Documentation](https://aquasecurity.github.io/trivy/)
- [Clair Documentation](https://quay.github.io/clair/)
- [Snyk Container Docs](https://docs.snyk.io/products/snyk-container)
- [Sysbox Runtime Docs](https://github.com/nestybox/sysbox)
- [OWASP Container Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Container_Security_Cheat_Sheet.html)

## 7.2 Configuration Reference

### Dockerfile Security Best Practices

```dockerfile
# Use specific base image versions (not :latest)
FROM python:3.11-slim-bookworm

# Use non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
USER appuser

# Copy only necessary files
COPY --chown=appuser:appgroup ./app /app

# No secrets in image
# Use: docker secret or environment variables at runtime
# BAD: COPY secrets.json /app/

# Minimal layers
RUN apt-get update && \
    apt-get install -y --no-install-recommends package1 && \
    rm -rf /var/lib/apt/lists/*

# Multi-stage build for small final image
FROM golang:1.21 AS builder
WORKDIR /build
COPY . .
RUN go build -o app

FROM alpine:3.19
COPY --from=builder /build/app /usr/local/bin/
RUN adduser -D -u 10000 appuser
USER appuser
CMD ["app"]
```

### Docker Daemon Security Configuration

```json
{
  "icc": false,
  "userns-remap": "default",
  "seccomp-profile": "/etc/docker/seccomp.json",
  "no-new-privileges": true,
  "userland-proxy": false,
  "live-restore": true,
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "experimental": false,
  "features": {
    "buildkit": true
  }
}
```

### Container Runtime Security (containerd)

```yaml
# /etc/containerd/config.toml
[plugins."io.containerd.grpc.v1.cri"]
  sandbox_image = "registry.k8s.io/pause:3.9"
  enable_tls_streaming = false

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  runtime_type = "io.containerd.runc.v2"
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    BinaryName = "/usr/bin/runc"
    # Security options
    NoNewPrivileges = true
    Isolator = "oci.catct"

[plugins."io.containerd.grpc.v1.cri".security_context]
  allow_privileged = false
  read_only_rootfs = true
```

### Kubernetes Security Context

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 10000
    runAsGroup: 10000
    fsGroup: 10000
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
      requests:
        memory: "64Mi"
        cpu: "250m"
```

## 7.3 Common Commands

| Command | Description |
|---------|-------------|
| `docker scan <image>` | Scan image with Snyk (requires Docker Desktop or login) |
| `trivy image <image>` | Scan image with Trivy |
| `trivy fs /path` | Scan filesystem |
| `trivy k8s` | Scan Kubernetes cluster |
| `docker history <image>` | Show image layers |
| `docker inspect <container>` | Show container config |
| `docker diff <container>` | Show filesystem changes |
| `docker secret ls` | List secrets |

### Trivy Commands

```bash
# Scan image
trivy image nginx:1.21
trivy image --severity HIGH,CRITICAL myrepo/myapp:latest

# Scan filesystem
trivy fs /path/to/project
trivy fs --security-checks vuln,config /project

# Scan running containers
trivy container --help  # requires containerd

# Scan Kubernetes
trivy k8s --report summary cluster
trivy k8s --cluster-context kind-cluster

# Scan Helm charts
trivy helm https://charts.bitnami.com/bitnami

# Export results
trivy image --format json --output report.json myimage
trivy image --format sarif --output report.sarif myimage
trivy image --format table myimage  # default

# Cache management
trivy image --clear-cache
trivy db --download
```

### Docker Security Commands

```bash
# Check image contents
docker history myimage:latest
docker inspect myimage:latest

# Container runtime checks
docker run --rm -it --security-opt seccomp=profile.json myimage

# User namespace remapping
docker info | grep "Remapped"

# Capability checks
docker run --rm -it --cap-add=all myimage  # Too permissive
docker run --rm -it --cap-drop=all myimage # More secure

# Network isolation
docker network create isolated-net
docker run --network isolated-net myimage

# Resource limits
docker run --rm --memory=256m --cpus=0.5 myimage
```

## 7.4 Version Compatibility

| Tool | Version | Kubernetes | Containerd | Docker |
|------|---------|------------|------------|--------|
| Trivy | 0.50+ | 1.25+ | 1.6+ | 20.10+ |
| Clair | 4.8+ | 1.24+ | 1.5+ | 19.03+ |
| Snyk | Latest | 1.24+ | 1.6+ | 20.10+ |
| Dagda | Latest | 1.22+ | 1.5+ | 19.03+ |

### Vulnerability Database Compatibility

| Database | CVE Feed | Update Frequency |
|----------|----------|-----------------|
| Trivy | Alpine, Debian, Ubuntu, RHEL, Go, PHP, etc. | Hourly |
| Clair | Debian Security, Ubuntu CVE, RHEL, etc. | Varies |
| Grype | Multiple OS and language DBs | Daily |
| Snyk | Proprietary + NVD | Continuous |

## 7.5 Use Cases

| Use Case | Tool | Command | Purpose |
|----------|------|---------|---------|
| Image scanning in CI | Trivy | `trivy image --exit-code 1 myimage` | Block vulnerable images |
| Kubernetes cluster audit | Trivy | `trivy k8s cluster` | Find cluster vulnerabilities |
| Dockerfile analysis | Hadolint | `hadolint Dockerfile` | Lint Dockerfile security |
| Runtime monitoring | Falco | `falco` | Detect runtime anomalies |
| Supply chain security | Sigstore | `cosign verify` | Verify image signatures |
| Secrets scanning | Gitleaks | `gitleaks detect` | Find secrets in Dockerfile |
