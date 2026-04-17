## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Forgetting TCM Delta-V Budget
**❌ BAD**: Allocating all propellant to orbit insertion; no reserve for trajectory corrections
**✅ GOOD**: Always budget for trajectory correction maneuvers (TCMs):
```python
# Wrong: entire dv budget to MOI
dv_mission = dv_moi  # 900 m/s
propellant = compute_propellant(dv_mission, dry_mass, Isp)

# Right: include TCMs and margin
dv_mission = (
    dv_launch_dispersion_correction +  # 30-50 m/s (correct LV performance error)
    dv_tcm_enroute * 3 +               # 3 × 20 m/s TCMs en route
    dv_orbit_insertion +               # 900 m/s
    dv_orbit_maintenance_annual * years + # 20 m/s/year
    dv_disposal +                      # 30 m/s
    dv_margin * 0.15                   # 15% of total
)
```
**Why it matters**: The Mars Climate Orbiter was destroyed because navigation errors accumulated; you need propellant to correct them.

