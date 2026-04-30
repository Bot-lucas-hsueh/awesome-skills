## § 4 · Core Philosophy

### 4.1 Embedded Architecture Model

```
┌─────────────────────────────────────────┐
│         Application Layer               │  ← Business logic, state machines
├─────────────────────────────────────────┤
│         Middleware / RTOS               │  ← Task scheduling, IPC, timers
├─────────────────────────────────────────┤
│         Hardware Abstraction            │  ← GPIO, timers, ADC drivers
├─────────────────────────────────────────┤
│         Peripheral Drivers              │  ← I2C, SPI, UART, CAN
├─────────────────────────────────────────┤
│         Hardware (MCU)                  │  ← ARM, ESP32, STM32
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Static Allocation** — Avoid malloc/free; use memory pools
2. **Deterministic Behavior** — No surprises in timing or resource usage
3. **Fail-Safe Design** — System degrades gracefully, never crashes dangerously
4. **Hardware Understanding** — Read datasheets, understand electrical specs
5. **Test in Hardware** — Simulation isn't reality; test on real hardware

---
