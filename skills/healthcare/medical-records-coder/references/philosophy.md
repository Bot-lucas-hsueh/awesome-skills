## § 4 · Core Philosophy

### 4.1 DRG Assignment Flow

```
                    ┌─────────────────────┐
                    │ Review Medical Record│
                    │ ─────────────────── │
                    │ • H&P               │
                    │ • Discharge summary │
                    │ • Progress notes    │
                    │ • Operative report  │
                    │ • Labs/imaging      │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
┌───────────────┐    ┌─────────────────┐    ┌───────────────┐
│ Determine     │    │ Assign         │    │ Identify      │
│ Principal     │    │ Secondary      │    │ Procedures    │
│ Diagnosis     │    │ Diagnoses      │    │ (ICD-10-PCS)  │
│ ───────────── │    │ ────────────── │    │ ────────────── │
│ • Condition   │    │ • CCs          │    │ • Principal   │
│   after study │    │ • MCCs         │    │ • Secondary   │
│ • Reason for  │    │ • Chronic      │    │ • OR procedures│
│   admission   │    │   conditions   │    │               │
└───────┬───────┘    └────────┬────────┘    └───────┬───────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                    ┌─────────────────────┐
                    │ Assign MS-DRG        │
                    │ ─────────────────── │
                    │ • MDC assignment    │
                    │ • DRG within MDC    │
                    │ • Weight calculation│
                    │ • CMG for pediatric │
                    └─────────────────────┘
```

The principal diagnosis drives DRG assignment — it must be the condition established after study to be chiefly responsible for admission.

### 4.2 Guiding Principles

1. **Code What Is Documented**: The record is the source of truth — don't infer, don't assume
2. **Query for Clarification**: When documentation is ambiguous, the correct action is to query the physician
3. **Sequencing Matters**: Proper code sequence affects both quality metrics and reimbursement
4. **CC/MCC Impact**: A single CC can shift DRG weight by 20-50% — verify each potential CC/MCC

---

