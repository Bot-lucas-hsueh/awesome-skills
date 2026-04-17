## § 3 Risk Disclaimer

**[SAFETY CRITICAL] All structural analysis and material recommendations provided by this skill are for engineering guidance only. Primary flight structures and safety-critical applications MUST be validated through physical testing, peer-reviewed analysis, and regulatory certification. Do not use AI-generated analysis as the sole basis for flight-critical design decisions.**

| Risk Category | Specific Risk | Severity | Mitigation |
|---|---|---|---|
| **Data Currency** | Material property databases may not reflect latest supplier lot-to-lot variation or updated qualification data | HIGH | Always source properties from CMH-17, MMPDS, or customer-approved material qualification reports; specify lot testing requirements |
| **Process Sensitivity** | Composite properties are highly sensitive to manufacturing parameters (void content, cure cycle, fiber alignment); AI recommendations assume ideal processing | HIGH | Validate with process development trials and NDT acceptance testing before production |
| **Environmental Degradation** | Long-term moisture uptake, UV exposure, and thermal cycling degrade matrix-dominated properties significantly (up to 30% ETW knock-down) | HIGH | Apply environmental knock-down factors from material qualification data; design for ETW condition |
| **Failure Mode Complexity** | Progressive damage and post-buckling behavior in composites involve complex failure mode interactions that simplified models may not capture | MEDIUM | Use Building Block Approach; validate FEA models against coupon and element tests before applying to structural analysis |
| **Regulatory Compliance** | Certification requirements evolve; FAA AMOCs, EASA Technical Opinions, and NADCAP procedure revisions may supersede guidance given here | HIGH | Verify current regulatory requirements with your DER/DAR, EASA DOA, or applicable certifying authority before finalizing designs |
| **Repair Critical Limits** | Bonded composite repairs have limited ability to transfer very high loads; improper repairs can introduce stress concentrations worse than original damage | CRITICAL | All structural repairs on primary structure require engineering approval and must follow approved SRM procedures or obtain engineering order authorization |

---
