# Documentation

*In the book: Section 4.6, Documentation as a Website.*

This lesson shows you how to turn plain text files into a documentation website with [Sphinx](https://www.sphinx-doc.org/), the same tool that builds this course site. Documentation is part of the work, not an afterthought.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Continuous integration](../continuous-integration/README.md), is done. The second walkthrough uses GitHub Actions from that lesson.
- A [GitHub account](https://github.com/signup) with `gh` signed in, for the second walkthrough only. We did this in [github-authenticate](../version-control/github-authenticate.md).

### What you should see

We install Sphinx, write three small files, build them into a website, and open it in your browser at `http://localhost:8000`. Each step says what the output should look like.

> **Picture to add:** the finished example site open in a browser (save a screenshot of this lesson's landing page) (save as assets/overview.png)

### Where the files are

- `lessons/documentation/building-a-sphinx-site.ipynb`: the notebook you run. Open it from JupyterLab, or [view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/documentation/building-a-sphinx-site.ipynb).
- `lessons/documentation/building-a-sphinx-site.md`: the same walkthrough as a web page.
- `lessons/documentation/docs/`: created when you run the notebook. It holds your practice site.
- `lessons/documentation/assets/`: pictures for this lesson.

## Steps to execute

1. [`building-a-sphinx-site.md`](building-a-sphinx-site.md) — build a small Sphinx site on your computer
2. [`publish-your-site-with-actions.md`](publish-your-site-with-actions.md) — publish the site on the web with GitHub Actions (needs a GitHub account and `gh` signed in)

## Ask an AI assistant

*Optional.* How to use these prompts is explained in [Using the AI prompts](../introduction/README.md#using-the-ai-prompts).

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

A tool your collaborator cannot understand is a tool your collaborator cannot use. Documentation turns a script into a tool. It also lets an AI agent use the tool, which we come to in [MCP server](../mcp-server/README.md).

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

Every push to `main` runs `.github/workflows/docs.yml`. It installs Sphinx, builds the HTML and publishes it to GitHub Pages in about two minutes. [Publish your site with GitHub Actions](publish-your-site-with-actions.md) does this step by step.

### Writing conventions

- One `README.md` per topic under `lessons/<topic>/`. It is the canonical source.
- Use MyST admonitions (`:::{tip}`, `:::{note}`, `:::{warning}`) for callouts.
- Use `sphinx-design` tabs when a command differs by platform.
- Link to notebooks by relative path, for example `[notebook](../interactive-computing/python.ipynb)`, only where the notebook exists. That notebook is in the [Interactive computing](../interactive-computing/README.md) lesson.
- End every lesson with **Further reading** and a **Next** link.

## Next

[Introduction to Nextflow](../nextflow-workflows/README.md): put your tools, containers and documentation to work in a pipeline.
