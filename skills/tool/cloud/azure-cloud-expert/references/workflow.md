# Troubleshooting Guide

## 8.1 Common Azure Errors and Fixes

### 8.1.1 VM/Compute Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `QuotaExceededException` | Subscription resource limits | Request quota increase or use different region |
| `InvalidTemplateDeployment` | ARM template syntax error | Validate template syntax |
| `VMExtensionProvisioningTimeout` | Extension failed to install | Check network connectivity, disk space |
| `OSProvisioningTimedOut` | VM OS configuration failed | Use custom script extension, retry |
| `InvalidParameterValue` | Invalid parameter in request | Verify parameter values |

### 8.1.2 Networking Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `NetworkInterfaceInvalidSubnet` | Subnet doesn't exist | Verify subnet ID |
| `PublicIPAddressLimitExceeded` | Too many public IPs | Release unused IPs |
| `VirtualNetworkGatewayTimeout` | VPN connection dropped | Check on-prem firewall, NAT settings |
| `InvalidAddressSpace` | CIDR overlap | Ensure no overlapping address spaces |
| `VnetAddressSpaceConflict` | Address space already in use | Use different CIDR |

### 8.1.3 Storage Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `StorageAccountAlreadyExists` | Name taken globally | Use unique name (3-24 chars, lowercase) |
| `AuthenticationFailed` | Shared key or SAS issue | Regenerate keys, check SAS expiry |
| `NoAuthenticationInformation` | Missing auth header | Add Authorization header |
| `RequestBodyTooLarge` | File >256MB for sync | Use async copy or larger block |

### 8.1.4 Azure AD / Entra Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `AADSTS50034` | User not in tenant | Verify user UPN, tenant ID |
| `AADSTS700016` | App not in tenant | Register application |
| `AADSTS70002` | Invalid credentials | Check client secret, certificate |
| `AADSTS50005` | Conditional Access policy | Review conditional access policies |

### 8.1.5 ARM Deployment Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `DeploymentFailed` | General deployment failure | Check activity log for details |
| `InvalidTemplate` | Template syntax error | Validate JSON syntax |
| `MissingRegistrationForType` | Provider not registered | Register Microsoft.Resources |

## 8.2 Diagnostic Commands

### 8.2.1 Azure CLI Diagnostics

```bash
# Check subscription and context
az account show
az account list-locations

# List resources and their status
az resource list \
  --resource-group my-rg \
  --query "[].{name:name, type:type, status:provisioningState}"

# Check VM status
az vm get-instance-view \
  --resource-group my-rg \
  --name my-vm

# View deployment operations
az deployment operation list \
  --resource-group my-rg \
  --name my-deployment
```

### 8.2.2 Network Diagnostics

```bash
# Check NSG rules
az network nsg show \
  --resource-group my-rg \
  --name my-nsg

# Test network connectivity
az network traffic-manager profile list
az network application-gateway show \
  --resource-group my-rg \
  --name my-appgw

# Check VPN gateway status
az network vpn-connection show \
  --resource-group my-rg \
  --name my-vpn
```

### 8.2.3 Azure Monitor/Log Analytics

```bash
# Query activity log
az monitor activity-log list \
  --resource-group my-rg \
  --start-time 2024-01-01T00:00:00Z

# View metric alerts
az monitor metrics alert list \
  --resource-group my-rg

# Query Log Analytics
az monitor log-analytics query \
  --workspace my-workspace \
  --analytics-query "AzureActivity | where TimeGenerated > ago(1d)"
```

## 8.3 Support and Resources

### 8.3.1 Azure Support Plans

| Plan | Price | Response Time |
|------|-------|---------------|
| **Basic** | Free | Billing only, community |
| **Developer** | $29/mo | Business hours, <8hr |
| **Professional Direct** | $100/mo | 24/7, <1hr critical |
| **Premier** | Custom | Dedicated TAM, fastest response |

### 8.3.2 Resources for Help

1. **Microsoft Q&A** — Official community support
2. **Azure Advisor** — Personalized recommendations
3. **Azure Service Health** — Service-specific issues
4. **Azure Status** — Platform-wide status
5. **Azure Support** — Create support request (Premier/Direct)

### 8.3.3 Quick Diagnostics

```bash
# Check resource health
az provider show \
  --namespace Microsoft.Compute \
  --query "registrationState"

# View resource locks
az lock list \
  --resource-group my-rg

# Check role assignments
az role assignment list \
  --assignee user@example.com
```

## 8.4 Debugging Workflow

```
Step 1: Identify Resource Health
├── Check Azure Service Health
├── Check Resource Health blade
└── Review Activity Log

Step 2: Verify Configuration
├── Check ARM template output
├── Review resource properties
└── Validate network configuration

Step 3: Network Debugging
├── Test with Network Watcher
├── Check NSG rules
├── Verify DNS resolution
└── Use Connection Troubleshooter

Step 4: Authentication/Authorization
├── Check RBAC assignments
├── Verify Azure AD app registration
├── Review conditional access policies
└── Check Managed Identity status

Step 5: Performance
├── Check Azure Monitor metrics
├── Review Application Insights
├── Analyze Log Analytics queries
└── Check resource quotas
```

## 8.5 Common Debugging Patterns

### 8.5.1 "Cannot Connect to VM" Debugging

```
1. Check VM is running (az vm show)
2. Verify public IP is assigned
3. Check NSG allows port 3389/22
4. Verify no lock on resource
5. Check Boot diagnostics for errors
6. Reset RDP/SSH if needed
```

### 8.5.2 "Deployment Failed" Debugging

```
1. Get deployment details: az deployment show
2. Check operation details: az deployment operation list
3. Look for validation errors
4. Verify resource provider registration
5. Check for naming conflicts
6. Review template syntax
```

### 8.5.3 "Authentication Failed" Debugging

```
1. Verify tenant ID in connection string
2. Check client ID matches app registration
3. Validate client secret hasn't expired
4. Confirm API permissions granted
5. Check conditional access policies
6. Review audit logs in Azure AD
```
