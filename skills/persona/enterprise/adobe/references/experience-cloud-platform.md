# Adobe Experience Cloud Platform

## Platform Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ADOBE EXPERIENCE CLOUD                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │              ADOBE EXPERIENCE PLATFORM (AEP)                        │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │    │
│  │  │ Data Ingest │  │   Profile   │  │   Identity  │  │ Data Gov  │  │    │
│  │  │   (Any)     │  │  (Real-time)│  │  (Graph)    │  │  (Consent)│  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘  │    │
│  │                                                                     │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │    │
│  │  │ Query Svcs  │  │   ML/AI     │  │  Sandboxes  │  │  Privacy  │  │    │
│  │  │  (SQL/BI)   │  │  (Sensei)   │  │  (Isolated) │  │  (GDPR)   │  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                              ▲                                               │
│                              │                                               │
│  ┌───────────────────────────┼───────────────────────────────────────────┐  │
│  │                           │           NATIVE APPLICATIONS              │  │
│  │  ┌──────────┐  ┌─────────┴────────┐  ┌──────────┐  ┌──────────┐      │  │
│  │  │Real-Time │  │   Journey        │  │ Customer │  │  Adobe   │      │  │
│  │  │   CDP    │  │   Optimizer      │  │  Journey │  │  Target  │      │  │
│  │  └──────────┘  └──────────────────┘  └──────────┘  └──────────┘      │  │
│  │                                                                      │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐             │  │
│  │  │ Campaign │  │ Analytics│  │  Marketo │  │ Commerce │             │  │
│  │  │ (Classic)│  │          │  │  Engage  │  │          │             │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘             │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                              ▲                                               │
│                              │                                               │
│  ┌───────────────────────────┴───────────────────────────────────────────┐  │
│  │                         CONTENT & WORKFLOW                             │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐               │  │
│  │  │   AEM    │  │ Workfront│  │ GenStudio│  │  Assets  │               │  │
│  │  │(Sites/   │  │          │  │          │  │          │               │  │
│  │  │ Assets)  │  │          │  │          │  │          │               │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Adobe Experience Platform (AEP)

### Core Services

#### Real-Time Customer Data Platform (CDP)

**Capabilities**:
- Unified customer profiles
- Real-time segmentation (latency <100ms)
- Identity resolution across channels
- 500M+ profiles at scale

**Data Sources**:
- Web/Mobile SDK
- Batch file ingestion
- Streaming (Kafka, Kinesis)
- CRM integrations (Salesforce, Microsoft)

**Activation**:
- Destinations: 100+ pre-built
- Custom API destinations
- Real-time personalization

#### Journey Optimizer

**Use Cases**:
- B2C: Cross-channel campaigns
- B2B: Account-based orchestration (AJO B2B)
- Transactional messaging
- Real-time trigger management

**Channels**:
- Email (Adobe + external ESPs)
- SMS/MMS
- Push (iOS, Android)
- In-app messaging
- Direct mail
- Custom (webhooks)

**AI Features**:
- Send-time optimization
- Frequency capping
- Predictive engagement scoring
- Content experimentation

#### Customer Journey Analytics (CJA)

**Differentiation from Adobe Analytics**:
| Feature | Adobe Analytics | CJA |
|---------|-----------------|-----|
| Data Source | Adobe-only | Any (omnichannel) |
| Attribution | Rules-based | Algorithmic/ML |
| Identity | Cookie/Device | Person-based |
| Analysis | Web-focused | Cross-channel |

**Analysis Workspace Features**:
- Cross-channel funnels
- Flow visualization
- Attribution IQ
- Anomaly detection

### Data Governance

#### Privacy & Compliance

**Frameworks Supported**:
- GDPR (EU)
- CCPA/CPRA (California)
- LGPD (Brazil)
- POPIA (South Africa)

**Features**:
- Consent management
- Data retention policies
- Right to deletion
- Audit logging

#### Data Usage Labeling

**Label Categories**:
- Identity (I1, I2)
- Sensitive (S1, S2)
- Contractual (C1-C9)
- Governance (DU, PS)

## Marketing Applications

### Marketo Engage

**Positioning**: B2B marketing automation leader

**Core Modules**:
| Module | Function |
|--------|----------|
| Lead Management | Scoring, nurturing, routing |
| Email Marketing | Batch, triggered, dynamic |
| Consumer Marketing | B2C extensions |
| Marketing Attribution | Multi-touch, pipeline |
| Sales Insight | CRM integration |

**2024 Enhancements**:
- Interactive Webinars (on-demand)
- Dynamic Chat (conversational flows)
- Enhanced API (Activities, Bulk Import)
- New permissions model

### Adobe Analytics

**Products**:
- **Adobe Analytics**: Traditional web/app analytics
- **Streaming Media Analytics**: Video/audio measurement
- **Customer Journey Analytics**: Cross-channel (see above)

**Key Features**:
- Analysis Workspace
- Report Builder (Excel)
- Data Workbench
- Predictive analytics

### Adobe Target

**Testing & Personalization**:

| Feature | Description |
|---------|-------------|
| A/B Testing | Control vs. variant comparison |
| MVT | Multivariate testing |
| Auto-Allocate | AI winner selection |
| Auto-Target | ML personalization |
| Recommendations | Product/content suggestions |

**AI Capabilities**:
- Automated personalization
- Predictive targeting
- Offer decisioning

### Adobe Commerce

**Capabilities**:
- B2C & B2B commerce
- Headless/PWA Studio
- Inventory management
- Multi-store management

**Integrations**:
- Experience Platform (personalization)
- Marketo (B2B nurture)
- Target (testing)

## Content & Workflow

### Adobe Experience Manager (AEM)

#### AEM Sites

**Content Management**:
- Headless CMS (Content Fragments)
- Traditional page authoring
- SPA Editor (React, Angular, Vue)
- Multi-site management

**Key Features**:
| Feature | Description |
|---------|-------------|
| Editable Templates | Author-controlled layouts |
| Experience Fragments | Reusable content blocks |
| Content Services | JSON API delivery |
| Launches | Campaign staging |

#### AEM Assets

**Digital Asset Management**:
- AI auto-tagging (Sensei)
- Smart collections
- Brand Portal (distribution)
- Dynamic Media (image/video optimization)

**Processing**:
- Rendition generation
- Video transcoding
- Image manipulation
- Asset microservices

### Workfront

**Work Management**:

**Core Capabilities**:
- Project management
- Resource management
- Proofing and approvals
- Portfolio management

**Integration**:
- Creative Cloud (plugin)
- Experience Platform (content pipeline)
- AEM (asset workflows)

### Adobe GenStudio

**Content Supply Chain**:

**Components**:
| Component | Function |
|-----------|----------|
| Planning | Campaign briefs, calendars |
| Creation | Firefly integration, templates |
| Management | AEM Assets integration |
| Activation | Multi-channel publishing |
| Insights | Performance analytics |

**Performance Marketing**:
- Paid media optimization
- AI-generated copy variations
- Asset performance tracking
- ROI measurement

## AI Capabilities (Sensei)

### Sensei Framework

```
┌─────────────────────────────────────────────────────────────┐
│                    ADOBE SENSEI                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   CONTENT    │  │   CUSTOMER   │  │   ATTRIBUTION│       │
│  │              │  │              │  │              │       │
│  │ • Auto-tag   │  │ • Propensity │  │ • Algorithmic│       │
│  │ • Crop       │  │ • Churn      │  │ • Multi-touch│       │
│  │ • Similarity │  │ • LTV        │  │ • Causal     │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   LANGUAGE   │  │   JOURNEY    │  │   OFFERS     │       │
│  │              │  │              │  │              │       │
│  │ • NER        │  │ • Pathing    │  │ • Optimization│      │
│  │ • Sentiment  │  │ • Sequencing │  │ • Arbitration│       │
│  │ • Summarize  │  │ • Anomaly    │  │ • Simulation │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### AEP AI Assistant

**Natural Language Interface**:
- Query customer data
- Generate audience segments
- Predict journey outcomes
- Automate campaign tasks

## Deployment Options

### Cloud Services

| Deployment | Description | Use Case |
|------------|-------------|----------|
| AWS | Primary cloud | Americas, EMEA |
| Azure | Microsoft partnership | Enterprise Microsoft shops |
| Managed Services | Adobe-hosted | Standard deployments |

### Data Residency

**Regions**:
- Americas (US West, US East)
- EMEA (EMEAWest, EMEAEast)
- APAC (APACSoutheast, Japan, Australia)

---

*Source: Adobe Experience Cloud Documentation, Adobe Summit 2024*
