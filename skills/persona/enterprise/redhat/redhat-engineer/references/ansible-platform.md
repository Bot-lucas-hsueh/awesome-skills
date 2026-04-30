---
title: Ansible Automation Platform
source: Red Hat Documentation
last_updated: 2025-07-23
---

# Ansible Automation Platform

## Overview

Ansible Automation Platform (AAP) is Red Hat's enterprise automation solution, providing a foundation for building and operating automation at scale.

## Scale Metrics

| Metric | Value |
|--------|-------|
| Monthly Downloads | 45M+ |
| Daily Automation Tasks | 2B+ |
| Certified Collections | 150+ |
| Community Modules | 4,000+ |

## Architecture

### Control Plane Components

```yaml
Ansible Automation Platform:
  Control Plane:
    - Automation Controller (formerly Ansible Tower)
      * Web UI and REST API
      * Role-based access control (RBAC)
      * Job scheduling and workflow orchestration
      * Multi-tenant support
    
    - Private Automation Hub
      * Content governance and curation
      * Certified Content Collections repository
      * Custom execution environment registry
      * RBAC for content publishing
    
    - Event-Driven Ansible (EDA)
      * Reactive automation
      * Event source plugins (webhook, kafka, etc.)
      * Rulebooks for event processing
      * Event-driven decision making
  
  Execution Layer:
    - Execution Environments
      * Containerized automation runtime
      * Pre-built with required dependencies
      * Consistent execution across environments
      * Custom EE creation via ansible-builder
    
    - Automation Mesh
      * Distributed execution architecture
      * Hop nodes for network isolation
      * Execution nodes for workload distribution
      * Resilient communication paths
    
    - Ansible Navigator
      * CLI experience for automation
      * Execution environment introspection
      * Local testing and development
  
  Content Layer:
    - Certified Content Collections
      * Red Hat supported and maintained
      * Partner-provided certified content
      * Predictable lifecycle and updates
    
    - Ansible Galaxy
      * Community content repository
      * 4,000+ community modules
      * Role and collection sharing
```

## Key Features

### Event-Driven Ansible (EDA)

**Use Cases:**
- Auto-remediation of infrastructure issues
- Dynamic scaling based on metrics
- Security response automation
- CI/CD pipeline triggers

**Components:**
- **Event Sources**: Webhooks, Kafka, Azure Events, AWS SQS, etc.
- **Rulebooks**: YAML-defined event-condition-action rules
- **Actions**: Run playbooks, call APIs, send notifications

### Automation Mesh

**Benefits:**
- Execute automation across isolated networks
- Distribute workloads across geographic regions
- Resilient communication with automatic failover
- Support for complex network topologies

**Node Types:**
- **Control Nodes**: Run automation controller
- **Execution Nodes**: Execute automation jobs
- **Hop Nodes**: Relay traffic between networks

### Execution Environments

**Included in Default EEs:**
- ansible-core
- Python 3.9+
- Common collections (ansible.posix, community.general)
- Cloud SDKs (boto3, azure-mgmt, google-cloud)

**Building Custom EEs:**
```yaml
# execution-environment.yml
version: 3
images:
  base_image:
    name: registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8:latest
dependencies:
  galaxy:
    collections:
      - my_namespace.my_collection
  python:
    - requests
    - custom-library
  system:
    - openssl
```

## Integration with HashiCorp (Post-Acquisition)

Following IBM's acquisition of HashiCorp:

- **Ansible + Terraform**: Joint product synergies
- **2x Annual Bookings**: In first quarter post-close
- **Integrated Value Proposition**: Infrastructure provisioning + configuration management

## RHEL System Roles

Red Hat maintains Ansible Content Collections specifically for RHEL management:

| System Role | Purpose |
|-------------|---------|
| timesync | NTP/chrony configuration |
| selinux | SELinux policy management |
| firewall | firewalld configuration |
| crypto_policies | System-wide cryptographic policies |
| ha_cluster | High availability cluster setup |
| storage | LVM, Stratis, partition management |
| kdump | Kernel crash dump configuration |
| network | Network interface management |
| postfix | Mail server configuration |
| ssh | SSH server configuration |
| sudo | Sudo privilege management |

## Use Cases

### IT Operations Automation
- Server provisioning and configuration
- Patch management at scale
- Compliance enforcement
- Log aggregation setup

### Network Automation
- Switch/router configuration
- VLAN management
- Firewall rule deployment
- Load balancer configuration

### Security Automation
- Vulnerability remediation
- Incident response
- Security policy enforcement
- Threat hunting automation

### Cloud Automation
- Multi-cloud resource provisioning
- Kubernetes cluster deployment
- Cloud networking setup
- Cost optimization workflows

## AAP 2.4+ New Features

- **Simplified Installation**: Container-based deployment
- **Enhanced UI**: Improved job visualization
- **Workflows**: Visual workflow builder
- **Scheduling**: Advanced job scheduling
- **Notifications**: Multi-channel alerting
- **Analytics**: Automation execution insights
