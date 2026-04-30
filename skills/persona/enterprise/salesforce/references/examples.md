## 4. Examples

### Example 1: Multi-Cloud Architecture Design

**Scenario**: A financial services company needs to implement Sales Cloud + Service Cloud + Experience Cloud for advisors, with Data Cloud for unified customer view and Agentforce for automated service.

**Architecture Solution**:

```
┌─────────────────────────────────────────────────────────────────┐
│                      CUSTOMER EXPERIENCE                        │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │   Advisor    │  │   Customer   │  │   Agentforce AI      │  │
│  │   Portal     │  │   Community  │  │   Service Agent      │  │
│  │  (Exp Cloud) │  │  (Exp Cloud) │  │                      │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
└─────────┼─────────────────┼────────────────────┼──────────────┘
          │                 │                    │
          └─────────────────┼────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                        SALESFORCE PLATFORM                      │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │   Sales Cloud    │  │  Service Cloud   │  │  Data Cloud  │  │
│  │  - Opportunities │  │  - Cases         │  │  - Profiles  │  │
│  │  - Forecasting   │  │  - Knowledge     │  │  - Segments  │  │
│  │  - CPQ           │  │  - Omni-Channel  │  │  - Insights  │  │
│  └──────────────────┘  └──────────────────┘  └──────────────┘  │
│                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │  Custom Objects  │  │  Flow Automation │  │  Security    │  │
│  │  - Policies      │  │  - Approval Proc │  │  - Shield    │  │
│  │  - Claims        │  │  - Auto-escalate │  │  - Sharing   │  │
│  └──────────────────┘  └──────────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────────────┘
          │                                    │
          └────────────────┬───────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      INTEGRATION LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │   MuleSoft   │  │  Heroku      │  │   External Systems   │  │
│  │  APIs/ESB    │  │  Connect     │  │  - Core Banking      │  │
│  │              │  │              │  │  - Document Mgmt     │  │
│  │              │  │              │  │  - Compliance DB     │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Key Decisions**:
- **Person Accounts** for B2C financial customers
- **Role hierarchy** mirroring advisor teams
- **Territory Management** for geographic coverage
- **Shield Platform Encryption** for PII/financial data
- **Event-driven integration** via Platform Events

---

### Example 2: Agentforce Service Agent Implementation

**Scenario**: Deploy an autonomous Agentforce agent to handle tier-1 customer service inquiries, integrated with existing Service Cloud implementation.

**Implementation Steps**:

**Step 1: Data Foundation**
```
Prerequisites:
□ Data Cloud provisioned and connected
□ Knowledge base articles indexed
□ Case history (12+ months) available
□ Customer data unified in Data Cloud
```

**Step 2: Agent Configuration**
```yaml
Agent Name: Customer Support Agent
Topics:
  - Order Status Inquiries:
      Actions: [QueryOrder, CheckShipment]
      Guardrails: "Cannot cancel orders >$10K without approval"
  
  - Product Information:
      Actions: [SearchKnowledge, CompareProducts]
      Guardrails: "Do not provide pricing for enterprise accounts"
  
  - Technical Support:
      Actions: [SearchKnowledge, CreateCase, ScheduleCallback]
      Guardrails: "Escalate to human if sentiment < -0.5"

Guardrails:
  - Max Refund Authorization: $500
  - Required Human Approval: Account closure, GDPR requests
  - Data Access: Respect field-level security and sharing rules
```

**Step 3: Integration Setup**
```javascript
// Example: Custom Action for Order Lookup
public class OrderLookupAction {
    @InvocableMethod(label='Query Order Status')
    public static List<OrderResult> lookupOrder(List<OrderRequest> requests) {
        // Integration with ERP via MuleSoft API
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:MuleSoft_API/orders/' + requests[0].orderNumber);
        req.setMethod('GET');
        // ... implementation
    }
}
```

**Step 4: Testing & Validation**
- Conversation testing in Agent Builder
- Grounding validation (ensure responses based on actual data)
- Guardrail boundary testing
- Handoff to human agent scenarios

---

### Example 3: Apex Trigger Refactoring

**Scenario**: Legacy org has 12 triggers on Account object causing recursion and governor limit issues. Refactor to trigger framework.

**Before (Problematic)**:
```java
// Bad: Multiple triggers on same object
trigger AccountTrigger1 on Account (before insert) {
    // Logic here
}

trigger AccountTrigger2 on Account (before insert, after insert) {
    // Different logic here - order of execution unpredictable
}
```

**After (Framework Pattern)**:
```java
// Single trigger delegating to handler
trigger AccountTrigger on Account (
    before insert, after insert,
    before update, after update,
    before delete, after delete,
    after undelete
) {
    TriggerDispatcher.dispatch(AccountTriggerHandler.class);
}

// Handler class implementing interface
public class AccountTriggerHandler implements ITriggerHandler {
    
    public void beforeInsert(List<SObject> newRecords) {
        AccountTriggerHelper.validateRequiredFields((List<Account>)newRecords);
        AccountTriggerHelper.setDefaultValues((List<Account>)newRecords);
    }
    
    public void afterInsert(Map<Id, SObject> newRecordsMap) {
        // Bulkified operations
        AccountTriggerHelper.createRelatedContacts(newRecordsMap.keySet());
    }
    
    public void beforeUpdate(Map<Id, SObject> oldRecords, 
                             Map<Id, SObject> newRecords) {
        AccountTriggerHelper.checkForFieldChanges(
            (Map<Id, Account>)oldRecords, 
            (Map<Id, Account>)newRecords
        );
    }
    
    // ... other methods
    
    // Disable flag for data migrations
    public static Boolean triggerDisabled = false;
    public Boolean isDisabled() {
        return triggerDisabled || TriggerSettings__c.getInstance().AccountTriggerDisabled__c;
    }
}
```

**Benefits**:
- Single trigger per object (predictable order)
- Recursion prevention built-in
- Easy to disable for bulk operations
- Centralized logging and error handling

---

### Example 4: Data Cloud Implementation

**Scenario**: Retail company wants unified customer profiles from online, in-store, and mobile app touchpoints for personalized marketing.

**Data Cloud Architecture**:

```
┌─────────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  E-commerce  │  │   POS System │  │   Mobile App         │  │
│  │  (Shopify)   │  │   (Square)   │  │   (Custom)           │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
└─────────┼─────────────────┼────────────────────┼──────────────┘
          │                 │                    │
          └─────────────────┼────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    INGESTION & TRANSFORMATION                   │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Data Cloud Ingestion API                   │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────────┐    │   │
│  │  │ Data Streams│  │ Calculated │  │ Identity       │    │   │
│  │  │ (Streaming)│  │ Insights   │  │ Resolution     │    │   │
│  │  └────────────┘  └────────────┘  └────────────────┘    │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  UNIFIED CUSTOMER PROFILE                       │
├─────────────────────────────────────────────────────────────────┤
│  Customer: Jane Smith                                           │
│  ├─ Unified ID: DC-12345                                        │
│  ├─ Contact Points: jane@email.com, +1-555-0100                 │
│  ├─ Engagement History:                                         │
│  │   ├─ Website: 15 visits, 3 cart abandons                     │
│  │   ├─ Store: 5 purchases, $2,400 LTV                          │
│  │   └─ App: 2 purchases, push notifications enabled            │
│  ├─ Segments: High-Value, Fashion-Enthusiast, Mobile-First      │
│  └─ Calculated: Churn Risk 15%, Next Best Action: SMS Offer     │
└─────────────────────────────────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     ACTIVATION                                  │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  Marketing   │  │  Sales Cloud │  │   Service Cloud      │  │
│  │  Cloud       │  │  Leads       │  │   Case Routing       │  │
│  │  Journeys    │  │  Scoring     │  │   Priority Queue     │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Implementation Steps**:
1. **Data Mapping**: Map source fields to Data Cloud data model
2. **Identity Resolution**: Configure matching rules (email, phone, loyalty ID)
3. **Calculated Insights**: Build LTV, churn risk, propensity models
4. **Activation**: Publish segments to Marketing Cloud and Sales Cloud

---

### Example 5: Lightning Web Component Best Practice

**Scenario**: Build a custom product configurator component for CPQ implementation.

**Component Structure**:
```javascript
// productConfigurator.js
import { LightningElement, api, wire, track } from 'lwc';
import { getRecord, getFieldValue } from 'lightning/uiRecordApi';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import getProductOptions from '@salesforce/apex/ProductController.getProductOptions';
import saveConfiguration from '@salesforce/apex/ProductController.saveConfiguration';

import NAME_FIELD from '@salesforce/schema/Opportunity.Name';

const FIELDS = [NAME_FIELD];

export default class ProductConfigurator extends LightningElement {
    @api recordId; // Opportunity Id
    @track productOptions = [];
    @track selectedOptions = {};
    @track isLoading = false;
    @track totalPrice = 0;

    // Wire service for record data
    @wire(getRecord, { recordId: '$recordId', fields: FIELDS })
    opportunity;

    // Wire to Apex method
    @wire(getProductOptions, { opportunityId: '$recordId' })
    wiredOptions({ error, data }) {
        if (data) {
            this.productOptions = data;
            this.calculateTotal();
        } else if (error) {
            this.handleError(error);
        }
    }

    get opportunityName() {
        return getFieldValue(this.opportunity.data, NAME_FIELD);
    }

    // Event handler
    handleOptionChange(event) {
        const { optionId, value } = event.detail;
        this.selectedOptions[optionId] = value;
        this.calculateTotal();
    }

    // Async operation with loading state
    async handleSave() {
        this.isLoading = true;
        try {
            const result = await saveConfiguration({
                opportunityId: this.recordId,
                configuration: JSON.stringify(this.selectedOptions)
            });
            
            this.showToast('Success', 'Configuration saved', 'success');
            this.dispatchEvent(new CustomEvent('configurationsaved', {
                detail: result
            }));
        } catch (error) {
            this.handleError(error);
        } finally {
            this.isLoading = false;
        }
    }

    calculateTotal() {
        this.totalPrice = this.productOptions.reduce((sum, option) => {
            const selected = this.selectedOptions[option.id];
            const price = selected ? option.choices.find(c => c.value === selected)?.price || 0 : 0;
            return sum + price;
        }, 0);
    }

    handleError(error) {
        const message = error.body?.message || error.message || 'Unknown error';
        this.showToast('Error', message, 'error');
        // Log to monitoring service
        console.error('Product Configurator Error:', error);
    }

    showToast(title, message, variant) {
        this.dispatchEvent(new ShowToastEvent({ title, message, variant }));
    }
}
```

**Key Best Practices Applied**:
- ✅ Use `@wire` for server data (caching, refresh)
- ✅ Lightning Data Service for record operations
- ✅ Track decorator for private reactive properties
- ✅ Error handling with user feedback
- ✅ Loading states for async operations
- ✅ Custom events for parent communication
- ✅ Separation of concerns (JS logic, HTML template, CSS)

---
