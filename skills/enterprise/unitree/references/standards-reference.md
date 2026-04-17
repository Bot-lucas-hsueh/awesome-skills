## § 8 — Standards & Reference

### 8.1 Robot Selection Matrix

| Use Case | Recommended | Budget | Why |
|----------|-------------|--------|-----|
| Education/Research | Go2 | $1,600 | Affordable, ROS2, good for learning |
| Industrial Inspection | B2 | $20,000 | IP67, 6 m/s, 5hr endurance |
| Humanoid Research (Startup) | G1 EDU | $40,000 | Best cost-performance, SDK access |
| Full-Size Humanoid | H1 | $90,000 | Record performance, mature platform |
| Competition | G1-Comp | $50,000 | RoboCup optimized, expanded DOF |

### 8.2 Technical Specifications

| Parameter | Go2 | B2 | G1 | H1 |
|-----------|-----|-----|-----|-----|
| **Dimensions** | Small | Large | Humanoid | Full-size |
| Height | ~40cm | ~60cm | 127cm | 180cm |
| Weight | ~15kg | ~60kg | ~35kg | ~47kg |
| **Mobility** | | | | |
| Max Speed | 3.5 m/s | 6 m/s | 2+ m/s | 3.3 m/s |
| DOF | 12 | 12 | 23-43 | 19-27 |
| **Perception** | | | | |
| LiDAR | 4D L1 | 3D LiDAR | Livox MID-360 | 3D LiDAR |
| Camera | Front | Front+Back | RealSense D435 | Depth camera |
| **Power** | | | | |
| Battery | ~2hr | 5hr+ | ~2hr | ~2hr |
| Hot-swap | No | Yes | Yes | Yes |
| **Environment** | | | | |
| IP Rating | Consumer | IP67 | Research | Research |
| **Development** | | | | |
| ROS2 | ✓ | ✓ | ✓ | ✓ |
| SDK | ✓ | ✓ | EDU only | ✓ |
| Simulation | ✓ | ✓ | ✓ | ✓ |

---
