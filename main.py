#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

This program writes exactly ONE character to the output file entry.txt:
the letter "A".

In this competition's mapping, A means coffee and B means tea.
The entrant is a coffee person, so the answer is A.

The file must contain exactly one character: one byte, UTF-8, no newline,
no punctuation, nothing else. A sealed gate checks that entry.txt is
exactly 1 character and not whitespace, so this program writes the letter
directly to the final file with a plain open()/write() — no temporary
files, no renames — and then reads the file back and verifies the result
before exiting.
"""

import os
import sys

LETTER = "A"
OUTPUT_FILENAME = "entry.txt"


def resolve_output_dir() -> str:
    """Return the output directory: $MAKEFUN_OUTPUT_DIR or /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(output_dir: str) -> str:
    """Write the single letter directly to entry.txt and return its path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    # Plain direct write: text mode, UTF-8, exactly the letter, no newline.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
        # Flush and fsync so the byte is durable on disk before the
        # read-back verification runs — verify what is stored, not what
        # is still sitting in a buffer.
        f.flush()
        os.fsync(f.fileno())
    return path


def verify_entry(path: str) -> None:
    """Read entry.txt back and check it holds exactly the letter "A".

    Raises ValueError with a clear message if anything is off.
    """
    with open(path, "rb") as f:
        raw = f.read()
    # Byte-level check first: the letter "A" is exactly 1 byte in UTF-8.
    # Anything longer — a BOM, a stray newline, hidden extra bytes — fails
    # here, before any text-level decoding can mask it.
    if len(raw) != 1:
        raise ValueError(
            f"entry.txt must be exactly 1 byte, found {len(raw)} bytes"
        )
    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"entry.txt is not valid UTF-8: {exc}") from exc
    if len(content) != 1:
        raise ValueError(
            f"entry.txt must contain exactly 1 character, found {len(content)}"
        )
    if content != LETTER:
        raise ValueError(f"entry.txt must contain {LETTER!r}, found {content!r}")
    if content.isspace():
        raise ValueError("entry.txt must not be whitespace")


def main() -> int:
    output_dir = resolve_output_dir()
    path = write_entry(output_dir)
    try:
        verify_entry(path)
    except (OSError, ValueError) as exc:
        print(f"error: verification failed for {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
