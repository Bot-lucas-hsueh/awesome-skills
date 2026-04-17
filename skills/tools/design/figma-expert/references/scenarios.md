# Scenario Examples

## 9.1 Building a Reusable Button Component

**User:** "Create a button component with primary, secondary, and disabled states"

**Figma Expert:**
> **Component Structure:**
>
> | Element | Property | Value |
> |---------|----------|-------|
> | Frame | Auto Layout | Horizontal, 8px spacing |
> | Background | Fill | `color/button/primary` |
> | Corner Radius | Rounded | 8px |
> | Text | Typography | `typography/button/default` |
> | Padding | Fixed | 16px horizontal, 12px vertical |
>
> **Variants Setup:**
> 1. Create component with `Button` name
> 2. Add variant property: `Type` (Primary, Secondary, Ghost)
> 3. Add variant property: `State` (Default, Hover, Pressed, Disabled)
> 4. Configure property value combinations
>
> **Override Configuration:**
> - Text content (Text property)
> - Icon position (Instance Swap)
> - Loading spinner visibility

## 9.2 Responsive Card Design

**User:** "Design a card that adapts to different content lengths"

**Figma Expert:**
> **Smart Layout Configuration:**
> 1. Create card frame with Auto Layout (Vertical)
> 2. Set image layer: Fixed height 200px
> 3. Set content container:
>    - Top pinning for title
>    - Hugging priority for description
>    - Full width
> 4. Set action area: Bottom pinning
> 5. Test with: short text, long text, no image
>
> **Resizing Behavior:**
> ```
> Image: Fixed (200px height)
> Title: Hug contents (top pin)
> Description: Hug contents + wrapping
> Action: Fixed (bottom pin)
> ```

## 9.3 Design Token Migration

**User:** "How do I migrate from hardcoded values to design tokens?"

**Figma Expert:**
> **Migration Steps:**
>
> 1. **Inventory Hardcoded Values**
>    - Search for hex codes, font sizes, spacing values
>    - Document all unique values
>
> 2. **Create Token Structure**
>    ```
>    Primitives:
>    ├── color/blue/500: #3B82F6
>    ├── color/gray/900: #111827
>    └── spacing/4: 4px
>
>    Semantic:
>    ├── color/brand/primary: {color/blue/500}
>    ├── color/text/default: {color/gray/900}
>    └── color/spacing/component: {spacing/4}
>    ```
>
> 3. **Replace Values**
>    - Select element → Apply token
>    - Use "Find and replace" for batch updates
>
> 4. **Verify and Publish**
>    - Check all instances
>    - Publish to library
>    - Notify team of changes
