# vSAN Reference Guide

## vSAN Architecture

### Disk Groups (Original Storage Architecture - OSA)
- **Cache Tier**: 1 device per disk group (SSD/NVMe)
  - 70% read cache, 30% write cache
  - Minimum 10% of consumed capacity
- **Capacity Tier**: 1-7 devices per disk group (SSD/HDD)
- **Maximum**: 5 disk groups per host

### Express Storage Architecture (ESA) - vSAN 8.0+
- **Unified Tier**: No separate cache/capacity
- **Log-Structured File System**: Optimal for NVMe
- **RAID-5/6 Support**: Better space efficiency
- **Requirements**: All-flash, 10 Gbps+ networking

## Storage Policies

### Policy Rules
| Rule | Description | Options |
|------|-------------|---------|
| FTT | Failures to Tolerate | 0, 1, 2, 3 |
| FTM | Failure Tolerance Method | RAID-1, RAID-5, RAID-6 |
| Stripe Width | Number of stripes | 1-12 |
| IOPS Limit | Per-object IOPS limit | 0-2147483647 |
| Object Space Reservation | Thick/Thin provisioning | 0%, 100% |
| Deduplication | Space efficiency | Enabled/Disabled |
| Compression | Space efficiency | Enabled/Disabled |

### FTT Calculation
| FTT | RAID | Minimum Hosts | Capacity Overhead |
|-----|------|---------------|-------------------|
| 1 | RAID-1 (Mirroring) | 3 | 2x |
| 1 | RAID-5 (Erasure Coding) | 4 | 1.33x |
| 2 | RAID-1 (Mirroring) | 5 | 3x |
| 2 | RAID-6 (Erasure Coding) | 6 | 1.5x |
| 3 | RAID-1 (Mirroring) | 7 | 4x |

## vSAN Cluster Types

### Standard Cluster
- **Minimum**: 3 hosts
- **Maximum**: 64 hosts (vSAN 8.0)
- **Witness**: Not required

### 2-Node Cluster
- **Use Case**: ROBO (Remote Office/Branch Office)
- **Witness**: Required (virtual appliance)
- **Network**: Direct-connect or via switch

### Stretched Cluster
- **Sites**: 2 data sites + 1 witness site
- **Witness**: Required at third site
- **Read Locality**: Read from local site
- **RTO**: Near-zero (automated failover)

### vSAN Max
- **Architecture**: Disaggregated storage
- **Compute**: Separate from storage
- **Scale**: Up to 24 storage-only nodes

## Performance Optimization

### Networking
- **Speed**: Minimum 10 Gbps, recommended 25/100 Gbps
- **NIC Teaming**: LACP or static binding
- **Jumbo Frames**: MTU 9000 recommended
- **Multicast**: Required for vSAN 6.6 and earlier (unicast in 6.7+)

### Disk Group Design
```
Best Practices:
- Use same disk models across hosts
- Size cache at 10% of capacity (OSA)
- Use NVMe for cache in all-flash
- Keep disk group utilization < 80%
```

### Performance Metrics
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Latency | <5ms | >10ms |
| Congestion | 0 | >10 |
| Recovery IOPS | As fast as possible | - |
| Resync Latency | <20ms | >50ms |

## Maintenance & Monitoring

### vSAN Health Service
- **Categories**: Hardware compatibility, performance, capacity, network
- **Checks**: 50+ health checks
- **Remediation**: Guided remediation steps

### Maintenance Mode
| Option | Description | Use Case |
|--------|-------------|----------|
| Ensure accessibility | Maintain accessibility | Quick reboot |
| Evacuate all data | Full evacuation | Extended maintenance |
| No data evacuation | No action | Host decommission |

### Degraded Device Handling (DDH)
- **Detection**: SMART data, latency monitoring
- **Action**: Automatically evacuate data
- **Threshold**: Configurable latency threshold

## vSAN File Services
- **Protocols**: NFS v3, NFS v4.1, SMB v2.1, SMB v3
- **Containers**: CSI driver for Kubernetes
- **Snapshots**: File share snapshots

## vSAN Encryption
- **Algorithm**: AES-256-XTS
- **KMS**: KMIP 1.1 compliant
- **Key Hierarchy**: KEK (external) + DEK (internal)
- **Performance Impact**: <5% overhead (hardware acceleration)

## PowerCLI vSAN Commands

```powershell
# Get vSAN cluster info
Get-Cluster | Get-VsanClusterConfiguration

# Create vSAN storage policy
New-SpbmStoragePolicy -Name "vSAN-Gold" `
    -AnyOfRuleSets (New-SpbmRuleSet -Name "Gold-Rules" `
    -AllOfRules (New-SpbmRule -Capability (Get-SpbmCapability -Name "VSAN.hostFailuresToTolerate") -Value 1),
                (New-SpbmRule -Capability (Get-SpbmCapability -Name "VSAN.forceProvisioning") -Value $false))

# Check vSAN health
Get-VsanClusterConfiguration -Cluster (Get-Cluster "Production") | Get-VsanHealth

# Get vSAN capacity
Get-VsanDisk -Cluster (Get-Cluster "Production") | 
    Select Name, CapacityGB, UsedGB, FreeGB

# Enter maintenance mode
Get-VMHost "esxi01.local" | Set-VMHost -State Maintenance `
    -VsanDataMigrationMode EnsureAccessibility
```

## Capacity Planning

### Formula
```
Usable Capacity = Raw Capacity / FTT Overhead × Space Efficiency

Example (3-node, RAID-1, FTT=1):
- 3 hosts × 4 TB = 12 TB raw
- RAID-1 overhead = 2x
- Deduplication savings = 1.5x
- Usable = 12 TB / 2 × 1.5 = 9 TB
```

### Rebuild Capacity
- **Requirement**: 1 host worth of capacity
- **Recommendation**: Maintain 25-30% free space
- **Slack Space**: For rebuilds and growth
