## § 8 · Standard Workflow

### Phase 1: Protocol Design and Architecture

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | Define use case and determine public/private/consortium blockchain fit | Platform selected with documented rationale | Platform chosen without requirements analysis |
| 2 | Design token model and economic incentives | Tokenomics simulation completed; no obvious attack vectors | Inflationary spiral or centralization risk in model |
| 3 | Architect smart contract system with module boundaries | Contract dependency diagram complete; no circular dependencies | Monolithic contract with excessive complexity |
| 4 | Design access control and admin key management | Multi-sig and timelock strategy documented | Single EOA holds admin privileges |
| 5 | Define upgrade strategy (immutable vs proxy) | Upgrade pattern documented with justification | No upgrade plan for a system likely to need changes |

### Phase 2: Development, Audit, and Deployment

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | Implement contracts with full test coverage | >95% branch coverage; all edge cases tested | Test coverage below 90% |
| 2 | Internal security review (automated + manual) | Slither/Echidna pass; manual review of all state changes | Known vulnerability class present |
| 3 | Third-party audit by reputable firm | Audit report received; all Critical/High findings resolved | Deploying with unresolved High severity findings |
| 4 | Testnet deployment and integration testing | Full protocol tested on testnet under load | Skipping testnet phase |
| 5 | Mainnet deployment with monitoring | On-chain monitoring (Forta, OpenZeppelin Defender) active | No incident response plan or monitoring |

