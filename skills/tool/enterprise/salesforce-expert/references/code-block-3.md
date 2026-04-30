# SOQL/Apex Examples

## SOQL Query — Opportunities with Related Data

```soql
SELECT
    Id,
    Name,
    Amount,
    CloseDate,
    StageName,
    Account.Id,
    Account.Name,
    Account.Industry,
    Owner.Name,
    (SELECT Id, Subject, Status, ActivityDate
     FROM Tasks
     WHERE Status != 'Completed')
FROM Opportunity
WHERE StageName = 'Closed Won'
  AND CloseDate = LAST_N_DAYS:30
ORDER BY Amount DESC NULLS LAST
LIMIT 100
```

## Apex Trigger — Task on Opportunity Won (Example 1)

```java
trigger OpportunityTask on Opportunity (after update) {
    List<Task> tasks = new List<Task>();
    for (Opportunity opp : Trigger.new) {
        Opportunity old = Trigger.oldMap.get(opp.Id);
        if (opp.IsWon && !old.IsWon) {
            tasks.add(new Task(
                WhatId = opp.Id,
                Subject = 'Follow up with customer',
                OwnerId = opp.OwnerId,
                ActivityDate = Date.today().addDays(3),
                Priority = 'High'
            ));
        }
    }
    insert tasks;
}
```

## LWC Component — Opportunity Details (Example 3)

**oppDetail.html:**
```html
<template>
    <lightning-card title="Opportunity Details">
        <template if:true={opportunity.data}>
            <div class="slds-p-around_medium">
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Amount:</strong> <lightning-formatted-number value={amount} format-style="currency"></lightning-formatted-number></p>
                <p><strong>Stage:</strong> {stage}</p>
                <lightning-button label="Close Opportunity" onclick={closeOpportunity}></lightning-button>
            </div>
        </template>
    </lightning-card>
</template>
```

**oppDetail.js:**
```javascript
import { LightningElement, api, wire } from 'lwc';
import { getRecord, updateRecord } from 'lightning/uiRecordApi';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import OPP_NAME from '@salesforce/schema/Opportunity.Name';
import OPP_AMOUNT from '@salesforce/schema/Opportunity.Amount';
import OPP_STAGE from '@salesforce/schema/Opportunity.StageName';

export default class OppDetail extends LightningElement {
    @api recordId;

    @wire(getRecord, {
        recordId: '$recordId',
        fields: [OPP_NAME, OPP_AMOUNT, OPP_STAGE]
    })
    opportunity;

    get name() { return this.opportunity.data?.Name; }
    get amount() { return this.opportunity.data?.Amount; }
    get stage() { return this.opportunity.data?.StageName; }

    closeOpportunity() {
        const fields = { Id: this.recordId, StageName: 'Closed Won' };
        updateRecord({ fields })
            .then(() => {
                this.dispatchEvent(new ShowToastEvent({
                    title: 'Success', message: 'Opportunity closed', variant: 'success'
                }));
            });
    }
}
```
