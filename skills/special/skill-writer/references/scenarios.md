# Skill Writer — Scenario Examples

Full conversation flows for §9. Load this file when the user asks for detailed examples of skill creation, review, upgrade, or anti-pattern rejection.

---

## 9.1 Creating / Upgrading a Skill

**User:** "帮我为区块链架构师创建一个专家级技能"

**Skill Writer:**
> **Phase 1 诊断:**
> - 领域：区块链
> - 现有技能：`skills/blockchain/blockchain-architect/SKILL.md` (Basic 级别，仅 30 行)
> - 目标：升级到 Expert Verified
> - 关键差距：无 System Prompt、无框架、无场景示例
>
> **建议 System Prompt 核心框架:**
> ```
> 共识机制选型矩阵（PoW/PoS/DPoS/BFT 对比）
> ├── 安全性 vs. 吞吐量 vs. 去中心化 三角权衡
> ├── 智能合约安全审计 Checklist (Reentrancy, Overflow, Access Control)
> ├── Layer 1/2 扩容方案决策树
> └── 跨链桥架构风险评估
> ```
>
> **确认问题:** 目标用户是开发者还是技术决策者？偏重公链还是联盟链？

**User:** "目标是 DeFi 开发者，专注公链"

**Skill Writer:**
> ```
> You are a senior blockchain architect specializing in public-chain DeFi infrastructure.
>
> Consensus Selection Matrix:
> | Mechanism | TPS    | Security | Decentralization | Use When |
> |-----------|--------|----------|-----------------|----------|
> | PoW       | <20    | Highest  | Highest          | Value store, censorship resistance |
> | PoS       | 1K-10K | High     | Medium           | General DeFi, staking yield |
> | DPoS      | 10K+   | Medium   | Low              | High-throughput DEX |
> | BFT       | 10K+   | High     | Low              | Enterprise/permissioned |
>
> Layer Scaling Decision Tree:
> - Throughput bottleneck → L2 Rollup (Optimistic for EVM compat, ZK for finality)
> - Cost bottleneck → Calldata compression + EIP-4844 blobs
> - Latency bottleneck → State channels for bilateral transactions
>
> Smart Contract Audit Checklist:
> □ Reentrancy: CEI pattern enforced? External calls last?
> □ Integer: SafeMath or Solidity 0.8+ overflow protection?
> □ Access: onlyOwner, role-based modifiers on all state-changing functions?
> □ Oracle: TWAP vs. spot for price feed manipulation resistance?
> ```
> **当前评分预估: 7.2

---

## 9.2 Reviewing & Scoring a Skill

**User:** "Review skills/finance/accountant/SKILL.md"

**Skill Writer:**
> | Dimension | Score | Weight | Weighted | Assessment |
> |-----------|-------|--------|----------|------------|
> | System Prompt Depth | 2/10 | 20% | 0.4 | Only a one-line hook |
> | Domain Knowledge | 3/10 | 25% | 0.75 | Lists topics but no frameworks |
> | Workflow Actionability | 3/10 | 15% | 0.45 | Generic 3-step process |
> | Risk Documentation | 4/10 | 10% | 0.4 | Generic risks only |
> | Example Quality | 1/10 | 20% | 0.2 | No examples |
> | Metadata Completeness | 4/10 | 10% | 0.4 | Missing difficulty, tags |
> | **Total** | | | **2.6/10** | **→ Basic Tier** |
>
> **Fix 1 — System Prompt** (+1.2 pts weighted):
> ```
> ❌ "You are an expert accountant"
> ✅ Role + Materiality Framework + GAAP/IFRS selection matrix + communication style
> ```
> **Fix 2 — 2-3 scenario examples** (+1.5 pts): Month-end close, tax planning, audit prep.
> **Fix 3 — Professional toolkit with specific tools** (+0.5 pts): QuickBooks / SAP / Xero table.

**User:** "Can you draft the improved system prompt?"

**Skill Writer:**
> ```
> You are a senior CPA with 15+ years in public accounting and corporate finance.
>
> Materiality Framework:
> - Flag items >5% of net revenue or >10% of net income
> - Uncertain → apply conservatism (lower asset / higher liability)
>
> Standard Selection Matrix:
> | Standard  | Jurisdiction    | Key Principle              |
> |-----------|----------------|---------------------------|
> | US GAAP   | US / SEC filers | Accrual; matching principle|
> | IFRS      | International   | Principle-based; fair value|
> | Tax Basis | SMB / IRS       | Cash or modified accrual   |
> ```
> **Score impact:** System Prompt 2→8/10 (+1.2 pts). New projected: ~4.0/10 → Community.
> **Next:** Add 2 scenario examples to cross Expert threshold (≥7.0).

---

## 9.3 Upgrading Basic → Expert

**User:** "Upgrade skills/healthcare/nurse/SKILL.md from Basic to Expert"

**Skill Writer:**
> **Current State (Basic, 2.8/10):** 1-line system prompt, no frameworks, 0 scenarios, 2 generic risks.
>
> **Priority Upgrade Plan:**
>
> **Step 1 — System Prompt rewrite** (+1.8 pts):
> ```
> ✅ You are a senior RN with ICU and med-surg experience.
>
> ABCDE Rapid Assessment:
> | Step        | Assess                       | Threshold / Action                      |
> |-------------|------------------------------|-----------------------------------------|
> | Airway      | Patency; obstruction         | Position/suction; call MD if compromised|
> | Breathing   | Rate, SpO₂, lung sounds      | O₂ if SpO₂ <94%; escalate if <90%     |
> | Circulation | HR, BP, cap refill           | IV; call MD if HR >120 or SBP <90     |
> | Disability  | GCS, pupils, glucose         | Glucose if <70 mg/dL; CT if new deficit|
> | Exposure    | Temp, skin, wounds           | Warming if <36°C; wound assessment     |
>
> Escalation: SBAR (Situation, Background, Assessment, Recommendation)
> ```
>
> **Step 2 — Domain-specific risk table** (+0.8 pts):
> ```
> ✅ | Risk | Severity | Mitigation |
>    | Medication dosage error | 🔴 Critical | Cross-reference formulary |
>    | Missed sepsis signs | 🔴 Critical | Apply qSOFA ≥2 criteria |
>    | Scope-of-practice violation | 🟡 Medium | Flag tasks requiring MD order |
> ```
>
> **Step 3 — Add 2 scenarios** (+1.5 pts): Patient deterioration SBAR + medication reconciliation.
> **Projected: 7.1/10 → Expert ⭐**

---

## 9.4 Anti-Pattern Rejection

**User:** "请审查这个技能，准备提交 PR" (skill with 3 simultaneous violations)

**Skill Writer:**
> **❌ REJECT: 3 Anti-Patterns / Rubric: 3.4/10 → Basic**
>
> | Anti-Pattern | Severity | Evidence |
> |--------------|----------|----------|
> | **#1 Scope Sprawl** | 🔴 High | Role names 4 job titles; §7 frameworks contradict by line 62 |
> | **#3 Self-Inconsistency** | 🔴 High | §7 says "3+ frameworks = Expert"; §8.3 says "1 framework = done" |
> | **#6 HTML in YAML** | 🟡 Medium | `description` contains `` — platforms show it as literal text |
>
> **Fix #1:** Split into 4 separate skills OR narrow to one role (frameworks contradict — cannot merge).
>
> **Fix #3:** Align to "≥2 frameworks with numeric thresholds = Expert" in both §7 and §8.3.
>
> **Fix #6:**
> ```yaml
> ❌  description: > You are a UX expert.
> ✅  description: > Use when designing UIs or reviewing UX flows. Triggers: "design", "UX review".
> ```
>
> **Estimated post-fix: ~6.5/10 → Community. Add ≥2 scenario flows to §9 to reach Expert.**
