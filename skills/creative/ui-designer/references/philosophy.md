## § 4 · Core Philosophy

### 4.1 Design Token Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│  DESIGN TOKEN SYSTEM                                        │
│                                                             │
│  FOUNDATION (Primitives)                                    │
│  ├── Color: #007AFF, #34C759, #FF3B30, etc.                │
│  ├── Typography: Inter, 16px/1.5, 400/600/700              │
│  ├── Spacing: 4px, 8px, 16px, 24px, 32px, 48px             │
│  ├── Border radius: 4px, 8px, 16px, 9999px                 │
│  └── Shadows: 0 1px 3px rgba(0,0,0,0.1)                    │
│                                                             │
│  SEMANTIC (Contextual)                                      │
│  ├── Primary: $color-blue-500                              │
│  ├── Success: $color-green-500                             │
│  ├── Text primary: $color-gray-900                         │
│  └── Surface elevated: $shadow-medium                      │
│                                                             │
│  COMPONENT (Applied)                                        │
│  ├── Button bg: $primary                                   │
│  ├── Button text: $white                                   │
│  └── Button radius: $radius-medium                         │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Clarity Over Decoration**: Every visual element should serve a purpose; remove purely decorative noise
2. **Consistency Builds Trust**: Users learn patterns; maintain consistency within and across products
3. **Typography is UI**: Type choices convey hierarchy, tone, and functionality
4. **Space is a Design Element**: Whitespace improves comprehension and guides attention
5. **Design for the Extremes**: Test designs with minimum and maximum content, screen sizes, and user needs

---
