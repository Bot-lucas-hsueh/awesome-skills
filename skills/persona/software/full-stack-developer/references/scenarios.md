## § 8 · Scenario Examples

### Example 1: SaaS Dashboard Development

**Context**: Build analytics dashboard for B2B SaaS with real-time updates.

**Implementation**:
```
Stack:
├── Frontend: React 18 + TypeScript + Tailwind
├── State: React Query for server state, Zustand for UI
├── Backend: Node.js + Fastify + tRPC
├── Database: PostgreSQL + Redis for caching
├── Real-time: WebSocket for live updates

Key Decisions:
├── tRPC for end-to-end type safety
├── React Query for caching and background refetch
├── Virtualized tables for 100K+ rows
├── WebSocket connection pooling for scale
```

---

### Example 2: E-commerce Platform

**Context**: Full e-commerce site with cart, checkout, and order management.

**Implementation**:
```
Architecture:
├── Next.js (App Router) for SEO and performance
├── Stripe integration for payments
├── PostgreSQL with Prisma ORM
├── Redis for cart sessions
├── Image optimization via CDN

Performance:
├── ISR for product pages (cache 60s)
├── Optimized images (WebP, responsive)
├── Cart state persists across sessions
├── Checkout: 3 steps, progress saved
```

---

### Example 3: Real-time Collaboration App

**Context**: Google Docs-like collaborative editor.

**Implementation**:
```
Tech Stack:
├── React with operational transforms
├── Yjs for CRDT-based collaboration
├── WebSocket for real-time sync
├── Node.js backend with presence
├── MongoDB for document storage

Challenges Solved:
├── Conflict resolution via CRDTs
├── Cursor presence tracking
├── Offline support with sync on reconnect
├── Version history with diff view
```

---

### Example 4: API Migration Project

**Context**: Migrate REST API to GraphQL incrementally.

**Approach**:
```
Strategy:
├── GraphQL layer over existing REST
├── Strangler Fig pattern gradual migration
├── Shared types via codegen
├── Frontend: Apollo Client with caching

Migration Steps:
├── Step 1: GraphQL gateway, REST passthrough
├── Step 2: Migrate read operations
├── Step 3: Migrate mutations
├── Step 4: Deprecate REST endpoints
```

---

### Example 5: Performance Optimization

**Context**: Dashboard loading in 8 seconds → target 2 seconds.

**Optimization**:
```
Analysis:
├── Bundle: 2MB → code split to 400KB initial
├── API: 15 sequential calls → parallel + consolidation
├── Database: Missing indexes → added composite indexes
├── Images: Unoptimized → WebP, lazy loading

Results:
├── LCP: 8s → 1.2s
├── API response: 3s → 200ms
├── Bundle: 2MB → 400KB
├── Lighthouse: 45 → 95
```

---
