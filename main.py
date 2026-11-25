#!/usr/bin/env python3
"""Write the 25 November 2026 front page to /output/entry.png.

The image itself is drawn once and shipped in this repository as
entry.png; this program only copies it to the output directory, so
every run writes exactly the same bytes.
"""

import argparse
import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Copy the 25 November 2026 front page to /output/entry.png."
    )
    parser.add_argument(
        "--out",
        default=OUTPUT,
        help="destination path for entry.png (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    with open(SOURCE, "rb") as source_file:
        data = source_file.read()

    destination_dir = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(destination_dir, exist_ok=True)
    with open(args.out, "wb") as output_file:
        output_file.write(data)

    digest = hashlib.sha256(data).hexdigest()

    # Verify the copy before reporting success: re-read what was
    # written and refuse to claim a good run on a corrupt copy.
    with open(args.out, "rb") as check_file:
        written = check_file.read()
    if hashlib.sha256(written).hexdigest() != digest:
        print(f"error: {args.out} failed verification after writing", file=sys.stderr)
        return 1

    print(f"wrote {args.out}: {len(data)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
