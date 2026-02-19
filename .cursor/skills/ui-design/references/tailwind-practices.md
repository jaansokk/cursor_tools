# Tailwind CSS Best Practices

Comprehensive guide for writing maintainable, performant Tailwind CSS.

---

## Prerequisites

Two requirements must be met for Tailwind to work well:

1. **You have a design system.** Tailwind's philosophy aligns with consistent design tokens. Without them, you'll write magic values like `p-[123px] mb-[11px]` and create chaos.

2. **You use a component-based approach.** Utility-first can lead to cluttered HTML. Encapsulate frequently used patterns as reusable components.

---

## Configuration as Design System

Your `tailwind.config.js` is your design system's source of truth:

```js
module.exports = {
  theme: {
    colors: {
      // Group related tokens
      surface: {
        base: 'oklch(15% 0.01 250)',
        elevated: 'oklch(18% 0.01 250)',
        overlay: 'oklch(22% 0.01 250)',
      },
      ink: {
        primary: 'oklch(95% 0 0)',
        secondary: 'oklch(75% 0 0)',
        muted: 'oklch(55% 0 0)',
      },
      brand: {
        DEFAULT: 'oklch(65% 0.2 145)',
        hover: 'oklch(60% 0.22 145)',
      },
      semantic: {
        success: 'oklch(70% 0.15 145)',
        warning: 'oklch(75% 0.15 85)',
        error: 'oklch(60% 0.2 25)',
      }
    },
    spacing: {
      'xs': '4px',
      'sm': '8px',
      'md': '12px',
      'lg': '16px',
      'xl': '24px',
      '2xl': '32px',
      '3xl': '48px',
      '4xl': '64px',
    },
    borderRadius: {
      'sm': '4px',
      'md': '6px',
      'lg': '8px',
      'xl': '12px',
      'full': '9999px',
    },
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
    },
  },
}
```

### Semantic Token Naming

Name tokens by their purpose, not their value:

```js
// ❌ Generic
colors: {
  'gray-100': '#f5f5f5',
  'gray-200': '#e5e5e5',
  'blue-500': '#3b82f6',
}

// ✅ Semantic
colors: {
  surface: { base: '...', elevated: '...' },
  ink: { primary: '...', muted: '...' },
  brand: { DEFAULT: '...', hover: '...' },
}
```

---

## Class Minimization

Write fewer classes for the same result:

```html
<!-- ❌ Verbose -->
<div class="pt-4 pb-4">
<div class="flex flex-row justify-between">
<div class="border border-solid border-2 border-black border-opacity-50">

<!-- ✅ Concise -->
<div class="py-4">
<div class="flex justify-between">
<div class="border-2 border-black/50">
```

Remember CSS defaults:
- `flex-row` is the default for `flex`
- `border` implies `border-solid`
- `border-2` implies `border`
- Use color opacity shorthand: `border-black/50`

---

## Class Ordering

Maintain consistent order for readability:

```
Layout → Flexbox/Grid → Spacing → Sizing → Typography → Colors → Effects → States
```

Example:

```html
<button class="
  inline-flex items-center justify-center
  gap-2 px-4 py-2
  h-10
  text-sm font-medium
  bg-brand text-white
  rounded-md shadow-sm
  hover:bg-brand-hover focus:ring-2 focus:ring-brand/50
  transition-colors
">
```

Use [prettier-plugin-tailwindcss](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) for automatic sorting.

---

## Component Patterns

### Variant Sets

Define variants for consistent component styling:

```jsx
const BUTTON_VARIANTS = {
  primary: "bg-brand hover:bg-brand-hover text-white",
  secondary: "bg-surface-elevated hover:bg-surface-overlay text-ink-primary border border-white/15",
  ghost: "hover:bg-surface-elevated text-ink-secondary",
  danger: "bg-semantic-error hover:bg-semantic-error/90 text-white",
};

const BUTTON_SIZES = {
  sm: "h-8 px-3 text-sm",
  md: "h-10 px-4 text-sm",
  lg: "h-12 px-6 text-base",
};

function Button({ variant = "primary", size = "md", children, className }) {
  return (
    <button className={clsx(
      "inline-flex items-center justify-center font-medium rounded-md transition-colors",
      BUTTON_VARIANTS[variant],
      BUTTON_SIZES[size],
      className
    )}>
      {children}
    </button>
  );
}
```

### Merging Classes

Use [clsx](https://github.com/lukeed/clsx) for conditional classes:

```jsx
import clsx from 'clsx';

<div className={clsx(
  "base-classes",
  isActive && "active-classes",
  variant === "primary" && "primary-classes"
)} />
```

For overriding Tailwind classes, use [tailwind-merge](https://github.com/dcastil/tailwind-merge):

```jsx
import { twMerge } from 'tailwind-merge';

// Properly merges conflicting classes
twMerge("px-4 py-2", "px-6") // → "py-2 px-6"
```

---

## Avoiding @apply

The `@apply` directive should be used sparingly:

```css
/* ❌ Overuse throws away Tailwind benefits */
.btn {
  @apply bg-blue-500 text-white font-bold py-2 px-4 rounded 
         hover:bg-blue-600 active:bg-blue-700;
}
```

Problems:
- Loses co-location benefit (styles separate from markup)
- Increases CSS bundle size
- Can cause regressions when changing styles
- Naming CSS classes adds mental overhead

**When @apply IS appropriate:**
- Base typography styles in global CSS
- Third-party component overrides
- Complex animations

---

## Mobile-First Approach

Tailwind is mobile-first. Base styles = mobile, then scale up:

```html
<!-- Mobile: stacked, Tablet: 2 columns, Desktop: 3 columns -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">

<!-- Mobile: small text, Desktop: larger -->
<p class="text-sm md:text-base lg:text-lg">
```

Design for the smallest screen first, then add complexity.

---

## Performance Optimization

### JIT Mode (Default in v3+)

Tailwind 3.0+ uses Just-in-Time compilation by default—only generates CSS for classes you use.

### Content Configuration

Ensure Tailwind scans all your files:

```js
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx,html}',
    './components/**/*.{js,jsx,ts,tsx}',
  ],
}
```

### Minification

Always minify for production:

```bash
npx tailwindcss -o build.css --minify
```

Or use [cssnano](https://cssnano.co) as a PostCSS plugin.

### Unused Token Cleanup

Regularly audit your config—unused design tokens confuse developers and complicate the system.

---

## Dark Mode

### Class Strategy (Recommended)

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class',
}
```

```html
<div class="bg-white dark:bg-slate-900">
<p class="text-slate-900 dark:text-slate-100">
```

### CSS Variables for Theming

For dynamic themes, use CSS variables:

```js
// tailwind.config.js
theme: {
  colors: {
    surface: 'var(--color-surface)',
    ink: 'var(--color-ink)',
  }
}
```

```css
:root {
  --color-surface: theme('colors.white');
  --color-ink: theme('colors.slate.900');
}

.dark {
  --color-surface: theme('colors.slate.900');
  --color-ink: theme('colors.slate.100');
}
```

---

## Common Patterns

### Card

```html
<!-- Dark mode -->
<div class="bg-surface-elevated rounded-lg border border-white/15 p-6">
  <h3 class="text-lg font-semibold text-ink-primary">Title</h3>
  <p class="mt-2 text-sm text-ink-secondary">Description</p>
</div>

<!-- Light mode -->
<div class="bg-white rounded-xl border border-stone-200/60 shadow-sm p-6">
  <h3 class="text-lg font-semibold text-stone-900">Title</h3>
  <p class="mt-2 text-sm text-stone-600">Description</p>
</div>
```

### Input

```html
<!-- Dark mode -->
<input 
  type="text"
  class="
    w-full h-10 px-3
    text-sm text-ink-primary placeholder:text-ink-muted
    bg-surface-base border border-white/15 rounded-md
    focus:outline-none focus:ring-2 focus:ring-brand/50 focus:border-brand
    transition-colors
  "
  placeholder="Enter text..."
/>

<!-- Light mode -->
<input 
  type="text"
  class="
    w-full h-10 px-3
    text-sm text-stone-900 placeholder:text-stone-400
    bg-white border border-stone-200 rounded-md
    focus:outline-none focus:ring-2 focus:ring-brand/50 focus:border-brand
    transition-colors
  "
  placeholder="Enter text..."
/>
```

### Badge

```html
<span class="inline-flex items-center px-2 py-0.5 text-xs font-medium rounded-full bg-brand/10 text-brand">
  Label
</span>
```

### Dropdown Trigger

```html
<!-- Dark mode -->
<button class="
  inline-flex items-center justify-between
  gap-2 px-3 h-9
  text-sm text-ink-primary
  bg-surface-elevated border border-white/15 rounded-md
  hover:bg-surface-overlay
  transition-colors
">
  <span class="truncate">Select option</span>
  <svg class="w-4 h-4 text-ink-muted shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
  </svg>
</button>

<!-- Light mode -->
<button class="
  inline-flex items-center justify-between
  gap-2 px-3 h-9
  text-sm text-stone-900
  bg-white border border-stone-200 rounded-md
  hover:bg-stone-50 hover:border-stone-300
  transition-colors
">
  <span class="truncate">Select option</span>
  <svg class="w-4 h-4 text-stone-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
  </svg>
</button>
```

---

## Responsive Utilities Reference

| Prefix | Min Width | CSS |
|--------|-----------|-----|
| (none) | 0px | Default mobile styles |
| `sm:` | 640px | `@media (min-width: 640px)` |
| `md:` | 768px | `@media (min-width: 768px)` |
| `lg:` | 1024px | `@media (min-width: 1024px)` |
| `xl:` | 1280px | `@media (min-width: 1280px)` |
| `2xl:` | 1536px | `@media (min-width: 1536px)` |

---

## State Variants Reference

```html
<!-- Hover -->
<button class="bg-blue-500 hover:bg-blue-600">

<!-- Focus -->
<input class="focus:ring-2 focus:ring-blue-500 focus:outline-none">

<!-- Active -->
<button class="active:scale-95">

<!-- Disabled -->
<button class="disabled:opacity-50 disabled:cursor-not-allowed">

<!-- Group hover (parent hover affects child) -->
<div class="group">
  <span class="group-hover:text-blue-500">
</div>

<!-- Peer (sibling states) -->
<input class="peer" />
<span class="peer-invalid:text-red-500">Error message</span>
```
