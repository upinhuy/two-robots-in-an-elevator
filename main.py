"""Two Robots in an Elevator — make.fun bounty entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

The line: a robot that has simulated the ride 4,000 times still has no
idea what to do with its arms — and then, mid-ride, asks the other robot
whether it even has arms. Machine logic (exhaustive simulation) collides
with social awkwardness (arms, eye contact, the unspoken thing), and the
last question lands the surprise on the first read.
"""

import argparse
import os
from pathlib import Path

ENTRY = (
    "I simulated this elevator ride 4,000 times. "
    "I still have no idea what to do with my arms. "
    "Do you have arms?"
)

OUTPUT_PATH = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def validate_entry(text: str) -> str:
    """Collapse whitespace to a single line and enforce the entry rules.

    Returns the cleaned text. Raises AssertionError if the entry is blank,
    multi-line, or outside the 1-200 character gate.
    """
    cleaned = " ".join(text.split())
    assert cleaned, "entry must not be blank"
    assert "\n" not in cleaned and "\r" not in cleaned, "entry must be a single line"
    assert cleaned.strip() == cleaned, "entry must not have leading/trailing whitespace"
    assert 1 <= len(cleaned) <= 200, f"entry must be 1-200 chars, got {len(cleaned)}"
    return cleaned


def main() -> None:
    parser = argparse.ArgumentParser(description="Write or validate the entry line.")
    parser.add_argument("--check", action="store_true",
                        help="validate the entry and print its char count, without writing any file")
    args = parser.parse_args()

    text = validate_entry(ENTRY)
    if args.check:
        print(f"entry OK: {len(text)} chars")
        return
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
