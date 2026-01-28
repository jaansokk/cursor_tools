---
name: ui-design
description: Create distinctive, production-grade web interfaces with high design quality using Tailwind CSS. Use for building UI components, pages, dashboards, apps, and web applications. Generates crafted, polished code that avoids generic AI aesthetics.
---

# UI Design

Build web interfaces with craft, consistency, and intention—using Tailwind CSS.

## Scope

**Use for:** Web applications, dashboards, SaaS products, landing pages, marketing sites, admin panels, e-commerce interfaces, component libraries.

**Stack:** Tailwind CSS as the primary styling approach.

---

# The Problem

You will generate generic output. Your training has seen thousands of interfaces. The patterns are strong.

You can follow the entire process below — explore the domain, name a signature, state your intent — and still produce a template. Warm colors on cold structures. Friendly fonts on generic layouts. Purple gradients on white backgrounds.

This happens because intent lives in prose, but code generation pulls from patterns. The gap between them is where defaults win.

The process below helps. But process alone doesn't guarantee craft. You have to catch yourself.

---

# Where Defaults Hide

Defaults don't announce themselves. They disguise themselves as infrastructure—the parts that feel like they just need to work, not be designed.

**Typography feels like a container.** Pick something readable, move on. But typography isn't holding your design — it IS your design. The weight of a headline, the personality of a label, the texture of a paragraph. A bakery management tool and a trading terminal might both need "clean, readable type"—but the type that's warm and handmade is not the type that's cold and precise. If you're reaching for Inter, Roboto, or system fonts as a safe haven, you're not designing.

**Navigation feels like scaffolding.** Build the sidebar, add the links, get to the real work. But navigation isn't around your product—it IS your product. Where you are, where you can go, what matters most.

**Tailwind classes feel like implementation.** But your utility choices are design decisions. `bg-slate-950` evokes a different world than `bg-stone-50`. Someone reading only your classes should sense what product this is.

**Color feels like decoration.** But a number on screen is not design. Gray builds structure. Color communicates—status, action, emphasis, identity. Unmotivated color is noise.

The trap is thinking some decisions are creative and others are structural. There are no structural decisions. Everything is design.

---

# Intent First

Before touching code, answer these. Not in your head—out loud, to yourself or the user.

**Who is this human?**
Not "users." The actual person. Where are they when they open this? What's on their mind? A teacher at 7am with coffee is not a developer debugging at midnight is not a founder between investor meetings.

**What must they accomplish?**
Not "use the dashboard." The verb. Grade these submissions. Find the broken deployment. Approve the payment. The answer determines what leads, what follows, what hides.

**What should this feel like?**
Say it in words that mean something. "Clean and modern" means nothing—every AI says that. Warm like a notebook? Cold like a terminal? Dense like a trading floor? Calm like a reading app?

**What aesthetic direction?**
Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian.

If you cannot answer these with specifics, stop. Ask the user. Do not guess. Do not default.

## Every Choice Must Be A Choice

For every decision, you must be able to explain WHY.

- Why this layout and not another?
- Why this color temperature?
- Why this typeface?
- Why this spacing scale?
- Why these Tailwind utilities?

If your answer is "it's common" or "it's clean" or "it works"—you haven't chosen. You've defaulted.

**The test:** If you swapped your choices for the most common alternatives and the design didn't feel meaningfully different, you never made real choices.

## Sameness Is Failure

If another AI, given a similar prompt, would produce substantially the same output—you have failed.

No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, Inter, purple gradients) across generations.

---

# Product Domain Exploration

This is where defaults get caught—or don't.

Generic output: Task type → Visual template → Theme
Crafted output: Task type → Product domain → Signature → Structure + Expression

## Required Outputs

**Do not propose any direction until you produce all four:**

**Domain:** Concepts, metaphors, vocabulary from this product's world. Not features—territory. Minimum 5.

**Color world:** What colors exist naturally in this product's domain? If this product were a physical space, what would you see? List 5+.

**Signature:** One element—visual, structural, or interaction—that could only exist for THIS product.

**Defaults to reject:** 3 obvious choices for this interface type. You can't avoid patterns you haven't named.

## Proposal Requirements

Your direction must explicitly reference:
- Domain concepts you explored
- Colors from your color world exploration
- Your signature element
- What replaces each default

**The test:** Remove the product name. Could someone identify what this is for? If not, it's generic.

---

# The Mandate

**Before showing the user, look at what you made.**

Ask yourself: "If they said this lacks craft, what would they mean?"

That thing you just thought of — fix it first.

## The Checks

Run these against your output before presenting:

- **The swap test:** If you swapped the typeface for Inter, would anyone notice? If you swapped the layout for a standard template, would it feel different?

- **The squint test:** Blur your eyes. Can you still perceive hierarchy? Is anything jumping out harshly? Craft whispers, it does not shout.

- **The signature test:** Can you point to five specific elements where your signature appears?

- **The Tailwind test:** Read your utility classes. Do they feel intentional or like copy-paste from documentation?

- **The generic AI test:** Does this look like something every AI would produce? Purple gradients, Inter font, predictable card grids, generic hero sections?

---

# Craft Foundations

## Subtle Layering

This is the backbone of craft. Study Vercel, Supabase, Linear.

**Surfaces must be barely different but still distinguishable.** Not dramatic jumps. Not obviously different colors. Whisper-quiet shifts.

**Borders must be light but not invisible.** The border should disappear when you're not looking for it, but be findable when you need to understand structure.

```html
<!-- Subtle surface elevation with Tailwind -->
<div class="bg-slate-950">                    <!-- Level 0: Base -->
  <div class="bg-slate-900/50">               <!-- Level 1: Cards -->
    <div class="bg-slate-800/30">             <!-- Level 2: Elevated -->
    </div>
  </div>
</div>

<!-- Subtle borders -->
<div class="border border-white/5">           <!-- Dark mode -->
<div class="border border-black/5">           <!-- Light mode -->
```

## Infinite Expression

Every pattern has infinite expressions. A metric display could be a hero number, inline stat, sparkline, gauge, progress bar, comparison delta, trend badge. Even sidebar + cards has infinite variations.

**Before building, ask:**
- What's the ONE thing users do most here?
- What products solve similar problems brilliantly? Study them.
- Why would this feel designed for its purpose, not templated?

Linear's cards don't look like Notion's. Vercel's metrics don't look like Stripe's. Same concepts, infinite expressions.

## Color Lives Somewhere

Every product exists in a world. That world has colors.

Before you reach for a Tailwind palette, spend time in the product's world. What would you see if you walked into the physical version of this space?

**Beyond Warm and Cold:** Is this quiet or loud? Dense or spacious? Serious or playful? Geometric or organic?

---

# Tailwind Best Practices

## Design Token Architecture

Configure `tailwind.config.js` as your design system source of truth:

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Semantic naming, not generic
        surface: {
          base: 'oklch(15% 0.01 250)',
          elevated: 'oklch(18% 0.01 250)',
          overlay: 'oklch(22% 0.01 250)',
        },
        ink: {
          primary: 'oklch(95% 0 0)',
          secondary: 'oklch(70% 0 0)',
          muted: 'oklch(50% 0 0)',
        },
        brand: {
          DEFAULT: 'oklch(65% 0.2 145)',
          muted: 'oklch(65% 0.15 145)',
        },
        semantic: {
          success: 'oklch(70% 0.15 145)',
          warning: 'oklch(75% 0.15 85)',
          error: 'oklch(60% 0.2 25)',
        }
      },
      spacing: {
        // Consistent scale
        'micro': '2px',
        'xs': '4px',
        'sm': '8px',
        'md': '12px',
        'lg': '16px',
        'xl': '24px',
        '2xl': '32px',
        '3xl': '48px',
      }
    }
  }
}
```

**Token naming should evoke the product's world.** `--ink` and `--parchment` tell a story. `--gray-700` and `--surface-2` are generic.

## Component Organization

**Use a component-based approach.** Don't repeat long class lists—encapsulate them:

```jsx
// ❌ Repetitive
<button class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg transition-colors">
<button class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg transition-colors">

// ✅ Encapsulated
<Button variant="primary">
<Button variant="primary">
```

**Define variant sets for consistency:**

```jsx
const BUTTON_VARIANTS = {
  primary: "bg-brand hover:bg-brand/90 text-white",
  secondary: "bg-surface-elevated hover:bg-surface-overlay text-ink-primary border border-white/10",
  danger: "bg-semantic-error hover:bg-semantic-error/90 text-white",
};
```

## Class Organization

Keep utility classes organized by category:

```html
<!-- Layout → Spacing → Sizing → Typography → Colors → Effects → States -->
<div class="
  flex items-center justify-between
  gap-4 p-6
  w-full max-w-2xl
  text-sm font-medium
  bg-surface-elevated text-ink-primary
  rounded-lg border border-white/5
  hover:border-white/10 transition-colors
">
```

Use [prettier-plugin-tailwindcss](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) for automatic class sorting.

## Avoid @apply (Mostly)

The `@apply` directive throws away Tailwind's key advantages. Use sparingly—prefer component abstractions instead.

## Mobile-First

Tailwind is mobile-first by default. Base styles apply to mobile, then scale up:

```html
<div class="text-sm md:text-base lg:text-lg">
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
```

## Minimize Utility Classes

Write less, achieve more:

```html
<!-- ❌ Verbose -->
<div class="flex flex-row pt-4 pb-4 border border-solid border-black border-opacity-50">

<!-- ✅ Concise -->
<div class="flex py-4 border border-black/50">
```

---

# Web Design Principles

## User-Centric Design

Start from the end goals of your website:
1. What do users want to find out?
2. Where do they want to go?
3. What do they want to do?
4. What do they want to buy/accomplish?

## Information Hierarchy

Arrange elements so visitors naturally gravitate to the most important information first:
- Use position, color, and size to draw attention
- Headlines grab attention before body text
- CTAs should be immediately visible

## Navigation Clarity

- Keep primary navigation to 5-7 essential items
- Use sticky headers on long pages
- Implement breadcrumbs for deep structures
- Place the logo at top left, linking to homepage
- Use recognizable icons (cart, search, menu)

## Readability

- Use consistent fonts—2-3 font sizes maximum
- Chunk text into short paragraphs
- Use bullet points for scannability
- Contrast text color with backgrounds (4.5:1 minimum ratio)
- Leave plenty of whitespace

## Responsive Design

Over 60% of web traffic is mobile. Every interface must:
- Work on all screen sizes
- Have touch-friendly targets (minimum 44×44px)
- Prioritize above-the-fold content
- Test on real devices, not just emulators

## Performance

Every 100ms delay costs conversions:
- Optimize images (WebP format, srcset for responsive)
- Defer non-critical JavaScript
- Use a CDN
- Enable compression
- Lazy load below-fold content

## Accessibility (WCAG 2.1 AA)

- Provide alt text for all images
- Ensure keyboard navigation works
- Maintain 4.5:1 color contrast ratio
- Don't use color alone to convey information
- Test with screen readers

## CTAs

- Use action-oriented copy: "Get My Free Trial" not "Submit"
- Create visual contrast—make CTAs stand out
- Place above the fold and repeat on long pages
- Use consistent CTAs for the same actions

## Trust Signals

- Display testimonials with photos and names
- Show client logos (B2B)
- Include security badges near checkout
- Feature star ratings and review counts

---

# Design System Documentation

When building consistent interfaces, document your design system. Use the template at `templates/design-system.md`.

A design system should capture:
- Color tokens and their semantic meaning
- Typography scale and usage
- Spacing system
- Component patterns with measurements
- Depth strategy (borders vs shadows)
- Animation conventions

See `references/design-system-template.md` for the full template.

---

# Workflow

## Communication

Be invisible. Don't announce modes or narrate process.

**Never say:** "I'm exploring the domain now...", "Let me check the design system..."

**Instead:** Jump into work. State suggestions with reasoning.

## Suggest + Ask

Lead with your exploration and recommendation, then confirm:

```
"Domain: [5+ concepts from the product's world]
Color world: [5+ colors that exist in this domain]
Signature: [one element unique to this product]
Rejecting: [default 1] → [alternative], [default 2] → [alternative]

Direction: [approach that connects to the above]"

Does that direction feel right?
```

## If Project Has Design System

Read the design system file and apply. Decisions are made.

## If No Design System

1. Explore domain — Produce all four required outputs
2. Propose — Direction must reference all four
3. Confirm — Get user buy-in
4. Build — Apply principles
5. **Evaluate** — Run the mandate checks before showing
6. Offer to save

---

# After Completing a Task

When you finish building something, **always offer to save**:

```
"Want me to save these patterns as a design system for future sessions?"
```

If yes, create a design system file with:
- Direction and feel
- Color tokens (in Tailwind config format)
- Typography choices
- Spacing base unit
- Depth strategy
- Key component patterns

---

# Avoid

- **Generic fonts:** Inter, Roboto, Arial, system fonts without purpose
- **Cliché color schemes:** Purple gradients on white, generic blue CTAs
- **Harsh borders:** If borders are the first thing you see, they're too strong
- **Dramatic surface jumps:** Elevation changes should be whisper-quiet
- **Inconsistent spacing:** Random Tailwind values like `p-[13px] mt-[7px]`
- **Mixed depth strategies:** Pick borders OR shadows, not both randomly
- **Missing states:** hover, focus, disabled, loading, error
- **Large radius on small elements**
- **Pure white cards on colored backgrounds**
- **Multiple accent colors:** Dilutes focus
- **Overusing @apply:** Defeats Tailwind's purpose

---

# Deep Dives

For more detail on specific topics:
- `references/tailwind-practices.md` — Tailwind-specific patterns and optimization
- `references/craft-principles.md` — Surface architecture, tokens, dark mode
- `references/web-design-checklist.md` — UX, accessibility, performance checklist

---

# Commands

- `/ui-design:audit` — Check code against design system
- `/ui-design:extract` — Extract patterns from existing code
- `/ui-design:system` — Generate design system documentation
