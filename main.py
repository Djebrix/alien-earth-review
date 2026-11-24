#!/usr/bin/env python3
"""Writes one original line: an alien tourist's review of planet Earth.

Stdlib only, no network, deterministic: the same line every run.
"""

import os
import sys

LINE = (
    "Visited Earth. The locals pay rent for ground they didn't build, "
    "then thank the landlord. 2/5 \u2014 the sunsets are doing all the "
    "heavy lifting."
)


def main() -> int:
    assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"
    assert LINE.strip(), "line is only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
