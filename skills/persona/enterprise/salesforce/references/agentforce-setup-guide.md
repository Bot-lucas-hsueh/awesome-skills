# Agentforce Setup Guide

## Overview

Agentforce is Salesforce's autonomous AI agent platform that enables businesses to deploy AI agents capable of reasoning, planning, and taking action across the Customer 360 platform.

## Prerequisites

- Enterprise, Unlimited, or Performance Edition
- Data Cloud provisioned (included by default in most editions as of 2025)
- "Manage Einstein" permission set
- Knowledge base content indexed (for service agents)

## Architecture Components

```
┌─────────────────────────────────────────────────────────────────┐
│                        AGENTFORCE PLATFORM                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Atlas Reasoning Engine                     │   │
│  │  • Topic Classification                                 │   │
│  │  • Instruction Loading                                  │   │
│  │  • Action Planning                                      │   │
│  │  • Grounding Check                                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│              ┌───────────────┼───────────────┐                  │
│              ▼               ▼               ▼                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Topics     │  │   Actions    │  │ Guardrails   │          │
│  │  (Intents)   │  │  (Tasks)     │  │ (Controls)   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Einstein Trust Layer                    │   │
│  │  • Data Masking  • Toxicity Detection                  │   │
│  │  • Audit Trails  • Zero Data Retention                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Setup Steps

### Step 1: Enable Einstein Generative AI

1. Navigate to **Setup** → Search for **"Einstein Setup"**
2. Toggle on **Einstein Generative AI**
3. Review and accept terms of service
4. Refresh page to see configuration options

### Step 2: Configure Einstein Trust Layer

```yaml
# Data Masking Rules
Sensitive Fields:
  - Social Security Number
  - Credit Card Numbers
  - Health Records (PHI)
  - Financial Account Numbers

# Toxicity Detection
Thresholds:
  - Hate Speech: Block
  - Harassment: Block
  - Self-Harm: Block + Alert
  - Sexual Content: Block

# Audit Logging
Retention: 12 months
Access: Admin + Compliance Team
```

### Step 3: Enable Data Cloud

Data Cloud powers Agentforce with:
- Unified customer profiles
- Real-time data activation
- RAG (Retrieval Augmented Generation)
- Audit trails

```
Setup → Data Cloud → Get Started
├── Connect Data Sources
│   ├── Salesforce CRM
│   ├── External Systems (MuleSoft)
│   └── Streaming Ingestion
├── Create Data Streams
├── Configure Identity Resolution
└── Enable Calculated Insights
```

### Step 4: Create Your First Agent

#### Using Agent Builder

```
Agent Builder → New Agent
├── Basic Information
│   ├── Name: Customer Support Agent
│   ├── Description: Handles tier-1 support inquiries
│   └── Channel: Web (or Slack, Mobile)
│
├── Topics (Define what agent can do)
│   ├── Order Status Inquiry
│   ├── Product Information
│   ├── Return/Refund Request
│   └── Technical Support
│
├── Actions (What agent can execute)
│   ├── Query Order (Apex/Flow)
│   ├── Search Knowledge Articles
│   ├── Create Case
│   └── Check Inventory
│
└── Guardrails (Safety controls)
    ├── Max refund: $500
    ├── Escalation trigger: Sentiment < -0.5
    └── Human approval: Account closure
```

#### Topic Configuration Example

```yaml
Topic: Order Status Inquiry
Instructions: |
  Help customers check their order status.
  - Ask for order number if not provided
  - Provide shipping tracking when available
  - Escalate if order shows as delayed > 5 days
  - Never provide order details for unverified users

Actions:
  - name: QueryOrder
    description: Look up order by order number
    input: orderNumber (string, required)
    
  - name: GetShippingStatus
    description: Get current shipping status
    input: orderId (string)
    
  - name: CheckDelayReason
    description: Check why order is delayed
    input: orderId (string)

Guardrails:
  - "Cannot cancel orders without user confirmation"
  - "Do not provide pricing for B2B accounts"
  - "Verify identity before sharing order details"
```

### Step 5: Configure Actions

#### Apex Action Example
```java
public class OrderLookupAction {
    
    @InvocableMethod(
        label='Query Order Status'
        description='Retrieves order details for customer inquiry'
    )
    public static List<OrderResult> lookupOrder(List<OrderRequest> requests) {
        List<OrderResult> results = new List<OrderResult>();
        
        for (OrderRequest req : requests) {
            // Query order
            Order__c order = [
                SELECT Id, Order_Number__c, Status__c, 
                       Shipping_Date__c, Tracking_Number__c
                FROM Order__c 
                WHERE Order_Number__c = :req.orderNumber
                LIMIT 1
            ];
            
            // Map to result
            OrderResult result = new OrderResult();
            result.orderId = order.Id;
            result.status = order.Status__c;
            result.trackingNumber = order.Tracking_Number__c;
            results.add(result);
        }
        
        return results;
    }
    
    public class OrderRequest {
        @InvocableVariable(required=true)
        public String orderNumber;
    }
    
    public class OrderResult {
        @InvocableVariable
        public String orderId;
        @InvocableVariable
        public String status;
        @InvocableVariable
        public String trackingNumber;
    }
}
```

#### Flow Action Example
```
Flow: Create Support Case
Type: Autolaunched Flow
Inputs:
  - customerId (Text)
  - issueDescription (Text)
  - priority (Text)

Process:
  1. Get Customer Record
  2. Create Case
     - AccountId = customerId
     - Subject = issueDescription  
     - Priority = priority
  3. Assign to Queue (based on priority)
  4. Return Case Number
```

### Step 6: Test Your Agent

#### Conversation Testing
```
Test Scenarios:
1. Happy Path
   User: "Where is my order?"
   User: "ORD-12345"
   Agent: Provides status + tracking

2. Missing Information
   User: "Check my order"
   Agent: Asks for order number

3. Escalation Trigger
   User: "My order is 2 weeks late!"
   Agent: Apologizes, explains, offers to escalate

4. Guardrail Test
   User: "Cancel my $50,000 order"
   Agent: Requires confirmation + manager approval
```

#### Grounding Validation
- Verify responses cite actual data
- Check hallucination prevention
- Ensure compliance with instructions

### Step 7: Deploy

```
Deployment Checklist:
□ Agent tested in sandbox
□ Guardrails validated
□ Actions have error handling
□ Audit logging enabled
□ Monitoring dashboard configured
□ Handoff to human process defined
□ User permissions assigned
```

## Out-of-the-Box Agents

| Agent | Purpose | Availability |
|-------|---------|--------------|
| **Service Agent** | Customer support automation | GA |
| **SDR Agent** | Lead engagement & qualification | GA |
| **Sales Coach** | Rep training & role-play | GA |
| **Campaign Optimizer** | Marketing automation | GA |
| **Personal Shopper** | E-commerce assistance | GA |
| **Buyer Agent** | B2B purchasing support | GA |

## Agentforce in Slack

### Setup
```
Slack App → Salesforce Integration
├── Install Salesforce App
├── Connect to Salesforce Org
├── Configure Agentforce
│   ├── Select Agent
│   ├── Define Triggers
│   └── Set Permissions
└── Test in Channel
```

### Usage
```
@Agentforce What's the status of ACME account?
@Agentforce Schedule follow-up with prospect
@Agentforce Summarize this thread
```

## Monitoring & Analytics

### Key Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| **Conversation Volume** | Total interactions | Track growth |
| **Resolution Rate** | % resolved without human | > 70% |
| **Avg Handle Time** | Time to resolution | < 5 min |
| **CSAT** | Customer satisfaction | > 4.0/5 |
| **Escalation Rate** | % transferred to human | < 15% |
| **Grounding Score** | Accuracy of responses | > 95% |

### Dashboard Setup
```
Einstein Analytics → Agentforce Dashboard
├── Conversation Volume by Day
├── Topic Distribution
├── Resolution Funnel
├── Agent Performance Comparison
└── Escalation Reasons
```

## Pricing

| Model | Pricing | Use Case |
|-------|---------|----------|
| **Per Conversation** | $2/conversation | Variable volume |
| **Per Action** | $0.10/action (Flex Credits) | Action-heavy agents |
| **Per User** | $125-$650/user/month | High-volume users |

## Best Practices

1. **Start Small**: Deploy one use case, expand based on learnings
2. **Knowledge First**: Ensure knowledge base is comprehensive
3. **Test Thoroughly**: Validate all conversation paths
4. **Monitor Continuously**: Review conversations weekly
5. **Iterate Often**: Update topics based on real usage
6. **Human Handoff**: Define clear escalation criteria

---

> **Note**: Agentforce 2.0 (February 2025) includes enhanced reasoning, Slack integration, and natural language agent creation
