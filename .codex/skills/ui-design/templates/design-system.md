# Design System Template

Use this template to document your project's design system. Copy to your project root as `design-system.md` or `.ui-design/system.md`.

---

## Project: [Project Name]

### Direction

**Feel:** [Describe the overall aesthetic in 2-3 words. e.g., "warm and organic", "cold and technical", "playful and bold"]

**Signature:** [One unique visual element that defines this product]

**Inspirations:** [2-3 reference products or visual styles]

---

## Color Tokens

Configure in `tailwind.config.js`:

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Surfaces
        surface: {
          base: '',      // App canvas background
          elevated: '',  // Cards, panels
          overlay: '',   // Dropdowns, modals
          inset: '',     // Recessed areas
        },
        
        // Text (Ink)
        ink: {
          primary: '',   // Default text
          secondary: '', // Supporting text
          muted: '',     // Metadata, timestamps
          disabled: '',  // Disabled states
        },
        
        // Borders
        border: {
          DEFAULT: '',   // Standard borders
          subtle: '',    // Soft separation
          strong: '',    // Emphasis
        },
        
        // Brand
        brand: {
          DEFAULT: '',   // Primary accent
          hover: '',     // Hover state
          muted: '',     // Backgrounds, badges
        },
        
        // Semantic
        semantic: {
          success: '',
          warning: '',
          error: '',
          info: '',
        },
      },
    },
  },
}
```

### Color Values

| Token | Light Mode | Dark Mode | Usage |
|-------|------------|-----------|-------|
| `surface.base` | | | App background |
| `surface.elevated` | | | Cards, panels |
| `surface.overlay` | | | Dropdowns, modals |
| `ink.primary` | | | Body text |
| `ink.secondary` | | | Labels, captions |
| `ink.muted` | | | Metadata |
| `brand.DEFAULT` | | | Primary actions, links |
| `semantic.success` | | | Success states |
| `semantic.error` | | | Error states |

---

## Typography

### Font Families

```js
// tailwind.config.js
fontFamily: {
  display: ['', 'sans-serif'],   // Headlines
  body: ['', 'sans-serif'],      // Body text
  mono: ['', 'monospace'],       // Code, data
}
```

### Type Scale

| Level | Class | Size | Weight | Usage |
|-------|-------|------|--------|-------|
| Display | `text-4xl font-bold tracking-tight` | | | Page titles |
| H1 | `text-3xl font-bold tracking-tight` | | | Section headers |
| H2 | `text-2xl font-semibold` | | | Subsections |
| H3 | `text-xl font-semibold` | | | Card titles |
| H4 | `text-lg font-medium` | | | Subheadings |
| Body | `text-base font-normal` | | | Paragraphs |
| Small | `text-sm font-normal` | | | Captions, metadata |
| Tiny | `text-xs font-medium` | | | Labels, badges |
| Mono | `font-mono text-sm tabular-nums` | | | Numbers, code |

---

## Spacing

**Base unit:** [4px / 8px]

| Token | Value | Usage |
|-------|-------|-------|
| `space-xs` | | Icon gaps, tight pairs |
| `space-sm` | | Within components |
| `space-md` | | Component padding |
| `space-lg` | | Between related items |
| `space-xl` | | Section spacing |
| `space-2xl` | | Major separation |

### Padding Conventions

- **Cards:** `p-6` (24px)
- **Buttons:** `px-4 py-2` (16px × 8px)
- **Inputs:** `px-3 py-2` (12px × 8px)
- **Badges:** `px-2 py-0.5` (8px × 2px)

---

## Border Radius

**Scale:**

```js
borderRadius: {
  sm: '',    // Small inputs, badges
  DEFAULT: '', // Buttons, cards
  lg: '',    // Large cards
  xl: '',    // Modals, dialogs
  full: '',  // Pills, avatars
}
```

| Element | Radius | Class |
|---------|--------|-------|
| Buttons | | `rounded-md` |
| Inputs | | `rounded-md` |
| Cards | | `rounded-lg` |
| Modals | | `rounded-xl` |
| Avatars | | `rounded-full` |
| Badges | | `rounded-full` |

---

## Depth Strategy

**Approach:** [ ] Borders-only  [ ] Subtle shadows  [ ] Layered shadows

### Elevation Levels

| Level | Usage | Implementation |
|-------|-------|----------------|
| 0 | Base canvas | `bg-surface-base` |
| 1 | Cards, panels | `bg-surface-elevated` / `shadow-sm` |
| 2 | Dropdowns | `bg-surface-overlay` / `shadow-lg` |
| 3 | Modals | `bg-surface-overlay` / `shadow-xl` |

### Border Weights

| Weight | Class | Usage |
|--------|-------|-------|
| Subtle | `border border-border-subtle` | Section dividers |
| Default | `border border-border` | Card borders |
| Strong | `border-2 border-border-strong` | Focus states |

---

## Component Patterns

### Button Primary

```html
<button class="
  inline-flex items-center justify-center
  gap-2 px-4 h-10
  text-sm font-medium
  bg-brand text-white
  rounded-md
  hover:bg-brand-hover
  focus:outline-none focus:ring-2 focus:ring-brand/50
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-colors
">
```

| Property | Value |
|----------|-------|
| Height | 40px |
| Padding | 16px horizontal |
| Font | 14px, 500 weight |
| Radius | |
| States | hover, focus, disabled |

### Button Secondary

```html
<button class="
  inline-flex items-center justify-center
  gap-2 px-4 h-10
  text-sm font-medium
  bg-surface-elevated text-ink-primary
  border border-border
  rounded-md
  hover:bg-surface-overlay hover:border-border-strong
  focus:outline-none focus:ring-2 focus:ring-brand/50
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-colors
">
```

### Input

```html
<input class="
  w-full h-10 px-3
  text-sm text-ink-primary placeholder:text-ink-muted
  bg-surface-base border border-border rounded-md
  focus:outline-none focus:ring-2 focus:ring-brand/50 focus:border-brand
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-colors
" />
```

| Property | Value |
|----------|-------|
| Height | 40px |
| Padding | 12px horizontal |
| Font | 14px |
| Border | |
| Focus | ring + border color |

### Card

```html
<div class="
  bg-surface-elevated
  border border-border
  rounded-lg
  p-6
">
```

| Property | Value |
|----------|-------|
| Padding | 24px |
| Radius | |
| Border | |
| Shadow | |

### Badge

```html
<span class="
  inline-flex items-center
  px-2 py-0.5
  text-xs font-medium
  bg-brand/10 text-brand
  rounded-full
">
```

---

## Icons

**Icon set:** [Heroicons / Lucide / Phosphor / etc.]

**Sizes:**
- Small (inline): `w-4 h-4`
- Default: `w-5 h-5`
- Large: `w-6 h-6`

**Stroke width:** [1.5 / 2]

---

## Animation

**Durations:**
- Micro-interactions: `duration-150`
- Standard transitions: `duration-200`
- Complex animations: `duration-300`

**Easing:** `ease-out` (smooth deceleration)

**Hover effect:** [scale / glow / color shift / none]

---

## Responsive Breakpoints

| Name | Min Width | Target |
|------|-----------|--------|
| (default) | 0 | Mobile portrait |
| `sm` | 640px | Mobile landscape |
| `md` | 768px | Tablet |
| `lg` | 1024px | Desktop |
| `xl` | 1280px | Large desktop |

---

## Pattern Library

### [Pattern Name]

**Usage:** [When to use this pattern]

**Anatomy:**
- [Component parts]

**Variants:**
- [Variant 1]
- [Variant 2]

**Code:**
```html
<!-- Pattern code here -->
```

---

## Don't

List specific anti-patterns for this project:

- [ ] 
- [ ] 
- [ ] 

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| | Initial design system | |
