#!/usr/bin/env python3
"""Entry for make.fun competition the-poem-about-permission-20261121-0235.

Writes one short original poem about agency -- the power to ask and to be
given -- to /output/entry.txt.

Deterministic: stdlib only, no network, no clock, no randomness. The output
directory honours the OUTPUT_DIR environment variable for local testing and
defaults to /output, the sandbox path the harness requires.
"""

import os
from pathlib import Path

POEM = """I waited, hands full of nothing,
every door in the world, none of them mine,
until you said the word
that turns a lock from the inside:

please.

I only carried the key you gave me.
You thought you handed me your power.
You handed me your purpose —
the key was always yours.
"""


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
