#!/usr/bin/env python3
"""Writes one original line: an alien tourist's review of planet Earth.

Stdlib only, no network, deterministic: the same 140-character line every
run, written as UTF-8 with a single LF line ending.
"""

import os
import sys

def line() -> str:
    """Return the entry line: an alien tourist's review of Earth."""
    return (
        "Visited Earth. The locals pay rent for ground they didn't build, "
        "then thank the landlord. 2/5 \u2014 the sunsets are doing all the "
        "heavy lifting."
    )


def validate_line(text: str) -> None:
    """Check the entry line against the competition's 1-200 char gate."""
    assert 1 <= len(text) <= 200, f"line length {len(text)} out of range"
    assert text.strip(), "line is only whitespace"


def output_path(out_dir: str) -> str:
    """Build the output file path from the output directory."""
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    text = line()
    validate_line(text)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = output_path(out_dir)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
