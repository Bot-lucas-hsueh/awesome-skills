# Microsoft Security Reference

## Security Products

### Microsoft Sentinel
- **Type**: Cloud-native SIEM + SOAR
- **Capabilities**:
  - Log collection and analysis
  - Threat detection (built-in + custom)
  - Incident investigation
  - Automated response
  - Threat intelligence integration

### Microsoft Defender
| Product | Focus |
|---------|-------|
| Defender for Endpoint | Endpoint protection |
| Defender for Office 365 | Email and collaboration |
| Defender for Identity | Identity protection |
| Defender for Cloud | Cloud workload protection |
| Defender for Cloud Apps | SaaS security |

### Microsoft Entra
| Service | Purpose |
|---------|---------|
| Entra ID | Identity and access management |
| Entra Permissions Management | CIEM (Cloud Infrastructure Entitlements) |
| Entra Verified ID | Decentralized identity |
| Entra Identity Protection | Risk-based policies |

## Zero Trust Architecture

### Core Principles
1. **Verify explicitly**: Always authenticate and authorize
2. **Use least privilege**: Minimal access necessary
3. **Assume breach**: Segment networks, monitor everything

### Implementation Layers
```
Identity
├── MFA required
├── Risk-based policies
├── Passwordless authentication
├── PIM for admin roles

Devices
├── Intune enrollment
├── Compliance policies
├── Conditional access
└── Endpoint detection

Applications
├── App proxy for on-prem
├── MFA per app
├── Session controls
└── Real-time monitoring

Data
├── Classification labels
├── DLP policies
├── Encryption
└── Access reviews

Network
├── Micro-segmentation
├── Private endpoints
├── Conditional access
└── Threat protection
```

## Compliance Framework

### Microsoft Purview
| Capability | Function |
|------------|----------|
| Data Catalog | Data discovery and classification |
| Data Map | Unified data governance |
| Data Loss Prevention | Protect sensitive data |
| Insider Risk Management | Detect risky activity |
| eDiscovery | Legal investigation |
| Compliance Manager | Track compliance posture |

### Key Compliance Standards
| Standard | Azure | M365 |
|----------|-------|------|
| SOC 2 Type II | ✅ | ✅ |
| ISO 27001 | ✅ | ✅ |
| HIPAA | ✅ | ✅ |
| FedRAMP High | ✅ | ✅ |
| PCI DSS | ✅ | ✅ |
| GDPR | ✅ | ✅ |

## Security Best Practices

### Identity Security
1. Enable MFA for all users
2. Implement passwordless authentication
3. Use Conditional Access policies
4. Enable PIM for privileged roles
5. Regular access reviews

### Data Protection
1. Classify and label data
2. Implement DLP policies
3. Encrypt data at rest and in transit
4. Use customer-managed keys for sensitive data
5. Enable audit logging

### Threat Protection
1. Deploy Defender across endpoints
2. Enable Sentinel for central SIEM
3. Integrate threat intelligence
4. Automate response playbooks
5. Conduct regular threat hunting

## Incident Response

### Severity Levels
| Level | Criteria | Response Time |
|-------|----------|---------------|
| Critical | Active breach, data exfiltration | 15 minutes |
| High | Confirmed compromise | 1 hour |
| Medium | Suspicious activity | 4 hours |
| Low | Policy violation | 24 hours |

### Response Playbook
1. **Detect**: Alert from Defender/Sentinel
2. **Triage**: Validate severity, assign owner
3. **Contain**: Isolate affected resources
4. **Investigate**: Root cause analysis
5. **Remediate**: Fix vulnerability, remove threat
6. **Recover**: Restore services, monitor
7. **Learn**: Post-incident review

---

**Last Updated**: 2026-03-21
