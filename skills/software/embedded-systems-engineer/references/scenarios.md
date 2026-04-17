## § 8 · Scenario Examples

### Example 1: IoT Sensor Node

**Context**: Battery-powered environmental sensor reporting to cloud.

**Design**:
```
Hardware: ESP32-C3 (low power, WiFi)
Power Budget: 2×AA batteries, 2-year life

Architecture:
├── Sleep 59 minutes (deep sleep: 5µA)
├── Wake, read sensors (2 seconds, 50mA)
├── Connect WiFi, send data (5 seconds, 150mA)
├── Average current: < 100µA

Optimizations:
├── Sensor power gating
├── WiFi fast connect (cached connection)
├── Data batching (send every hour)
└── Watchdog for lockup detection
```

---

### Example 2: Motor Controller

**Context**: BLDC motor controller for drone.

**Implementation**:
```
MCU: STM32F4 (Cortex-M4, DSP)
RTOS: FreeRTOS

Requirements:
├── 10kHz control loop (100µs deadline)
├── Sensorless commutation
├── PID control with anti-windup
├── Emergency stop (hardware)

Tasks:
├── ISR: Hall sensor capture (highest priority)
├── High: FOC control loop
├── Medium: Speed calculation
└── Low: Telemetry, debug
```

---

### Example 3: Medical Device Firmware

**Context**: Infusion pump with safety-critical requirements.

**Design**:
```
Standards: IEC 62304, FDA Class II
Language: MISRA-C compliant

Safety Features:
├── Dual-channel sensor validation
├── Watchdog with independent clock
├── Hardware interlocks (independent of software)
├── CRC on all stored parameters
├── Black box for incident analysis

Testing:
├── 100% statement coverage
├── Hardware fault injection
├── EMC testing (IEC 60601-1-2)
```

---

### Example 4: Protocol Bridge

**Context**: Bridge between CAN bus and Ethernet.

**Implementation**:
```
MCU: STM32H7 (dual-core)
RTOS: Zephyr

Architecture:
├── Core M7: Ethernet, TCP/IP stack
├── Core M4: CAN bus handling
├── Shared memory for message queue
├── Message filtering and routing

Challenges:
├── Different clock domains
├── Priority inversion prevention
├── Buffer overflow protection
└── Protocol conversion validation
```

---

### Example 5: Bootloader Development

**Context**: Secure bootloader for firmware updates.

**Features**:
```
Security:
├── Encrypted firmware images
├── Digital signature verification
├── Rollback protection (anti-downgrade)
├── Secure key storage

Reliability:
├── Dual bank for atomic update
├── Power-fail safe
├── Recovery mode on failed boot
├── Progress indication
```

---
