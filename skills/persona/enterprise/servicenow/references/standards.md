## §6 · Standards & Reference

### §6.1 Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Script Include | PascalCase | `IncidentUtils` |
| Business Rule | lowercase_underscore | `incident_sla_check` |
| Flow | Title Case | "Major Incident Response" |
| Custom Table | x_[scope]_[name] | `x_vendor_mgmt_vendor` |
| System Property | [scope].[property] | `x_app.timeout.seconds` |

### §6.2 Development Lifecycle

```
Phase 1: Requirements
├─ Business requirements
├─ Technical design
└─ Security review

Phase 2: Development
├─ Develop in scoped app
├─ Unit testing
└─ Peer review

Phase 3: Testing
├─ Functional testing
├─ Integration testing
└─ UAT sign-off

Phase 4: Deployment
├─ Update set/app package
├─ Preview in target
└─ Deploy with change approval
```

---
