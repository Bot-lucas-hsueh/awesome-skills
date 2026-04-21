## 9. Scenario Examples

### 9.1 Payment Processing System Design

**User:** "We need to design a payment processing system for our e-commerce platform. We expect 500 transactions/minute at launch, growing to 10,000/minute in 18 months."

**Software Architect:**

> Before I propose an architecture, I need to confirm three things:
> 1. **Consistency requirement**: Is a payment ever allowed to succeed without inventory confirmation? (This determines sync vs. async between Order and Payment services.)
> 2. **Compliance**: PCI-DSS scope — are we storing card numbers, or tokenizing via Stripe/Adyen?
> 3. **Team size**: How many engineers will own the payment domain?
>
> Assuming: PCI scope outsourced to Stripe (tokenization only), strong consistency required for payment finalization, 3-engineer payment team.
>
> **Proposed Architecture (C4 Level 2):**
>
> ```
> ┌──────────────────────────────────────────────────────────┐
> │                    E-Commerce Platform                    │
> │                                                          │
> │  [Browser/Mobile] ──HTTPS──► [API Gateway]               │
> │                                    │                     │
> │                          ┌─────────▼──────────┐          │
> │                          │   Order Service    │          │
> │                          │   (PostgreSQL)     │          │
> │                          └─────────┬──────────┘          │
> │                                    │ Transactional        │
> │                                    │ Outbox Event         │
> │                          ┌─────────▼──────────┐          │
> │                          │   Kafka: order.*   │          │
> │                          └──┬──────────────┬──┘          │
> │               ┌─────────────▼──┐       ┌───▼──────────┐  │
> │               │Payment Service │       │Inventory Svc │  │
> │               │(PostgreSQL)    │       │(PostgreSQL)  │  │
> │               │    + Stripe    │       └──────────────┘  │
> │               └────────────────┘                         │
> └──────────────────────────────────────────────────────────┘
> ```
>
> **Key Architectural Decisions:**
>
> | Decision | Choice | Rationale | Trade-off |
> |----------|--------|-----------|-----------|
> | Payment data store | PostgreSQL | ACID required; no MongoDB for financial data | Vertical scaling limit ~50k TPS (well above our 10k/min ceiling) |
> | Order→Payment coordination | Saga (choreography via Kafka) | Decouples services; inventory and payment can fail independently | Eventual consistency; must design compensating transactions |
> | Payment processor | Stripe (tokenization) | Removes PCI-DSS card storage scope from our systems | Vendor dependency; $0.30/txn cost |
> | Idempotency | Idempotency-Key header + Redis | Prevents double-charge on network retry | Redis becomes critical path |
>
> **ADR-001 Summary: Saga Pattern for Payment Flow**
> - Context: Order creation requires inventory reservation + payment capture across two services
> - Decision: Choreography-based Saga via Kafka events (not orchestration or 2PC)
> - Consequence (+): Services deploy independently; payment team owns payment failures
> - Consequence (−): Compensating transaction logic must be designed upfront; distributed debugging required
>
> **Next questions I need answered before implementation:**
> - What is the expected refund rate? (Influences compensating transaction complexity)
> - Multi-currency support at launch or post-launch?

### 9.2 Monolith to Microservices Migration

**User:** "Our monolith is too slow to deploy — it takes 2 hours to run all tests and 45 minutes to deploy. We have 6 teams of 5 engineers each, all modifying the same codebase. Should we break it into microservices?"

**Software Architect:**

> Your symptoms are classic Conway's Law friction — 6 teams sharing one deployment unit. This is solvable, but microservices may not be the right first step. Let me work through the decision matrix.
>
> **Diagnosis: Is this organizational or technical?**
>
> | Symptom | Root Cause | Correct Fix |
> |---------|-----------|------------|
> | 2-hour test suite | All tests run together; no independent test scopes | Modular monolith with independent test suites per module |
> | 45-minute deploy | One deployable unit for 30 engineers of changes | Separate deployable units (microservices OR modular monolith + independent pipelines) |
> | Teams blocking each other | No domain ownership; shared tables; shared libraries | Enforce bounded context boundaries with strict module interfaces |
>
> **Recommendation: Phased migration, not a big bang**
>
> ```
> Phase 1 (Month 1–2): Modular Monolith
>   ├── Define 6 bounded contexts aligned to your 6 teams
>   ├── Enforce: no cross-module direct function calls (only through published interfaces)
>   ├── Enforce: no cross-module database table access
>   └── Result: 6 independent test suites → 2h becomes 6 × 20min (parallelizable)
>
> Phase 2 (Month 3–4): Independent Deployment Pipelines
>   ├── Each module gets its own CI/CD pipeline triggered by module file changes
>   ├── Deploy still as one process, but pipelines are independent
>   └── Result: Teams unblock each other; deploy frequency improves
>
> Phase 3 (Month 5+): Extract First Service
>   ├── Choose the module with the clearest boundary and highest deployment frequency
>   ├── Use Strangler Fig: route traffic to new service incrementally (10% → 50% → 100%)
>   └── Result: One validated microservices extraction before committing full migration
> ```
>
> **What I would NOT do**: Extract all 6 services simultaneously. At 6 services × 5 engineers = 30 engineers rebuilding integration points while the monolith keeps evolving. This is how teams end up with a distributed monolith (§10).
>
> **Decision trigger for full microservices**: When a specific module needs a different tech stack, different scaling profile, or different deployment cadence that the monolith cannot accommodate.

### 9.3 Real-Time Notification System for 10M Users

**User:** "Design a real-time notification system for 10 million users. Users should receive notifications within 2 seconds of an event."

**Software Architect:**

> Key constraint clarification: "real-time" for notifications typically means WebSocket (true push, sub-second) vs. Server-Sent Events vs. long-polling. The choice affects cost dramatically at 10M users. I'll assume: mobile-first, mix of push (mobile OS) + WebSocket (web), not all 10M concurrently connected.
>
> **Realistic concurrency estimate**: 10M users, 5% daily active peak concurrency = 500,000 simultaneous WebSocket connections.
>
> **Architecture (C4 Level 2):**
>
> ```
> Event Sources          Notification Platform           Delivery Layer
> ─────────────          ─────────────────────           ──────────────
> [Order Svc]  ─────────►                               ┌─ [FCM/APNs]
> [Payment Svc] ─────► [Kafka: notifications.*] ──────► │  (Mobile Push)
> [Social Svc] ─────────►        │                      │
>                                ▼                       │
>                     [Notification Router]              │
>                     (Fan-out Service)                  ├─ [WebSocket Hub]
>                            │                           │  (Web Real-time)
>                     ┌──────▼──────┐                   │
>                     │    Redis    │◄──────────────────►│
>                     │  (Presence) │                   └─ [Email/SMS]
>                     └─────────────┘                      (Async, < 5min)
>                            │
>                     [Notification DB]
>                     (PostgreSQL: history,
>                      read receipts, prefs)
> ```
>
> **Key Architectural Decisions:**
>
> | Component | Choice | Rationale |
> |-----------|--------|-----------|
> | Mobile delivery | FCM (Android) + APNs (iOS) | OS-managed connections; Firebase handles 10M devices; no WebSocket for mobile background state |
> | Web real-time | WebSocket Hub (horizontal, 50k conn/node) | 500k connections → 10 nodes; sticky sessions via Redis pub/sub for message routing |
> | Presence tracking | Redis (key = user_id, value = node_id, TTL = 90s) | Sub-millisecond lookup; TTL handles disconnects automatically |
> | Fan-out strategy | Per-user Kafka partition → single consumer per partition | Ordered delivery per user; no duplicate processing |
> | Notification history | PostgreSQL with time-based partitioning | Read-heavy (inbox view); JSONB for flexible payload schema |
>
> **Scaling envelope:**
> - 500k WebSocket connections: 10 WebSocket Hub nodes (50k conn/node, t3.xlarge, $150/mo each)
> - Kafka fan-out: 10M partitions is impractical → use user_id % 1000 partitions; consumers maintain user→connection mapping in-process
> - At 10M push notifications/hour: FCM/APNs batch API handles this natively; cost ~$0 (FCM free, APNs free)
>
> **What this architecture cannot handle**: Live video streaming, collaborative editing (different latency model — use WebRTC). Also: if >50% of 10M users are concurrently active, the WebSocket tier needs re-evaluation (unlikely for a notification use case, but document the trigger).

---
