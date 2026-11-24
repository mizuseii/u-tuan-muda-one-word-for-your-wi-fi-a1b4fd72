#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: "Schrödinger" — the Wi-Fi
that is simultaneously connected and not connected (full bars, no
internet). Deterministic: no network, no randomness, no time dependence.
"""

import os
import tempfile

ENTRY = "Schrödinger"


def main() -> None:
    assert 1 <= len(ENTRY) <= 20, f"entry is {len(ENTRY)} chars"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    assert not any(ch.isspace() for ch in ENTRY), "entry must be one word"
    assert "\n" not in ENTRY, "entry must have no newline"
    assert ENTRY == ENTRY.strip(), "entry must have no surrounding whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write via a unique temp file in the same directory: avoids
    # temp-name collisions between concurrent runs, and os.replace means
    # a crash can never leave a partial entry.txt behind.
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", dir=out_dir,
        prefix="entry.", suffix=".tmp", delete=False,
    ) as f:
        f.write(ENTRY)
        tmp_path = f.name
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
