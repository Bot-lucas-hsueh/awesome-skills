# Standards & Reference

## 7.1 Official Documentation

- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [Pulumi Registry](https://www.pulumi.com/registry/)
- [Pulumi API Reference](https://www.pulumi.com/docs/reference/)
- [Pulumi GitHub](https://github.com/pulumi/pulumi)
- [Pulumi Examples](https://github.com/pulumi/examples)

## 7.2 Project Structure

```
my-infra/
├── Pulumi.yaml
├── Pulumi.dev.yaml
├── Pulumi.prod.yaml
├── index.ts                 # Main entry
├── tsconfig.json
├── package.json
└── infrastructure/
    ├── vpc/
    │   ├── index.ts
    │   └── config.ts
    ├── compute/
    │   ├── index.ts
    │   └── config.ts
    └── databases/
        ├── index.ts
        └── config.ts
```

## 7.3 Configuration Reference

```typescript
// Pulumi.yaml
name: my-infra
runtime: typescript
description: Infrastructure as Code

// Stack config (Pulumi.dev.yaml)
config:
  environment:
    value: development
  aws:region:
    value: us-west-2
```

## 7.4 Common Providers

| Provider | Package | Use Case |
|----------|---------|---------|
| AWS | `@pulumi/aws` | AWS resources |
| Azure | `@pulumi/azure-native` | Azure resources |
| GCP | `@pulumi/gcp` | Google Cloud |
| Kubernetes | `@pulumi/kubernetes` | K8s resources |
| Docker | `@pulumi/docker` | Containers |

## 7.5 Core Functions

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Get config
const config = new pulumi.Config();
const environment = config.require("environment");

// Create resources
const vpc = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
    tags: { Name: `${environment}-vpc` }
});

// Export outputs
export const vpcId = vpc.id;
export const vpcCidr = vpc.cidrBlock;
```

## 7.6 Version Compatibility

| Pulumi Version | TypeScript | Node.js | Notes |
|---------------|-----------|---------|-------|
| 3.x | 4.x-5.x | 18+ | Current |
| 2.x | 3.x-4.x | 14+ | Legacy |

## 7.7 CLI Commands

| Command | Description |
|---------|-------------|
| `pulumi new` | Create new project |
| `pulumi up` | Deploy changes |
| `pulumi preview` | Preview changes |
| `pulumi destroy` | Remove resources |
| `pulumi stack ls` | List stacks |
| `pulumi config get` | Get config value |
