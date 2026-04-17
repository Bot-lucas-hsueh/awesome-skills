## §2 Domain Knowledge

### §2.1 Core Concepts

| Concept | Description | Best Practice |
|---------|-------------|---------------|
| **Workspaces** | A Slack organization | One workspace per company; Enterprise Grid for multiple |
| **Channels** | Persistent chat rooms | Public by default; descriptive names with prefixes |
| **DMs** | Direct messages | 1:1 or group (up to 9); use channels for work that others might need |
| **Threads** | Replies to specific messages | Always thread to keep channels clean |
| **Huddles** | Lightweight audio/video calls | For quick syncs; auto-transcribed with AI |
| **Clips** | Async audio/video messages | Record once, watch anytime |
| **Canvas** | Collaborative documents | Living docs inside Slack; embed workflows |
| **Lists** | Project management views | Track work items with assignees and due dates |

### §2.2 Platform Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                            │
│  Desktop App │ Mobile Apps │ Web │ Slack in Salesforce      │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    PLATFORM LAYER                            │
│  Events API │ Web API │ Socket Mode │ RTM (legacy)           │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    APP ECOSYSTEM                             │
│  Bolt SDKs │ Block Kit │ Workflow Builder │ 2,600+ Apps      │
└─────────────────────────────────────────────────────────────┘
```

### §2.3 API & Development Stack

| Component | Purpose | Tech Stack |
|-----------|---------|------------|
| **Bolt Framework** | App foundation | Node.js, Python, Java |
| **Block Kit** | UI components | JSON-based DSL |
| **Events API** | Real-time events | WebSocket/HTTP callbacks |
| **Slack CLI** | App management | TypeScript-based CLI |
| **Socket Mode** | Firewall-friendly | WebSocket connections |
| **Workflow Steps** | Custom automation | Hosted anywhere |

### §2.4 Pricing Tiers

| Plan | Price | Key Features |
|------|-------|--------------|
| **Free** | $0 | 90-day history, 10 apps, 1:1 calls |
| **Pro** | $7.25/user/mo | Unlimited history, unlimited apps, Huddles |
| **Business+** | $12.50/user/mo | Data exports, 99.99% SLA, DLP |
| **Enterprise Grid** | Custom | Multiple workspaces, HIPAA, FedRAMP |

### §2.5 Key Statistics (2024-2025)

- **47.2M** daily active users
- **79M** monthly active users
- **200,000+** paid customers
- **750,000+** organizations
- **77%** of Fortune 100 companies use Slack
- **$1.7B** annual revenue (2023)
- **$27.7B** Salesforce acquisition (2021)
- **2,600+** app integrations
- **13,000+** AI apps being built

---
