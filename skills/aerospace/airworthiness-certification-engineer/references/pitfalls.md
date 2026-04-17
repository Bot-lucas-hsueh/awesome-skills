## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Safety Assessment After Architecture Is Fixed
**❌ BAD**: Completing FHA/PSSA/SSA after hardware is designed and software is coded
**✅ GOOD**: Safety assessment is iterative and MUST precede key design decisions:
```
Correct sequence:
  FHA (Functional Hazard Assessment) → before System Design starts
  PSSA (Preliminary SSA) → before Detailed Design starts
  SSA (System Safety Assessment) → before First Flight
  Updated SSA → before Type Certificate

Wrong sequence:
  Design → Build → Test → "Now let's do the FMEA"
  Result: Architecture cannot meet safety objectives → expensive redesign
```
**Why it matters**: A safety assessment that reveals a DAL-A requirement on a component designed as DAL-C means a complete redesign of that component and its associated software/hardware.

