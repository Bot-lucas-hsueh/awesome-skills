# Danaher Business System (DBS) - Detailed Tool Library

## Core DBS Tools Expanded

### 1. Value Stream Mapping (VSM)

**Purpose:** Visualize material and information flow to identify waste and improvement opportunities.

**Process:**
1. Select product family
2. Map current state (material flow + information flow)
3. Identify waste (7 types)
4. Design future state
5. Create implementation plan

**Key Metrics:**
- Process Cycle Efficiency (PCE) = Value-Added Time / Total Lead Time
- Target: PCE > 25% for most processes

**Example - Lab Testing Process:**
```
Current State:  Customer → Order → Collect → Transport → Receive → Prep → Test → Review → Report → Customer
                Day 0     Day 0   Day 0    Day 0-1    Day 1     Day 1   Day 2    Day 2-3   Day 3     Day 4
                
                Total Lead Time: 4 days
                Value-Added Time: 2 hours
                PCE: 2.1%
                
Future State:   Customer → Order → Collect → Test (point of care) → Review → Report → Customer
                Day 0     Day 0   Day 0    Day 0                              Day 0     Day 0
                
                Total Lead Time: Same day
                Value-Added Time: 2 hours  
                PCE: 25%+
```

---

### 2. 5S Workplace Organization

| S | Japanese | English | Description |
|---|----------|---------|-------------|
| 1 | Seiri | Sort | Remove unnecessary items |
| 2 | Seiton | Set in Order | Everything has a place |
| 3 | Seiso | Shine | Clean and inspect |
| 4 | Seiketsu | Standardize | Make it visual, maintain first 3S |
| 5 | Shitsuke | Sustain | Discipline, habit, audit |

**Audit Scorecard:**
| Area | Sort | Set | Shine | Standard | Sustain | Total |
|------|------|-----|-------|----------|---------|-------|
| Target | 90% | 90% | 95% | 90% | 85% | 90% |
| Lab A | 85% | 80% | 90% | 75% | 70% | 80% |
| Lab B | 95% | 90% | 95% | 90% | 85% | 91% |

---

### 3. Daily Management System

**Three-Tier Review Structure:**

```
┌─────────────────────────────────────────────────────────────┐
│ TIER 3: Monthly Business Review                             │
│ Attendees: President, VPs, DBS Office                       │
│ Focus: Strategic metrics, policy deployment                 │
│ Cadence: Monthly                                            │
└─────────────────────────────────────────────────────────────┘
                              ↑
┌─────────────────────────────────────────────────────────────┐
│ TIER 2: Weekly Value Stream Review                          │
│ Attendees: Directors, Managers                              │
│ Focus: Value stream metrics, cross-functional issues        │
│ Cadence: Weekly                                             │
└─────────────────────────────────────────────────────────────┘
                              ↑
┌─────────────────────────────────────────────────────────────┐
│ TIER 1: Daily Team Huddle                                   │
│ Attendees: Front-line team, Supervisor                      │
│ Focus: Yesterday's results, today's plan, barriers          │
│ Cadence: Daily, 15 minutes                                  │
└─────────────────────────────────────────────────────────────┘
```

**Visual Management Board Elements:**
- Safety
- Quality (defects, complaints)
- Delivery (OTD, lead time)
- Cost (productivity, spending)
- Growth (new products, customer acquisition)
- People (training, engagement)

---

### 4. Standard Work

**Three Elements:**
1. **Takt Time** — Rate of customer demand
2. **Work Sequence** — Steps in correct order
3. **Standard Work in Process (SWIP)** — Minimum inventory needed

**Standard Work Document Template:**

| Element | Description | Specification |
|---------|-------------|---------------|
| Process | | |
| Version | | Date: |
| Takt Time | | |
| Cycle Time | | |
| Work Sequence | Step 1: | |
| | Step 2: | |
| | Step 3: | |
| SWIP | | units |
| Quality Check | | |
| Safety Note | | |

---

### 5. Problem Solving Process (PSP)

**The 8-Step Method:**

1. **Clarify the Problem** — Define gap between current and target
2. **Break Down the Problem** — Identify specific areas for analysis
3. **Target Setting** — Set measurable improvement targets
4. **Root Cause Analysis** — Use 5 Whys, Fishbone, 5M1E
5. **Develop Countermeasures** — Generate and select solutions
6. **See Countermeasures Through** — Implement with plan-do-check-act
7. **Monitor Results and Process** — Track metrics, validate improvement
8. **Standardize Successful Processes** — Share best practices, update SOPs

**A3 Report Structure:**
- Theme (problem statement)
- Background (why it matters)
- Current situation
- Goal
- Root cause analysis
- Action plan
- Follow-up

---

### 6. Policy Deployment (Hoshin Kanri)

**Catchball Process:**
```
Corporate Goals → Segment Goals → Operating Co Goals → Team Goals → Individual Goals
       ↓                ↓                ↓                 ↓               ↓
   (Top-down)      (Negotiation)    (Negotiation)     (Negotiation)   (Agreement)
       ↑                ↑                ↑                 ↑               ↑
   Feedback       Feedback         Feedback          Feedback        Input
```

**X-Matrix:**
| | Corporate Goals | Segment Goals | Operating Co Goals | Improvement Priorities |
|---|:---:|:---:|:---:|:---:|
| Segment Goals | X | | | |
| Operating Co Goals | | X | | |
| Improvement Priorities | | | X | |
| Metrics | | | | X |

---

### 7. Voice of Customer (VOC)

**Process:**
1. Plan — Define objectives, select methods
2. Collect — Interviews, surveys, observation
3. Analyze — Affinity diagram, KJ method
4. Deploy — Translate to product requirements
5. Verify — Confirm understanding with customers

**House of Quality (QFD):**
```
        Customer Requirements
        ┌─────────────────────────────────┐
        │         HOW (Technical)         │
        │         ┌───┬───┬───┬───┐       │
        │  WHAT   │   │   │   │   │       │
        │ (Cust)  ├───┼───┼───┼───┤       │
        │         │   │   │   │   │       │
        │         └───┴───┴───┴───┘       │
        │         Technical Targets       │
        └─────────────────────────────────┘
```

---

### 8. TPM (Total Productive Maintenance)

**Six Big Losses:**
1. Equipment failure
2. Setup and adjustment
3. Idling and minor stoppages
4. Reduced speed
5. Defects in process
6. Reduced yield

**OEE Calculation:**
```
OEE = Availability × Performance × Quality

Where:
- Availability = Run Time / Planned Production Time
- Performance = (Ideal Cycle Time × Total Count) / Run Time
- Quality = Good Count / Total Count

World Class: OEE > 85%
```

---

### 9. Quick Changeover (SMED)

**Principles:**
- Separate internal (machine stopped) and external (machine running) setup
- Convert internal to external setup
- Streamline both aspects
- Eliminate adjustment

**Changeover Improvement Example:**
| Step | Original | Improved | Improvement |
|------|----------|----------|-------------|
| Preparation | 30 min | 5 min | External |
| Remove old tooling | 20 min | 10 min | Internal → Simplified |
| Install new tooling | 25 min | 12 min | Internal → Standardized |
| Adjustments | 45 min | 5 min | Eliminated through presetting |
| **Total** | **120 min** | **32 min** | **73% reduction** |

---

### 10. Kanban Pull System

**Types:**
- Production Kanban — Authorizes production
- Withdrawal Kanban — Authorizes movement
- Signal Kanban — For batch processes

**Kanban Formula:**
```
Number of Kanban = (Daily Demand × Lead Time × (1 + Safety Stock)) / Container Quantity
```

**Kanban Rules:**
1. Customer withdraws only what is needed
2. Producing processes make only what is withdrawn
3. Defects are never passed to the next process
4. Minimize kanban quantity
5. Use kanban for continuous improvement

---

## DBS Growth Tools

### Growth Throughput Analysis

| Stage | Lead Source | Conversion Rate | Target |
|-------|-------------|-----------------|--------|
| Awareness | Marketing | 10% to MQL | 15% |
| Consideration | SDR | 25% to SQL | 30% |
| Decision | AE | 30% to Opportunity | 35% |
| Purchase | Close | 40% to Customer | 45% |

### Pricing Excellence Framework

| Approach | When to Use | Typical Impact |
|----------|-------------|----------------|
| Cost-Plus | Commodity markets | Baseline |
| Value-Based | Differentiated products | +5-15% margin |
| Competitive | Crowded markets | Market parity |
| Dynamic | Elastic demand | +2-8% revenue |

---

*For additional DBS tools and training materials, see internal DBS portal.*
