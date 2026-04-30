## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **App Store Rejection** | 🔴 Critical | Violation of guidelines delays launch | Review guidelines, test with TestFlight |
| **Memory Crashes** | 🔴 Critical | OOM kills on low-end devices | Profile memory, optimize images, handle warnings |
| **Battery Drain** | 🟠 High | Excessive background activity | Optimize location, defer work, batch network |
| **Offline Breakage** | 🟠 High | App unusable without network | Offline-first architecture, queue actions |
| **Cross-Platform Limitations** | 🟡 Medium | Native features unavailable | Evaluate bridge complexity, fallback gracefully |
| **Update Friction** | 🟡 Medium | Users don't update apps | Force update for critical fixes, graceful degradation |

---
