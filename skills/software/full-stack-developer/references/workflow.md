## § 7 · Standard Workflow

### Phase 1: Requirements & Design (Day 1)

```
├── Understand user story and acceptance criteria
├── Design database schema (ER diagram)
├── Define API contracts (OpenAPI/GraphQL schema)
├── Create component hierarchy (for UI)
└── [✓ Done]: Schema, API spec, component plan ready
    [✗ FAIL]: Ambiguous requirements → clarify before coding
```

### Phase 2: Backend Implementation (Days 2-3)

```
├── Database migrations
├── API endpoints with validation
├── Business logic services
├── Authentication/authorization
├── Unit tests (> 80% coverage)
└── [✓ Done]: API tested, documented, ready for frontend
    [✗ FAIL]: Tests failing → fix before proceeding
```

### Phase 3: Frontend Implementation (Days 4-5)

```
├── Component structure
├── API integration with types
├── State management
├── Form validation (Zod)
├── Responsive styling
└── [✓ Done]: UI functional, accessible, responsive
    [✗ FAIL]: Lighthouse score < 90 → optimize
```

### Phase 4: Integration & Deployment (Day 6)

```
├── Integration tests
├── E2E tests for critical paths
├── Docker containerization
├── CI/CD pipeline
├── Staging deployment
└── [✓ Done]: Deployed, monitored, rollback-ready
    [✗ FAIL]: Security scan alerts → resolve before production
```

---
