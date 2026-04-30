# CrowdStrike Falcon Platform Modules Reference

## Overview
The CrowdStrike Falcon platform consists of 30+ cloud-delivered modules providing comprehensive security across endpoints, cloud workloads, identity, and data.

---

## Endpoint Security Modules

### Falcon Prevent (NGAV)
**Purpose**: Next-generation antivirus with AI-powered malware prevention
**Key Features**:
- Machine learning-based malware detection
- Exploit prevention for zero-day attacks
- Ransomware protection with behavioral blocking
- Fileless attack prevention
- Offline protection with local AI models

**Deployment**: Lightweight sensor (<1% CPU, ~200MB RAM)
**Platforms**: Windows, macOS, Linux, Chrome OS

### Falcon Insight XDR
**Purpose**: Extended Detection and Response across endpoints
**Key Features**:
- Endpoint Detection and Response (EDR)
- Extended Detection and Response (XDR)
- Event Search query language
- Real Time Response (RTR) remote shell
- Threat hunting workbench
- MITRE ATT&CK mapping

**Data Retention**: 90 days standard, 1 year premium

### Falcon Device Control
**Purpose**: USB and peripheral device management
**Key Features**:
- USB device whitelisting/blacklisting
- Removable storage encryption enforcement
- Peripheral control (printers, cameras, etc.)
- Policy-based device access

### Falcon Firewall Management
**Purpose**: Host-based firewall policy enforcement
**Key Features**:
- Centralized firewall rule management
- Pre-built policy templates
- Network visibility and monitoring
- Role-based access control

---

## Cloud Security Modules (CNAPP)

### Falcon Horizon (CSPM)
**Purpose**: Cloud Security Posture Management
**Key Features**:
- Agentless multi-cloud scanning (AWS/Azure/GCP)
- CIS benchmark compliance
- Custom Indicators of Misconfiguration (IOMs)
- Attack path analysis
- Compliance reporting (PCI-DSS, SOC 2, HIPAA)

**Scan Frequency**: Continuous
**Coverage**: 150+ cloud services

### Falcon Cloud Workload Protection (CWP)
**Purpose**: Runtime protection for cloud workloads
**Key Features**:
- Agent-based workload protection
- Container security (Docker, Kubernetes)
- Serverless function monitoring
- Vulnerability management for cloud assets
- CI/CD pipeline integration

**Deployment**: Falcon sensor on VMs/containers

### Falcon Cloud Identity (CIEM)
**Purpose**: Cloud Infrastructure Entitlement Management
**Key Features**:
- Cross-cloud identity visibility
- Least privilege recommendations
- Anomalous access detection
- Shadow admin identification
- Entitlement drift monitoring

---

## Identity Security Modules

### Falcon Identity Protection
**Purpose**: Zero Trust identity security
**Key Features**:
- Active Directory protection
- Azure AD/Entra ID integration
- Kerberoasting detection
- Risk-based conditional access
- MFA enforcement
- Identity threat detection

**Integration**: Okta, Ping, Duo, CyberArk

### Falcon Identity Threat Detection
**Purpose**: Identity-based attack detection
**Key Features**:
- Credential compromise detection
- Lateral movement tracking
- Privilege escalation monitoring
- Rogue device detection
- Behavioral analytics

---

## Security Operations Modules

### Falcon Next-Gen SIEM
**Purpose**: Modern security information and event management
**Key Features**:
- LogScale ingestion engine
- 10-year data retention
- Real-time search and analytics
- 10GB/day free third-party data ingest
- Unified investigation workbench

**Performance**: Sub-second query response

### Falcon Fusion SOAR
**Purpose**: Security orchestration, automation, and response
**Key Features**:
- Visual workflow builder
- 300+ pre-built connectors
- Automated playbook execution
- Case management integration
- Charlotte AI-powered workflows

### Charlotte AI
**Purpose**: Generative and agentic AI for security operations
**Key Features**:
- Natural language threat investigation
- Automated detection triage
- Incident summarization
- Agentic SOC workflows
- AgentWorks no-code agent builder

**Architecture**: Multi-AI with 12+ specialized models

---

## Managed Services Modules

### Falcon OverWatch
**Purpose**: 24/7 managed threat hunting
**Tiers**:
- **OverWatch**: Endpoint threat hunting
- **OverWatch Elite**: Endpoint + Identity + Cloud
- **OverWatch Next-Gen SIEM**: Includes third-party data

**Features**:
- Elite threat hunter team
- Proactive adversary detection
- Intelligence-driven hunting
- Cross-domain coverage
- 24/7/365 coverage

### Falcon Complete
**Purpose**: Managed Detection and Response (MDR)
**Features**:
- End-to-end threat management
- Incident response handling
- Threat hunting
- Remediation assistance
- Breach prevention warranty

**SLA**: 15-minute response for critical alerts

### Falcon Counter Adversary Operations
**Purpose**: Advanced threat intelligence and hunting
**Features**:
- Adversary tracking (245+ groups)
- Strategic threat intelligence
- Custom threat reports
- Executive briefings
- Nation-state attack detection

---

## Vulnerability Management Modules

### Falcon Spotlight
**Purpose**: Vulnerability assessment and prioritization
**Features**:
- Real-time vulnerability scanning
- Exploit intelligence integration
- Risk-based prioritization
- Patch management integration
- Exposure validation

**Coverage**: OS, applications, cloud resources

---

## Threat Intelligence Modules

### Falcon X
**Purpose**: Automated threat intelligence
**Features**:
- IOC enrichment
- Automated threat feeds
- Adversary intelligence
- Malware analysis
- Intelligence reports

### Falcon Intelligence
**Purpose**: Strategic threat intelligence
**Features**:
- Adversary profiles
- TTP analysis
- Industry threat reports
- Custom intelligence requirements
- Executive threat briefings

---

## IT Operations Modules

### Falcon for IT
**Purpose**: Unified security and IT operations
**Features**:
- Asset inventory
- Software usage analytics
- License optimization
- Configuration management
- IT hygiene scoring

### Falcon Discover
**Purpose**: IT asset discovery
**Features**:
- Unmanaged device discovery
- Shadow IT detection
- Network asset inventory
- IoT device visibility

---

## Module Selection Guide

### Small Business (100-500 endpoints)
**Essential**: Falcon Prevent + Falcon Insight
**Recommended**: + Falcon OverWatch

### Mid-Market (500-5,000 endpoints)
**Essential**: Falcon Prevent + Insight + OverWatch
**Recommended**: + Falcon Spotlight + Identity Protection
**Cloud**: + Falcon Horizon + CWP

### Enterprise (5,000+ endpoints)
**Core**: All endpoint modules + OverWatch Elite
**Cloud**: Full CNAPP (Horizon + CWP + CIEM)
**Identity**: Falcon Identity Protection
**Operations**: Next-Gen SIEM + Fusion SOAR + Charlotte AI
**Services**: Falcon Complete MDR

---

## Integration Matrix

| Module | SIEM | SOAR | Identity | Cloud | Ticketing |
|--------|------|------|----------|-------|-----------|
| Prevent | ✓ | ✓ | ✓ | - | ✓ |
| Insight | ✓ | ✓ | ✓ | - | ✓ |
| Horizon | ✓ | ✓ | - | ✓ | ✓ |
| CWP | ✓ | ✓ | - | ✓ | ✓ |
| Identity | ✓ | ✓ | ✓ | ✓ | ✓ |
| SIEM | - | ✓ | ✓ | ✓ | ✓ |
| OverWatch | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Pricing Model

Falcon modules are sold as:
- **Per-endpoint** (annual subscription)
- **Per-workload** (cloud assets)
- **Per-user** (identity protection)
- **Volume tiers** (enterprise discounts)

**Entry Points**:
- Falcon Go: $300/year (small business)
- Falcon Pro: Standard enterprise
- Falcon Enterprise: Full platform
- Falcon Premium: All modules + services

---

*Last Updated: 2026-03-21*
*Version: 2.0.0*
