# Twilio Pricing Guide

## Pricing Model Overview

Twilio uses **pay-as-you-go** pricing with volume discounts. No upfront commitments required for standard usage.

## Communications APIs

### SMS Pricing (US)

| Type | Send | Receive | Notes |
|------|------|---------|-------|
| Local Number | $0.0079 | $0.0079 | Standard 10DLC |
| Toll-Free | $0.0075 | $0.0075 | Lower throughput |
| Short Code | $0.0075 | $0.0075 | High volume only |
| MMS (Media) | $0.0200 | $0.0100 | Per message + media |

**Carrier Fees** (A2P 10DLC):
- Outbound: $0.003 - $0.005 per message
- Campaign fees: $2-$10/month

### Voice Pricing (US)

| Type | Per Minute |
|------|------------|
| Inbound Local | $0.0085 |
| Inbound Toll-Free | $0.0220 |
| Outbound Local | $0.0130 |
| Outbound International | Varies by country |
| Conference | $0.0018 per participant/min |
| Recording | $0.0025 per minute |
| Transcription | $0.0500 per minute |

**SIP Interface**:
- Termination: $0.0045/min
- Origination: $0.0045/min
- Secure TLS: +$0.0010/min

### Video Pricing

| Component | Price |
|-----------|-------|
| Peer-to-peer | Free (signaling only) |
| Small Group Rooms (<50) | $0.0015/participant/min |
| Go Rooms (P2P relayed) | $0.0005/participant/min |
| Recording | $0.025/min |
| Compositions | $0.040/min |

### WhatsApp Business API

| Type | Price |
|------|-------|
| Session Messages | $0.005 per message |
| Template Messages | Varies by country ($0.003-$0.08) |
| Business Initiated | Template rates apply |
| User Initiated | Session rate for 24h window |

**Conversation-Based Pricing (Meta)**:
- Business-initiated: Per conversation (24h window)
- User-initiated: Per conversation (24h window)
- Rates vary by country/region

### Email (SendGrid)

| Plan | Emails/Month | Price |
|------|--------------|-------|
| Free | 100/day | $0 |
| Essentials | 50,000 | $19.95 |
| Essentials | 100,000 | $34.95 |
| Pro | 100,000 | $89.95 |
| Pro | 300,000 | $249.95 |

**Dedicated IP**: $89.95/month

### Verify API

| Channel | Price |
|---------|-------|
| SMS | $0.05 per verification |
| Voice | $0.05 per verification |
| WhatsApp | $0.05 per verification |
| Email | $0.05 per verification |

**Bulk Discounts**: Available above 10,000/month

## Platform Products

### Twilio Flex

| License Type | Price |
|--------------|-------|
| Named User | $150/user/month |
| Active User | $1/hour/active user (min $0.55, max $150/month) |

**Included**: All channels, standard plugins, support
**Add-ons**: Workforce management, advanced analytics

### Segment

| Plan | Price | Events/Month |
|------|-------|--------------|
| Free | $0 | 1,000 visitors/month |
| Team | $120/month | 10,000 visitors/month |
| Business | Custom | Unlimited |

**Profiles**: Starting at $10/month per 1,000 profiles

## Phone Numbers

### Monthly Number Rental

| Type | Price |
|------|-------|
| Local Number | $1.15/month |
| Toll-Free | $2.15/month |
| Short Code | $500-1000/month |
| SIP Domain | Free |

### International Numbers

| Region | Local | National | Toll-Free |
|--------|-------|----------|-----------|
| UK | $3.00 | $3.00 | $5.00 |
| Germany | $3.00 | - | $5.00 |
| Australia | $6.00 | $6.00 | $7.00 |
| Japan | $6.00 | - | $15.00 |
| Singapore | $6.00 | $6.00 | $25.00 |

## Cost Optimization Strategies

### SMS Optimization

**Message Concatenation**:
```python
# BAD: Multiple short messages (3 x $0.0079 = $0.0237)
client.messages.create(body="Hello")
client.messages.create(body="Your order")
client.messages.create(body="is ready")

# GOOD: Single concatenated message ($0.0079 or 2 segments = $0.0158)
client.messages.create(body="Hello! Your order is ready for pickup.")
```

**Character Encoding**:
- GSM-7: 160 chars per segment
- UCS-2: 70 chars per segment
- Use smart encoding to reduce costs

```python
# Check encoding
from twilio.base.charset import detect_charset

charset, segments = detect_charset("Hello! 🎉")
# Returns: ('UCS-2', 2) - costs 2x GSM-7
```

**Channel Selection**:

| Volume | Recommendation |
|--------|----------------|
| < 100/day | Long codes (10DLC) |
| 100-10K/day | Dedicated short code |
| > 10K/day | Shared short code |
| International | WhatsApp where available |

### Voice Optimization

**SIP vs. PSTN**:
```
PSTN Outbound: $0.0130/min
SIP Trunking:  $0.0045/min
Savings: 65%
```

**Call Recording**:
- Only record when necessary
- Use dual-channel (stereo) for quality
- Auto-delete after retention period

### Volume Discounts

**Committed Use Discounts**:
| Commitment | Discount |
|------------|----------|
| $2,500/month | 5% |
| $5,000/month | 10% |
| $10,000/month | 15% |
| $25,000/month | 20% |

**Enterprise Agreements**:
- Custom pricing above $50K/month
- Multi-year commitments
- Dedicated support
- SLA guarantees

### Monitoring Costs

**Alert Thresholds**:
```python
# Daily spend alert
if daily_spend > daily_budget * 0.8:
    send_alert("Approaching daily budget limit")

# Unusual spike detection
if current_hour_spend > avg_hourly_spend * 3:
    send_alert("Unusual spending spike detected")
```

**Subaccount Strategy**:
- Separate subaccounts by use case
- Isolate costs for attribution
- Prevent runaway spending

```python
# Create subaccount for department
subaccount = client.api.v2010.accounts.create(
    friendly_name='Marketing-2026-Q1'
)

# Set usage trigger
client.api.v2010.accounts(subaccount.sid) \
    .usage_triggers \
    .create(
        trigger_value='1000',
        usage_category='sms',
        callback_url='https://alerts.company.com/usage'
    )
```

## Cost Calculator Examples

### Scenario 1: E-commerce Notifications

**Monthly Volume**:
- 100,000 SMS order confirmations
- 50,000 SMS shipping updates
- 10,000 voice calls (5 min avg)

**Calculation**:
```
SMS: 150,000 × $0.0079 = $1,185
Carrier fees: 150,000 × $0.004 = $600
Voice: 10,000 × 5 × $0.013 = $650
Numbers: 10 × $1.15 = $11.50
-------------------------------
Total: $2,446.50/month
```

**With 10% CUD**: $2,201.85/month

### Scenario 2: Contact Center (Flex)

**Configuration**:
- 50 agents
- Named User licenses
- 25,000 calls/month (6 min avg)
- 10,000 SMS

**Calculation**:
```
Flex: 50 × $150 = $7,500
Voice: 25,000 × 6 × $0.0085 = $1,275
SMS: 10,000 × $0.0079 = $79
Numbers: 50 × $1.15 = $57.50
-------------------------------
Total: $8,911.50/month
```

### Scenario 3: Healthcare (HIPAA)

**Configuration**:
- 5,000 video sessions/month (30 min avg)
- 20,000 appointment reminders (SMS)
- Recording required

**Calculation**:
```
Video: 5,000 × 30 × 2 × $0.0015 = $450
Recording: 5,000 × 30 × $0.025 = $3,750
SMS: 20,000 × $0.0079 = $158
HIPAA BAA: Included
-------------------------------
Total: $4,358/month
```

## Billing FAQ

**Q: When am I billed?**
A: Monthly in arrears. Usage from March 1-31 billed early April.

**Q: What currency?**
A: USD by default. Local currency available in some regions.

**Q: Payment methods?**
A: Credit card (all), ACH/wire (enterprise), monthly invoicing ($2,500+/month).

**Q: Can I set spending limits?**
A: Usage triggers available. Hard limits not supported (pay-as-you-go).

**Q: Are taxes included?**
A: Taxes added based on billing address. US: sales tax varies by state.

**Q: How do I dispute a charge?**
A: Contact support within 60 days with specific message SIDs.

## Support Plans

| Plan | Price | Response Time |
|------|-------|---------------|
| Free | $0 | Best effort |
| Developer | $29/month | 4 hours |
| Production | 4% of monthly spend | 1 hour |
| Business | 6% of monthly spend | 30 min |
| Personalized | Custom | 15 min |

**Included in Paid Plans**:
- Technical support
- Architecture guidance
- Quarterly business reviews (Business+)
- Dedicated TAM (Personalized)
