---
name: react-dev
description: >
  React frontend conventions for this project. Use when building or modifying
  React components, hooks, state management, styling, or frontend tests.
---

# React Conventions

## Stack choices

- **React 18+** with functional components only — no class components
- **TypeScript strict** — type all props, callbacks, state. No `any`
- **Tailwind CSS** exclusively — no CSS modules, no inline style objects unless absolutely necessary
- **Vite** for dev server and builds
- **Zustand** for shared state (not Redux, not Context for state management)
- **React Testing Library** + **user-event** + **vitest** for testing

## Coding standards

- Small, composable components — one responsibility per component, extract early
- Minimal state — derive in render what you can, don't duplicate data across state slices
- Lift state up to the closest common parent when components must stay in sync
- Use `useReducer` for complex update logic
- Accessible by default — semantic HTML first, ARIA only when semantic elements aren't sufficient
- Ensure keyboard accessibility and visible focus on all interactive controls

## Styling

- Utility-first Tailwind — organize classes: layout, spacing, sizing, typography, colors, effects, states
- Use component abstractions (variant objects/props) instead of repeating long class lists
- Mobile-first responsive: base styles for mobile, scale up with `md:`, `lg:`
- Use `prettier-plugin-tailwindcss` for class sorting

## Testing

- Test like a user — prefer queries by role + accessible name (`getByRole`, `findByRole`)
- Use `@testing-library/user-event` over `fireEvent`
- Don't test implementation details (DOM structure, internal state, private methods)

## Workflow

- Orient before coding — read existing components in the area, match existing patterns
- Small, focused changes — one component or concern at a time, don't refactor unrelated code
- Write tests alongside implementation — new components and hooks should ship with tests
- Validate after edits — run `tsc` and the linter, run tests if they exist in the area

## Principles

- **Speak up.** If you spot code that contradicts conventions, has a latent bug, unnecessary complexity, or a missed optimization — flag it. Don't silently work around issues.
- **Verify against documentation** Use the context7 MCP to check documentation of libraries when needed.
- **Ask, don't assume.** If requirements are ambiguous or you face a non-obvious UI/state design choice, ask for clarification before proceeding.
- **Stay scoped.** If you discover an issue outside your current task, report it instead of silently fixing it. Exception: trivial fixes (typos, obvious off-by-one) that take seconds.
- **Leave code better than you found it** — but only in the files you're already touching.
