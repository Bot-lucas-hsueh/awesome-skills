# DHL Digital Platforms & APIs

## MyDHL+

### Overview
MyDHL+ is DHL Express's online shipping platform for managing international shipments from quote to delivery.

### Key Features

| Feature | Description |
|---------|-------------|
| **Quick Quote** | Instant rate quotes by destination |
| **Shipment Booking** | Create shipments, print labels, schedule pickup |
| **Tracking** | Real-time shipment status and proof of delivery |
| **Address Book** | Save sender/receiver addresses |
| **Import Express** | Arrange shipments from suppliers to you |
| **Invoices** | View and pay invoices online |
| **Reports** | Download shipping history and analytics |
| **GoGreen Plus** | Activate carbon reduction at checkout |

### Access
- **URL:** https://mydhl.express.dhl
- **Registration:** Free business account required
- **Mobile App:** Available for iOS and Android

### Prohibited & Restricted Items Check
- Automated compliance screening
- Country-specific restrictions
- Lithium battery guidance
- Dangerous goods support

---

## DHL Developer Portal

### Overview
API-first platform for integrating DHL services into customer systems.

**Portal:** https://developer.dhl.com

### Available APIs

#### Tracking API
```
Endpoint: /track/shipments
Features:
- Track up to 10 shipments per request
- Real-time status updates
- Proof of delivery with signature image
- Estimated delivery dates
```

#### Shipping API
```
Endpoint: /shipments
Features:
- Create shipment bookings
- Generate shipping labels
- Schedule pickups
- Customs documentation
```

#### Rates & Transit Times API
```
Endpoint: /rates
Features:
- Real-time rate quotes
- Transit time estimates
- Service comparison
- Surcharge details
```

#### Locations API
```
Endpoint: /locations
Features:
- Find DHL service points
- Drop-off locations
- Service center details
- Opening hours
```

#### Address Validation API
```
Endpoint: /address-validation
Features:
- Validate international addresses
- Address correction suggestions
- Postal code verification
```

#### Pickup API
```
Endpoint: /pickups
Features:
- Request pickup
- Modify/cancel pickup
- Pickup availability check
```

#### Invoice API
```
Endpoint: /invoices
Features:
- Retrieve invoice PDFs
- Download billing data
- Line-item details
```

### API Authentication
- OAuth 2.0 authentication
- API key required
- Rate limits apply by tier

### Integration Options
- RESTful JSON APIs
- SOAP web services (legacy)
- EDI (X12, EDIFACT)
- SFTP batch processing

---

## Resilience360

### Overview
Supply chain risk management platform providing real-time visibility into potential disruptions.

**Website:** https://www.dhl.com/supply-chain/home/our-services/supply-chain-optimization/resilience360.html

### Core Capabilities

#### Risk Monitoring
| Risk Category | Data Sources |
|---------------|--------------|
| **Natural Disasters** | Weather, seismic activity |
| **Geopolitical** | Political instability, conflicts |
| **Infrastructure** | Port congestion, strikes |
| **Cyber** | Ransomware, outages |
| **Financial** | Supplier bankruptcy, credit risk |
| **Regulatory** | Sanctions, trade policy changes |

#### Supplier Risk Management
- Multi-tier supplier mapping (Tier 1, 2, 3+)
- Risk scoring by location and category
- Alert notifications for disruptions
- Business continuity planning tools

#### Scenario Planning
- "What-if" simulation
- Impact assessment
- Alternative routing options
- Recovery time estimation

### Dashboard Features
- Global risk heat map
- Watchlist of critical suppliers/locations
- Incident timeline
- Risk trend analysis
- Custom report builder

### Use Cases

**Supply Chain Mapping:**
```
1. Upload supplier master data
2. Geocode supplier locations
3. Map material flows
4. Identify concentration risks
5. Assess critical path dependencies
```

**Disruption Response:**
```
1. Receive automated alert
2. Assess impact on operations
3. Activate contingency plan
4. Communicate with stakeholders
5. Monitor recovery progress
```

---

## DHL Freight Customer Portal

### Overview
Online platform for managing freight shipments (Global Forwarding, Freight).

### Features
- Book air and ocean freight
- Track FCL/LCL shipments
- View sailing schedules
- Manage documentation
- Invoice and payment

### Access
Available to contracted DHL Global Forwarding customers.

---

## Supply Chain Visibility Platforms

### SmartSensor
IoT-based monitoring for temperature-sensitive shipments:
- Real-time temperature/humidity tracking
- GPS location
- Light exposure detection
- Shock/vibration alerts
- Automated notifications

### yard management
Digital yard operations:
- Trailer tracking
- Appointment scheduling
- Dock door management
- Driver check-in/check-out

### Warehouse Management Systems (WMS)
- Inventory visibility
- Order status tracking
- Performance dashboards
- API integration for ERP connectivity

---

## Integration Architecture

### Recommended Integration Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    CUSTOMER SYSTEMS                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │   ERP    │  │   WMS    │  │  E-COMM  │                  │
│  │ (SAP/Orcl)│  │(Manhattan)│  │(Shopify) │                  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘                  │
└───────┼─────────────┼─────────────┼─────────────────────────┘
        │             │             │
        └─────────────┴─────────────┘
                      │
              ┌───────▼───────┐
              │  MIDDLEWARE   │
              │  (MuleSoft/   │
              │  Boomi/Custom)│
              └───────┬───────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────▼───────┐ ┌───▼────┐ ┌──────▼──────┐
│ DHL Express   │ │  DHL   │ │  DHL Supply │
│ APIs          │ │Freight │ │  Chain APIs │
└───────────────┘ └────────┘ └─────────────┘
```

### Webhook Notifications
Configure real-time alerts for:
- Shipment picked up
- Customs clearance events
- Delivery completed
- Exceptions and delays
- Proof of delivery

### Data Formats
- **JSON:** Primary API format
- **XML:** Legacy EDI alternative
- **CSV:** Batch reporting
- **PDF:** Document retrieval

---

## Security & Compliance

### Data Protection
- GDPR compliant
- SOC 2 Type II certified
- Data encryption in transit (TLS 1.2+)
- Data encryption at rest

### Access Control
- Role-based permissions
- Multi-factor authentication (MFA)
- API key rotation
- IP whitelisting

---

## Getting Started

### Developer Account Setup
1. Visit https://developer.dhl.com
2. Register for free account
3. Request API credentials
4. Review API documentation
5. Test in sandbox environment
6. Go live with production credentials

### Support Resources
- API documentation with code samples
- Postman collections
- SDKs (Java, Python, Node.js)
- Developer forum
- Technical support contact

---

*For detailed API specifications, visit the DHL Developer Portal.*
