# Interactive computing with Jupyter


> *In the book: Chapter 6 — Interactive computing with Jupyter.*

:::{admonition} What you'll learn
:class: tip

- What a Jupyter kernel actually is — and why that matters.
- Launch JupyterLab on your machine or on a Lifebit notebook.
- The Restart-and-Run-All habit that catches order-of-cell bugs.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

A Jupyter notebook is one of the most welcoming places to start a new
analysis: write a few lines, run them, see the result, write a few more.
It's also one of the most misunderstood — full of moving parts (kernels,
sessions, checkpoints, magic commands) that nobody explains because
"everyone knows."

This step explains them. Then we run two short notebooks together: one in
Python, one in R.

:::{admonition} What you'll have at the end
:class: tip

A clear mental model of what a kernel is, why "Restart and Run All" is the
single most important button in your career as a notebook user, and two
working notebooks you can edit, rerun, and use as templates for your own
exploration.
:::

## What a notebook actually is

A Jupyter notebook is a **JSON file** (extension `.ipynb`) containing an
ordered list of **cells**. Each cell is either:

- **Markdown** — text, headings, links, math.
- **Code** — sent to a **kernel** for execution.

The **kernel** is a separate process that runs your code. When you open a
Python notebook, Jupyter starts a Python kernel in the background. When you
open an R notebook, it starts an R kernel. Variables you create live in
*the kernel*, not in the file. That's why restarting the kernel wipes them.

## Launch Jupyter

In your terminal, with the `eos` env active:

```bash
conda activate eos
jupyter lab
```

A browser window opens. You'll see a file tree on the left and a launcher
in the middle.

## Launch JupyterLab

::::{tab-set}

:::{tab-item} macOS / Windows
:sync: local

```bash
conda activate eos-lessons
jupyter lab
# A browser tab opens at http://localhost:8888/lab
```
:::

:::{tab-item} Lifebit
:sync: lifebit

On Lifebit, a JupyterLab session is already running — open the
notebook URL the platform gave you when the workspace started. No
`jupyter lab` invocation needed.
:::

::::

## The two starter notebooks

Open these from JupyterLab's file tree. They live in this lessons repo
under `ipynb/`:

- [`ipynb/starter_python.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/interactive-computing/notebooks/python.ipynb)
- [`ipynb/starter_r.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/interactive-computing/notebooks/r.ipynb)

Each one is short on purpose. The goal is to give you a runnable artefact
that demystifies the basics, not to teach you pandas or tidyverse — those
are the rest of your career.

In each notebook, you'll find:

1. A "What this notebook is" cell.
2. A few code cells that produce real output.
3. An "Inspect your environment" section — showing which kernel, which
   conda env, which package versions you're actually running. This is
   gold when something stops working later.
4. A "Try it yourself" prompt.

## A real worked example

If you'd like to see what a published, real-data notebook looks like — the
same pattern, just longer — open Anne's existing
[`chapters/reasoning-from-metadata/01_explore_metadata.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/chapters/reasoning-from-metadata/01_explore_metadata.ipynb)
in JupyterLab. It pulls real metadata from the ENA API for the
endometriosis dataset the book is built around. It's a great study text.

## The "Restart and Run All" habit

A notebook's cells can be run in any order. That's a feature when you're
exploring. It's a curse when you save the notebook, reopen it tomorrow, and
your variables are gone — but the cells you ran in some random order have
left output that *looks* legitimate.

**Habit:** before saving a notebook you intend to share, click
**Kernel → Restart Kernel and Run All Cells**. If the notebook still
produces the same output, it's reproducible. If it doesn't, you've just
caught a problem — better now than in a paper review.

## A note for the All of Us Researcher Workbench

The All of Us Workbench gives you Jupyter natively — Python, R, and
Nextflow are all supported. What it *doesn't* give you is a direct
`git pull` from GitHub. That doesn't have to stop you from versioning your
notebooks; it just changes the workflow. See
[Bridge patterns](../bridges/index.md) for the gentle approach.

## Where to next

→ Next lesson: [From notebooks toward Nextflow](nextflow-workflows.md)
