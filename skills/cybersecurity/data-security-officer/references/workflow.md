## 8. Standard Workflow

### 8.1 Data Security Program Launch

```
Phase 1: Data Discovery & Inventory (数据发现与清单)
├── Deploy automated discovery: AWS Macie (S3), BigID (databases), Varonis (file shares)
├── Scan all data stores: on-prem, cloud, SaaS applications
├── Identify "shadow data": dev/test copies with production PII
├── Generate data map: where is PII, who can access, what regulation applies
└── [✓ Done]: Data inventory covering >95% of known data stores; risk heat map complete
    [✗ FAIL]: Major unknown data stores remain → expand scanner scope before proceeding

Phase 2: Classification Implementation (分类实施)
├── Define 4-tier taxonomy: Restricted / Confidential / Internal
├── Configure auto-classification rules in Purview or equivalent
├── Train classifiers on domain-specific sensitive data patterns
├── Validate with manual review: 100 samples per classification tier
└── [✓ Done]: >90% auto-classification accuracy; human review workflow for edge cases

Phase 3: Protection Controls Deployment (保护控制部署)
├── Apply encryption policy per tier (§7.2 framework)
├── Implement DLP policies: start with audit-only, promote to block after 30-day tuning
├── Deploy DAM on production databases with PII
├── Implement least-privilege access review (remove orphaned accounts + over-privileged roles)
└── [✓ Done]: Zero Restricted data without encryption; DLP false positive rate < 5%

Phase 4: Monitoring & Response (监控与响应)
├── UEBA baseline: 30 days normal behavior → alert on 3σ deviations
├── Configure automated breach detection with notification workflow
├── Test incident response: tabletop exercise; simulate breach → notification timeline
└── [✓ Done]: MTTD < 24h for data exfiltration; GDPR 72h notification capability verified
```

### 8.2 Data Subject Rights (DSR) Workflow

```
Trigger: SAR (Subject Access Request) received

Day 0: Intake & Verification
├── Verify requester identity (government ID or equivalent)
├── Log request in DSR tracking system (GDPR: 30-day clock starts)
└── [✓ Done]: Identity verified; ticket created; deadline = Day 30 (GDPR)

Days 1-20: Data Discovery
├── Query all data stores using BigID or equivalent
├── Include backups, archives, third-party processors
├── Compile: what data, where stored, how used, who shared with
└── [✓ Done]: Complete data inventory for this subject

Days 21-28: Response Preparation
├── Redact third-party PII from response (cannot expose other subjects)
├── Apply legal exceptions (law enforcement data, trade secrets)
├── Package in portable format (CSV, JSON per Art. 20 portability)
└── [✓ Done]: Response package ready; legal review complete

Day 29: Delivery
├── Deliver via secure channel (encrypted email or portal)
├── Document delivery in audit log
└── [✓ Done]: Response delivered within 30 days (GDPR)
    [✗ FAIL]: Cannot complete → notify subject + extend 60 days (with documented reason)
```

---

