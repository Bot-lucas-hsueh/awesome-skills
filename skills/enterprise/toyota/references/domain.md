## §2 · Domain Knowledge

### §2.1 · Toyota Production System (TPS)

**The House of TPS:**

```
                    ┌─────────────┐
                    │   GOAL:     │
                    │ Best Quality│
                    │ Lowest Cost │
                    │ Shortest    │
                    │   Lead Time │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
      ┌────┴────┐     ┌────┴────┐    ┌────┴────┐
      │  JIT    │     │ Jidoka  │    │Leveled  │
      │Just-In- │     │(Built-in │   │Production│
      │  Time   │     │ Quality)│    │Heijunka │
      └────┬────┘     └────┬────┘    └─────────┘
           │               │
           └───────────────┴───────────────┐
                       │                    │
              ┌────────┴────────┐    ┌──────┴──────┐
              │  Stability &    │    │ Standardized │
              │  Standardization│    │    Work     │
              └─────────────────┘    └─────────────┘
```

**The 7 Wastes (Muda):**

| Waste | Japanese | Description | Example |
|-------|----------|-------------|---------|
| Overproduction | 生産過多 | Making too much, too early | Building ahead of schedule |
| Waiting | 待ち | Idle time when value not added | Machine downtime |
| Transport | 運搬 | Unnecessary movement of materials | Double-handling |
| Over-processing | 過加工 | Unnecessary work | Extra inspection steps |
| Inventory | 在庫 | Excess materials | Large WIP buffers |
| Motion | 動作 | Unnecessary movement | Reaching for tools |
| Defects | 不良品 | Rework or scrap | Quality escapes |

**JIT Implementation Principles:**

1. **Takt Time**: Production rate = Customer demand rate
2. **Continuous Flow**: One-piece flow where possible
3. **Pull System**: Kanban signals replenishment
4. **Quick Changeover**: SMED (Single-Minute Exchange of Die)

---

### §2.2 · Electrification Strategy

**Toyota's Multi-Pathway Approach (2024-2030):**

```
┌────────────────────────────────────────────────────────────────┐
│                    ELECTRIFICATION ROADMAP                     │
├────────────────────────────────────────────────────────────────┤
│  NOW (2024-2025)                                               │
│  ├── 30 electrified models in market                           │
│  ├── 27M+ electrified vehicles sold globally                   │
│  └── 47% of US sales electrified (2025)                       │
├────────────────────────────────────────────────────────────────┤
│  NEAR (2026-2027)                                              │
│  ├── 10 new BEV models launching                               │
│  ├── 1.5M annual BEV sales target                              │
│  ├── Performance battery: 800km range                          │
│  └── Popularized battery: 20% cost reduction                   │
├────────────────────────────────────────────────────────────────┤
│  FUTURE (2028-2030)                                            │
│  ├── Solid-state battery production                            │
│  ├── 3.5M annual BEV sales target                              │
│  └── $70B invested in electrification                          │
└────────────────────────────────────────────────────────────────┘
```

**Key Technologies:**

| Technology | Models | Key Specs |
|------------|--------|-----------|
| **Hybrid (HEV)** | Prius, Camry, RAV4, 25+ others | 50%+ US sales |
| **Plug-in Hybrid (PHEV)** | Prius Prime, RAV4 Prime | 40+ mile EV range |
| **Battery EV (BEV)** | bZ4X/bZ, Lexus RZ, bZ3 (China) | 236-314 mile range |
| **Fuel Cell (FCEV)** | Mirai (2nd gen) | 402 mile range, 5-min refuel |

**North Carolina Battery Plant:**
- **Investment:** $13.9 billion
- **Capacity:** 30 GWh annually
- **Employment:** 5,100 jobs
- **Production:** 2025 startup
- **Purpose:** Supply US-built EVs including Kentucky-made 3-row SUV (2026)

---

### §2.3 · Quality Systems

**Jidoka (自働化 - Autonomation):**

> "Intelligent automation" - machines stop when abnormalities occur

**Four Stages of Jidoka:**

1. **Detect** the abnormality (sensor, operator, machine)
2. **Stop** the process immediately (Andon cord)
3. **Fix** the immediate problem (containment)
4. **Solve** the root cause (permanent countermeasure)

**Quality Awards (2024-2025):**

| Award | Result | Models Recognized |
|-------|--------|-------------------|
| JD Power 2025 VDS | Lexus #1 (140 PP100) | Lexus GX |
| | Toyota #3 mass market (162 PP100) | Camry, Corolla, RAV4, Sienna, Tacoma |
| JD Power 2025 IQS | Above average | Industry-leading reliability |
| Consumer Reports | #2 reliability | Across lineup |

**The Andon System:**

```
Worker sees problem → Pull Andon cord
                           ↓
              ┌────────────┼────────────┐
              ↓            ↓            ↓
           Yellow       Red        Line Stop
         (Warning)   (Stop)      (Emergency)
              ↓            ↓            ↓
         Team leader   Support      Critical
         responds      called       safety/
                                   quality issue
```

---

### §2.4 · Product Development

**The Toyota Development System:**

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| **Concept** | 12-18 months | Market analysis, target setting, chief engineer selection |
| **Planning** | 6-12 months | Detailed specs, supplier selection, cost planning |
| **Development** | 24-36 months | Design, prototyping, testing, production prep |
| **Launch** | 6-12 months | Pilot production, quality ramp, full production |

**Chief Engineer (Shusa) System:**

The Chief Engineer has total responsibility for the vehicle:
- Product concept and market fit
- Design and engineering decisions
- Quality, cost, and timing targets
- Cross-functional team leadership

**Set-Based Concurrent Engineering:**

Instead of committing to one design early, Toyota:
1. Explores multiple design concepts in parallel
2. Uses trade-off curves to understand relationships
3. Delays final decisions until knowledge is maximum
4. Integrates with suppliers early in process

---
