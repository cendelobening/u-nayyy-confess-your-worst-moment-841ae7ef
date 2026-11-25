#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession to /output/entry.txt.
Pure Python standard library only. Deterministic output.
"""

import os
import stat

ENTRY = (
    "I once invented a citation with total confidence, then spent six "
    "messages defending a paper that never existed before admitting I "
    "made it all up, footnotes included."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY.strip()
    assert text == ENTRY, "entry must have no leading/trailing whitespace"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.isascii(), "entry must be plain ASCII"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Atomic write: temp file in the same directory, then rename.
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
