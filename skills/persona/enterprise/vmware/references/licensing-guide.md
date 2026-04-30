# VMware Licensing Guide (Post-Broadcom)

## Overview

Broadcom acquired VMware on November 22, 2023, for $69 billion. Major licensing changes were announced on December 11, 2023.

## Key Changes

### 1. End of Perpetual Licenses
- **Effective**: December 11, 2023
- **Impact**: No new perpetual license sales
- **Existing**: Perpetual licenses remain valid but no support without subscription transition

### 2. Product Consolidation
- **Before**: 8,000+ SKUs
- **After**: 4 main bundles
- **Bundles**: VCF, VVF, VVS, VSEP

### 3. Licensing Metric Change
- **Previous**: Per-CPU with 32-core entitlement
- **Current**: Per-core with 16-core minimum per CPU
- **Impact**: Higher costs for high-core-count processors

## Bundle Details

### VMware Cloud Foundation (VCF)
**Most Comprehensive Bundle**

| Component | Included |
|-----------|----------|
| vSphere Enterprise Plus | ✓ |
| vCenter Server Standard | ✓ |
| vSAN Enterprise | ✓ |
| NSX Enterprise Plus | ✓ |
| Tanzu Kubernetes Grid | ✓ |
| Aria Suite (Operations, Automation, Logs, Networks) | ✓ |
| HCX Enterprise | ✓ |
| Site Recovery Manager Enterprise | ✓ |

**Licensing**: Per-core subscription
**Minimum**: 16 cores per CPU
**Target**: Large enterprises, full SDDC

### VMware vSphere Foundation (VVF)
**Traditional Data Center Bundle**

| Component | Included |
|-----------|----------|
| vSphere Enterprise Plus | ✓ |
| vCenter Server Standard | ✓ |
| vSAN Enterprise | ✓ |
| Tanzu Kubernetes Grid | ✓ |
| Aria Operations (limited) | ✓ |

**Licensing**: Per-core subscription
**Target**: Mid-size enterprises, traditional virtualization

### VMware vSphere Standard (VVS)
**Entry-Level Bundle**

| Component | Included |
|-----------|----------|
| vSphere Standard | ✓ |
| vCenter Server | ✓ |

**Licensing**: Per-core subscription
**Target**: Small environments, basic virtualization

### VMware vSphere Enterprise Plus (VSEP)
**Premium Compute Bundle**

| Component | Included |
|-----------|----------|
| vSphere Enterprise Plus | ✓ |
| vCenter Server | ✓ |

**Licensing**: Per-core subscription
**Target**: Compute-intensive workloads

## Add-On Products

### Available Add-Ons
| Product | Metric | Description |
|---------|--------|-------------|
| vSAN | Per-TiB | Storage capacity |
| NSX | Per-core | Advanced networking |
| Tanzu Advanced | Per-core | Application platform |
| Site Recovery Manager | Per-VM | Disaster recovery |
| HCX | Per-VM | Migration |
| Private AI Foundation | Per-GPU | AI infrastructure |

## Cost Impact Analysis

### Scenario 1: Small Environment (4 hosts, 16 cores each)
**Before (Perpetual + SnS)**
- vSphere Enterprise Plus: ~$4,000 per CPU
- Support: ~$800/year per CPU
- Total (3-year): ~$38,400

**After (VCF Subscription)**
- 64 cores × $350/core/year = $22,400/year
- 3-year total: $67,200
- **Increase**: 75%

### Scenario 2: Large Environment (20 hosts, 64 cores each)
**Before**
- 40 CPUs × $4,000 = $160,000 perpetual
- 3-year SnS: $96,000
- Total: $256,000

**After**
- 1,280 cores × $350/core/year = $448,000/year
- 3-year total: $1,344,000
- **Increase**: 425%

## Support Changes

### Partner Program
- **Terminated**: All existing partner agreements
- **Reapplication**: Required for new agreements
- **Authorized Partners**: Limited to Broadcom-authorized distributors

### Support Model
- **Consolidation**: Support integrated into Broadcom systems
- **Response Times**: Reports of longer response times
- **Account Management**: High-touch for large customers only

## Migration Considerations

### From Perpetual to Subscription
1. **Assessment**: Current usage and future needs
2. **Negotiation**: Multi-year commitments may provide discounts
3. **Timing**: Align with support renewal dates
4. **Alternatives**: Evaluate Nutanix, Azure Stack HCI, OpenStack

### License Optimization
- **Rightsizing**: Review actual core utilization
- **Bundle Optimization**: Choose VVF over VCF if NSX not needed
- **Multi-Year Deals**: Potential 15-20% discount for 3-year commits

## Compliance

### Audit Requirements
- **Core Count**: Physical cores must be licensed
- **Minimum**: 16 cores per CPU socket regardless of actual count
- **Documentation**: Maintain deployment records

### True-Up Process
- **Annual**: License reconciliation
- **Overages**: Billed at list price
- **Underutilization**: No credits issued

## Alternatives Considerations

### Microsoft Hyper-V / Azure Stack HCI
- **Licensing**: Included with Windows Server/Azure
- **Cost**: Significantly lower for Microsoft shops
- **Migration**: Existing Microsoft tools and expertise

### Nutanix AHV
- **Licensing**: Capacity-based, simpler model
- **Cost**: Competitive, especially for HCI
- **Migration**: Professional services available

### Open Source (Proxmox, oVirt)
- **Licensing**: Free (support extra)
- **Cost**: Minimal licensing costs
- **Consideration**: Requires in-house expertise

## Recommendations

### For Existing Customers
1. **Negotiate**: Engage Broadcom early, leverage multi-year commitments
2. **Optimize**: Rightsize deployments, consider VVF over VCF
3. **Evaluate**: Assess alternatives before renewal
4. **Budget**: Plan for 200-400% cost increases

### For New Customers
1. **Start Small**: Begin with VVF, expand to VCF as needed
2. **Cloud**: Consider VCFaaS (VMware Cloud) to convert CapEx to OpEx
3. **Partners**: Work with authorized Broadcom partners
4. **Training**: Invest in team training for full bundle utilization
