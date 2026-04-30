# Red Hat OpenShift Technical Reference

## Overview

Red Hat OpenShift is the leading enterprise Kubernetes platform, providing a consistent foundation for building, deploying, and managing applications across hybrid cloud, multi-cloud, and edge environments.

## Platform Architecture

```yaml
OpenShift Container Platform (OCP):
  Control Plane:
    Components:
      - API Server: Kubernetes API endpoint
      - etcd: Distributed configuration store
      - Controller Manager: Cluster state reconciliation
      - Scheduler: Pod placement decisions
      - OpenShift Controllers: Route, Build, Deployment controllers
    High Availability:
      - 3+ control plane nodes recommended
      - etcd quorum (majority for consensus)
      - Automated failover
  
  Worker Nodes:
    Container Runtime:
      - CRI-O (default, lightweight)
      - Containerd (alternative)
    Networking:
      - OVN-Kubernetes (default CNI)
      - OpenShift SDN (legacy)
      - Multus (multi-network)
    Storage:
      - CSI drivers for cloud storage
      - OpenShift Data Foundation (Ceph-based)
```

## Deployment Topologies

### On-Premise (IPI/UPI)

| Method | Description | Use Case |
|--------|-------------|----------|
| **IPI** (Installer-Provisioned Infrastructure) | Automated provisioning | VMware, Bare metal with Ironic |
| **UPI** (User-Provisioned Infrastructure) | Manual infrastructure | Restricted environments, custom networking |
| **Assisted Installer** | Web-based installation | Bare metal, edge deployments |

### Cloud Deployments

| Cloud | Integration | Special Features |
|-------|-------------|------------------|
| **AWS** | ROSA (Red Hat OpenShift on AWS) | Managed service, integrated billing |
| **Azure** | ARO (Azure Red Hat OpenShift) | Managed service, Azure AD integration |
| **GCP** | OpenShift Dedicated on GCP | Managed service, GCP networking |
| **IBM Cloud** | ROKS (Red Hat OpenShift on IBM Cloud) | IBM Cloud Paks integration |

### Edge Deployments

```yaml
OpenShift Edge:
  Single Node OpenShift (SNO):
    - Control plane + workers on single node
    - For edge, remote locations
    - 64GB RAM, 8 CPU minimum
    
  3-Node Compact Cluster:
    - Control plane + workers on 3 nodes
    - High availability at edge
    - 5G, manufacturing, retail use cases
    
  Remote Worker Nodes:
    - Control plane in cloud/datacenter
    - Workers at edge locations
    - Kubelet certificate rotation for intermittent connectivity
```

## Core Components

### Developer Experience

```yaml
Developer Tools:
  OpenShift Dev Spaces:
    - Cloud-based IDE (Eclipse Che)
    - Pre-configured development environments
    - Kubernetes-native
    
  Developer Hub:
    - Backstage-based portal
    - Software catalog
    - Templates and documentation
    
  Source-to-Image (S2I):
    - Automatic container builds from source
    - Builder images for common languages
    - Integrated with OpenShift Pipelines
    
  Helm:
    - Chart repository integration
    - Tiller-less Helm 3
```

### CI/CD

```yaml
OpenShift Pipelines (Tekton):
  - Kubernetes-native CI/CD
  - Tasks, Pipelines, Triggers
  - GitOps integration
  
OpenShift GitOps (ArgoCD):
  - Declarative continuous delivery
  - Application synchronization
  - Multi-cluster management
```

### Service Mesh

```yaml
OpenShift Service Mesh (Istio + Kiali + Jaeger):
  Traffic Management:
    - Routing rules
    - Canary deployments
    - Circuit breakers
    
  Observability:
    - Distributed tracing (Jaeger)
    - Service graph (Kiali)
    - Metrics (Prometheus/Grafana)
    
  Security:
    - mTLS between services
    - Authorization policies
    - Rate limiting
```

### Serverless

```yaml
OpenShift Serverless (Knative):
  Serving:
    - Scale-to-zero
    - Traffic splitting
    - Auto-scaling
    
  Eventing:
    - Event-driven architecture
    - Triggers and brokers
    - CloudEvents support
```

### Virtualization

```yaml
OpenShift Virtualization (KubeVirt):
  - Run VMs alongside containers
  - VM live migration
  - Import from VMware, RHV
  - Shared storage with containers
```

## Security Features

### Platform Security

```yaml
Security Controls:
  RBAC:
    - Role-based access control
    - ClusterRoles, Roles
    - ServiceAccounts
    
  Network Policies:
    - Namespace isolation
    - Egress/ingress rules
    - Default deny policies
    
  Security Context Constraints (SCC):
    - Pod security policies
    - Privileged, restricted, anyuid profiles
    
  Image Security:
    - Integrated image scanning (Clair/ACS)
    - Image signing and verification
    - Quay integration
```

### Compliance

| Standard | Certification | Notes |
|----------|---------------|-------|
| FIPS 140-2 | Validated | Cryptographic modules |
| DISA STIG | Certified | DoD deployments |
| Common Criteria | EAL4+ | Government use |
| PCI-DSS | Compliant | Payment processing |
| HIPAA | Compliant | Healthcare |

## Storage Options

```yaml
Storage Classes:
  CSI Drivers:
    - AWS EBS, Azure Disk, GCP PD
    - vSphere CSI
    - Ceph CSI (ODF)
    
  OpenShift Data Foundation (ODF):
    - Ceph-based storage
    - Block, file, object
    - Multi-cloud gateway
    
  Persistent Volumes:
    - RWO (ReadWriteOnce)
    - RWX (ReadWriteMany) - NFS, CephFS
    - ROX (ReadOnlyMany)
```

## Monitoring & Logging

```yaml
Observability Stack:
  Monitoring:
    - Prometheus (metrics collection)
    - Alertmanager (alerting)
    - Grafana (visualization)
    - Default dashboards for cluster health
    
  Logging:
    - Loki (log aggregation)
    - Vector collectors
    - Kibana/Grafana for visualization
    
  Tracing:
    - Jaeger (distributed tracing)
    - Tempo (alternative)
```

## Day 2 Operations

### Cluster Updates

```yaml
Over-the-Air Updates:
  Channels:
    - stable: Production-ready
    - fast: Latest features
    - candidate: Pre-release testing
    - eus: Extended update support (2-year window)
    
  Update Process:
    - CVO (Cluster Version Operator)
    - Canary node updates
    - Automatic rollback on failure
```

### Backup & Disaster Recovery

| Component | Tool | RTO/RPO |
|-----------|------|---------|
| etcd | etcdctl backup | Minutes |
| Applications | OADP (Velero) | Configurable |
| Persistent Data | Storage snapshots | Storage-dependent |

## Integration with IBM Technologies

### IBM Cloud Paks

| Cloud Pak | Purpose | OpenShift Integration |
|-----------|---------|----------------------|
| CP4D (Data) | Data and AI platform | Operator-based install |
| CP4I (Integration) | API, messaging, events | Certified containers |
| CP4A (Automation) | Business automation | Workflow operators |
| CP4S (Security) | Security platform | Threat detection |
| CP4WAIOps | AIOps | Observability integration |

### watsonx on OpenShift

```yaml
watsonx.ai on OpenShift:
  - Self-managed AI platform
  - GPU operator for NVIDIA/AMD
  - Data residency compliance
  - Multi-tenancy support
```

## Best Practices

### Cluster Design
- Size control plane for HA (3+ nodes)
- Separate infrastructure and worker nodes
- Use machine sets for auto-scaling
- Plan network CIDRs carefully

### Application Deployment
- Use DeploymentConfigs or Deployments
- Implement health checks (liveness/readiness)
- Configure resource requests/limits
- Use ConfigMaps and Secrets for configuration

### Security
- Enable audit logging
- Use least-privilege RBAC
- Implement network policies
- Regular security scans

---

*Source: Red Hat OpenShift Documentation, OpenShift Commons, IBM Cloud Paks Documentation*
