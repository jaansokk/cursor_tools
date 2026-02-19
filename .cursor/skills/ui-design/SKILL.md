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

- **The squint test:** Blur your eyes. Can you still perceive hierarchy? Is anything jumping out harshly?

- **The contrast test:** Take a screenshot and view it at 50% zoom. Can you still distinguish every card from its background? Can you read every text element? If any boundary disappears or any text blurs into its surface — raise the contrast. This is the most common AI failure mode.

- **The arm's-length test:** Imagine viewing this on a cheap office monitor at arm's length. Borders at `white/5`, text at `stone-400` on `white` — these vanish. If it only looks good on a retina display at close range, it fails.

- **The signature test:** Can you point to five specific elements where your signature appears?

- **The Tailwind test:** Read your utility classes. Do they feel intentional or like copy-paste from documentation?

- **The generic AI test:** Does this look like something every AI would produce? Purple gradients, Inter font, predictable card grids, generic hero sections?

---

# Craft Foundations

## Layering & Contrast

This is the backbone of craft. Study Vercel, Supabase, Linear — but do not confuse subtlety with invisibility.

**Surfaces must be distinguishable at arm's length on a non-retina display.** Quiet, not silent. If you squint and two surfaces merge, you've gone too far.

**Borders must be visible without hunting.** A user glancing at the interface should perceive structure. Borders do not need to shout, but they must register.

### Light Mode

Light mode contrast is deceptive — white-on-near-white is the most common failure. Use named palette steps, not raw opacity on black.

```html
<!-- Light mode surfaces -->
<div class="bg-stone-50">                          <!-- Level 0: Canvas -->
  <div class="bg-white border border-stone-200/60 shadow-sm">  <!-- Level 1: Cards -->
    <div class="bg-stone-50">                      <!-- Level 2: Inset/nested -->
    </div>
  </div>
</div>

<!-- Light mode borders — minimum thresholds -->
<div class="border border-stone-200/60">           <!-- Subtle (floor) -->
<div class="border border-stone-200">              <!-- Default -->
<div class="border border-stone-300">              <!-- Strong / hover -->
```

### Dark Mode

In dark mode, use opacity on white — but never below `/8` for any visible boundary.

```html
<!-- Dark mode surfaces -->
<div class="bg-slate-950">                         <!-- Level 0: Base -->
  <div class="bg-slate-900/70">                    <!-- Level 1: Cards -->
    <div class="bg-slate-800/50">                  <!-- Level 2: Elevated -->
    </div>
  </div>
</div>

<!-- Dark mode borders — minimum thresholds -->
<div class="border border-white/8">                <!-- Subtle (floor) -->
<div class="border border-white/15">               <!-- Default -->
<div class="border border-white/25">               <!-- Strong / hover -->
```

### The Contrast Floor

These are non-negotiable minimums, not targets:
- **Borders:** Must be visible without pixel-peeping. `border-white/5` and `border-black/5` are effectively invisible on most displays — never use them.
- **Surface steps:** Adjacent elevation levels must differ by enough that a screenshot at 50% zoom still shows the boundary.
- **Text on surfaces:** Every text token must pass WCAG AA (4.5:1) against its background. Muted/caption text at `stone-500` on `white` is the floor for light mode.

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

## Data-Dense Contexts

Dashboards, tables, analytics, trading interfaces — these need **more** contrast, not less. When information density is high, subtle layering works against the user.

**Raise contrast when:**
- Multiple data blocks compete for attention on one screen
- Tables have many rows/columns — row borders and alternating backgrounds must be clearly visible
- Small text (captions, labels, axis ticks) sits on colored or tinted backgrounds
- Charts sit inside cards that sit on a canvas — three elevation levels need three distinct steps

**Practical rules for dense UIs:**
- Card borders: use named palette steps (`stone-200`, `stone-300`) not raw opacity
- Table dividers: `divide-stone-100` minimum, `divide-stone-200` for busy tables
- Context bars / toolbars: `bg-stone-200/40` with `border-stone-300/40` — distinctly different from both canvas and cards
- Numbers and data: monospace, `tabular-nums`, and sufficient weight to read at small sizes

The "whisper-quiet" philosophy applies to marketing sites and reading apps. Data tools need structure you can see.

## Font Alternatives

The skill says no Inter, no Roboto. Here are distinctive alternatives by category:

**Geometric / Clean:** Satoshi, General Sans, Outfit, Plus Jakarta Sans, Switzer
**Humanist / Warm:** Manrope, Source Sans 3, Nunito Sans, Atkinson Hyperlegible
**Technical / Precise:** JetBrains Mono (data), IBM Plex Sans, DM Sans, Geist
**Editorial / Expressive:** Fraunces, Newsreader, Literata, Instrument Serif
**Display / Distinctive:** Cabinet Grotesk, Clash Display, Zodiak, Erode

Pick based on the product's feel, not "what looks nice." A bakery management tool might use Nunito Sans. A trading terminal might use DM Sans + JetBrains Mono. An architecture portfolio might use another font.

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
          secondary: 'oklch(75% 0 0)',
          muted: 'oklch(55% 0 0)',
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
  secondary: "bg-surface-elevated hover:bg-surface-overlay text-ink-primary border border-white/15",
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
  rounded-lg border border-white/15
  hover:border-white/25 transition-colors
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

See `templates/design-system.md` for the full template.

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
- **Invisible borders:** `border-white/5`, `border-black/5` are invisible on most displays. The floor is `/8` dark mode, `stone-200/60` light mode
- **Invisible elevation:** If cards don't visually separate from canvas in a 50%-zoom screenshot, contrast is too low
- **Dramatic surface jumps:** Elevation changes should be calm but perceptible — not whisper-quiet to the point of vanishing
- **Inconsistent spacing:** Random Tailwind values like `p-[13px] mt-[7px]`
- **Random depth mixing:** Combining border + shadow intentionally is fine. Randomly switching between borders-only, shadows-only, and combined across similar elements is not
- **Missing states:** hover, focus, disabled, loading, error
- **Large radius on small elements**
- **Pure white cards on colored backgrounds**
- **Multiple accent colors:** Dilutes focus
- **Overusing @apply:** Defeats Tailwind's purpose
- **Muted text that fails WCAG:** `stone-400` on `white` fails AA. `stone-500` is the floor for muted text on white backgrounds

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
