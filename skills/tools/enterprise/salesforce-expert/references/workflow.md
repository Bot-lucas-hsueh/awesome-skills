# Standard Workflow

## 8.1 Getting Started

```
Phase 1: Environment Setup
├── Install Salesforce CLI (sf)
├── Set up development environment (VS Code + extensions)
├── Configure Salesforce org authentication
├── Enable Dev Hub (for scratch orgs)
└── Install required plugins

Phase 2: Project Setup
├── Create project with manifest
sf project generate --name my-project --manifest
├── Authorize Dev Hub
sf org login web --set-default-dev-hub
├── Retrieve metadata
sf project retrieve start --manifest config/package.xml
└── Configure .sfdx/sfdx-config.json

Phase 3: Development
├── Create Apex classes and triggers
├── Build Lightning components
├── Configure flows and validations
├── Write tests with >75% coverage
└── Use scratch orgs for development

Phase 4: Deployment
├── Run all tests
├── Deploy to sandbox for UAT
├── Run regression tests
├── Deploy to production
└── Monitor deployment status
```

## 8.2 Common Workflows

### Apex Development

```bash
# Create project
sf project generate --name my-sfdx-project

# Create Apex class
sf generate apex class --name AccountService --template Standard

# Create Apex trigger
sf generate apex trigger --name AccountTrigger --sobject Account

# Create test class
sf generate apex class --name AccountServiceTest --template ApexUnitTest

# Execute anonymous Apex
sf apex run --file scripts/run.apex

# Run tests
sf apex run test --class-names AccountServiceTest --code-coverage

# Open in browser
sf org open
```

### Lightning Web Component Development

```bash
# Create LWC
sf generate lightning component --name myComponent --type lwc

# Create Apex controller for LWC
sf generate apex class --name MyComponentController

# Deploy to org
sf project deploy start --source-dir force-app

# Open Lightning App Builder
sf org open --path /lightning/setup/home
```

### Data Management

```bash
# Export data using query
sf data export tree \
  --query "SELECT Id, Name, Industry FROM Account LIMIT 100" \
  --output-dir ./data

# Import data
sf data import tree --files ./data/Account.json

# Use Data Loader via CLI
sf data bulk export --query "SELECT Id FROM Account"

# Delete records
sf data delete record --sobject Account --record-id "001XX000003XXXX"
```

### Deployment Workflow

```bash
# 1. Validate deployment (quick check)
sf project deploy validate \
  --manifest config/package.xml \
  --target-org production \
  --test-level RunLocalTests

# 2. Deploy (after validation)
sf project deploy start \
  --manifest config/package.xml \
  --target-org production \
  --test-level RunLocalTests \
  --wait 60

# 3. Monitor deployment
sf project deploy report --job-id 0AfXX000000XXXX

# 4. Rollback on failure
sf project deploy cancel --job-id 0AfXX000000XXXX
```

## 8.3 CI/CD Pipeline

### GitHub Actions Workflow

```yaml
name: Salesforce CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install Salesforce CLI
        run: |
          npm install -g sfdx-cli
          sf version

      - name: Authenticate with Dev Hub
        run: |
          echo "$JWT_KEY" > server.key
          sf org login jwt \
            --client-id $CLIENT_ID \
            --jwt-key-file server.key \
            --username $DEV_HUB_USERNAME \
            --set-default-dev-hub

      - name: Create Scratch Org
        run: |
          sf org create scratch \
            --definition-file config/project-scratch-def.json \
            --set-default-username \
            --alias ci-scratch

      - name: Push Source
        run: sf project deploy start \
          --source-dir force-app \
          --target-org ci-scratch

      - name: Run Tests
        run: sf apex run test \
          --target-org ci-scratch \
          --test-level RunLocalTests \
          --codecoverage

      - name: Delete Scratch Org
        if: always()
        run: sf org delete scratch --target-org ci-scratch --no-prompt

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Salesforce CLI
        run: npm install -g sfdx-cli

      - name: Authenticate Production
        run: |
          echo "$JWT_KEY" > server.key
          sf org login jwt \
            --client-id $CLIENT_ID \
            --jwt-key-file server.key \
            --username $PROD_USERNAME \
            --set-default-username

      - name: Deploy to Production
        run: |
          sf project deploy start \
            --manifest config/package.xml \
            --target-org production \
            --test-level RunLocalTests \
            --wait 60
```

## 8.4 Scratch Org Configuration

```json
{
  "orgName": "My Project",
  "edition": "Developer",
  "features": [
    "AuthorApex",
    "Communities",
    "LiveAgent",
    "Workflow",
    "ProcessBuilder",
    "API",
    "AddOnProducts"
  ],
  "settings": {
    "lightningExperienceSettings": {
      "enableLightningExperience": true
    },
    "securitySettings": {
      "enableAdminLoginAsAny": true
    },
    "mobileSettings": {
      "enableMobileApp": true
    },
    "experienceBundleSettings": {
      "enableExperienceBundles": true
    }
  },
  "objectSettings": {
    "opportunity": {
      "sharingModel": "ReadWrite"
    }
  }
}
```

## 8.5 Source Tracking

```bash
# Pull latest changes
sf project retrieve start --source-dir force-app

# Convert source to metadata
sf project convert source --output-dir metadata

# Convert metadata to source
sf project convert metadata --output-dir force-app

# Deploy with source tracking
sf project deploy start \
  --source-dir force-app \
  --target-org my-sandbox \
  --ignore-conflicts

# Show differences
sf project diff \
  --source-dir force-app \
  --target-org my-sandbox
```

## 8.6 Package Development

```bash
# Create unlocked package
sf package create \
  --name my-package \
  --package-type Unlocked \
  --description "My package"

# Add to package
sf package version create \
  --package my-package \
  --installation-key-bypass \
  --wait 30

# Install package
sf package install \
  --package my-package@1.0.0 \
  --target-org my-sandbox \
  --publish-wait 30

# List installed packages
sf package installed list --target-org my-sandbox
```
