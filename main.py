"""Copy entry.png to the output directory.

Standard library only. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable when it is set, and falls
back to /output otherwise. The copied file is always named entry.png.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    if not destination.is_file():
        raise SystemExit("entry.png was not copied: destination is missing")
    if destination.stat().st_size != source.stat().st_size:
        raise SystemExit("entry.png was not copied: size mismatch")


if __name__ == "__main__":
    main()
