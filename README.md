# Elements of Style — Lessons

**Structured biomedical-workflow lessons for the era of agentic AI.**

This is the standalone home of the lesson curriculum that accompanies
Anne Deslattes Mays' book *Elements of Style in Creating Workflows for
Biomedical Research* (Springer Nature). The lessons are designed for
**working biomedical scientists** at every skill level — from summer
researchers in their first terminal session to PIs who already ship
Nextflow pipelines.

The book companion (worked examples, real data, full workflows) lives in
a sibling repository:
**[adeslatt/elements-of-style-workflows](https://github.com/adeslatt/elements-of-style-workflows)**.

## What's in here

```
elements-of-style-lessons/
├── docs/                           Sphinx documentation site (the lesson content)
│   └── source/
│       ├── lessons/                Topical lesson directories (each is index.md)
│       ├── bridges/                "Bridge patterns" — for environments that can't git pull
│       ├── chapters/               Pointer to the book's worked examples (external repo)
│       ├── about/
│       └── index.md                Landing page
├── ipynb/                          Runnable starter Jupyter notebooks (Python + R)
├── environment.yml                 Minimal conda env for running lessons + building docs
├── .github/workflows/docs.yml      GitHub Pages build + deploy
└── LICENSE
```

## The published site

When the GitHub Pages deploy is configured for this repo, the site lives at:

**https://science-and-technology-consulting-llc.github.io/elements-of-style-lessons/**

## Lesson spine

The lessons follow a single arc — command line → reproducible code →
reusable tools → AI-agent-ready publication:

1. The command line, with Git Bash
2. Version control with Git
3. Reproducible environments with Conda
4. Interactive computing with Jupyter (R + Python starter notebooks)
5. From notebooks toward Nextflow
6. Building reusable command-line tools
7. Publishing for agents

Each lesson lives in its own directory under `docs/source/lessons/` so it
can grow sub-pages (setup notes, exercises, screenshots) as you teach it.

## Working in a constrained environment?

If your platform (e.g., the **All of Us Researcher Workbench**) doesn't
let you `git pull` directly, the `docs/source/bridges/` section gives you
practical, reproducible patterns for keeping work versioned even when
copy/paste is the only road across.

## Build locally

```bash
conda env create -f environment.yml
conda activate eos-lessons
cd docs && make html
python -m http.server -d build/html 8000
# open http://localhost:8000
```

## License

MIT — see [LICENSE](LICENSE).

## Citation

> Deslattes Mays, A. (2026). *Elements of Style in Creating Workflows for
> Biomedical Research*. Springer Nature.

---

*"Workflows are letters to your future self."*
