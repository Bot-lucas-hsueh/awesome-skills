## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| **Incorrect DAL Assignment** | CATASTROPHIC | Safety-critical function has insufficient assurance; may not detect failure modes; potential for catastrophic aircraft loss | ARP4754A independence requirement for DAL-A/B; independent safety reviewer; SSA must be completed before DAL assignment is finalized |
| **Certification Basis Change Mid-Program** | CRITICAL | Amdt. cutoff date change can add years to program; compliance data may need to be regenerated | Lock certification basis at program initiation with ACO; document in TCP; any changes require formal issue paper |
| **Undisclosed Novel Feature** | CRITICAL | Authority discovers novel feature during flight test phase; program halted for Issue Paper; 12-24 month delay | Novel feature review at concept phase; proactive IP submission; don't assume novelty won't be noticed |
| **Incomplete Independence (DO-178C)** | SERIOUS | DAL-A software without independent V&V cannot be approved; requires costly program restart | Plan independence from Day 1; separate teams for development and verification; DER must review independence artifacts |
| **BASA Scope Limitations** | MODERATE | Not all design features are covered by bilateral agreement; unexpected direct EASA/CAAC review required | Review BASA scope before program planning; identify features outside bilateral scope early |
| **Test Witness Requirements** | MODERATE | FAA/EASA requires advance notice for test witnessing; failure to notify can invalidate test data | Submit TIA (Test Initiation Acknowledgment) with 5+ working days notice; confirm witness attendance before test |

---
