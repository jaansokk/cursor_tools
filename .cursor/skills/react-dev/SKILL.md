---
name: react-dev
description: >
  React 18+ development: components, hooks, state, effects, TypeScript, Tailwind CSS,
  performance, accessibility, testing, and security. Use when building or modifying
  React UI, state management, hooks/effects, forms, styling, or frontend tests.
metadata:
  version: "0.2"
  scope: "React (web) / JSX / TSX"
---

# React Development

## When to use this skill

Use this whenever you are asked to:
- Build or refactor React components, hooks, or UI flows
- Fix bugs involving state, effects, rendering, or controlled inputs
- Improve performance (unnecessary re-renders, slow lists, heavy computations)
- Work with Tailwind CSS styling or responsive design
- Add/repair accessibility (semantic HTML, keyboard support, ARIA)
- Write or update frontend tests (React Testing Library)

For UI/styling work that requires high design quality, also read the UI Design skill at `.cursor/skills/ui-design/SKILL.md`.

## Outcome targets

- **Correctness:** no hook rule violations, no state mutation, no effect loops, no controlled/uncontrolled switching
- **Maintainability:** clear component boundaries, minimal state, readable data flow
- **Type safety:** strict TypeScript at all boundaries — no `any`
- **UX + A11y:** semantic HTML first; predictable focus and keyboard behavior
- **Performance:** measure before optimizing; optimize the right bottleneck
- **Safety:** avoid XSS footguns; never inject untrusted HTML

---

## Stack and tooling

- **React 18+** — functional components, hooks, concurrent features
- **TypeScript** — strict typing, generics, discriminated unions
- **Tailwind CSS** — utility-first styling, responsive design, design tokens
- **Vite** — fast dev server, build config, env handling
- **State management** — Zustand, React context, local state (pick the right level)
- **Testing** — React Testing Library, user-event, vitest/jest

---

## Coding standards

1. **TypeScript strict** — type all props, callbacks, state. Avoid `any`.
2. **Functional components only** — no class components.
3. **Tailwind for styling** — no CSS modules or inline style objects unless absolutely necessary.
4. **Small, composable components** — one responsibility per component. Extract early.
5. **Minimal state** — derive in render what you can. Don't duplicate data across state slices.
6. **Accessible by default** — semantic HTML, keyboard nav, visible focus, ARIA when needed.
7. **No side effects in render** — effects are for external synchronization only.

---

## Best-practice rules

### A) Components and Hooks must be pure

- Render functions must be **pure and idempotent**: same inputs (props/state/context) -> same JSX.
- Do not perform side effects during render (no subscriptions, no direct DOM mutation, no network calls).
- Keep event handlers as the primary place where user actions trigger state updates.

### B) Follow the Rules of Hooks

- Call Hooks **only at the top level** of React components or custom hooks.
- Never call Hooks inside loops, conditions, or nested functions.
- Prefer enabling and respecting `eslint-plugin-react-hooks` (rules-of-hooks + exhaustive-deps).

### C) State modeling: keep it minimal and coherent

- Prefer the smallest state that can drive the UI:
  - Avoid **redundant/derived state** (compute during render or memoize if expensive).
  - Avoid **deeply nested state**; normalize when it grows.
  - Keep a single source of truth.
- When multiple components must stay in sync:
  - **Lift state up** to the closest common parent.
  - Consider `useReducer` for complex update logic; combine with `Context` when passing deeply.

### D) Never mutate props/state

- Treat props/state as immutable snapshots.
- Update objects/arrays by creating new ones (spread, map/filter, or Immer if already used).
- Do not mutate values read from state and then call setState with the same reference.

### E) Effects are for external synchronization only

Use `useEffect` when synchronizing with an **external system**, e.g.:
- Browser APIs (timers, observers), subscriptions, manual DOM work, network (when not handled by a framework/data layer)

Rules:
- Don't use effects to orchestrate your app's internal data flow.
- Always declare the full dependency list; avoid "lying" dependency arrays.
- Implement cleanup for subscriptions/timers/listeners.
- Expect Strict Mode to run an extra setup/cleanup cycle in development; your effect should be resilient.

### F) Refs are for "escape hatches"

Use `useRef` for:
- Holding mutable values that shouldn't trigger renders (timeouts, previous values, instance handles)
- Accessing DOM nodes (focus, measurement) sparingly

Avoid using refs to replace state for UI rendering.

### G) Lists: keys must be stable

- Use stable IDs from data for `key`.
- Avoid array indices as keys when items can reorder/insert/delete (it breaks state preservation and causes UI glitches).
- Never generate keys during render (e.g., `Math.random()`).

### H) Forms: pick controlled vs uncontrolled and stick to it

- **Controlled** inputs (`value` + `onChange`) when you need validation, conditional UI, or instant feedback.
- **Uncontrolled** inputs (`defaultValue` / refs / `FormData`) for simpler forms.
- Never switch an input between controlled and uncontrolled across renders.

---

## TypeScript

- Type props, callbacks, and event handlers at component boundaries.
- Use `React.ComponentProps<"button">` / `ComponentPropsWithoutRef` for wrapper components.
- Avoid `any`; prefer explicit unions and narrowing.
- Keep prop types readable; don't over-genericize until needed.

---

## Performance guidance

- **Measure first** (React DevTools Profiler) before optimizing.
- Prefer structural fixes over micro-optimizations:
  - Split large components; colocate state near where it's used.
  - Avoid passing "new" object/function props to memoized children unless needed.
- Use memoization tools intentionally:
  - `memo` to skip re-renders when props are stable
  - `useMemo` for expensive calculations
  - `useCallback` when function identity stability matters (prop to memoized children / hook deps)
- Be mindful with Context:
  - Context updates re-render consumers; keep provider values stable and consider splitting contexts by concern.

---

## Accessibility

- Prefer **semantic HTML** ("right element for the right job") before ARIA.
- Ensure every interactive control has an **accessible name** (visible label, `aria-label`, or `aria-labelledby`).
- Ensure keyboard accessibility:
  - Tab order makes sense
  - Focus is visible and managed for dialogs/menus
- When building custom widgets, follow the WAI-ARIA Authoring Practices patterns.

---

## Testing

- Use Testing Library's principles:
  - Test the app like a user uses it.
  - Prefer queries by role + accessible name (`getByRole`, `findByRole`).
  - Avoid testing implementation details (DOM structure, internal state, private methods).
- Prefer `@testing-library/user-event` over low-level `fireEvent` for realistic interactions.

---

## Security

- Avoid `dangerouslySetInnerHTML`. If you must render HTML:
  - Only render **trusted** content or sanitize it with a well-reviewed sanitizer.
- Use defense-in-depth:
  - Configure CSP where possible.
  - Follow OWASP XSS prevention guidance.

---

## Common failure modes (fast triage)

| Symptom | Likely cause | Fix |
|---|---|---|
| Infinite render/effect loop | Effect sets state + deps cause re-run | Move logic to render derivation or fix deps |
| Stale closures | Effect/handler reads old state | Ensure deps are correct or use functional updates |
| "Rendered fewer hooks" | Hooks inside condition/loop | Refactor so hooks are unconditional |
| Controlled/uncontrolled warning | `value` flips between `undefined` and defined | Initialize state and keep consistent |
| List UI glitches | Unstable keys | Fix keys to stable IDs |

---

## Sources

### React (official)
- Keeping Components Pure — https://react.dev/learn/keeping-components-pure
- Components and Hooks must be pure — https://react.dev/reference/rules/components-and-hooks-must-be-pure
- You Might Not Need an Effect — https://react.dev/learn/you-might-not-need-an-effect
- useEffect — https://react.dev/reference/react/useEffect
- useState (immutability notes) — https://react.dev/reference/react/useState
- Choosing the State Structure — https://react.dev/learn/choosing-the-state-structure
- Sharing State Between Components — https://react.dev/learn/sharing-state-between-components
- useContext — https://react.dev/reference/react/useContext
- memo / useMemo / useCallback — https://react.dev/reference/react/memo ; https://react.dev/reference/react/useMemo ; https://react.dev/reference/react/useCallback
- eslint-plugin-react-hooks — https://react.dev/reference/eslint-plugin-react-hooks
- Using TypeScript — https://react.dev/learn/typescript
- Profiler — https://react.dev/reference/react/Profiler

### Accessibility
- MDN: HTML accessibility — https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML
- W3C: ARIA Authoring Practices — https://www.w3.org/WAI/ARIA/apg/
- W3C: WCAG 2.2 — https://www.w3.org/TR/WCAG22/

### Testing
- Testing Library Guiding Principles — https://testing-library.com/docs/guiding-principles/
- React Testing Library — https://testing-library.com/docs/react-testing-library/intro/
- user-event — https://testing-library.com/docs/user-event/intro

### Security
- OWASP: XSS Prevention — https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- MDN: CSP — https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP
