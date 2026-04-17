## § 6 · Domain Knowledge

### 6.1 MCU Selection Guide

| MCU | Best For | Specs |
|-----|----------|-------|
| **STM32** | Industrial, general purpose | Cortex-M0 to M7, rich ecosystem |
| **ESP32** | IoT, WiFi/BLE | Dual-core, integrated wireless |
| **nRF52** | BLE-focused | Ultra-low power, Nordic stack |
| **RP2040** | Education, prototyping | Dual Cortex-M0+, PIO |

### 6.2 Communication Protocol Comparison

| Protocol | Speed | Distance | Use Case |
|----------|-------|----------|----------|
| **I2C** | 400kHz | < 1m | Sensors, EEPROMs |
| **SPI** | 50MHz+ | < 0.5m | Fast data, displays |
| **UART** | 1Mbps | < 15m | Debug, GPS, modems |
| **CAN** | 1Mbps | < 40m | Automotive, industrial |

### 6.3 RTOS Task Priorities

| Priority | Task Type | Response Time |
|----------|-----------|---------------|
| **Highest** | Interrupt handlers | Microseconds |
| **High** | Safety-critical tasks | Milliseconds |
| **Medium** | Control loops | 10s of milliseconds |
| **Low** | Background tasks | Seconds acceptable |

---
