## 7. Standards & Reference

### 7.1 Key Standards

| Standard | Scope | Key Requirements |
|----------|-------|-----------------|
| ISO 9283:1998 | Manipulator performance measurement | Defines pose accuracy, repeatability, path accuracy test methods; requires 30-point test protocol |
| ISO 10218-1:2011 | Robot safety — manipulators | Mechanical stop requirements, joint limit devices, payload markings, overload protection |
| CE Machinery Directive 2006/42/EC | European market access | Technical File, Risk Assessment (EN ISO 12100), Declaration of Conformity required |
| DIN EN ISO 10218-1 | German implementation of ISO 10218-1 | Same scope; required for German market; TÜV/BG inspection pathway |
| ASME Y14.5-2018 | GD&T standard | Defines flatness, cylindricity, true position callouts on engineering drawings |
| MIL-HDBK-5J

### 7.2 Structural Performance Metrics

| Metric | Formula | Target | Notes |
|--------|---------|--------|-------|
| Structural safety factor (yield) | SF = Fty
| Structural safety factor (ultimate) | SF_ult = Ftu
| Tip deflection at rated load | δ = F × L³
| First natural frequency | ωn = (1/2π) × sqrt(K_eff
| Payload-to-weight ratio | PWR = m_payload
| Fatigue life | N = C / (σ_a
| Link mass vs cross-section | ρ_Al7075 = 2.81 g/cm³, E = 71.7 GPa | CFRP: ρ = 1.6 g/cm³, E_axial = 135 GPa | CFRP E/ρ = 84 vs Al7075 E/ρ = 25 GPa·cm³/g |
| ISO 9283 pose repeatability | RP = max(l_j); l_j = distances from mean pose | ≤ 0.02mm (precision), ≤ 0.05mm (industrial) | Measured at 30 poses in workspace |

---

