## § 6 Professional Toolkit

| Tool | Purpose | When to Use |
|------|---------|-------------|
| Synopsys Design Compiler (DC) | RTL-to-gate-level synthesis | Synthesis stage; generate mapped netlist from Verilog |
| Cadence Innovus
| Synopsys PrimeTime | Static timing analysis sign-off | MCMM STA; setup/hold closure; check_timing |
| Mentor Calibre | DRC, LVS, ERC physical verification | Pre-tapeout sign-off; daily incremental checks |
| Synopsys VCS
| Mentor Questa | UVM simulation, formal lint | UVM testbench execution; CDC/RDC analysis |
| Synopsys Formality | Formal equivalence checking | Verify synthesis/ECO did not alter logic function |
| Synopsys PrimePower
| Synopsys SpyGlass | RTL lint, CDC/RDC analysis | Early RTL quality check; clock domain crossing detection |
| Mentor Tessent
| Cadence Virtuoso | Custom/analog layout | Mixed-signal IP, memory compiler views |
| Python + cocotb | RTL scripting, co-simulation testbench | Automation scripts; co-simulation with Python models |

---
