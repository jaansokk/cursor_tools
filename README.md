# ui-design (Cursor Skill)

A Cursor Agent Skill for designing and implementing **high-quality web UI** using **Tailwind CSS**, with explicit intent, craft checks, and design-system-first constraints.

## What this skill is for

- Building **production-grade** UIs (components, pages, dashboards, apps)
- Avoiding “template energy” by forcing **specificity** (who/what/why) + a **signature**
- Keeping Tailwind maintainable via **tokens**, **scales**, and **variants**
- Documenting a **design system spec** (template included)

## Install

Copy this folder into your project:

```
.cursor/skills/ui-design/
```

Then restart Cursor so it re-indexes skills.

## Use

- Cursor can auto-apply skills based on context.
- You can also explicitly invoke it in Agent chat by typing `/` and selecting `ui-design` (see Cursor docs).

## Included files

```
ui-design/
├── SKILL.md
├── README.md
├── LICENSE.txt
├── references/
│   ├── craft-principles.md
│   ├── tailwind-practices.md
│   └── web-design-checklist.md
└── templates/
    └── design-system.md
```

## License

This skill’s original content is licensed under **MIT** (see `LICENSE.txt`).

**Note on sources:** this repo links to external articles and docs for further reading. Those sources are governed by their own licenses/terms.

## References / sources

- Cursor Skills docs: `https://cursor.com/docs/context/skills`
- Tailwind / maintainability:
  - `https://evilmartians.com/chronicles/5-best-practices-for-preventing-chaos-in-tailwind-css`
  - `https://www.uxpin.com/studio/blog/tailwind-best-practices/`
  - `https://github.com/tailwindlabs/prettier-plugin-tailwindcss`
  - `https://tailwindcss.com/docs/reusing-styles#avoiding-premature-abstraction`
- Web design best practices:
  - `https://contentsquare.com/guides/web-design/best-practices/`
  - `https://www.sugarpixels.com/best-practices-for-web-design/`

### Inspiration (local references)

This skill was created using local reference materials in your workspace:

- `ref/interface-design-main/.claude/skills/interface-design/` (MIT licensed upstream; see `ref/interface-design-main/LICENSE`)
- `ref/claude_frontend_SKILL.md`

