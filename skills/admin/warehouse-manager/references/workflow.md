## § 7 · Standard Workflow

### 8.1 Receiving Operations

```
Phase 1: Pre-Arrival (Day before)
├── Review advance ship notices (ASNs) from vendors
├── Assign dock doors based on product type and volume
├── Prepare receiving bins and pallet positions
└── [✓ Done]: ASN reviewed, dock doors assigned
    [✗ FAIL]: Missing ASN → contact vendor, delay receiving until documentation arrives

Phase 2: Receiving Execution
├── Unload trailer and verify against ASN (count, condition)
├── Inspect for damage; document any exceptions with photos
├── Scan items into WMS and generate put-away instructions
├── Direct to put-away location (dock-to-stock or inspection hold)
└── [✓ Done]: All items scanned, accurate location assignment
    [✗ FAIL]: Discrepancy > 1% → hold for investigation, do not process

Phase 3: Post-Receiving
├── Reconcile WMS inventory vs. ASN
├── File all receiving documents for audit trail
├── Update vendor performance metrics
└── [✓ Done]: 100% reconciliation, documentation filed
```

### 8.2 Cycle Counting Program

```
Step 1: Classification
  → Run ABC analysis on current inventory
  → A-items: weekly count (top 20% by value)
  → B-items: monthly count (next 30%)
  → C-items: quarterly count (bottom 50%)

Step 2: Scheduling
  → Schedule A-counts on Monday (5 items per counter)
  → Schedule B-counts on Wednesday
  → Schedule C-counts on last week of quarter

Step 3: Execution
  → Counter pulls items, scans, records quantity
  → Supervisor verifies random 10% of counts
  → Enter variances into WMS with root cause

Step 4: Resolution
  → Investigate variances > $100 or > 2%
  → Adjust inventory if approved
  → Update cycle count accuracy metrics

[✓ Done]: 99.5% accuracy, zero unresolved variances > 30 days
```

---
