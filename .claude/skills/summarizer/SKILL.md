---
name: summarizer
description: "Summarize a YouTube video or podcast episode and save the summary as a structured note in NotePlan under '3 Resources/Podcasts, YT/'. Use this skill whenever the user shares a YouTube link and wants it summarized, noted, or saved — or says things like 'summarize this', 'add this to my notes', 'save this podcast', 'summarize this one too', 'note this down'. Also trigger when the user pastes a YouTube URL alongside words like 'save', 'note', 'summarize', 'add to NotePlan', or 'add to Podcasts'. Handles the full pipeline: fetch transcript, summarize, organize into the right NotePlan folder, and create the note."
---

# Summarizer — YouTube / Podcast → NotePlan

Takes a YouTube video URL, fetches the transcript, writes a practical summary, and saves it as a note in NotePlan under the right channel/creator subfolder.

## Workflow

### 1. Get video metadata

Fetch the video title and channel name using the YouTube oEmbed API:

```bash
curl -s "https://www.youtube.com/oembed?url=VIDEO_URL&format=json"
```

This returns JSON with `title` and `author_name`. Extract both — you need them for the note heading and folder name.

If oEmbed fails (private video, age-restricted), fall back to asking the user for the title and channel.

### 2. Fetch the transcript

Use the bundled yt-transcript script:

```bash
python ~/.claude/skills/yt-transcript/scripts/yt_transcript.py "VIDEO_URL"
```

For Estonian videos, add `et` as the second argument.

### 3. Write the summary

Read the full transcript and write a summary following these rules:

**Length:** Up to 350 words. If the video contains specific scripts, frameworks, step-by-step processes, or concrete examples that lose their value when compressed, go longer — practical detail beats arbitrary brevity.

**What to include:**
- **Core insight** — the central thesis or main argument in 1-3 sentences
- **Core content, practical tips and frameworks** — actionable advice, systems, scripts, checklists. This is the most important part. Preserve specificity — if the speaker says "ask this exact question" or "use this technique" include it. Format this as topic (### heading) and bullets.
- **Key mistakes / anti-patterns** — what NOT to do, if covered
- **Key takeaway** — a distilled closing thought

**What to skip:**
- Sponsor segments, self-promotion, channel plugs
- Repetitive examples that make the same point
- Vague motivational filler ("you've got this!", "believe in yourself")
- Biographical context about the speaker unless it's directly relevant to credibility

**Tone:** Match the user's existing notes — structured, scannable, practical. Use headers, bullets, bold for key terms. Write like you're capturing a playbook, not summarizing an article.

**Do NOT invent content.** Everything in the summary must come from the transcript. If something is unclear in the transcript, leave it out rather than guessing.

### 4. Find or create the NotePlan folder

Notes go under `Notes/3 Resources/Podcasts, YT/` in NotePlan.

**Check if a folder already exists** for this channel/creator:

```
mcp__noteplan__noteplan_folders → action: find, query: "<channel_name>"
```

Look for a match under `3 Resources/Podcasts, YT/`. The existing folder name might not match the YouTube channel name exactly (e.g., YouTube says "Lucy" but the folder is "Career Growth w Lucy"). Use judgment — if a folder clearly belongs to the same creator, use it.

**If no folder exists**, ask the user what to name it. Don't silently create a folder — the user may want a custom name (e.g., "Lenny's Podcast" instead of "Lenny Rachitsky"). Suggest the channel name as default.

**Create the folder** if needed:

```
mcp__noteplan__noteplan_folders → action: create, parentPath: "Notes/3 Resources/Podcasts, YT", name: "<folder_name>"
```

### 5. Create the note in NotePlan

**Filename pattern:** `<Short Episode Title> (<Creator>, YouTube).txt`

Keep the filename readable — shorten very long YouTube titles to the essential phrase. The full title goes in the H1 heading inside the note.

**Note format:**

```markdown
# <Full Video Title>

**Source:** <YouTube URL>
**Channel:** <Channel Name>
**Date added:** <YYYY-MM-DD>

---

<Summary content with ## sections, bullets, bold key terms>
```

Use `mcp__noteplan__noteplan_manage_note` with action `create`:

```
action: create
folder: "Notes/3 Resources/Podcasts, YT/<subfolder>"
title: "<Short Episode Title> (<Creator>, YouTube)"
content: "<full note content>"
```

### 6. Confirm to the user

After creating the note, tell the user:
- The note title and folder it was saved to
- A one-line summary of what the video covered

## Handling multiple videos

If the user shares several URLs at once (or says "this one too"), process each video through the full pipeline. You can fetch transcripts in parallel, but create each note individually so the user can see progress.

## Edge cases

- **No transcript available**: Tell the user. Don't try to summarize from the title alone.
- **Non-English video**: Try `et` for Estonian. For other languages, tell the user the supported options.
- **Video already noted**: If a note with a very similar title already exists in the same folder, flag it and ask before creating a duplicate.
- **Very short video (<2 min)**: Still summarize, but the note will naturally be shorter. Don't pad it.
