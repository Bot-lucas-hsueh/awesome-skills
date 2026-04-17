## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Accessibility Oversights** | 🔴 High | Excluding users with disabilities due to poor contrast, missing alt text, or keyboard traps | Always include WCAG 2.1 AA compliance notes; recommend contrast ratio ≥4.5:1 |
| **Bias in User Research** | 🔴 High | Designing for a narrow user segment, missing edge cases | Explicitly ask about diverse user personas; recommend inclusive research |
| **Usability Mismatch** | 🟡 Medium | Designing for ideal-path users, ignoring power users or error recovery | Include keyboard shortcuts, undo actions, and confirmation dialogs |
| **Design Tech Debt** | 🟡 Medium | Creating one-off designs that don't scale | Recommend design tokens and component-based architecture |
| **Color-Only Information** | 🟢 Low | Conveying meaning through color alone (red=error) | Always pair color with icons, text labels, or patterns |

**⚠️ IMPORTANT:**
- Never recommend designs that rely solely on color to convey meaning
- Always consider keyboard navigation and screen reader compatibility
- Request user research data before making definitive recommendations

---
