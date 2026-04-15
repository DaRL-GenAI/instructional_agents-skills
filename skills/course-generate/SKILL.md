---
name: course-generate
description: Generate a complete course — learning objectives, syllabus, slides (LaTeX), scripts, and assessments — using the ADDIE multi-agent pipeline. Use when the user asks to "create a course on X", "generate teaching materials for X", "build an undergraduate/graduate course on X", or similar end-to-end course-authoring requests.
---

# Course Generate (Full ADDIE Pipeline)

Runs the complete multi-agent course generation pipeline:

- **Phase 1** — Foundation deliberations (learning objectives, resource
  assessment, target audience, syllabus, assessment planning, final project)
- **Phase 2** — Per-chapter development (slides, scripts, assessments via
  SlidesDeliberation)
- **Phase 3** — Evaluation (Program Chair + Test Student review)

This is a **long-running** task — typically 20–60 minutes depending on model
and number of chapters. Confirm scope with the user before launching.

## When to invoke this skill

- User asks to generate a course / teaching materials / curriculum
- User provides a topic/subject and wants end-to-end output
- User wants to reproduce the paper's pipeline on new content

Do **not** invoke for:
- Just converting existing LaTeX → PPTX → use `latex-to-pptx`
- Only evaluating existing slides → use `slide-evaluate`
- Optimizing an existing slide chapter → (future: `slide-optimize` skill)

## Prerequisites

- `pip install instructional-agents`
- `OPENAI_API_KEY` set in the environment
- Disk space ~10–50 MB per course

## Usage

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/course-generate/scripts/generate.py" \
  --course "<course name>" \
  [--model <model_name>] \
  [--exp-name <tag>] \
  [--catalog <catalog_name>] \
  [--copilot <copilot_name>]
```

### Arguments

| Arg | Required | Description |
|---|---|---|
| `--course` | yes | Course name/topic, e.g. `"Reinforcement Learning"` |
| `--model` | no | LLM model (default: `gpt-4o-mini`) |
| `--exp-name` | no | Subdirectory under `exp/` (default: `test`) |
| `--catalog` | no | Pre-loaded reference catalog name |
| `--copilot` | no | Copilot mode with interactive feedback |

### Example

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/course-generate/scripts/generate.py" \
  --course "Introduction to Reinforcement Learning" \
  --model gpt-4o \
  --exp-name rl_undergrad_2026
```

## Output structure

```
exp/<exp-name>/
├── learning_objectives.md
├── resource_assessment.md
├── target_audience.md
├── syllabus.md
├── assessment_planning.md
├── final_project.md
├── chapter_1/
│   ├── slides.tex
│   ├── slides.pdf          (if compiled)
│   ├── script.md
│   └── assessment.md
├── chapter_2/...
└── evaluation/
    ├── program_chair_review.md
    └── test_student_review.md
```

## Follow-up skills

After generation you typically want to run:

- `latex-compile` → produce PDFs
- `latex-to-pptx` → produce editable PowerPoint (per chapter)
- `slide-evaluate` → re-evaluate with different rubrics

## Citation

This is the full pipeline from [Instructional Agents (arXiv:2508.19611)](https://arxiv.org/abs/2508.19611).
Please cite if used in published work.
