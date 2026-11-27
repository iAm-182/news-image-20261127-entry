#!/usr/bin/env python3
"""Entry program for the news-image-20261127 competition.

Writes the finished front-page image for Friday 27 November 2026 to the
grading output directory. The image was drawn during the build session and
is shipped in this repository as entry.png; this program only copies it,
so the two grading runs always write identical bytes.

Python standard library only: no network, no extra packages, no fonts.
The output directory is MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os
import shutil
import sys


def source_path():
    """Path of the shipped image next to this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def target_dir():
    """Directory the grader reads the image from."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Copy entry.png into the grading output directory."""
    src = source_path()
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    with open(src, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    dst_dir = target_dir()
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
