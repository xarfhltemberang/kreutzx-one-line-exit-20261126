#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes the entry to /output/entry.txt with no trailing newline,
exactly as the kit requires (UTF-8, 1-140 characters, one line).

The joke: the resignation letter itself is the evidence — the office
printer jams on the very letter quitting it, so the workplace cannot
even process someone leaving.
"""

import os

ENTRY = (
    "I hereby resign \u2014 the office printer has jammed on this letter "
    "four times, and I refuse to work somewhere that won't even let me leave."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
