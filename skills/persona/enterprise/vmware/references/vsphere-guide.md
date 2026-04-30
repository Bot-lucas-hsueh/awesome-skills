# vSphere Reference Guide

## vSphere Architecture Components

### ESXi Hypervisor
- **Type**: Type 1 (bare-metal) hypervisor
- **Footprint**: ~150MB footprint, minimal attack surface
- **Management**: DCUI (Direct Console User Interface), SSH, ESXi Shell
- **API**: vSphere API (SOAP/REST)

### vCenter Server Appliance (VCSA)
- **Deployment**: Appliance-based (Photon OS)
- **Database**: Embedded PostgreSQL (vPostgres)
- **Services**: 
  - vCenter Server
  - Platform Services Controller (SSO, Licensing, Certificate Authority)
  - Update Manager
  - Auto Deploy

## Cluster Features

### vSphere High Availability (HA)
- **Heartbeat**: Network (default) + Datastore heartbeating
- **Admission Control**: 
  - Slot policy (default)
  - Cluster resource percentage
  - Dedicated failover hosts
- **Restart Priority**: Lowest → Low → Medium → High → Highest
- **VM Monitoring**: Application monitoring via VM Tools

### vSphere Distributed Resource Scheduler (DRS)
- **Automation Levels**: Manual → Partially Automated → Fully Automated
- **Migration Threshold**: 1 (Conservative) to 5 (Aggressive)
- **Predictive DRS**: Integration with vRealize Operations
- **VM Overrides**: Per-VM DRS automation levels

### vSphere vMotion
- **Requirements**: Shared storage (or vMotion without Shared Storage), VMkernel port
- **Network**: Minimum 1 Gbps, recommended 10 Gbps+
- **MTU**: 1500 (standard) or 9000 (jumbo frames)
- **Encryption**: Encrypted vMotion (AES-256-GCM)

## Resource Management

### Resource Pools
- **Shares**: Low (2000), Normal (4000), High (8000), Custom
- **Reservations**: Guaranteed minimum resources
- **Limits**: Maximum resource ceiling
- **Expandable Reservation**: Child can borrow from parent

### Storage I/O Control (SIOC)
- **Congestion Threshold**: Default 30ms latency
- **Shares**: Per-VMDK I/O priority
- **Limit IOPS**: Per-VMDK I/O throttling

### Network I/O Control (NIOC)
- **Resource Pools**: vMotion, iSCSI, NFS, FT, Management, Virtual machine
- **Shares**: Bandwidth allocation priority
- **Limits**: Bandwidth caps per traffic type

## Virtual Hardware

### Virtual Hardware Versions
| Version | vSphere | Features |
|---------|---------|----------|
| 19 | 7.0 U2 | vSGX, Precision Clock |
| 20 | 8.0 | NVMe 1.4, vGPU enhancements |
| 21 | 8.0 U2 | DPU support, vVols 2.0 |
| 22 | 9.0 | Next-gen features |

### VM Limits (vSphere 8.0)
- **vCPUs per VM**: 768
- **Memory per VM**: 24 TB
- **VM Disk Size**: 62 TB (VMDK)
- **vNICs per VM**: 10

## Security Features

### TPM 2.0 & Virtualization-based Security
- **vTPM**: Virtual Trusted Platform Module
- **VBS**: Virtualization-based Security (Windows)
- **Credential Guard**: Protected credential storage

### VM Encryption
- **vSphere VM Encryption**: AES-256-XTS
- **KMS Integration**: KMIP 1.1 compliant key servers
- **Encrypted vMotion**: AES-256-GCM

## PowerCLI Quick Reference

```powershell
# Connect to vCenter
Connect-VIServer -Server vcenter.local -Credential (Get-Credential)

# Get VM Information
Get-VM | Select Name, PowerState, NumCpu, MemoryGB

# Create New VM
New-VM -Name "NewVM" -ResourcePool "Production" -Datastore "vsanDatastore" `
       -DiskGB 100 -MemoryGB 16 -NumCpu 4 -GuestId "windows2019srv_64Guest"

# Configure DRS
Get-Cluster "Production" | Set-Cluster -DrsEnabled:$true -DrsAutomationLevel 'FullyAutomated'

# vMotion VM
Move-VM -VM "VMName" -Destination "esxi02.local"

# Export VM
Export-VApp -VM "VMName" -Destination "C:\Exports"
```
