# Troubleshooting Guide

## 8.1 Subscription & Billing Issues

### Subscription Not Found
- Verify subscription ID in Azure portal
- Check if subscription is disabled or expired
- Confirm user has proper RBAC access to subscription
```bash
az account show
az account list --output table
az role assignment list --assignee <user-email>
```

### Unexpected Costs
1. Check Cost Management + Billing in portal
2. Review Resource Group costs
3. Enable budgets and alerts
4. Check for orphaned resources
```bash
# List running VMs
az vm list --output table

# List expensive resources
az resource list --query "[?type=='Microsoft.Compute/virtualMachines']" --output table
```

## 8.2 Authentication & Authorization Issues

### Login Failures
```bash
# Clear cached credentials
az account clear
az login --tenant <tenant-id>

# Check current account
az account show

# Re-login with service principal
az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>
```

### RBAC Permission Denied
| Error | Cause | Fix |
|-------|-------|-----|
| "AuthorizationFailed" | No role assignment | Add role with `az role assignment create` |
| "Forbidden" | Insufficient scope | Request at subscription/resource group level |
| "PrincipalNotFound" | Deleted service principal | Recreate or update managed identity |

### Managed Identity Issues
```bash
# Enable system managed identity
az vm identity assign --name <vm-name> --resource-group <rg>

# Get access token
curl -H "Metadata: true" "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com"
```

## 8.3 Resource Deployment Issues

### Resource Group Locked
```bash
# List locks
az lock list --resource-group <rg-name>

# Delete lock (requires Owner)
az lock delete --name <lock-name> --resource-group <rg-name> --resource-type Microsoft.Resources/resourceGroups
```

### Template Deployment Failures
```bash
# Validate template
az deployment group validate \
  --resource-group <rg> \
  --template-file template.json \
  --parameters parameters.json

# See deployment history
az deployment group list --resource-group <rg> --output table

# Get deployment details
az deployment group show --resource-group <rg> --name <deployment-name>
```

## 8.4 Network Connectivity Issues

### VNet Peering Issues
- Check address spaces don't overlap
- Verify both subscriptions in same AAD tenant
- Ensure Gateway Transit enabled if needed

### DNS Resolution Failures
```bash
# Check custom DNS on VNet
az network vnet show --name <vnet-name> --resource-group <rg> --query dnsServers

# Test DNS from VM
nslookup <internal-domain>
az vm run-command invoke --command-id RunShellScript --name <vm> -g <rg> --scripts "nslookup <domain>"
```

### VPN Connection Issues
```bash
# Check VPN gateway status
az network vpn-connection show --name <conn-name> --resource-group <rg> --query connectionStatus

# Check gateway connection
az network vpn-gateway show --name <gateway-name> --resource-group <rg>
```

## 8.5 Compute Issues

### VM Boot Failures
1. Check Boot Diagnostics in Azure Portal
2. Run serial console for error messages
3. Verify managed identity not causing issues

### AKS Cluster Issues
```bash
# Check cluster status
az aks show --name <cluster> --resource-group <rg>

# Get credentials
az aks get-credentials --name <cluster> --resource-group <rg>

# Check nodes
kubectl get nodes
kubectl describe node <node-name>

# View cluster events
kubectl get events --sort-by='.lastTimestamp'
```

### Azure Functions Issues
- Check Function App runtime version
- Verify app settings for connection strings
- Check Kudu/SCM site for logs

## 8.6 Database Issues

### Cosmos DB Connection
- Verify endpoint URL correct
- Check firewall settings
- Validate connection string format
- Ensure IP firewall allows client IP

### SQL Database Performance
- Check DTU utilization in portal
- Review query execution plans
- Verify indexing strategy

## 8.7 Performance Optimization Checklist

- [ ] Right-size underutilized VMs
- [ ] Enable auto-scaling where applicable
- [ ] Use Managed Disks instead of unmanaged
- [ ] Enable Azure Advisor recommendations
- [ ] Review Cost Management recommendations
- [ ] Use Azure CDN for static content

## 8.8 Diagnostic Commands

```bash
# Subscription health
az graph query -q "Resources | summarize count() by subscriptionId"

# Resource health
az resource show --id <resource-id> --query properties.health

# Activity log
az monitor activity-log list --resource-group <rg> --output table

# Advisor recommendations
az advisor recommendation list --output table
```