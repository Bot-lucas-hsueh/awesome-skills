# Tanzu Reference Guide

## Tanzu Editions

### Tanzu Basic
- **Included in**: vSphere Enterprise Plus with Tanzu
- **Features**: TKG, Harbor registry
- **Use Case**: Kubernetes on vSphere

### Tanzu Standard
- **Includes**: Basic + Tanzu Mission Control
- **Features**: Multi-cluster management
- **Use Case**: Fleet management

### Tanzu Advanced
- **Includes**: Standard + TAP (Tanzu Application Platform)
- **Features**: Developer experience, supply chain
- **Use Case**: Platform engineering

## vSphere IaaS Control Plane (Supervisor)

### Architecture
```
vSphere Cluster with Supervisor Enabled
├── Supervisor Control Plane VMs (3 VMs)
│   ├── Kubernetes API Server
│   ├── etcd
│   └── Controller Manager
├── Supervisor Namespaces
│   ├── Network Policies
│   ├── Storage Policies
│   └── Resource Quotas
└── Tanzu Kubernetes Grid (TKG) Clusters
    └── Workload Clusters
```

### Requirements
- **vSphere**: 7.0+ (8.0+ recommended)
- **Licensing**: vSphere Enterprise Plus with Tanzu
- **Networking**: NSX or vSphere Distributed Switch (VDS)
- **Storage**: vSAN or VMFS/vVOLs

### VM Service
- **Purpose**: Run VMs alongside containers
- **Use Case**: Traditional apps in Kubernetes
- **API**: Kubernetes VM Operator

## Tanzu Kubernetes Grid (TKG)

### Management Cluster
- **Purpose**: Lifecycle management of workload clusters
- **Tools**: clusterctl, tanzu CLI
- **Provider**: Cluster API (CAPI)

### Workload Clusters
- **Deployment**: Declarative (YAML) or CLI
- **CNI**: Antrea (default), Calico
- **CSI**: vSphere CSI, Tanzu CSI

### TKG Architecture
```
Management Cluster
├── CAPI Controllers
│   ├── Cluster API
│   ├── Kubeadm Control Plane
│   └── Kubeadm Bootstrap
└── Infrastructure Providers
    ├── vSphere
    ├── AWS
    └── Azure

Workload Clusters (Created by Management Cluster)
├── Control Plane Nodes
├── Worker Nodes
└── Workload Applications
```

## Tanzu Application Platform (TAP)

### Supply Chain
```
Source → Build → Test → Scan → Deploy → Run
```

### Components
| Component | Purpose |
|-----------|---------|
| Cartographer | Supply chain choreography |
| Knative | Serverless platform |
| Cloud Native Runtimes | Knative serving |
| App Live View | Application monitoring |
| API Portal | API documentation |
| Learning Center | Tutorials and workshops |

### Supply Chain Types
- **Basic**: Source to URL
- **Testing**: Include testing stage
- **Scanning**: Include vulnerability scanning
- **Custom**: User-defined supply chains

## Tanzu Mission Control (TMC)

### Features
- **Cluster Management**: Attach any conformant Kubernetes
- **Policy Engine**: Access, network, security policies
- **Data Protection**: Velero-based backups
- **Observability**: Cluster health and metrics

### Policy Types
| Policy Type | Scope | Description |
|-------------|-------|-------------|
| Access Policy | Global/Cluster/Namespace | RBAC management |
| Network Policy | Cluster/Namespace | Pod-to-pod traffic |
| Security Policy | Cluster/Namespace | Pod security standards |
| Quota Policy | Namespace | Resource limits |
| Custom Policy | Any | OPA/Gatekeeper rules |

## Tanzu CLI

### Installation
```bash
# Install Tanzu CLI
curl -H "Accept: application/json" -H "Content-Type: application/json" \
  https://api.github.com/repos/vmware-tanzu/tanzu-framework/releases/latest

# Install plugins
tanzu plugin install kubernetes-release
tanzu plugin install management-cluster
tanzu plugin install cluster
tanzu plugin install package
```

### Common Commands

```bash
# Create management cluster
tanzu management-cluster create --ui

# Create workload cluster
tanzu cluster create production-cluster \
  --plan dev \
  --namespace default \
  --worker-machine-count 3

# List clusters
tanzu cluster list

# Get cluster kubeconfig
tanzu cluster kubeconfig get production-cluster --admin

# Delete cluster
tanzu cluster delete production-cluster

# Deploy package (TAP)
tanzu package install tap -p tap.tanzu.vmware.com -v 1.6.0 \
  --values-file tap-values.yaml \
  -n tap-install
```

## Tanzu Build Service (TBS)

### Purpose
- **Function**: Automated container image builds
- **Technology**: Cloud Native Buildpacks (CNB)
- **Benefits**: Reproducible builds, CVE patching

### Key Concepts
| Concept | Description |
|---------|-------------|
| Builder | Collection of buildpacks and stack |
| Stack | OS layers (build/run) |
| Buildpack | Build automation component |
| Image Resource | Configuration for automated builds |

## Kubernetes on vSphere (CSI/CPI)

### vSphere CSI (Container Storage Interface)
- **Features**: Dynamic provisioning, snapshots, expansion
- **Storage**: vSAN, VMFS, NFS, vVOLs
- **Access Modes**: RWO, RWX (vSAN File Services)

### vSphere CPI (Cloud Provider Interface)
- **Features**: Node discovery, load balancer (NSX)
- **Labels**: Zone/region topology
- **Integration**: vSphere HA/DRS awareness

### Storage Classes
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: vsan-default
provisioner: csi.vsphere.vmware.com
parameters:
  storagepolicyname: "vSAN Default Storage Policy"
  datastoreurl: "ds:///vmfs/volumes/vsan:52ed..."
```
