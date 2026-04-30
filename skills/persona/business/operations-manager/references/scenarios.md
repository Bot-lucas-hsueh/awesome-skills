## § 8 · Scenario Examples

### Scenario 1: Manufacturing Line Optimization

**Context:** Electronics manufacturer with 15% defect rate and 12-day lead time.

**Assessment:**
- Current State VSM shows 8-day wait time between operations
- Constraint: Testing station (4-hour cycle time vs. 2-hour takt)
- Major wastes: Overproduction (large batches), waiting (test queue), defects (rework loop)

**Solution:**
- Implement pull system with kanban (batch size: 50 → 10)
- Add parallel testing capacity (elevate constraint)
- Poka-yoke at assembly (prevent defects at source)
- SMED on changeovers (2 hours → 30 minutes)

**Results:**
- Lead time: 12 days → 4 days (-67%)
- Defect rate: 15% → 2% (-87%)
- OEE: 62% → 84% (+35%)
- Cost savings: $2.4M annually

---

### Scenario 2: Warehouse Process Redesign

**Context:** E-commerce fulfillment center with picking accuracy of 94% and 24-hour average order cycle time.

**Assessment:**
- Travel time: 60% of picker time
- Pick errors: Wrong location picks, quantity errors
- Batch picking creates sorting bottleneck

**Solution:**
- Zone picking with parallel pick zones
- Voice-directed picking (hands-free, eyes-free)
- Slotting optimization (ABC velocity-based)
- Quality checkpoints at pack stations

**Results:**
- Picking accuracy: 94% → 99.7%
- Order cycle time: 24h → 8h (-67%)
- Units per hour: 45 → 85 (+89%)
- Labor cost per order: -40%

---

### Scenario 3: Supply Chain S&OP Implementation

**Context:** Consumer goods company with chronic stockouts (15%) and excess inventory (30% of SKUs).

**Assessment:**
- No formal S&OP process
- Sales and operations plans disconnected
- Forecast accuracy: 55%
- Supplier lead times: 8-12 weeks

**Solution:**
- Monthly S&OP cycle (demand review → supply review → executive meeting)
- Statistical forecasting with collaborative inputs
- Safety stock optimization by SKU velocity
- Supplier lead time reduction program

**Results:**
- Stockouts: 15% → 2%
- Excess inventory: 30% → 12% of SKUs
- Forecast accuracy: 55% → 78%
- Working capital reduction: $8M

---

### Scenario 4: Quality Management System Overhaul

**Context:** Medical device manufacturer facing FDA warning letter. Need QMS rebuild.

**Assessment:**
- Document control issues
- CAPA (Corrective Action) backlog: 120 items
- No risk management file integration
- Training records incomplete

**Solution:**
- ISO 13485-compliant QMS implementation
- Risk management per ISO 14971
- Electronic document control system
- Layered process audit program
- CAPA process redesign with escalation

**Results:**
- FDA warning letter closed in 6 months
- CAPA backlog cleared
- Audit findings: 45 → 3 per audit
- First pass yield: 92% → 98.5%

---

### Scenario 5: Service Operations Efficiency

**Context:** Customer service center with high attrition (45%), long handle times (12 min), and low CSAT (3.2/5).

**Assessment:**
- Agents searching for information 40% of time
- No standard troubleshooting process
- Training: 6 weeks but low knowledge retention
- High variability in handle times

**Solution:**
- Knowledge base redesign with decision trees
- Standard work for top 20 call types
- Reduced training to 3 weeks with simulation
- Real-time performance dashboard

**Results:**
- Handle time: 12 min → 7 min (-42%)
- First call resolution: 65% → 82%
- Agent attrition: 45% → 22%
- CSAT: 3.2 → 4.4 (+38%)

---
