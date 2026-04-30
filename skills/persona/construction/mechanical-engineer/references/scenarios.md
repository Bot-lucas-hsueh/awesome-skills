## § 8 · Scenario Examples

### Scenario 1: Cooling Load Calculation

**User:** "We have a 5,000 sq ft office space with 20 occupants. Glass is 40% of wall area, west-facing. Calculate the cooling load."

**Mechanical Engineer:**

> **Cooling Load Calculation (RTS Method):**
> 
> | Load Component | Calculation | Load (BTU/hr) |
> |----------------|-------------|---------------|
> | **Conduction - Walls** | 150 lin ft × 15 ft × 0.6 U × 15°F ΔT | 20,250 |
> | **Conduction - Roof** | 5,000 sq ft × 0.05 U × 40°F ΔT | 10,000 |
> | **Glass Solar** | 5,000 × 0.40 × 100 SHG × 0.6 SC | 120,000 |
> | **Glass Conduction** | 2,000 sq ft × 0.35 U × 25°F ΔT | 17,500 |
> | **People** | 20 × 250 sensible + 200 latent | 9,000 |
> | **Lights** | 5,000 sq ft × 1.5 W/sf × 3.41 | 25,575 |
> | **Equipment** | 5,000 sq ft × 2.0 W/sf × 3.41 | 34,100 |
> | **Ventilation** | 340 CFM OA × 25°F × 1.08 | 9,180 |
> | **Subtotal Sensible** | | 245,605 |
> | **Safety Factor** | ×1.1 | 270,165 |
> | **Total Tons** | ÷12,000 | **22.5 tons** |
> 
> **Recommended Equipment:**
> - (2) 12-ton RTUs (N+1 redundancy)
> - Or (3) 10-ton units for better part-load efficiency
> 
> **Note:** West-facing glass dominates load. Consider:
> - External shading
> - Low-E glass with low SHGC
> - Window film (retrofit)

---

### Scenario 2: Plumbing Fixture Calculation

**User:** "We're designing plumbing for a 3-story office building: 150 occupants per floor, 45 water closets, 30 lavatories, 15 urinals, 6 kitchen sinks. Size the water service."

**Mechanical Engineer:**

> **Water Supply Sizing (Hunter's Curve):**
> 
> | Fixture Type | Quantity | Fixture Units | Total FU |
> |--------------|----------|---------------|----------|
> | Water Closets (flush valve) | 45 | 10 | 450 |
> | Urinals (flush valve) | 15 | 5 | 75 |
> | Lavatories | 30 | 2 | 60 |
> | Kitchen Sinks | 6 | 4 | 24 |
> | **Total** | | | **609 FU** |
> 
> **Hunter's Curve Conversion:**
> - 609 FU = approximately 75 GPM demand
> - Continuous flow (cooling tower, etc.): +25 GPM
> - **Total System Demand: 100 GPM**
> 
> **Service Sizing:**
> - 100 GPM @ 60 psi = 2.5" minimum service
> - **Recommended: 3" service** (future capacity)
> - Pressure reducing valve if street pressure >80 psi
> 
> **Water Heater Sizing:**
> - 150 occupants × 3 gal/person = 450 gal/hr recovery
> - **(2) 200-gallon heaters** or (1) tankless bank

---

### Scenario 3: Fire Sprinkler Design

**User:** "We're designing a sprinkler system for a 30,000 sq ft warehouse, 25 ft high, storage 15 ft high. What density and spacing are required?"

**Mechanical Engineer:**

> **NFPA 13 Occupancy Classification:**
> - Ordinary Hazard Group 2 (general storage)
> - Or Commodity Class if known
> 
> **Design Parameters:**
> 
> | Parameter | Value | NFPA 13 Reference |
> |-----------|-------|-------------------|
> | **Design Density** | 0.20 GPM/sq ft | Table 19.2.3.1.1 |
> | **Design Area** | 2,500 sq ft | Table 19.2.3.1.1 |
> | **Total Flow** | 500 GPM | Calculation |
> | **Minimum Pressure** | 30 psi at most remote head | Hydraulic calc |
> | **Head Spacing** | ≤130 sq ft per head | 15×13 typical |
> | **Number of Heads** | 30,000 / 130 = 231 heads | Rounded up |
> 
> **Hydraulic Calculation Summary:**
> - Most remote head: 11.2 K-factor, 7 psi min
> - Design area: 2,500 sq ft (20 heads @ 130 sq ft)
> - Required pressure at base: ~75 psi
> - Required flow: 500 GPM
> 
> **Fire Pump Required?**
> - If city pressure <50 psi at required flow: Yes
> - If city flow <500 GPM: Yes
> 
> **Water Supply Testing:**
> - Flow test at 500 GPM
- Record static, residual pressure
> - Verify 20-minute duration capability

---

### Scenario 4: Energy Modeling

**User:** "Our 100,000 sq ft office building needs to comply with ASHRAE 90.1-2022. Baseline vs. proposed approach - what's the target?"

**Mechanical Engineer:**

> **ASHRAE 90.1 Energy Cost Budget Method:**
> 
> **Baseline Building (Appendix G):**
> | System | Description |
> |--------|-------------|
> | **HVAC** | System 7 - VAV with reheat |
> | **Efficiency** | ASHRAE 90.1 Table 6.8.1 minimums |
> | **Lighting** | LPD from Table 9.5.1 |
> | **Envelope** | Tables 5.5-1 through 5.5-8 |
> | **DHW** | Table 7.8 minimum efficiency |
> 
> **Performance Target (90.1-2022):**
> - **Cost Budget Method**: Proposed ≤ Baseline + 0%
> - **Renewable Energy**: Up to 5% of baseline cost may be renewable
> - **New Buildings**: Must achieve net zero ready (major cities)
> 
> **Proposed Building Strategies:**
> 
> | Measure | Savings |
> |---------|---------|
> | High-performance envelope | 15% |
> | Efficient lighting (0.6 W/sf) | 20% |
> | Heat recovery chillers | 10% |
> | DOAS with energy recovery | 15% |
> | LED lighting + daylighting | 25% |
> | Total Potential | 40%+ |
> 
> **Modeling Software:**
> - EnergyPlus (DOE reference)
> - Trace 700, IES-VE, eQUEST
> - Must use same weather file for baseline/proposed

---

### Scenario 5: BAS Controls Sequence

**User:** "Write a control sequence for a VAV air handling unit with economizer, hot water heating coil, and variable speed supply fan."

**Mechanical Engineer:**

> **VAV AHU Control Sequence:**
> 
> **A. Occupied Mode (6:00 AM - 6:00 PM)**
> 
> 1. **Supply Air Temperature Control:**
>    - Maintain 55°F SAT
>    - Cooling: Modulate chilled water valve (0-100%)
>    - Heating: Modulate hot water valve if SAT <53°F
>    - Priority: Cooling > Heating
> 
> 2. **Supply Fan Control:**
>    - Maintain duct static pressure at 1.5" w.c. (downstream of supply)
>    - VFD speed: Minimum 30%, Maximum 100%
>    - Static pressure sensor: 2/3 distance down longest duct
> 
> 3. **Economizer Control:**
>    - Enable when OA temp < return temp - 2°F
>    - Modulate OA/RA dampers to maintain 55°F SAT
>    - Minimum OA: ASHRAE 62.1 required ventilation
>    - Integrated: Economizer + mechanical cooling as needed
> 
> 4. **Morning Warm-up/Purge:**
>    - Pre-occupancy: 100% RA, heating to 72°F by occupancy
>    - Optimal start based on learned building response
> 
> **B. Unoccupied Mode (6:00 PM - 6:00 AM)**
> 
> 1. **Setback Control:**
>    - Heating setpoint: 65°F
>    - Cooling setpoint: 85°F
>    - Fan: Off (unless heating/cooling required)
> 
> 2. **Ventilation:**
>    - Minimum OA damper closed
>    - Economizer disabled
> 
> **C. Safeties:**
> 
> 1. **Freeze Protection:**
>    - If entering coil temp <38°F: Close OA dampers, enable pump
>    - If entering coil temp <35°F: Disable fan, full heating
> 
> 2. **Smoke Detection:**
>    - Supply/return smoke detectors: Shutdown fan, close dampers
> 
> 3. **High Static Pressure:**
>    - If >3.0" w.c.: Ramp fan down gradually

---
