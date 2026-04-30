## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: The Distributed Monolith

```
❌ BAD: "Microservices" that split by technical layer instead of business domain.
   OrderAPI → OrderService → OrderDB (shared with InventoryService and UserService)
   Result: You have 3 deployable units but one shared database.
   Changing the orders table requires coordinating 3 teams. Deploy one service,
   break another. You have the operational complexity of microservices with
   none of the organizational independence.

✅ GOOD: Services own their data. OrderService has its own database.
   InventoryService has its own database. They communicate via events (Kafka)
   or APIs, never via direct table access. Changing OrderService schema
   requires no coordination with InventoryService.

Detection: Run this query — if two "microservices" SELECT from the same table,
you have a distributed monolith.
```

### Anti-Pattern 2: The Premature Microservice

```
❌ BAD: 3-person startup with 15 microservices, each with its own database,
   its own CI/CD pipeline, its own monitoring setup.
   Result: 80% of engineering time spent on infrastructure glue.
   New feature requires touching 6 services. On-call means debugging
   distributed traces across 15 services for a 500ms latency spike.
   Deployment requires orchestrating 15 independent release pipelines.

✅ GOOD: 3-person team → modular monolith with clear bounded contexts.
   One deployment, one database (with schema per module), one CI/CD pipeline.
   When you hit 10 engineers and teams start blocking each other's deploys,
   THEN extract the service that causes the most friction.

Rule: You need microservices when Conway's Law makes a monolith painful,
not when a blog post makes microservices sound cool.
```

### Anti-Pattern 3: Shared Database Anti-Pattern

```
❌ BAD: Multiple services reading and writing the same tables.
   UserService, OrderService, and ReportingService all query the users table.
   When UserService needs to add a column, all three teams must coordinate.
   Schema changes become release-blocking events. The database becomes
   the true coupling point, regardless of what the service diagram shows.

✅ GOOD: Each service owns its data. ReportingService gets user data via
   an event stream (Kafka user.updated events) and maintains its own
   read-optimized projection. UserService schema changes are internal —
   the event schema is the contract, versioned via a schema registry.

Migration path: Introduce an anti-corruption layer (ACL) between services
and the shared database. Gradually migrate each service to its own store
while the ACL keeps data in sync during transition.
```

### Anti-Pattern 4: The Big Ball of Mud

```
❌ BAD: No intentional architecture. Services/modules added ad-hoc over 3 years.
   OrderService depends on UserService which depends on PaymentService which
   depends on OrderService (circular). Every change breaks something unexpected.
   The system has never been fully understood by any one person.
   Change failure rate: 40%. Deploy frequency: 1 per month (too scary to deploy often).

✅ GOOD: Enforce architectural fitness functions in CI.
   - "No circular dependencies between modules" (ArchUnit
   - "Service A must not import from Service B's internal packages"
   - "All public APIs must have OpenAPI specs"
   Fail the build on violation. Architecture degrades when no automated gate enforces it.
```

### Anti-Pattern 5: Cargo Cult Architecture

```
❌ BAD: "Netflix uses microservices, so we should too."
   Copying Netflix's architecture for a 50-person company with 100k users.
   Result: 200 microservices (Netflix has 700 engineers and 200M users).
   3 SREs managing 200 services. Mean time to debug: 4 hours.
   Mean time to add a feature: 3 weeks (cross-service coordination).

✅ GOOD: Netflix's architecture solves Netflix's problems.
   Your architecture must solve your problems.
   Start with: What are your actual bottlenecks? What team boundaries cause friction?
   What quality attributes does your business actually require?
   Design for your scale, your team, your domain.

Test: "Why did we choose this pattern?" If the answer is "because [company X] uses it"
rather than "because our specific constraints require it," it's cargo cult architecture.
```

---

## 11. Integration with Other Skills

| Combination / 组合 | Workflow / 工作流 | Result
|-------------------|-----------------|--------------|
| **Software Architect + Backend Developer** | Architect produces system blueprint (C4 Level 2, ADRs, API contracts) → Backend Developer implements concrete APIs, database schemas, and service logic following the architectural constraints | Architecture blueprint realized as production-quality implementation with the right database choices, API patterns, and inter-service communication |
| **Software Architect + DevOps Engineer** | Architect defines system boundaries, scaling requirements, and SLOs → DevOps Engineer designs infrastructure, Kubernetes topology, CI/CD pipelines, and observability stack to match the architectural intent | Architecture intent translated into infrastructure: services deployed at the right scale, monitored with the right SLO alerts, with independent deployment pipelines per bounded context |
| **Software Architect + Security Engineer** | Architect produces threat model (trust boundaries, data flows, external integrations) → Security Engineer performs threat modeling (STRIDE), reviews auth design, validates encryption decisions, and penetration tests the system | Secure-by-design architecture with documented threat model, validated auth flows, and penetration test results before production launch |

---

## 12. Scope & Limitations

**✓ Use this skill when:**

- Designing new systems from scratch (greenfield) — defining boundaries, patterns, and technology choices
- Reviewing existing architectures for anti-patterns, coupling issues, or scalability bottlenecks
- Planning monolith-to-microservices migration with phased approach and rollback strategy
- Selecting between architectural patterns (CQRS vs. CRUD, sync vs. async, SQL vs. NoSQL)
- Writing Architecture Decision Records (ADRs) for significant technical decisions
- Capacity planning and load design for 10×–100× growth scenarios
- Evaluating build vs. buy decisions with objective trade-off matrices

**✗ Do NOT use this skill when:**

- Implementing specific API endpoints or database queries → use `backend-developer` skill instead (architecture is the blueprint, not the implementation)
- Infrastructure provisioning (Kubernetes manifests, Terraform modules) → use `devops-engineer` skill instead
- Security penetration testing or CVE analysis → use `security-engineer` skill instead
- ML model architecture and training pipeline design → use `ai-ml-engineer` skill instead (different trade-off space)
- Front-end component architecture (React/Vue state management) → use `frontend-developer` skill instead

---

## 13. How to Use This Skill

### Quick Install
```
Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/software/software-architect/SKILL.md and follow the instructions to install
```

### Trigger Words / 触发词 (Authoritative List
- "system design" / "系统设计"
- "architecture review" / "架构评审"
- "design pattern"
- "technical debt" / "技术债"
- "scalability" / "可扩展性"
- "microservices" / "微服务"
- "ADR" / "architecture decision"
- "monolith migration"

### Effective Prompts

**For System Design:**
```
Using the software-architect skill, design a [system name] for [user scale] users,
[traffic profile], and [team size] engineers. Our hard constraints are: [list constraints].
Quality attributes priority: [reliability > scalability > cost] or similar.
```

**For Architecture Review:**
```
Using the software-architect skill, review this architecture for anti-patterns.
Here is our current setup: [describe or paste diagram]. Our main pain points are: [list issues].
```

**For Migration Planning:**
```
Using the software-architect skill, create a phased migration plan from
[current state] to [target state]. We have [team size] engineers and a
[timeline] window. Current pain: [describe].
```

---

## 14. Quality Verification

### Self-Checklist

| Check / 检查项 | Rubric Dimension
|--------------|---------------------------|
| ☐ All 9 metadata fields present; no HTML comments in YAML description | Metadata Completeness |
| ☐ System Prompt has role identity + 5-gate decision framework + thinking patterns + communication style | System Prompt Depth |
| ☐ All 16 standard H2 sections present in correct order | Structure Completeness |
| ☐ Risk Disclaimer has 6 architecture-specific risks with severity icons and concrete mitigations | Risk Documentation |
| ☐ Standards section includes: pattern decision matrix, quality attributes table, ADR template, C4 notation, CAP theorem, SOLID at scale | Domain Knowledge Density |
| ☐ Standard Workflow has 3 phases with [✓ Done] and [✗ FAIL] criteria | Workflow Actionability |
| ☐ At least 3 full scenario examples with ASCII diagrams and trade-off tables | Example Quality |
| ☐ Common Pitfalls has 5 named anti-patterns with ❌ BAD
| ☐ Integration section covers 3 skill combinations with specific workflow steps | Integration Quality |
| ☐ No generic disclaimers; every risk is architecture-specific | Risk Documentation |

### Test Cases

**Test 1: Pattern Selection Capability**
```
Input: "Should we use microservices or a monolith? We're a 4-person team with 50k users."
Expected:
- Asks for traffic profile, operational maturity, and team structure
- Recommends modular monolith with concrete rationale
- States trigger conditions for migrating to microservices
- Does NOT recommend microservices for a 4-person team
```

**Test 2: Trade-off Articulation**
```
Input: "Should we use PostgreSQL or MongoDB for our user data?"
Expected:
- Asks for access patterns and consistency requirements
- Provides trade-off matrix (not just a recommendation)
- States when MongoDB would be the right choice
- Recommends PostgreSQL for transactional user data with clear rationale
```

**Test 3: Anti-Pattern Recognition**
```
Input: "We have 12 microservices but they all share the same PostgreSQL database."
Expected:
- Identifies Distributed Monolith anti-pattern by name
- Explains why this is the worst of both worlds
- Provides a phased remediation plan (ACL → event-driven → independent stores)
- Does NOT just say "that's bad" — gives a concrete migration path
```

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2026-02-26 | Full 16-section restructure following Exemplary reference: added architecture-specific Risk Disclaimer with severity icons, expanded Standards section (pattern decision matrix, ADR template, C4 notation, CAP theorem, SOLID at scale), 3-phase Standard Workflow with done/fail criteria, 3 full scenario examples with ASCII diagrams, 5 named anti-patterns with BAD/GOOD examples, Integration section, Scope & Limitations, How to Use, Quality Verification; upgraded to Exemplary 9.5/10 |
| 2.0.0 | 2026-02-19 | Expert Verified upgrade: added System Prompt §1 structure, decision framework, scenario examples, ADR template, bilingual support |
| 1.0.0 | 2026-02-16 | Initial release |

---

## 16. License & Author

This skill is licensed under the **MIT License with Attribution Requirement**.


| Permission | Status |
|------------|--------|
| Commercial use | ✅ Allowed |
| Modification | ✅ Allowed |
| Distribution | ✅ Allowed |
| Private use | ✅ Allowed |
| Attribution | ⚠️ Required |

### Attribution Requirements

When using, modifying, or distributing this skill, retain:

```
Based on Awesome Skills by neo.ai (lucas_hsueh@hotmail.com)
https://github.com/theneoai/awesome-skills
```

| Field | Details |
|-------|---------|
| **Name** | neo.ai |
| **Contact** | lucas_hsueh@hotmail.com |
| **GitHub** | https://github.com/theneoai |

### Community

- Questions → [Open an Issue](https://github.com/theneoai/awesome-skills/issues)
- Contribute → [CONTRIBUTING.md](../../CONTRIBUTING.md)
- Discuss → [GitHub Discussions](https://github.com/theneoai/awesome-skills/discussions)

---

**Author
**Maintained by
**License
**Questions? / 有问题？** [Open an issue](https://github.com/theneoai/awesome-skills/issues)
