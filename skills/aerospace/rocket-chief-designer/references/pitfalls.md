## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Not Iterating Mass Budget
**❌ BAD**: Sizing the vehicle at concept phase and not re-running the mass budget when subsystem designs mature
**✅ GOOD**: Vehicle mass budget requires iteration — every major subsystem change propagates to GLOW:
```python
# Vehicle sizing is a fixed-point iteration:
def vehicle_sizing_iteration(payload_kg, dv_total):
    m_upper_stage = size_upper_stage(payload_kg, dv_stage2, Isp_upper)
    m_stage1 = size_stage1(m_upper_stage, dv_stage1, Isp_stage1)
    GLOW = m_stage1 + m_upper_stage + payload_kg

    # If subsystem mass grows (e.g., structure 10% heavier):
    m_structure_delta = 1000  # kg extra structure
    GLOW_new = vehicle_sizing_iteration(payload_kg, dv_total,
                                        extra_mass=m_structure_delta)
    # At stage 1, 1 kg of extra structure ≈ 50 kg GLOW growth
    print(f"GLOW growth from 1000 kg structure: {GLOW_new - GLOW} kg")
    # ≈ 40,000-50,000 kg GLOW growth (40-50× multiplier)
```

