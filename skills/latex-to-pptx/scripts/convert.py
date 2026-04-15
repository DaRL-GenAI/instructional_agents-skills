#!/usr/bin/env python3
"""
Thin wrapper: Beamer .tex → editable .pptx.

Delegates to `src.latex_to_pptx` in the `instructional-agents` PyPI package.
"""
import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert a Beamer .tex file into an editable .pptx deck."
    )
    parser.add_argument("input", help="Path to the .tex file")
    parser.add_argument(
        "--output",
        help="Output .pptx path (default: same dir, same stem as input)",
        default=None,
    )
    args = parser.parse_args()

    try:
        from src.latex_to_pptx import LaTeXToPPTXConverter  # type: ignore
    except ImportError:
        print(
            "ERROR: `instructional-agents` is not installed.\n"
            "Install with:  pip install instructional-agents",
            file=sys.stderr,
        )
        return 2

    in_path = Path(args.input).expanduser().resolve()
    if not in_path.is_file():
        print(f"ERROR: input file not found: {in_path}", file=sys.stderr)
        return 2

    out_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else in_path.with_suffix(".pptx")
    )

    try:
        converter = LaTeXToPPTXConverter()
        converter.convert(str(in_path), str(out_path))
    except Exception as exc:
        print(f"ERROR: conversion failed: {exc}", file=sys.stderr)
        return 1

    print(f"✅ Wrote {out_path}")
    print(
        "\n📖 If this was useful in your work, please cite: "
        "https://arxiv.org/abs/2508.19611"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
