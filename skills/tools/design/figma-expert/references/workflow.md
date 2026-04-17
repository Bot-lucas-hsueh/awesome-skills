# Standard Workflow

## 8.1 Component Design Workflow

```
Phase 1: Foundation
├── Define design tokens (colors, typography, spacing)
├── Create color variables in Figma
└── Set up typography styles

Phase 2: Base Components
├── Design atoms: Button, Input, Badge, Icon
├── Apply Auto Layout
└── Create component variants

Phase 3: Composite Components
├── Combine atoms into molecules
├── Card, Modal, Navigation, Form
└── Test responsive behavior

Phase 4: Documentation
├── Add usage guidelines in component notes
├── Create example frames
└── Publish to team library
```

## 8.2 Developer Handoff Workflow

```
Step 1: Organize Layers
├── Name all layers meaningfully
├── Group related elements
└── Lock guide elements

Step 2: Create Sections
├── Organize frames by feature/screen
├── Add section labels
└── Ensure Dev Mode visibility

Step 3: Export Preparation
├── Add slices for exportable elements
├── Set export presets
└── Configure asset delivery options

Step 4: Handoff Review
├── Use Dev Mode inspection
├── Verify spacing and measurements
└── Provide CSS/code specs
```

## 8.3 Design System Maintenance

| Task | Frequency | Tool |
|------|-----------|------|
| Token updates | As needed | Variables panel |
| Component review | Monthly | Branch workflow |
| Library publish | Release-based | Version history |
| Deprecate old components | Quarterly | Archive strategy |

## 8.4 Collaboration Workflow

| Role | Action | Tool |
|------|--------|------|
| Designer | Create/update components | Figma Editor |
| Designer | Request review | Comments |
| Developer | Inspect specs | Dev Mode |
| Developer | Export assets | Asset panel |
| PM | Verify acceptance criteria | Comments |
