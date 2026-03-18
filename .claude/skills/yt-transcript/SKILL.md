---
name: yt-transcript
description: "Fetch YouTube video transcripts and load them into context for further processing. Use this skill whenever the user shares a YouTube URL or video ID and wants to work with the video's content — summarizing, extracting insights, answering questions about it, translating, or feeding it into another workflow. Also trigger when the user says things like 'watch this', 'what does this video say', 'get the transcript', or pastes any youtube.com or youtu.be link. Supports English and Estonian transcripts."
---

# YouTube Transcript Fetcher

Fetches the transcript of a YouTube video and loads the full text into your context so you can work with it immediately.

## How it works

There's a Python script bundled with this skill that uses `youtube-transcript-api` to pull subtitles directly from YouTube — no browser or API key needed. It prints plain text to stdout. You capture that output and you're ready to go.

## Prerequisites

The `youtube-transcript-api` package must be installed:

```bash
pip install youtube-transcript-api
```

Check first with `pip show youtube-transcript-api` to avoid reinstalling.

## Usage

```bash
python /path/to/yt-transcript/scripts/yt_transcript.py "<youtube_url_or_video_id>" [lang]
```

- First argument: any YouTube URL format (watch, shorts, embed, youtu.be) or a raw 11-character video ID
- Second argument (optional): language code. Defaults to `en`. Use `et` for Estonian.

The script prints the full transcript as plain text to stdout. Capture it and work with it directly — no files are created.

## Workflow

1. User shares a YouTube link (or video ID)
2. Ensure `youtube-transcript-api` is installed
3. Run the script, capturing stdout
4. The transcript is now in your context — proceed with whatever the user needs (summarize, answer questions, extract key points, feed into another skill, etc.)

## Language handling

- Default: English (`en`)
- If the user asks for Estonian or the video is in Estonian, use `et`
- The script prefers manual subtitles over auto-generated ones when available

## Error handling

If the script fails (e.g., no transcript available, video is private, invalid URL), relay the error to the user clearly. Common issues:
- "Could not extract a valid YouTube video ID" — the URL format wasn't recognized
- Transcript not available — the video may not have subtitles, or they may be disabled
- Network errors — check connectivity

## Important notes

- This skill is designed for Claude Code where the script runs on the user's machine with direct network access. It will not work in sandboxed environments that block youtube.com.
- The transcript text can be long for lengthy videos. That's fine — just work with it in context.
- Don't save transcript files unless the user explicitly asks for it.
