# Standards & Reference

## 7.1 Official Documentation

- [Sketch Documentation](https://www.sketch.com/docs/)
- [Sketch Help Center](https://www.sketch.com/help/)
- [Sketch Blog](https://www.sketch.com/blog/)
- [Sketch API Documentation](https://www.sketch.com/developers/)
- [Sketch Mac App](https://www.sketch.com/apps/)

## 7.2 Component Standards

### Symbol Naming Convention

| Type | Example | Description |
|------|---------|-------------|
| Component | `Button/Primary` | Main component |
| Variant | `Button/Primary/Hover` | State variant |
| Override | `Icon/Left` | Swap-able element |
| Style | `Text/Heading/Large` | Text style |

### Symbol Hierarchy

```
Design System
├── Components
│   ├── Buttons
│   │   ├── Button/Primary
│   │   ├── Button/Secondary
│   │   └── Button/Icon
│   ├── Inputs
│   │   ├── Input/Text
│   │   ├── Input/Search
│   │   └── Input/Select
│   └── Navigation
│       ├── NavBar
│       └── NavItem
├── Styles
│   ├── Colors
│   ├── Typography
│   └── Effects
└── Templates
    ├── Page/Default
    └── Page/Dashboard
```

## 7.3 Auto Layout Properties

| Property | Value | Description |
|----------|-------|-------------|
| Direction | Horizontal/Vertical | Stack orientation |
| Spacing | Number | Gap between elements |
| Alignment | Left/Center/Right | Content alignment |
| Distribution | None/Fill/Gap | Element distribution |
| Resizing | Hug/Fill/Fixed | Size behavior |

## 7.4 Export Settings

| Format | Suffix | Use Case |
|--------|--------|----------|
| PNG | @1x, @2x, @3x | iOS/Android |
| SVG | (none) | Web icons |
| PDF | (none) | Print |
| JPG | @2x | Photos |

## 7.5 Shortcuts Reference

| Action | Shortcut |
|--------|----------|
| New Document | ⌘+N |
| Create Symbol | ⌘+K |
| Group | ⌘+G |
| Toggle Pixel Grid | ⌘+' |
| Show Components | ⌘+J |
| Export | ⌘+⇧+E |
| Copy Style | ⌘+⌥+C |
| Paste Style | ⌘+⌥+V |

## 7.6 Version Compatibility

| Sketch Version | Features | Notes |
|---------------|----------|-------|
| 99+ | Cloud, MCP integration | Current standard |
| 95+ | Shared Libraries | Widely supported |
| 90+ | Variable Colors | Recommended |
