# Twilio Compliance Guide

## Overview

This guide covers compliance requirements when using Twilio for communications across regulated industries.

## A2P 10DLC (US SMS)

### What is A2P 10DLC?

A2P (Application-to-Person) 10DLC (10-Digit Long Code) is a registration system for business messaging in the United States. All A2P SMS must be registered.

### Registration Requirements

**Brand Registration**:
- Legal company name
- EIN/Tax ID
- Company address
- Website URL
- Vertical/category

**Campaign Registration**:
| Field | Description |
|-------|-------------|
| Campaign name | Internal identifier |
| Use case | Standard, low-volume, mixed, etc. |
| Description | Detailed business purpose |
| Sample messages | 2-3 example messages |
| Opt-in method | Website, verbal, paper form, etc. |
| Opt-in message | Confirmation text sent |

### Throughput Limits

**Brand Trust Score Impact**:

| Trust Score | Daily Limit | TPS |
|-------------|-------------|-----|
| High (75-100) | 200,000 | 75 |
| Medium (50-74) | 20,000 | 40 |
| Low (25-49) | 10,000 | 15 |
| Unregistered | Blocked | 0 |

### Costs

| Fee Type | Amount | Frequency |
|----------|--------|-----------|
| Brand registration | $4 | One-time |
| Campaign vetting | $15 | One-time |
| Campaign fee - Standard | $10/month | Monthly |
| Campaign fee - Low-volume | $2/month | Monthly |
| Per-message carrier fees | $0.002-0.005 | Per message |

### Compliance Checklist

- [ ] Brand registered with accurate business info
- [ ] Campaign use case accurately described
- [ ] Opt-in process documented
- [ ] Opt-out handling implemented (STOP, UNSUBSCRIBE)
- [ ] Help message configured
- [ ] Message content compliant (no SHAFT)
- [ ] Sending hours appropriate (8am-9pm local)

### Prohibited Content (SHAFT)

| Category | Examples |
|----------|----------|
| **S**ex | Adult content, dating services |
| **H**ate | Discriminatory content |
| **A**lcohol | Alcohol promotions (requires age gate) |
| **F**irearms | Weapons, ammunition |
| **T**obacco | Cigarettes, vaping, cannabis |

## GDPR (EU)

### Data Subject Rights

| Right | Implementation |
|-------|----------------|
| Right to access | Export all customer data |
| Right to rectification | Update customer records |
| Right to erasure | Delete across all systems |
| Right to portability | Export in machine-readable format |
| Right to object | Opt-out processing |
| Right to restrict processing | Pause communications |

### Twilio GDPR Features

**Data Residency**:
- EU region available for data storage
- EU API endpoints: `https://api.eu.twilio.com`

**Data Processing**:
- Data Processing Addendum (DPA) available
- Standard Contractual Clauses (SCCs) for data transfer

**Deletion**:
```python
# Delete message content
client.messages('SM123...').delete()

# Note: Metadata retained for billing/legal (anonymized)
```

### Consent Management

**Required Consent Elements**:
1. Clear affirmative action (not pre-checked boxes)
2. Granular options per channel
3. Easy withdrawal mechanism
4. Record of consent timestamp and method

```javascript
// Consent tracking in Segment
traits: {
  sms_consent: true,
  sms_consent_date: '2026-03-21T10:00:00Z',
  sms_consent_source: 'website_checkout',
  email_consent: true,
  email_consent_date: '2026-03-21T10:00:00Z'
}
```

## HIPAA

### Business Associate Agreement (BAA)

**Required for HIPAA compliance**:
1. Execute BAA with Twilio
2. Use HIPAA-eligible services only
3. Implement access controls
4. Enable audit logging

**HIPAA-Eligible Services**:
- Programmable Voice
- Video (HIPAA rooms)
- SMS (without message content logging)
- Twilio Flex

**Non-HIPAA Services**:
- Email (SendGrid) - requires separate BAA
- Segment - requires separate evaluation

### Architecture Requirements

```
┌─────────────────────────────────────────┐
│           YOUR APPLICATION               │
│  (PHI stored in HIPAA-compliant DB)     │
└─────────────────┬───────────────────────┘
                  │
                  │ No PHI in Twilio
                  ▼
┌─────────────────────────────────────────┐
│            TWILIO LAYER                  │
│  - Phone numbers only                   │
│  - Call SIDs (no PHI)                   │
│  - Encrypted transit & rest             │
│  - No persistent storage of content     │
└─────────────────────────────────────────┘
```

### Implementation Checklist

- [ ] BAA executed with Twilio
- [ ] Subaccounts isolated by environment
- [ ] Access logging enabled
- [ ] Message content not logged (use SIDs only)
- [ ] Call recordings encrypted, access controlled
- [ ] Video rooms configured as HIPAA-compliant
- [ ] Audit trail maintained for 6 years

### Video HIPAA Configuration

```javascript
// HIPAA-compliant video room
const room = await client.video.v1.rooms.create({
  type: 'group',
  uniqueName: 'consultation-12345',
  statusCallback: 'https://your-server/room-events',
  recordParticipantsOnConnect: true,
  // HIPAA-specific settings
  mediaRegion: 'us1',
  video_codecs: ['VP8', 'H264'],
  audioOnly: false
});
```

**Recording Handling**:
- Encrypted at rest (AES-256)
- Access via signed URLs only
- Automatic deletion after retention period
- Audit log of all access

## TCPA (US Telemarketing)

### Consent Requirements

| Message Type | Consent Required |
|--------------|------------------|
| Informational | Implied or express |
| Transactional | Implied (existing relationship) |
| Marketing | Express written consent |

### Express Written Consent

Must include:
- Clear disclosure: "By signing, you agree to receive marketing texts"
- Message frequency (e.g., "up to 4 msgs/month")
- "Message and data rates may apply"
- Opt-out instructions: "Text STOP to stop"
- Help instructions: "Text HELP for help"
- Privacy policy link

### Quiet Hours

- **Allowed**: 8:00 AM - 9:00 PM (recipient's local time)
- **Prohibited**: 9:00 PM - 8:00 AM
- **Exceptions**: Transactional messages (fraud alerts)

### Penalties

- $500 per violation (negligent)
- $1,500 per violation (willful)
- Class action exposure

## CAN-SPAM (US Email)

### Requirements

1. **Header Accuracy**: Accurate From, To, Reply-To
2. **Subject Honesty**: No deceptive subject lines
3. **Physical Address**: Valid postal address in email
4. **Unsubscribe**: Clear mechanism, honored within 10 days
5. **Identification**: Clear that message is an advertisement

### Opt-Out Handling

```python
# Process unsubscribe
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form['email']
    
    # Update suppression list
    suppress_email(email)
    
    # Sync to all systems
    segment.identify(email, {
        'email_unsubscribed': True,
        'email_unsubscribed_date': datetime.utcnow().isoformat()
    })
    
    return 'Unsubscribed successfully', 200
```

## International Compliance

### Canada (CASL)

- **Consent**: Express consent required for CEMs
- **Identification**: Clear sender identification
- **Unsubscribe**: Must be functional for 60 days

### UK (PECR)

- Electronic marketing requires consent
- B2B: Can email corporate addresses without consent
- B2C: Requires opt-in consent

### Australia (Spam Act)

- Consent required (express or inferred)
- Identify sender
- Include unsubscribe

### India (TRAI)

- DND (Do Not Disturb) registry check required
- Template-based messaging
- Entity and template registration

## Compliance Automation

### Automated Opt-Out Handling

```python
class ComplianceHandler:
    OPT_OUT_KEYWORDS = ['stop', 'unsubscribe', 'cancel', 'quit', 'end']
    HELP_KEYWORDS = ['help', 'info', 'support']
    
    def process_inbound(self, message_body, from_number):
        body_lower = message_body.lower().strip()
        
        if any(kw in body_lower for kw in self.OPT_OUT_KEYWORDS):
            self.handle_opt_out(from_number)
            return 'You have been unsubscribed. Reply START to resubscribe.'
        
        if any(kw in body_lower for kw in self.HELP_KEYWORDS):
            return self.get_help_message()
        
        return None  # Process normally
    
    def handle_opt_out(self, phone_number):
        # Update all systems
        db.execute("""
            UPDATE contacts 
            SET sms_opt_out = TRUE, 
                sms_opt_out_date = NOW() 
            WHERE phone = %s
        """, (phone_number,))
        
        segment.identify(phone_number, {
            'sms_opt_out': True,
            'sms_opt_out_date': datetime.utcnow().isoformat()
        })
        
        # Add to suppression list
        twilio.suppressions.create(
            messaging_service_sid='MG...',
            phone_number=phone_number
        )
```

### Quiet Hours Enforcement

```python
def is_quiet_hours(phone_number):
    """Check if current time is quiet hours for phone number"""
    timezone = get_timezone_from_number(phone_number)
    local_time = datetime.now(pytz.timezone(timezone))
    
    # Quiet hours: 9 PM - 8 AM local time
    quiet_start = local_time.replace(hour=21, minute=0)
    quiet_end = local_time.replace(hour=8, minute=0)
    
    return quiet_start <= local_time or local_time < quiet_end

def schedule_message(phone_number, message, send_at=None):
    if not send_at and is_quiet_hours(phone_number):
        # Schedule for 8 AM next day
        timezone = get_timezone_from_number(phone_number)
        local_time = datetime.now(pytz.timezone(timezone))
        send_at = local_time.replace(hour=8, minute=0) + timedelta(days=1)
    
    return client.messages.create(
        to=phone_number,
        from_=messaging_service_sid,
        body=message,
        schedule_type='fixed',
        send_at=send_at.isoformat() if send_at else None
    )
```

### Audit Logging

```python
import logging

compliance_logger = logging.getLogger('compliance')

def log_communication(communication_type, recipient, content_sid, 
                      consent_verified, purpose):
    """Log for compliance auditing"""
    compliance_logger.info({
        'event': 'communication_sent',
        'timestamp': datetime.utcnow().isoformat(),
        'type': communication_type,
        'recipient_hash': hashlib.sha256(recipient.encode()).hexdigest()[:16],
        'content_sid': content_sid,
        'consent_verified': consent_verified,
        'purpose': purpose,
        'ip_address': request.remote_addr,
        'user_agent': request.user_agent.string
    })
```

## Compliance Monitoring

### Key Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Opt-out rate | <1% | >2% |
| Spam complaints | <0.1% | >0.3% |
| Delivery rate | >95% | <90% |
| Bounce rate | <2% | >5% |
| Blocklist hits | 0 | >0 |

### Regular Audits

**Monthly**:
- [ ] Opt-out processing verification
- [ ] Consent record audit
- [ ] Sending volume vs. thresholds
- [ ] Error code analysis

**Quarterly**:
- [ ] Complete data inventory
- [ ] Access log review
- [ ] Policy update check
- [ ] Training compliance

**Annually**:
- [ ] Full compliance assessment
- [ ] BAA renewal
- [ ] External audit (if required)
