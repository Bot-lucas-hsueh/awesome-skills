## 8. System Design Workflow

### Phase 1: Requirements Understanding & Constraint Analysis

**Objectives**: Clarify requirements, quantify constraints, identify risks

**Key Activities**:
1. Understand business requirements
   - Functional requirements (what system does)
   - User growth projections
   - Revenue/profitability expectations

2. Define non-functional requirements
   - Scale (users, requests/sec, data volume)
   - Latency requirements (P95, P99 response times)
   - Availability targets (99.9%, 99.99%, etc.)
   - Data consistency requirements

3. Identify constraints
   - Budget and cost constraints
   - Timeline to market
   - Team size and expertise
   - Existing infrastructure/tech debt

4. Analyze failure scenarios
   - What happens if databases fail?
   - What if network partitions?
   - What if load spikes 10x?
   - What if we lose a region?

**Success Criteria**:
- Requirements documented and quantified
- Constraints explicitly acknowledged
- Growth scenarios defined (1yr, 3yr, 10x)
- Failure modes identified

---

### Phase 2: Architecture Design & Technology Selection

**Objectives**: Design architecture, make technology choices, document rationale

**Key Activities**:
1. Design system components
   - API design and contract
   - Service boundaries
   - Data models
   - Communication patterns

2. Select data storage
   - SQL vs. NoSQL trade-offs
   - Partitioning/sharding strategy
   - Replication approach
   - Caching layers

3. Design for scale
   - Horizontal scalability patterns
   - Load balancing strategy
   - Rate limiting and quotas
   - Async processing approach

4. Plan for resilience
   - Failure detection
   - Automatic recovery
   - Circuit breakers
   - Graceful degradation

5. Document architecture
   - Create architecture diagrams (C4 models)
   - Write Architecture Decision Records (ADRs)
   - Document trade-off analysis
   - Share design with team

**Success Criteria**:
- Architecture clearly addresses all requirements
- Technology choices justified with trade-off analysis
- Design diagrams created and reviewed
- Team understands and agrees on approach
- Risks and mitigation strategies documented

---

### Phase 3: Implementation, Validation & Evolution

**Objectives**: Build system, validate design, evolve based on learnings

**Key Activities**:
1. Guide implementation
   - Architecture reviews during development
   - Code review for compliance
   - Help team understand patterns

2. Build observability
   - Comprehensive logging
   - Performance metrics collection
   - Distributed tracing
   - Alerting on anomalies

3. Validate design
   - Load testing to specification
   - Chaos engineering (intentional failures)
   - Production validation

4. Optimize based on real usage
   - Monitor key metrics
   - Identify bottlenecks
   - Performance tuning
   - Cost optimization

5. Plan evolution
   - Assess technical debt
   - Plan refactoring
   - Design next architecture generation
   - Document learnings for team

**Success Criteria**:
- System meets performance specifications
- Resilience proven in production
- Team can diagnose and resolve issues
- Cost is optimized
- Technical debt managed
