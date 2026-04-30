# Salesforce Security Best Practices

## Security Model Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                              │
├─────────────────────────────────────────────────────────────────┤
│  Layer 1: Organization-Wide Defaults (OWD)                      │
│  Layer 2: Role Hierarchy                                        │
│  Layer 3: Sharing Rules                                         │
│  Layer 4: Profiles & Permission Sets                            │
│  Layer 5: Field-Level Security                                  │
│  Layer 6: Record-Level Security (Apex/Manual)                   │
└─────────────────────────────────────────────────────────────────┘
```

## Organization-Wide Defaults (OWD)

### Access Levels
| Setting | Description | Use Case |
|---------|-------------|----------|
| **Private** | Only owner and above have access | Sensitive data (HR, Financial) |
| **Public Read Only** | All can view, owner can edit | Reference data |
| **Public Read/Write** | All can view and edit | Collaboration scenarios |
| **Controlled by Parent** | Child inherits parent access | Related objects |

### Recommended Defaults
```
Account: Private
Contact: Controlled by Parent
Opportunity: Private
Case: Private
Lead: Private
Custom Objects: Evaluate based on sensitivity
```

## Role Hierarchy

```
                    CEO
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    VP Sales    VP Service   VP Marketing
        │            │            │
   ┌────┴────┐   ┌───┴───┐    ┌───┴───┐
   ↓         ↓   ↓       ↓    ↓       ↓
Director  Director Mgrs  Mgrs Dir     Dir
   │         │    │       │    │       │
  Reps      Reps  Reps   Reps Reps   Reps
```

**Key Principle**: Managers can see records owned by or shared with their subordinates.

**Best Practices**:
- Keep hierarchy flat when possible
- Use territories for complex access patterns
- Regular cleanup of inactive roles

## Sharing Rules

### Criteria-Based Sharing
```
Share Opportunities WHERE:
  Industry = "Healthcare" AND
  Amount > 100000
WITH: Healthcare Sales Team (Public Group)
```

### Owner-Based Sharing
```
Share records owned by:
  Role: "East Coast Sales"
WITH:
  Role: "West Coast Sales"
```

**Limits**:
- 300 total sharing rules per object
- 50 criteria-based rules per object
- Evaluate asynchronously when > 25 rules

## Profiles vs Permission Sets

### Profiles (Legacy Identity)
```yaml
Profile: Standard User
License: Salesforce
Tab Settings:
  Accounts: Default On
  Contacts: Default On
  Custom_App__c: Default Off
Object Permissions:
  Account:
    Read: true
    Create: true
    Edit: true
    Delete: false
Field Permissions:
  Account.Social_Security_Number__c:
    Read: false
    Edit: false
```

### Permission Sets (Modern Approach)
```yaml
Permission Set: Sales_User_Permissions
Description: Core permissions for sales users

Object Permissions:
  Opportunity:
    Read: true
    Create: true
    Edit: true
    Delete: false
    View All: false
    Modify All: false

Field Permissions:
  Opportunity.Discount_Approved__c:
    Read: true
    Edit: true

Apex Class Access:
  - OpportunityController
  - PricingService

Visualforce Page Access:
  - OpportunityEdit

Custom Permissions:
  - Can_Approve_Discounts
```

### Permission Set Groups
```
Sales Representative:
├── Base User Permissions (PSG)
├── Sales Cloud Permissions (PS)
├── CPQ Permissions (PS)
└── Opportunity-to-Order (PS)
```

## Field-Level Security

### Implementation
```java
// Always check FLS in Apex
public with sharing class SecureController {
    
    public List<Account> getAccounts() {
        // Schema describes check field accessibility
        if (Schema.sObjectType.Account.fields.Name.isAccessible() &&
            Schema.sObjectType.Account.fields.Industry.isAccessible()) {
            
            return [SELECT Name, Industry FROM Account LIMIT 100];
        }
        return new List<Account>();
    }
}
```

### StripInaccessible Pattern (Security.stripInaccessible)
```java
List<Account> accounts = [SELECT Id, Name, Secret_Field__c FROM Account];

// Remove fields user can't access
SObjectAccessDecision decision = Security.stripInaccessible(
    AccessType.READABLE,
    accounts
);

List<Account> safeAccounts = (List<Account>) decision.getRecords();
// safeAccounts now only contains accessible fields
```

## Shield Platform Encryption

### Deterministic Encryption
- Allows filtering (WHERE clauses)
- Same value = same encrypted value
- Use for: External IDs, picklists

### Probabilistic Encryption
- Maximum security
- Random ciphertext each time
- Use for: Sensitive text, comments

### Setup
```
Setup → Platform Encryption → Encryption Policy
├── Encrypt Fields:
│   ├── Account.Social_Security_Number__c (Deterministic)
│   ├── Contact.Credit_Card_Number__c (Probabilistic)
│   └── Case.Customer_Feedback__c (Probabilistic)
├── Encrypt Files
└── Encrypt Attachments
```

## Event Monitoring

### Transaction Security Policies
```java
// Apex Policy for suspicious login
public class SuspiciousLoginPolicy implements TxnSecurity.Policy {
    
    public boolean evaluate(TxnSecurity.Event e) {
        // Check if login from unexpected country
        LoginHistory lh = [
            SELECT SourceIp, Country FROM LoginHistory 
            WHERE Id = :e.entityId
        ];
        
        Set<String> allowedCountries = new Set<String>{'US', 'CA', 'UK'};
        return !allowedCountries.contains(lh.Country);
    }
}
```

### Event Types to Monitor
- Report exports (data exfiltration)
- Permission changes
- Login anomalies
- Setup changes
- Data exports

## Privacy Compliance

### Privacy Center
```
Setup → Privacy Center
├── Consent Management
│   ├── Capture consent preferences
│   ├── Track consent history
│   └── Respect consent in marketing
├── Data Subject Requests
│   ├── Right to Access
│   ├── Right to Delete
│   └── Right to Portability
└── Retention Policies
    ├── Automatic data deletion
    └── Archive before deletion
```

### GDPR/CCPA Compliance Checklist
- [ ] Consent tracking enabled
- [ ] Data retention policies defined
- [ ] DSR automation configured
- [ ] Privacy policy updated
- [ ] Cookie consent implemented
- [ ] Data processing agreements signed

## Secure Coding

### SOQL Injection Prevention
```java
// BAD - vulnerable to injection
String name = ApexPages.currentPage().getParameters().get('name');
List<Account> accs = Database.query('SELECT Id FROM Account WHERE Name = \'' + name + '\'');

// GOOD - use binding variables
String name = ApexPages.currentPage().getParameters().get('name');
List<Account> accs = [SELECT Id FROM Account WHERE Name = :name];

// GOOD - use escapeSingleQuotes if dynamic
String name = String.escapeSingleQuotes(
    ApexPages.currentPage().getParameters().get('name')
);
```

### XSS Prevention
```java
// BAD - unescaped output
public String getUserInput() {
    return ApexPages.currentPage().getParameters().get('input');
}

// GOOD - HTML encode output
public String getUserInput() {
    return EncodingUtil.urlEncode(
        ApexPages.currentPage().getParameters().get('input'),
        'UTF-8'
    );
}
```

### CRUD/FLS Enforcement
```java
public with sharing class SecureController {
    
    public void updateAccount(Account acc) {
        // Check object-level permissions
        if (!Schema.sObjectType.Account.isUpdateable()) {
            throw new SecurityException('Insufficient privileges');
        }
        
        // Check field-level permissions
        if (!Schema.sObjectType.Account.fields.Name.isUpdateable()) {
            throw new SecurityException('Cannot update Name field');
        }
        
        update acc;
    }
}
```

## Health Check

```
Setup → Security → Health Check

Recommended Settings:
├── Password Policies
│   ├── Minimum length: 10
│   ├── Complexity: Alphanumeric + special
│   └── Lockout: 5 attempts
├── Session Settings
│   ├── Timeout: 2 hours
│   ├── IP restrictions for API
│   └── Secure cookies
├── Network Access
│   ├── Trusted IP ranges
│   └── Login IP ranges per profile
└── Certificate Management
    └── Valid SSL certificates
```

## Security Review Checklist

### Pre-Deployment
- [ ] Sharing model documented
- [ ] FLS enforced in all Apex
- [ ] No hardcoded credentials
- [ ] Named credentials for callouts
- [ ] SOQL injection prevention
- [ ] XSS protection
- [ ] CRUD checks implemented
- [ ] Shield encryption applied to sensitive fields

### Post-Deployment
- [ ] Login history reviewed weekly
- [ ] Permission set assignments audited
- [ ] Event monitoring alerts configured
- [ ] Data backup verified
- [ ] Security Health Check score > 90%

---

> **Golden Rule**: Default to `with sharing` in Apex classes. Only use `without sharing` when explicitly necessary and document why.
