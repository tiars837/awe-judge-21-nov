#!/usr/bin/env python3
"""Write one short calming text to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness.
The text itself is the entry: plain concrete words, a slow rhythm,
and an image that keeps growing after it is read.
"""

import os

TEXT = (
    "Above the rooftops, the stars keep their slow, unhurried turning, "
    "and the sea below repeats its one long sentence against the shore \u2014 "
    "night after night, patient as breathing, asking nothing of us at all."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
