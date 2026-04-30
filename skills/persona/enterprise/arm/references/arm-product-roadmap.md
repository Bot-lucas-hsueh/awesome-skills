# Arm Product Portfolio and Roadmap

## CPU Architecture Roadmap

### Client/Mobile (Cortex)

| Generation | Big Core | Mid Core | Small Core | GPU | Launch |
|------------|----------|----------|------------|-----|--------|
| **TCS23** | Cortex-X4 | Cortex-A720 | Cortex-A520 | Immortalis-G720 | 2023 |
| **TCS24** | Cortex-X925 | Cortex-A725 | Cortex-A520 | Immortalis-G925 | 2024 |
| **TCS25** | Cortex-X930 | Cortex-A730 | Cortex-A525 | Immortalis-G930 | 2025 (est) |

**Key Improvements (X925 vs X4)**:
- 36% peak performance uplift
- 59% AI inference speed improvement
- 3nm process optimization

### Infrastructure (Neoverse)

| Platform | Core | Target | TDP | Key Feature |
|----------|------|--------|-----|-------------|
| **CSS N2** | Neoverse N2 | Scale-out | 100W+ | Cloud-optimized |
| **CSS V3** | Neoverse V3 | High-perf | 200W+ | HBM support, AI |
| **CSS N3** | Neoverse N3 | Edge/5G | 40W | 20% perf/watt vs N2 |
| **CSS V4** | Neoverse V4 | HPC/AI | 300W+ | 2025 (est) |

**Neoverse V3 Specifications**:
- Up to 128 cores per socket
- 2MB L2 cache per core
- CMN S3 mesh
- PCIe 5.0 + CXL 3.0
- DDR5 + HBM3 support

### Real-Time (Cortex-R)

| Core | Target | Safety | Use Case |
|------|--------|--------|----------|
| Cortex-R52+ | Automotive | ASIL-D | Domain controllers |
| Cortex-R82 | Storage | - | SSD controllers |
| Cortex-R82AE | Automotive | ASIL-B | Zone controllers |

### Microcontroller (Cortex-M)

| Core | Architecture | Use Case |
|------|--------------|----------|
| Cortex-M33 | v8-M | Secure IoT |
| Cortex-M55 | v8.1-M | ML at edge |
| Cortex-M85 | v8.1-M | High-perf embedded |
| Cortex-M52 | v8.1-M | Cost-optimized ML |

## Compute Subsystems (CSS)

### CSS Portfolio

| CSS | Target Market | Components | Value Proposition |
|-----|---------------|------------|-------------------|
| **CSS for Client** | Premium mobile/PC | X925 + A725 + G925 + System IP | AI performance, efficiency |
| **CSS N3** | Edge/5G/DPU | N3 cores + CMN + System IP | 20% better perf/watt |
| **CSS V3** | Cloud/HPC | V3 cores + CMN + HBM | Maximum performance |
| **Zena CSS** | Automotive | AE cores + Safety IP | ASIL-D, faster time-to-market |

**CSS Benefits**:
- Pre-integrated and validated
- 12-18 months faster time-to-market
- Higher royalty value vs. individual IP
- Production-proven (AWS Graviton4, Microsoft Cobalt)

## GPU Portfolio (Mali/Immortalis)

| Series | Target | Ray Tracing | Key Feature |
|--------|--------|-------------|-------------|
| Mali-G310 | Entry | No | Smallest GPU |
| Mali-G510 | Mid | No | Gaming capable |
| Mali-G710 | Premium | No | High refresh |
| Mali-G720 | Flagship | No | 2023 flagship |
| **Immortalis-G925** | Ultra | Yes | Hardware RT, 37% perf uplift |

## NPU Portfolio (Ethos)

| NPU | TOPS | Efficiency | Target |
|-----|------|------------|--------|
| Ethos-U55 | 0.5 | 0.5 TOPS/W | Tiny ML |
| Ethos-U65 | 1 | 0.5 TOPS/W | IoT |
| Ethos-U85 | 4 | 4 TOPS/W | Edge AI |
| Ethos-N77 | 4 | - | Mobile |

## Software and Tools

### Development Tools
- **Arm Compiler**: C/C++ compilation optimized for Arm
- **Arm Development Studio**: IDE for embedded development
- **Arm Performance Studio**: Profiling and optimization
- **Arm Virtual Hardware**: Cloud-based development/testing

### AI Software Stack
- **KleidiAI**: Optimized AI libraries for Arm
- **Arm NN**: Neural network inference engine
- **Ethos NPU driver stack**

### Operating System Support
- Android (native)
- Linux (distro and embedded)
- Windows 11 (on Arm)
- RTOS (FreeRTOS, Zephyr, etc.)

## Architecture Features

### Armv9 Key Features

| Feature | Benefit |
|---------|---------|
| **SVE2** | Vector processing for HPC/AI |
| **MTE** | Memory safety (reduces security vulnerabilities) |
| **BTI** | Branch target identification |
| **PAC** | Pointer authentication |
| **CCA/RME** | Confidential computing |
| **RAS** | Reliability, availability, serviceability |

### Security Technologies
- **TrustZone**: Secure/Normal world separation
- **Secure-EL2**: Hypervisor security
- **Realm Management Extension**: Confidential compute

---

*Source: Arm Technical Documentation, Product Announcements, Tech Symposia*
