---
name: spec-review-codex
description: >
  Review project specs for internal conflicts, goal-vs-implementation drift, ambiguity,
  and implementability gaps. Uses OpenAI Codex CLI with gpt-5.2 at xhigh reasoning effort.
  Read-only — produces a findings report, no edits.
  Use when the user says "review specs", "check specs", "spec review", "audit specs",
  or after major spec changes to catch issues before implementation begins.
disable-model-invocation: true
---

# Spec Review via Codex CLI

A **read-only review** of the project's `_specs/` directory using Codex as an independent reviewer. The goal is to surface problems that would cause confusion, rework, or wrong implementations — before engineering time is wasted.

## When to use

- After writing or significantly updating specs, before starting implementation
- Periodically as a health check when specs have grown organically
- When onboarding to understand spec quality and gaps

## Behavior

- **Read-only**: No files are modified. Output is a findings report.
- **Cross-references codebase**: Where specs reference implementation details, the reviewer checks actual code for drift.
- **Focuses on actionable issues**: Not a style guide audit — only problems that would mislead an implementer or cause rework.

## Steps

1. **Check for specs directory**:
   - If `_specs/` does not exist, report: "No `_specs/` directory found. Nothing to review." and stop.

2. **Read the spec index** (`_specs/spec-index.md` if it exists, otherwise list `_specs/` contents) to understand the structure.

3. **Run the review via Codex CLI**:

```bash
codex exec \
  -m gpt-5.2 \
  -c model_reasoning_effort='"xhigh"' \
  -s read-only \
  --ephemeral \
  -o /tmp/spec-review-output.md \
  "You are a senior product engineer reviewing project specs before implementation. Your job is to catch problems that would cause an engineer to build the wrong thing, build it twice, or get stuck.

Start by reading _specs/spec-index.md (if it exists) to understand the spec structure, then read every spec file under _specs/. Also read relevant source code when specs reference implementation details — you need to check for drift.

Review the specs against the following checklist. Only report real problems — skip minor wording preferences.

Use the context7 MCP to check documentation of libraries when needed.

## Review checklist

### 1. Internal contradictions
- Specs that directly conflict with each other (different stated behaviors for the same feature)
- Inconsistent terminology (same concept called different names, or same name meaning different things)
- Conflicting constraints (e.g., one spec says sync, another says async for the same flow)
- Version/date mismatches between related specs

### 2. Goal vs. implementation drift
- Architecture or tech choices that don't serve the stated goals (overengineered, wrong tradeoff)
- Features that have evolved away from their original stated purpose
- Specs that describe what was built rather than what should be built (post-hoc rationalization)
- UX goals that are contradicted by technical decisions (e.g., goal says 'fast and simple' but spec describes a complex multi-step flow)

### 3. Ambiguity that would block an implementer
- Requirements with no clear success criteria ('should be fast', 'user-friendly', 'robust')
- Undefined terms or acronyms used without explanation
- Vague quantifiers ('some', 'many', 'usually', 'when appropriate')
- Missing decisions marked as TBD/TODO that are blocking for implementation
- Conditional logic without defined behavior for all branches ('if X, do Y' — but what if not X?)

### 4. Missing specs and gaps
- User flows or interactions described in one spec but with no corresponding spec for dependent components
- Error states and failure modes not covered (what happens when the API is down, the user has no data, the payment fails?)
- Missing edge cases: empty states, first-run experience, concurrent users, data migration from old behavior
- Security and auth requirements absent for features that clearly need them
- No spec for how the feature degrades (offline, slow network, partial failures)

### 5. Implementability
- Requirements that are technically infeasible or extremely expensive given the described architecture
- Specs that require information or dependencies not available at the described point in the flow
- Missing interface contracts between components (spec A says 'sends data to B' but B's spec doesn't describe receiving it)
- Performance requirements stated without a credible path to meeting them
- Requirements that assume capabilities not present in the described tech stack

### 6. Staleness and rot
- Specs that reference removed features, deprecated APIs, or old architecture
- Specs contradicted by the current codebase (check the code when in doubt)
- Decision records whose context has materially changed since they were written
- Links to external docs, tools, or services that no longer exist

### 7. Testability
- Requirements that cannot be verified with a test (manual or automated)
- Acceptance criteria missing entirely
- Success metrics that are unmeasurable or subjective without a defined threshold
- No clear definition of done

## Output format

For each finding:
- **Severity**: HIGH / MEDIUM / LOW
  - HIGH = would cause wrong implementation, major rework, or blocks progress
  - MEDIUM = creates confusion or risk, but a good engineer could work around it
  - LOW = should be fixed but won't cause immediate harm
- **Spec file**: which file and section
- **Issue**: one-sentence description
- **Impact**: what goes wrong if this isn't fixed (wasted time, wrong build, user-facing bug)
- **Suggestion**: how to resolve it (be specific — not just 'clarify this')

Group findings by severity (HIGH first).

After all findings, provide:

### Summary
- Total findings by severity
- Top 3 riskiest specs (most findings or most severe)
- Overall verdict: HEALTHY (minor issues only), NEEDS WORK (significant gaps but structure is sound), or RETHINK (fundamental contradictions or missing specs that would cause major rework)"
```

4. **Read the output** and present findings to the user exactly as returned. Do not summarize or reformat.

$ARGUMENTS