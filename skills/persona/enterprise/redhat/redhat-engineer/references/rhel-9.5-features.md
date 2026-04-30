---
title: RHEL 9.5 Key Features & Enhancements
source: Red Hat Official Documentation
last_updated: 2025-11-13
---

# RHEL 9.5 Key Features & Enhancements

RHEL 9.5 was released in November 2024, bringing significant updates for enterprise infrastructure, AI workloads, and developer experience.

## Security Enhancements

### Confidential Computing for AI Workloads
- Data protection for AI training and inference
- Keeps AI workload data separate from OS data
- Enables secure AI processing with data compliance
- Prevents data exposure and minimizes insider threat risks

### Enhanced SELinux Policies
- Updated SELinux policies for more granular control
- OpenSSL 3.0 with FIPS mode improvements
- Improved firewalld and SCAP security profiles

### Pre-hardened Image Configurations
- Image Builder integrates security fixes early ("shift left")
- Pre-hardened configurations via image-builder
- Reduces setup time without requiring security expertise

### Sudo System Role
- New RHEL system role for sudo configuration at scale
- Automates sudo privilege provisioning
- Non-administrators can perform tasks securely with guardrails

## Developer Experience

### Updated Language Runtimes & Tools

| Component | Version | Notes |
|-----------|---------|-------|
| PostgreSQL | 16 | With pgvector extension for AI workloads |
| Node.js | 22 | V8 JavaScript engine upgraded to v12.4 |
| JDK | 17 (default) | JDK 11 still available |
| HTTPD | 2.4.62 | Enhanced SSL support |
| .NET | 9 | C# 13, F# 8, built-in OpenAPI support |
| Python | 3.11 | Latest stable |
| PHP | 8.2 | Modern web development |

### Toolsets & Compilers

**Rust 1.79**
- Support for stable inline `const` expressions
- Bounds in associated type position
- Improved automatic temporary lifetime extension
- Debug assertions for unsafe preconditions

**GCC 14**
- Binutils support for architecture extensions (Intel 64-bit, ARM)
- New linker script command: `asciz <string>`
- C23 and C++26 feature support

**LLVM 18**
- `code_model` attribute for global variables
- Improved AArch64, AMDGPU, PowerPC, RISC-V, IBM z, x86 backends
- LLD linker support for s390x

## Container Management (Podman 5.0)

- Multi-architecture container images with `podman farm build`
- Automatically generate systemd service files from pod descriptions (Quadlet)
- New API endpoint: `/libpod/images/$name/resolve`
- Support for zstd:chunked image compression
- Option to disable healthcheck_events

### Image Mode for RHEL
- FIPS mode support in bootc images
- Logically bound app images for system installation
- bootc-image-builder supports custom kickstart files

## System Roles Enhancements

### New ha_cluster System Role Features
- Configuring utilization attributes for node/primitive resources
- Node addresses and SBD options via `ha_cluster_node_options`

### GFS2 File System Support
- Automated GFS2 configuration for RHEL HA clusters
- Sets up dlm and lvmlockd cluster resources
- Creates LVM volume groups and logical volumes

### Storage Role - Stratis Support
- Create encrypted/unencrypted Stratis pools
- Add volumes and disks to existing pools
- Create fingerprints on managed nodes

## Web Console (Cockpit) Improvements

- **File Manager**: New GUI for file management without command line
  - Browse file system
  - Upload/download files
  - Change permissions
  - Create directories

- Advanced system metrics visualization
- Enhanced container management GUI
- Improved role-based access control

## Networking Features

- Enhanced IPsec VPN support with IPv6 addressing
- Support for `leftsubnet` parameter for complex subnet-to-subnet configs
- BIND 9.18 for improved DNS management

## SAP & Enterprise Workloads

- SAP HANA index server crash detection during scale-out/scale-in
- RHEL HA cluster health check tool for SAP HANA/S/4HANA (Tech Preview)
- RHEL High Availability on Azure Government Cloud

## Satellite 6.16

- RHEL 9 as Base OS (install on RHEL 8 or 9)
- Simple Content Access as default
- **Online Backups**: No need to stop Satellite during backup
- **Container Push**: Full OCI-compliant container registry capability
- **All Hosts Menu UI**: Bulk actions support
- **Easier Compliance**: Run playbooks directly from OpenSCAP reports
- PostgreSQL 13 and Puppet Server 8

## RHEL 10 Beta

- Real-time container image available: `registry.redhat.io/rhel10-beta/rteval`
- Run latency analysis on containerized vs bare-metal setups
