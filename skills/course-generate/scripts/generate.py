#!/usr/bin/env python3
"""Thin wrapper: run the full ADDIE multi-agent course generation pipeline."""
import argparse
import os
import sys


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a complete course via the ADDIE multi-agent pipeline."
    )
    parser.add_argument("--course", required=True, help="Course name / topic")
    parser.add_argument("--model", default="gpt-4o-mini", help="LLM model name")
    parser.add_argument("--exp-name", default="test", help="Experiment tag (output subdir)")
    parser.add_argument("--catalog", default=None, help="Reference catalog name")
    parser.add_argument("--copilot", default=None, help="Copilot source name")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    parser.add_argument("--temperature", type=float, default=None, help="LLM temperature")
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.", file=sys.stderr)
        return 2

    try:
        from run import run_instructional_design  # type: ignore
    except ImportError:
        print(
            "ERROR: `instructional-agents` is not installed.\n"
            "Install with:  pip install instructional-agents",
            file=sys.stderr,
        )
        return 2

    print(f"🚀 Starting course generation: {args.course}")
    print(f"   Model: {args.model}")
    print(f"   Output: exp/{args.exp_name}/")
    print("   This may take 20–60 minutes. Progress will stream below.\n")

    try:
        run_instructional_design(
            course_name=args.course,
            copilot=args.copilot,
            catalog=args.catalog,
            model_name=args.model,
            exp_name=args.exp_name,
            seed=args.seed,
            temperature=args.temperature,
        )
    except Exception as exc:
        print(f"\nERROR: generation failed: {exc}", file=sys.stderr)
        return 1

    print(f"\n✅ Course written to exp/{args.exp_name}/")
    print(
        "\n📖 If this was useful in your work, please cite: "
        "https://arxiv.org/abs/2508.19611"
    )
    print("\nFollow-up skills you can invoke next:")
    print("  • latex-compile   — build PDFs from the .tex files")
    print("  • latex-to-pptx   — export editable PowerPoint per chapter")
    print("  • slide-evaluate  — run extra review passes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
