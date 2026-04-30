# Standards & Reference

## 7.1 Official Documentation

- [Figma Documentation](https://help.figma.com/hc/en-us) - Official help center
- [Figma Design Handbook](https://www.figma.com/best-practices/) - Best practices guide
- [Figma Community](https://www.figma.com/community) - Templates and plugins
- [Dev Mode Documentation](https://help.figma.com/hc/en-us/sections/4405269443991-Dev-Mode) - Developer handoff

## 7.2 Component Standards

### Design Token Structure

| Token Type | Example | Usage |
|------------|---------|-------|
| Color | `color/brand/primary` | `#2563EB` |
| Typography | `typography/body/small` | Inter 14px |
| Spacing | `spacing/component/padding` | 16px |
| Border | `border/radius/small` | 8px |

### Component Naming Convention

```
Component/Variant/State
Button/Primary/Default
Button/Primary/Hover
Button/Secondary/Disabled
```

## 7.3 Auto Layout Properties

| Property | Values | Description |
|----------|--------|-------------|
| Direction | Horizontal, Vertical | Stack orientation |
| Spacing | Number (px) | Gap between elements |
| Padding | Number (px) | Inner margins |
| Alignment | Start, Center, End, Stretch | Content alignment |
| Resizing | Hug Contents, Fill Container | Size behavior |

## 7.4 Version Compatibility

| Figma Version | Features | Notes |
|---------------|----------|-------|
| 2023+ | Dev Mode, Variables | Current standard |
| 2022+ | Component properties, Variants | Widely supported |
| 2021+ | Auto Layout 3.0 | Minimum recommended |

## 7.5 Export Settings

| Format | Suffix | Use Case |
|--------|--------|----------|
| PNG | `@1x`, `@2x`, `@3x` | iOS/Android apps |
| SVG | (none) | Web icons, vectors |
| PDF | (none) | Print, complex vectors |
| JPG | `@2x` | Photography, backgrounds |

## 7.6 Figma API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/files/:key` | GET | Get file data |
| `/v1/files/:key/components` | GET | Get component library |
| `/v1/images/:key` | GET | Export images |
| `/v1/comments` | GET/POST | Manage comments |
