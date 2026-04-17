## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重程度 | Domain Consequence / 领域后果 | Mitigation
|------------|--------------------|-----------------------------|---------------------|
| **Motion Sickness / 晕动症** | HIGH | >40% untrained users experience sickness from VR; can cause vomiting and disorientation lasting hours | Keep angular velocity <30°/s, use comfort vignetting, avoid artificial locomotion without teleportation option |
| **Eye Strain & Vergence-Accommodation Conflict / 视觉疲劳** | HIGH | Extended AR/VR use causes headaches, blurred vision, and long-term visual fatigue in vergence-accommodation mismatch designs | Limit sessions to 20–30 min, set UI at 1.5m+ depth, avoid rapid depth changes |
| **Physical Collision Risk / 物理碰撞风险** | HIGH | Users immersed in VR cannot see real-world obstacles; falls and collisions cause injury | Mandatory Guardian/Boundary system, minimum 2×2m play area, real-world passthrough option |
| **Privacy & Camera Data
| **Platform API Breaking Changes / 平台API重大变更** | MEDIUM | ARKit/ARCore APIs change with OS releases; apps can break silently after system updates | Pin SDK versions, run regression suite on beta OS, test with fallback detection for deprecated APIs |
| **Accessibility Gaps
| **Content Security in Shared Spaces

---
