# Apex & Lightning Web Components Quick Reference

## Apex Fundamentals

### Trigger Pattern
```java
// One trigger per object - delegates to handler
trigger AccountTrigger on Account (before insert, before update, after insert, after update) {
    new AccountTriggerHandler().execute();
}

// Handler class
public class AccountTriggerHandler extends TriggerHandler {
    
    public override void beforeInsert() {
        AccountHelper.setDefaults((List<Account>) Trigger.new);
    }
    
    public override void afterInsert() {
        AccountHelper.createRelatedRecords((Map<Id, Account>) Trigger.newMap);
    }
}

// Base Handler class
public abstract class TriggerHandler {
    public void execute() {
        if (Trigger.isBefore) {
            if (Trigger.isInsert) beforeInsert();
            if (Trigger.isUpdate) beforeUpdate();
        }
        if (Trigger.isAfter) {
            if (Trigger.isInsert) afterInsert();
            if (Trigger.isUpdate) afterUpdate();
        }
    }
    protected virtual void beforeInsert() {}
    protected virtual void beforeUpdate() {}
    protected virtual void afterInsert() {}
    protected virtual void afterUpdate() {}
}
```

### Bulkification Pattern
```java
public class AccountHelper {
    public static void processAccounts(List<Account> accounts) {
        // Collect all needed IDs in one loop
        Set<Id> ownerIds = new Set<Id>();
        for (Account acc : accounts) {
            if (acc.OwnerId != null) {
                ownerIds.add(acc.OwnerId);
            }
        }
        
        // Single query for all related data
        Map<Id, User> owners = new Map<Id, User>(
            [SELECT Id, Email FROM User WHERE Id IN :ownerIds]
        );
        
        // Process in memory
        for (Account acc : accounts) {
            User owner = owners.get(acc.OwnerId);
            // Process...
        }
    }
}
```

### Asynchronous Apex

#### Future Method
```java
public class AsyncOperations {
    @future(callout=true)
    public static void makeCallout(Set<Id> recordIds) {
        // Callouts from future methods
        HttpRequest req = new HttpRequest();
        // ...
    }
    
    @future
    public static void processRecordsAsync(Set<Id> recordIds) {
        // Long-running operations
        List<Account> accounts = [SELECT Id FROM Account WHERE Id IN :recordIds];
        // Process...
    }
}
```

#### Queueable Apex
```java
public class AccountProcessingQueue implements Queueable {
    private List<Account> accountsToProcess;
    
    public AccountProcessingQueue(List<Account> accounts) {
        this.accountsToProcess = accounts;
    }
    
    public void execute(QueueableContext context) {
        // Process records
        for (Account acc : accountsToProcess) {
            acc.Last_Processed__c = System.now();
        }
        update accountsToProcess;
        
        // Chain another job if needed
        if (hasMoreRecords()) {
            System.enqueueJob(new NextBatchQueue());
        }
    }
}

// Usage
System.enqueueJob(new AccountProcessingQueue(accounts));
```

#### Batch Apex
```java
public class AccountBatch implements Database.Batchable<SObject>, Database.Stateful {
    
    public Database.QueryLocator start(Database.BatchableContext bc) {
        return Database.getQueryLocator([
            SELECT Id, Name FROM Account WHERE CreatedDate = LAST_N_DAYS:30)
        ]);
    }
    
    public void execute(Database.BatchableContext bc, List<Account> scope) {
        // Process batch (default 200 records)
        for (Account acc : scope) {
            acc.Description = 'Processed: ' + System.now();
        }
        update scope;
    }
    
    public void finish(Database.BatchableContext bc) {
        // Send notification, chain jobs, etc.
        AsyncApexJob job = [
            SELECT Id, Status, NumberOfErrors FROM AsyncApexJob WHERE Id = :bc.getJobId()
        ];
        // Log/notify...
    }
}

// Usage
Database.executeBatch(new AccountBatch(), 200); // batch size 200
```

## Lightning Web Components

### Component Structure
```javascript
// myComponent.js
import { LightningElement, api, wire, track } from 'lwc';
import { getRecord, getFieldValue } from 'lightning/uiRecordApi';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import { refreshApex } from '@salesforce/apex';

import ACCOUNT_NAME from '@salesforce/schema/Account.Name';
import getRelatedContacts from '@salesforce/apex/AccountController.getRelatedContacts';

export default class MyComponent extends LightningElement {
    // Public property - set by parent
    @api recordId;
    
    // Private reactive properties
    @track contacts = [];
    @track isLoading = false;
    @track error;
    
    // Wire adapter for record data
    @wire(getRecord, { recordId: '$recordId', fields: [ACCOUNT_NAME] })
    wiredRecord;
    
    // Wire to Apex method
    @wire(getRelatedContacts, { accountId: '$recordId' })
    wiredContacts(result) {
        this.wiredContactsResult = result;
        if (result.data) {
            this.contacts = result.data;
            this.error = undefined;
        } else if (result.error) {
            this.error = result.error;
            this.contacts = [];
        }
    }
    
    // Getter
    get accountName() {
        return getFieldValue(this.wiredRecord.data, ACCOUNT_NAME);
    }
    
    // Event handler
    handleRefresh() {
        refreshApex(this.wiredContactsResult);
    }
    
    // Imperative Apex call
    async handleCreateContact() {
        this.isLoading = true;
        try {
            await createContact({ accountId: this.recordId });
            this.showToast('Success', 'Contact created', 'success');
            refreshApex(this.wiredContactsResult);
        } catch (error) {
            this.showToast('Error', error.body.message, 'error');
        } finally {
            this.isLoading = false;
        }
    }
    
    showToast(title, message, variant) {
        this.dispatchEvent(new ShowToastEvent({ title, message, variant }));
    }
}
```

```html
<!-- myComponent.html -->
<template>
    <lightning-card title={accountName} icon-name="standard:account">
        <!-- Loading spinner -->
        <template if:true={isLoading}>
            <lightning-spinner alternative-text="Loading..."></lightning-spinner>
        </template>
        
        <!-- Error display -->
        <template if:true={error}>
            <div class="slds-text-color_error">
                {error.body.message}
            </div>
        </template>
        
        <!-- Data display -->
        <template if:true={contacts}>
            <lightning-datatable
                key-field="id"
                data={contacts}
                columns={columns}
                hide-checkbox-column>
            </lightning-datatable>
        </template>
        
        <!-- Actions -->
        <div slot="footer">
            <lightning-button 
                label="Refresh" 
                onclick={handleRefresh}>
            </lightning-button>
            <lightning-button 
                label="New Contact" 
                variant="brand"
                onclick={handleCreateContact}>
            </lightning-button>
        </div>
    </lightning-card>
</template>
```

```css
/* myComponent.css */
.my-custom-class {
    background-color: #f3f3f3;
    padding: 1rem;
}
```

### Component Communication

#### Parent to Child (@api)
```javascript
// childComponent.js
import { LightningElement, api } from 'lwc';

export default class ChildComponent extends LightningElement {
    @api message;
    
    @api
    publicMethod() {
        // Can be called from parent
        return 'Called from parent';
    }
}
```

#### Child to Parent (Custom Event)
```javascript
// childComponent.js
handleClick() {
    const event = new CustomEvent('itemselected', {
        detail: { id: this.itemId, name: this.itemName },
        bubbles: true,      // bubble up through DOM
        composed: true      // cross shadow boundary
    });
    this.dispatchEvent(event);
}

// parentComponent.html
<template>
    <c-child-component onitemselected={handleItemSelected}></c-child-component>
</template>
```

#### Pub-Sub (Unrelated Components)
```javascript
// pubsub.js (utility)
const events = {};

export default {
    register(eventName, callback) {
        if (!events[eventName]) {
            events[eventName] = new Set();
        }
        events[eventName].add(callback);
    },
    
    unregister(eventName, callback) {
        if (events[eventName]) {
            events[eventName].delete(callback);
        }
    },
    
    fire(eventName, data) {
        if (events[eventName]) {
            events[eventName].forEach(callback => {
                try {
                    callback(data);
                } catch (error) {
                    console.error(error);
                }
            });
        }
    }
};

// Or use Lightning Message Service for cross-tab communication
```

## Governor Limits Quick Reference

| Limit | Synchronous | Asynchronous |
|-------|-------------|--------------|
| SOQL queries | 100 | 200 |
| Query rows | 50,000 | 50,000 |
| SOSL queries | 20 | 20 |
| DML statements | 150 | 150 |
| DML rows | 10,000 | 10,000 |
| Heap size | 6 MB | 12 MB |
| CPU time | 10,000 ms | 60,000 ms |
| Max timeout | 10 min (callout) | 5 min (Queueable) |

---

> **Best Practice**: Always write unit tests with @IsTest annotation, minimum 75% coverage required for deployment
