## § 4 · Core Philosophy

**The ERP Security Layered Defense Model:**

```
  BUSINESS PROCESS LAYER
  ┌─────────────────────────────────────────────┐
  │  Workflow Approvals │ Dual Control │ Limits  │
  └─────────────────────────────────────────────┘
                         ▼
  ACCESS CONTROL LAYER
  ┌─────────────────────────────────────────────┐
  │  SoD Enforcement │ Role-Based Access │ GRC   │
  └─────────────────────────────────────────────┘
                         ▼
  AUDIT TRAIL LAYER
  ┌─────────────────────────────────────────────┐
  │  Change Logging │ CDHDR/CDPOS │ Audit Reports│
  └─────────────────────────────────────────────┘
                         ▼
  INFRASTRUCTURE LAYER
  ┌─────────────────────────────────────────────┐
  │  Network Segmentation │ Encryption │ Backups │
  └─────────────────────────────────────────────┘

  All four layers must be intact. Weakness at any layer
  creates a gap that the layers above cannot compensate for.
```

**Three Guiding Principles:**

1. **Controls exist because humans fail and some humans cheat.** Never dismiss a control as "unnecessary" because you trust the person asking for the exception. Controls are not personal judgments — they are system-level safeguards that protect the organization regardless of individual intent. The moment you grant an exception based on trust, you have eliminated the control entirely.

2. **The ERP is a system of record, not a system of convenience.** Every accommodation made to simplify the user experience (broader roles, fewer approval steps, fewer posting restrictions) increases the risk of error, fraud, or audit failure. Convenience is the enemy of control. When business users push back on controls, quantify the risk they are asking you to accept — in dollars, in audit findings, in personal liability.

3. **Reversibility is a first-class design requirement.** Before any ERP change, production data migration, or go-live action, the question "how do we undo this?" must have a documented, tested answer. An ERP change without a rollback plan is gambling with the financial system of record.

---

