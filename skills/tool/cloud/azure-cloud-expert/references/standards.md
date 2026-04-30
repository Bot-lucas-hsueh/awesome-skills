# Standards & Reference

## 7.1 Official Documentation

- [Azure Documentation](https://learn.microsoft.com/azure/) — Full documentation for all Azure services
- [Azure Architecture Center](https://learn.microsoft.com/azure/architecture/) — Design patterns, best practices, reference architectures
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/architecture/framework/) — Reliability, Security, Cost Optimization, Operational Excellence
- [Azure Identity Best Practices](https://learn.microsoft.com/azure/active-directory/fundamentals/identity-best-practices) — MFA, conditional access, PIM
- [Azure Regions](https://learn.microsoft.com/azure/global-infrastructure/geographies/) — Available regions and services
- [Azure CLI Reference](https://learn.microsoft.com/cli/azure/) — All Azure CLI commands
- [Azure REST API Reference](https://learn.microsoft.com/rest/api/azure/) — REST API documentation
- [Azure Support Plans](https://azure.microsoft.com/support/plans/) — Basic, Developer, Professional Direct, Premier

## 7.2 Azure AD / Entra ID Security Best Practices

### 7.2.1 Identity Protection

| Practice | Implementation |
|----------|----------------|
| **MFA for all users** | Enable conditional access requiring MFA |
| **Passwordless auth** | FIDO2 security keys, Windows Hello, Microsoft Authenticator |
| **Conditional Access** | Block legacy auth, require compliant devices |
| **Privileged Identity Management** | Just-in-time admin access, approval workflows |
| **Identity Protection** | Automated risk-based policies |

### 7.2.2 Conditional Access Policy Example

```json
{
  "displayName": "Block Legacy Authentication",
  "state": "enabled",
  "conditions": {
    "clientAppTypes": ["exchangeActiveSync", "other"],
    "platforms": [],
    "locations": [],
    "clientApplications": []
  },
  "grantControls": {
    "operator": "block",
    "builtInControls": []
  }
}
```

### 7.2.3 RBAC Best Practices

| Principle | Implementation |
|-----------|----------------|
| **Least privilege** | Use built-in roles; create custom only when needed |
| **Scope appropriately** | Assign at resource group or subscription level |
| **Use groups** | Assign roles to groups, not individual users |
| **Break-glass accounts** | Emergency access accounts with permanent privileges |

### 7.2.4 Built-in RBAC Roles

| Role | Use Case |
|------|----------|
| **Reader** | View all resources |
| **Contributor** | Create/manage resources (no access control) |
| **Owner** | Full access including delegation |
| **User Access Administrator** | Manage user access |
| **Network Contributor** | Network resource management |
| **Storage Blob Data Contributor** | Read/write blob storage |

## 7.3 Region Selection

### 7.3.1 Key Considerations

| Factor | Consideration |
|--------|---------------|
| **Data residency** | EU, Germany, France have strict data sovereignty |
| **Latency** | Choose region closest to users |
| **Service availability** | Not all services in all regions |
| **Sovereignty** | Government clouds (US Gov, China) |
| **Pricing** | Varies by region, check calculator |

### 7.3.2 Common Azure Regions

| Region | Name | Use Case |
|--------|------|----------|
| eastus | East US | Low cost, many services |
| westus2 | West US 2 | High availability, large capacity |
| westeurope | West Europe | EU workloads, GDPR |
| southeastasia | Southeast Asia | APAC workloads |
| australiaeast | Australia East | ANZ workloads |
| uksouth | UK South | UK data residency |

## 7.4 Cost Optimization

### 7.4.1 Cost Management Hierarchy

```
Azure Cost Management
├── Azure Advisor recommendations
├── Reserved VM instances (30-72% savings)
├── Azure Hybrid Benefit (up to 40% savings)
├── Spot VMs (60-90% savings)
├── Auto-shutdown for dev/test
└── Right-size underutilized resources
```

### 7.4.2 Azure Hybrid Benefit

| Scenario | Benefit |
|----------|---------|
| Windows Server with SA | Save up to 40% on VMs |
| SQL Server with SA | Save up to 55% on SQL VMs |
| Azure Dev/Test | Discounted rates for dev/test |

### 7.4.3 Azure Reserved Instances

| Term | Savings vs Pay-as-you-go |
|------|-------------------------|
| 1 year | Up to 72% |
| 3 years | Up to 72% |
| 3 years with Azure Hybrid Benefit | Up to 80% |

### 7.4.4 Storage Cost Tiers

| Tier | Access Tier | Cost | Use Case |
|------|-------------|------|----------|
| Hot | Hot | Highest | Frequently accessed |
| Cool | Cool | ~50% less | Infrequently accessed (>30 days) |
| Cold | Cold | ~80% less | Rarely accessed (>90 days) |
| Archive | Archive | ~95% less | Never accessed (>180 days) |

## 7.5 Resource Naming Conventions

| Resource Type | Pattern | Example |
|--------------|---------|---------|
| Resource Group | rg-{environment}-{project} | rg-prod-webapp |
| Virtual Network | vnet-{region}-{project} | vnet-eastus-main |
| Subnet | snet-{environment}-{purpose} | snet-prod-app |
| VM | vm-{environment}-{role} | vm-prod-web01 |
| Storage Account | st{region}{project} | steastusmyapp |
| App Service | app-{project}-{env} | app-myapp-prod |
| SQL Server | sql-{project}-{env} | sql-myapp-prod |

## 7.6 Azure Well-Architected Framework Pillars

| Pillar | Focus Areas |
|--------|-------------|
| **Reliability** | SLAs, availability zones, disaster recovery |
| **Security** | Defense in depth, encryption, identity |
| **Cost Optimization** | Right-sizing, reserved capacity, auto-scaling |
| **Operational Excellence** | Monitoring, automation,IaC |
| **Performance Efficiency** | Auto-scaling, load balancing, caching |
