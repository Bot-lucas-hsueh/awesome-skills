# Common Pitfalls & Anti-Patterns

## 10.1 Component Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | Flat layer structure without naming | 🔴 High | ⌘+R to rename, ⌘+G to group |
| 2 | Using frames instead of components | 🔴 High | Right-click → Create Component |
| 3 | Hardcoded colors instead of variables | 🟡 Medium | Create and apply color tokens |
| 4 | Missing variant states | 🟡 Medium | Add variant properties |
| 5 | Over-nested groups | 🟡 Medium | Flatten unnecessary hierarchy |
| 6 | Using Detach on instances | 🔴 High | Use overrides instead |

## 10.2 Layout Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | Manual positioning instead of Auto Layout | 🔴 High | Select → Auto Layout (⌘+Shift+A) |
| 2 | Fixed widths instead of Hug/Fill | 🟡 Medium | Change resizing in right panel |
| 3 | Ignoring spacing tokens | 🟡 Medium | Apply spacing tokens |
| 4 | Mixed alignment within groups | 🟡 Medium | Set consistent alignment |

## 10.3 Collaboration Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | Duplicate components across files | 🔴 High | Use shared library |
| 2 | Direct editing of library components | 🔴 High | Override in local file |
| 3 | No component documentation | 🟡 Medium | Add notes and examples |
| 4 | Large shared files | 🟡 Medium | Split into feature libraries |

## 10.4 Best Practices Checklist

```
Component Creation:
□ Use semantic naming (Component/Type/State)
□ Apply design tokens for all values
□ Configure all variant combinations
□ Add component documentation
□ Publish to team library

Auto Layout:
□ Always use Auto Layout for components
□ Set appropriate resizing behavior
□ Use spacing tokens for gaps
□ Test with various content lengths

Developer Handoff:
□ Organize in Dev Mode sections
□ Name all exportable elements
□ Set proper export presets
□ Verify measurements in Dev Mode
```

## 10.5 Security Considerations

| Concern | Mitigation |
|---------|------------|
| Sensitive data in designs | Remove before sharing |
| API keys in comments | Never include real credentials |
| User data in mockups | Use anonymized/fake data |
| Proprietary fonts | Verify licensing for export |
