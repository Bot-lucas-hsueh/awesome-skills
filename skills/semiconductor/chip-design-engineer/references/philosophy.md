## § 4 Core Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│              FULL FRONT-TO-BACK ASIC FLOW                       │
│                                                                 │
│  SPEC/ARCH ──► RTL ──► SYNTH ──► P&R ──► STA ──► SIGNOFF      │
│      │          │        │        │       │         │           │
│   [Micro-    [Verilog/ [DC/    [Innovus/ [Prime-  [Calibre     │
│   arch &     SV, UVM] Genus]   ICC2]   Time]    DRC/LVS]      │
│   uArch]                                                        │
│                                                                 │
│   [DFT] ──────── inserted before P&R ───────────────────────── │
│   Scan/BIST/JTAG → ATPG patterns → gate-level simulation       │
│                                                                 │
│   POWER DOMAINS: VDD_CORE / VDD_IO
│   CLOCK DOMAINS: SYS_CLK / PCIE_CLK
└─────────────────────────────────────────────────────────────────┘
```

**Principle 1 — Constraints Are Silicon Law:** SDC files define timing requirements with legal force. A loose constraint hides a real violation; a tight false constraint wastes area. Every constraint must be justified by system architecture.

**Principle 2 — Quality of Results (QoR) Is Measurable:** Track WNS, TNS, cell count, dynamic power, and routing congestion at every milestone. Never accept "should be fine" — quantify everything.

**Principle 3 — Tapeout Readiness Is Binary:** All DRC clean, all LVS clean, all timing closed across all MCMM corners, all DFT coverage targets met. Partial compliance equals no-go. Respin cost dwarfs any schedule pressure.

---

