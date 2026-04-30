# MEB Platform Technical Specifications

**Full Name:** Modular Electric Drive Matrix (Modularer E-Antriebs-Baukasten)  
**Launch:** 2019 (VW ID.3)  
**Investment:** ~€7 billion development cost

---

## Architecture Overview

The MEB is Volkswagen Group's dedicated battery electric vehicle platform designed for high-volume production across multiple brands and vehicle segments.

### Design Philosophy
- **Skateboard Architecture:** Battery pack integrated into floorpan
- **Rear-Wheel Drive Standard:** Optimizes packaging and handling
- **Scalability:** Single platform for compact cars to large SUVs
- **Cost Optimization:** 40%+ component sharing across brand variants

---

## Technical Specifications

### Dimensions
| Parameter | Range |
|-----------|-------|
| Wheelbase | 2,700 - 3,000 mm |
| Length | 4,100 - 5,200 mm |
| Width | 1,800 - 2,000 mm |
| Height | 1,500 - 1,800 mm |
| Ground Clearance | 150 - 220 mm |

### Battery Options
| Variant | Capacity (Net/Gross) | Chemistry | Application |
|---------|---------------------|-----------|-------------|
| Standard | 45 kWh / 48 kWh | LFP | Entry models (ID.3 Pure) |
| Medium | 58 kWh / 62 kWh | NMC 622 | Volume models (ID.3 Pro) |
| Large | 77 kWh / 82 kWh | NMC 712 | Long-range (ID.4/ID.5) |
| Max | 91 kWh / 96 kWh | NMC 811 | ID. Buzz, premium variants |

### Electric Motors

**APP 310 Rear-Mounted Motor:**
- Type: Permanent magnet synchronous motor (PMSM)
- Power: 150 kW (204 PS)
- Torque: 310 Nm
- Efficiency: ~93%

**APP 550 Updated Motor (2023+):**
- Power: 210 kW (286 PS)
- Torque: 545 Nm
- Improved efficiency and thermal management

**Dual-Motor AWD (4Motion):**
- Front motor: 80 kW asynchronous
- Combined power: Up to 250 kW (340 PS)
- Combined torque: Up to 460 Nm

### Performance Specifications
| Metric | Entry | Mid | Performance |
|--------|-------|-----|-------------|
| 0-100 km/h | 9.0s | 7.5s | 5.4s |
| Top Speed | 160 km/h | 160 km/h | 180 km/h |
| Range (WLTP) | 330 km | 420 km | 520 km |

### Charging Capabilities

**AC Charging:**
- Onboard charger: 11 kW (standard) / 22 kW (optional)
- Connector: Type 2

**DC Fast Charging:**
- Peak power: 135 kW (standard MEB) / 200 kW (MEB+ update)
- Architecture: 400V system
- 10-80% time: ~30 minutes (depending on battery)
- Connector: CCS2 (Europe) / CCS1 (North America)

---

## Platform Variants

### MEB (Original)
- Launch: 2019
- Vehicles: ID.3, ID.4, ID.5, Enyaq, Q4 e-tron
- E³ Architecture: 1.1 (initial), 1.2 (update)

### MEB+ (2024+)
- Enhanced battery chemistry
- 200 kW charging capability
- Improved software architecture
- New motor generations

### MEB-Small (Announced)
- For entry segment (A-segment)
- Target price: €20,000
- Partnership: VW-Rivian collaboration

---

## Production Network

| Plant | Location | Annual Capacity | Models |
|-------|----------|-----------------|--------|
| Zwickau | Germany | 330,000 | ID.3, ID.4, ID.5, Cupra Born |
| Dresden | Germany | 30,000 | ID.3 (premium) |
| Emden | Germany | 300,000 | ID.4, ID.7 |
| Hanover | Germany | 130,000 | ID. Buzz |
| Mlada Boleslav | Czech Republic | 350,000 | Enyaq, Elroq |
| Anting | China | 300,000 | ID.4, ID.6, ID.3 |
| Foshan | China | 300,000 | ID.4, Audi Q4 e-tron |
| Chattanooga | USA | 150,000 | ID.4 (US market) |

---

## Brand Applications

### Volkswagen
- ID.3 (Compact hatchback)
- ID.4 (Compact SUV)
- ID.5 (Coupé SUV)
- ID.7 (Executive sedan/tourer)
- ID. Buzz (Van/Microbus)

### Audi
- Q4 e-tron (Compact SUV)
- Q4 Sportback e-tron

### Škoda
- Enyaq iV (Family SUV)
- Enyaq Coupé iV
- Elroq (Compact SUV, upcoming)

### CUPRA
- Born (Performance hatchback)
- Tavascan (Performance SUV, upcoming)

---

## Software Architecture (E³)

### E³ 1.1 (Initial)
- Distributed ECU architecture
- ICAS1: Body/comfort domain
- ICAS2: Autonomous driving
- ICAS3: Infotainment

### E³ 1.2 (Update)
- Consolidated computing power
- Over-the-air (OTA) capability
- VW.OS integration

### E³ 2.0 (Future)
- Centralized HPC (High-Performance Computer)
- Software-defined vehicle
- Unified architecture with PPE

---

## Cost Structure

**Target Platform Cost Reduction:**
- Battery: €100/kWh target (2025)
- Motors: 30% reduction through scale
- Electronics: Shared across 10M+ units

**Manufacturing Efficiency:**
- 30% fewer parts than comparable ICE platform
- Shared assembly lines (flexible manufacturing)
- Target: 40% production cost savings vs. first-gen EVs

---

## Success Metrics

**Volume Achievement:**
- 4 million MEB-based BEVs delivered (as of March 2026)
- 50% of Group BEV volume

**Geographic Distribution:**
- Europe: 68% of MEB vehicles
- China: 20%
- North America: 8%
- Rest of world: 4%

---

## Future Evolution

**SSP Integration (Scalable Systems Platform):**
- MEB and PPE convergence (post-2026)
- Unified cell format (PowerCo)
- 800V architecture standardization
- Software-defined capabilities

**Entry-Level Extension:**
- ID.2all concept (€25,000 target)
- ID.1 (sub-€20,000 planned)
- Partnership with Rivian for cost optimization
