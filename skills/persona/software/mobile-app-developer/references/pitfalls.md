## § 9 · Common Pitfalls

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Main Thread Blocking** | UI freezes, ANR/crash | Move work to background queues |
| **Memory Leaks** | Retain cycles, OOM crashes | Weak references, proper cleanup |
| **Over-Requesting Permissions** | Users deny, app limited | Request only when needed |
| **Ignoring Accessibility** | App unusable for disabled | VoiceOver/TalkBack testing |
| **No Offline Handling** | App broken without network | Cache critical data, queue actions |
| **Hardcoded Strings** | Localization impossible | String resources from day one |

---
