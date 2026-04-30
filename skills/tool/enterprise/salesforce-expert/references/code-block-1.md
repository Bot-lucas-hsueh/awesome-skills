# java Example

```
public class OpportunityTriggerHandler {
    private static boolean alreadyRan = false;

    public static void run() {
        if (alreadyRan) return;
        alreadyRan = true;

        if (Trigger.isBefore && Trigger.isInsert) {
            handleBeforeInsert(Trigger.new);
        }
        if (Trigger.isAfter && Trigger.isUpdate) {
            handleAfterUpdate(Trigger.new, Trigger.oldMap);
        }
    }

    private static void handleBeforeInsert(List<Opportunity> newList) {
        for (Opportunity opp : newList) {
            if (opp.Amount == null) {
                opp.Amount = 0;
            }
            opp.Description = 'Created: ' + Date.today();
        }
    }

    private static void handleAfterUpdate(
        List<Opportunity> newList,
        Map<Id, Opportunity> oldMap
    ) {
        List<Task> tasksToCreate = new List<Task>();
        for (Opportunity opp : newList) {
            Opportunity old = oldMap.get(opp.Id);
            if (opp.IsWon && !old.IsWon) {
                tasksToCreate.add(new Task(
                    WhatId = opp.Id,
                    Subject = 'Post-sale follow up',
                    OwnerId = opp.OwnerId,
                    ActivityDate = Date.today().addDays(3)
                ));
            }
        }
        if (!tasksToCreate.isEmpty()) {
            insert tasksToCreate;
        }
    }
}
```
