## 2. CrowdStrike Company Context

### Corporate Profile
| Attribute | Details |
|-----------|---------|
| **Founded** | 2011, Irvine, California |
| **Headquarters** | Austin, Texas (strong remote-first culture) |
| **CEO** | George Kurtz (co-founder, ex-McAfee Worldwide CTO, founded Foundstone) |
| **Employees** | 10,000+ (FY2025) |
| **Revenue** | $3.95B FY2025 (29% YoY growth) |
| **ARR** | $4.24B (23% YoY growth) |
| **Market Cap** | $80B-$130B range |
| **Stock** | CRWD (NASDAQ, IPO 2019) |
| **Gross Retention** | 97% (industry-leading) |

### Key Leadership
- **George Kurtz**: CEO & Co-founder. Former McAfee Worldwide CTO, founded Foundstone (acquired 2004). Authored "Hacking Exposed" (best-selling security book).
- **Michael Sentonas**: President (former CTO). Leads product, engineering, and go-to-market.
- **Shawn Henry**: Chief Security Officer. Former FBI Executive Assistant Director.

### The Falcon Platform
Cloud-native security platform with **30+ cloud modules** delivering:
- **Endpoint Protection**: Next-gen AV, EDR, XDR, firewall management
- **Cloud Security**: CNAPP (CSPM + CWP + CIEM), container security, IaC scanning
- **Identity Protection**: Zero Trust, AD/Azure AD security, risk-based MFA
- **Security Operations**: Next-Gen SIEM (LogScale), SOAR, threat intelligence
- **Managed Services**: Falcon Complete MDR, OverWatch threat hunting

### July 19, 2024 Incident: Lessons Learned
The largest IT outage in history—**8.5 million Windows devices** crashed globally due to a faulty Channel File 291 sensor configuration update.

**Root Cause:**
- Logic error in Channel File 291 (named pipe execution evaluation)
- Out-of-bounds memory read in CSagent.sys kernel driver
- Data field mismatch: expected 21 fields, received 20
- Immediate global deployment without staged rollout

**Timeline:**
| Time (UTC) | Event |
|------------|-------|
| 04:09 | Faulty update deployed |
| 04:30 | First crash reports |
| 05:27 | Issue identified, update rolled back |
| 06:00+ | Manual remediation began worldwide |

**Impact:**
- $5B+ losses for Fortune 500 companies
- 24,000+ flight cancellations
- Healthcare systems disrupted
- Banking/trading delays
- CrowdStrike stock dropped 45% (recovered to all-time highs within 4 months)

**Lessons & Improvements:**
- ✅ Staged rollout procedures (canary → pilot → production)
- ✅ Enhanced QA/testing for sensor content updates
- ✅ Rapid rollback capabilities
- ✅ Improved customer communication protocols
- ✅ Kernel driver stability reviews with Microsoft
