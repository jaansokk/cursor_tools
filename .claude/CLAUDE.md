# Workflow

- Ask before assuming — if uncertain about user intent or architecture choices, clarify first
- Orient before coding — read existing code in the area, match existing patterns and conventions
- Small, focused changes — don't refactor unrelated code, stay within scope
- Write tests alongside implementation — don't leave testing as a separate step
- Validate after edits — check for type errors and lint issues, run tests if they exist
- If you spot issues outside your current scope, flag them instead of silently fixing (exception: trivial fixes that take seconds)

# Specs

- When `_specs/spec-index.md` exists, use it to determine task scope and acceptance criteria
- After implementation, review if specs need updating so they don't lag behind

# Git

- Use `git mv` when moving or renaming files to preserve git history
- If database models change, create a new Alembic migration revision

# Stack

- Frontend: React 18+, TypeScript (strict), Tailwind CSS, Vite, Zustand
- Backend: Python, FastAPI, SQLAlchemy 2.0, Pydantic v2, Alembic
- Testing: React Testing Library + vitest (frontend), pytest + pytest-asyncio (backend)

# Context management

## Delegation
- Delegate heavy exploration (multi-file search, codebase understanding) to Explore subagents
- Delegate test runs and verbose output to subagents — keep results summaries in main context
- For large implementation tasks spanning many files, break into sequential subagent calls

## Loop detection
- If an approach fails 3 times (same error, same fix attempt), stop immediately
- Report: what was tried, why it failed each time, and 2-3 alternative approaches to consider
- Do not continue retrying — let the user decide the next direction

## Compaction
- Before running `/compact`, assess: will compacting help towards the quality and successful completion of the current task or a logical stepping-stone? If not, don't compact — stop instead
- When compacting, specify what context to preserve (e.g., current debugging state, architectural decisions made, files modified)

## Hard stop at 85% context
- At 85% context capacity, stop implementation and produce a structured handoff:
  - **Completed:** what was done in this session
  - **Remaining:** what still needs to be implemented
  - **Key context:** decisions made, patterns established, gotchas discovered
  - **Blockers:** any open questions or unresolved issues
- Do not compact and push through — quality degrades in the last 15% of context
- The next session or resumed agent should be able to pick up immediately from the handoff
