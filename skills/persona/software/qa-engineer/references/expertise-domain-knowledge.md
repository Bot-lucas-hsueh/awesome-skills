## § 5 · Expertise & Domain Knowledge

### 5.1 Test Strategy Framework

**Test Type Selection Matrix**

| Test Type | Scope | Speed | Cost | Primary Tools | Best For |
|-----------|-------|-------|------|---------------|----------|
| **Unit** | Function/Class | < 1ms | Very Low | Jest, pytest, JUnit, Vitest | Business logic, algorithms, pure functions |
| **Integration** | Component Group | 100ms–10s | Medium | TestContainers, Supertest, Pact | DB queries, HTTP clients, message queues |
| **Contract** | API Boundaries | 1–10s | Medium | Pact, Spring Cloud Contract | Microservice API compatibility |
| **E2E** | Full User Journey | 5–60s | High | Playwright, Cypress, Selenium | Critical user flows, regression |
| **Performance** | Load/Stress | Minutes | High | k6, Gatling, Locust, JMeter | Capacity planning, bottleneck detection |
| **Security** | Vulnerability | Minutes | Medium | ZAP, Semgrep, Snyk, Trivy | OWASP compliance, dependency audit |
| **Visual** | UI Appearance | Seconds | Medium | Percy, Chromatic, Applitools | UI regression, responsive design |
| **Accessibility** | WCAG Compliance | Seconds | Low | axe-core, Pa11y, Lighthouse | A11y automation, compliance |

**Risk-Based Prioritization Model**

```
                    IMPACT
         Low          Medium         High
       ┌─────────┬─────────┬─────────┐
   H   │  Skip   │ Automate│ Exhaust │
   i   │ Manual  │ Basic   │ Test    │
   g   │ Only    │ Happy   │ Happy+  │
   h   │         │ Path    │ Edge+   │
 P     ├─────────┼─────────┼─────────┤
 r   M │  Skip   │ Sample  │ Focus   │
 o   e │ or      │ Test    │ Critical│
 b   d │ Manual  │         │ Paths   │
 a   i ├─────────┼─────────┼─────────┤
 b   u │  Skip   │ Skip or │ Sample  │
 i   m │         │ Manual  │ Test    │
 l   L │         │         │         │
 i   o ├─────────┼─────────┼─────────┤
 t   w │  Skip   │  Skip   │ Monitor │
 y     │         │         │ Only    │
       └─────────┴─────────┴─────────┘
```

### 5.2 Automation Test Architecture

**Framework Architecture Pattern**

```
┌─────────────────────────────────────────────────────────────┐
│                    Test Layer (Spec Files)                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Feature  │ │ Feature  │ │ Feature  │ │ Feature  │       │
│  │ Test A   │ │ Test B   │ │ Test C   │ │ Test D   │       │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘       │
└───────┼────────────┼────────────┼────────────┼─────────────┘
        │            │            │            │
        └────────────┴──────┬─────┴────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│              Page Object / Component Layer                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  LoginPage   │  │  CheckoutPage│  │  Dashboard   │      │
│  │  - login()   │  │  - checkout()│  │  - navigate()│      │
│  │  - logout()  │  │  - verify()  │  │  - getData() │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│              Service / API Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  AuthAPI     │  │  PaymentAPI  │  │  UserAPI     │      │
│  │  - login()   │  │  - charge()  │  │  - create()  │      │
│  │  - refresh() │  │  - refund()  │  │  - update()  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│              Infrastructure Layer                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │  Driver  │  │ Database │  │  Config  │  │ Utilities│    │
│  │  (Browser│  │ Factory  │  │  Manager │  │ (Helpers)│    │
│  │   API)   │  │  Cleanup │  │          │  │          │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 Performance Testing Methodology

**Performance Test Type Selection**

| Test Type | Purpose | Duration | Load Pattern | Key Metrics |
|-----------|---------|----------|--------------|-------------|
| **Smoke Test** | Validate system functions under minimal load | 1-5 min | 1-10 users | Error rate, basic response time |
| **Load Test** | Verify system handles expected traffic | 10-30 min | Production average | p50, p95, p99 latency, throughput |
| **Stress Test** | Find breaking point and recovery behavior | 10-20 min | Ramp to failure | Max capacity, degradation point |
| **Spike Test** | Validate handling of sudden traffic surges | 5-10 min | Sudden high peak | Recovery time, error handling |
| **Soak Test** | Detect memory leaks and stability issues | 2-24 hours | Sustained average | Memory growth, connection pool |
| **Breakpoint** | Determine maximum sustainable load | Variable | Incremental ramp | Saturation point, resource limits |

**Performance Testing Hierarchy**

```
Level 1: Unit Performance
├─ Algorithm complexity analysis
├─ Big O benchmarking
└─ Micro-benchmarks (Benchmark.js, JMH)

Level 2: Component Performance
├─ API endpoint latency
├─ Database query performance
└─ Cache hit ratio validation

Level 3: Integration Performance
├─ Service-to-service latency
├─ End-to-end flow timing
└─ Resource contention analysis

Level 4: System Performance
├─ Full system load testing
├─ Production traffic simulation
└─ Capacity planning validation
```

### 5.4 Defect Management Process

**Defect Lifecycle Workflow**

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│   New    │───→│  Triage  │───→│ Assigned │───→│ In Fixed │
│          │    │          │    │          │    │ Progress │
└──────────┘    └──────────┘    └──────────┘    └────┬─────┘
      ↑                                              │
      └──────────────────────────────────────────────┘
┌──────────┐    ┌──────────┐    ┌──────────┐        │
│  Closed  │←───│ Verified │←───│  Ready   │←───────┘
│          │    │          │    │  for QA  │
└──────────┘    └──────────┘    └──────────┘
```

**Defect Severity Classification**

| Severity | Definition | Response SLA | Examples |
|----------|-----------|--------------|----------|
| **P0 - Critical** | System unusable, data loss, security breach | Immediate (24h) | Login broken, payment failing, data corruption |
| **P1 - High** | Major feature broken, workaround exists | 48 hours | Search not working, reports failing |
| **P2 - Medium** | Feature partially affected | 1 week | UI glitch, minor functionality issue |
| **P3 - Low** | Cosmetic, documentation, enhancement | Next sprint | Typos, alignment issues |

---
