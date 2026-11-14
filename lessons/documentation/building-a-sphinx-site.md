# Building a Sphinx site: the local build and deploy loop

You will build a small documentation website on your own computer and see how GitHub publishes it. Documentation is what turns a script into a tool that someone else can use.

*Part of the [documentation](README.md) lesson.*

## What you will do

- Install [Sphinx](https://www.sphinx-doc.org/) and the add-ons that read Markdown.
- Write three small files: a settings file, a home page and one more page.
- Build the files into a website of HTML pages.
- Read the workflow file that publishes the site on GitHub Pages.

## What you need

- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).
- Python 3 and `pip` inside a conda environment named `eos`. See [creating a conda environment](../conda-environments/creating-a-conda-environment.md).
- [JupyterLab](https://jupyter.org/) with a Bash kernel. The "Check your setup" section below covers the kernel.
- A [GitHub account](https://github.com/signup), only for the last step (publishing). You can do every other step without one.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`building-a-sphinx-site.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/documentation/building-a-sphinx-site.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

## Check which folder you are in

Why: the next steps create a folder called `docs`. You want it next to this notebook, not inside the repository's own `docs` folder.

```bash
pwd
```

**What you should see:** a path that ends in `lessons/documentation`. If it ends in `elements-of-style-lessons` instead, stop. The next steps would write into the repository's real `docs` folder. Close the notebook and open it again from JupyterLab's file browser, or run `cd lessons/documentation` in your terminal first.

## Install Sphinx and its add-ons

Why: [Sphinx](https://www.sphinx-doc.org/) turns text files into a website. The add-ons let it read [Markdown](https://myst-parser.readthedocs.io/) pages and notebooks, use the Read the Docs look, and add a copy button to code blocks.

Start JupyterLab from the `eos` environment: run `conda activate eos` in a terminal, then `jupyter lab`.

```bash
pip install sphinx sphinx-rtd-theme myst-parser myst-nb \
            sphinx-copybutton sphinx-design linkify-it-py
```

**What you should see:** many lines of text. Lines that start with `Requirement already satisfied` mean the package was already there. At the end you should see `Successfully installed` followed by package names, or only `already satisfied` lines. Any line that starts with `ERROR` is a problem (see below).

## Make the folders for the site

Why: Sphinx wants all the page files in one folder. The `-p` flag makes the parent folder too and does not complain if it already exists.

```bash
mkdir -p docs/source
```

**What you should see:** nothing. No message means it worked.

## Write the settings file

Why: `conf.py` tells Sphinx the name of the site, which add-ons to load and which look to use. The cell writes the file for you. `cat > file <<'EOF'` is a shell trick that sends the lines below it into a file, up to the line `EOF`.

```bash
cat > docs/source/conf.py <<'EOF'
project = "My Lessons"
author = "Your Name"

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence", "deflist", "linkify"]

html_theme = "sphinx_rtd_theme"
EOF
```

**What you should see:** nothing. To check the file is there, run `ls docs/source` in a terminal. You should see `conf.py`.

## Write the home page

Why: every Sphinx site needs a home page. This one lists the other pages in a table of contents (`toctree`).

````bash
cat > docs/source/index.md <<'EOF'
# My Lessons

Welcome.

```{toctree}
:maxdepth: 2

intro
```
EOF
````

**What you should see:** nothing.

## Write a second page

Why: the home page points at a page called `intro`. This file is that page.

```bash
cat > docs/source/intro.md <<'EOF'
# Intro

First page.
EOF
```

**What you should see:** nothing.

## Build the site

Why: this turns the three files into HTML pages. The `-W` flag treats warnings as errors. That is a good habit, because it keeps broken links out of the site.

```bash
cd docs
sphinx-build -W -b html source build/html
cd ..
```

**What you should see:** a stream of lines that starts with `Running Sphinx v7.2.6` (your version number may differ). Near the end you should see `building [html]: targets for 2 source files that are out of date`, then the lines `reading sources`, `checking consistency` and `preparing documents`. The last lines are `build succeeded.` and `The HTML pages are in build/html.` That means it worked.

## Look at the site

Why: seeing the real page is the point of the build. This command starts a small web server. It keeps running until you stop it with Ctrl-C, so it is not a notebook cell. Open a terminal, go to this folder, and run:

```text
cd docs
python -m http.server -d build/html 8000
```

Then open <http://localhost:8000> in your browser. When you are done, go back to the terminal and press Ctrl-C.

**What you should see:** a page titled *My Lessons* with the word *Welcome* and a link to *Intro*. In the terminal you will see lines that start with `GET /`.

> **Picture to add:** the finished site in the browser at localhost:8000 (save as assets/building-a-sphinx-site-step-8.png)

## Publish the site with GitHub Pages (optional)

Why: GitHub can rebuild and publish your site every time you push. You tell it how in a file called `.github/workflows/docs.yml`. A *workflow* is a list of jobs that GitHub runs for you. You need a [GitHub account](https://github.com/signup) and a repository for this step. The next lesson, [continuous integration](../continuous-integration/README.md), explains workflows in more detail.

Create `.github/workflows/docs.yml` with this content. This is a text block to read and copy, not a cell to run.

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

Then push the file to GitHub. On the repository's page open **Settings**, then **Pages**, and set **Source** to **GitHub Actions**.

**What you should see:** after the push, a new run appears on the repository's **Actions** tab. When it turns green (about two minutes), the site is live at `https://<user>.github.io/<repo>/`. Replace `<user>` with your GitHub name and `<repo>` with the repository name.

> **Picture to add:** the repository's Settings, Pages screen with Source set to GitHub Actions (save as assets/building-a-sphinx-site-step-9.png)

## If something goes wrong

- **`sphinx-build: command not found`.** The install in *Write the settings file* went into a different Python. Run `conda activate eos` in the terminal, start JupyterLab from there, and run *Write the settings file* again.
- **Build stops with `WARNING` and `build finished with problems`.** `-W` makes any warning an error. Read the line above it. It names the file and the problem, usually a typo in `conf.py` or `index.md`. Fix the file and run *Build the site* again.
- **`bash: conda: command not found` on Windows.** Open *Git Bash*, not PowerShell, and see [conda-environments](../conda-environments/README.md).
- **The page at localhost:8000 does not load.** The server from *Look at the site* is not running, or another program uses port 8000. Run the command in *Look at the site* again, or change `8000` to `8001` in both the command and the address.

## Next

[Continuous integration](../continuous-integration/README.md): the maintenance-testing pattern that runs next to the docs deploy. Or return to the [documentation lesson](README.md).
