# 4680 Battery Deep Dive

## Overview

The 4680 battery cell (46mm diameter × 80mm height) represents Tesla's revolutionary approach to battery design, announced at Battery Day 2020. The name refers to its dimensions: **46**mm diameter × **80**mm height × **0** (cylindrical format).

## Specifications Comparison

| Specification | 18650 (Legacy) | 2170 (Model 3/Y) | 4680 (Tesla) |
|--------------|----------------|------------------|--------------|
| **Dimensions** | 18mm × 65mm | 21mm × 70mm | 46mm × 80mm |
| **Volume** | 16.5 cm³ | 24.2 cm³ | 132.7 cm³ |
| **Volume Ratio** | 1× | 1.5× | 8× |
| **Energy Capacity** | ~12 Wh | ~18 Wh | ~98 Wh |
| **Energy Ratio** | 1× | 1.5× | 8× |
| **Cells per 75kWh Pack** | 6,250 | 4,416 | 828 |
| **Power Output** | Baseline | Baseline | 6× improvement |
| **Internal Resistance** | Higher | Medium | Lower (tabless) |

## Key Innovations

### 1. Tabless Electrode Design

**Traditional Cell:**
- Current flows from active material → tab → collector
- Long path = higher resistance, heat generation
- Limited power output

**4680 Tabless Design:**
```
Current path:
Active material → Multiple connection points → Collector
                    ↓
            ("Flower" pattern - current collectors 
             distributed across entire base)
```

**Benefits:**
- 5× reduction in electrical path length
- Lower internal resistance → less heat
- Higher power output (6× improvement)
- Faster charging capability
- Better thermal distribution

### 2. Dry Electrode Process

**Wet Process (Traditional):**
```
Mix materials → Add solvent → Coat foil → 
Dry (12-24 hours, massive ovens) → Compress → Cut
```
- Energy intensive: Drying ovens consume 30-50% of factory energy
- Large factory footprint (long ovens)
- Toxic solvent handling (NMP)
- Environmental concerns

**Dry Process (Tesla/Maxwell):**
```
Mix dry powder → Press into film → 
Bond to foil (minutes, not hours) → Cut
```

**Breakthrough Achievement (Q4 2025):**
- Both anode AND cathode now using dry process
- 7-10× faster production speed
- 30%+ energy reduction
- 15% smaller factory footprint
- No toxic solvents
- Major cost reduction pathway

**Timeline:**
- 2019: Acquired Maxwell Technologies for dry electrode tech
- 2020-2024: Dry anode production; struggling with dry cathode
- Q4 2025: **Full dry electrode production achieved** (both electrodes)

### 3. Structural Battery Pack

**Traditional Architecture:**
```
Cells → Modules (with wiring, cooling) → 
Pack (structural enclosure) → 
Vehicle (pack bolted to chassis)
```
- Parts: ~1,700
- Weight: ~480 kg
- Multiple assembly steps
- Redundant structural elements

**Tesla Structural Pack:**
```
Cells → Structural Pack (IS the vehicle floor)
```
- Parts: ~370
- Weight: ~420 kg
- Fewer assembly steps
- Pack = structural element

**Benefits:**
- 78% parts reduction (1,700 → 370)
- 12% weight reduction
- Increased vehicle stiffness
- Simplified manufacturing
- Better crash performance

## Chemistry Evolution

### Generation 1 (2020-2023)
- NCM 811 cathode (Nickel 80%, Cobalt 10%, Manganese 10%)
- Silicon-carbon anode
- Target: 300 Wh/kg at cell level

### Generation 2 / "Cybercell" (2023-2025)
- High-nickel NCM (up to 90% nickel)
- Increased silicon content anode
- Energy density: 290-300 Wh/kg
- Powers Cybertruck

### Future Chemistries (2025+)
- NC05: Dry electrode optimized chemistry
- NC30: Higher energy density variant
- Solid-state pathway exploration

## Manufacturing Status (2025)

### Production Capacity

| Facility | Status | Output (2025) | Target |
|----------|--------|---------------|--------|
| Gigafactory Texas | Production | 15-20 GWh/year | 100 GWh |
| Gigafactory Nevada | Expansion | Pilot production | 100 GWh expansion |
| Panasonic Nevada | Production | N/A | 4680 supply |
| LG Arizona | Building | 2026 start | Mass production |

### Production Milestones

| Date | Milestone |
|------|-----------|
| 2020 | Kato Road pilot line announced |
| 2022 | First 4680 Model Y delivered (Texas) |
| 2023 | 10M cells produced |
| 2024 | 100M+ cells produced |
| 2025 | 150M+ cells, dry electrode breakthrough |

### Vehicle Applications

| Vehicle | Cell Type | Pack Size | Range |
|---------|-----------|-----------|-------|
| Model Y (Texas) | 4680 Gen 1 | 67-82 kWh | 279-330 mi |
| Cybertruck | 4680 Gen 2 | 123 kWh | 340+ mi |
| Semi | 4680 | 500+ kWh | 500 mi |
| Future affordable model | 4680 | TBD | TBD |

## Cost Analysis

### Cost Floor Model (per kWh)

| Component | 2170 | 4680 (Wet) | 4680 (Dry) |
|-----------|------|------------|------------|
| Cathode materials | $55 | $45 | $40 |
| Anode materials | $8 | $6 | $5 |
| Electrolyte | $5 | $4 | $3 |
| Separator | $3 | $2 | $2 |
| Can/cap | $8 | $4 | $3 |
| Manufacturing | $35 | $20 | $12 |
| Cell subtotal | $114 | $81 | $65 |
| Pack integration | $26 | $19 | $15 |
| **TOTAL** | **$140** | **$100** | **$80** |

**Target by 2027-2028: <$50/kWh at pack level**

## Technical Challenges Overcome

### 1. Yield Rate
- **Challenge:** Early production had <50% yield
- **Solution:** Process optimization, quality control
- **Status:** >95% yield achieved (2025)

### 2. Dry Cathode
- **Challenge:** Cathode materials harder to process dry
- **Solution:** Years of R&D, equipment development
- **Status:** Achieved Q4 2025

### 3. Thermal Management
- **Challenge:** Large cells generate more heat
- **Solution:** Tabless design, improved thermal pathways
- **Status:** Production validated

### 4. Manufacturing Speed
- **Challenge:** Slower production than 2170
- **Solution:** Dry electrode (7-10× faster)
- **Status:** Scaling up

## Competitive Landscape

### Tesla Advantages
1. Vertical integration (cell → pack → vehicle)
2. Structural pack design
3. Dry electrode technology
4. Fleet learning and data
5. Manufacturing at scale

### Competitors Developing 46mm Cells

| Company | Status | Target Customers |
|---------|--------|------------------|
| Panasonic | Production | Tesla, others |
| LG Energy Solution | 2026 start | Tesla, BMW |
| Samsung SDI | Development | BMW |
| CATL | Testing | Various |
| BYD | Development | Internal |

## Future Roadmap

### 2025-2026
- Scale dry electrode production
- 200M+ cells annual production
- Expand to all vehicle lines
- Cost reduction to $80/kWh

### 2026-2028
- 1 TWh+ total capacity across suppliers
- <$50/kWh cost target
- Next-generation chemistry (NC05, NC30)
- Solid-state development

### 2028+
- Potential solid-state transition
- Fully automated production
- Integration with Optimus robotics
- Terawatt-hour scale manufacturing

---

*Last Updated: March 2026*
*Sources: Tesla Battery Day 2020, Earnings calls, Technical disclosures*
