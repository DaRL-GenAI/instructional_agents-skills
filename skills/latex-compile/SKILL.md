---
name: latex-compile
description: Batch-compile every .tex file in a directory tree into .pdf, with caching. Use when the user wants to compile LaTeX files — for example "compile all slides in exp/ml/", "build the PDFs for this chapter", or after editing multiple .tex files.
---

# LaTeX Batch Compile

Recursively finds `.tex` files under a directory and compiles each to `.pdf`
using `pdflatex` (or `xelatex`), with a per-file cache directory so that
auxiliary files don't pollute the source tree.

## When to invoke this skill

- User asks to "compile all `.tex` in folder X"
- User has modified LaTeX files and wants fresh PDFs
- Post-processing after `course-generate` (it emits `.tex`, not `.pdf`)

## Prerequisites

A LaTeX distribution on PATH. Check:

```bash
which pdflatex || which xelatex
```

If missing, point the user to [TeX Live](https://tug.org/texlive/) or MacTeX.

## Usage

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/latex-compile/scripts/compile.py" \
  <directory> [--also-pptx]
```

### Arguments

| Arg | Required | Description |
|---|---|---|
| `<directory>` | yes | Root directory to scan recursively |
| `--also-pptx` | no | Also convert each `.tex` to `.pptx` after PDF compilation |

### Engine

The underlying compiler uses `pdflatex` (hardcoded in `src.compile.LaTeXCompiler`).
For xelatex / lualatex support, open an issue upstream.

### Example

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/latex-compile/scripts/compile.py" \
  exp/reinforcement_learning --also-pptx
```

## Output

- `*.pdf` next to each `*.tex`
- Aux files (`.aux`, `.log`, `.toc`, …) stored in `<dir>/.cache/<stem>/`

## Citation

This skill wraps `src.compile` from [Instructional Agents (arXiv:2508.19611)](https://arxiv.org/abs/2508.19611).
