#!/usr/bin/env python3
"""Fetch a YouTube video transcript and print it to stdout."""
import re
import sys
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(value: str) -> str:
    value = value.strip()
    if re.fullmatch(r"[\w-]{11}", value):
        return value
    parsed = urlparse(value)
    if parsed.netloc in {"youtu.be", "www.youtu.be"}:
        vid = parsed.path.lstrip("/").split("/")[0]
        if re.fullmatch(r"[\w-]{11}", vid):
            return vid
    if "youtube.com" in parsed.netloc:
        if parsed.path == "/watch":
            vid = parse_qs(parsed.query).get("v", [None])[0]
            if vid and re.fullmatch(r"[\w-]{11}", vid):
                return vid
        parts = [p for p in parsed.path.split("/") if p]
        for i, p in enumerate(parts):
            if p in {"shorts", "embed", "live"} and i + 1 < len(parts):
                vid = parts[i + 1]
                if re.fullmatch(r"[\w-]{11}", vid):
                    return vid
    raise ValueError("Could not extract a valid YouTube video ID")


def main():
    if len(sys.argv) < 2:
        print("Usage: yt_transcript.py <youtube_url_or_video_id> [lang]", file=sys.stderr)
        sys.exit(1)

    video_id = extract_video_id(sys.argv[1])
    lang = sys.argv[2] if len(sys.argv) > 2 else "en"

    api = YouTubeTranscriptApi()
    transcript_list = api.list(video_id)

    transcript = None
    try:
        transcript = transcript_list.find_manually_created_transcript([lang])
    except Exception:
        try:
            transcript = transcript_list.find_generated_transcript([lang])
        except Exception:
            transcript = transcript_list.find_transcript([lang])

    fetched = transcript.fetch()
    text = " ".join(s.text.strip() for s in fetched if s.text.strip())
    print(text)


if __name__ == "__main__":
    main()
