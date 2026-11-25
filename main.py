#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes the locked status update (75 chars) to /output/entry.txt.
"""

import os

LINE = "His dot went grey at 23:41. Mine is still green, and no one is watching it."

MAX_CHARS = 200


def main() -> None:
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
