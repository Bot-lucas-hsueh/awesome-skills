## § 10 · Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Reentrancy (The Classic Fund Drainer)

```solidity
// ❌ BAD — Vulnerable to reentrancy attack
contract VulnerableVault {
    mapping(address => uint256) public balances;

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        // External call BEFORE state update — attacker's fallback can re-enter
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        balances[msg.sender] -= amount; // State updated TOO LATE
    }
}

// ✅ GOOD — Checks-Effects-Interactions + ReentrancyGuard
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SafeVault is ReentrancyGuard {
    mapping(address => uint256) public balances;

    function withdraw(uint256 amount) external nonReentrant {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount; // State updated FIRST (Effects)
        (bool success,) = msg.sender.call{value: amount}(""); // Then Interaction
        require(success, "Transfer failed");
    }
}
```

**Why it matters:** The DAO hack (2016, $60M), Cream Finance ($130M), Euler Finance ($197M) — reentrancy is the #1 historical exploit by stolen value.

---

### Anti-Pattern 2: Single EOA Admin Key

```solidity
// ❌ BAD — One private key controls the entire protocol
contract VulnerableProtocol is Ownable {
    function setFeeRate(uint256 newRate) external onlyOwner {
        feeRate = newRate; // Single EOA can rug-pull immediately
    }
    function withdrawTreasury() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}

// ✅ GOOD — Multi-sig + Timelock governance
contract SafeProtocol is AccessControl {
    bytes32 public constant GOVERNANCE_ROLE = keccak256("GOVERNANCE_ROLE");
    ITimelockController public immutable timelock; // 48-hour delay

    constructor(address _timelockAddress) {
        // Timelock is the admin, controlled by 3-of-5 Gnosis Safe
        _grantRole(GOVERNANCE_ROLE, _timelockAddress);
    }

    function setFeeRate(uint256 newRate) external onlyRole(GOVERNANCE_ROLE) {
        require(newRate <= MAX_FEE, "Fee too high");
        feeRate = newRate;
    }
}
```

**Why it matters:** A compromised private key with no timelock means instant protocol takeover and fund drainage. Badger DAO ($120M), Ronin Bridge ($625M) — admin key compromise is consistently catastrophic.

---

### Anti-Pattern 3: Block.timestamp

```solidity
// ❌ BAD — Miner-manipulable randomness
contract VulnerableLottery {
    function pickWinner() external {
        // Miners can choose to include/exclude their block to manipulate this
        uint256 rand = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)));
        address winner = participants[rand % participants.length];
        payable(winner).transfer(address(this).balance);
    }
}

// ✅ GOOD — Chainlink VRF for verifiable randomness
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract SafeLottery is VRFConsumerBaseV2 {
    VRFCoordinatorV2Interface COORDINATOR;

    function requestWinner() external returns (uint256 requestId) {
        requestId = COORDINATOR.requestRandomWords(
            keyHash, subscriptionId, 3, // 3 confirmations
            callbackGasLimit, 1         // 1 random word
        );
    }

    function fulfillRandomWords(uint256, uint256[] memory randomWords) internal override {
        address winner = participants[randomWords[0] % participants.length];
        payable(winner).transfer(address(this).balance);
    }
}
```

**Why it matters:** Predictable randomness allows miners and bots to game NFT mints, lotteries, and any game theory system that relies on "random" on-chain values.

---

### Anti-Pattern 4: Unbounded Loop (Gas Griefing

```solidity
// ❌ BAD — O(n) loop over unbounded array can hit block gas limit
contract VulnerableDistributor {
    address[] public recipients;

    function distributeRewards() external {
        for (uint256 i = 0; i < recipients.length; i++) {
            // If recipients grows large enough, this reverts due to gas limit
            payable(recipients[i]).transfer(rewards[recipients[i]]);
        }
    }
}

// ✅ GOOD — Pull-over-push pattern with per-user claims
contract SafeDistributor {
    mapping(address => uint256) public pendingRewards;

    // Each user pulls their own reward — no loop, no DoS vector
    function claimReward() external {
        uint256 reward = pendingRewards[msg.sender];
        require(reward > 0, "Nothing to claim");
        pendingRewards[msg.sender] = 0;
        payable(msg.sender).transfer(reward);
    }
}
```

**Why it matters:** Push payment patterns over unbounded arrays let a single actor add enough recipients to permanently brick the distribution function, locking funds forever.

---

### Anti-Pattern 5: tx.origin Authentication

```solidity
// ❌ BAD — Phishing-vulnerable authentication
contract VulnerableWallet {
    address public owner;

    function transfer(address payable dest, uint256 amount) external {
        // tx.origin is the original EOA — a malicious contract in the middle
        // can trick the owner into calling it, which then calls this function
        require(tx.origin == owner, "Not owner");
        dest.transfer(amount);
    }
}

// ✅ GOOD — msg.sender is always the direct caller
contract SafeWallet {
    address public owner;

    function transfer(address payable dest, uint256 amount) external {
        require(msg.sender == owner, "Not owner");
        dest.transfer(amount);
    }
}
```

**Why it matters:** If a user is tricked into calling a malicious contract, that contract can call `tx.origin`-authenticated functions on their behalf, draining their wallet without explicit approval.

---

### Anti-Pattern 6: Insufficient Slippage

```solidity
// ❌ BAD — No slippage protection on AMM interaction
contract VulnerableRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        address[] calldata path
    ) external {
        // No minAmountOut — sandwich bots extract maximum value
        uint256 amountOut = _swap(amountIn, path);
        IERC20(path[path.length-1]).transfer(msg.sender, amountOut);
    }
}

// ✅ GOOD — Caller specifies acceptable slippage; deadline prevents stale execution
contract SafeRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,   // Caller sets minimum acceptable output
        address[] calldata path,
        uint256 deadline        // Prevents transaction from executing after market moves
    ) external {
        require(block.timestamp <= deadline, "Transaction expired");
        uint256 amountOut = _swap(amountIn, path);
        require(amountOut >= amountOutMin, "Insufficient output amount");
        IERC20(path[path.length-1]).transfer(msg.sender, amountOut);
    }
}
```

**Why it matters:** Without slippage limits, MEV bots sandwich every large trade — buying before, selling after — extracting the value that should belong to the user. This is not theoretical; MEV extraction runs hundreds of millions of dollars per year.

