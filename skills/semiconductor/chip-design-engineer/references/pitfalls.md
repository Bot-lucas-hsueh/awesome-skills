## § 10 Common Pitfalls

### Anti-Pattern 1 — Unconstrained Clock Domain Crossing

❌ **BAD:**
```systemverilog
// Direct register crossing clk_a domain to clk_b — METASTABILITY
always_ff @(posedge clk_b) begin
  data_out <= data_from_clk_a_domain;  // No synchronizer!
end
```

✅ **GOOD:**
```systemverilog
// Two-flop synchronizer for single-bit control signals
logic sync_ff1, sync_ff2;
always_ff @(posedge clk_b or negedge rst_n) begin
  if (!rst_n) {sync_ff2, sync_ff1} <= 2'b0;
  else        {sync_ff2, sync_ff1} <= {sync_ff1, data_from_clk_a};
end
assign data_out = sync_ff2;
```

**Why it matters:** Unconstrained CDC causes random functional failures in silicon, nearly impossible to reproduce and debug in the lab. Metastability probability never reaches zero — synchronizers are mandatory.

