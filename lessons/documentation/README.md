# Documentation

> *In the book: Chapter 11 — Documentation.*

:::{admonition} What you'll learn
:class: tip

- Why documentation is a first-class deliverable, not an afterthought.
- The Sphinx + MyST + `sphinx_rtd_theme` toolchain — the same one that
  renders this site.
- How to write a lesson in Markdown and include Jupyter notebooks with
  their outputs.
- How to build the site locally and deploy it to GitHub Pages via
  `.github/workflows/docs.yml`.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*A screenshot will land at `assets/overview.png` showing this site's
landing page. Reference it as `![overview](assets/overview.png){width=520}`
once captured.*
:::

## Why documentation

A tool your collaborator cannot understand is a tool your collaborator
cannot use. Documentation is what turns a script into a *tool.* It is
also what turns a tool into something an AI agent can use ([MCP
server](mcp-server.md)).

The rule from [The Rules](elements-of-style-rules.md):

> **Document data and functions.** Every column has units. Every
> function has a purpose. Every CLI flag has a meaning.

Sphinx is the tool that lets you write that documentation once and
render it many ways — a website, a PDF, an epub.

## The toolchain

This site uses:

- **[Sphinx](https://www.sphinx-doc.org/)** — the documentation
  generator behind the official Python docs and thousands of technical
  sites.
- **[MyST-parser](https://myst-parser.readthedocs.io/)** — lets you
  write in Markdown instead of reStructuredText.
- **[MyST-NB](https://myst-nb.readthedocs.io/)** — same parser, extends
  to Jupyter notebooks so `.ipynb` files render with their outputs.
- **[`sphinx_rtd_theme`](https://sphinx-rtd-theme.readthedocs.io/)** —
  the Read the Docs visual theme.
- **[`sphinx-design`](https://sphinx-design.readthedocs.io/)** — grids,
  cards, tabs, admonitions.
- **[`sphinx-copybutton`](https://sphinx-copybutton.readthedocs.io/)** —
  one-click copy on code blocks.

## Layout of this site

```
docs/
├── Makefile                    # `make html` builds the site
└── source/
    ├── conf.py                 # Sphinx config
    ├── index.md                # landing page
    └── lessons/
        ├── introduction.md     # include-shims → lessons/<topic>/README.md
        ├── containers.md
        └── ...
```

Everything on this site is either a Markdown file in `docs/source/` or
an include-shim in `docs/source/lessons/` that pulls content from the
canonical `lessons/<topic>/README.md`. The include-shim pattern is what
lets each lesson's content live *with the lesson* (in `lessons/<topic>/`)
while the docs tree renders it.

## Build it — three ways

::::{tab-set}

:::{tab-item} macOS
:sync: mac

```bash
conda activate eos-lessons
cd docs && make html
python -m http.server -d build/html 8000
# open http://localhost:8000
```
:::

:::{tab-item} Windows (Git Bash)
:sync: win

```bash
conda activate eos-lessons
cd docs && make html
python -m http.server -d build/html 8000
# open http://localhost:8000
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# On a Lifebit notebook server, the same commands work.
# The workspace's port-forwarding gives you the served URL.
cd docs && make html
python -m http.server -d build/html 8000
```
:::

::::

## Deploy it — GitHub Pages via Actions

Every push to `main` triggers `.github/workflows/docs.yml`, which
installs Sphinx, runs `sphinx-build`, and pushes the HTML to GitHub
Pages. The deploy takes about two minutes. Details in the
[Continuous integration](continuous-integration.md) lesson.

## Writing conventions

- One `README.md` per topic under `lessons/<topic>/`. That is the
  canonical source.
- Use MyST admonitions (`:::{tip}`, `:::{note}`, `:::{warning}`) for
  callouts.
- Use `sphinx-design` tabs when a command differs by platform.
- Reference notebooks by relative path from the README —
  `[notebook](notebooks/python.ipynb)`.
- End every lesson with a **Further reading** section (see below) and
  a **Where to next** link.

## Further reading

- [Sphinx documentation](https://www.sphinx-doc.org/en/master/) — the
  authoritative reference.
- [MyST-parser guide](https://myst-parser.readthedocs.io/en/latest/) —
  Markdown syntax that Sphinx understands.
- [MyST-NB guide](https://myst-nb.readthedocs.io/en/latest/) — Jupyter
  notebook rendering.
- [Read the Docs theme](https://sphinx-rtd-theme.readthedocs.io/) —
  visual theme reference.
- [sphinx-design](https://sphinx-design.readthedocs.io/) — cards,
  grids, tabs.
- [Diátaxis](https://diataxis.fr/) — a framework for organising
  technical documentation (tutorials, how-to, reference, explanation).
- [Write the Docs](https://www.writethedocs.org/) — community and
  guides for documentation as a craft.

## Where to next

→ [Continuous integration](continuous-integration.md) — automate the
build + deploy of this site (and everything else) with GitHub Actions.
