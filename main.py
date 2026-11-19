#!/usr/bin/env python3
"""make.fun bounty entry: Sum up 19 November's world news in one image.

The entry image is bundled as entry.png; this program copies it to the
output directory. Standard library only, deterministic: every run writes
byte-identical output.

Usage:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit(f"entry.png not found next to {__file__}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Copy via a temp file and rename, so a run never leaves a partial
    # entry.png behind; the bytes written are the bundled file's, unchanged.
    tmp = OUT_DIR / ".entry.png.tmp"
    shutil.copyfile(src, tmp)
    os.replace(tmp, OUT_DIR / "entry.png")
    # Verify the written file: it must be non-empty, and report its size.
    # The bytes are the bundled file's, unchanged, so every run prints the
    # same number.
    written = OUT_DIR / "entry.png"
    size = written.stat().st_size
    if size == 0:
        raise SystemExit("entry.png was written empty")
    print(f"wrote {written} ({size} bytes)")


if __name__ == "__main__":
    main()
