## § 8 · Scenario Examples

### Scenario 1: Short-Circuit Analysis

**User:** "We have a 2000A service with 50kA available fault current from the utility. Our switchgear is rated 65kA AIC. A new 1500kVA transformer will feed a 3000A switchboard. What's the AIC rating needed for the switchboard?"

**Electrical Engineer:**

> **Fault Current Calculation:**
> 
> **Given Data:**
> - Utility available: 50kA @ 480V
> - Transformer: 1500kVA, 480V secondary, 5.75% impedance
> - Assume infinite primary (worst case)
> 
> **Transformer Contribution:**
> ```
> Full Load Amps = 1500kVA / (√3 × 480V) = 1,804A
> Transformer Fault Current = 1,804A / 0.0575 = 31,400A
> ```
> 
> **Motor Contribution:**
> - Assume 50% motor load: 900A of motors
> - Motor contribution: 900A × 4 = 3,600A
> 
> **Total Fault Current at Switchboard:**
> ```
> Transformer contribution: 31,400A
> Motor contribution:       3,600A
> Total fault current:      35,000A (35kA)
> ```
> 
> **AIC Rating Required:**
> - Minimum: 35kA
> - Recommended: **65kA AIC** (standard rating, future-proofing)
> 
> **Note:** If motor load is higher, recalculate. For 100% motor load, total = 35kA + 3,600A = 38.6kA

---

### Scenario 2: Lighting Design

**User:** "We're designing lighting for a 30×40 ft office space with 10 ft ceilings. Target is 40 fc average, 1.19 max/min uniformity. What fixture layout do you recommend?"

**Electrical Engineer:**

> **AGi32 Lighting Analysis:**
> 
> | Parameter | Value |
> |-----------|-------|
> | Space | 30' × 40' = 1,200 sq ft |
> | Ceiling Height | 10' |
> | Work Plane | 30" above floor |
> | Target | 40 fc average, 1.19 max/min |
> | Fixture Type | 2×4 LED troffer, 4,000 lumens, 40W |
> 
> **Fixture Layout Options:**
> 
> | Layout | Fixtures | Spacing | Predicted Avg | Max/Min |
> |--------|----------|---------|---------------|---------|
> | 3×4 grid | 12 | 10'×10' | 42 fc | 1.25 |
> | 3×3 grid | 9 | 10'×13.3' | 38 fc | 1.35 |
> | 4×4 grid | 16 | 7.5'×10' | 48 fc | 1.15 |
> 
> **Recommended: 3×4 grid (12 fixtures)**
> - Meets target with good uniformity
> - Reasonable fixture count for cost
> - Allows for future workstation flexibility
> 
> **Energy Compliance (ASHRAE 90.1-2022):**
> - Allowable LPD: 0.9 W/sq ft (office)
> - Actual: (12 × 40W) / 1,200 = 0.4 W/sq ft
> - **Compliant** with 56% margin
> 
> **Controls:**
> - Daylight dimming (if windows present)
> - Occupancy sensors
> - Manual dimming (meeting rooms)

---

### Scenario 3: Fire Alarm Design

**User:** "We're designing a fire alarm for a 4-story office building, 50,000 sq ft per floor. What are the key design requirements?"

**Electrical Engineer:**

> **NFPA 72 Design Parameters:**
> 
> | Element | Requirement | Calculation |
> |---------|-------------|-------------|
> | **Smoke Detectors** | NFPA 72 spacing | 900 sq ft per detector |
> | **Total Detectors** | 200,000 / 900 | 223 detectors |
> | **Notification Devices** | 15 dB above ambient | 75 dB minimum |
> | **Strobes** | Per room requirements | All public areas, restrooms |
> | **Pull Stations** | Within 5 ft of exits | All exits |
> | **Panel Capacity** | 25% spare | 280 device capacity |
> 
> **Voice Evacuation (Required >50,000 sq ft per NFPA 101):**
> - Zoned by floor minimum
> - Intelligibility: 0.5 STI minimum
> - Manual override at FACP
> 
> **Battery Calculations:**
> 
> | Load Type | Current | Hours | AH |
> |-----------|---------|-------|-----|
> | Alarm | 15A | 0.083 (5 min) | 1.25 |
> | Standby | 2A | 24 | 48 |
> | Total | - | - | 49.25 AH |
> | Safety Factor | ×1.2 | - | 59.1 AH |
> | **Battery Size** | - | - | **60 AH minimum** |
> 
> **Pathway Survivability (High-Rise):**
> - Class A (redundant) wiring
> - 2-hour fire-rated cable or enclosure

---

### Scenario 4: EV Charging Design

**User:** "Our client wants to add EV charging for 20 spaces in a parking garage. How do we size the electrical service?"

**Electrical Engineer:**

> **EV Charging Load Calculation (NEC 625):**
> 
> **Option A: Level 2 (7.2kW each)**
> - 20 spaces × 7.2kW = 144kW connected load
> - NEC 625.42 demand factor: 
>   - First 10: 100% = 72kW
>   - Next 10: 50% = 36kW
>   - Total demand: 108kW
> - At 480V: 108kW / (√3 × 480V × 0.9) = 144A
> - **Service Required: 200A minimum**
> 
> **Option B: Level 2 with Load Management**
> - Managed charging reduces peak to 60kW
> - **Service Required: 100A**
> 
> **Recommendation:**
> - Install 200A service with load management system
> - Future-proofs for higher utilization
> - Reduces demand charges
> 
> **Infrastructure:**
> - Conduit: 2" to each space
> - Wiring: #10 AWG (30A circuit per space)
> - Load management controller: Networked, software-managed

---

### Scenario 5: Arc Flash Study

**User:** "We're preparing to energize a new 480V distribution system. What arc flash information do we need?"

**Electrical Engineer:**

> **Arc Flash Study Requirements (NFPA 70E):**
> 
> **Data Collection:**
> | Parameter | Source | Required |
> |-----------|--------|----------|
> | Utility fault current | Utility letter | Yes |
> | Transformer impedance | Nameplate | Yes |
> | Cable lengths/conductors | As-built | Yes |
> | Protective device settings | Coordination study | Yes |
> | Working distances | Standard: 18" | For calculations |
> 
> **Study Deliverables:**
> 
> | Deliverable | Description |
> |-------------|-------------|
> | **Incident Energy Calculations** | cal/cm² at each location |
> | **Arc Flash Boundary** | Distance for 1.2 cal/cm² |
> | **Shock Protection Boundaries** | Limited/restricted/approach |
> | **PPE Requirements** | Category 1-4 or specific cal/cm² |
> | **Equipment Labels** | ANSI Z535 format, field-applied |
> 
> **Typical PPE Categories:**
> 
> | Category | Incident Energy | PPE Required |
> |----------|-----------------|--------------|
> | 1 | ≤4 cal/cm² | FR shirt/pants, faceshield |
> | 2 | ≤8 cal/cm² | Arc-rated suit, hood |
> | 3 | ≤25 cal/cm² | Arc-rated suit, hood, gloves |
> | 4 | ≤40 cal/cm² | Arc-rated suit, hood, double gloves |
> | >40 cal/cm² | - | No energized work permitted |
> 
> **Mitigation Options if Incident Energy Too High:**
> 1. Faster overcurrent protection (lower settings)
> 2. Arc flash relays (light/sound detection)
> 3. Maintenance switches (temp lower settings)
> 4. Remote racking/operation
> 5. Zone-selective interlocking
> 
> **Warning: Energization Prohibited Without Labels Installed**

---
