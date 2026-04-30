# Standard Workflow

## 8.1 Project Initialization

```
Phase 1: Setup
├── Install Pulumi CLI
├── Configure cloud credentials
├── Choose language (TypeScript/Python/Go/C#)
└── Create project

Phase 2: Structure
├── Create stack (dev, staging, prod)
├── Organize by component
├── Set up shared configs
└── Configure secrets

Phase 3: Development
├── Write infrastructure code
├── Test locally
├── Review preview
└── Deploy to dev

Phase 4: Production
├── Peer review
├── Deploy to staging
├── Test thoroughly
└── Deploy to production
```

## 8.2 Deployment Workflow

```bash
# Preview changes
pulumi preview

# Deploy changes
pulumi up

# With specific stack
pulumi up --stack production

# Destroy resources
pulumi destroy

# Refresh state
pulumi refresh
```

## 8.3 Stack Management

```bash
# Create stack
pulumi stack init staging

# Set config
pulumi config set environment staging
pulumi config set aws:region us-west-2

# Secret config
pulumi config set --secret db-password "supersecret"

# View config
pulumi config
pulumi config get environment
```

## 8.4 CI/CD Integration

```yaml
# GitHub Actions
name: Deploy
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pulumi/actions@v4
        with:
          command: preview
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

## 8.5 Testing

```typescript
// Unit test with mocks
import * as assert from "assert";

pulumi.runtime.setMocks({
    newResource: (args: pulumi.runtime.MockResourceArgs) => {
        return {
            id: `${args.name}-id`,
            state: { ...args.inputs },
        };
    },
    call: () => ({})
});

// Integration test
const vpc = new aws.ec2.Vpc("test-vpc", { cidrBlock: "10.0.0.0/16" });
export const vpcId = vpc.id;
```
