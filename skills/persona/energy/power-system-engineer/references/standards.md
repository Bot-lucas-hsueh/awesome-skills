## § 7 · Standards & Reference

### 7.1 Power System Analysis Frameworks

| Framework| When to Use| Key Steps|
|-----------------|----------------------|-------------------|
| **Newton-Raphson Load Flow** | Large transmission systems, ill-conditioned grids | 1. Form Y-bus → 2. Initialize voltages → 3. Calculate mismatches → 4. Jacobian update → 5. Iterate to convergence (<0.1 MW/MVAR) |
| **DC Power Flow** | Preliminary screening, contingency ranking | 1. Extract B-matrix → 2. Solve linear DC → 3. Apply shift factors → 4. Rank by overload |
| **Equal Area Criterion** | Transient stability assessment, two-machine systems | 1. Define pre-fault, fault, post-fault areas → 2. Calculate acceleration/deceleration areas → 3. Determine CCT |
| **PV Curve Analysis** | Voltage stability, maximum power transfer | 1. Vary load power factor → 2. Track voltage at weak bus → 3. Identify nose point |

### 7.2 Key Standards

| Standard| Coverage| Key Requirement|
|--------------|--------------|---------------|
| **IEEE 1547-2018** | DER interconnection | Ride-through, voltage regulation, frequency response |
| **IEEE 399** | Industrial power system design | Motor starting, harmonic limits, grounding |
| **ANSI C84.1** | Voltage ratings | 0.95-1.05 pu service voltage, 0.90-1.05 pu utilization |
| **NERC TPL-001** | Transmission system planning | N-1 contingency compliance |
| **IEC 60909** | Short-circuit calculation | Temperature correction, impedance tolerance |

---
