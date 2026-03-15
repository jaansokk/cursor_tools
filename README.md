# Cursor & Claude Tools

A collection of **skills**, **agents**, **rules**, and **commands** for Cursor and Claude Code. Designed to be used per project or synced to `~/.cursor` / `~/.claude` for global use across projects.

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

.claude/
├── CLAUDE.md             — Global workflow and stack guidelines
├── settings_example.json — Permission/settings template
├── agents/
│   ├── codex-coder.md    — Coding delegation via Codex CLI
│   ├── researcher.md     — Research & evaluation specialist
│   └── verifier.md       — QA verification specialist
└── skills/
    ├── code-review-codex/ — Code review skill
    ├── commit/            — Commit message formatting
    ├── python-dev/        — FastAPI, SQLAlchemy, Pydantic, pytest
    ├── react-dev/         — React 18+ development
    ├── spec-review-codex/ — Spec review skill
    └── ui-design/         — Web UI design with Tailwind CSS
```

## Install

### Copy to a specific project

Copy the items you want into your project's `.cursor/` or `.claude/` directory:

```sh
cp -r .cursor/skills/ui-design  /your/project/.cursor/skills/
cp -r .claude/agents             /your/project/.claude/
```

Restart Cursor / Claude Code to re-index.

### Sync globally

Use the included scripts to sync tools to `~/.cursor` or `~/.claude` for use across all projects:

**Cursor** (`scripts/sync_cursor.sh`):

```sh
scripts/sync_cursor.sh              # sync everything
scripts/sync_cursor.sh --agents     # sync only agents
scripts/sync_cursor.sh --skills     # sync only skills
scripts/sync_cursor.sh --rules      # sync only rules
scripts/sync_cursor.sh --commands   # sync only commands
```

**Claude Code** (`scripts/sync_claude.sh`):

```sh
scripts/sync_claude.sh              # sync everything
scripts/sync_claude.sh --agents     # sync only agents
scripts/sync_claude.sh --skills     # sync only skills
scripts/sync_claude.sh --claude-md  # sync only CLAUDE.md
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
- Claude Code docs: `https://docs.anthropic.com/en/docs/claude-code`
- Tailwind / maintainability:
  - `https://evilmartians.com/chronicles/5-best-practices-for-preventing-chaos-in-tailwind-css`
  - `https://github.com/tailwindlabs/prettier-plugin-tailwindcss`
  - `https://tailwindcss.com/docs/reusing-styles#avoiding-premature-abstraction`
