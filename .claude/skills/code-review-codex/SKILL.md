---
name: code-review-codex
description: Final-gate code review via Codex CLI (codex-5.3, xhigh). Finds bugs, security issues, and regressions before commit. No edits — findings report only.
disable-model-invocation: true
---

# Code Review via Codex CLI

A **read-only, post-implementation review** using OpenAI Codex CLI as an independent second opinion. The goal is to catch real issues before commit, not to make edits.

## When to use

- After completing a feature, fix, or refactor — as the last step before committing
- When the user says "review", "check my code", "final review", or "sanity check"
- For security or correctness confidence on sensitive code paths

## Behavior

- **Read-only**: Codex reviews and reports. No files are modified.
- **Report back**: Output is returned to Claude as structured findings for the user to triage.
- **Skip noise**: No style nits, no formatting opinions, no "consider renaming" suggestions.

## Steps

1. **Determine scope** from `$ARGUMENTS`:
   - No arguments → review uncommitted changes (`--uncommitted`)
   - Branch name (e.g. `main`) → review diff against that branch (`--base <branch>`)

2. **Run the Codex review** using `codex exec` (supports full prompt alongside diff scope):

### Uncommitted changes (default):

```bash
codex exec \
  -m gpt-5.3-codex \
  -c model_reasoning_effort='"xhigh"' \
  -s read-only \
  --ephemeral \
  -o /tmp/code-review-output.md \
  "You are a senior engineer doing a final gate review on code that is about to be committed. This is post-implementation — the work is done, you are looking for real problems only.

Start by running: git diff HEAD to see all uncommitted changes (staged and unstaged). Also run git status to catch untracked files that may be relevant.

Review ONLY for issues that would cause bugs, outages, security incidents, or serious perf regressions in production. Ignore style, naming, formatting, and minor code smells.
Use the context7 MCP to check documentation of libraries when needed.

## Review checklist

### 1. Correctness
- Logic errors: wrong conditions, off-by-one, inverted checks, unreachable branches
- State bugs: stale closures, race conditions, mutations of shared state
- Null/undefined access, unhandled promise rejections, uncaught exceptions
- Incorrect API usage or wrong assumptions about library behavior
- Edge cases: empty inputs, boundary values, concurrent access

### 2. Security
- Injection vectors: SQL, XSS, command injection, path traversal
- Auth/authz gaps: missing permission checks, broken access control
- Secrets or credentials in code, logs, or error messages
- Insecure defaults: permissive CORS, disabled CSRF, weak crypto
- User input flowing unsanitized to sensitive sinks

### 3. Data integrity
- Missing or incorrect validation at system boundaries (API inputs, DB writes, file I/O)
- Silent data loss: swallowed errors, ignored return values, dropped events
- Inconsistent state from partial failures (no transaction, no rollback)

### 4. Performance (only if clearly problematic)
- N+1 queries, unbounded loops over large datasets
- Blocking calls in async/event-loop code
- Missing pagination or limits on user-controlled queries
- Obvious memory leaks (growing caches, unclosed resources, dangling listeners)

### 5. Robustness
- Error handling: catch blocks that swallow context, missing retry/backoff on network calls
- Missing timeouts on external calls (HTTP, DB, queues)
- Failure modes that cascade (one failing dependency takes down everything)

## Output format

For each finding:
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW
- **File:Line**: exact location
- **What**: one-sentence description of the problem
- **Why it matters**: what breaks or goes wrong in production
- **Fix**: concrete code suggestion or approach (keep it short)

Group findings by severity (CRITICAL first). If nothing significant is found, say so — a clean review is a valid outcome.

End with a one-line verdict: PASS (ship it), PASS WITH NOTES (minor items), or BLOCK (must fix before commit)."
```

### Branch diff:

```bash
codex exec \
  -m gpt-5.3-codex \
  -c model_reasoning_effort='"xhigh"' \
  -s read-only \
  --ephemeral \
  -o /tmp/code-review-output.md \
  "You are a senior engineer doing a final gate review on code that is about to be committed. This is post-implementation — the work is done, you are looking for real problems only.

Start by running: git diff <branch>...HEAD to see all changes on this branch relative to <branch>. Also run git log <branch>..HEAD --oneline to understand the commit scope.

Review ONLY for issues that would cause bugs, outages, security incidents, or serious perf regressions in production. Ignore style, naming, formatting, and minor code smells.
Use the context7 MCP to check documentation of libraries when needed.

## Review checklist

### 1. Correctness
- Logic errors: wrong conditions, off-by-one, inverted checks, unreachable branches
- State bugs: stale closures, race conditions, mutations of shared state
- Null/undefined access, unhandled promise rejections, uncaught exceptions
- Incorrect API usage or wrong assumptions about library behavior
- Edge cases: empty inputs, boundary values, concurrent access

### 2. Security
- Injection vectors: SQL, XSS, command injection, path traversal
- Auth/authz gaps: missing permission checks, broken access control
- Secrets or credentials in code, logs, or error messages
- Insecure defaults: permissive CORS, disabled CSRF, weak crypto
- User input flowing unsanitized to sensitive sinks

### 3. Data integrity
- Missing or incorrect validation at system boundaries (API inputs, DB writes, file I/O)
- Silent data loss: swallowed errors, ignored return values, dropped events
- Inconsistent state from partial failures (no transaction, no rollback)

### 4. Performance (only if clearly problematic)
- N+1 queries, unbounded loops over large datasets
- Blocking calls in async/event-loop code
- Missing pagination or limits on user-controlled queries
- Obvious memory leaks (growing caches, unclosed resources, dangling listeners)

### 5. Robustness
- Error handling: catch blocks that swallow context, missing retry/backoff on network calls
- Missing timeouts on external calls (HTTP, DB, queues)
- Failure modes that cascade (one failing dependency takes down everything)

## Output format

For each finding:
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW
- **File:Line**: exact location
- **What**: one-sentence description of the problem
- **Why it matters**: what breaks or goes wrong in production
- **Fix**: concrete code suggestion or approach (keep it short)

Group findings by severity (CRITICAL first). If nothing significant is found, say so — a clean review is a valid outcome.

End with a one-line verdict: PASS (ship it), PASS WITH NOTES (minor items), or BLOCK (must fix before commit)."
```

3. **Present the review output** to the user exactly as returned. Do not edit, summarize, or reformat the findings.

$ARGUMENTS