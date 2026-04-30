## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| Timing sign-off miss at tapeout | CRITICAL | Silicon failure; full respin cost $1M–$10M | MCMM STA with all PVT corners; freeze netlist 2 weeks before tapeout |
| DRC/LVS violations at GDS submission | CRITICAL | Foundry rejects GDS; 4–8 week delay and penalty cost | Daily incremental DRC during P&R; Calibre sign-off mandatory |
| CDC metastability (unconstrained crossing) | HIGH | Random functional failures in silicon; field returns | SpyGlass CDC or JasperGold analysis; two-flop synchronizer insertion |
| Insufficient DFT coverage (<95% stuck-at) | HIGH | Defective chips shipped to customers; field recall risk | ATPG coverage report before tapeout; BIST for memories |
| Power grid IR drop > 5% VDD | HIGH | Timing degradation and electromigration failure | Voltus dynamic IR analysis; add decoupling caps and power straps |
| Process node PDK misuse | CRITICAL | Electrical rule violations; long-term reliability failure | Use only foundry-approved PDK version; no manual rule overrides |
| Late ECO mask cost overrun | MEDIUM | $500K+ per metal mask layer respin | Freeze design 3 weeks before tape; use metal-only ECO flow if possible |

---
