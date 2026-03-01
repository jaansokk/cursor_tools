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

### The Contrast Principle

This is where most AI-generated interfaces fail — in both directions. Study Vercel, Supabase, Linear: their surfaces are calm but **clearly distinguishable**. Their borders are quiet but **visible without hunting**.

**The rule:** Subtle does not mean invisible. Every boundary must be perceivable on a non-retina display at arm's length. If you have to pixel-peep to find it, it's too subtle.

**For dark mode surfaces:**

```css
/* Tailwind dark mode surfaces — note higher opacity than naive defaults */
.surface-base { @apply bg-slate-950; }
.surface-elevated { @apply bg-slate-900/70; }     /* clearly lifted */
.surface-overlay { @apply bg-slate-800/50; }       /* distinct from elevated */
```

**For light mode surfaces:**

```html
<!-- Light mode uses named palette steps, not raw opacity -->
<div class="bg-stone-50">                                          <!-- Canvas -->
  <div class="bg-white border border-stone-200/60 shadow-sm">     <!-- Card -->
    <div class="bg-stone-50">                                      <!-- Nested/inset -->
    </div>
  </div>
</div>
```

**For dark mode borders — minimum thresholds:**

```html
<div class="border border-white/8">    <!-- Subtle (absolute floor) -->
<div class="border border-white/15">   <!-- Default -->
<div class="border border-white/25">   <!-- Strong / hover -->
```

**For light mode borders — minimum thresholds:**

```html
<div class="border border-stone-200/60">  <!-- Subtle (floor) -->
<div class="border border-stone-200">     <!-- Default -->
<div class="border border-stone-300">     <!-- Strong / hover -->
```

**The test:** Take a screenshot and view it at 50% zoom. Can you still distinguish every elevation level? Can you see where cards end and canvas begins? If any boundary vanishes — raise the contrast.

### Common AI Mistakes

- **Too subtle:** `border-white/5`, `border-black/5` are invisible on most displays. Never use them.
- **Too subtle (surfaces):** `bg-slate-900/50` on `bg-slate-950` is nearly invisible. Use `/70` minimum.
- **Too dramatic:** Going from `slate-950` to `slate-700` in one step. Build graduated levels.
- **Using raw opacity on named colors in light mode:** `border-black/10` is less predictable than `border-stone-200`. Prefer named palette steps in light mode.
- **Different hues for different surfaces:** Keep surfaces on the same hue axis.
- **Muted text that fails WCAG:** `stone-400` on `white` fails AA (3.6:1). `stone-500` is the floor (4.6:1).

---

## Text Hierarchy via Tokens

Build four distinct levels. Every level must pass WCAG AA (4.5:1) against its background except disabled/placeholder states.

**Dark mode (on ~slate-950 background):**

```html
<!-- Primary: Default text, highest contrast -->
<p class="text-slate-100">Main content</p>

<!-- Secondary: Supporting text, clearly readable -->
<p class="text-slate-300">Supporting info</p>

<!-- Tertiary: Metadata, timestamps — still readable -->
<span class="text-slate-400">2 hours ago</span>

<!-- Muted: Disabled, placeholder only -->
<span class="text-slate-500">Placeholder</span>
```

**Light mode (on white/stone-50 background):**

```html
<!-- Primary: Headings, key data -->
<p class="text-stone-900">Main content</p>

<!-- Secondary: Body text, table cells -->
<p class="text-stone-600">Supporting info</p>

<!-- Tertiary: Captions, metadata — floor for readable text -->
<span class="text-stone-500">2 hours ago</span>

<!-- Muted: Disabled, placeholder only — does NOT pass AA -->
<span class="text-stone-400">Placeholder</span>
```

Use all four consistently. If you're only using two, your hierarchy is too flat. If your "muted" text is unreadable, you've gone too far — `stone-500` / `slate-400` is the floor for text that users need to read.

---

## Border Progression

Borders aren't binary. Build a scale — but never start below the visibility floor.

**Dark mode:**

```html
<!-- Subtle: Soft separation (floor) -->
<div class="border border-white/8">

<!-- Default: Standard borders -->
<div class="border border-white/15">

<!-- Strong: Emphasis, hover states -->
<div class="border border-white/25">

<!-- Stronger: Focus rings -->
<div class="ring-2 ring-brand/50">
```

**Light mode:**

```html
<!-- Subtle: Soft separation (floor) -->
<div class="border border-stone-200/60">

<!-- Default: Standard borders -->
<div class="border border-stone-200">

<!-- Strong: Emphasis, hover states -->
<div class="border border-stone-300">

<!-- Stronger: Focus rings -->
<div class="ring-2 ring-brand/50">
```

Match border intensity to the importance of the boundary. In light mode, prefer named palette steps over opacity on black — they produce more predictable, warmer results.

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

Pick a primary strategy and use it consistently. Combining border + shadow (e.g. `border-stone-200/60 shadow-sm`) is fine when both serve a purpose — border defines the edge, shadow provides lift. What to avoid is *random* mixing where some cards have borders, others have shadows, others have both, with no logic.

### Borders-Only (Flat)

Clean, technical, dense. For utility-focused tools where information density matters.

```html
<div class="border border-white/15 rounded-lg">
  <!-- No shadows, just borders -->
</div>
```

### Borderless (Shadows + Spacing)

Minimal, editorial, calm. Relies on shadow and whitespace alone to define structure — no visible border lines.

```html
<div class="bg-white shadow-sm rounded-xl p-6">
  <!-- On a bg-stone-50 canvas — shadow + color contrast defines the card -->
</div>
```

**Works well for:**
- Content-focused layouts, portfolios, marketing pages
- Interfaces with few elevation levels (canvas + cards, 2 levels max)
- Editorial / reading-app aesthetics where borders feel heavy

**Breaks down when:**
- **Data-dense UIs** — dashboards, tables, admin panels. When 4+ cards sit in a grid, shadows alone can't disambiguate adjacent elements.
- **Adjacent same-color surfaces** — two white cards side by side with only `shadow-sm` produces ambiguous overlapping shadows. Borders solve this.
- **Tables** — row separation without borders or `divide-*` rules forces alternating row colors, limiting palette flexibility.
- **Dark mode** — shadows are nearly invisible on dark backgrounds. Borderless dark mode drifts into flat soup.
- **Small/dense elements** — chips, badges, input groups, filter pills. At small sizes `shadow-sm` is imperceptible. These need borders or strong background contrast.
- **3+ elevation levels** — canvas → card → dropdown → nested dropdown. Shadow stacking gets visually muddy past 2 levels.

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

### Border + Shadow (Combined)

The practical middle ground most polished products land on. Border defines the edge precisely, shadow provides depth. Common in data-heavy apps.

```html
<!-- Light mode — border for structure, shadow for lift -->
<div class="bg-white border border-stone-200/60 shadow-sm rounded-xl p-6">
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

## Light Mode Specifics

Light mode has its own contrast traps — different from dark mode.

**White-on-near-white is the #1 failure.** A `bg-white` card on a `bg-gray-50` canvas with `border-black/5` is effectively invisible. Use visible borders (`stone-200/60` minimum) or combine with `shadow-sm`.

**Named palette steps over raw opacity.** In light mode, `border-stone-200` is more predictable and warmer than `border-black/10`. Raw opacity on black produces cold, harsh results at higher values and invisible results at lower values.

**Practical light-mode elevation stack:**

```html
<!-- Canvas -->
<div class="bg-stone-50">

  <!-- Context bar / toolbar -->
  <div class="bg-stone-200/40 border border-stone-300/40">

  <!-- Cards -->
  <div class="bg-white border border-stone-200/60 shadow-sm rounded-xl">

    <!-- Inset / nested surfaces -->
    <div class="bg-stone-50 rounded-lg">
```

**Text contrast in light mode:**
- `stone-900` for headings and primary text
- `stone-700` for CTA buttons, bold labels
- `stone-600` for secondary body text
- `stone-500` for captions, metadata (WCAG AA floor on white)
- `stone-400` only for disabled/placeholder (fails AA — intentional)

---

## Data-Dense Contexts

Dashboards, analytics, trading tools, and admin panels need **higher contrast** than marketing sites or reading apps.

**Why:** When multiple data blocks, tables, and charts compete for attention on one screen, the user relies on visible structure to parse information quickly. "Whisper-quiet" layering makes data tools feel washed-out and hard to navigate.

**Raise contrast when:**
- Multiple cards/blocks sit on the same canvas
- Tables have many rows and columns
- Small text (axis labels, captions, data cells) sits on tinted backgrounds
- Three or more elevation levels are visible simultaneously

**Practical rules:**
- Card borders: named palette steps (`stone-200`, not `black/5`)
- Table row dividers: `divide-stone-100` minimum, `divide-stone-200` for busy tables
- Table header borders: `border-stone-200` — clearly stronger than row dividers
- Context bars: distinctly different from both canvas and card surfaces
- Chart containers: visible card boundary so chart data doesn't float

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
               text-sm bg-surface-elevated border border-white/15 rounded-md
               hover:bg-surface-overlay transition-colors">
  <span class="truncate">Selected value</span>
  <ChevronDownIcon class="w-4 h-4 text-ink-muted shrink-0" />
</button>
```

Custom triggers must use `inline-flex` with `whitespace-nowrap` to keep text and icons aligned.
