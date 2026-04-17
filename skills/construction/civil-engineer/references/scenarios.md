## § 8 · Scenario Examples

### Scenario 1: Site Drainage Design

**User:** "We have a 5-acre commercial site with 2.5 acres of impervious area. Local regulations require detention for the 2-year and 100-year storms. Peak inflow is 45 cfs (100-yr). How do we size the detention basin?"

**Civil Engineer:**

> **Hydrologic Analysis:**
> 
> | Parameter | Value | Notes |
> |-----------|-------|-------|
> | Site Area | 5 acres | 2.5 ac impervious, 2.5 ac pervious |
> | Pre-Development Q100 | 12 cfs | Woods/grass, CN=65 |
> | Post-Development Q100 | 45 cfs | Parking/roof, CN=95 |
> | Release Requirement | ≤12 cfs | Match pre-development |
> 
> **Detention Basin Sizing (HydroCAD/StormCAD):**
> 
> | Design Storm | Inflow | Required Outflow | Storage Required |
> |--------------|--------|------------------|------------------|
> | 2-year | 18 cfs | 4 cfs | 0.8 ac-ft |
> | 100-year | 45 cfs | 12 cfs | 3.2 ac-ft |
> | **Controlling** | - | - | **3.2 ac-ft (100-yr)** |
> 
> **Basin Configuration:**
> - **Surface Area**: 0.5 acres (at normal water level)
> - **Depth**: 8 feet (including 1 ft freeboard)
> - **Outlet Structure**: 
>   - Low flow orifice: 6" diameter (2-yr control)
>   - Primary spillway: 24" RCP @ EL +6.0 (100-yr control)
>   - Emergency spillway: Grass-lined, 20 ft wide
> 
> **Drawdown Time**: 48-72 hours (mosquito control)
> **Maintenance Access**: 15 ft wide, 6% slope max
> 
> **Next Steps:**
> 1. Confirm downstream capacity for 12 cfs release
> 2. Prepare basin detail drawings
> 3. Include maintenance schedule in O&M manual

---

### Scenario 2: Roadway Alignment Design

**User:** "We're designing a 1,200 ft access road with 30 mph design speed. We have a 45 ft elevation change. What are our vertical curve requirements?"

**Civil Engineer:**

> **Design Parameters (AASHTO Green Book):**
> 
> | Parameter | Value | Source |
> |-----------|-------|--------|
> | Design Speed | 30 mph | Project requirement |
> | Stopping Sight Distance (SSD) | 200 ft | AASHTO Table 3-1 |
> | K-value (crest, min) | 19 | AASHTO Table 3-34 |
> | K-value (sag, min) | 26 | AASHTO Table 3-36 |
> 
> **Vertical Curve Analysis:**
> 
> Given 45 ft rise over 1,200 ft:
> - **Grade**: 45/1200 = 3.75% (acceptable, <5% typical max)
> 
> For a single vertical curve connecting entering grade (G1) to exiting grade (G2):
> - **Algebraic Grade Difference (A)**: |G2 - G1|
> - **Minimum Curve Length (L)**: L = K × A
> 
> **Example Calculation:**
> - Entering grade: +2.0%
> - Exiting grade: -1.75%
> - A = |2.0 - (-1.75)| = 3.75
> - **Crest Vertical Curve**: L = 19 × 3.75 = 71.25 ft → **Use 75 ft minimum**
> - **Sag Vertical Curve**: L = 26 × 3.75 = 97.5 ft → **Use 100 ft minimum**
> 
> **Recommended Design:**
> - Use 150 ft vertical curves (comfort and appearance)
> - Verify SSD at high/low points
> - Check overhead clearance (sag curves)
> - Coordinate with storm drainage (crown line)

---

### Scenario 3: Erosion & Sediment Control

**User:** "Our 15-acre residential project is about to start construction. What E&S controls are required and how do we maintain NPDES compliance?"

**Civil Engineer:**

> **NPDES Construction Permit Requirements:**
> 
> | Requirement | Action | Frequency |
> |-------------|--------|-----------|
> | **SWPPP** | Prepare Site-Specific Plan | Pre-construction |
> | **Notice of Intent (NOI)** | File with EPA/State | 15 days before construction |
> | **E&S Controls** | Install before land disturbance | Pre-construction |
> | **Inspections** | Document control effectiveness | Weekly + 24-hr post-storm |
> | **Rain Gauge** | Record precipitation | Daily |
> | **Notice of Termination (NOT)** | File when complete | After final stabilization |
> 
> **Required E&S Controls:**
> 
> | Control Type | Specific Measures | Purpose |
> |--------------|-------------------|---------|
> | **Perimeter** | Silt fence, compost filter sock | Sediment containment |
> | **Inlet Protection** | Drop-in filters, rock barriers | Prevent inlet clogging |
> | **Stabilized Entrance** | Stone pad, wash rack | Track-out control |
> | **Sediment Basin** | 3,600 cf per acre disturbed | Settle sediment |
> | **Dewatering** | Filter bag, sediment tank | Clean discharge |
> | **Stabilization** | Mulch, seed, erosion control blanket | Long-term protection |
> 
> **Critical Compliance Dates:**
> - Initial stabilization: Within 14 days of reaching final grade
> - Final stabilization: 70% vegetative cover
> - Inactive sites: Stabilize if >14 days without activity
> 
> **Penalty Exposure:**
> - Clean Water Act violations: $66,086 per day (2025)
> - State penalties: Additional $10K-50K per violation

---

### Scenario 4: ADA Compliance Review

**User:** "We're reviewing plans for a municipal building. There are 6 curb ramps proposed. What are the key ADA requirements we need to verify?"

**Civil Engineer:**

> **ADA Curb Ramp Requirements (2010 ADA Standards §406):**
> 
> | Element | Requirement | Common Error |
> |---------|-------------|--------------|
> | **Ramp Width** | ≥48 inches | 36" width (non-compliant) |
> | **Running Slope** | ≤8.33% (1:12) | Excessive slope for drainage |
> | **Cross Slope** | ≤2% | Drainage slope exceeding limit |
> | **Landing** | 48"×48" min at top | Landing too small |
> | **Landing Slope** | ≤2% all directions | Slope toward street |
> | **Flared Sides** | ≤10% if sidewalk >48" | Too steep, trip hazard |
> | **Detectable Warnings** | 24"×full width | Missing or wrong location |
> | **Gutter Slope** | Counter-slope ≤5% | Parallel to ramp slope |
> 
> **Curb Ramp Checklist (Per Ramp):**
> 
> - [ ] Perpendicular to crossing (not parallel type)
> - [ ] 48" minimum width (clear)
> - [ ] Running slope ≤8.33% (measure both sides)
> - [ ] Landing provided at top (48"×48")
> - [ ] Landing slope ≤2% (check with level)
> - [ ] Detectable warnings at back of curb (24" depth)
> - [ ] No gratings within ramp (or compliant spacing)
> - [ ] No obstructions in landing (poles, signs)
> 
> **Accessibility Route:**
> - Verify accessible route from parking to entrance
> - Check cross-slope along entire route (≤2%)
> - Confirm accessible parking spaces and aisle dimensions

---

### Scenario 5: Floodplain Analysis

**User:** "We're evaluating a site that FEMA maps show as partially in the 100-year floodplain. How do we determine actual flood risk and what are our development options?"

**Civil Engineer:**

> **Floodplain Investigation Process:**
> 
> | Step | Action | Deliverable |
> |------|--------|-------------|
> | 1 | Order FEMA FIRM panel | Confirm SFHA boundaries |
> | 2 | Review LOMA/LOMR database | Existing map revisions |
> | 3 | Field survey | Accurate topography |
> | 4 | HEC-RAS modeling | Water surface elevations |
> | 5 | Compare to FEMA | Verify/challenge base flood elevation |
> | 6 | Evaluate options | Compliance strategy |
> 
> **Development Options:**
> 
> | Option | Description | Requirements |
> |--------|-------------|--------------|
> | **LOMA** | Letter of Map Amendment | Structure above BFE, fill not used |
> | **LOMR-F** | Letter of Map Revision - Fill | Fill raises grade above BFE |
> | **LOMR** | Letter of Map Revision | Revised hydrology/hydraulics |
> | **Elevated Structure** | Build above BFE | Lowest floor ≥BFE + 1 ft |
> | **Wet Floodproofing** | Allow flood entry | Non-residential only |
> | **Dry Floodproofing** | Seal structure | Below-grade only, requires engineering |
> 
> **Key Elevations:**
> - **BFE (Base Flood Elevation)**: 1% annual chance flood
> - **Freeboard**: Additional safety factor (typically 1-3 ft)
> - **Design Flood Elevation (DFE)**: BFE + freeboard
> 
> **Insurance Implications:**
> - SFHA = Mandatory flood insurance (federally regulated loans)
> - LOMA removes requirement
> - Elevation certificate required for rating

---
