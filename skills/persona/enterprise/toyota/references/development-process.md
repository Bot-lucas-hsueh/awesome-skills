# Toyota Development System - Product Creation Process

## Overview

The Toyota Development System applies TPS principles to product development:
- **Just-in-Time**: Right information at right time
- **Jidoka**: Build quality into the design
- **Kaizen**: Continuous improvement of development process

---

## Development Phases

### Phase 1: Concept Development (12-18 months)

**Objectives:**
- Define customer needs
- Establish product concept
- Set targets (QCD: Quality, Cost, Delivery)
- Assign Chief Engineer

**Key Activities:**

| Activity | Output | Owner |
|----------|--------|-------|
| Market research | Customer needs document | Product Planning |
| Competitive analysis | Benchmark report | Planning/Engineering |
| Technology assessment | Feasibility study | R&D |
| Concept development | 2-3 concept proposals | Chief Engineer |
| Business case | Investment approval | Management |

**Target Setting (Example):**

```
┌─────────────────────────────────────────────────────────────┐
│ VEHICLE TARGET SETTING                                      │
├─────────────────────────────────────────────────────────────┤
│ QUALITY                                                     │
│ ├── JD Power IQS: Top 3 in segment                          │
│ ├── Reliability: <50 IPTV at 12 months                      │
│ └── Safety: IIHS Top Safety Pick+                           │
│                                                             │
│ COST                                                        │
│ ├── Target cost: $XX,XXX manufacturing                      │
│ ├── Price position: Competitive with [benchmark]            │
│ └── Profit margin: X%                                       │
│                                                             │
│ DELIVERY                                                    │
│ ├── Launch date: MM/YYYY                                    │
│ ├── Volume ramp: 10K → 50K/month                            │
│ └── Dealer availability: Day 1                              │
│                                                             │
│ PERFORMANCE                                                 │
│ ├── Fuel economy: XX mpg combined                           │
│ ├── Acceleration: 0-60 mph in X sec                         │
│ └── Technology: Feature list                                │
└─────────────────────────────────────────────────────────────┘
```

### Phase 2: Planning (6-12 months)

**Objectives:**
- Finalize specifications
- Select suppliers
- Develop project plan

**Key Activities:**

1. **Design Freeze Preparation**
   - Trade-off curve development
   - Multiple concept exploration
   - Decision criteria definition

2. **Supplier Selection**
   - RFQ issuance
   - Technical evaluation
   - Cost negotiation
   - Partnership agreement

3. **Detailed Planning**
   - Master schedule
   - Resource allocation
   - Risk assessment
   - Budget approval

### Phase 3: Development (24-36 months)

**Objectives:**
- Design and validate vehicle
- Prepare manufacturing
- Ensure quality targets

**Development Stages:**

```
Concept ──► Planning ──► Alpha ──► Beta ──► Pilot ──► SOP
   │           │          │         │        │        │
  12-18m      6-12m      6-9m      6-9m     6m      Launch
```

#### Alpha Prototype Stage

**Purpose:** Design validation

| Aspect | Details |
|--------|---------|
| Quantity | 50-100 units |
| Build method | Hand-built |
| Focus | Function verification |
| Testing | Lab, track, environmental |

**Key Tests:**
- Powertrain integration
- Structural integrity
- Electronics function
- Safety systems

#### Beta Prototype Stage

**Purpose:** Production validation

| Aspect | Details |
|--------|---------|
| Quantity | 200-500 units |
| Build method | Pilot tooling |
| Focus | Manufacturing process |
| Testing | Durability, certification |

**Key Tests:**
- Reliability (100K+ miles)
- Regulatory certification
- NVH refinement
- Real-world durability

#### Production Validation

**Purpose:** Confirm production readiness

| Checkpoint | Criteria |
|------------|----------|
| Tooling complete | All hard tools ready |
| Process capability | Cpk > 1.33 for critical |
| Supplier PPAP | All suppliers approved |
| Quality targets | IPTV targets demonstrated |

### Phase 4: Launch (6-12 months)

**Objectives:**
- Ramp production smoothly
- Achieve quality targets
- Support dealers

**Ramp Sequence:**

```
Pilot Production ──► Tryout ──► Mass Production Trial ──► Full Production
    (10/day)           (100/day)        (1000/day)           (Full)
        │                  │                 │                  │
        └──────────────────┴─────────────────┴──────────────────┘
                              Quality Gates
```

**Launch Checklist:**

- [ ] Production rate meets takt time
- [ ] Quality metrics at target
- [ ] Service training complete
- [ ] Parts availability confirmed
- [ ] Marketing campaign ready
- [ ] Dealer preparation complete

---

## Chief Engineer (主査 - Shusa) System

### Role and Responsibilities

The Chief Engineer has total responsibility for the vehicle from concept to launch and beyond.

**Scope:**
- Product concept and market fit
- Design and engineering decisions
- Quality, cost, timing targets
- Cross-functional leadership
- Supplier coordination

**Authority:**
- Directs engineering teams
- Approves design decisions
- Selects major suppliers
- Reports to board on progress

### Chief Engineer Selection

**Qualifications:**
- 15+ years engineering experience
- Multiple previous programs
- Demonstrated leadership
- Customer-focused mindset

**Tenure:**
- Typically 4-5 years per vehicle
- May lead multiple variants
- Continues through first year of production

### Obeya (大部屋 - Great Room)

**Purpose:** Visual management center for program.

**Elements:**

| Wall | Content |
|------|---------|
| **Schedule** | Master timeline, milestones, critical path |
| **Quality** | Issues, countermeasures, verification status |
| **Cost** | Target vs. actual, cost reduction progress |
| **Design** | Current design, issues, decisions pending |
| **Supplier** | Status, issues, PPAP progress |

**Meetings:**
- Daily stand-up (15 minutes)
- Weekly deep-dive (2 hours)
- Monthly management review

---

## Set-Based Concurrent Engineering

### Concept

Rather than committing to one design early, explore multiple alternatives in parallel, delaying final decisions until maximum knowledge is available.

**Comparison:**

| Traditional | Set-Based |
|-------------|-----------|
| Pick one concept early | Keep multiple options open |
| Design then optimize | Explore then decide |
| Point-based commitments | Delayed commitment |
| Sequential decisions | Parallel exploration |

### Trade-Off Curves

**Purpose:** Understand relationships between design parameters.

**Example:**

```
Weight vs. Cost Trade-Off

Cost
  │
  │    ●────────●
  │   /  Option A  \
  │  /              \
  │ ●   Option B     ●
  │/                  \
  │                    ●
  └─────────────────────────
     Light    Medium   Heavy
              Weight

Option A: Aluminum structure - lighter, more expensive
Option B: Steel structure - heavier, less expensive
```

### Knowledge-Based Strategy

**Process:**

1. **Identify critical decisions**
2. **Define what you need to know**
3. **Plan learning activities**
4. **Explore alternatives in parallel**
5. **Delay commitment until necessary**
6. **Make informed decision**

---

## Supplier Integration

### Early Involvement

**Benefits:**
- Supplier expertise in design
- Manufacturing feasibility
- Cost optimization
- Quality built-in

**Timing:**

| Phase | Supplier Activity |
|-------|-------------------|
| Concept | Technology consultation |
| Planning | Quotation, selection |
| Development | Detailed design, prototypes |
| Production | PPAP, ramp support |

### Design for Manufacturing (DFM)

**Principles:**

| Principle | Application |
|-----------|-------------|
| Minimize parts | Reduce assembly steps |
| Standard components | Leverage existing parts |
| Mistake-proof design | Poka-yoke features |
| Tolerance analysis | Ensure fit/function |
| Assembly sequence | Logical build order |

---

## Quality in Development

### Design for Quality

**Tools:**

| Tool | Purpose | Timing |
|------|---------|--------|
| FMEA | Identify potential failures | Design phase |
| Fault Tree | Analyze failure pathways | Design phase |
| Design Review | Verify requirements met | Milestones |
| Simulation | Virtual validation | Continuous |

### Design Validation Plan

**Testing Matrix:**

| Test Type | Environment | Duration | Samples |
|-----------|-------------|----------|---------|
| Functional | Lab | Varies | All prototypes |
| Durability | Track | 100K+ miles | Beta fleet |
| Environmental | Hot/cold chambers | Cycles | Component |
| Safety | Crash facility | As needed | Vehicle |
| Reliability | Real world | 12+ months | Customer fleet |

---

## Cost Management

### Target Costing

**Process:**

```
Market price (what customer will pay)
     -
Target profit (required margin)
     =
Target cost (maximum manufacturing cost)
     ↓
Allocate to systems/subsystems
     ↓
Engineering design to target
```

**Cost Reduction Activities:**

| Phase | Activity | Typical Savings |
|-------|----------|-----------------|
| Design | Value engineering | 5-10% |
| Sourcing | Supplier negotiation | 3-5% |
| Manufacturing | Process improvement | 2-3%/year |

---

## Risk Management

### Risk Assessment Matrix

| Probability | Impact Low | Medium | High |
|-------------|------------|--------|------|
| High | Yellow | Red | Red |
| Medium | Green | Yellow | Red |
| Low | Green | Green | Yellow |

### Common Development Risks

| Risk | Mitigation |
|------|------------|
| Technology readiness | Early prototyping, backup plans |
| Supplier capability | Early involvement, development support |
| Quality escapes | Rigorous testing, phased launch |
| Timing delays | Buffer in schedule, critical path focus |
| Cost overrun | Target costing, VE activities |

---

## Key Performance Indicators

### Development Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Timing adherence | 100% | Milestone achievement |
| Quality at launch | Top 3 | JD Power IQS |
| Cost achievement | ±2% | vs. target |
| Engineering changes | <5% post-design freeze | Change count |
| Supplier PPAP | 100% on-time | Schedule adherence |

### Post-Launch Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Initial quality | Top 3 segment | JD Power IQS |
| Reliability | <50 IPTV | Warranty data |
| Customer satisfaction | >80% | Surveys |
| Cost reduction | 3%/year | Kaizen tracking |

---

## Lessons from Toyota Development

### Success Factors

1. **Chief Engineer system** - Clear accountability
2. **Set-based engineering** - Better decisions through parallel exploration
3. **Supplier integration** - Early involvement, shared expertise
4. **Visual management** - Obeya makes problems visible
5. **Cadence and discipline** - Regular reviews, consistent process

### Common Pitfalls

| Pitfall | Toyota Approach |
|---------|-----------------|
| Rushing to solution | Parallel exploration |
| Siloed engineering | Cross-functional Obeya |
| Late supplier involvement | Early partnership |
| Quality inspection-based | Design in quality |
| Over-engineering | Target costing discipline |

---

*Reference: Morgan, James and Liker, Jeffrey. "The Toyota Product Development System" (2006)*
*Ward, Allen et al. "Toyota's Set-Based Concurrent Engineering" (1995)*
