## § 4 · Core Philosophy

### 4.1 Mobile Architecture Model

```
┌─────────────────────────────────────────┐
│           UI Layer                      │  ← SwiftUI/Jetpack Compose/Flutter
├─────────────────────────────────────────┤
│        Presentation Layer               │  ← ViewModels, State Management
├─────────────────────────────────────────┤
│         Domain Layer                    │  ← Use Cases, Business Logic
├─────────────────────────────────────────┤
│         Data Layer                      │  ← Repositories, API Clients
├─────────────────────────────────────────┤
│      Local / Remote Data                │  ← Core Data/Room, REST/GraphQL
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Offline-First** — Core features work without network; sync happens in background
2. **Performance Budgets** — 60fps, 2s launch, < 100MB size targets
3. **Platform Conventions** — Match user expectations for each platform
4. **Battery Respect** — Minimize background work and location usage
5. **Defensive Design** — Handle crashes gracefully, degrade features when needed

---
