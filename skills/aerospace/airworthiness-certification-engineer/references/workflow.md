## § 7 Standard Workflow

See [references/08-workflow.md](references/08-workflow.md)

---

---

## Anti-Pattern 2: Treating DO-178C as a Documentation Exercise
**❌ BAD**: Creating DO-178C plans and documentation after the software is written
**✅ GOOD**: DO-178C is a development process standard — the plans must be written and followed DURING development, not retroactively created:
```
DO-178C Table A-1 requires:
✓ Software Development Plan (SDP) — written BEFORE coding starts
✓ Software Verification Plan (SVP) — written BEFORE verification starts
✓ Software Configuration Management Plan (SCMP) — active THROUGHOUT development
✓ Software Quality Assurance Plan (SQAP) — active THROUGHOUT development

Retroactive documentation:
✗ Will fail audits
✗ Cannot establish the development history required for compliance
✗ DER will not sign compliance statement for retroactively documented software
```

---

### Anti-Pattern 3: Misclassifying Failure Conditions
**❌ BAD**: Classifying a failure as "Major" when pilot workload and combined effects make it "Hazardous"
**✅ GOOD**: Failure condition classification must consider combined effects, not just the single failure:
```
Example: "Display system failure" analysis

Wrong classification:
  Single display loss → crew can continue using other displays → "Minor"

Correct classification under ARP4761:
  Single display loss at critical flight phase (IMC approach):
  + Increased workload (+)
  + Reduction in safety margin (+ for IMC)
  + Effect if coincident with another event → "Hazardous" (not Minor)

The FHA must consider: phase of flight, crew workload, combined failure effects
```

---

### Anti-Pattern 4: Submitting Issue Papers Too Late
**❌ BAD**: Discovering novel features during certification review and submitting Issue Papers then
**✅ GOOD**: Submit Issue Papers for all novel/unusual features at program initiation:
```
Novel features list for modern aircraft — identify all of these at Day 1:
□ Fly-by-wire flight controls (no mechanical backup)
□ Lithium battery primary power source
□ Software-controlled fuel management
□ Composite primary structure (novel materials)
□ All-glass cockpit without backup analog instruments
□ Novel propulsion (electric, hybrid)
□ FANS/ADS-B equipage novel implementation

Late IP submission costs: typically 6-18 months per undisclosed novel feature
```

---

### Anti-Pattern 5: Assuming BASA Covers Everything
**❌ BAD**: Planning European market entry assuming FAA cert automatically validates in EASA
**✅ GOOD**: BASA has specific scope limitations:
```
NOT covered by FAA-EASA BASA:
✗ Military aircraft derivatives
✗ Certain very large transport (reviewed case-by-case)
✗ National differences items (must still be addressed)
✗ Modifications not covered by original TC data package

Country-specific requirements NOT covered by BASA:
✗ CAAC validation (China has separate procedures; no direct TC equivalency with FAA)
✗ ANAC (Brazil) validation — separate bilateral
✗ TCCA (Canada) — separate bilateral
✗ ICAO Annex 8 differences for specific countries
```

---

