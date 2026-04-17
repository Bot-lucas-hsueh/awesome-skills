## § 7 · Standards & Reference

### ERC/EIP Standards Table

| Standard | Name | Use Case | Key Security Considerations |
|----------|------|----------|-----------------------------|
| ERC-20 | Fungible Token | Governance tokens, stablecoins, utility tokens | Approve/transferFrom reentrancy; use safeTransfer; beware fee-on-transfer tokens in DeFi |
| ERC-721 | Non-Fungible Token | Unique digital assets, identity, deeds | onERC721Received callback reentrancy; validate ownerOf before transfer |
| ERC-1155 | Multi-Token Standard | Game items, mixed fungible/non-fungible batches | Batch transfer callbacks; ensure safeBatchTransferFrom respects balances |
| ERC-4337 | Account Abstraction | Smart wallets, gasless UX, session keys | UserOperation validation must be deterministic; paymaster abuse vectors |
| EIP-1559 | Fee Market Reform | Base fee + priority tip; predictable gas costs | maxFeePerGas must exceed baseFee for inclusion; not applicable in L2s uniformly |
| EIP-2612 | Permit (Gasless Approvals) | Off-chain signed ERC-20 approvals | Signature replay across chains; always include chainId + nonce + deadline |

### Common Vulnerability Classes (SWC Registry)

```
SWC-107 — Reentrancy              (use checks-effects-interactions pattern)
SWC-101 — Integer Overflow        (use SafeMath or Solidity 0.8+)
SWC-105 — Unprotected SELFDESTRUCT (restrict to authorized callers only)
SWC-115 — tx.origin Authentication (use msg.sender, never tx.origin)
SWC-116 — Block values as time source (dangerous for randomness)
SWC-136 — Unencrypted Private Data (all on-chain data is public)
```

### Upgrade Patterns

```
Transparent Proxy Pattern   → OpenZeppelin TransparentUpgradeableProxy
UUPS (Universal Upgradeable) → More gas efficient, logic in implementation
Diamond Pattern (EIP-2535)  → Multi-facet, fine-grained upgradeability
Immutable Deployment        → No upgrade path; maximum trustlessness
```

### Protocol Quality Metrics

**TVL Thresholds (Risk-Gated Deployment):**

| TVL Range | Required Security Measures |
|-----------|---------------------------|
| < $100K (testnet
| $100K – $1M | One professional audit; bug bounty program |
| $1M – $10M | Two independent audits; formal verification of critical paths |
| $10M – $100M | Multiple audits; economic simulation; guardian multisig; Forta monitoring |
| > $100M | Continuous audit retainer; formal verification of all contracts; insurance coverage |

**Audit Coverage Targets:**

| Contract Type | Minimum Branch Coverage | Fuzzing Runs | Formal Verification |
|---------------|------------------------|--------------|---------------------|
| ERC-20 token | 95% | 10,000 | Optional |
| Lending/AMM core | 98% | 100,000 | Required (invariants) |
| Bridge
| ZK verifier contract | 100% | N/A (circuit-level) | Required (soundness) |

**Gas Optimization Targets:**

| Operation | Current Baseline | Target (Optimized) | Technique |
|-----------|-----------------|-------------------|-----------|
| ERC-20 transfer | ~65,000 gas | ~35,000 gas | Pack storage slots; use events not storage for history |
| AMM swap | ~130,000 gas | ~80,000 gas | Minimize SLOADs; cache storage reads in memory |
| NFT mint | ~150,000 gas | ~70,000 gas | ERC-721A batch mint; bitmap storage for balances |
| Governance vote | ~80,000 gas | ~45,000 gas | Snapshot off-chain; only finalize on-chain |

**Gas Cost Reference (Ethereum):**

```
SSTORE (cold write):  20,000 gas
SLOAD (cold read):    2,100 gas
CALL:                 100 gas base
LOG (32 bytes):       ~750 gas
ERC-20 Transfer:      ~65,000 gas
Uniswap V3 Swap:      ~130,000 gas
```

