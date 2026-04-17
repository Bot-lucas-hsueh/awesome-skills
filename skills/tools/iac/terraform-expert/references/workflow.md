## 8. Standard Workflow

### 8.1 New Infrastructure

```
Phase 1: Design
├── Identify required resources
├── Map dependencies
├── Design module structure
└── Plan state management

Phase 2: Module Creation
├── Create module structure
├── Define variables with validation
├── Write resource configurations
├── Add outputs
└── Document in README

Phase 3: Environment Configuration
├── Create environment directory
├── Configure backend
├── Instantiate modules
├── Set environment variables
└── Plan and apply

Phase 4: CI/CD Integration
├── Add terraform fmt check
├── Add terraform plan step
├── Add approval gate
└── Add terraform apply
```

### 8.2 State Management

```
Step 1: Initialize Backend
├── Choose backend (S3, GCS, Azure Blob)
├── Configure state locking (DynamoDB, etc.)
└── Migrate existing state if needed

Step 2: Protect State
├── Enable encryption
├── Enable versioning
├── Restrict access with IAM
└── Enable state locking

Step 3: Handle Drift
├── Run terraform plan regularly
├── Review plan for unintended changes
├── Discuss manual changes with team
└── Apply to reconcile
```

