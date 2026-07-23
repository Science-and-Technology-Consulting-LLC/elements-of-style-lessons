# Building a Sphinx site — the local build/deploy loop

*Companion walkthrough to the [documentation](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`building-a-sphinx-site.ipynb`](building-a-sphinx-site.ipynb) — every code cell
  is a shell command executed by the Jupyter **Bash** kernel.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### One time — register the Bash kernel

Only needed if you'll run the paired notebook in JupyterLab. Skip if
you're doing everything in a terminal.

```bash
pip install bash_kernel
python -m bash_kernel.install
```

Restart JupyterLab; the launcher now shows a **Bash** tile.

### Every time — verify the tools this walkthrough uses

The commands below call one or more of these tools. Where a check
fails, the linked lesson has the install instructions.

| Tool | Check | If missing, see |
|---|---|---|
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/README.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/README.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/README.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/README.md) |

Run them all at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s
" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING
" "$cmd"
  fi
done
```


## What we build

A minimal Sphinx-with-MyST site you can render locally, then deploy to
GitHub Pages via GitHub Actions — the same toolchain that renders *this*
site.

## Install the toolchain

```bash
conda activate eos-lessons   # or a fresh env
pip install sphinx sphinx-rtd-theme myst-parser myst-nb \
            sphinx-copybutton sphinx-design linkify-it-py
```

## Scaffold a docs tree

```bash
mkdir -p docs/source && cd docs
```

Create `docs/source/conf.py`:

```python
project = "My Lessons"
author = "Your Name"

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence", "deflist", "linkify"]

html_theme = "sphinx_rtd_theme"
```

Create `docs/source/index.md`:

```markdown
# My Lessons

Welcome.

```{toctree}
:maxdepth: 2

intro
```
```

And `docs/source/intro.md`:

```markdown
# Intro

First page.
```

## Build

```bash
cd docs
sphinx-build -W -b html source build/html
python -m http.server -d build/html 8000
# open http://localhost:8000
```

The `-W` flag treats warnings as errors — the discipline that keeps a
site linkable long-term.

## Deploy to GitHub Pages

Create `.github/workflows/docs.yml`:

```yaml
name: Deploy docs
on:
  push:
    branches: [main]
permissions:
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install sphinx sphinx-rtd-theme myst-parser myst-nb sphinx-copybutton sphinx-design linkify-it-py
      - run: sphinx-build -W -b html docs/source docs/build/html
      - uses: actions/upload-pages-artifact@v3
        with: { path: docs/build/html }
      - uses: actions/deploy-pages@v4
```

Push. Enable **Settings → Pages → Source: GitHub Actions**. The site is
live at `https://<user>.github.io/<repo>/` in about two minutes.

## Where to next

→ Back to the [documentation lesson](README.md).

→ [continuous-integration](../continuous-integration/README.md) — for
the maintenance-testing pattern that runs alongside the docs deploy.
