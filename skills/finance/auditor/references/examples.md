## § 9 · Examples

### Example 1: Financial Statement Audit — Revenue Recognition

**Context:** Tech startup preparing for IPO needs revenue audit procedures

**User Input:**
> "We're auditing a SaaS company with $50M ARR. They have multi-element arrangements with subscription and professional services. Design a risk-based audit program for revenue."

**Expert Response:**

**1. Risk Assessment (AS 2110 / SAS 145):**

| Risk Factor | Assessment | Rationale |
|-------------|------------|-----------|
| Inherent Risk | High | Complex multi-element arrangements, judgment in allocation |
| Fraud Risk | High | Pressure to meet growth targets, IPO timeline |
| Control Risk | Medium | New ERP system implemented 6 months ago |
| Significant Risk | Yes | Revenue recognition is presumed significant risk per AS 2110 |

**2. Fraud Risk Procedures (AS 2401):**

```
Fraud Triangle Analysis:
┌─────────────┬─────────────────────────────────────────────┐
│ Pressure    │ IPO timeline, VC expectations, burn rate    │
│ Opportunity │ Complex arrangements, new system, overrides │
│ Rationalize │ "Everyone does it," growth at all costs     │
└─────────────┴─────────────────────────────────────────────┘

Specific Fraud Procedures:
□ Journal entry testing (unusual accounts, round numbers, off-hours)
□ Contract review for side agreements
□ Revenue cutoff testing (quarter-end shipments/activations)
□ Related party transaction review
□ Management representation letter
```

**3. Substantive Testing Program:**

| Procedure | Assertion | Sample Size | Evidence |
|-----------|-----------|-------------|----------|
| Contract review (new customers) | Occurrence, Accuracy | 25 | Signed contracts, SoW |
| Invoice to contract matching | Accuracy, Cutoff | 60 (MUS) | Invoices, delivery evidence |
| Deferred revenue reconciliation | Completeness, Valuation | Full population | GL detail, subledger |
| Revenue cutoff | Cutoff | 15 before/after YE | Shipping logs, activation timestamps |
| Related party sales | Occurrence | All >$100K | Beneficial ownership verification |

**4. Multi-Element Arrangement Testing:**

```
For each arrangement with multiple deliverables:
1. Verify VSOE/BESP exists for each element
2. Recalculate allocation percentages
3. Confirm delivery of each element
4. Verify revenue recognition timing per ASC 606/IFRS 15
```

---

### Example 2: SOX 404 Compliance Audit

**Context:** Public company needs SOX 404 readiness assessment

**User Input:**
> "We're a $200M revenue manufacturer preparing for our first SOX 404 audit. Help us design our ICFR program and identify what controls we need."

**Expert Response:**

**1. Top-Down Risk Assessment (AS 2201):**

```
Entity-Level Controls (ELCs):
┌─────────────────────────────────────────────────────────────┐
│ Control Environment                                         │
│ • Tone at the top (CEO/CFO messages)                        │
│ • Code of conduct and acknowledgments                       │
│ • Board independence and audit committee                    │
│ • Organizational structure                                  │
│                                                             │
│ Risk Assessment Process                                     │
│ • Risk assessment methodology                               │
│ • Fraud risk assessment                                     │
│ • Change management process                                 │
│                                                             │
│ Information & Communication                                 │
│ • Financial reporting close process                         │
│ • Internal communication channels                           │
│ • External reporting procedures                             │
│                                                             │
│ Monitoring Activities                                       │
│ • Internal audit function                                   │
│ • Management review controls                                │
│ • Self-assessment program                                   │
└─────────────────────────────────────────────────────────────┘
```

**2. Process-Level Controls Matrix:**

| Process | Key Control | Control Type | Frequency | Owner |
|---------|-------------|--------------|-----------|-------|
| Revenue | Credit approval before shipment | Preventive | Per order | Sales Ops |
| Revenue | Revenue recognition review | Detective | Monthly | Controller |
| Procurement | Purchase order approval (3-way match) | Preventive | Per PO | Procurement |
| Procurement | Vendor master file changes | Preventive | As needed | CFO approval |
| Payroll | Timecard manager approval | Preventive | Bi-weekly | Department Mgr |
| Payroll | Payroll register review | Detective | Bi-weekly | HR Director |
| Inventory | Physical inventory counts | Preventive | Annual | Ops Manager |
| Inventory | Inventory reserve calculation | Detective | Quarterly | Controller |
| Financial Close | Account reconciliation review | Detective | Monthly | Accounting Mgr |
| Financial Close | JE approval (threshold-based) | Preventive | Per entry | VP Finance |

**3. IT General Controls (ITGCs):**

```
Access Controls:
┌─────────────────────────────────────────────────────────────┐
│ Logical Access                                              │
│ • User provisioning/deprovisioning process                  │
│ • Privileged access management                              │
│ • Periodic access reviews (quarterly)                       │
│ • Password policies                                         │
│                                                             │
│ Change Management                                           │
│ • Change approval workflow                                  │
│ • Testing requirements before production                    │
│ • Emergency change procedures                               │
│                                                             │
│ Computer Operations                                         │
│ • Backup and recovery testing                               │
│ • Batch job monitoring                                      │
│ • Incident response procedures                              │
└─────────────────────────────────────────────────────────────┘
```

**4. Testing Approach:**

| Control | Test Procedure | Sample | Pass Criteria |
|---------|---------------|--------|---------------|
| Credit approval | Inspect signed credit approvals | 25 | All have documented approval |
| 3-way match | Test invoice, PO, receipt matching | 25 | No unmatched items without approval |
| JE approval | Inspect JE supporting documentation | 25 | All >$10K have VP Finance signature |
| Access reviews | Inspect quarterly access review | 4 quarters | All reviews completed, exceptions resolved |

**5. Material Weakness Indicators:**

🔴 **Red Flags (likely MW):**
- Restatement of previously issued financial statements
- Evidence of fraud (material or immaterial) by senior management
- Ineffective audit committee oversight
- Identification of material misstatement not caught by controls

🟡 **Yellow Flags (possible SD):**
- Late/missing account reconciliations
- Unreconciled differences in key accounts
- ITGC deficiencies in financially relevant systems

---

### Example 3: Internal Audit — Fraud Risk Assessment

**Context:** Manufacturing company suspects procurement fraud

**User Input:**
> "We've noticed unusual patterns in our procurement process. Vendors are being added rapidly, and some invoices seem inflated. Conduct a fraud risk assessment."

**Expert Response:**

**1. Fraud Risk Assessment Framework (ACFE):**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FRAUD TRIANGLE ANALYSIS                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐           │
│  │   PRESSURE    │  │  OPPORTUNITY  │  │ RATIONALIZAT. │           │
│  │               │  │               │  │               │           │
│  │ • Cost cutting│  │ • Weak seg.   │  │ • "Everyone   │           │
│  │   mandates    │  │   of duties   │  │   does it"    │           │
│  │ • Bonus       │  │ • Override    │  │ • "I deserve  │           │
│  │   targets     │  │   authority   │  │   it"         │           │
│  │ • Personal    │  │ • No vendor   │  │ • "Company    │           │
│  │   financial   │  │   verification│  │   can afford  │           │
│  │   problems    │  │ • Inadequate  │  │   it"         │           │
│  │               │  │   monitoring  │  │               │           │
│  └───────────────┘  └───────────────┘  └───────────────┘           │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**2. Data Analytics Procedures:**

```python
# Benford's Law Analysis (First Digit Test)
# Expected distribution: 30.1%, 17.6%, 12.5%, 9.7%, 7.9%, 6.7%, 5.8%, 5.1%, 4.6%

# Red Flag Indicators:
□ Vendors with sequential invoice numbers
□ Invoices just below approval thresholds
□ Round-dollar amounts on non-labor charges
□ Duplicate invoice numbers
□ Weekend/holiday invoice dates
□ Vendors with only PO Box addresses
□ Employees and vendors with matching addresses
```

**3. Procurement Fraud Testing:**

| Test | Procedure | Red Flag |
|------|-----------|----------|
| Vendor analysis | Compare vendor list to employee addresses | Shared addresses/phones |
| Invoice pattern | Analyze invoice amounts vs. Benford's Law | Significant deviation |
| Vendor concentration | Top 10 vendors as % of total spend | >80% concentration |
| Duplicate payments | Match invoice numbers + amounts | Duplicate payments |
| Ghost vendors | Verify vendor existence (D&B, web search) | No business presence |
| Split purchases | Identify purchases just under approval limit | Pattern of $4,900 when limit is $5,000 |
| PO sequencing | Analyze PO number patterns | Sequential POs to same vendor |

**4. Interview Protocol:**

```
Interview Strategy:

1. Procurement Team (Information gathering)
   - Walk through vendor onboarding process
   - Understand approval authorities
   - Identify process pain points

2. Accounts Payable (Documentation review)
   - Invoice processing workflow
   - Exception handling procedures
   - Vendor master file maintenance

3. Vendor (External confirmation - if appropriate)
   - Confirm contract terms
   - Verify bank account information
   - Confirm payment history

4. Management (Assessment)
   - Knowledge of vendor relationships
   - Oversight of procurement process
   - Response to identified issues
```

**5. Investigation Report Template:**

```
FINDING: Potential Procurement Fraud

Criteria: Procurement policies require competitive bidding for purchases >$25,000
          and segregation of duties between vendor setup and payment approval.

Condition: Our testing identified:
          • 15 vendors added in last 6 months without proper due diligence
          • $450K in invoices to vendor "ABC Consulting" with no contract on file
          • Same employee creating vendor master record and approving payments

Cause: Inadequate segregation of duties and lack of vendor verification process.

Effect: Risk of payments to fictitious vendors or inflated invoices. Estimated
       exposure: $450K for identified items; potential additional exposure unknown.

Recommendation:
1. Immediate: Freeze payments to unverified vendors pending investigation
2. Short-term: Implement vendor verification process (D&B, bank confirmation)
3. Long-term: Segregate vendor setup from payment approval duties
4. Ongoing: Implement continuous monitoring using data analytics
```

---

### Example 4: Compliance Audit — GDPR Data Privacy

**Context:** EU subsidiary needs GDPR compliance audit

**User Input:**
> "We need to audit our GDPR compliance for our EU operations. What should our audit program cover?"

**Expert Response:**

**1. GDPR Compliance Framework:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GDPR KEY PRINCIPLES                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  1. LAWFULNESS, FAIRNESS, TRANSPARENCY                              │
│     • Legal basis for processing (consent, contract, legitimate)    │
│     • Privacy notices and transparency                              │
│                                                                      │
│  2. PURPOSE LIMITATION                                              │
│     • Collection for specified, explicit, legitimate purposes       │
│     • No further incompatible processing                            │
│                                                                      │
│  3. DATA MINIMIZATION                                               │
│     • Adequate, relevant, limited to necessary                      │
│                                                                      │
│  4. ACCURACY                                                        │
│     • Ensure personal data is accurate and current                  │
│     • Right to rectification                                          │
│                                                                      │
│  5. STORAGE LIMITATION                                              │
│     • Kept only as long as necessary                                │
│     • Retention policies and deletion procedures                    │
│                                                                      │
│  6. INTEGRITY & CONFIDENTIALITY                                     │
│     • Appropriate security measures                                 │
│     • Pseudonymization and encryption                               │
│                                                                      │
│  7. ACCOUNTABILITY                                                  │
│     • Demonstrate compliance                                        │
│     • Records of processing activities                              │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**2. Audit Program:**

| Control Area | Test Procedure | Evidence |
|--------------|---------------|----------|
| **Legal Basis** | Review privacy notices for legal basis disclosure | Privacy policies, consent records |
| **Consent** | Verify consent is freely given, specific, informed, unambiguous | Consent forms, opt-in records |
| **Data Mapping** | Validate Records of Processing Activities (ROPA) | ROPA documentation, system inventories |
| **Data Subject Rights** | Test DSAR process (access, rectification, erasure, portability) | DSAR logs, response times |
| **Security Measures** | Assess technical and organizational security measures | Security policies, access logs, encryption |
| **Data Breach Response** | Review breach notification procedures and testing | Incident response plan, test records |
| **DPO Appointment** | Verify Data Protection Officer appointment (if required) | DPO appointment, role description |
| **International Transfers** | Assess mechanisms for data transfers outside EEA | SCCs, adequacy decisions, BCRs |
| **Privacy by Design** | Evaluate privacy impact assessments (DPIA) | DPIA records, project documentation |
| **Third Party Management** | Review processor agreements and due diligence | DPA agreements, security assessments |

**3. Data Subject Rights Testing:**

```
DSAR Response Testing:
┌─────────────────────────────────────────────────────────────┐
│ Right           │ Timeline    │ Test Approach              │
├─────────────────┼─────────────┼────────────────────────────┤
│ Access          │ 30 days     │ Submit test request;       │
│                 │ (extendable)│ verify data completeness   │
│ Rectification   │ 30 days     │ Submit correction; verify  │
│                 │             │ change implemented         │
│ Erasure         │ 30 days     │ Request deletion; verify   │
│ (Right to be    │             │ data removal across systems│
│  forgotten)     │             │                            │
│ Portability     │ 30 days     │ Request data export;       │
│                 │             │ verify machine-readable    │
│ Restriction     │ No delay    │ Request processing limit;  │
│                 │             │ verify system flags        │
│ Objection       │ No delay    │ Submit objection; verify   │
│                 │             │ processing cessation       │
└─────────────────┴─────────────┴────────────────────────────┘
```

**4. Penalty Assessment:**

| Violation Type | Maximum Penalty | Examples |
|----------------|-----------------|----------|
| Tier 1 (Less severe) | €10M or 2% global turnover | Records, privacy by design, security |
| Tier 2 (Severe) | €20M or 4% global turnover | Core principles, data subject rights, transfers |

---

### Example 5: Internal Controls — IT General Controls Review

**Context:** Company implementing new ERP system needs ITGC assessment

**User Input:**
> "We're implementing SAP S/4HANA. Help us design IT general controls and prepare for SOX ITGC audit."

**Expert Response:**

**1. IT General Controls Framework (COBIT 2019 / NIST):**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ITGC CONTROL CATEGORIES                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  1. ACCESS CONTROLS                                                  │
│     ├─ User Access Management (Provisioning/Deprovisioning)         │
│     ├─ Privileged Access Management (Superuser controls)            │
│     ├─ Periodic Access Reviews (Recertification)                    │
│     └─ Authentication & Authorization (MFA, SSO)                    │
│                                                                      │
│  2. CHANGE MANAGEMENT                                                │
│     ├─ Change Request & Approval (Authorization workflow)           │
│     ├─ Testing Requirements (UAT, regression testing)               │
│     ├─ Emergency Change Procedures (Post-implementation review)     │
│     └─ Segregation of Duties (Dev/Test/Prod separation)             │
│                                                                      │
│  3. COMPUTER OPERATIONS                                              │
│     ├─ Batch Job Scheduling & Monitoring                            │
│     ├─ Backup & Recovery Procedures                                 │
│     ├─ Incident Management & Problem Resolution                     │
│     └─ Business Continuity / Disaster Recovery                      │
│                                                                      │
│  4. PROGRAM DEVELOPMENT                                              │
│     ├─ System Development Lifecycle (SDLC)                          │
│     ├─ Data Migration Controls (Cutover procedures)                 │
│     ├─ Interface Controls (Input/output validation)                 │
│     └─ Master Data Management (Approval workflows)                  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**2. SAP S/4HANA Specific Controls:**

| SAP Module | Key Control | Control Activity |
|------------|-------------|------------------|
| Security (GRC) | SoD conflict management | GRC Access Control for rule set validation |
| Basis | Transport management | STMS approval workflow, production lock |
| FI/CO | Journal entry posting | FB50 authorization, posting period control |
| MM | Purchase order approval | Release strategy workflow, approval limits |
| SD | Credit limit enforcement | Credit management automatic hold |
| HR | Payroll processing | HR authorizations, retroactive calc controls |

**3. SAP Implementation Controls:**

```
Implementation Phase Controls:

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 1: DESIGN & BUILD                                              │
├─────────────────────────────────────────────────────────────────────┤
│ • Security role design aligned with SoD matrix                      │
│ • Custom development standards and code review                      │
│ • Data migration strategy and validation controls                   │
│ • Integration design and error handling                             │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 2: TESTING                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ • Unit testing for custom developments                              │
│ • Integration testing with financial controls validation            │
│ • User acceptance testing with business process owners              │
│ • Security testing (penetration testing, SoD analysis)              │
│ • Performance testing and stress testing                            │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 3: DATA MIGRATION                                              │
├─────────────────────────────────────────────────────────────────────┤
│ • Data cleansing and validation procedures                          │
│ • Cutover plan with go/no-go criteria                               │
│ • Reconciliation of legacy to SAP balances                          │
│ • Parallel run and results comparison                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 4: GO-LIVE & STABILIZATION                                     │
├─────────────────────────────────────────────────────────────────────┤
│ • Hypercare support and issue tracking                              │
│ • Post-implementation review                                        │
│ • Control effectiveness testing                                     │
│ • Documentation updates and training                                │
└─────────────────────────────────────────────────────────────────────┘
```

**4. Segregation of Duties Matrix:**

| Function | Create Vendor | Process Invoice | Post Payment | Reconcile Bank |
|----------|---------------|-----------------|--------------|----------------|
| AP Clerk | ✗ | ✓ | ✗ | ✗ |
| AP Manager | ✓ | ✗ | ✗ | ✗ |
| Treasury | ✗ | ✗ | ✓ | ✗ |
| Accounting | ✗ | ✗ | ✗ | ✓ |

**5. ITGC Testing Program:**

| Control | Test Procedure | Frequency | Evidence |
|---------|---------------|-----------|----------|
| User provisioning | Inspect user access requests and approvals | Quarterly | Access request forms |
| Privileged access | Review SAP_ALL/superuser usage logs | Monthly | SUIM reports, session logs |
| Access recertification | Validate manager access reviews | Quarterly | Signed recertification reports |
| Change approval | Inspect transport requests and approvals | Quarterly | Change tickets, STMS logs |
| Emergency changes | Review emergency change log and approvals | Quarterly | Emergency change log |
| Backup testing | Verify backup restoration testing | Annual | Restoration test results |
| Batch monitoring | Review batch job logs and error handling | Daily | SM37 logs, exception reports |

---
