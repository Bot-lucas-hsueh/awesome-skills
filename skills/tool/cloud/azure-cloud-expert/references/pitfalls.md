# Examples

## 10.1 Azure CLI Commands

### 10.1.1 Resource Group and VM Commands

```bash
# Create resource group
az group create \
  --name rg-prod-webapp \
  --location eastus

# Create VM
az vm create \
  --resource-group rg-prod-webapp \
  --name vm-web-01 \
  --image UbuntuLTS \
  --size Standard_DS1_v2 \
  --admin-username azureuser \
  --generate-ssh-keys

# Open ports on VM
az vm open-port \
  --resource-group rg-prod-webapp \
  --name vm-web-01 \
  --port 80 --priority 100

# Start/Stop/Deallocate VM
az vm start --resource-group rg-prod-webapp --name vm-web-01
az vm stop --resource-group rg-prod-webapp --name vm-web-01
az vm deallocate --resource-group rg-prod-webapp --name vm-web-01
```

### 10.1.2 Web App Commands

```bash
# Create App Service Plan
az appservice plan create \
  --resource-group rg-prod-webapp \
  --name asp-prod \
  --sku S1 \
  --is-linux

# Create Web App
az webapp create \
  --resource-group rg-prod-webapp \
  --plan asp-prod \
  --name mywebapp-prod \
  --runtime "NODE|18-lts"

# Configure deployment slots
az webapp deployment slot create \
  --resource-group rg-prod-webapp \
  --name mywebapp-prod \
  --slot staging

# Swap slots
az webapp deployment slot swap \
  --resource-group rg-prod-webapp \
  --name mywebapp-prod \
  --slot staging
```

### 10.1.3 Storage Commands

```bash
# Create storage account
az storage account create \
  --resource-group rg-prod-webapp \
  --name stmyappprod \
  --sku Standard_LRS \
  --kind StorageV2

# Get connection string
az storage account show-connection-string \
  --resource-group rg-prod-webapp \
  --name stmyappprod

# Upload blob
az storage blob upload \
  --account-name stmyappprod \
  --container-name mycontainer \
  --name myfile.txt \
  --file ./myfile.txt

# Create SAS token
az storage blob generate-sas \
  --account-name stmyappprod \
  --container-name mycontainer \
  --name myfile.txt \
  --permissions r \
  --expiry 2024-12-31T23:59:59Z
```

### 10.1.4 Azure AD Commands

```bash
# Get current tenant info
az ad signed-in-user show

# List users
az ad user list --query "[].{displayName:displayName, mail:mail}"

# Create service principal
az ad sp create-for-rbac \
  --name http://myapp \
  --role Contributor \
  --scopes /subscriptions/xxx/resourceGroups/rg-prod-webapp

# Assign role
az role assignment create \
  --assignee http://myapp \
  --role Reader \
  --scope /subscriptions/xxx/resourceGroups/rg-prod-webapp
```

### 10.1.5 AKS Commands

```bash
# Create AKS cluster
az aks create \
  --resource-group rg-aks \
  --name myaks \
  --node-count 3 \
  --enable-addons monitoring \
  --generate-ssh-keys

# Get credentials
az aks get-credentials \
  --resource-group rg-aks \
  --name myaks

# Scale cluster
az aks scale \
  --resource-group rg-aks \
  --name myaks \
  --node-count 5

# Show cluster info
az aks show \
  --resource-group rg-aks \
  --name myaks
```

## 10.2 Terraform IaC Patterns

### 10.2.1 Resource Group and VM

```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "rg-${var.env}-${var.project}"
  location = var.location

  tags = {
    Environment = var.env
    Project     = var.project
  }
}

resource "azurerm_virtual_network" "main" {
  name                = "vnet-${var.env}"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}

resource "azurerm_subnet" "internal" {
  name                 = "snet-internal"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_network_interface" "main" {
  name                = "nic-${var.vm_name}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.internal.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "main" {
  name                = var.vm_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  size                = "Standard_DS1_v2"
  admin_username      = var.admin_username
  network_interface_ids = [azurerm_network_interface.main.id]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  admin_ssh_key {
    username   = var.admin_username
    public_key = file("~/.ssh/id_rsa.pub")
  }
}
```

### 10.2.2 App Service with Deployment Slot

```hcl
resource "azurerm_app_service_plan" "main" {
  name                = "asp-${var.env}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  kind                = "Linux"
  reserved            = true

  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "main" {
  name                = "app-${var.project}-${var.env}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id
  https_only          = true

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = "1"
    "NODE_ENV"                = "production"
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_app_service_slot" "staging" {
  name                = "staging"
  app_service_name    = azurerm_app_service.main.name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id
}
```

### 10.2.3 Azure SQL with Failover Group

```hcl
resource "azurerm_sql_server" "primary" {
  name                         = "sql-${var.project}-${var.env}"
  resource_group_name          = azurerm_resource_group.main.name
  location                     = azurerm_resource_group.main.location
  version                      = "12.0"
  administrator_login          = var.db_username
  administrator_login_password = var.db_password

  threat_detection_policy {
    enabled = true
    storage_endpoint           = azurerm_storage_account.primary.primary_blob_endpoint
    storage_account_access_key = azurerm_storage_account.primary.primary_access_key
  }
}

resource "azurerm_sql_database" "main" {
  name                = "sqldb-${var.project}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  server_name         = azurerm_sql_server.primary.name
  edition             = "Standard"
  collation           = "SQL_Latin1_General_CP1_CI_AS"
  max_size_bytes      = 5368709120

  threat_detection_policy {
    enabled = true
    storage_endpoint = azurerm_storage_account.primary.primary_blob_endpoint
  }
}

resource "azurerm_sql_failover_group" "main" {
  name                = "fog-${var.project}"
  resource_group_name = azurerm_resource_group.main.name
  server_name         = azurerm_sql_server.primary.name
  partner_servers     = [azurerm_sql_server.secondary.id]

  read_write_endpoint {
    failover_policy = "Automatic"
    failover_delay_in_seconds = 60
  }
}
```

### 10.2.4 AKS Cluster with Monitoring

```hcl
resource "azurerm_kubernetes_cluster" "main" {
  name                = "aks-${var.env}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  dns_prefix          = "aks-${var.env}"
  kubernetes_version  = var.kubernetes_version

  default_node_pool {
    name                = "default"
    node_count          = var.node_count
    vm_size             = "Standard_DS2_v2"
    enable_auto_scaling = true
    min_count           = 1
    max_count           = 5
  }

  identity {
    type = "SystemAssigned"
  }

  oms_agent {
    log_analytics_workspace_id = azurerm_log_analytics_workspace.main.id
  }

  azure_active_directory_role_based_access_control {
    managed                = true
    azure_rbac_enabled      = true
  }
}

resource "azurerm_log_analytics_workspace" "main" {
  name                = "log-${var.env}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}
```

## 10.3 ARM Template Snippets

### 10.3.1 Simple VM Deployment

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "adminUsername": {
      "type": "string",
      "metadata": {
        "description": "Admin username"
      }
    }
  },
  "variables": {
    "vmSize": "Standard_DS1_v2",
    "imagePublisher": "Canonical",
    "imageOffer": "UbuntuServer",
    "imageSKU": "18.04-LTS"
  },
  "resources": [
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2022-11-01",
      "name": "vm-web-01",
      "location": "[resourceGroup().location]",
      "properties": {
        "hardwareProfile": {
          "vmSize": "[variables('vmSize')]"
        },
        "osProfile": {
          "computerName": "vm-web-01",
          "adminUsername": "[parameters('adminUsername')]"
        },
        "storageProfile": {
          "imageReference": {
            "publisher": "[variables('imagePublisher')]",
            "offer": "[variables('imageOffer')]",
            "sku": "[variables('imageSKU')]",
            "version": "latest"
          }
        }
      }
    }
  ]
}
```

## 10.4 Deployment Configurations

### 10.4.1 Azure DevOps Pipeline for App Service

```yaml
trigger:
  branches:
    include:
      - main

variables:
  azureServiceConnection: 'my-azure-sp'
  appName: 'mywebapp-prod'
  slotName: 'staging'

stages:
  - stage: Deploy_Staging
    jobs:
      - deployment: DeployStaging
        environment: 'staging'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: $(azureServiceConnection)
                    appName: $(appName)
                    slotName: $(slotName)
                    package: $(Pipeline.Workspace)/drop/**/*.zip

  - stage: Smoke_Test
    dependsOn: Deploy_Staging
    jobs:
      - job: SmokeTest
        steps:
          - script: |
              curl -f $(appName)-$(slotName).azurewebsites.net/health

  - stage: Swap_to_Production
    dependsOn: Smoke_Test
    condition: succeeded()
    jobs:
      - job: Swap
        steps:
          - task: AzureAppServiceManage@0
            inputs:
              azureSubscription: $(azureServiceConnection)
              Action: 'Swap Slots'
              WebAppName: $(appName)
              SourceSlot: $(slotName)
```
