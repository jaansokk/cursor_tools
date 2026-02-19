# Cursor Tools

A collection of Cursor **skills**, **agents**, **rules**, and **commands** for building with Cursor. Designed to be used per project or copied to `~/.cursor` for global use across projects.

## Contents

```
.cursor/
├── skills/
│   ├── ui-design/        — Web UI design with Tailwind CSS
│   ├── react-dev/        — React 18+ development
│   └── python-dev/       — FastAPI, SQLAlchemy, Pydantic, pytest
├── agents/
│   ├── engineer.md       — Full-stack coding agent
│   └── verifier.md       — Code review and verification
├── rules/
│   ├── ask-first.mdc     — Ask before assuming on new tasks
│   ├── include-specs.mdc — Use spec-index.md for task scope
│   ├── git-mv-rename.mdc — Always use git mv when renaming
│   └── update-specs.mdc  — Keep specs up to date after implementation
└── commands/
    └── commit-msg.md     — Commit message formatting
```

## Install

### Copy to a specific project

Copy the items you want into your project's `.cursor/` directory:

```sh
cp -r .cursor/skills/ui-design  /your/project/.cursor/skills/
cp -r .cursor/agents             /your/project/.cursor/
```

Restart Cursor to re-index.

### Copy everything globally (`~/.cursor`)

Use the included script to copy all tools to `~/.cursor` for use across all projects:

```sh
./copy-to-global.sh           # copy everything
./copy-to-global.sh --skills  # copy only skills
./copy-to-global.sh --agents  # copy only agents
./copy-to-global.sh --rules   # copy only rules
./copy-to-global.sh --commands # copy only commands
```

## Skills

Skills give the agent specialised knowledge for a domain. Cursor can auto-apply them based on context, or you can invoke them explicitly in Agent chat with `/`.

| Skill | Description |
|-------|-------------|
| `ui-design` | Build distinctive web interfaces with Tailwind CSS. Includes craft checks, design-system templates, and component patterns. |
| `react-dev` | React 18+: components, hooks, state, effects, TypeScript, Tailwind, testing. |
| `python-dev` | FastAPI, SQLAlchemy 2.0, Alembic, Pydantic v2, async Python, pytest. |

## License

MIT — see `LICENSE.txt`.

**Note on sources:** this repo links to external articles and docs for further reading. Those sources are governed by their own licenses/terms.

## References

- Cursor Skills docs: `https://cursor.com/docs/context/skills`
- Tailwind / maintainability:
  - `https://evilmartians.com/chronicles/5-best-practices-for-preventing-chaos-in-tailwind-css`
  - `https://github.com/tailwindlabs/prettier-plugin-tailwindcss`
  - `https://tailwindcss.com/docs/reusing-styles#avoiding-premature-abstraction`
