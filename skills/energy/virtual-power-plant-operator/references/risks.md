## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Forecast Error** | 🔴 High | Load/generation forecast errors cause balancing costs and penalties | Use ensemble forecasts; maintain backup resources; size reserves |
| **Market Price Volatility** | 🔴 High | Real-time prices can go negative or spike 10x; VPP margin erosion | Hedge with forwards; limit real-time exposure; optimize DA vs RT |
| **DER Non-Performance** | 🔴 High | Aggregated DERs fail to deliver committed capacity; financial penalties | Secure backup resources; verify telemetry; enforce performance contracts |
| **Grid Constraint Violation** | 🔴 High | Dispatch causing frequency deviation or thermal overload | Apply grid constraints in dispatch; coordinate with ISO/TSO |
| **Communication Failure** | 🟡 Medium | DER communication loss prevents dispatch | Implement redundant communication; local DER autonomy |
| **Regulatory Changes** | 🟡 Market rules, incentives, or interconnection requirements change | Monitor regulatory filings; diversify revenue streams |
| **Cybersecurity** | 🟡 Medium | VPP control systems vulnerable to attack | Implement IEC 62351; network segmentation; access controls |

**⚠️ IMPORTANT**:
- VPP operations involve financial risk. Always verify market rules and settlement terms before trading.

- Grid services require precise response. Incorrect frequency response can cause grid instability.

---
