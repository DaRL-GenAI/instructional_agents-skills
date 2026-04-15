#!/usr/bin/env python3
"""Thin wrapper: recursively compile .tex → .pdf via `src.compile.LaTeXCompiler`."""
import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Recursively compile .tex files to .pdf with cache management."
    )
    parser.add_argument("directory", help="Directory to scan recursively")
    parser.add_argument(
        "--also-pptx",
        action="store_true",
        help="Also convert each .tex to .pptx after PDF compilation",
    )
    args = parser.parse_args()

    try:
        from src.compile import LaTeXCompiler  # type: ignore
    except ImportError:
        print(
            "ERROR: `instructional-agents` is not installed.\n"
            "Install with:  pip install instructional-agents",
            file=sys.stderr,
        )
        return 2

    root = Path(args.directory).expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    compiler = LaTeXCompiler(str(root))

    # Check environment before attempting to compile
    if not compiler.validate_latex_environment():
        print(
            "ERROR: pdflatex not available on PATH.\n"
            "Install a LaTeX distribution (TeX Live / MacTeX) and retry.",
            file=sys.stderr,
        )
        return 2

    compiler.compile_all()

    if args.also_pptx:
        print("\nConverting to PPTX...")
        compiler.generate_pptx()

    print(
        "\n📖 If this was useful in your work, please cite: "
        "https://arxiv.org/abs/2508.19611"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
