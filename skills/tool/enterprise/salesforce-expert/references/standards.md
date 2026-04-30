# Standards & Reference

## 7.1 Official Documentation

- [Salesforce Developers](https://developer.salesforce.com/docs)
- [Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/)
- [SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [Salesforce REST API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/)
- [Salesforce SOAP API](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_list.htm)
- [Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/)
- [Lightning Web Components](https://developer.salesforce.com/docs/component-library/bundle/lightning-progress-step/documentation)
- [Flow Builder](https://help.salesforce.com/s/articleView?id=sf.flow_builder.htm)
- [Schema Builder](https://help.salesforce.com/s/articleView?id=sf.schema_builder.htm)
- [Experience Cloud](https://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/)

## 7.2 Configuration Reference

### Salesforce CLI and Authentication

```bash
# Install Salesforce CLI
sf plugins install @salesforce/plugin-auth
sf plugins install @salesforce/plugin-data

# Authenticate (interactive)
sf org login web --set-default-dev-hub --alias my-org

# Authenticate with JWT
sf org login jwt --client-id $CONSUMER_KEY \
  --jwt-key-file ./server.key \
  --username $SF_USERNAME \
  --set-default-dev-hub

# Authenticate with access token
sf org login access-token \
  --instance-url https://myorg.salesforce.com \
  --access-token $ACCESS_TOKEN

# List orgs
sf org list

# Open org in browser
sf org open

# Display org info
sf org display --target-org my-org
```

### Data Operations

```bash
# Query with SOQL
sf data query --soql "SELECT Id, Name, Account.Name FROM Contact LIMIT 10"

# Export data
sf data export tree --query "SELECT Id, Name FROM Account LIMIT 10" \
  --output-dir ./data --prefix accounts

# Import data
sf data import tree --files ./data/accounts.json

# Bulk operations
sf data create bulk --soql "SELECT Id FROM Account WHERE Industry='Technology'"

# Get record
sf data get record --sobject Account --record-id "001XX000003GYGW"

# Update record
sf data update record --sobject Account \
  --record-id "001XX000003GYGW" \
  --values "Name='Updated Name' Industry='Technology'"
```

### Apex Operations

```bash
# Execute Apex anonymous
sf apex execute --file ./scripts/test.apex

# Run Apex tests
sf apex run test --class-names AccountServiceTest --code-coverage

# Generate test class
sf generate apex class --template UnitTest \
  --name AccountServiceTest

# Get Apex log
sf apex get log --log-id "04gXX000000XXXX"

# Tail Apex log
sf apex log tail --color
```

## 7.3 SOQL and SOSL Reference

### SOQL Examples

```sql
-- Basic query
SELECT Id, Name, Email, Account.Name, Account.Industry
FROM Contact
WHERE Account.Industry = 'Technology'
  AND Email != null
ORDER BY CreatedDate DESC
LIMIT 100

-- Aggregate queries
SELECT COUNT(Id) total,
       Account.Industry industry,
       MAX(AnnualRevenue) maxRevenue
FROM Account
GROUP BY Account.Industry
HAVING COUNT(Id) > 5

-- Relationship queries (subqueries)
SELECT Id, Name,
       (SELECT Id, Subject, Status FROM Cases),
       (SELECT Id, Name FROM Contacts)
FROM Account
WHERE Name LIKE '%Corp%'

-- Date functions
SELECT Id, Name, CreatedDate
FROM Opportunity
WHERE CreatedDate = LAST_N_DAYS:30
  AND CloseDate > TODAY

-- Polymorphic relationship
SELECT Id, WhatId, WhoId, Subject
FROM Task
WHERE What.Type = 'Account'
  AND Who.Name = 'John Doe'
```

### SOSL Examples

```sql
-- Search across objects
FIND 'Acme*' IN ALL FIELDS
RETURNING Account(Id, Name), Contact(Id, Name, Email)

-- With WHERE clause
FIND 'John' IN Name FIELDS
RETURNING Contact(Id, Name WHERE Department = 'Sales')

-- Email search
FIND '{!User.Name}' IN EMAIL FIELDS
RETURNING Case(Id, Subject, Status)
```

## 7.4 Apex Code Reference

### Class Structure

```apex
// Trigger Handler Pattern
public class AccountTriggerHandler {
    private static boolean alreadyProcessed = false;

    public static void handleBeforeInsert(List<Account> newAccounts) {
        for (Account acc : newAccounts) {
            if (String.isBlank(acc.Description)) {
                acc.Description = 'Created automatically';
            }
            // Set external ID
            acc.External_Id__c = generateExternalId(acc);
        }
    }

    public static void handleAfterInsert(Map<Id, Account> newMap) {
        List<Contact> contacts = new List<Contact>();
        for (Account acc : newMap.values()) {
            contacts.add(new Contact(
                AccountId = acc.Id,
                LastName = acc.Name + ' Primary'
            ));
        }
        if (!contacts.isEmpty()) {
            insert contacts;
        }
    }

    private static String generateExternalId(Account acc) {
        return acc.Name.left(10) + '_' + Date.today().format();
    }
}
```

### SOQL in Apex

```apex
// Safe SOQL with guard clauses
public static List<Account> getAccountsByIndustry(String industry) {
    if (String.isBlank(industry)) {
        return new List<Account>();
    }

    return [
        SELECT Id, Name, Industry, Owner.Name,
               (SELECT Id, Name FROM Contacts LIMIT 5)
        FROM Account
        WHERE Industry = :industry
        WITH SECURITY_ENFORCED
        ORDER BY Name
        LIMIT 100
    ];
}

// Aggregate SOQL
public static Map<String, Decimal> getRevenueByIndustry() {
    AggregateResult[] results = [
        SELECT Industry, SUM(AnnualRevenue) totalRevenue
        FROM Account
        WHERE AnnualRevenue != null
        GROUP BY Industry
    ];

    Map<String, Decimal> revenueMap = new Map<String, Decimal>();
    for (AggregateResult ar : results) {
        revenueMap.put(
            (String) ar.get('Industry'),
            (Decimal) ar.get('totalRevenue')
        );
    }
    return revenueMap;
}

// Dynamic SOQL
public static List<sObject> searchRecords(String objectName, String searchField, String searchValue) {
    String query = String.format(
        'SELECT Id, Name FROM {0} WHERE {1} LIKE :searchValue WITH SECURITY_ENFORCED LIMIT 100',
        new List<String>{ objectName, searchField }
    );
    return Database.query(query);
}
```

### Batch Apex

```apex
public class AccountBatchProcess implements Database.Batchable<SObject> {
    public Database.QueryLocator start(Database.BatchableContext BC) {
        return Database.getQueryLocator([
            SELECT Id, Name, Industry, AnnualRevenue
            FROM Account
            WHERE Industry = 'Technology'
        ]);
    }

    public void execute(Database.BatchableContext BC, List<Account> scope) {
        for (Account acc : scope) {
            acc.Revenue_Category__c = categorizeRevenue(acc.AnnualRevenue);
        }
        update scope;
    }

    public void finish(Database.BatchableContext BC) {
        // Send notification
        AsyncApexJob job = [
            SELECT Id, Status, JobItemsProcessed, TotalJobItems, NumberOfErrors
            FROM AsyncApexJob
            WHERE Id = :BC.getJobId()
        ];
        System.debug('Batch completed: ' + job.Status);
    }

    private String categorizeRevenue(Decimal revenue) {
        if (revenue == null) return 'Unknown';
        if (revenue < 100000) return 'Small';
        if (revenue < 1000000) return 'Medium';
        return 'Large';
    }
}

// Execute batch
Database.executeBatch(new AccountBatchProcess(), 200);
```

## 7.5 Trigger Patterns

```apex
// Trigger with handler
trigger AccountTrigger on Account (
    before insert, before update,
    after insert, after update,
    before delete, after delete
) {
    if (Trigger.isBefore) {
        if (Trigger.isInsert) {
            AccountTriggerHandler.handleBeforeInsert(Trigger.new);
        } else if (Trigger.isUpdate) {
            AccountTriggerHandler.handleBeforeUpdate(Trigger.new, Trigger.oldMap);
        } else if (Trigger.isDelete) {
            AccountTriggerHandler.handleBeforeDelete(Trigger.old);
        }
    } else if (Trigger.isAfter) {
        if (Trigger.isInsert) {
            AccountTriggerHandler.handleAfterInsert(Trigger.newMap);
        } else if (Trigger.isUpdate) {
            AccountTriggerHandler.handleAfterUpdate(Trigger.newMap, Trigger.oldMap);
        } else if (Trigger.isDelete) {
            AccountTriggerHandler.handleAfterDelete(Trigger.oldMap);
        }
        // Call Flow from trigger
        if (Trigger.isInsert || Trigger.isUpdate) {
            Flow.Interview.My_Flow flow = new Flow.Interview.My_Flow(
                new Map<String, Object>{'AccountIds' => Trigger.newMap.keySet()}
            );
            flow.start();
        }
    }
}
```

## 7.6 API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/services/data/v59.0/sobjects/` | GET | List all sObjects |
| `/services/data/v59.0/query/` | GET | Execute SOQL |
| `/services/data/v59.0/sobjects/Account` | POST | Create Account |
| `/services/data/v59.0/sobjects/Account/{id}` | GET | Get Account |
| `/services/data/v59.0/sobjects/Account/{id}` | PATCH | Update Account |
| `/services/data/v59.0/sobjects/Account/{id}` | DELETE | Delete Account |
| `/services/data/v59.0/sobjects/Account/{id}/contacts` | GET | Get related Contacts |
| `/services/data/v59.0/sobjects/Account/{id}/contacts` | POST | Create related Contact |
| `/services/data/v59.0/search/` | GET | Execute SOSL |
| `/services/data/v59.0/limits/` | GET | API limits |
| `/services/data/v59.0/sobjects/User/{id}/password` | POST | Set password |

### REST API with curl

```bash
# Get access token
curl -X POST "https://login.salesforce.com/services/oauth2/token" \
  -d "grant_type=password" \
  -d "client_id=$CLIENT_ID" \
  -d "client_secret=$CLIENT_SECRET" \
  -d "username=$USERNAME" \
  -d "password=$PASSWORD"

# Query
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  "$INSTANCE_URL/services/data/v59.0/query/?q=SELECT+Id,Name+FROM+Account"

# Create record
curl -X POST \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"Name":"Test Account","Industry":"Technology"}' \
  "$INSTANCE_URL/services/data/v59.0/sobjects/Account"

# Update record
curl -X PATCH \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"AnnualRevenue":500000}' \
  "$INSTANCE_URL/services/data/v59.0/sobjects/Account/001XX000003XXXX"
```
