## 8. Standard Workflow

### 8.1 New Application Deployment

```
Phase 1: Namespace Setup
├── Create namespace manifest
├── Apply RBAC (ServiceAccount, Role, RoleBinding)
└── Set up resource quotas

Phase 2: Application Manifests
├── Create Deployment with security context
├── Add health probes
├── Set resource requests/limits
├── Create Service
└── Add ConfigMaps/Secrets

Phase 3: Networking
├── Create Ingress (if needed)
├── Apply NetworkPolicy
└── Configure DNS

Phase 4: Validation
├── Apply all manifests
├── Verify pods are running
├── Check health endpoints
└── Verify network connectivity

Phase 5: Monitoring
├── Set up Prometheus metrics
├── Configure alerts
└── Add log aggregation
```

### 8.2 Troubleshooting Flow

```
Pod Not Running
├── kubectl describe pod <name>
│   ├── Check Events for errors
│   └── Check Status conditions
├── kubectl logs <name>
│   ├── Application logs
│   └── Previous logs (--previous)
└── kubectl exec -it <name> -- sh
    └── Debug inside container

Network Issues
├── kubectl get endpoints <service>
├── kubectl get networkpolicy
└── Test with kubectl run test --rm -it --image=busybox
```

