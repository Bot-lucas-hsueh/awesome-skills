# Standard Workflow

## 8.1 Reconnaissance & Enumeration Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: Image Inventory & Discovery                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 1. List all images in registry/cluster                           │
│    docker images                                               │
│    crane ls gcr.io/project                                      │
│    trivy image --download-db-only                              │
│                                                                  │
│ 2. Identify running containers                                  │
│    docker ps -a                                                │
│    kubectl get pods -A                                         │
│    crictl ps -a                                                │
│                                                                  │
│ 3. Image layer analysis                                         │
│    docker history myimage:latest                               │
│    docker inspect myimage:latest                               │
│                                                                  │
│ 4. Build SBOM for each image                                   │
│    syft myimage:latest -o json > sbom.json                    │
│    syft myimage:latest -o cyclonedx                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: Vulnerability Scanning                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 1. Scan all images (or use cache)                              │
│    trivy image --input images.tar                             │
│    # or                                                         │
│    trivy image myrepo/myimage:tag                             │
│                                                                  │
│ 2. Filter by severity                                          │
│    trivy image --severity HIGH,CRITICAL myimage               │
│    trivy image --ignore-unfixed myimage                        │
│                                                                  │
│ 3. Generate reports                                            │
│    trivy image -f json -o report.json myimage                  │
│    trivy image -f sarif -o report.sarif myimage               │
│                                                                  │
│ 4. Check for specific CVEs                                     │
│    trivy image --vuln-prefix CVE-2024 myimage                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: Runtime Security Assessment                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 1. Review container configs                                     │
│    kubectl get pods -A -o yaml | trivy k8s                     │
│    docker inspect $(docker ps -q)                             │
│                                                                  │
│ 2. Check capabilities                                          │
│    docker run --rm --cap-add=all myimage cat /proc/self/status │
│                                                                  │
│ 3. Network policies review                                     │
│    kubectl get networkpolicies -A                               │
│    kubectl describe networkpolicy my-np                        │
│                                                                  │
│ 4. RBAC audit                                                   │
│    kubectl auth can-i --list                                   │
│    kubectl get rolebindings -A --as=serviceaccount            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Container Registry Scanning

```bash
# AWS ECR
aws ecr describe-repositories
aws ecr list-images --repository-name myrepo
trivy image --input <(docker save myrepo/myimage:tag)

# GCR (Google Container Registry)
gcloud container images list
gcloud container images list-tags gcr.io/project/myimage
trivy image gcr.io/project/myimage:tag

# Docker Hub
docker search myrepo/myimage
trivy image myrepo/myimage:tag

# Harbor
curl -k https://harbor/api/v2.0/projects
trivy image harbor.example.com/myproject/myimage:tag
```

## 8.2 Scanning Methodology

### CI/CD Pipeline Integration

```
┌─────────────────────────────────────────────────────────────────┐
│ BUILD-TIME SCANNING                                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ Dockerfile Lint:                                                 │
│ hadolint Dockerfile                                             │
│                                                              │
│ Build Secret Scan:                                              │
│ docker run --rm -v $(pwd):/workspace sonatype-taint /workspace │
│                                                              │
│ SBOM Generation:                                               │
│ syft myimage:latest -o cyclonedx > sbom.json                  │
│                                                              │
│ Vulnerability Scan (block on HIGH/CRIT):                       │
│ trivy image --exit-code 1 --severity HIGH,CRITICAL myimage    │
│                                                              │
│ Signature Verification:                                        │
│ cosign verify --certificate-identity myimage                   │
│                                                              │
└─────────────────────────────────────────────────────────────────┘
```

### Trivy Scan Workflow

```bash
# 1. Initial full scan (all severities)
trivy image --severity UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL \
     --ignore-unfixed \
     --output scan_results.json \
     myrepo/myimage:1.0.0

# 2. Security-only scan (ignore low)
trivy image --severity HIGH,CRITICAL \
     --ignore-unfixed \
     --exit-code 1 \
     myrepo/myimage:1.0.0

# 3. Scan with policy (blockfile)
trivy image --policy ./policy.rego \
     --severity HIGH,CRITICAL \
     myrepo/myimage:1.0.0

# 4. Compare images
trivy image --input old_image.tar
trivy image --input new_image.tar
# Compare differences manually

# 5. Continuous monitoring
trivy image --refresh myrepo/myimage:latest
```

### Kubernetes Cluster Scanning

```bash
# Cluster-wide scan
trivy k8s --report summary cluster

# Specific namespace
trivy k8s --namespace production --report summary cluster

# Individual resource types
trivy k8s k8s://default/deployments/myapp
trivy k8s k8s://kube-system/configmaps/kube-proxy

# RBAC scan
trivy k8s --components rbac cluster

# Export cluster report
trivy k8s cluster --format json --output cluster_report.json
```

## 8.3 Reporting Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ REPORTING & COMPLIANCE                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ SCAN EXPORT FORMATS:                                             │
│                                                                  │
│ JSON - for automation and parsing                               │
│   trivy image -f json myimage > report.json                    │
│                                                                  │
│ SARIF - for GitHub/GitLab integration                           │
│   trivy image -f sarif myimage > report.sarif                  │
│                                                                  │
│ HTML - for human review                                         │
│   trivy image -f html myimage > report.html                    │
│                                                                  │
│ TABLE - for CLI output (default)                                │
│   trivy image myimage                                           │
│                                                                  │
│ COMPLIANCE REPORTS:                                              │
│   trivy image --compliance myimage \                           │
│       --format table \                                          │
│       --show-suppressed \                                       │
│       myimage                                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Integration with Issue Trackers

```bash
# Generate CSV for import
trivy image -f json myimage | \
  jq -r '.Results[].Vulnerabilities[] |
         "\(.PkgName),\(.InstalledVersion),\(.FixedVersion),\(.Severity),\(.CVSS)"' \
  > vulns.csv

# JIRA ticket creation (via API)
#!/bin/bash
VULNS=$(trivy image -f json myimage | jq '.Results[].Vulnerabilities | length')
if [ "$VULNS" -gt 0 ]; then
  curl -X POST "$JIRA_URL" \
    -d "{\"summary\": \"Critical vulnerabilities in $IMAGE\"}"
fi

# GitHub Issues integration
trivy image -f sarif myimage | \
  gh issue create --title "Fix vulnerabilities" --body-file -
```

### SBOM Workflow

```bash
# Generate SBOM
syft myimage:latest -o json > myimage.sbom.json

# Sign SBOM
cosign attest --predicate myimage.sbom.json myimage:latest

# Verify SBOM
syft myimage:latest -o json | \
  cosign verify-blob \
    --certificate-identity myimage:latest \
    --certificate-oidc-issuer https://github.com \
    myimage:latest

# Export to SPDX
syft myimage:latest -o spdx-json > myimage.spdx

# Export to CycloneDX
syft myimage:latest -o cyclonedx-json > myimage.cdx
```
