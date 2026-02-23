---
name: codex-review
description: >
  Run code reviews with the Codex CLI, prioritizing bugs, regressions, security risks,
  and missing tests. Use when the user asks for code review, PR review, diff review,
  or commit-range review via codex.
metadata:
  version: "0.1"
  scope: "Codex CLI / Git diff and PR review"
---

# Codex Review

## When to use this skill

Use this whenever the user asks to:
- Review local changes, staged changes, or a commit range
- Review a branch or pull request with Codex CLI
- Run a second-opinion review focused on correctness and risk

## Default model

- Default to `gpt-5.3-codex`.
- Baseline command:

```bash
codex -m gpt-5.3-codex
```

- Current docs recommend `gpt-5.3-codex` as the default coding model.
- A separate `gpt-5.3-codex-high` slug is not documented in the public model list.
- If the user explicitly wants to try a high-reasoning alias anyway, attempt it once and fall back to `gpt-5.3-codex` if unavailable.

## Review workflow

1. Scope the review target first:
   - working tree (`git diff`)
   - staged only (`git diff --staged`)
   - commit range (`git diff <base>...<head>`)
2. Gather context:
   - `git status --short`
   - `git log --oneline -n 20`
   - relevant diff output
3. Ask Codex for a risk-focused review (not a style nit pass).
4. Return findings ordered by severity, with concrete file/symbol references and suggested fixes.
5. Always call out test gaps and regression risk if coverage is unclear.

## Command templates

### A) Review current local changes (interactive)

```bash
codex -m gpt-5.3-codex "Review the current repository changes.
Focus on correctness bugs, behavioral regressions, security issues, and missing tests.
Ignore low-value style nits.
Return findings ordered by severity with file paths and concise fix suggestions."
```

### B) Review staged diff (non-interactive)

```bash
codex -m gpt-5.3-codex -q "$(cat <<'EOF'
Review the staged git diff in this repository.
Prioritize:
1) correctness and logic flaws,
2) behavioral regressions,
3) security concerns,
4) missing/weak tests.

Output format:
- Severity: Critical/High/Medium/Low
- File: path
- Issue: short title
- Why it matters
- Suggested fix
EOF
)"
```

### C) Optional model override with fallback

```bash
MODEL="gpt-5.3-codex-high"
codex -m "$MODEL" -q "Review current changes for bugs, regressions, security, and missing tests." \
  || codex -m gpt-5.3-codex -q "Review current changes for bugs, regressions, security, and missing tests."
```

## Review quality bar

- Findings first; no long preamble.
- Prefer high-signal issues over broad commentary.
- Include exact failure mode or scenario whenever possible.
- Mark uncertain points as assumptions.
- If no material issues are found, state that explicitly and list residual risks.
