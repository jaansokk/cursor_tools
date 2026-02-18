# Write a descriptive commit message with a description

- Write a conventional commit message about the changes since the last commit in the current branch.
- Format: `type(scope): summary`
- Use **imperative mood** (e.g. "add", "fix", "update"), keep summary **<= 72 chars**
- 1–2 sentences on the **why / impact** (not a file-by-file recap)
- Add a bullet list of the changes, grouped by area if the scope is wide enough.
- Tests: if tests were run, list. If no coverage or N/A, omit this.
- Give the message as a MD snippet in chat, do not make the commit automatically.