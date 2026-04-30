---
title: OpenShift 4.17 - 4.19 New Features
source: Red Hat OpenShift Documentation & Release Notes
last_updated: 2026-02-25
---

# OpenShift 4.17 - 4.19 New Features

## OpenShift 4.17 (Released 2025)

### Core Platform
- **Kubernetes 1.30** with CRI-O runtime
- **IPsec Encryption** for managed multi-node clusters with GitOps ZTP
- **Image-based Installation** for SNO clusters - reduces deployment time significantly
- **IBM Z & LinuxONE Support** - z/VM, LPAR, RHEL KVM installation options

### Networking Enhancements
- **UserDefinedNetwork (UDN)** - Technology Preview
  - Create multiple networks as primary/secondary
  - Namespace isolation without complex network policies
- **NIC Partitioning for SR-IOV** - Generally Available
- **SR-IOV VF Network Updates** - Update host network settings in existing clusters (GA)
- **Kubernetes NMState Operator** on Azure (limited support)
- **PTP Fast Events API v2** - O-RAN Release 3 compliant REST API

### Developer Experience
- OpenShift Dev Spaces enhancements
- Pipelines (Tekton) improvements
- GitOps (ArgoCD) updates

## OpenShift 4.18

### Platform Improvements
- Enhanced stability and performance
- Updated Kubernetes base
- Improved operator lifecycle management

## OpenShift 4.19 (Latest - 2025)

### Core Features

#### Gateway API - Generally Available
- Kubernetes' next-generation service networking standard
- Installed side-by-side with HAProxy
- OpenShift Ingress operator manages Gateway API via OSSM
- Out-of-the-box DNS and LB support
- Service Mesh not required for Gateway API

**API Analogs:**
| Istio Concept | OpenShift Equivalent |
|--------------|---------------------|
| Envoy | HAProxy |
| Gateway | IngressController |
| HTTPRoute | Route |

#### BGP Support in OVN-Kubernetes (GA)
- Cluster Admin privileged Primary UDN advertisements
- Import/Export routes enabled independently
- BFD (Bidirectional Forwarding Detection) support
- Expose pod networks directly in provider network
- EgressIP supports L3 topology for node network
- VRF-Lite extends UDN tenant isolation

**Roadmap:**
- No-overlay support
- EVPN support

#### OpenShift Lightspeed - Generally Available
- Generative AI-based chat assistant
- Operator install with Chat UI in OCP console
- Interactive OpenShift documentation/help
- Attach feature to explain pod YAML, debug logs, and alerts
- **Supported LLMs:** Watsonx, Azure AI, OpenAI, OpenShift AI, RHEL AI
- Disconnected deployment supported
- **Tech Preview Features:**
  - Cluster-interaction
  - BYO knowledge

### Virtualization

- **Storage Class Migration** - Move VMs between storage classes
- **OpenShift Virtualization on ARO** - Public Preview
- **OpenShift Virtualization on OSD** - Public Preview
- **Simplified Installer** for OpenShift Virtualization Engine
- **OpenShift Virtualization Hardening Guide**

### Security

- **Cert-manager** support for routes certificates
- **Confidential Nodes on Google Cloud** - Intel TDX and AMD SEV-SNP
- **Confidential Nodes on Azure** - AMD SEV-SNP
- **Confidential Containers for IBM Z** via IBM Hyper Protect Services

### Platform Plus (RHACS & RHACM)

#### RHACS 4.8
- Policy as code
- Compliance scanning
- External IPs support

#### RHACM 2.14
- On-demand from AWS Marketplace
- Regional DR support for multiple ODF storage classes
- Right-sizing recommendations at namespace & cluster level (Tech Preview)

### Observability & Monitoring

#### OpenShift Monitoring (4.19)
- **Prometheus 3.x** integration
- Promoted scrape profiles to GA
- Configuring external Alertmanagers with proxy_url

**Updated Components:**
| Component | Version |
|-----------|---------|
| Alertmanager | 0.28.1 |
| Prometheus Operator | 0.81.0 |
| Prometheus | 3.2.1 |
| kube-state-metrics | 2.15.0 |
| node-exporter | 1.9.1 |
| Thanos | 0.37.2 |

#### Cluster Observability Operator (COO) 1.2
- **Accelerators Dashboard** - GPU/AI accelerator visibility
- **Traces UI GA** - Scatter Plot, Trace Table, Gantt Chart
- **Advanced Traces Filtering**
- **Logging UI** - OTEL Support
- **Incident Detection** (Tech Preview) - Groups related alerts
- **Signal Correlation** (Tech Preview) - Root cause analysis

#### OpenShift Logging 6.3
- Expanded Splunk metadata keys
- Multiple CloudWatch outputs with STS authentication
- Loki virtual host style configuration
- Resource limits (Tech Preview)

#### Power Monitoring 0.5 (Tech Preview)
- Kepler 0.10.0 with modular design
- Supports OCP 4.17 - 4.19
- Bare-metal support for Node, Pods, Containers, VMs, Process

### AI Accelerator Ecosystem

#### NVIDIA Support
- **Blackwell GPU Support** - B200, RTX PRO 6000 Blackwell Server Edition
- **GPU Operator 25.3.0** for OpenShift 4.19
- **DGX H200 and DGX B200** certified
- **Multi-node, Multi-GPU** - Documented GPUDirect RDMA configuration

#### AMD Support
- **MI325X GPU** support with OpenShift
- **GPU Health Monitoring** - Real-time checks via metrics exporter
- Automatic removal of unhealthy GPUs from schedulable resources

#### Unified Dashboard
- AI accelerator telemetry dashboard in OpenShift web console
- Visibility into GPU/AI accelerator performance and power usage

### Service Mesh 3.1 (Coming Soon)

- Based on Istio 1.26 and Kiali 2.11
- End-to-end Kubernetes Gateway API support (OCP 4.19+)
- **Istio Ambient Mode** - Technology Preview
  - No sidecars required
  - Significantly less resource usage
  - ZTunnel for lightweight pod-to-pod mTLS
  - Independently scalable Waypoints for L7 features

### GitOps (ArgoCD)

#### OpenShift GitOps 1.17
- Argo CD 3.0 and Argo Rollouts 1.8.0
- Argo CD Agent Tech Preview
- Argo Rollouts in OpenShift Console
- JSON logging for all components (RFE-4607)

#### Multi-cluster GitOps with Argo CD Agent (Tech Preview)
- One-way communication Agent -> Control plane
- Reduced footprint for hub and spoke clusters
- Resilient and flexible network connectivity

### Builds & Pipelines

- OpenShift Pipelines (Tekton) updates
- OpenShift Builds enhancements

### Developer Tools

#### OpenShift Toolkit for VS Code 1.19.0
- OpenShift Pipeline Tasks in Cluster View
- Multiple K8s configuration files support in KUBECONFIG
- IntelliJ OpenShift support discontinued

#### Quarkus Tools 1.21.0
- Qute language server performance improvements
- Integer operators support in Qute files

### Azure Red Hat OpenShift (ARO) Updates

#### June 2025 - Version 4.17
- OpenShift 4.17 available as install option
- US Gov Arizona region live

#### May 2025
- **OpenShift Virtualization** - Public Preview on ARO

#### April 2025
- **Managed Identity** - Public Preview
  - Short-term, limited privilege credentials
  - Replace long-lived credentials

#### March 2025 - Version 4.16
- OpenShift 4.16 GA
- Cluster-wide proxy support
- SDN to OVN-Kubernetes migration guidance

#### Extended Update Support (EUS)
- All even minor versions from 4.16+ support EUS Term 1

#### Global Expansion
- Spain Central (Jan 2025)
- UAE Central (Q2 2025)
- US Gov Texas (Q2 2025)

## ROSA (Red Hat OpenShift on AWS)

- OpenShift 4.17 support
- Extended Update Support Add-On available
- Prometheus data persistence enabled
