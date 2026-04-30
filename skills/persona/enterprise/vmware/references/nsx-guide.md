# NSX Reference Guide

## NSX Architecture

### Management Plane
- **NSX Manager**: Policy and management API, UI
- **Cluster**: 3-node cluster for HA (requires NSX+ license for 3rd node)
- **Backup**: FTP/SFTP-based backup/restore

### Control Plane
- **Central Control Plane (CCP)**: Runs on NSX Manager cluster
- **Local Control Plane (LCP)**: Runs on transport nodes (ESXi, Edge, KVM)
- **Routing**: BGP, OSPF, static routes

### Data Plane
- **Kernel Modules**: VIBs installed on ESXi
- **DPDK**: Data Plane Development Kit for performance
- **SR-IOV**: Single Root I/O Virtualization support

## Transport Zones

| Type | Purpose | Use Case |
|------|---------|----------|
| VLAN | Layer 2 VLAN-backed | Physical network extension |
| Overlay | VXLAN/GENEVE encapsulated | Virtual networks |

### GENEVE (NSX-T)
- **Encapsulation**: UDP port 6081
- **MTU**: Minimum 1600 bytes (recommended 9000)
- **Header**: 8 bytes + options

## Logical Networking

### Tier-0 Gateway
- **Function**: North-south routing, external connectivity
- **HA Mode**: Active-Active or Active-Standby
- **Protocols**: BGP, OSPF, static routing
- **Services**: NAT, VPN, Load Balancer (limited)

### Tier-1 Gateway
- **Function**: East-west routing, tenant/department router
- **Connectivity**: Connects to Tier-0 (optional)
- **Services**: NAT, Load Balancer, VPN, DHCP
- **DR Mode**: Distributed routing only (no Edge for E-W)

### Segments (Logical Switches)
- **Type**: VLAN-backed or Overlay
- **Subnets**: CIDR definition per segment
- **Dhcp**: Local DHCP server or relay

## Security

### Distributed Firewall (DFW)
- **Enforcement**: Kernel-level on each ESXi host
- **Rules**: Applied to vNICs (not VMs)
- **Modes**: Stateless (L3/L4) or Stateful (L3-L7)
- **Hit Count**: Rule usage tracking

### Gateway Firewall
- **Location**: Applied at Tier-0 or Tier-1
- **Direction**: North-south traffic
- **VPN**: IPsec VPN integration

### Micro-Segmentation Strategy
```
1. Identify application tiers (Web, App, DB)
2. Create segments for each tier
3. Define DFW policies:
   - Allow Web → App (HTTP/HTTPS)
   - Allow App → DB (database ports)
   - Deny all other traffic
4. Apply tags for dynamic grouping
5. Enable logging for policy validation
```

### IDS/IPS
- **Modes**: Detect only or Detect & Prevent
- **Signatures**: Regularly updated threat signatures
- **Profiles**: Custom or default profiles

## Load Balancer

### Types
| Type | Use Case | Layer |
|------|----------|-------|
| L4 Load Balancer | TCP/UDP load balancing | Transport |
| L7 Load Balancer | HTTP/HTTPS with routing | Application |
| Ingress | Kubernetes ingress | L7 |

### Algorithms
- **Round Robin**: Equal distribution
- **Least Connection**: Fewest active connections
- **IP Hash**: Source IP-based distribution
- **Weighted**: Based on server capacity

## VPN Services

### IPsec VPN
- **Modes**: Policy-based or Route-based
- **IKE Versions**: IKEv1 or IKEv2
- **Encryption**: AES-GCM, AES-CBC
- **DH Groups**: 14-21, 24, 31

### L2VPN
- **Use Case**: Layer 2 extension over L3
- **Modes**: Server (NSX Edge) or Client (standalone edge)

## NSX CLI Quick Reference

```bash
# Get transport nodes
get transport-nodes

# Check tunnel status
get tunnel

# Verify routing table
get logical-routers
get route

# Check DFW rules
vsipioctl getrules

# Trace traffic flow
start traffic-trace vnic <vnic-id>
```

## PowerNSX Quick Reference

```powershell
# Connect to NSX Manager
Connect-NsxServer -Server nsx.local -Credential (Get-Credential)

# Create Transport Zone
New-NsxTransportZone -Name "TZ-Overlay" -TransportType "Overlay"

# Create Logical Switch (Segment)
New-NsxLogicalSwitch -Name "Web-Segment" -TransportZone (Get-NsxTransportZone "TZ-Overlay")

# Configure DFW Rule
Get-NsxFirewallSection "Application Rules" | 
    New-NsxFirewallRule -Name "Allow Web to App" `
    -Source (Get-NsxSecurityGroup "Web-Servers") `
    -Destination (Get-NsxSecurityGroup "App-Servers") `
    -Service (Get-NsxService "HTTP", "HTTPS") `
    -Action allow
```
