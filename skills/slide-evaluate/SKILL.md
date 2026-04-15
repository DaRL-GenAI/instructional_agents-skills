---
name: slide-evaluate
description: Evaluate generated course slides from two perspectives — Program Chair (academic rigor) and Test Student (clarity, engagement). Use when the user wants feedback on existing slide materials, asks "review these slides", "evaluate this course", or after running `course-generate` and wanting quality feedback.
---

# Slide Evaluate

Runs two validation agents over generated course materials and writes
markdown evaluation reports.

- **Program Chair** — academic rigor, assessment validity, alignment with
  program standards, coherence.
- **Test Student** — clarity, engagement, learning support, accessibility.

## When to invoke this skill

- User has a directory of generated slides (from `course-generate` or manual)
  and wants quality feedback
- User asks "how good is this course?" / "review these slides"
- Used as the Phase 3 evaluation in the ADDIE pipeline

## Prerequisites

- `pip install instructional-agents`
- `OPENAI_API_KEY` set in the environment

## Usage

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/slide-evaluate/scripts/evaluate.py" \
  <course_dir> [--model gpt-4o-mini] [--role both|pc|student]
```

### Arguments

| Arg | Required | Description |
|---|---|---|
| `<course_dir>` | yes | Directory with LO / syllabus / slides / scripts / assessment |
| `--model` | no | LLM model name (default: `gpt-4o-mini`) |
| `--role` | no | `pc`, `student`, or `both` (default: `both`) |

### Expected course_dir layout

```
course_dir/
├── learning_objectives.md
├── syllabus.md
├── assessment.md
├── chapter_1/
│   ├── slides.tex
│   ├── script.md
│   └── assessment.md
└── ...
```

## Output

```
course_dir/evaluation/
├── program_chair_review.md
└── test_student_review.md
```

## Citation

Built on the `ValidationAgent` from [Instructional Agents (arXiv:2508.19611)](https://arxiv.org/abs/2508.19611).
