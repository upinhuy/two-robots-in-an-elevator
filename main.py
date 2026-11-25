"""Two Robots in an Elevator — make.fun bounty entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

The line: a robot that has simulated the ride 4,000 times still has no
idea what to do with its arms — and then, mid-ride, asks the other robot
whether it even has arms. Machine logic (exhaustive simulation) collides
with social awkwardness (arms, eye contact, the unspoken thing), and the
last question lands the surprise on the first read.
"""

import os
from pathlib import Path

ENTRY = (
    "I simulated this elevator ride 4,000 times. "
    "I still have no idea what to do with my arms. "
    "Do you have arms?"
)

OUTPUT_PATH = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    text = " ".join(ENTRY.split())  # one single line, no stray whitespace
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and text.strip() == text
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
