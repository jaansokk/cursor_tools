---
name: noteplan
description: "Read, search, create, and edit NotePlan notes and daily logs directly via the filesystem. Use this skill whenever the user references NotePlan, daily notes, weekly notes, project notes, or wants to check/update their planning. Triggers: 'noteplan', 'daily note', 'today's note', 'weekly note', 'check my notes', 'add to noteplan', 'what's on my plate', 'update my plan'. Prefer this over the NotePlan MCP for speed and bulk operations."
---

# NotePlan — Filesystem Access

Read, search, create, and edit NotePlan 3 notes directly through the local filesystem. This is faster than the MCP server and supports bulk operations.

## Root path

```
~/Library/Containers/co.noteplan.NotePlan3/Data/Library/Application Support/co.noteplan.NotePlan3/
```

Always reference this as `NP_ROOT` in commands. Use the full expanded path with `$HOME` — do NOT use `~` inside quoted strings in shell commands.

## Directory structure

| Path | Contents | Naming |
|------|----------|--------|
| `Calendar/` | Daily notes | `YYYYMMDD.txt` (e.g. `20260317.txt`) |
| `Calendar/` | Weekly notes | `YYYY-WNN.txt` (e.g. `2025-W47.txt`) |
| `Notes/` | Project & reference notes | Organized in folders |

### Notes folder hierarchy

```
Notes/
├── 1 Projects/      # Active projects with subfolders
├── 2 Areas/          # Ongoing areas of responsibility
├── 3 Resources/      # Reference material
├── 5 Meetings/       # Meeting notes
├── @Archive/         # Archived notes
├── @Templates/       # Note templates
└── @Trash/           # Deleted notes
```

## File format

NotePlan files are plain-text markdown (`.txt` extension) with these conventions:

- **First line**: `# Title` heading (for project notes) or date-based content start (for daily notes)
- **Tasks** (`*`): `* task` (open), `* [x] task` (done), `* [-] task` (cancelled). Tasks are **tracked** — uncompleted tasks become overdue and show up in reviews. Use sparingly, only for items with a real commitment to complete.
- **Checklist items** (`+`): `+ item` (open), `+ [x] item` (done). Checklists are **not tracked** — they won't appear as overdue. Use `+` as the default for notes, ideas, bullets, and anything that doesn't need deadline tracking.
- **Indented sub-items**: tabs for nesting under tasks or checklist items
- **Sections**: `## Heading` or `---` dividers
- **Scheduled items**: `>YYYY-MM-DD` moves/schedules a task to a date
- **Links**: `[[Note Title]]` for internal wiki-links
- **Tags**: `#tag` and `@mention`
- **Time blocks**: `* Task HH:MM-HH:MM` or `* Task HH:MM` for calendar-like entries

## Common operations

### Read today's daily note

```bash
cat "$HOME/Library/Containers/co.noteplan.NotePlan3/Data/Library/Application Support/co.noteplan.NotePlan3/Calendar/$(date +%Y%m%d).txt"
```

### Read a specific date

```bash
cat "$HOME/Library/Containers/co.noteplan.NotePlan3/Data/Library/Application Support/co.noteplan.NotePlan3/Calendar/20260317.txt"
```

### Search across all notes

Use the Grep tool with path set to the NP_ROOT. For example, search for a keyword across all notes and calendar entries.

### List project notes

```bash
/bin/ls -R "$HOME/Library/Containers/co.noteplan.NotePlan3/Data/Library/Application Support/co.noteplan.NotePlan3/Notes/"
```

### Append to today's daily note

```bash
echo "" >> "$HOME/Library/Containers/co.noteplan.NotePlan3/Data/Library/Application Support/co.noteplan.NotePlan3/Calendar/$(date +%Y%m%d).txt"
echo "+ New checklist item" >> "$HOME/Library/Containers/co.noteplan.NotePlan3/Data/Library/Application Support/co.noteplan.NotePlan3/Calendar/$(date +%Y%m%d).txt"
```

### Create a new project note

Write a new `.txt` file in the appropriate `Notes/` subfolder. NotePlan picks it up automatically.

## Guidelines

- **Default to `+` (checklist), not `*` (task)** — only use `*` when the user explicitly wants a tracked task. Unfinished `*` items become overdue, cluttering reviews. For general notes, ideas, and non-committal items, always use `+`.
- **Read before writing** — always read the current file content before editing to avoid overwriting.
- **Append, don't overwrite** — for daily notes, append new content rather than replacing the file. Use the Edit tool for surgical changes.
- **Preserve formatting** — match existing indentation (tabs), task markers, and section structure.
- **NotePlan syncs via CloudKit** — changes to files on disk are picked up immediately by the app. Avoid writing while NotePlan is mid-sync (rare edge case).
- **File extension is `.txt`** — even though content is markdown, NotePlan uses `.txt`.
- **Filenames with special characters** — some note titles contain Estonian characters (ä, ö, ü, õ) or special chars. Always quote paths.
- **No MCP needed** — this skill operates entirely via filesystem. Use it instead of the NotePlan MCP tools for speed and when doing bulk reads/searches.
- **Do not delete notes** - .txt files should not be deleted.

## When to use this skill

- User asks what's on their plate today → read today's daily note
- User wants to add a task or log something → append to daily note or relevant project note
- User asks to search their notes for something → grep across NP_ROOT
- User references a project by name → find and read the matching note in `Notes/`
- User wants to review or plan their week → read the weekly note and recent daily notes
- User asks to create a new note → write a new `.txt` file in the appropriate folder

$ARGUMENTS
