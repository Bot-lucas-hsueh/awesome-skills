# CARIAD Software Roadmap

**Company:** CARIAD SE (Volkswagen Group Software Company)  
**Founded:** 2020 (consolidated from Volkswagen software units)  
**Headquarters:** Munich, Germany  
**Employees:** ~6,000 (2025, down from peak)

---

## Mission & Vision

**Mission:** Develop leading software platforms and digital functions for Volkswagen Group vehicles, enabling a unified software stack across all brands.

**Vision:** Transform VW Group into a software-driven mobility provider with seamless digital experiences.

---

## Organizational Structure

### Leadership
- **CEO:** Peter Bosch (appointed 2023)
- **CTO:** TBD
- **Parent:** Volkswagen AG (100% owned)

### Operating Units
1. **Platform Development:** Core OS and middleware
2. **Vehicle Functions:** ADAS, body electronics, powertrain software
3. **Digital Experience:** Infotainment, connectivity, ecosystem
4. **Cloud & Data:** VW.AC (Automotive Cloud), analytics

### Global Presence
- **Munich:** Headquarters, platform development
- **Ingolstadt:** Audi-specific development
- **Weissach:** Porsche-specific development
- **Wolfsburg:** VW brand development
- **Berlin:** UX/UI design
- **Silicon Valley:** AI/ADAS R&D
- **Seattle:** Cloud engineering
- **China:** Local software adaptation

---

## Software Platforms

### VW.OS (Volkswagen Operating System)
**Description:** Unified operating system for all VW Group vehicles

**Architecture:**
- Linux-based foundation
- Microservices architecture
- Hypervisor for safety isolation
- OTA update capability

**Versions:**
| Version | Release | Features |
|---------|---------|----------|
| VW.OS 1.0 | 2020 | Basic connectivity, limited OTA |
| VW.OS 1.2 | 2022 | Enhanced ADAS, improved UX |
| VW.OS 2.0 | 2024 | Unified HPC, advanced autonomy |
| VW.OS 3.0 | 2026 | AI integration, full SDV |

### E³ Architecture Evolution

**E³ 1.1 (MEB Initial):**
- Three ICAS (In-Car Application Servers)
- ICAS1: Body/comfort (Gateway)
- ICAS2: ADAS
- ICAS3: Infotainment
- ~70 ECUs in vehicle

**E³ 1.2 (MEB Update):**
- Consolidated domain controllers
- Enhanced computing power
- Improved OTA capability
- ~40 ECUs

**E³ 2.0 (PPE/Advanced MEB):**
- Central HPC (High-Performance Computer)
- Zonal architecture
- ~15 ECUs
- Full SDV capabilities

**E³ 3.0 (SSP):**
- Single central computer
- Complete software decoupling from hardware
- Continuous feature updates

### ADAS/Autonomy Stack

**Current Capabilities (IQ.Drive):**
- Travel Assist: L2+ highway driving
- Lane keeping, adaptive cruise
- Emergency assist
- Park Assist Plus

**Development Path:**
| Level | Timeline | Features |
|-------|----------|----------|
| L2+ | Current | Highway assist, traffic jam |
| L2++ | 2025-26 | Urban assist, automated parking |
| L3 | 2027-28 | Traffic Jam Pilot, highway autonomy |
| L4 | 2030+ | Robotaxi capabilities |

**Partnerships:**
- **Horizon Robotics:** China-specific ADAS
- **Qualcomm:** Snapdragon Ride platform
- **Mobileye:** EyeQ6 for select applications
- **Bosch:** Sensor integration

---

## Financial Performance

| Year | Revenue | Operating Loss | Headcount |
|------|---------|----------------|-----------|
| 2021 | €0.5B | €-1.3B | ~4,500 |
| 2022 | €0.8B | €-2.0B | ~5,500 |
| 2023 | €1.1B | €-2.4B | ~6,200 |
| 2024 | €1.3B | €-2.4B | ~6,500 |
| 2025 | €1.8B | €-2.2B | ~6,000 |

**Key Metrics (2025):**
- Revenue growth: +33.8%
- Loss improvement: +8.3%
- Software deliveries to brands: Significant increase
- Restructuring expenses: High but declining

---

## Product Delivery Status

### Delivered
- MEB E³ 1.1 (all MEB vehicles)
- ICAS3 infotainment (MIB3)
- VW.OS basic functionality
- OTA capability (limited)
- We Connect/We Connect Plus

### Delayed
- E³ 1.2: 12-18 months behind schedule
- E³ 2.0: Development ongoing, delayed
- Porsche Macan EV software: Launch affected
- Audi Q6 e-tron: Software delays

### In Development
- E³ 2.0 for PPE platform
- SSP unified architecture
- Scout Motors software stack
- L3 autonomous functions

---

## Key Challenges

### 1. Delivery Delays
- Multiple vehicle launches impacted
- Quality issues requiring post-launch updates
- Reputational damage

### 2. Organizational Complexity
- Matrix structure with brands creates conflicts
- Resource allocation disputes
- Talent retention issues

### 3. Talent Competition
- Competition with Tesla, Apple, Google
- German salary scales vs. Silicon Valley
- Remote work limitations

### 4. Technical Debt
- Legacy architecture constraints
- Integration complexity
- Testing and validation bottlenecks

---

## Strategic Partnerships

### Rivian ($5.8B Investment)
**Scope:** Joint venture for electrical architecture and software
**Focus:**
- Zonal E/E architecture
- Software platform for Scout Motors
- Cost optimization for entry EVs

### Qualcomm
**Scope:** Chipset partnership for ADAS and infotainment
**Products:**
- Snapdragon Cockpit Platforms
- Snapdragon Ride for autonomy

### Google
**Scope:** Android Automotive for infotainment layer
**Applications:**
- App ecosystem
- Google Maps integration
- Voice assistant

### Horizon Robotics (China)
**Scope:** ADAS for Chinese market
**Products:**
- Journey chips
- Localized perception systems

### Xpeng
**Scope:** Platform collaboration
**Focus:**
- China-specific EV architectures
- ADAS technology sharing

---

## Transformation Program

### Restructuring Actions (2024-2025)
- Headcount reduction: ~1,000 positions
- Management layer consolidation
- Agile transformation
- External partnership expansion

### Target State (2027)
- Headcount: 4,000-4,500
- Revenue: €3B+
- Break-even: Target 2027
- Delivery: On-time software releases

### Organizational Changes
1. **Decentralized Development:** Brand-specific pods
2. **Platform Focus:** Core OS centralized
3. **External Integration:** Partner-managed applications
4. **Cloud-First:** VW.AC expansion

---

## Scout Motors Specific

**Challenge:** Scout EREV requires integration of Rivian EV software with range-extender engine management

**Solution Path:**
- Cariad adapting Rivian stack for EREV
- Collaboration with VW engine management teams
- Hybrid powertrain software integration

**Timeline:** Contributing to Scout production delay

---

## Future Roadmap

### 2026 Milestones
- E³ 2.0 first production release
- L2++ ADAS deployment
- VW.OS 2.0 rollout
- Break-even progress

### 2027-2028 Targets
- L3 autonomous functions
- SSP platform software ready
- Scout Motors software delivery
- Full SDV capabilities

### 2030 Vision
- Unified software stack across all brands
- L4 autonomous capabilities
- Complete OTA feature updates
- Software revenue streams
