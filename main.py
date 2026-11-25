#!/usr/bin/env python3
"""Write one one-line office joke to the competition output file.

Standard library only. The joke is a single sentence about one concrete
office scene: a printer jam that turns a resignation letter against the
person trying to quit. The harm lands in the last clause: HR files the
letter before it is signed, so the resignation counts and the employee
is still trapped in the job.
"""

import os

JOKE = (
    "The office printer jammed on my resignation letter, "
    "so IT fixed it, printed three copies, "
    "and HR filed one before I could sign it."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def build_entry() -> str:
    line = " ".join(JOKE.split())
    if not 1 <= len(line.encode("utf-8")) <= 199:
        raise ValueError("entry must be 1-199 bytes, got %d" % len(line.encode("utf-8")))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    entry = build_entry()
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")


if __name__ == "__main__":
    main()
