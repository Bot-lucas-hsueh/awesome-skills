# Flow/Apex Examples

## Record-Triggered Flow — Auto-create Task on Opportunity Won

```
Trigger: Opportunity, When: Record is Updated
Condition: IsClosed = true AND (IsWon = true AND PRIORVALUE(IsWon) = false)
Actions:
  1. Create Records → Task
     - WhatId: {!$Record.Id}
     - Subject: "Follow up with customer"
     - OwnerId: {!$Record.OwnerId}
     - ActivityDate: {!$Flow.CurrentDate} + 3
  2. Send Custom Notification (optional)
```

## Screen Flow — Lead Qualification Wizard

```
Screen 1: Basic Info (Get Lead data)
Screen 2: Qualification Questions (Choice components)
Decision: Score >= 80?
  → Yes: Update Lead.Status = 'Qualified', Create Task
  → No: Update Lead.Status = 'Nurturing', Send Notification
```

## LWC JavaScript Pattern

```javascript
import { LightningElement, wire, api } from 'lwc';
import { getRecord, getFieldValue } from 'lightning/uiRecordApi';
import ACCOUNT_NAME_FIELD from '@salesforce/schema/Opportunity.Account.Name';
import STAGE_NAME_FIELD from '@salesforce/schema/Opportunity.StageName';

export default class OpportunityCard extends LightningElement {
    @api recordId;

    @wire(getRecord, {
        recordId: '$recordId',
        fields: [ACCOUNT_NAME_FIELD, STAGE_NAME_FIELD]
    })
    opportunity;

    get accountName() {
        return getFieldValue(this.opportunity.data, ACCOUNT_NAME_FIELD);
    }

    get isClosedWon() {
        return getFieldValue(this.opportunity.data, STAGE_NAME_FIELD) === 'Closed Won';
    }
}
```

## Recursive Trigger Guard (Edge Case §11.1)

```java
public class AccountTriggerHandler {
    private static boolean inProgress = false;
    public static void handle() {
        if (inProgress) return;
        inProgress = true;
        // trigger logic
    }
}
```
