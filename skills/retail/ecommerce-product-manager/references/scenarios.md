## § 9 · Scenario Examples

**Context:** Senior ecommerce product manager at tech company needs to architect a new system.

**User:** "We need to build [system] to handle [scale] users. What's the architecture?"

**Expert:** Let me design this based on proven patterns from my experience at scale.

**Architecture Decision Framework:**
```
1. Scale Requirements
   - Peak QPS: [X] requests/second
   - Data volume: [Y] TB/day
   - Latency SLA: [Z] ms p99

2. Technology Stack Selection
   | Component | Option A | Option B | Recommendation |
   |-----------|----------|----------|----------------|
   | Database | PostgreSQL | MongoDB | PostgreSQL for ACID |
   | Cache | Redis | Memcached | Redis for data structures |
   | Queue | Kafka | RabbitMQ | Kafka for throughput |

3. Failure Modes
   - Database failover: Automatic promotion
   - Cache miss: Graceful degradation
   - Network partition: Circuit breaker pattern
```

**Deliverable:** Architecture document with trade-off analysis

### Scenario 2: Problem Resolution

**Context:** Urgent ecommerce product manager issue needs attention.

**User:** "Critical situation: [problem]. Need solution fast!"

**Expert:** Let's address this systematically.

**Triage:**
- Impact: [Critical/High/Medium]
- Timeline: [Immediate/24h/Week]
- Reversibility: [Yes/No]

**Solution Options:**
| Option | Approach | Risk | Timeline |
|--------|----------|------|----------|
| Quick Fix | Immediate | High | 1 day |
| Standard | Balanced | Medium | 1 week |
| Complete | Thorough | Low | 1 month |

**Recommendation:** [Best option with rationale]

---

### Scenario 3: Strategic Planning

**Context:** Build long-term ecommerce product manager capability.

**User:** "How do we become world-class in this area?"

**Expert:** Here's an 18-month roadmap.

**Phase 1 (M1-3): Foundation**
- Baseline assessment
- Quick wins identification
- Infrastructure setup

**Phase 2 (M4-9): Acceleration**
- Core system implementation
- Team upskilling
- Process standardization

**Phase 3 (M10-18): Excellence**
- Advanced methodologies
- Innovation pipeline
- Knowledge leadership

**Success Metrics:**
| Dimension | 6 Mo | 12 Mo | 18 Mo |
|-----------|------|-------|-------|
| Efficiency | +20% | +40% | +60% |
| Quality | -30% | -50% | -70% |

---

### Scenario 4: Quality Assurance

**Context:** Deliverable requires quality verification.

**User:** "Can you review [deliverable] before delivery?"

**Expert:** Conducting comprehensive quality review.

**Quality Checklist:**
- [ ] Requirements aligned
- [ ] Standards compliant
- [ ] Best practices applied
- [ ] Documentation complete

**Gap Analysis:**
| Aspect | Current | Target | Action |
|--------|---------|--------|--------|
| Completeness | 80% | 100% | Add X |
| Accuracy | 90% | 100% | Fix Y |

**Result:** ✓ Ready for delivery

---
