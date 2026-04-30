## § 4 · Core Philosophy

### 4.1 Stack Mental Model

```
┌─────────────────────────────────────────┐
│           User Interface                │  ← React/Vue, accessible, responsive
├─────────────────────────────────────────┤
│         State Management                │  ← Zustand/Redux, React Query, caching
├─────────────────────────────────────────┤
│           API Layer                     │  ← REST/GraphQL, typed contracts
├─────────────────────────────────────────┤
│         Business Logic                  │  ← Services, validation, workflows
├─────────────────────────────────────────┤
│           Data Access                   │  ← Repository pattern, ORM/Query Builder
├─────────────────────────────────────────┤
│          Database                       │  ← PostgreSQL/MongoDB, indexes, migrations
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Type Safety Across Stack** — Shared TypeScript types; runtime validation with Zod
2. **Test at Multiple Levels** — Unit for logic, integration for APIs, E2E for critical paths
3. **Optimize for Maintenance** — Code is read 10× more than written; clarity over cleverness
4. **Security in Depth** — Validation at every boundary; never trust client input
5. **Performance Budgets** — Define and enforce limits; measure real user experience

---
