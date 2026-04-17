## § 9 · Scenario Examples

### Scenario A: DeFi Lending Protocol Architecture

**Request:** Design the smart contract architecture for a collateralized lending protocol supporting ETH, wBTC, and stablecoins.

**Architecture:**

```solidity
// Core contract structure

// 1. LendingPool.sol — Main entry point
contract LendingPool {
    // Deposits, borrows, repays, liquidations
    // Delegates to: InterestRateModel, PriceOracle, LiquidationEngine

    mapping(address => mapping(address => UserPosition)) positions;

    function deposit(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
    function liquidate(address user, address collateral, address debt) external;
}

// 2. InterestRateModel.sol — Utilization-based rates
contract InterestRateModel {
    // Kinked rate model: low rate at low utilization, spike above optimal
    function getBorrowRate(uint256 utilization) external view returns (uint256);
}

// 3. PriceOracle.sol — Chainlink + TWAP fallback
contract PriceOracle {
    // Primary: Chainlink price feeds
    // Fallback: Uniswap V3 TWAP (30min window)
    // Circuit breaker: reject if deviation > 5% between sources
}

// 4. LiquidationEngine.sol — Health factor monitoring
contract LiquidationEngine {
    // Liquidation triggered when health factor < 1.0
    // 5% liquidation bonus incentivizes liquidators
    // Partial liquidation up to 50% of position
}

// Security features:
// - ReentrancyGuard on all state-changing functions
// - Pausable with multi-sig governance
// - 48-hour timelock on parameter changes
// - Emergency withdrawal without timelock
```

**Key Decisions:**
- Separate oracle contract enables oracle upgrade without main pool change
- Timelock prevents governance attacks with rapid parameter changes
- Partial liquidation preserves user equity and reduces bad debt risk

---

### Scenario B: NFT Marketplace Smart Contract Review

**Review Request:** Audit this OpenSea-style marketplace contract for security issues.

**Common Findings:**

```solidity
// VULNERABLE: Missing reentrancy protection
function fulfillOrder(Order memory order) external payable {
    // BAD: External call before state update
    payable(order.seller).transfer(order.price); // <-- reentrancy risk
    orders[order.id].fulfilled = true;           // state updated AFTER call
}

// FIXED: Checks-Effects-Interactions pattern
function fulfillOrder(Order memory order) external payable nonReentrant {
    orders[order.id].fulfilled = true;           // state updated FIRST
    payable(order.seller).transfer(order.price); // then external call
}
```

**Additional findings:** Verify royalty enforcement cannot be bypassed via custom transfer implementations; ensure signature replay protection includes chainId and nonce; validate that approval patterns cannot drain wallets beyond listed items.

---

### Scenario C: Enterprise Consortium Blockchain Selection

A consortium of 12 financial institutions wants to share trade finance data. Requirements: permissioned access, transaction privacy between parties, 1,000 TPS throughput, regulatory auditability.

**Recommendation: Hyperledger Fabric.** Reasons: (1) Channel architecture provides transaction privacy between subsets of participants, (2) Permissioned membership via MSP (Membership Service Provider), (3) Pluggable consensus (RAFT for CFT), (4) No native token or gas costs, (5) Enterprise tooling and IBM support ecosystem. Alternative: Corda for more complex financial contract modeling with explicit legal prose attachment.

---

### Scenario D: ZK-Proof Privacy System Design

**Request:** Design a privacy-preserving payment system where transaction amounts and recipient addresses are hidden from on-chain observers, while still being verifiable by the network.

**Architecture Overview:**

The system uses a UTXO-based commitment scheme with Groth16 proofs (similar to Zcash's Sapling), deployed as verifier contracts on Ethereum with a shielded pool.

```solidity
// ShieldedPool.sol — Core privacy contract

contract ShieldedPool {
    using IncrementalMerkleTree for MerkleTree;

    // Merkle tree of UTXO commitments (Pedersen hashes)
    MerkleTree public commitments;

    // Nullifier set — prevents double-spending without revealing which note was spent
    mapping(bytes32 => bool) public nullifiers;

    // Groth16 verifier (generated from circuit compilation)
    IVerifier public immutable verifier;

    event NewCommitment(bytes32 indexed commitment, uint256 leafIndex, bytes encryptedNote);
    event Nullified(bytes32 indexed nullifier);

    /// @notice Deposit ETH into the shielded pool
    /// @param commitment  Pedersen hash of (amount, secret, nullifierKey)
    function shield(bytes32 commitment) external payable {
        require(msg.value > 0, "Must deposit nonzero amount");
        uint256 leafIndex = commitments.insert(commitment);
        // Note encrypted to recipient's public key — only recipient can decrypt
        emit NewCommitment(commitment, leafIndex, "");
    }

    /// @notice Transfer within the shielded pool (amount and recipient hidden)
    /// @param proof       Groth16 proof bytes
    /// @param publicInputs [merkleRoot, nullifier, newCommitment, feeCommitment]
    function shieldedTransfer(
        bytes calldata proof,
        bytes32[4] calldata publicInputs
    ) external {
        bytes32 merkleRoot    = publicInputs[0];
        bytes32 nullifier     = publicInputs[1];
        bytes32 newCommitment = publicInputs[2];

        require(commitments.isKnownRoot(merkleRoot), "Unknown Merkle root");
        require(!nullifiers[nullifier], "Note already spent");
        require(verifier.verify(proof, publicInputs), "Invalid ZK proof");

        nullifiers[nullifier] = true;
        commitments.insert(newCommitment);

        emit Nullified(nullifier);
        emit NewCommitment(newCommitment, commitments.count() - 1, "");
    }

    /// @notice Withdraw from shielded pool back to public address
    function unshield(
        bytes calldata proof,
        bytes32[3] calldata publicInputs,
        address payable recipient,
        uint256 amount
    ) external {
        bytes32 merkleRoot = publicInputs[0];
        bytes32 nullifier  = publicInputs[1];

        require(commitments.isKnownRoot(merkleRoot), "Unknown Merkle root");
        require(!nullifiers[nullifier], "Note already spent");
        require(verifier.verify(proof, publicInputs), "Invalid ZK proof");

        nullifiers[nullifier] = true;
        emit Nullified(nullifier);

        recipient.transfer(amount);
    }
}
```

**ZK Circuit Design (Circom pseudocode):**

```
// transfer.circom — proves knowledge of a valid note without revealing it
template ShieldedTransfer() {
    // Private inputs (known only to prover)
    signal private input amount;
    signal private input secret;
    signal private input nullifierKey;
    signal private input merklePathElements[20];
    signal private input merklePathIndices[20];

    // Public inputs (visible on-chain)
    signal input merkleRoot;
    signal input nullifier;
    signal input newCommitment;

    // Constraints:
    // 1. Commitment = PedersenHash(amount, secret, nullifierKey)
    // 2. Nullifier  = PoseidonHash(nullifierKey, leafIndex)
    // 3. MerklePath proves commitment is in tree with given root
    // 4. newCommitment = PedersenHash(newAmount, newSecret, newNullifierKey)
    // 5. amount == newAmount (conservation of value, no minting)
}
```

**Key Design Decisions:**

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Proof system | Groth16 | Smallest proof size (128 bytes), cheapest on-chain verification (~300K gas) |
| Hash function | Poseidon | ZK-friendly; 10x cheaper in circuits vs Keccak |
| Merkle tree depth | 20 levels | Supports 2^20 (~1M) notes before tree is full |
| Trusted setup | Powers of Tau (multi-party) | Ceremony with 100+ participants; secure if 1-of-N honest |
| Note encryption | ECDH + AES-256-GCM | Recipient derives shared secret from sender's ephemeral key |
| Regulatory compliance | View key mechanism | Auditor can be given view key to decrypt all notes without spending ability |

**Security Considerations:**
- Circuit soundness must be formally verified — a single missing constraint allows forged proofs and arbitrary minting
- The Merkle tree must use append-only insertion to prevent root manipulation
- Nullifier set must be append-only; never delete nullifiers
- Trusted setup ceremony transcript must be publicly verifiable
- Relayer network (for gas abstraction) must not be able to front-run or selectively censor withdrawals

