# Codex, Claude & Cursor Tools

A collection of **skills**, **agents**, **rules**, and **commands** for Codex, Claude Code, and Cursor. Designed for project or user-level use.

UI Design has one authored source at `skills/ui-design/`. The repository entries at `.codex/skills/ui-design`, `.claude/skills/ui-design`, and `.cursor/skills/ui-design` are relative symlinks to it. Edit the shared source; keep tool-specific metadata in its `agents/` directory. Installed packages are independent copies so they do not depend on the repository location.

## Contents

```
.cursor/
├── skills/
│   ├── ui-design/        — Link to shared UI design principles
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
    └── ui-design/         — Link to shared UI design principles
```

## Install

### Copy to a specific project

Use the scoped installer for UI Design. Pass the complete destination directory, ending in `ui-design`; it works for Codex, Claude, and Cursor:

```sh
python3 scripts/install_ui_design.py /your/project/.cursor/skills/ui-design
```

It replaces only that skill package, removes superseded files, and backs up the prior package outside the `skills/` directory. Other tools can be copied as before:

```sh
cp -r .claude/agents             /your/project/.claude/
```

Restart or reload the relevant tool to re-index.

### Sync globally

To install only UI Design at the user level, use the scoped installer with the desired destination:

```sh
python3 scripts/install_ui_design.py ~/.codex/skills/ui-design
python3 scripts/install_ui_design.py ~/.claude/skills/ui-design
python3 scripts/install_ui_design.py ~/.cursor/skills/ui-design
```

These commands replace the active skill with the version in the current checkout. The broader Claude and Cursor sync scripts also use this installer for UI Design; their other skills retain the existing copy behavior. The installer requires Python 3.

Use the included scripts to sync other tools to `~/.cursor` or `~/.claude` for use across all projects:

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
| `ui-design` | Framework-independent UI principles: function first, Gestalt grouping, spacing, hierarchy, readable typography, purposeful color, and explicit project choices. Includes six annotated design articles and an optional project-decision template. |
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
