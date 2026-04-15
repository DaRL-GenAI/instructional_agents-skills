---
name: latex-to-pptx
description: Convert a Beamer LaTeX (.tex) file into a fully-editable PowerPoint (.pptx) deck. Use this when the user has a .tex slide source and wants an editable .pptx — for example "convert this LaTeX to PPT", "export my beamer slides as PowerPoint", or when they mention editing slides in PowerPoint/Keynote.
---

# LaTeX → PPTX Conversion

Converts a Beamer `.tex` file into a native, editable PowerPoint deck using
the `instructional_agents` parser plus `pptxgenjs`.

## When to invoke this skill

- User has a `.tex` file (Beamer or Beamer-compatible) and wants a `.pptx`
- User asks to "export LaTeX slides to PowerPoint / Keynote"
- User wants to edit generated slides in PowerPoint (vs. getting a static PDF)

Do **not** invoke this for:
- Generating new slides from scratch → use `course-generate`
- Compiling LaTeX to PDF → use `latex-compile`

## Prerequisites

Before running, verify:

1. Python 3.11+ with `instructional-agents` installed:
   ```bash
   pip show instructional-agents || pip install instructional-agents
   ```
2. Node.js with `pptxgenjs`:
   ```bash
   node -e "require('pptxgenjs')" 2>/dev/null || npm install -g pptxgenjs
   ```

If either is missing, tell the user and offer to install.

## Usage

Run the wrapper script with the input `.tex` path. The `.pptx` is written
next to the source unless `--output` is given.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/latex-to-pptx/scripts/convert.py" \
  <input.tex> [--output <output.pptx>]
```

### Arguments

| Arg | Required | Description |
|---|---|---|
| `<input.tex>` | yes | Path to the Beamer `.tex` file |
| `--output <path>` | no | Output `.pptx` path (default: same dir, same stem) |

### Example

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/latex-to-pptx/scripts/convert.py" \
  ~/courses/ml/chapter1.tex
# → ~/courses/ml/chapter1.pptx
```

## Supported LaTeX constructs

`itemize`, `enumerate`, `block`, `alertblock`, code listings (`lstlisting`),
inline & display math, `columns`, `tikz` (rendered as placeholder boxes).

## Output

An editable `.pptx` — every text object, bullet list, and code block is
a native PowerPoint shape, not an embedded image. Safe to edit in PowerPoint,
Keynote, or Google Slides.

## Troubleshooting

- **"pptxgenjs not found"** → `npm install -g pptxgenjs`
- **Math doesn't render** → `pptxgenjs` doesn't support native LaTeX math;
  the skill emits math as plain text. For math-heavy decks, keep the PDF.
- **`\include` / `\input`** → flatten first with `latexpand input.tex > flat.tex`
  then run the skill on `flat.tex`.

## Citation

This skill wraps code from [Instructional Agents (arXiv:2508.19611)](https://arxiv.org/abs/2508.19611).
If used in published work, please cite the paper — see the plugin README.
