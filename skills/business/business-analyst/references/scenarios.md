## § 8 · Scenario Examples

### Scenario 1: Requirements for New CRM Implementation

**Context:** Mid-size B2B company replacing legacy CRM with Salesforce.

**Discovery:**
- 15 stakeholder interviews (sales, marketing, customer success)
- 3 process observation sessions
- Document analysis of current system pain points

**Key Findings:**
- Sales reps spend 4 hours/week on manual data entry
- No visibility into pipeline health for management
- Customer data scattered across 3 systems
- Reporting takes 2 days to compile manually

**Deliverables:**
- BRD with 127 functional requirements
- AS-IS/TO-BE process models (BPMN)
- 89 user stories across 5 epics
- Data migration mapping (150 fields)
- UAT test scenarios (200+ cases)

**Results:**
- Requirements approved with 98% stakeholder agreement
- Project delivered on time, $50K under budget
- User adoption: 92% in first month
- Sales productivity: +25%

---

### Scenario 2: Process Optimization for Claims Processing

**Context:** Insurance company with 15-day average claims processing time.

**AS-IS Analysis:**
- BPMN model showing 47 process steps
- 8 handoffs between departments
- 23% of claims require rework
- Customer satisfaction: 3.1/5

**Root Causes:**
- Manual document routing
- No automated validation
- Inconsistent adjuster practices
- Missing integration with external data sources

**TO-BE Design:**
- Automated workflow routing
- OCR for document processing
- Rules engine for straight-through processing
- Self-service portal for customers

**Results:**
- Processing time: 15 days → 3 days (-80%)
- Rework rate: 23% → 5%
- Cost per claim: -40%
- CSAT: 3.1 → 4.4

---

### Scenario 3: Data Warehouse Requirements

**Context:** Retail chain building enterprise data warehouse for analytics.

**Requirements Elicitation:**
- 20+ business users interviewed
- 50+ report requirements catalogued
- Source system analysis (12 systems)
- Data quality assessment

**Data Modeling:**
- Dimensional model with 8 fact tables
- 35 dimension tables
- Slowly changing dimension strategy defined
- Data lineage documentation

**Key Requirements:**
- Near real-time inventory data (<15 min lag)
- 5-year historical data retention
- Self-service reporting capability
- Mobile dashboard access

**Results:**
- 40% reduction in report generation time
- Single source of truth established
- Self-service adoption: 70% of users
- $200K annual savings in manual reporting

---

### Scenario 4: Mobile App Feature Prioritization

**Context:** Fintech startup with 50+ feature requests for mobile app.

**Approach:**
- User story mapping workshop
- MoSCoW prioritization
- Kano model analysis
- Technical complexity assessment

**Prioritization Framework:**
| Feature | User Value | Business Value | Complexity | Priority |
|---------|-----------|----------------|------------|----------|
| Biometric login | High | Medium | Low | Must |
| Budget alerts | High | High | Medium | Must |
| Investment tracking | Medium | High | High | Should |
| Social sharing | Low | Low | Medium | Won't |

**MVP Scope:** 12 must-have features
**Roadmap:** 3 releases over 6 months

**Results:**
- MVP delivered in 8 weeks
- App store rating: 4.7/5
- User retention: +35%
- Clear roadmap reduced stakeholder conflicts

---

### Scenario 5: Regulatory Compliance System

**Context:** Bank implementing new KYC/AML system for regulatory compliance.

**Complexity:**
- 5 regulatory jurisdictions
- 200+ business rules
- Integration with 8 internal systems
- 3 external data providers

**Requirements Approach:**
- Rule traceability matrix
- Regulatory requirement mapping
- Risk-based testing strategy
- Audit trail specifications

**Key Deliverables:**
- 340 functional requirements
- 156 business rules documented
- Compliance checklist with evidence requirements
- Regulatory mapping document

**Results:**
- Zero findings in regulatory audit
- 60% reduction in KYC processing time
- $2M fine avoidance
- Process standardization across regions

---
