# Scenario Examples

## 9.1 Bulk Record Processing

**User:** "We need to process 50,000 records nightly. How do we handle this efficiently?"

**Expert:**
> **Solution with Batch Apex:**
>
> ```apex
> // Batch class for bulk processing
> public class ProcessContactsBatch implements Database.Batchable<SObject> {
>
>     private String query;
>     private Map<String, Object> parameters;
>
>     public ProcessContactsBatch() {
>         this.query = 'SELECT Id, FirstName, LastName, Email, ' +
>                      'AccountId, MailingState ' +
>                      'FROM Contact ' +
>                      'WHERE Active__c = true AND Email = null ' +
>                      'ORDER BY LastModifiedDate DESC';
>     }
>
>     public Database.QueryLocator start(Database.BatchableContext BC) {
>         return Database.getQueryLocator(query);
>     }
>
>     public void execute(Database.BatchableContext BC, List<Contact> scope) {
>         List<Contact> contactsToUpdate = new List<Contact>();
>         List<Database.Error> errors = new List<Database.Error>();
>
>         for (Contact con : scope) {
>             try {
>                 // Process each contact
>                 con.Email = generateEmail(con);
>                 con.State__c = standardizeState(con.MailingState);
>                 contactsToUpdate.add(con);
>             } catch (Exception e) {
>                 errors.add(new Database.Error(
>                     'Processing error: ' + e.getMessage(), con.Id
>                 ));
>             }
>         }
>
>         // Use allOrNone=false to continue on partial success
>         Database.SaveResult[] results = Database.update(
>             contactsToUpdate, false
>         );
>
>         // Handle individual failures
>         for (Integer i = 0; i < results.size(); i++) {
>             if (!results[i].isSuccess()) {
>                 System.debug('Failed: ' + contactsToUpdate[i].Id +
>                     ' Error: ' + results[i].getErrors());
>             }
>         }
>     }
>
>     public void finish(Database.BatchableContext BC) {
>         // Get job status
>         AsyncApexJob job = [
>             SELECT Id, Status, JobItemsProcessed,
>                    TotalJobItems, NumberOfErrors
>             FROM AsyncApexJob
>             WHERE Id = :BC.getJobId()
>         ];
>
>         // Send email notification
>         sendNotification(job);
>     }
>
>     private String generateEmail(Contact con) {
>         return (con.FirstName != null ? con.FirstName.left(1) : '') +
>                con.LastName + '@example.com';
>     }
>
>     private String standardizeState(String state) {
>         if (String.isBlank(state)) return null;
>         Map<String, String> stateMap = new Map<String, String>{
>             'CALIFORNIA' => 'CA', 'NEW YORK' => 'NY'
>         };
>         return stateMap.get(state.toUpperCase());
>     }
>
>     private void sendNotification(AsyncApexJob job) {
>         Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
>         mail.setToAddresses(new String[]{'admin@example.com'});
>         mail.setSubject('Batch Process Complete: ' + job.Status);
>         mail.setPlainTextBody(
>             'Processed ' + job.TotalJobItems + ' batches with ' +
>             job.NumberOfErrors + ' errors.'
>         );
>         Messaging.sendEmail(new Messaging.SingleEmailMessage[]{mail});
>     }
> }
>
> // Execute from anonymous Apex
> System.scheduleBatch(
>     new ProcessContactsBatch(),
>     'NightlyContactProcessing',
>     60,  // minutes
>     200  // batch size
> );
> ```

## 9.2 Platform Events Integration

**User:** "How do we integrate Salesforce with an external ERP system using events?"

**Expert:**
> **Solution:**
>
> **1. Create Platform Event:**
> ```xml
> <!-- In src/objects/Order_Event__e.object -->
> <?xml version="1.0" encoding="UTF-8"?>
> <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
>     <eventPayload>{"OrderId__c":"{!Order__c.Id}","Status__c":"{!Order__c.Status__c}"}</eventPayload>
>     <fields>
>         <name>Order_Id__c</name>
>         <type>Text</type>
>         <length>18</length>
>     </fields>
>     <fields>
>         <name>Status__c</name>
>         <type>Picklist</type>
>     </fields>
> </CustomObject>
> ```
>
> **2. Publish Event from Flow:**
> ```apex
> // Apex Action to publish event
> public class OrderEventPublisher {
>     @InvocableMethod(label='Publish Order Event')
>     public static void publishOrderEvents(List<Order> orders) {
>         List<Order_Event__e> events = new List<Order_Event__e>();
>
>         for (Order ord : orders) {
>             events.add(new Order_Event__e(
>                 Order_Id__c = ord.Id,
>                 Status__c = ord.Status
>             ));
>         }
>
>         EventBus.publish(events);
>     }
> }
> ```
>
> **3. Subscribe with Trigger:**
> ```apex
> trigger OrderEventTrigger on Order_Event__e(after insert) {
>     for (Order_Event__e event : Trigger.New) {
>         if (event.Status__c == 'Fulfilled') {
>             // Call ERP system
>             callERP(event.Order_Id__c);
>         }
>     }
> }
> ```
>
> **4. CometD Subscription (External System):**
> ```javascript
> // Subscribe to platform events from external system
> const subscribeToOrderEvents = () => {
>     const replayId = -1;  // Get all events
>
>     const subscription = emitter.subscribe(
>         '/event/Order_Event__e',
>         replayId,
>         (event) => {
>             console.log('Order Event:', event.data.payload);
>             processOrderEvent(event.data.payload);
>         }
>     );
> };
> ```

## 9.3 Custom REST API

**User:** "How do we expose custom endpoints for our mobile app?"

**Expert:**
> **Solution:**
>
> ```apex
> // Custom REST API Controller
> @RestResource(urlMapping='/mobile/v1/orders/*')
> global with sharing class MobileOrderAPI {
>
>     @HttpGet
>     global static OrderWrapper getOrder() {
>         RestRequest request = RestContext.request;
>         String orderId = request.requestURI
>             .substringAfter('/mobile/v1/orders/')
>             .substringBefore('/');
>
>         Order ord = [
>             SELECT Id, OrderNumber, Account.Name, Status,
>                    TotalAmount,
>                    (SELECT Quantity, UnitPrice, PricebookEntry.Product2.Name
>                     FROM OrderItems)
>             FROM Order
>             WHERE Id = :orderId
>             WITH SECURITY_ENFORCED
>             LIMIT 1
>         ];
>
>         return new OrderWrapper(ord);
>     }
>
>     @HttpPost
>     global static OrderResponse createOrder(OrderInput input) {
>         try {
>             Order newOrder = new Order(
>                 AccountId = input.accountId,
>                 EffectiveDate = Date.today(),
>                 Status = 'Draft',
>                 ShippingCity = input.shippingCity,
>                 ShippingState = input.shippingState
>             );
>
>             insert newOrder;
>
>             // Create order items
>             List<OrderItem> items = new List<OrderItem>();
>             for (OrderItemInput item : input.items) {
>                 items.add(new OrderItem(
>                     OrderId = newOrder.Id,
>                     PricebookEntryId = item.pricebookEntryId,
>                     Quantity = item.quantity,
>                     UnitPrice = item.unitPrice
>                 ));
>             }
>             insert items;
>
>             return new OrderResponse(true, newOrder.Id, 'Order created');
>
>         } catch (DMLException e) {
>             return new OrderResponse(false, null, e.getMessage());
>         }
>     }
>
>     @HttpPatch
>     global static OrderResponse updateOrderStatus() {
>         RestRequest request = RestContext.request;
>         String orderId = request.requestURI
>             .substringAfter('/mobile/v1/orders/');
>
>         Map<String, Object> body = (Map<String, Object>)
>             JSON.deserializeUntyped(request.requestBody.toString());
>
>         Order ord = [SELECT Id FROM Order WHERE Id = :orderId];
>         ord.Status = (String) body.get('status');
>         update ord;
>
>         return new OrderResponse(true, ord.Id, 'Status updated');
>     }
>
>     // Wrapper classes
>     global class OrderWrapper {
>         public String orderId;
>         public String orderNumber;
>         public String accountName;
>         public String status;
>         public Decimal totalAmount;
>         public List<OrderItemWrapper> items;
>
>         public OrderWrapper(Order ord) {
>             this.orderId = ord.Id;
>             this.orderNumber = ord.OrderNumber;
>             this.accountName = ord.Account.Name;
>             this.status = ord.Status;
>             this.totalAmount = ord.TotalAmount;
>             this.items = new List<OrderItemWrapper>();
>             for (OrderItem item : ord.OrderItems) {
>                 items.add(new OrderItemWrapper(item));
>             }
>         }
>     }
>
>     global class OrderInput {
>         public Id accountId;
>         public String shippingCity;
>         public String shippingState;
>         public List<OrderItemInput> items;
>     }
>
>     global class OrderItemInput {
>         public Id pricebookEntryId;
>         public Integer quantity;
>         public Decimal unitPrice;
>     }
>
>     global class OrderResponse {
>         public Boolean success;
>         public Id orderId;
>         public String message;
>
>         public OrderResponse(Boolean success, Id orderId, String message) {
>             this.success = success;
>             this.orderId = orderId;
>             this.message = message;
>         }
>     }
> }
> ```

## 9.4 Dynamic Apex: Query Builder

**User:** "How do we build a flexible query builder that handles various filters?"

**Expert:**
> **Solution:**
>
> ```apex
> public class QueryBuilder {
>     private String baseQuery;
>     private List<String> selectFields;
>     private List<String> whereConditions;
>     private List<String> orderByFields;
>     private List<Object> bindValues;
>     private Integer bindIndex = 0;
>
>     public QueryBuilder(String objectName) {
>         this.selectFields = new List<String>();
>         this.whereConditions = new List<String>();
>         this.orderByFields = new List<String>();
>         this.bindValues = new List<Object>();
>         this.baseQuery = 'SELECT {0} FROM ' + objectName;
>     }
>
>     public QueryBuilder select(List<String> fields) {
>         this.selectFields.addAll(fields);
>         return this;
>     }
>
>     public QueryBuilder selectAll() {
>         this.selectFields.add('Id');
>         return this;
>     }
>
>     public QueryBuilder whereEquals(String field, Object value) {
>         bindIndex++;
>         this.whereConditions.add(field + ' = :val' + bindIndex);
>         this.bindValues.add(value);
>         return this;
>     }
>
>     public QueryBuilder whereNotEquals(String field, Object value) {
>         bindIndex++;
>         this.whereConditions.add(field + ' != :val' + bindIndex);
>         this.bindValues.add(value);
>         return this;
>     }
>
>     public QueryBuilder whereIn(String field, List<Object> values) {
>         bindIndex++;
>         this.whereConditions.add(field + ' IN :vals' + bindIndex);
>         this.bindValues.add(values);
>         return this;
>     }
>
>     public QueryBuilder whereLike(String field, String value) {
>         bindIndex++;
>         this.whereConditions.add(field + ' LIKE :val' + bindIndex);
>         this.bindValues.add('%' + value + '%');
>         return this;
>     }
>
>     public QueryBuilder whereGreaterThan(String field, Object value) {
>         bindIndex++;
>         this.whereConditions.add(field + ' > :val' + bindIndex);
>         this.bindValues.add(value);
>         return this;
>     }
>
>     public QueryBuilder orderBy(String field) {
>         this.orderByFields.add(field);
>         return this;
>     }
>
>     public QueryBuilder orderByDesc(String field) {
>         this.orderByFields.add(field + ' DESC');
>         return this;
>     }
>
>     public QueryBuilder limitRecords(Integer limitCount) {
>         this.baseQuery += ' LIMIT ' + limitCount;
>         return this;
>     }
>
>     public String toSOQL() {
>         // Build SELECT clause
>         String fields = selectFields.isEmpty() ? 'Id' :
>                         String.join(selectFields, ', ');
>
>         String query = String.format(
>             baseQuery.replace('{0}', fields),
>             new List<String>()
>         );
>
         if (!whereConditions.isEmpty()) {
>             query += ' WHERE ' + String.join(whereConditions, ' AND ');
>         }
>
>         if (!orderByFields.isEmpty()) {
>             query += ' ORDER BY ' + String.join(orderByFields, ', ');
>         }
>
>         return query;
>     }
>
>     public List<SObject> run() {
>         String query = toSOQL();
>         return Database.query(query);
>     }
>
>     public Integer count() {
>         String countQuery = 'SELECT COUNT() FROM ' +
>             baseQuery.split(' FROM ')[1].split(' LIMIT ')[0];
>         if (!whereConditions.isEmpty()) {
>             countQuery += ' WHERE ' + String.join(whereConditions, ' AND ');
>         }
>         return Database.countQuery(countQuery);
>     }
> }
>
> // Usage
> List<Account> accounts = new QueryBuilder('Account')
>     .select(new List<String>{'Id', 'Name', 'Industry'})
>     .whereEquals('Active__c', true)
>     .whereLike('Name', 'Acme')
>     .whereIn('Industry', new List<String>{'Technology', 'Healthcare'})
>     .orderByDesc('AnnualRevenue')
>     .limitRecords(100)
>     .run();
> ```

## 9.5 Scheduled Reports Delivery

**User:** "How do we schedule and email weekly reports to stakeholders?"

**Expert:**
> **Solution:**
>
> ```apex
> // Scheduled class for report delivery
> public class WeeklyReportScheduler implements Schedulable {
>
>     public void execute(SchedulableContext SC) {
>         // Get report ID
>         Id reportId = [SELECT Id FROM Report
>                        WHERE DeveloperName = 'Weekly_Sales_Summary'
>                        LIMIT 1].Id;
>
>         // Execute report asynchronously
>         System.enqueueJob(new ReportDeliveryJob(reportId));
>
>         // Reschedule for next week
>         scheduleNext();
>     }
>
>     private void scheduleNext() {
>         Datetime nextWeek = Datetime.now().addDays(7);
>         String cron = String.valueOf(nextWeek.second()) + ' ' +
>                        String.valueOf(nextWeek.minute()) + ' ' +
>                        String.valueOf(nextWeek.hour()) + ' ' +
>                        String.valueOf(nextWeek.day()) + ' ' +
>                        String.valueOf(nextWeek.month()) + ' ' +
>                        ' ? ' +
>                        String.valueOf(nextWeek.year());
>
>         System.schedule('Weekly Report ' + nextWeek, cron, new WeeklyReportScheduler());
>     }
> }
>
> public class ReportDeliveryJob implements Queueable {
>
>     private Id reportId;
>
>     public ReportDeliveryJob(Id reportId) {
>         this.reportId = reportId;
>     }
>
>     public void execute(QueueableContext context) {
>         // Get report metadata
>         Report report = [SELECT Id, Name FROM Report WHERE Id = :reportId];
>
>         // Execute async report
>         Reports.ReportResults results = Reports.ReportManager.runReport(
>             reportId, true
>         );
>
>         // Build email body
>         String emailBody = buildEmailBody(results);
>
>         // Get recipients from custom setting
>         List<String> recipients = getReportRecipients();
>
>         // Send email
>         Messaging.SingleEmailMessage email = new Messaging.SingleEmailMessage();
>         email.setToAddresses(recipients);
>         email.setSubject('Weekly Sales Report - ' + Date.today().format());
>         email.setHtmlBody(emailBody);
>         email.setSaveAsActivity(true);
>
>         Messaging.sendEmail(new Messaging.SingleEmailMessage[]{email});
>     }
>
> private String buildEmailBody(Reports.ReportResults results) {
>     Reports.Dimension dim = results.getGroupingDown();
>
>     String html = '<h1>Weekly Sales Summary</h1>';
>     html += '<p>Generated: ' + Datetime.now().format() + '</p>';
>     html += '<table border="1"><tr><th>Account</th><th>Amount</th></tr>';
>
>     if (dim != null) {
>         for (Reports.GroupingValue gv : dim.getGroupings()) {
>             Map<String, Object> groupingKey = gv.getGroupKey();
>             Reports.ReportFact fact = results.getFactMap()
>                 .get(gv.getKey() + '!T');
>
>             for (SObject record : fact.getRows()) {
>                 html += '<tr><td>' + groupingKey.get('ACCOUNT_NAME') + '</td>';
>                 html += '<td>' + record.get('AMOUNT') + '</td></tr>';
>             }
>         }
>     }
>
>     html += '</table>';
>     return html;
> }
>
> private List<String> getReportRecipients() {
>     List<String> emails = new List<String>();
>     for (Report_Recipient__c r : [
>         SELECT Email__c FROM Report_Recipient__c
>         WHERE Active__c = true AND Report_Type__c = 'Weekly'
>     ]) {
>         emails.add(r.Email__c);
>     }
>     return emails;
> }
>
> // Schedule the class
> System.schedule('Weekly Report', '0 0 8 ? * MON', new WeeklyReportScheduler());
> ```

## 9.6 External Data Integration

**User:** "How do we sync data with an external system using REST API?"

**Expert:**
> **Solution:**
>
> ```apex
> public class ExternalAccountSync {
>
>     private static final String API_ENDPOINT =
>         'https://api.external-system.com/v1';
>     private static final String API_KEY = 'EXTERNAL_API_KEY';
>
>     @Future(Callout=true)
>     public static void syncAccountsToExternal(List<Id> accountIds) {
>         List<Account> accounts = [
>             SELECT Id, Name, External_Id__c, Industry,
>                    AnnualRevenue, Website, BillingCity, BillingState
>             FROM Account
>             WHERE Id IN :accountIds
>         ];
>
>         List<AccountUpdate> updates = new List<AccountUpdate>();
>
>         for (Account acc : accounts) {
>             updates.add(new AccountUpdate(
>                 acc.Id, acc.External_Id__c, acc.Name,
>                 acc.Industry, acc.AnnualRevenue, acc.Website
>             ));
>         }
>
>         HttpRequest request = new HttpRequest();
>         request.setEndpoint('callout:ExternalSystem/services/accounts');
>         request.setMethod('POST');
>         request.setHeader('Content-Type', 'application/json');
>         request.setHeader('X-API-Key', API_KEY);
>         request.setTimeout(30000);
>         request.setBody(JSON.serialize(updates));
>
>         Http http = new Http();
>         HttpResponse response = http.send(request);
>
>         if (response.getStatusCode() == 200) {
>             handleSuccess(response.getBody(), accountIds);
>         } else {
>             handleFailure(response.getStatusCode(), response.getBody());
>         }
>     }
>
>     @Future(Callout=true)
>     public static void pullAccountsFromExternal() {
>         HttpRequest request = new HttpRequest();
>         request.setEndpoint('callout:ExternalSystem/services/accounts');
>         request.setMethod('GET');
>         request.setHeader('Accept', 'application/json');
>
>         Http http = new Http();
>         HttpResponse response = http.send(request);
>
>         if (response.getStatusCode() == 200) {
>             List<ExternalAccount> externalAccounts =
>                 (List<ExternalAccount>) JSON.deserialize(
>                     response.getBody(),
>                     List<ExternalAccount>.class
>                 );
>             processExternalAccounts(externalAccounts);
>         }
>     }
>
>     private static void processExternalAccounts(
>         List<ExternalAccount> externalAccounts
>     ) {
>         Map<String, ExternalAccount> externalMap =
>             new Map<String, ExternalAccount>();
>
>         for (ExternalAccount ea : externalAccounts) {
>             externalMap.put(ea.externalId, ea);
>         }
>
>         List<Account> existingAccounts = [
>             SELECT Id, External_Id__c, Name
>             FROM Account
>             WHERE External_Id__c IN :externalMap.keySet()
>         ];
>
>         Map<String, Account> accountMap = new Map<String, Account>();
>         for (Account acc : existingAccounts) {
>             accountMap.put(acc.External_Id__c, acc);
>         }
>
>         List<Account> toUpdate = new List<Account>();
>         List<Account> toInsert = new List<Account>();
>
>         for (ExternalAccount ea : externalAccounts) {
>             if (accountMap.containsKey(ea.externalId)) {
>                 Account acc = accountMap.get(ea.externalId);
>                 acc.Name = ea.name;
>                 acc.Industry = ea.industry;
>                 acc.AnnualRevenue = ea.revenue;
>                 toUpdate.add(acc);
>             } else {
>                 toInsert.add(new Account(
>                     Name = ea.name,
>                     External_Id__c = ea.externalId,
>                     Industry = ea.industry,
>                     AnnualRevenue = ea.revenue
>                 ));
>             }
>         }
>
>         if (!toUpdate.isEmpty()) update toUpdate;
>         if (!toInsert.isEmpty()) insert toInsert;
>     }
>
>     // Wrapper classes
>     public class AccountUpdate {
>         public String salesforceId;
>         public String externalId;
>         public String name;
>         public String industry;
>         public Decimal revenue;
>         public String website;
>
>         public AccountUpdate(String sfId, String extId, String n,
>                              String ind, Decimal rev, String web) {
>             this.salesforceId = sfId;
>             this.externalId = extId;
>             this.name = n;
>             this.industry = ind;
>             this.revenue = rev;
>             this.website = web;
>         }
>     }
>
>     public class ExternalAccount {
>         public String externalId;
>         public String name;
>         public String industry;
>         public Decimal revenue;
>     }
> }
> ```
