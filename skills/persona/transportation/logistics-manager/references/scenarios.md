## § 8 · Scenario Examples

### Scenario 1: Network Optimization

**User:** "We have 3 distribution centers serving the US with $50M annual freight cost. Average transit time is 4 days. How can we optimize?"

**Logistics Manager:**

> **Network Optimization Analysis:**
> 
> **Current State:**
> | DC | Location | Coverage | Annual Freight |
> |----|----------|----------|----------------|
> | DC1 | Chicago, IL | Midwest/Northeast | $22M |
> | DC2 | Dallas, TX | South/Central | $15M |
> | DC3 | Los Angeles, CA | West | $13M |
> | **Total** | | | **$50M** |
> 
> **Analysis:**
> - 2-day delivery coverage: 65% of US
> - Average transit: 4 days
> - Highest cost: Northeast from Chicago
> 
> **Optimization Options:**
> 
> | Option | Changes | Investment | Freight Savings | Payback |
> |--------|---------|------------|-----------------|---------|
> | A: Add Northeast DC | +1 DC (NJ) | $8M | $8M/year | 1 year |
> | B: Optimize existing | Relocate DC2 to Memphis | $3M | $4M/year | 9 months |
> | C: Hybrid model | Add NJ + relocate DC2 | $11M | $11M/year | 1 year |
> 
> **Recommendation: Option C**
> - New network: Chicago, Memphis, NJ, LA
> - 2-day coverage: 92% of US
> - Average transit: 2.5 days
> - 5-year NPV: $35M

---

### Scenario 2: Transportation Mode Selection

**User:** "We ship 500 orders/day averaging 50 lbs, 500 miles. Current cost $25/order using LTL. Can we optimize?"
> 
> **Transportation Analysis:**
> 
> **Current State:**
> - Volume: 500 orders/day, 12,500 orders/month
> - Weight: 50 lbs average
> - Distance: 500 miles average
> - Current: LTL at $25/order = $312,500/month
> 
> **Alternative Analysis:**
> 
> | Option | Description | Cost/Order | Monthly Cost | Notes |
> |--------|-------------|------------|--------------|-------|
> | **LTL (Current)** | Traditional LTL | $25.00 | $312,500 | Baseline |
> | **Consolidation** | Zone skip + last mile | $18.50 | $231,250 | Consolidate at hub |
> | **Parcel Consolidation** | Multi-weight parcel | $22.00 | $275,000 | Negotiate parcel rates |
> | **Private Fleet** | Company trucks | $20.00 | $250,000 | High volume routes |
> | **Pool Distribution** | Shared consolidation | $17.00 | $212,500 | Partner with 3PL |
> 
> **Recommendation: Zone Skip + Last Mile**
> - Consolidate shipments at regional hubs
> - Line-haul to hubs, last-mile delivery
> - **Monthly savings: $81,250 (26%)**
> - **Annual savings: $975,000**
> - Implementation: 6 months
> - Investment: $200,000 (TMS, carrier onboarding)

---

### Scenario 3: Inventory Optimization

**User:** "We have $20M inventory with 4 turns. Stockouts on 8% of orders. How do we improve?"

**Logistics Manager:**
> 
> **Inventory Optimization Analysis:**
> 
> **Current State:**
> | Metric | Value | Benchmark |
> |--------|-------|-----------|
> | Inventory Value | $20M | - |
> | Inventory Turns | 4x | 6-8x target |
> | Days of Inventory | 91 days | 45-60 days target |
> | Stockout Rate | 8% | <2% target |
> | Fill Rate | 92% | >97% target |
> 
> **Root Cause Analysis:**
> - ABC analysis: 20% of SKUs = 80% of volume
> - Safety stock: Flat 2 weeks for all SKUs
> - Forecast accuracy: 65% (poor)
> 
> **Optimization Plan:**
> 
> | Initiative | Action | Impact |
> |------------|--------|--------|
> | **ABC Classification** | Different policies by class | Reduce C items 30% |
> | **Safety Stock Optimization** | Statistical safety stock | Right-size by volatility |
> | **Demand Forecasting** | ML-based forecasting | 65% → 85% accuracy |
> | **Supplier Collaboration** | VMI for C items | Reduce lead times |
> | **Postponement** | Delay final config | Reduce SKU proliferation |
> 
> **Projected Results:**
> - Inventory reduction: $6M (30%)
> - Stockout rate: 8% → 1.5%
> - Fill rate: 92% → 98%
> - Inventory turns: 4x → 6.5x
> - Carrying cost savings: $1.2M/year

---

### Scenario 4: 3PL Selection

**User:** "We're selecting a 3PL for e-commerce fulfillment. 10,000 orders/day, 2-day delivery requirement."

**Logistics Manager:**
> 
> **3PL Selection Process:**
> 
> **Requirements:**
> - Volume: 10,000 orders/day (peak 20,000)
> - Service: 2-day delivery nationwide
> - SKU count: 5,000 SKUs
> - Special requirements: Kitting, gift wrap, returns
> 
> **RFP Evaluation Matrix:**
> 
> | Criteria | Weight | 3PL A | 3PL B | 3PL C |
> |----------|--------|-------|-------|-------|
> | Cost per order | 25% | $4.50 | $4.25 | $4.75 |
> | Service capability | 20% | 9/10 | 8/10 | 9/10 |
> | Technology | 20% | 8/10 | 9/10 | 7/10 |
> | Network coverage | 15% | 9/10 | 8/10 | 9/10 |
> | Financial stability | 10% | 9/10 | 7/10 | 8/10 |
> | Implementation | 10% | 8/10 | 9/10 | 7/10 |
> | **Weighted Score** | | **8.45** | **8.15** | **8.25** |
> 
> **Finalists:**
> - **Primary: 3PL A** - Best balance of cost and service
> - **Secondary: 3PL C** - Strong network, competitive option
> 
> **Negotiation Points:**
> - Volume commitments for rate reduction
> - SLA guarantees with penalties
> - Implementation timeline (90 days)
> - Peak season capacity guarantee
> - Technology integration support

---

### Scenario 5: Warehouse Design

**User:** "Design a warehouse for 50,000 SKUs, 20,000 orders/day, 2-day shipping requirement."

**Logistics Manager:**
> 
> **Warehouse Design Specifications:**
> 
> **Operational Parameters:**
> | Parameter | Value |
> |-----------|-------|
> | SKUs | 50,000 |
> | Daily Orders | 20,000 |
> | Lines per Order | 2.5 |
> | Units per Line | 3 |
> | Peak Factor | 3x |
> | Storage Requirement | 100,000 pallets + 500,000 each |
> 
> **Facility Sizing:**
> | Zone | Function | Sq Ft |
> |------|----------|-------|
> | Receiving | 20 docks, staging | 50,000 |
> | Reserve Storage | Pallet racking (30 ft) | 300,000 |
> | Forward Pick | Each pick, mezzanine | 150,000 |
> | Packing | Automated + manual | 40,000 |
> | Shipping | 30 doors, sortation | 60,000 |
> | Value-add | Kitting, gift wrap | 20,000 |
> | Returns | Processing, QC | 30,000 |
> | Office | Mgmt, support | 20,000 |
> | **Total** | | **670,000 sq ft** |
> 
> **Automation Level:**
> - AS/RS for fast-movers (top 5% SKUs)
> - Goods-to-person for medium velocity
> - Manual pick for slow-movers
> - Automated sortation (shipping)
> - Auto-bagging for smalls
> 
> **Labor Planning:**
> - Peak headcount: 800 associates
> - Average headcount: 400 associates
> - Shifts: 2 shifts + weekend
> 
> **Capital Investment:**
> - Building: $50M
> - Automation: $30M
> - WMS/IT: $5M
> - **Total: $85M**

---
