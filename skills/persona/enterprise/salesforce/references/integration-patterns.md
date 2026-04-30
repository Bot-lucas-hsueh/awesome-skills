# Salesforce Integration Patterns

## Integration Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      SALESFORCE PLATFORM                        │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │   UI Layer   │  │  Process     │  │   Data Layer         │  │
│  │  (LWC/VF)    │  │  (Flow/Apex) │  │  (Objects)           │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
└─────────┼─────────────────┼────────────────────┼──────────────┘
          │                 │                    │
          └─────────────────┼────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    INTEGRATION LAYER                            │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  REST API    │  │  Bulk API    │  │  Streaming API       │  │
│  │  (Real-time) │  │  (Data Load) │  │  (Events)            │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  MuleSoft    │  │  Heroku      │  │  External Services   │  │
│  │  (ESB/iPaaS) │  │  (PaaS)      │  │  (OpenAPI)           │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   EXTERNAL SYSTEMS                              │
├─────────────────────────────────────────────────────────────────┤
│  ERP | Data Warehouse | Payment Gateways | Legacy Systems | IoT │
└─────────────────────────────────────────────────────────────────┘
```

## Pattern 1: Request-Reply (Synchronous)

**Use Case**: Real-time data lookup, validation

```java
// Apex Callout Pattern
public class ERPIntegration {
    
    public static OrderStatus getOrderStatus(String erpOrderId) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:ERP_Named_Credential/orders/' + erpOrderId);
        req.setMethod('GET');
        req.setHeader('Content-Type', 'application/json');
        req.setTimeout(30000); // 30 second timeout
        
        Http http = new Http();
        HttpResponse res = http.send(req);
        
        if (res.getStatusCode() == 200) {
            return (OrderStatus) JSON.deserialize(res.getBody(), OrderStatus.class);
        } else {
            throw new IntegrationException('ERP call failed: ' + res.getBody());
        }
    }
}

// Usage in Trigger (be careful - can cause delays)
// Better: Queueable or Future for callouts from triggers
```

**Considerations**:
- 120-second timeout limit for synchronous
- Handle failures gracefully
- Consider user experience delays
- Idempotent design for retries

## Pattern 2: Fire-and-Forget (Asynchronous)

**Use Case**: Notifications, logging, non-critical updates

```java
// Platform Events - Event-Driven Architecture
public class OrderEventPublisher {
    
    public static void publishOrderCreated(Id orderId) {
        Order_Created__e event = new Order_Created__e(
            Order_Id__c = orderId,
            Created_Date__c = System.now(),
            User_Id__c = UserInfo.getUserId()
        );
        Database.SaveResult result = EventBus.publish(event);
        
        if (!result.isSuccess()) {
            // Log error, trigger compensating transaction
            LogService.logError('Event publish failed', result.getErrors());
        }
    }
}

// Trigger subscriber (Platform Event Trigger)
trigger OrderCreatedTrigger on Order_Created__e (after insert) {
    List<Task> tasks = new List<Task>();
    for (Order_Created__e event : Trigger.new) {
        tasks.add(new Task(
            Subject = 'Follow up on new order',
            WhatId = event.Order_Id__c,
            OwnerId = event.User_Id__c
        ));
    }
    insert tasks;
}
```

**Considerations**:
- High-volume platform events for scale
- Event replay for reliability
- Decouples systems

## Pattern 3: Batch Data Synchronization

**Use Case**: Nightly syncs, data migrations

```java
// Batch Apex for outbound sync
public class AccountSyncBatch implements Database.Batchable<SObject>, 
                                         Database.AllowsCallouts,
                                         Database.Stateful {
    
    private List<SyncError> errors = new List<SyncError>();
    
    public Database.QueryLocator start(Database.BatchableContext bc) {
        return Database.getQueryLocator([
            SELECT Id, Name, AccountNumber, LastModifiedDate
            FROM Account
            WHERE LastModifiedDate = LAST_N_DAYS:1
        ]);
    }
    
    public void execute(Database.BatchableContext bc, List<Account> scope) {
        List<AccountPayload> payloads = new List<AccountPayload>();
        
        for (Account acc : scope) {
            payloads.add(new AccountPayload(acc));
        }
        
        try {
            HttpResponse res = sendToERP(JSON.serialize(payloads));
            if (res.getStatusCode() != 200) {
                recordErrors(scope, res.getBody());
            }
        } catch (Exception e) {
            recordErrors(scope, e.getMessage());
        }
    }
    
    public void finish(Database.BatchableContext bc) {
        if (!errors.isEmpty()) {
            sendErrorNotification(errors);
        }
    }
    
    // ... helper methods
}

// Schedule daily
System.schedule('Account Sync', '0 0 2 * * ?', new AccountSyncScheduler());
```

**Considerations**:
- Schedule during off-peak hours
- Handle partial failures
- Implement retry logic
- Monitor batch execution time

## Pattern 4: Change Data Capture (CDC)

**Use Case**: Real-time sync to external systems

```java
// Enable CDC on object: Setup → Change Data Capture → Account

// Apex Trigger on CDC event
trigger AccountChangeEvent on AccountChangeEvent (after insert) {
    List<String> changedAccounts = new List<String>();
    
    for (AccountChangeEvent event : Trigger.new) {
        // Check specific field changes
        EventBus.ChangeEventHeader header = event.ChangeEventHeader;
        
        if (header.changedFields.contains('Name') || 
            header.changedFields.contains('Industry')) {
            
            changedAccounts.add(JSON.serialize(new Map<String, Object>{
                'id' => header.recordIds[0],
                'name' => event.Name,
                'industry' => event.Industry,
                'changeType' => header.changeType
            }));
        }
    }
    
    if (!changedAccounts.isEmpty()) {
        // Queue callout to external system
        System.enqueueJob(new ExternalSyncQueueable(changedAccounts));
    }
}
```

**Considerations**:
- Automatic field tracking
- Enrichment capabilities
- High-volume event support

## Pattern 5: MuleSoft Integration

**Use Case**: Enterprise integration, API-led connectivity

```yaml
# MuleSoft API Specification (RAML)
#%RAML 1.0
title: Salesforce Customer API
version: v1
baseUri: https://api.company.com/salesforce

types:
  Customer:
    properties:
      id: string
      name: string
      email: string
      salesforceId?: string

/customers:
  post:
    description: Create customer in Salesforce
    body:
      application/json:
        type: Customer
    responses:
      201:
        body:
          application/json:
            type: Customer

  /{id}:
    get:
      description: Get customer from Salesforce
      responses:
        200:
          body:
            application/json:
              type: Customer
```

```java
// Salesforce calling MuleSoft via Named Credential
public class CustomerIntegration {
    
    public static Customer createCustomer(CustomerRequest request) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:MuleSoft_API/customers');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setBody(JSON.serialize(request));
        
        HttpResponse res = new Http().send(req);
        
        if (res.getStatusCode() == 201) {
            return (Customer) JSON.deserialize(res.getBody(), Customer.class);
        }
        throw new IntegrationException('Failed: ' + res.getBody());
    }
}
```

## Pattern 6: Heroku Connect

**Use Case**: Bidirectional sync with PostgreSQL

```
Heroku Connect Architecture:

Salesforce ←→ Heroku Connect ←→ PostgreSQL
     ↑                              ↑
     └─────── Real-time Sync ───────┘
```

**Setup**:
1. Provision Heroku app with Postgres
2. Install Heroku Connect add-on
3. Configure connection to Salesforce org
4. Map objects for sync (read-only or read-write)

**Use Cases**:
- Data warehouse integration
- Custom app backend
- Complex reporting
- External processing

## Pattern 7: Composite API

**Use Case**: Reduce API calls by batching

```java
// Composite API request
{
  "compositeRequest": [
    {
      "method": "POST",
      "url": "/services/data/v60.0/sobjects/Account",
      "referenceId": "newAccount",
      "body": {
        "Name": "Acme Corporation"
      }
    },
    {
      "method": "POST",
      "url": "/services/data/v60.0/sobjects/Contact",
      "referenceId": "newContact",
      "body": {
        "LastName": "Smith",
        "AccountId": "@{newAccount.id}"
      }
    }
  ]
}
```

**Benefits**:
- Single round-trip for related operations
- Up to 25 sub-requests per composite call
- Rollback on partial failure (AllOrNone)

## Pattern 8: Pub-Sub API

**Use Case**: High-volume event streaming

```java
// Subscribe to events via Pub/Sub API
// Uses gRPC for efficient streaming

// External client (Java example)
/*
PubSubGrpc.PubSubBlockingStub stub = PubSubGrpc.newBlockingStub(channel);

FetchRequest request = FetchRequest.newBuilder()
    .setTopicName("/data/AccountChangeEvent")
    .setNumRequested(10)
    .build();

stub.subscribe(request).forEachRemaining(response -> {
    // Process event batch
    processEvents(response.getEventsList());
});
*/
```

## Error Handling Best Practices

```java
public class IntegrationException extends Exception {}

public class IntegrationLogger {
    
    public static void logCallout(String endpoint, String request, 
                                   HttpResponse response, Long duration) {
        Integration_Log__c log = new Integration_Log__c(
            Endpoint__c = endpoint,
            Request__c = request.left(131072), // Max field size
            Response__c = response?.getBody()?.left(131072),
            Status_Code__c = response?.getStatusCode(),
            Duration_ms__c = duration,
            Timestamp__c = System.now()
        );
        insert log;
    }
}

// Retry pattern with exponential backoff
public class RetryableCallout {
    
    public static HttpResponse executeWithRetry(HttpRequest req, Integer maxRetries) {
        Integer attempts = 0;
        Exception lastException;
        
        while (attempts < maxRetries) {
            try {
                HttpResponse res = new Http().send(req);
                if (res.getStatusCode() < 500) {
                    return res; // Success or client error (no retry)
                }
            } catch (Exception e) {
                lastException = e;
            }
            
            attempts++;
            if (attempts < maxRetries) {
                // Exponential backoff: 1s, 2s, 4s, 8s...
                Integer delay = (Integer) Math.pow(2, attempts - 1) * 1000;
                // Note: Can't Thread.sleep in Apex - use Scheduled job instead
            }
        }
        
        throw new IntegrationException('Max retries exceeded: ' + lastException?.getMessage());
    }
}
```

## Security Considerations

1. **Named Credentials**: Store endpoint URLs and auth securely
2. **OAuth 2.0**: Use JWT or username-password flows appropriately
3. **IP Restrictions**: Whitelist Salesforce IP ranges
4. **Encryption**: Use TLS 1.2+ for all connections
5. **Field-Level Security**: Respect FLS in integrations

---

> **Tip**: Always design integrations to be idempotent - same input produces same result, no duplicates on retry
