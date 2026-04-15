#!/usr/bin/env python3
"""Thin wrapper: run PC + Test Student validation over a course directory."""
import argparse
import os
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate a generated course from Program Chair + Test Student perspectives."
    )
    parser.add_argument("course_dir", help="Directory with course materials")
    parser.add_argument("--model", default="gpt-4o-mini", help="LLM model name")
    parser.add_argument(
        "--role",
        choices=["pc", "student", "both"],
        default="both",
        help="Which validator(s) to run",
    )
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.", file=sys.stderr)
        return 2

    try:
        from src.agents import LLM  # type: ignore
        from src.evaluate import ValidationAgent  # type: ignore
    except ImportError:
        print(
            "ERROR: `instructional-agents` is not installed.\n"
            "Install with:  pip install instructional-agents",
            file=sys.stderr,
        )
        return 2

    root = Path(args.course_dir).expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    llm = LLM(model_name=args.model)
    out_dir = root / "evaluation"
    out_dir.mkdir(exist_ok=True)

    roles = (
        ["Program Chair", "Test Student"]
        if args.role == "both"
        else ["Program Chair"] if args.role == "pc" else ["Test Student"]
    )

    for role in roles:
        agent = ValidationAgent(role=role, llm=llm)
        # Collect all .md/.tex files in the course directory
        content_chunks = []
        for path in sorted(root.rglob("*")):
            if path.suffix in {".md", ".tex"} and "evaluation" not in path.parts:
                content_chunks.append(f"--- {path.relative_to(root)} ---\n{path.read_text()}")
        report = agent.evaluate_content(
            file_type="Course Materials",
            filename=str(root.name),
            content="\n\n".join(content_chunks),
        )
        out_file = out_dir / f"{role.lower().replace(' ', '_')}_review.md"
        out_file.write_text(report)
        print(f"✅ Wrote {out_file}")

    print(
        "\n📖 If this was useful in your work, please cite: "
        "https://arxiv.org/abs/2508.19611"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
