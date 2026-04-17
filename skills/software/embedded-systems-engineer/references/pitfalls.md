## § 9 · Common Pitfalls

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Printf Debugging** | UART impact on timing | Conditional compilation, ring buffers |
| **Busy Waiting** | Wastes CPU cycles | Use interrupts, RTOS delays |
| **Magic Numbers** | Unmaintainable code | Named constants, enums |
| **No Watchdog** | System hangs indefinitely | Refresh only in main loop |
| **Ignoring Datasheets** | Incorrect timing, voltages | Always verify electrical specs |
| **No Version Info** | Can't identify firmware | Version in flash, readable externally |

---
