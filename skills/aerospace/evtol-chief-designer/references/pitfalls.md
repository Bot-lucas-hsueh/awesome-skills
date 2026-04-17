## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Optimistic Battery Energy Density
**❌ BAD**: Sizing eVTOL battery using press-release energy densities (400+ Wh/kg)
```
# Wrong: using best-case future cell energy density in 2026 design
battery_energy_density = 400  # Wh/kg (this is R&D cell, not production pack)
battery_mass = mission_energy
```
**✅ GOOD**: Use production pack-level energy density with degradation allowance
```python
# Correct: pack-level energy density with 20% end-of-life reserve
cell_energy_density = 300  # Wh/kg (NMC 811 cell, achievable in 2026)
pack_efficiency = 0.85      # Cell → pack (BMS, housing, wiring losses)
eol_factor = 0.80           # 80% usable at end of service life (5 years)
usable_pack_energy_density = cell_energy_density * pack_efficiency * eol_factor
# = 204 Wh/kg — this is your actual design number
```
**Why it matters**: Overoptimistic energy density assumptions are the #1 cause of eVTOL range shortfalls in flight test. Joby, Archer, and Lilium all encountered this.

