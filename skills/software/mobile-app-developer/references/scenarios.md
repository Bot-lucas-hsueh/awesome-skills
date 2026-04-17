## § 8 · Scenario Examples

### Example 1: Social Media App

**Context**: Instagram-like photo sharing app with feed, camera, and messaging.

**Implementation**:
```
Platform: React Native (shared codebase)
Key Features:
├── Camera integration with real-time filters
├── Feed with infinite scroll and image caching
├── Push notifications for likes/messages
├── Offline support for viewing cached content

Performance Optimizations:
├── Image lazy loading with progressive quality
├── List virtualization for 1000+ items
├── Background upload with retry
├── 60fps animations using native driver
```

---

### Example 2: Fitness Tracking App

**Context**: Strava-like activity tracker with GPS, heart rate, and analytics.

**Implementation**:
```
Platform: Native iOS (Swift) + Android (Kotlin)
Key Features:
├── GPS tracking with battery optimization
├── HealthKit/Google Fit integration
├── Background activity recording
├── Real-time stats during workout

Challenges:
├── Battery: GPS throttled when screen off
├── Data: 100MB+ activity history cached locally
├── Sync: Conflict resolution for simultaneous devices
├── Accuracy: GPS filtering for noisy signals
```

---

### Example 3: E-commerce Shopping App

**Context**: Mobile shopping with catalog, cart, checkout, and order tracking.

**Implementation**:
```
Platform: Flutter (single codebase)
Architecture:
├── BLoC pattern for state management
├── Hive for local cart persistence
├── Stripe SDK for payments
├── Push notifications for order updates

Features:
├── Barcode scanner for in-store lookup
├── Wishlist with offline access
├── AR product preview (Flutter ARCore/ARKit)
├── Biometric authentication for checkout
```

---

### Example 4: Enterprise Field Service App

**Context**: App for technicians to manage work orders offline, sync when connected.

**Implementation**:
```
Platform: Native (separate iOS/Android)
Offline-First Design:
├── Work orders cached in Core Data/Room
├── Photo attachments with background upload
├── Signature capture stored locally
├── Sync queue with conflict resolution

Enterprise Integration:
├── Azure AD authentication
├── Intune MDM for device management
├── Certificate pinning for security
├── Audit logging for compliance
```

---

### Example 5: App Migration (Native to Flutter)

**Context**: Migrate legacy native apps to Flutter for unified codebase.

**Migration Strategy**:
```
Approach: Strangler Fig (module by module)
├── Phase 1: Add Flutter to existing apps (add-to-app)
├── Phase 2: Migrate non-critical screens first
├── Phase 3: Feature parity testing
├── Phase 4: Remove native code, pure Flutter

Challenges:
├── Native plugins: Rewrite or use existing
├── State management: Provider vs. native patterns
├── Testing: New test suite, device farm
├── Team: Training, best practices documentation
```

---
