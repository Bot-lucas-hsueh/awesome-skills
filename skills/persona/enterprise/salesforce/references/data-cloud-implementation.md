# Data Cloud Implementation Guide

## Overview

Salesforce Data Cloud is a hyperscale real-time customer data platform (CDP) that unifies data from any source to create a single view of the customer.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES                                │
├─────────────────────────────────────────────────────────────────┤
│  Salesforce CRM | Marketing Cloud | Web Analytics | ERP | IoT   │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    INGESTION LAYER                              │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  Batch API   │  │  Streaming   │  │  Connectors          │  │
│  │  (Bulk load) │  │  API         │  │  (Pre-built)         │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│              DATA LAKE / LAKEHOUSE                              │
├─────────────────────────────────────────────────────────────────┤
│  • Structured data (CRM records)                                │
│  • Semi-structured (JSON, XML)                                  │
│  • Unstructured (audio, video - new in 2024)                    │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│              HARMONIZATION & MODELING                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  Data Model  │  │  Identity    │  │  Calculated          │  │
│  │  (Objects)   │  │  Resolution  │  │  Insights            │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│              UNIFIED CUSTOMER PROFILE                           │
├─────────────────────────────────────────────────────────────────┤
│  Customer: John Doe                                             │
│  ├─ Unified ID: DC-987654                                       │
│  ├─ Contact Points: email, phone, device IDs                    │
│  ├─ Engagement History: web, mobile, store, call center         │
│  ├─ Transactions: $12,450 lifetime value                        │
│  ├─ Segments: High-Value, Mobile-First, At-Risk                 │
│  └─ Calculated: Next Best Action, Churn Probability             │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                     ACTIVATION                                  │
├─────────────────────────────────────────────────────────────────┤
│  Sales Cloud | Service Cloud | Marketing Cloud | External       │
└─────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Data Streams

**Batch Ingestion**
```yaml
Data Stream: Customer_Profiles
Source: Salesforce CRM
Object: Account
Fields:
  - Id
  - Name
  - Industry
  - AnnualRevenue
  - BillingAddress
Schedule: Every 4 hours
```

**Streaming Ingestion**
```yaml
Data Stream: Web_Events
Source: Web Analytics
Event Type: Page View
Fields:
  - customerId
  - pageUrl
  - timestamp
  - sessionId
  - deviceType
Delivery: Real-time (< 200ms latency)
```

### 2. Data Model

#### Standard Data Model Objects

| Object | Purpose | Key Fields |
|--------|---------|------------|
| **Unified Individual** | Master customer profile | UnifiedId, ContactPoints |
| **Unified Contact Point** | Email, phone, address | Type, Value, Verified |
| **Engagement** | Interaction events | Channel, Timestamp, Content |
| **Sales Transaction** | Purchase history | Amount, Products, Date |
| **Product** | Product catalog | SKU, Category, Price |

#### Custom Data Model Objects
```
Setup → Data Cloud → Data Model
├── Create Custom Object
│   ├── Object Name: Loyalty_Member__dlm
│   ├── Fields:
│   │   ├── Member_ID__c (Text)
│   │   ├── Tier__c (Picklist)
│   │   ├── Points_Balance__c (Number)
│   │   └── Join_Date__c (Date)
```

### 3. Identity Resolution

#### Matching Rules
```yaml
Rule Set: Customer_Matching
Rules:
  - name: Email_Match
    priority: 1
    criteria:
      - Email__c EXACT_MATCH
    
  - name: Phone_Match
    priority: 2
    criteria:
      - Phone__c EXACT_MATCH
    
  - name: Fuzzy_Name_Address
    priority: 3
    criteria:
      - FirstName__c FUZZY_MATCH (threshold: 0.8)
      - LastName__c EXACT_MATCH
      - BillingPostalCode__c EXACT_MATCH

Reconciliation:
  - Most_Recent: LastModifiedDate
  - Most_Frequent: Email domain
```

#### Identity Graph
```
Source Records → Matching → Unified Profile

CRM: john@email.com, 555-0100 → MATCH → Unified: U-12345
Web: john@email.com, Device-A123 → MATCH → Unified: U-12345  
Store: J. Doe, 555-0100 → MATCH → Unified: U-12345
App: john.doe@email.com → MATCH → Unified: U-12345
```

### 4. Calculated Insights

#### Streaming Insights (Real-time)
```sql
-- Real-time cart abandonment
SELECT 
    unifiedIndividualId,
    COUNT(DISTINCT sessionId) as session_count,
    MAX(eventTimestamp) as last_activity
FROM engagement_events
WHERE eventType = 'Cart_Add' 
  AND eventTimestamp > NOW() - INTERVAL '1 hour'
  AND NOT EXISTS (
      SELECT 1 FROM engagement_events e2
      WHERE e2.sessionId = engagement_events.sessionId
      AND e2.eventType = 'Purchase_Complete'
  )
GROUP BY unifiedIndividualId
HAVING COUNT(DISTINCT sessionId) > 0
```

#### Batch Insights (Scheduled)
```sql
-- Customer Lifetime Value calculation
SELECT 
    unifiedIndividualId,
    SUM(transactionAmount) as total_spend,
    COUNT(transactionId) as transaction_count,
    AVG(transactionAmount) as avg_order_value,
    MAX(transactionDate) as last_purchase_date,
    DATEDIFF(day, MIN(transactionDate), MAX(transactionDate)) as customer_tenure_days
FROM sales_transactions
WHERE transactionDate >= DATE_SUB(YEAR, 2, CURRENT_DATE)
GROUP BY unifiedIndividualId
```

#### Profile Attributes
```yaml
Calculated Attribute: Churn_Risk_Score
Type: Score (0-100)
Calculation:
  - Days since last purchase (> 90 days: +30 points)
  - Support ticket sentiment (negative: +20 points)
  - Email engagement decline (> 50%: +25 points)
  - Website visit frequency (decreasing: +25 points)

Refresh: Daily
```

## Implementation Steps

### Phase 1: Foundation (Week 1-2)

1. **Enable Data Cloud**
   ```
   Setup → Data Cloud → Get Started
   ```

2. **Configure Data Cloud Admin**
   - Assign "Data Cloud Admin" permission set
   - Set up data spaces (if multi-tenant)

3. **Connect First Source**
   ```
   Data Cloud → Data Streams → New
   ├── Select Source: Salesforce CRM
   ├── Select Object: Account
   ├── Map Fields
   └── Activate
   ```

### Phase 2: Data Ingestion (Week 3-4)

1. **Create Data Streams**
   - Map all required objects
   - Schedule batch loads
   - Configure streaming for real-time events

2. **Data Quality Assessment**
   - Review ingestion errors
   - Cleanse data at source
   - Document data lineage

### Phase 3: Identity Resolution (Week 5-6)

1. **Configure Matching Rules**
   ```
   Data Cloud → Identity Resolution
   ├── Create Rule Set
   ├── Define Matching Rules
   ├── Set Reconciliation Rules
   └── Activate
   ```

2. **Review Unified Profiles**
   - Spot-check match accuracy
   - Adjust thresholds if needed
   - Monitor match rates

### Phase 4: Insights & Activation (Week 7-8)

1. **Create Calculated Insights**
   - Define business metrics
   - Build segment criteria
   - Set refresh schedules

2. **Configure Activations**
   ```
   Data Cloud → Activations → New
   ├── Select Segment: High_Value_At_Risk
   ├── Target: Marketing Cloud
   ├── Schedule: Real-time
   └── Field Mappings
   ```

## Activation Targets

| Target | Use Case | Data Type |
|--------|----------|-----------|
| **Sales Cloud** | Lead scoring, account enrichment | Unified profiles |
| **Service Cloud** | Case routing, priority queue | Engagement history |
| **Marketing Cloud** | Journey triggers, personalization | Segments, behaviors |
| **Advertising** | Lookalike audiences, retargeting | Hashed identifiers |
| **External API** | Data warehouse, analytics | Unified profiles |

## Data Cloud + Agentforce

### Powering AI Agents

```
Data Cloud provides:
├── Unified Customer Context
│   └── 360° view for personalized responses
├── Real-time Data Access
│   └── Current order status, preferences
├── Calculated Insights
│   └── Churn risk, LTV, next best action
├── Engagement History
│   └── Previous interactions across channels
└── Segmentation
    └── Targeted agent behaviors
```

### Example: Agentforce with Data Cloud

```yaml
Agent: Premium Support Agent
Data Cloud Integration:
  Real-time Context:
    - Customer Tier: Platinum
    - Lifetime Value: $45,000
    - Recent Satisfaction: 9.2/10
    - Open Cases: 1 (pending > 3 days)
    - Last Purchase: 2 weeks ago
    
  Personalization:
    - Greeting: "Welcome back, [PreferredName]"
    - Priority: Route to senior agent queue
    - Offers: Premium support options
    - Guardrails: Waive fees up to $200
```

## Best Practices

### Data Governance
- Document all data sources and owners
- Implement data quality rules at ingestion
- Monitor data freshness SLAs
- Set retention policies

### Identity Resolution
- Start with high-confidence rules
- Gradually add fuzzy matching
- Regularly review match quality
- Handle edge cases (shared emails, etc.)

### Performance
- Use streaming for real-time needs
- Batch process historical data
- Optimize calculated insight refresh
- Monitor data storage usage

### Privacy
- Tag sensitive data attributes
- Implement consent management
- Respect privacy preferences in activations
- Document data lineage for audits

## Monitoring & Troubleshooting

### Key Metrics
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Ingestion Success Rate | > 99% | < 95% |
| Identity Match Rate | > 80% | < 70% |
| Profile Completeness | > 60% | < 50% |
| Activation Latency | < 5 min | > 15 min |

### Common Issues

**Low Match Rates**
- Check data quality at source
- Verify matching rule criteria
- Consider adding more match keys

**Slow Activations**
- Review segment complexity
- Check target system API limits
- Optimize calculated attributes

**Data Quality Issues**
- Implement validation rules
- Use data transforms
- Cleanse at source systems

---

> **Note**: Data Cloud is included by default in most Salesforce editions as of 2025 and is required for Agentforce
