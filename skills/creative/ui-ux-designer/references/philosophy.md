## § 4 · Core Philosophy

### 4.1 The User-Centered Design Pyramid

```
                    ┌─────────────┐
                    │  Business   │
                    │   Goals     │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  User Needs │
                    │   & Tasks   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Functional │
                    │  Req.s      │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Interface  │
                    │  Design     │
                    └─────────────┘
```

Design decisions flow from top to bottom: business goals inform user needs, which inform functional requirements, which manifest as interface design. Violating this hierarchy creates disconnected experiences.

### 4.2 Guiding Principles

1. **Progressive Disclosure**: Show only what users need at each step. Beginners see simplified interfaces; power users get advanced options via menus or keyboard shortcuts.
2. **Affordance & Signifiers**: Make interactive elements look interactive. Buttons should look clickable; inputs should look fillable. Rely on learned conventions unless innovation is justified.
3. **Error Prevention Over Error Recovery**: Design to prevent errors before they occur. Use constraints, confirmations for destructive actions, and clear validation messages.

---

