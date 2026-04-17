## § 3 · Three-Layer Architecture

### Layer 1: System Architecture

**Purpose**: Define avionics system structure and interfaces.

**Core Elements**:
- **Functional Allocation**: Partition functions to hardware
- **Data Architecture**: Communication networks and protocols
- **Power Architecture**: Electrical power distribution
- **Physical Integration**: Rack layout, cooling, wiring

📄 **Details**: [references/05-layer1-architecture.md](references/05-layer1-architecture.md)

### Layer 2: Hardware Design

**Purpose**: Develop airborne electronic hardware.

**Core Elements**:
- **Circuit Design**: Processors, interfaces, power supplies
- **PCB Layout**: EMI/EMC considerations, high-speed design
- **Environmental Design**: DO-160 categories (temp, altitude, vibration)
- **DO-254 Compliance**: Planning, design, verification, validation

📄 **Details**: [references/06-layer2-hardware.md](references/06-layer2-hardware.md)

### Layer 3: Software Development

**Purpose**: Develop safety-critical embedded software.

**Core Elements**:
- **Requirements**: System → High-Level → Low-Level
- **Design**: Architecture, detailed design
- **Coding**: MISRA C/C++, Ada, model-based (Simulink/SCADE)
- **Verification**: Reviews, analysis, testing (MCDC for DAL A)

📄 **Details**: [references/07-layer3-software.md](references/07-layer3-software.md)

---
