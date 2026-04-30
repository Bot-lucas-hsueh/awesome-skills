# Sales Cloud Quick Reference

## Core Objects

| Object | Purpose | Key Fields |
|--------|---------|------------|
| **Lead** | Prospects not yet qualified | Status, Lead Source, Rating, Converted |
| **Contact** | People associated with Accounts | Email, Phone, AccountId, ReportsToId |
| **Account** | Companies/organizations | Type, Industry, AnnualRevenue, OwnerId |
| **Opportunity** | Potential deals | Stage, Amount, CloseDate, Probability |
| **Product2** | Sellable items | ProductCode, Family, IsActive, Price |
| **Pricebook2** | Product pricing collections | IsActive, Description |
| **Quote** | Customer proposals | Status, ExpirationDate, TotalPrice |

## Sales Process Configuration

```
Sales Process → Opportunity Stages → Forecast Categories
                    ↓
            Page Layouts → Record Types
                    ↓
            Validation Rules → Automation
```

### Opportunity Stage Setup

| Stage | Probability | Category | Type |
|-------|-------------|----------|------|
| Prospecting | 10% | Pipeline | Open |
| Qualification | 25% | Pipeline | Open |
| Needs Analysis | 50% | Pipeline | Open |
| Value Proposition | 65% | Best Case | Open |
| Id. Decision Makers | 75% | Commit | Open |
| Perception Analysis | 90% | Commit | Open |
| Proposal/Price Quote | 95% | Closed | Open |
| Negotiation/Review | 99% | Closed | Open |
| Closed Won | 100% | Closed | Closed/Won |
| Closed Lost | 0% | Omitted | Closed/Lost |

## Key Automation

### Lead Assignment Rules
```
Criteria → Assign To → Email Template → Notification
```

### Auto-Response Rules
- New Lead submitted via Web-to-Lead
- Response within 24 hours SLA

### Validation Rules (Examples)

```javascript
// Opportunity must have Products when Stage = Closed Won
AND(
    ISPICKVAL(StageName, "Closed Won"),
    NOT(HASOPPLINEITEM)
)

// Close Date cannot be in past
CloseDate < TODAY()
```

## Forecasting

### Forecast Types
1. **Opportunity Split** - Revenue split among team
2. **Product Family** - Forecast by product category
3. **Schedule Date** - Forecast by delivery date
4. **Custom** - User-defined criteria

### Forecast Hierarchy
```
CEO
└─ VP Sales
   ├─ Regional Director - East
   │  ├─ Sales Manager - Northeast
   │  └─ Sales Manager - Southeast
   └─ Regional Director - West
      └─ Sales Manager - Northwest
```

## CPQ (Configure, Price, Quote) Essentials

```
Product → Features → Options → Constraints
              ↓
        Price Rules → Quote Calculations
              ↓
         Quote Template → PDF Output
```

### Key CPQ Objects
- **SBQQ__Product__c** - CPQ products
- **SBQQ__Quote__c** - Quotes
- **SBQQ__QuoteLine__c** - Line items
- **SBQQ__Subscription__c** - Renewal management

## Reports & Dashboards

### Essential Sales Reports
| Report | Purpose |
|--------|---------|
| Pipeline by Stage | Funnel visibility |
| Closed Won This Quarter | Win tracking |
| Win Rate by Rep | Performance |
| Average Deal Size | Trend analysis |
| Sales Cycle Length | Efficiency |
| Lead Conversion Rate | Marketing effectiveness |

### Key Metrics
- **Quota Attainment** - % of quota achieved
- **Win Rate** - Closed Won / (Closed Won + Closed Lost)
- **Average Deal Size** - Total Closed Won / # of Deals
- **Sales Cycle** - Average days from creation to close

---

> **Tip**: Enable Enhanced Forecasting for AI-powered predictions
