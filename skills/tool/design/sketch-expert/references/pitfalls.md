# Common Pitfalls & Anti-Patterns

## 10.1 Component Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | Flat layer structure without naming | 🔴 High | ⌘+R to rename, ⌘+G to group |
| 2 | Copy-paste instead of symbols | 🔴 High | ⌘+K to create symbol |
| 3 | Hardcoded styles instead of shared | 🟡 Medium | Create and apply shared styles |
| 4 | Missing variant states | 🟡 Medium | Use Override panel |
| 5 | Over-nested groups | 🟡 Medium | Flatten unnecessary hierarchy |
| 6 | Detaching symbols unnecessarily | 🔴 High | Use overrides instead |

## 10.2 Layout Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | Manual positioning instead of Auto Layout | 🔴 High | Layer → Smart Layout |
| 2 | Fixed sizes instead of Hug/Fill | 🟡 Medium | Adjust resizing in right panel |
| 3 | Ignoring spacing values | 🟡 Medium | Use consistent spacing tokens |
| 4 | Mixed alignment within groups | 🟡 Medium | Set consistent alignment |

## 10.3 Collaboration Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | Duplicate symbols across files | 🔴 High | Use shared Library |
| 2 | Editing library symbols directly | 🔴 High | Override in local file |
| 3 | No naming convention | 🟡 Medium | Follow Component/Type/State pattern |
| 4 | Large shared documents | 🟡 Medium | Split into feature libraries |

## 10.4 Best Practices Checklist

```
Component Creation:
□ Use semantic naming (Component/Type/State)
□ Apply shared styles for all values
□ Configure all variant combinations
□ Add component notes
□ Publish to team Library

Auto Layout:
□ Always use Smart Layout for components
□ Set appropriate resizing behavior
□ Use consistent spacing
□ Test with various content lengths

Developer Handoff:
□ Organize in logical artboard structure
□ Name all exportable elements
□ Set proper export presets
□ Verify measurements
```

## 10.5 Security Considerations

| Concern | Mitigation |
|---------|------------|
| Sensitive data in designs | Remove before sharing |
| API keys in comments | Never include real credentials |
| User data in mockups | Use anonymized/fake data |
| Proprietary fonts | Verify licensing for export |
