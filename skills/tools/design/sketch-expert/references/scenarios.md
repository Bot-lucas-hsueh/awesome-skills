# Scenario Examples

## 9.1 Building a Button Component

**User:** "Create a button component with primary/secondary/disabled states"

**Sketch Expert:**
> **Component Structure:**
>
> | Element | Property | Value |
> |---------|----------|-------|
> | Symbol | Name | Button/Primary |
> | Background | Fill | Shared Style: Button/Primary/Background |
> | Corner Radius | Fixed | 8px |
> | Text | Style | Text/Button/Default |
> | Padding | Smart Layout | 16px H, 12px V |
>
> **States Setup:**
> 1. Create symbol with default state
> 2. Right-click → Create Variant
> 3. Add variant property: Type (Primary, Secondary, Ghost)
> 4. Add variant property: State (Default, Hover, Pressed, Disabled)
> 5. Configure property combinations
>
> **Override Configuration:**
> - Text content (Text property)
> - Icon visibility (Override)
> - Loading spinner (Override)

## 9.2 Responsive Card Design

**User:** "Design a card that adapts to different content lengths"

**Sketch Expert:**
> **Smart Layout Configuration:**
> 1. Create card group with Auto Layout
> 2. Set image: Fixed height 200px
> 3. Configure content area:
>    - Title: Hug contents, top pinning
>    - Description: Hug contents + wrapping
>    - Action: Fixed, bottom pinning
> 4. Test with varying content lengths
>
> **Resizing Behavior:**
> ```
> Image: Fixed (200px height)
> Title: Hug (top pin)
> Description: Hug + wrapping (fills space)
> Action: Fixed (bottom pin)
> ```

## 9.3 Icon System Setup

**User:** "How do I set up an icon library in Sketch?"

**Sketch Expert:**
> **Icon System Workflow:**
>
> 1. **Create Icon Canvas**
>    - Artboard: 24x24 (or 20x20)
>    - Grid: 2px inset
>
> 2. **Symbol Structure**
>    ```
>    Icons/
>    ├── Actions
>    │   ├── Icon/Add
>    │   ├── Icon/Edit
> │   └── Icon/Delete
>    ├── Navigation
>    │   ├── Icon/Home
>    │   └── Icon/Back
>    └── Status
>        ├── Icon/Check
>        └── Icon/Warning
>    ```
>
> 3. **Override Setup**
>    - Color: Override (bind to style)
>    - Size: Fixed (24x24)
>
> 4. **Export Presets**
>    - SVG (for web)
>    - PDF (for iOS)
>    - PNG @1x, @2x, @3x (for Android)
