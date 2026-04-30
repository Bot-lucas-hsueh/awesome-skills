# Twilio API Reference

## Core APIs

### Programmable SMS

**Send Message**
```http
POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages.json
```

**Parameters**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| `To` | Yes | Destination E.164 number (+1234567890) |
| `From` | Yes | Twilio number or Messaging Service SID |
| `Body` | Conditional | Message text (max 1600 chars) |
| `MediaUrl` | No | URL to media (MMS) |
| `StatusCallback` | No | Webhook for delivery status |
| `ValidityPeriod` | No | Message validity in seconds (1-14400) |

**Response**:
```json
{
  "sid": "SM1234567890abcdef",
  "date_created": "Mon, 21 Mar 2026 12:00:00 +0000",
  "date_updated": "Mon, 21 Mar 2026 12:00:01 +0000",
  "date_sent": null,
  "account_sid": "AC1234567890abcdef",
  "to": "+1234567890",
  "from": "+1987654321",
  "messaging_service_sid": null,
  "body": "Hello from Twilio!",
  "status": "queued",
  "num_segments": "1",
  "num_media": "0",
  "direction": "outbound-api",
  "api_version": "2010-04-01",
  "price": null,
  "price_unit": "USD",
  "error_code": null,
  "error_message": null,
  "uri": "/2010-04-01/Accounts/AC123/Messages/SM123.json"
}
```

**Status Values**:
- `queued` - Message queued for sending
- `sending` - In process of being sent
- `sent` - Sent to carrier
- `delivered` - Confirmed delivery
- `undelivered` - Failed delivery
- `failed` - Sending failed
- `receiving` - Inbound message received
- `received` - Inbound message complete
- `accepted` - WhatsApp template accepted
- `scheduled` - Scheduled for future sending
- `read` - WhatsApp message read

### Programmable Voice

**Make Call**
```http
POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls.json
```

**Parameters**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| `To` | Yes | Destination number |
| `From` | Yes | Twilio number |
| `Url` | Yes* | TwiML URL (or `Twiml` parameter) |
| `Twiml` | Yes* | Inline TwiML |
| `StatusCallback` | No | Status change webhook |
| `StatusCallbackEvent` | No | Events to notify: initiated, ringing, answered, completed |
| `Record` | No | Record call: true, false, record-from-answer |
| `RecordingStatusCallback` | No | Recording available webhook |
| `MachineDetection` | No | Detect voicemail: Enable, DetectMessageEnd |
| `AsyncAmd` | No | Async machine detection: true, false |

**TwiML Quick Reference**:

```xml
<!-- Basic response -->
<Response>
  <Say voice="Polly.Joanna">Hello, welcome to our service.</Say>
  <Pause length="2"/>
  <Gather action="/handle-input" numDigits="1">
    <Say>Press 1 for sales, 2 for support.</Say>
  </Gather>
</Response>

<!-- Conference -->
<Response>
  <Dial>
    <Conference startConferenceOnEnter="true" 
                endConferenceOnExit="false"
                record="record-from-start"
                statusCallback="/conference-events">
      Room-1234
    </Conference>
  </Dial>
</Response>

<!-- Call forwarding with whisper -->
<Response>
  <Dial>
    <Number url="/whisper">
      +15551234567
    </Number>
  </Dial>
</Response>

<!-- Voicemail -->
<Response>
  <Say>Please leave a message after the tone.</Say>
  <Record 
    action="/handle-recording"
    maxLength="300"
    transcribe="true"
    transcribeCallback="/handle-transcription"
  />
</Response>
```

### Verify API

**Start Verification**
```http
POST https://verify.twilio.com/v2/Services/{ServiceSid}/Verifications
```

**Parameters**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| `To` | Yes | Phone number or email |
| `Channel` | Yes | sms, call, email, whatsapp |
| `Locale` | No | Language code (en, es, fr, etc.) |
| `CustomFriendlyName` | No | App name in message |
| `CustomMessage` | No | Custom SMS template (approved) |
| `SendDigits` | No | DTMF tones for voice calls |

**Check Verification**
```http
POST https://verify.twilio.com/v2/Services/{ServiceSid}/VerificationCheck
```

**Parameters**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| `To` | Conditional | Phone/email (if no VerificationSid) |
| `VerificationSid` | Conditional | SID from start request |
| `Code` | Yes | Verification code entered by user |

### Conversations API

**Create Conversation**
```http
POST https://conversations.twilio.com/v1/Conversations
```

**Add Participant**
```http
POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Participants
```

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `Identity` | Unique user identifier |
| `MessagingBinding.Address` | Phone number for SMS/WhatsApp |
| `MessagingBinding.ProxyAddress` | Twilio proxy number |

**Send Message**
```http
POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages
```

### Messaging Services

**High-volume sending best practices**:

```python
# Create messaging service for high volume
messaging_service = client.messaging.v1 \
    .services \
    .create(
        friendly_name='Marketing Campaigns',
        inbound_request_url='https://example.com/inbound',
        inbound_method='POST',
        fallback_url='https://example.com/fallback',
        status_callback='https://example.com/status'
    )

# Add numbers to pool
client.messaging.v1 \
    .services(messaging_service.sid) \
    .phone_numbers \
    .create(phone_number_sid='PN123...')

# Set sticky sender (same From for same To)
client.messaging.v1 \
    .services(messaging_service.sid) \
    .update(
        sticky_sender=True,
        smart_encoding=True,
        validity_period=14400
    )
```

**Messaging Service Features**:
- **Sticky Sender**: Same From number for same recipient
- **Smart Encoding**: Auto-convert Unicode to GSM-7 when possible
- **Scalable**: Distribute load across number pool
- **Geomatch**: Match sender to recipient geography
- **Short Code Rollover**: Failover to long codes

## Error Codes

### SMS Error Codes

| Code | Meaning | Resolution |
|------|---------|------------|
| 30001 | Queue overflow | Reduce sending rate |
| 30002 | Account suspended | Contact support |
| 30003 | Unreachable | Check number validity |
| 30004 | Message blocked | Carrier filter, check content |
| 30005 | Unknown number | Invalid destination |
| 30006 | Landline | Use voice instead |
| 30007 | Carrier violation | Check for spam keywords |
| 30008 | Unknown error | Retry with backoff |
| 30009 | Missing segment | Check concatenation |
| 30010 | Message price exceeds max | Adjust price limit |

### Voice Error Codes

| Code | Meaning |
|------|---------|
| 13201 | Dial: Invalid caller ID |
| 13214 | Dial: Invalid number format |
| 13225 | Dial: Number unreachable |
| 13226 | Dial: Busy signal |
| 13230 | Dial: No answer |
| 21211 | Invalid 'To' number |
| 21212 | Invalid 'From' number |
| 21610 | Message already queued |
| 21614 | 'To' number not mobile |

### REST API Status Codes

| HTTP | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | Deleted |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 429 | Too Many Requests |
| 500 | Server Error |

## Rate Limits

### Default Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| API requests | 100/sec/account | Burst to 200/sec |
| SMS sends | 1/sec/From number | Use Messaging Service to scale |
| Voice calls | 1 concurrent/number | Buy more numbers |
| Verify requests | 5/min/To | Fraud prevention |

### Increasing Limits

1. **Upgrade account** (remove trial limits)
2. **Use Messaging Services** (pool numbers)
3. **Request increase** via support (business justification)
4. **Multiple subaccounts** (shard by use case)

### Backoff Strategy

```python
import time
from twilio.base.exceptions import TwilioRestException

def retry_with_backoff(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except TwilioRestException as e:
            if e.status == 429:  # Rate limited
                wait = (2 ** attempt) + random.random()
                time.sleep(wait)
            else:
                raise
    raise Exception("Max retries exceeded")
```

## Webhooks

### Signature Validation

```python
from twilio.request_validator import RequestValidator

def validate_twilio_request(request):
    validator = RequestValidator(auth_token)
    url = request.url
    params = request.form
    signature = request.headers.get('X-Twilio-Signature', '')
    
    return validator.validate(url, params, signature)
```

### Security Checklist

- [ ] Always validate request signatures
- [ ] Use HTTPS for all webhook URLs
- [ ] Implement idempotency (prevent double-processing)
- [ ] Return 200 OK quickly (process async)
- [ ] Set reasonable timeouts (10-30 seconds)
- [ ] Implement retry logic for outbound calls

### Webhook Events

**SMS Status Callback**:
```json
{
  "MessageSid": "SM123...",
  "MessageStatus": "delivered",
  "To": "+1234567890",
  "From": "+1987654321",
  "ApiVersion": "2010-04-01",
  "SmsStatus": "delivered"
}
```

**Voice Status Callback**:
```json
{
  "Called": "+1234567890",
  "CallSid": "CA123...",
  "CallStatus": "completed",
  "From": "+1987654321",
  "To": "+1234567890",
  "CallDuration": "45",
  "RecordingUrl": "https://api.twilio.com/...",
  "RecordingSid": "RE123...",
  "RecordingDuration": "45"
}
```

## Pagination

```python
# List messages with pagination
messages = client.messages.list(limit=100)

# Manual pagination
messages = client.messages.list(page_size=50, page=0)
next_page_uri = messages.next_page_uri

# Auto-paginate
for message in client.messages.list():
    print(message.sid)
```
