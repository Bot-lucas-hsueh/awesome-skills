## § 9 · Common Pitfalls

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **God Component** | 1000-line React component | Split into smaller, focused components |
| **Prop Drilling** | Props passed through 5+ layers | Use context or state management |
| **API Coupling** | Frontend directly calls backend URLs | API client abstraction layer |
| **No Error Boundaries** | One error crashes entire app | React Error Boundaries, error reporting |
| **Over-fetching** | API returns data not used | GraphQL or query parameters |
| **Missing Input Validation** | Trusting client input | Zod validation on both ends |

---
