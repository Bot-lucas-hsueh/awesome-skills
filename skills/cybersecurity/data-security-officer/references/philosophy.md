## § 4 · Core Philosophy

### 4.1 Data Security Posture Model

```
DATA SECURITY POSTURE FRAMEWORK

┌──────────────────────────────────────────────────────────┐
│                    DISCOVER                              │
│  What data exists? Where? Who can access? Sensitivity?  │
│  Tools: AWS Macie, BigID, Varonis DSPM, Google DLP API  │
├──────────────────────────────────────────────────────────┤
│                   CLASSIFY                               │
│  4 Tiers: Restricted → Confidential → Internal → Public │
│  Auto-classify + human validation for edge cases        │
├──────────────────────────────────────────────────────────┤
│                    PROTECT                               │
│  Encryption (at-rest/transit/use) + DLP + Tokenization  │
│  Access control: least-privilege + ABAC + DAM monitoring │
├──────────────────────────────────────────────────────────┤
│                    MONITOR                               │
│  UEBA anomaly detection + audit trails + DLP alerts     │
│  Insider threat detection + data exfiltration patterns  │
├──────────────────────────────────────────────────────────┤
│                    RESPOND                               │
│  Automated breach detection → notification workflows    │
│  Forensic preservation → regulatory reporting → CAPA   │
└──────────────────────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Data you don't know about is data you can't protect**: Shadow data discovery must precede protection controls; automatic discovery must run continuously, not as a one-time project

2. **Classification drives everything**: Encryption strength, access control granularity, retention periods, and DLP sensitivity all derive from data classification

3. **Compliance is the minimum, trust is the goal**: Organizations that achieve regulatory compliance but ignore customer data expectations lose competitive advantage

---

