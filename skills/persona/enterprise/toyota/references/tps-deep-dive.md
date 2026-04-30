# Toyota Production System (TPS) - Deep Dive

## Historical Development

### Origins (1940s-1950s)

**Sakichi Toyoda** (1867-1930):
- Founder of Toyoda Automatic Loom Works
- Invented automatic loom with "stop-at-defect" mechanism
- This principle became the foundation of Jidoka

**Kiichiro Toyoda** (1894-1952):
- Established Toyota Motor Corporation (1937)
- Visited Ford Rouge plant in 1929
- Conceived "Just-in-Time" concept
- "We should produce only what we need, when we need it"

**Taiichi Ohno** (1912-1990):
- Chief Engineer of TPS development
- Created Kanban system (1950s)
- Authored "Toyota Production System: Beyond Large-Scale Production"
- Known as the "father of TPS"

**Eiji Toyoda** (1913-2013):
- Led Toyota's modernization (1950s-1980s)
- Championed TPS implementation
- Oversaw global expansion

**Shigeo Shingo** (1909-1990):
- Industrial engineer consultant to Toyota
- Developed SMED (Single-Minute Exchange of Die)
- Created Poka-Yoke (error-proofing)
- Authored "A Study of the Toyota Production System"

---

## The House of TPS - Detailed

### Foundation: Stability & Standardization

**Standardized Work (標準作業 - Hyōjun Sagyō):**

Three elements:
1. **Takt Time** - Rate of customer demand
2. **Work Sequence** - Steps in correct order
3. **Standard WIP** - Minimum inventory to maintain flow

Standardized work is:
- The current best known method
- The baseline for improvement
- Living documentation (updated after each Kaizen)

### Left Pillar: JIT (Just-in-Time)

**Takt Time (タクトタイム):**

```
Takt Time = Available Production Time / Customer Demand

Example:
- Available time: 480 minutes/shift (8 hours)
- Customer demand: 240 units/shift
- Takt Time = 480 / 240 = 2 minutes/unit
```

**Continuous Flow (流れ作業 - Nagare Sagyō):**

- One-piece flow where possible
- Small batch transfer when necessary
- Eliminate batch-and-queue mentality

**Pull System (引き取り - Hikitori):**

```
Customer → Process N → Process N-1 → ... → Process 1 → Supplier
   ↑          ↑            ↑                    ↑          ↑
  (pull)    (pull)       (pull)               (pull)     (pull)
```

Kanban types:
- **Production Kanban** (P-kanban): Signal to produce
- **Withdrawal Kanban** (W-kanban): Signal to move
- **Signal Kanban**: For batch processes

**Kanban Rules:**
1. Never pass on defective products
2. Take only what is needed
3. Produce the exact quantity required
4. Level the production
5. Fine-tune production
6. Stabilize and rationalize the process

### Right Pillar: Jidoka (Autonomation)

**Definition:** Automation with a human touch - machines stop when abnormalities occur.

**Four Stages:**

1. **Detection** - Identify abnormality
   - Sensors (automatic)
   - Operators (manual)
   - Statistical process control

2. **Stop** - Halt the process
   - Andon cord (manual stop)
   - Automatic machine stop
   - Line stop authority

3. **Fix** - Immediate response
   - Contain the defect
   - Restore normal condition
   - Resume production

4. **Solve** - Root cause elimination
   - 5 Whys analysis
   - Countermeasure implementation
   - Standardization

**Andon System (行灯 - Originally paper lantern):**

```
Green  → Normal operation
Yellow → Attention needed (line continues)
Red    → Stop (abnormality detected)

Operator pulls Andon cord → Light turns yellow
Team leader responds within seconds
If resolved: Green restored
If not resolved: Red light, line stops
```

### Cross-Beams: Heijunka & Built-in Quality

**Heijunka (平準化 - Production Leveling):**

```
Without Heijunka (Batch Production):
Mon: 100 A | Tue: 100 A | Wed: 100 B | Thu: 100 B | Fri: 100 C

With Heijunka (Mixed Production):
Mon-Fri: 20 A, 20 A, 20 B, 20 B, 20 C (each day)
```

Benefits:
- Reduced inventory
- Flexible response to demand changes
- Balanced workload
- Exposes problems quickly

**Built-in Quality (品質内作り - Hinshitsu Uchi-zukuri):**

- Quality at the source
- 100% inspection by machines or operators
- Self-quality (Jiko-kansei)
- Successive check (Tsugiarai)

---

## The Seven Wastes (Muda) - Expanded

### 1. Overproduction (生産過多 - Seisan Kata)

**Definition:** Producing more, earlier, or faster than needed.

**Why it's the worst waste:**
- Creates inventory (carries costs)
- Hides other problems
- Increases lead time
- Risk of obsolescence

**Symptoms:**
- Large WIP inventories
- Early production schedules
- "Just in case" production

**Countermeasures:**
- Takt time production
- Pull system
- SMED (reduce batch sizes)

### 2. Waiting (待ち - Machi)

**Definition:** Idle time when value is not being added.

**Types:**
- Material waiting
- Machine breakdown
- Operator waiting
- Approval waiting

**Countermeasures:**
- Continuous flow
- Preventive maintenance
- Balanced workloads
- Parallel processing

### 3. Transport (運搬 - Unpan)

**Definition:** Unnecessary movement of materials.

**Causes:**
- Poor layout
- Centralized operations
- Large batch sizes

**Countermeasures:**
- Cellular manufacturing
- Point-of-use storage
- Smaller batch sizes

### 4. Over-processing (過加工 - Kako-sugi)

**Definition:** More work than required by the customer.

**Examples:**
- Excess precision
- Redundant inspections
- Unnecessary reports
- Extra polishing/protection

**Countermeasures:**
- Understand customer requirements
- Value stream mapping
- Standard work

### 5. Inventory (在庫 - Zaiko)

**Definition:** Excess materials beyond immediate needs.

**Types:**
- Raw material
- Work-in-process (WIP)
- Finished goods
- Indirect materials

**Why inventory is waste:**
- Carrying costs
- Obsolescence risk
- Damage risk
- Hides problems

**Countermeasures:**
- JIT production
- Pull system
- SMED

### 6. Motion (動作 - Dosa)

**Definition:** Unnecessary movement by people.

**Examples:**
- Reaching for tools
- Walking to get parts
- Searching for items
- Awkward positions

**Countermeasures:**
- 5S workplace organization
- Ergonomic design
- Point-of-use storage

### 7. Defects (不良品 - Furyo-hin)

**Definition:** Products that don't meet specifications.

**Costs:**
- Scrap
- Rework
- Inspection
- Warranty
- Lost reputation

**Countermeasures:**
- Jidoka (stop at defect)
- Poka-yoke (error-proofing)
- Source inspection
- Standard work

---

## Support Tools & Techniques

### 5S Workplace Organization

| Japanese | English | Purpose |
|----------|---------|---------|
| Seiri | Sort | Keep only what is needed |
| Seiton | Set in order | A place for everything |
| Seiso | Shine | Clean and inspect |
| Seiketsu | Standardize | Make it routine |
| Shitsuke | Sustain | Discipline to maintain |

### Poka-Yoke (防誤 - Mistake-proofing)

**Types:**

1. **Control Type** - Cannot make error
   - Wrong part won't fit
   - Wrong sequence prevented

2. **Warning Type** - Alerts to error
   - Alarm
   - Light
   - Buzzer

**Examples:**
- Asymmetric connectors
- Sensors detecting presence
- Checklists
- Templates and fixtures

### SMED (Single-Minute Exchange of Die)

**Steps:**

1. **Separate internal/external setup**
   - Internal: Can only do when machine stopped
   - External: Can do while machine running

2. **Convert internal to external**
   - Pre-heating dies
   - Pre-assembly
   - Standardization

3. **Streamline all aspects**
   - Quick fasteners
   - Locating pins
   - Eliminate adjustments

4. **Eliminate adjustments**
   - Fixed stops
   - Standard settings

**Target:** Reduce changeover to under 10 minutes (single-digit).

### Value Stream Mapping (VSM)

**Current State Map:**
- Shows actual flow
- Documents wait times
- Identifies waste

**Future State Map:**
- Design improved flow
- Apply TPS principles
- Set implementation plan

**Icons:**
```
[===] Process box
<<  >> Inventory triangle
────── Push arrow
────► Pull arrow
⚡ Electronic information
📋 Kanban signal
```

---

## Kaizen (改善 - Continuous Improvement)

### Types of Kaizen

| Type | Scope | Duration | Frequency |
|------|-------|----------|-----------|
| **Point Kaizen** | Single workstation | Immediate | Daily |
| **Line Kaizen** | Production line | Days-weeks | Monthly |
| **System Kaizen** | Value stream | Months | Quarterly |
| **Innovation** | Breakthrough | Years | As needed |

### Kaizen Event Structure

**Pre-Event (1 week):**
- Define scope and objectives
- Collect baseline data
- Train team in Kaizen methodology

**Event Week:**

| Day | Activity |
|-----|----------|
| Mon | Training, current state observation |
| Tue | Analyze waste, identify root causes |
| Wed | Develop countermeasures |
| Thu | Implement improvements |
| Fri | Validate results, standardize, report |

**Post-Event:**
- Monitor results (30, 60, 90 days)
- Yokoten (share to other areas)
- Document lessons learned

### The Kaizen Mindset

**Principles:**
1. Everything can be improved
2. Every problem is an opportunity
3. Go to gemba (actual place)
4. Ask "Why?" five times
5. Small improvements add up
6. Everyone participates
7. Focus on process, not blame

---

## Hoshin Kanri (方針管理 - Policy Deployment)

**Purpose:** Align organizational goals from top to bottom.

**The Process:**

```
Corporate Vision (3-5 years)
         ↓
Annual Hoshin (Objectives)
         ↓
Department Objectives
         ↓
Team/Individual Targets
         ↓
Daily Management
```

**Key Elements:**

1. **Strategic Planning** (Top-down)
   - What must we achieve?
   - Why is it important?

2. **Catchball** (Bidirectional)
   - Discussion between levels
   - Negotiation of targets
   - Resource allocation

3. **Implementation** (Bottom-up)
   - Action plans
   - Monthly reviews
   - Problem-solving

4. **Review** (Continuous)
   - Annual review
   - Learn and adjust
   - Standardize success

---

## Summary: TPS Principles

| Principle | Japanese | Application |
|-----------|----------|-------------|
| Go and See | Genchi Genbutsu | Observe actual situation |
| Ask Why Five Times | 5 Whys | Root cause analysis |
| Mistake-proof | Poka-yoke | Build in quality |
| Visual Management | Mieruka | Make problems visible |
| Continuous Improvement | Kaizen | Never accept status quo |
| Respect for People | Hitonami Soncho | Develop people |
| Level Production | Heijunka | Smooth flow |
| Right-sized | Chobo Seisan | Match capacity to demand |

---

*Reference: Toyota Motor Corporation, "The Toyota Way" (2001, 2020)*
*Ohno, Taiichi. "Toyota Production System" (1988)*
*Liker, Jeffrey. "The Toyota Way" (2004)*
