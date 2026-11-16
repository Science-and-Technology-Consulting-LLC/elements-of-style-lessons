# Documentation

*In the book: Section 4.6, Documentation as a Website.*

This lesson shows you how to turn plain text files into a documentation website with [Sphinx](https://www.sphinx-doc.org/), the same tool that builds this course site. You will see why documentation is part of the work, not an afterthought.

## Start here

### Before you start

The previous lesson is [Continuous integration](../continuous-integration/README.md). You need the `eos` environment from [Reproducible environments with Conda](../conda-environments/README.md), and the second notebook uses the ideas of GitHub Actions.

### Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/documentation/building-a-sphinx-site.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/documentation/building-a-sphinx-site.ipynb)) and run each cell in order, top to bottom. The notebook has a *Check your setup* section at the top for the Bash kernel.

### What you should see

You install Sphinx, write three small files, build them into a website, and open it in your browser at `http://localhost:8000`. Each step in the notebook says what the output should look like.

> **Picture to add:** the finished example site open in a browser (save a screenshot of this lesson's landing page) (save as assets/overview.png)

### Where the files are

- `lessons/documentation/building-a-sphinx-site.ipynb`: the notebook you run.
- `lessons/documentation/building-a-sphinx-site.md`: the same walkthrough as a web page.
- `lessons/documentation/docs/`: created when you run the notebook. It holds your practice site.
- `lessons/documentation/assets/`: pictures for this lesson.

## Steps to execute

1. [`building-a-sphinx-site.md`](building-a-sphinx-site.md) — build a small Sphinx site on your computer
2. [`publish-your-site-with-actions.md`](publish-your-site-with-actions.md) — publish the site on the web with GitHub Actions (needs a GitHub account and `gh` signed in)

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what Sphinx, MyST and a toctree are, and how a Markdown file becomes a web page. Keep it to ten lines.
```

**Ask it to build.**

```text
Create a minimal Sphinx site for my project: conf.py using myst_nb and the Read the Docs theme, an index.md with a toctree, and one page for each of these topics: <list>. Add a GitHub Actions workflow that builds with `sphinx-build -W` and publishes to GitHub Pages only from main. Give me the exact commands to build it on my computer first.
```

**Ask it to review.**

```text
Read the page below as a new user would. List every place where you would not know what to do next, every term that is not explained, and every command that has no stated output. Do not rewrite it.

<paste page>
```


## Further reading

- [Sphinx documentation](https://www.sphinx-doc.org/en/master/): the authoritative reference.
- [MyST-parser guide](https://myst-parser.readthedocs.io/en/latest/): Markdown syntax that Sphinx understands.
- [MyST-NB guide](https://myst-nb.readthedocs.io/en/latest/): notebook rendering.
- [Diátaxis](https://diataxis.fr/): a framework for organising technical documentation.
- [Write the Docs](https://www.writethedocs.org/): community and guides for documentation as a craft.

## Supplementary information

### Why documentation

A tool your collaborator cannot understand is a tool your collaborator cannot use. Documentation turns a script into a tool. It also lets an AI agent use the tool (see [MCP server](../mcp-server/README.md)).

The rule from [The Rules](../elements-of-style-rules/README.md):

> **Document data and functions.** Every column has units. Every function has a purpose. Every CLI flag has a meaning.

Sphinx lets you write the documentation once and render it as a website, a PDF or an epub.

### The toolchain this site uses

- [Sphinx](https://www.sphinx-doc.org/): the documentation generator behind the official Python docs.
- [MyST-parser](https://myst-parser.readthedocs.io/): lets you write in Markdown instead of reStructuredText.
- [MyST-NB](https://myst-nb.readthedocs.io/): shows `.ipynb` notebooks with their outputs.
- [`sphinx_rtd_theme`](https://sphinx-rtd-theme.readthedocs.io/): the Read the Docs look.
- [`sphinx-design`](https://sphinx-design.readthedocs.io/): grids, cards, tabs, admonitions.
- [`sphinx-copybutton`](https://sphinx-copybutton.readthedocs.io/): a copy button on code blocks.

### Layout of this site

```text
docs/
├── Makefile                    # `make html` builds the site
└── source/
    ├── conf.py                 # Sphinx config
    ├── index.md                # landing page
    └── lessons/
        ├── introduction.md     # include-shim -> lessons/<topic>/README.md
        ├── containers.md
        └── ...
```

Every page is either a Markdown file in `docs/source/` or an *include-shim* (a tiny file that pulls in another file) in `docs/source/lessons/`. The shims pull content from each lesson's `README.md`, so the content lives with the lesson.

### Build the course site

On a Mac, in Windows Git Bash, or on Linux, the commands are the same:

```bash
conda activate eos
cd docs && make html
python -m http.server -d build/html 8000
# open http://localhost:8000
```

On a cloud platform such as Lifebit, the workspace's port forwarding gives you the web address.

### Deploy with GitHub Pages

Every push to `main` runs `.github/workflows/docs.yml`. It installs Sphinx, builds the HTML and publishes it to GitHub Pages. This takes about two minutes. See [publish your site with GitHub Actions](publish-your-site-with-actions.md).

### Writing conventions

- One `README.md` per topic under `lessons/<topic>/`. It is the canonical source.
- Use MyST admonitions (`:::{tip}`, `:::{note}`, `:::{warning}`) for callouts.
- Use `sphinx-design` tabs when a command differs by platform.
- Link to notebooks by relative path, for example `[notebook](python.ipynb)`, only where the notebook exists.
- End every lesson with **Further reading** and a **Next** link.

## Next

[Introduction to Nextflow](../nextflow-workflows/README.md): put your tools, containers and documentation to work in a pipeline.
