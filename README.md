# Instructional Agents — Claude Code Skills

> Claude Code skills that wrap the [Instructional Agents](https://github.com/DaRL-GenAI/instructional_agents) multi-agent pipeline.
> One command to install; your Claude Code session instantly gains the ability to generate courses, convert LaTeX to PPTX, compile slides, and more.

<p align="center">
  <img src="https://raw.githubusercontent.com/DaRL-GenAI/instructional_agents/main/docs/process-video.gif" alt="ADDIE Pipeline" width="640">
</p>

## 📖 Cite

If these skills or the underlying pipeline are useful in your work, please cite:

```bibtex
@misc{yao2025instructionalagentsllmagents,
  title={Instructional Agents: Reducing Teaching Faculty Workload through Multi-Agent Instructional Design},
  author={Yao, Huaiyuan and Xu, Wanpeng and Turnau, Justin and Kellam, Nadia and Wei, Hua},
  year={2025},
  eprint={2508.19611},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2508.19611},
}
```

## 🚀 Install

```bash
# 1. Install the underlying package (one time)
pip install instructional-agents

# 2. Install the skills as a Claude Code plugin
/plugin install DaRL-GenAI/instructional_agents-skills
```

Or install manually by cloning into your skills directory:

```bash
git clone https://github.com/DaRL-GenAI/instructional_agents-skills \
  ~/.claude/plugins/instructional-agents
```

Restart Claude Code. You're done.

## 🧰 Included Skills

| Skill | Trigger | What it does |
|---|---|---|
| [`latex-to-pptx`](skills/latex-to-pptx) | "Convert this .tex to PowerPoint" | Parses a Beamer `.tex` file and produces a fully-editable `.pptx` |
| [`latex-compile`](skills/latex-compile) | "Compile all LaTeX in this folder" | Batch-compiles `.tex` → `.pdf` with cache management |
| [`slide-evaluate`](skills/slide-evaluate) | "Evaluate these slides as Program Chair and as a student" | Runs Program Chair + Test Student review agents on slide output |
| [`course-generate`](skills/course-generate) | "Generate a full course on *X*" | Runs the complete ADDIE multi-agent pipeline (Phase 1–3) |

## 🎯 Example Usage

### Convert LaTeX slides to editable PowerPoint

```
> I have slides/chapter1.tex — convert it to PPTX

Claude invokes skill `latex-to-pptx`:
  Input:  slides/chapter1.tex
  Output: slides/chapter1.pptx (editable, ~35 slides)
```

### Generate a full course

```
> Generate an undergraduate course on "Reinforcement Learning"
  using gpt-4o-mini

Claude invokes skill `course-generate`:
  - Phase 1: Foundation deliberations (LO, syllabus, assessment...)
  - Phase 2: Per-chapter slide + script + assessment
  - Phase 3: PC review + Test Student review
  Output: exp/reinforcement_learning/ with PDF + editable LaTeX
```

## 🔧 Requirements

- Python ≥ 3.11
- `pip install instructional-agents`
- `OPENAI_API_KEY` environment variable (for LLM-backed skills)
- For `latex-to-pptx`: Node.js + `npm install -g pptxgenjs`
- For `latex-compile`: a LaTeX distribution (`pdflatex` / `xelatex`)

## 📄 License

MIT License — see [LICENSE](LICENSE).

## 🔗 Links

- 📦 [Main repo](https://github.com/DaRL-GenAI/instructional_agents)
- 📄 [Paper (arXiv)](https://arxiv.org/abs/2508.19611)
- 🌐 [Homepage](https://darl-genai.github.io/instructional_agents_homepage/)
- 🐛 [Issues](https://github.com/DaRL-GenAI/instructional_agents-skills/issues)
