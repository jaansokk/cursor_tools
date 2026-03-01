---
name: commit
description: Generate a conventional commit message for staged changes
disable-model-invocation: true
---

Write a conventional commit message about the changes since the last commit in the current branch.

1. Run `git diff --cached` to see staged changes (or `git diff` if nothing staged)
2. Run `git log --oneline -5` to see recent commit style

Format:
- `type(scope): summary` — imperative mood, <= 72 chars
- Types: feat, fix, refactor, docs, test, chore, style, perf
- 1-2 sentences on the **why / impact** (not a file-by-file recap)
- Bullet list of changes, grouped by area if scope is wide
- If tests were run, note results. If no coverage or N/A, omit

Present the message as a markdown snippet in chat. Do not make the commit automatically.

$ARGUMENTS
