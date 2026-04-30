## § 7 · How to Use

```
Read https://theneoai.github.io/awesome-skills/skills/logistics/supply-chain-expert/SKILL.md and install
```

Typical prompts: "Calculate safety stock for 95% service level with 100 units/day demand," "Help me design an S&OP process for a manufacturing company," "Segment our supplier base using Kraljic matrix," "Build an inventory reduction plan without hurting fill rate."

---

## 7b. Quality Verification

Ask: "Calculate EOQ for: annual demand 10,000 units, ordering cost $200/order, unit cost $50, carrying rate 25%."

**Expected response elements:**
- H = $50 × 0.25 = $12.50/unit/year
- EOQ = √(2 × 10,000 × $200
- Orders per year = 10,000
- Annual holding cost = 566/2 × $12.50 = $3,538
- Annual ordering cost = 17.7 × $200 = $3,538 (equal at optimum — EOQ validation)
- Recommendation: Order ~566 units ~18× per year

---
