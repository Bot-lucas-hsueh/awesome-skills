# Integration Hub Guide

## Overview
Integration Hub enables connectivity to 200+ enterprise systems through pre-built spokes.

## Architecture
```
┌─────────────────────────────────────────────────────────┐
│              INTEGRATION HUB                            │
├─────────────────────────────────────────────────────────┤
│  Spokes: Pre-built connectors                           │
│  • Microsoft: Office 365, Teams, Azure AD              │
│  • AWS: EC2, S3, Lambda                                │
│  • Salesforce: CRM, Service Cloud                      │
│  • SAP: ERP, S/4HANA                                   │
│  • Workday: HR, Financials                             │
├─────────────────────────────────────────────────────────┤
│  Custom Integrations:                                   │
│  • REST/HTTP                                            │
│  • SOAP                                                 │
│  • JDBC                                                 │
│  • PowerShell                                           │
├─────────────────────────────────────────────────────────┤
│  MID Server: On-premise gateway                         │
│  (For systems behind firewall)                          │
└─────────────────────────────────────────────────────────┘
```

## Common Spokes

### Microsoft Office 365
```yaml
Actions:
  - Create meeting
  - Send email
  - Create calendar event
  - Manage user

Configuration:
  - Azure AD app registration
  - OAuth 2.0 credentials
  - API permissions granted
```

### Active Directory
```yaml
Actions:
  - Create user
  - Update user
  - Add to group
  - Reset password
  - Disable account

Use Cases:
  - Employee onboarding
  - Access management
  - Offboarding automation
```

### AWS
```yaml
Actions:
  - EC2: Start, stop, terminate instances
  - S3: Upload, download files
  - Lambda: Invoke functions
  - CloudWatch: Get metrics

Use Cases:
  - Cloud resource management
  - Automated provisioning
  - Cost optimization
```

## Custom Integration Pattern

### REST Message
```javascript
// Define REST message
var r = new sn_ws.RESTMessageV2('My Integration', 'POST');
r.setEndpoint('https://api.example.com/v1/data');
r.setRequestHeader('Authorization', 'Bearer ' + token);
r.setRequestBody(JSON.stringify(payload));

// Execute
var response = r.execute();
var body = response.getBody();
var status = response.getStatusCode();
```

### Error Handling
```yaml
Retry Strategy:
  - Attempt 1: Immediate
  - Attempt 2: Wait 30 seconds
  - Attempt 3: Wait 2 minutes
  - Final: Create failed task

Error Types:
  - Timeout: Retry
  - Auth failure: Alert admin
  - Data validation: Create error record
  - Server error: Retry with backoff
```

## MID Server

### When Required
- Systems behind corporate firewall
- On-premise databases
- Legacy systems without APIs
- File system operations

### Setup
```yaml
Requirements:
  - Windows or Linux server
  - Java 11+
  - Network access to target systems
  - HTTPS to ServiceNow instance

Configuration:
  1. Download MID Server package
  2. Configure config.xml
  3. Start MID Server service
  4. Validate in instance
  5. Configure capabilities
```

### Capabilities
- JDBC
- SSH
- PowerShell
- FTP/SFTP
- REST/SOAP
- LDAP

## Security

### Credentials
```yaml
Storage:
  - Credential alias in ServiceNow
  - Never hardcode in scripts
  - Use OAuth where possible
  - Rotate regularly

Types:
  - Basic Auth
  - OAuth 2.0
  - API Keys
  - Certificate-based
```

### Data Protection
- Encrypt sensitive data in transit
- Validate all inputs
- Sanitize outputs
- Log without exposing secrets

## Monitoring

### Integration Health Dashboard
- Success/failure rates
- Average response times
- API rate limits
- Error trends

### Alerting
```yaml
Critical Alerts:
  - Authentication failures
  - Success rate < 95%
  - Response time > 10 seconds

Warning Alerts:
  - Success rate < 98%
  - Retry rate > 5%
  - Rate limit approaching
```
