# UI Designer - Standards & References

## Design Token Structure

### Foundation (Primitives)
- Colors: Brand palette, semantic colors, neutrals
- Typography: Font families, sizes, weights, line heights
- Spacing: Base unit (usually 4px or 8px), scale
- Elevation: Shadows, z-index layers
- Border: Widths, radii, styles

### Semantic (Contextual)
- $color-primary: Brand main color
- $color-success: Positive actions
- $color-error: Errors and warnings
- $text-primary: Main text color
- $surface-elevated: Card/modal backgrounds

## WCAG Color Contrast

| Usage | Minimum Ratio | Enhanced |
|-------|---------------|----------|
| Normal text | 4.5:1 | 7:1 |
| Large text | 3:1 | 4.5:1 |
| UI components | 3:1 | - |

## Typography Scale (Major Third - 1.25)

| Token | Size | Line Height | Usage |
|-------|------|-------------|-------|
| text-4xl | 48px | 56px | Display |
| text-3xl | 38px | 46px | H1 |
| text-2xl | 30px | 38px | H2 |
| text-xl | 24px | 32px | H3 |
| text-lg | 20px | 28px | H4 |
| text-base | 16px | 24px | Body |
| text-sm | 14px | 20px | Small |
| text-xs | 12px | 16px | Caption |

## Platform Guidelines

- iOS: Human Interface Guidelines
- Android: Material Design
- Web: Tailwind CSS, Bootstrap patterns

## Resources

| Resource | URL |
|----------|-----|
| Refactoring UI | refactoringui.com |
| Design Systems | designsystems.com |
| UI8 | ui8.net |
| Mobbin | mobbin.com |
