# Core Craft Principles

These apply regardless of design direction. This is the quality floor.

---

## Surface & Token Architecture

Professional interfaces don't pick colors randomly—they build systems. Understanding this architecture is the difference between "looks okay" and "feels like a real product."

### The Primitive Foundation

Every color in your interface should trace back to a small set of primitives:

- **Foreground** — text colors (primary, secondary, muted)
- **Background** — surface colors (base, elevated, overlay)
- **Border** — edge colors (default, subtle, strong)
- **Brand** — your primary accent
- **Semantic** — functional colors (destructive, warning, success)

Don't invent new colors. Map everything to these primitives.

### Surface Elevation Hierarchy

Surfaces stack. A dropdown sits above a card which sits above the page. Build a numbered system:

```
Level 0: Base background (the app canvas)
Level 1: Cards, panels (same visual plane as base or slightly elevated)
Level 2: Dropdowns, popovers (floating above)
Level 3: Nested dropdowns, stacked overlays
Level 4: Highest elevation (rare)
```

In dark mode, higher elevation = slightly lighter. In light mode, higher elevation = slightly lighter or uses shadow.

### The Subtlety Principle

This is where most interfaces fail. Study Vercel, Supabase, Linear—their surfaces are **barely different** but still distinguishable. Their borders are **light but not invisible**.

**For surfaces:** The difference between elevation levels should be subtle—a few percentage points of lightness, not dramatic jumps. In dark mode:

```css
/* Tailwind dark mode surfaces */
.surface-base { @apply bg-slate-950; }           /* ~3% lightness */
.surface-elevated { @apply bg-slate-900/50; }    /* ~7% lightness */
.surface-overlay { @apply bg-slate-800/30; }     /* ~12% lightness */
```

**For borders:** Use low opacity values:

```html
<!-- Dark mode borders -->
<div class="border border-white/5">   <!-- Subtle -->
<div class="border border-white/10">  <!-- Default -->
<div class="border border-white/20">  <!-- Strong -->

<!-- Light mode borders -->
<div class="border border-black/5">   <!-- Subtle -->
<div class="border border-black/10">  <!-- Default -->
```

**The test:** Squint at your interface. You should still perceive hierarchy—what's above what, where regions begin and end. But no single border or surface should jump out.

### Common AI Mistakes

- Borders that are too visible (`border-gray-700` instead of `border-white/5`)
- Surface jumps that are too dramatic (going from `slate-950` to `slate-700`)
- Using different hues for different surfaces
- Harsh dividers where subtle borders would do

---

## Text Hierarchy via Tokens

Build four distinct levels:

```html
<!-- Primary: Default text, highest contrast -->
<p class="text-slate-100">Main content</p>

<!-- Secondary: Supporting text, slightly muted -->
<p class="text-slate-300">Supporting info</p>

<!-- Tertiary: Metadata, timestamps -->
<span class="text-slate-400">2 hours ago</span>

<!-- Muted: Disabled, placeholder -->
<span class="text-slate-500">Placeholder</span>
```

Use all four consistently. If you're only using two, your hierarchy is too flat.

---

## Border Progression

Borders aren't binary. Build a scale:

```html
<!-- Subtle: Soft separation -->
<div class="border border-white/5">

<!-- Default: Standard borders -->
<div class="border border-white/10">

<!-- Strong: Emphasis, hover states -->
<div class="border border-white/20">

<!-- Stronger: Focus rings -->
<div class="ring-2 ring-brand/50">
```

Match border intensity to the importance of the boundary.

---

## Spacing System

Pick a base unit (4px or 8px) and use multiples. Every spacing value should be explainable:

```html
<!-- Tailwind spacing scale based on 4px -->
gap-1    <!-- 4px: Micro spacing -->
gap-2    <!-- 8px: Tight element pairs -->
p-3      <!-- 12px: Component internal -->
p-4      <!-- 16px: Standard padding -->
gap-6    <!-- 24px: Section spacing -->
py-8     <!-- 32px: Major separation -->
py-12    <!-- 48px: Page sections -->
```

### Symmetrical Padding

Keep padding symmetrical unless content naturally creates balance:

```html
<!-- ✅ Good -->
<div class="p-4">
<div class="px-4 py-3">  <!-- Only when horizontal needs more room -->

<!-- ❌ Bad: Random asymmetry -->
<div class="pt-6 pb-4 pl-3 pr-5">
```

---

## Border Radius Consistency

Sharper = technical. Rounder = friendly. Build a scale:

```html
<!-- Sharp: Technical, data-dense -->
rounded-sm   <!-- 4px -->

<!-- Balanced: Modern default -->
rounded-md   <!-- 6px -->
rounded-lg   <!-- 8px -->

<!-- Soft: Friendly, approachable -->
rounded-xl   <!-- 12px -->
rounded-2xl  <!-- 16px -->

<!-- Full: Pills, avatars -->
rounded-full <!-- 9999px -->
```

Consistency matters more than the specific value. Don't mix sharp and soft randomly.

---

## Depth & Elevation Strategy

Match depth approach to design direction. Choose ONE and commit:

### Borders-Only (Flat)

Clean, technical, dense. For utility-focused tools where information density matters.

```html
<div class="border border-white/10 rounded-lg">
  <!-- No shadows, just borders -->
</div>
```

### Subtle Single Shadows

Soft lift without complexity. For approachable products.

```html
<div class="shadow-sm rounded-lg">
  <!-- shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05) -->
</div>
```

### Layered Shadows

Rich, premium, dimensional. For cards that need presence.

```html
<div class="shadow-lg rounded-lg">
  <!-- Or custom layered shadow -->
  <style>
    .shadow-layered {
      box-shadow:
        0 0 0 1px rgba(0, 0, 0, 0.05),
        0 1px 2px rgba(0, 0, 0, 0.04),
        0 2px 4px rgba(0, 0, 0, 0.03),
        0 4px 8px rgba(0, 0, 0, 0.02);
    }
  </style>
</div>
```

### Surface Color Shifts

Background tints establish hierarchy without shadows:

```html
<div class="bg-white">  <!-- Card -->
  <!-- On a bg-slate-50 background, this already feels elevated -->
</div>
```

---

## Typography Hierarchy

Build distinct levels that are visually distinguishable at a glance:

```html
<!-- Headlines: Heavy weight, tight tracking -->
<h1 class="text-3xl font-bold tracking-tight">

<!-- Subheadings: Medium weight -->
<h2 class="text-xl font-semibold">

<!-- Body: Comfortable for reading -->
<p class="text-base font-normal leading-relaxed">

<!-- Labels/UI: Works at smaller sizes -->
<label class="text-sm font-medium">

<!-- Data: Monospace, tabular numbers -->
<span class="font-mono text-sm tabular-nums">
```

Don't rely on size alone. Combine size, weight, and letter-spacing.

---

## Data Typography

Numbers, IDs, codes, timestamps belong in monospace:

```html
<span class="font-mono tabular-nums">1,234,567</span>
<code class="font-mono text-sm bg-slate-800 px-1.5 py-0.5 rounded">user_id_123</code>
```

`tabular-nums` ensures numbers align in columns.

---

## Iconography

Icons clarify, not decorate. If removing an icon loses no meaning, remove it.

```html
<!-- Icon with text: align optically -->
<button class="inline-flex items-center gap-2">
  <svg class="w-4 h-4" />
  <span>Label</span>
</button>

<!-- Standalone icon: give presence with background -->
<div class="p-2 rounded-lg bg-surface-elevated">
  <svg class="w-5 h-5 text-ink-secondary" />
</div>
```

---

## Animation

Keep it fast and functional:

```html
<!-- Micro-interactions: ~150ms -->
<button class="transition-colors duration-150">

<!-- Larger transitions: ~200-250ms -->
<div class="transition-all duration-200">

<!-- Easing: smooth deceleration -->
<div class="transition-all ease-out">
```

Avoid spring/bounce effects in professional interfaces—they feel playful, not serious.

---

## Interaction States

Every interactive element needs complete states:

```html
<button class="
  bg-brand text-white
  hover:bg-brand/90
  active:scale-[0.98]
  focus:outline-none focus:ring-2 focus:ring-brand/50
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-all
">
```

Data states too:
- Loading: skeleton or spinner
- Empty: helpful message, illustration
- Error: clear error message, retry action

---

## Navigation Context

Screens need grounding. A data table floating in space feels like a component demo, not a product.

Include:
- **Navigation** — sidebar or top nav showing location
- **Location indicator** — breadcrumbs, page title, active nav state
- **User context** — who's logged in, what workspace

For sidebars, consider using the same background as main content with a subtle border for separation.

---

## Dark Mode Specifics

Dark interfaces have different needs:

**Borders over shadows:** Shadows are less visible on dark backgrounds. Lean on borders.

**Adjust semantic colors:** Status colors often need slight desaturation for dark backgrounds:

```html
<!-- Light mode -->
<span class="text-green-600">Success</span>

<!-- Dark mode: slightly desaturated -->
<span class="dark:text-green-400">Success</span>
```

**Same structure, inverted values:** The hierarchy system still applies, just reversed.

---

## Custom Form Controls

**Never use native form elements for styled UI.** Native `<select>`, `<input type="date">` render OS-native dropdowns that cannot be styled.

Build custom:
- Custom select: trigger button + positioned dropdown
- Custom date picker: input + calendar popover
- Custom checkbox/radio: styled div with state management

```html
<!-- Custom select trigger -->
<button class="inline-flex items-center justify-between gap-2 px-3 h-9 w-full
               text-sm bg-surface-elevated border border-white/10 rounded-md
               hover:bg-surface-overlay transition-colors">
  <span class="truncate">Selected value</span>
  <ChevronDownIcon class="w-4 h-4 text-ink-muted shrink-0" />
</button>
```

Custom triggers must use `inline-flex` with `whitespace-nowrap` to keep text and icons aligned.
