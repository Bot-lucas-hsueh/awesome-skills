## § 7 · Standard Workflow

### Phase 1: Requirements & Hardware Selection (Week 1)

```
├── Define functional requirements
├── Determine resource constraints (RAM, flash, speed)
├── Select MCU based on requirements
├── Review datasheet and reference manual
└── [✓ Done]: MCU selected, specs validated
    [✗ FAIL]: Resources insufficient → select different MCU
```

### Phase 2: Architecture & Design (Week 2)

```
├── Design software architecture (layers, modules)
├── Define task structure (if using RTOS)
├── Design state machines for main logic
├── Plan memory map and allocation
└── [✓ Done]: Architecture document, memory budget
    [✗ FAIL]: Architecture too complex → simplify
```

### Phase 3: Implementation (Weeks 3-6)

```
├── HAL and driver implementation
├── Middleware/RTOS integration
├── Application logic development
├── Unit tests on host (where possible)
└── [✓ Done]: Code complete, builds without warnings
    [✗ FAIL]: Warnings or static analysis errors → fix
```

### Phase 4: Integration & Testing (Weeks 7-8)

```
├── Hardware-in-the-loop testing
├── Protocol compliance verification
├── Power consumption measurement
├── Stress testing (thermal, EMI)
└── [✓ Done]: All tests passing, certified
    [✗ FAIL]: Timing or power issues → optimize
```

---
