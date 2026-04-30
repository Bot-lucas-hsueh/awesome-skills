# python Example

```
# 3+3 dose escalation for CAR-T Phase I trial
def dose_escalation_3plus3(dose_levels_cells_per_kg):
    """
    Standard 3+3 design for CAR-T cell therapy.
    DLT window: 28 days post-infusion (CRS, ICANS, prolonged cytopenias)
    """
    protocol = []
    for i, dose in enumerate(dose_levels_cells_per_kg):
        cohort = {
            'level': i + 1,
            'dose': dose,
            'dose_str': f"{dose/1e6:.1f}×10^6 CAR-T/kg",
            'n_patients': 3,
            'DLT_window_days': 28,
            'escalation_rule': (
                '0/3 DLTs → escalate to next level; '
                '1/3 DLTs → expand to 6; ≤1/6 → escalate; '
                '≥2/6 DLTs → STOP, declare MTD at previous level'
            ),
        }
        protocol.append(cohort)
    return protocol

dose_levels = [0.5e6, 1e6, 2.5e6, 5e6, 10e6]  # CAR-T cells/kg
plan = dose_escalation_3plus3(dose_levels)
for p in plan:
    print(f"Cohort {p['level']}: {p['dose_str']}")

# CRS/ICANS grading per ASTCT 2019 consensus
CRS_GRADES = {
    1: 'Fever ≥38°C (no hypotension, no hypoxia) → close monitoring',
    2: 'Fever + hypotension responding to IV fluids OR O2 by low-flow NC → tocilizumab 8 mg/kg IV',
    3: 'Hypotension needing vasopressors OR O2 by high-flow/CPAP → tocilizumab + dexamethasone',
    4: 'Life-threatening hypotension + respiratory failure (intubation) → ICU, high-dose steroids',
}
```
