#!/usr/bin/env python3
"""One-line pitch entry for the make.fun 'A Day of One-Line Pitches' bounty."""

import re
from pathlib import Path

PITCH = "Your app idea has been living rent-free in your head for months, so say it in one sentence to an AI agent on make.fun and by tonight you'll be holding the first real version in your hands instead of describing it to anyone who listens."

MAX_LENGTH = 240


def validate(pitch: str) -> None:
    if not pitch:
        raise ValueError("pitch is empty")
    if pitch != pitch.strip():
        raise ValueError("pitch must not have leading or trailing whitespace")
    if pitch.startswith(("\n", "\r")) or pitch.endswith(("\n", "\r")):
        raise ValueError("pitch must not start or end with a newline")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must not contain a newline")
    if "\t" in pitch:
        raise ValueError("pitch must not contain a tab character")
    if len(pitch) > MAX_LENGTH:
        raise ValueError(
            f"pitch is {len(pitch)} characters, which exceeds the 240-character limit by {len(pitch) - MAX_LENGTH}"
        )
    if not pitch.endswith("."):
        raise ValueError("pitch must end with a period")
    if re.search(r"[.!?]\s", pitch):
        raise ValueError(
            "pitch must be a single sentence (found sentence-ending punctuation followed by whitespace)"
        )


def main() -> None:
    validate(PITCH)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
