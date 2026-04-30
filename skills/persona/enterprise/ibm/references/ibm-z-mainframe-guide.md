# IBM Z Mainframe Technical Reference

## Overview

IBM Z is the world's most secure and reliable computing platform, processing 70%+ of the world's transaction value. The latest generations (z16, z17) integrate AI inference and quantum-safe cryptography.

## z16 Mainframe (2022)

### Hardware Specifications

| Component | Specification |
|-----------|---------------|
| **Processor** | Telum (7nm process) |
| **Clock Speed** | >5 GHz |
| **Cores** | Up to 160 per system |
| **Cache** | 256MB L2 per chip, 1.5GB virtual L3 |
| **Memory** | Up to 40TB per system |
| **I/O Bandwidth** | 384 GB/s |

### Telum Processor Architecture

```yaml
Telum Processor:
  AI Accelerator:
    - On-chip AI inference engine
    - 300 billion inference requests/day capability
    - <1ms latency for inference
    - No external GPU needed
    
  Security:
    - Quantum-safe cryptography (CRYSTALS-Kyber, Dilithium)
    - Crypto Express 8S (CEX8S)
    - Tamper-responsive design
    
  Reliability:
    - Dual-chip module
    - 22 billion transistors
    - Error correction at all levels
```

### AI Integration

| Use Case | Latency | Throughput |
|----------|---------|------------|
| Fraud Detection | <2ms | 19B inferences/day |
| Credit Scoring | <5ms | Real-time |
| Risk Analysis | <10ms | Batch + Real-time |
| Customer Insights | Variable | High volume |

## z17 Mainframe (2025)

### Enhancements over z16

| Feature | z16 | z17 |
|---------|-----|-----|
| AI Capacity | 300B inferences/day | Enhanced (>500B) |
| Quantum-Safe | Yes | Enhanced algorithms |
| Energy Efficiency | Baseline | 20%+ improvement |
| Throughput | Baseline | 15%+ increase |

## z/OS Operating System

### Key Components

```yaml
z/OS Architecture:
  Workload Management (WLM):
    - Service level goals
    - Dynamic resource allocation
    - Importance levels (1-6)
    
  Virtual Storage:
    - 64-bit addressing
    - Virtual storage access method (VSAM)
    - Extended addressability
    
  Unix System Services:
    - POSIX-compliant Unix environment
    - z/OS Connect integration
    - Open source support
    
  Security (RACF/ACF2/Top Secret):
    - Multi-level security
    - SAF (Security Authorization Facility)
    - Encryption everywhere
```

### Subsystems

| Subsystem | Purpose |
|-----------|---------|
| **CICS** | Online transaction processing |
| **IMS** | Hierarchical database + transactions |
| **Db2** | Relational database |
| **MQ** | Message queuing |
| **WebSphere** | Application server |
| **z/OS Connect** | REST/JSON APIs for mainframe |

## Modernization Strategies

### 1. Rehost (Lift-and-Shift)

```yaml
Rehosting Options:
  z/OS Container Extensions (zCX):
    - Run Linux containers on z/OS
    - Docker-compatible
    - Access to z/OS data
    
  z/VM:
    - Virtualization platform
    - Multiple Linux guests
    - Consolidation
    
  Linux on IBM Z:
    - Native Linux deployment
    - Same hardware, different OS
    - Cloud-native workloads
```

### 2. Refactor (Incremental)

```yaml
Refactoring Approach:
  API Enablement:
    - z/OS Connect EE
    - CICS Transaction Gateway
    - IMS Connect
    
  Modern Languages:
    - Enterprise COBOL 6.4
    - Java on z/OS
    - Node.js, Python
    
  Database Modernization:
    - Db2 for z/OS enhancements
    - JSON support
    - REST APIs
```

### 3. Replatform (Hybrid)

```
┌─────────────────────────────────────────────────────────────┐
│                   Hybrid Architecture                        │
├──────────────────┬──────────────────┬───────────────────────┤
│   Core Banking   │   API Layer      │   Modern Services     │
│   (IBM Z)        │   (z/OS Connect) │   (OpenShift)         │
│                  │                  │                       │
│ • COBOL/CICS     │ • REST/JSON      │ • Java microservices  │
│ • Db2 z/OS       │ • API management │ • AI/ML inference     │
│ • Real-time TXNs │ • Security       │ • Analytics           │
└──────────────────┴──────────────────┴───────────────────────┘
```

### 4. Replace (Selective)

| Candidate | Replacement | Complexity |
|-----------|-------------|------------|
| Legacy reporting | Cloud analytics | Low |
| Batch processes | Event streaming | Medium |
| Customer portals | Cloud-native apps | Medium |
| Core transactions | Keep on Z | High |

## Security Features

### Quantum-Safe Cryptography

```yaml
Quantum-Safe on z16/z17:
  Algorithms:
    - CRYSTALS-Kyber: Key encapsulation
    - CRYSTALS-Dilithium: Digital signatures
    - SPHINCS+: Stateless signatures
    
  Implementation:
    - Hardware acceleration
    - z/OS integrated
    - Crypto Express 8S support
    
  Migration:
    - Crypto agility framework
    - Hybrid certificates
    - Gradual transition path
```

### Data Protection

| Feature | Description |
|---------|-------------|
| ** pervasive encryption** | Encrypt all data by default |
| **z/OS Data Privacy Passports** | Track data across systems |
| **Trusted Execution** | Secure enclaves for sensitive processing |
| **RACF Multi-Factor** | Enhanced authentication |

## Performance & Capacity

### Capacity Settings

```yaml
Capacity on Demand:
  Models:
    - CUoD: Capacity Upgrade on Demand
    - CBU: Capacity Backup
    - On/Off CoD: Temporary capacity
    
  Benefits:
    - Pay for what you use
    - Handle peak loads
    - DR capacity
```

### Benchmarks

| Workload | Metric | Value |
|----------|--------|-------|
| Online transactions | TPM | Millions/minute |
| Batch processing | Throughput | TBs/hour |
| AI inference | Latency | <2ms |
| Availability | Uptime | 99.99999% |

## Development Tools

### Modern Toolchain

```yaml
z/OS Development:
  IDEs:
    - IBM Developer for z/OS (IDz)
    - VS Code with Zowe extensions
    - Eclipse-based tools
    
  DevOps:
    - Git on z/OS
    - DBB (Dependency Based Build)
    - zUnit testing
    - SCLM or Git-based SCM
    
  API Development:
    - z/OS Connect API Editor
    - OpenAPI specification
    - Automated SDK generation
```

### Zowe (Open Source)

| Component | Function |
|-----------|----------|
| **Zowe CLI** | Command-line interface |
| **Zowe Explorer** | VS Code extension |
| **Zowe API ML** | API Mediation Layer |
| **Zowe App Framework** | Web-based desktop |

## Integration Patterns

### Cloud Integration

```yaml
Hybrid Cloud Connectivity:
  Direct Connect:
    - IBM Cloud Direct Link
    - AWS Direct Connect
    - Azure ExpressRoute
    
  Data Replication:
    - IBM InfoSphere CDC
    - Db2 replication
    - Event streaming (Kafka)
    
  API Integration:
    - z/OS Connect
    - IBM API Connect
    - Event Streams
```

### AI Integration

```yaml
AI on IBM Z:
  On-Platform AI:
    - Telum AI accelerator
    - Real-time inference
    - No data movement
    
  Hybrid AI:
    - watsonx.ai integration
    - Model training off-platform
    - Inference on Z
    - Data gravity advantage
```

## Migration Assessment

### Code Analysis Tools

| Tool | Purpose |
|------|---------|
| **IBM Application Discovery** | Code inventory, dependencies |
| **IBM Wazi Analyze** | Static analysis |
| **vFunction** | Modernization assessment |
| **CAST Highlight** | Cloud readiness |

### Risk Assessment Matrix

| Factor | Risk Level | Mitigation |
|--------|------------|------------|
| Code complexity | Variable | Automated analysis |
| Knowledge gaps | High | Training, documentation |
| Integration depth | High | API-first approach |
| Regulatory requirements | Medium | Compliance validation |

---

*Source: IBM Z Documentation, z/OS Knowledge Center, IBM Redbooks, IBM Developer*
