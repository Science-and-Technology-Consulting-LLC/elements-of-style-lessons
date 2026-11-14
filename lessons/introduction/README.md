# Introduction

This lesson explains why the course follows *The Elements of Style*, then walks you through setting up your computer and running a first notebook.

> *In the book: the Introduction, and Chapter 3 — Elements of Style.*

## Before you start

None. This is the first lesson.

## Do this

1. **Clone the repository.** This copies the lessons to your computer. In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](other-places-to-run.md). If `git` is missing, the walkthrough's *Install a terminal and Git* section shows how to install it.
3. **Open the notebook** `lessons/introduction/lets-dive-in.ipynb`. From the repository folder, start JupyterLab with `jupyter lab`. Then open [`lets-dive-in.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/introduction/lets-dive-in.ipynb) and run each cell in order, top to bottom. You can also read the same steps as a web page: [Let's dive in](lets-dive-in.md).

## What you should see

- `git --version` and `conda --version` each print a version number.
- A `(eos)` prefix on your terminal prompt after `conda activate eos`.
- JupyterLab opens in your browser with a **Bash** tile in the Launcher.
- A list of tools, each with a location or the word `MISSING`.

## Where the files are

- `lessons/introduction/README.md` — this page.
- `lessons/introduction/lets-dive-in.ipynb` — the notebook you run.
- `lessons/introduction/lets-dive-in.md` — the same steps as a web page.
- `eos.yml` in the repository root — the recipe for the conda environment.

## Next

[The Rules](../elements-of-style-rules/README.md)

## Background

### The spirit

Strunk and White called *The Elements of Style* a summation of the case for cleanliness, accuracy and brevity in the use of English. Kernighan and Ritchie, and Kernighan and Plauger, brought the same spirit to programming. These lessons bring it to biomedical workflows.

Brevity and clarity matter even more when you work with an AI agent. A computer cannot reason or judge. You must say exactly what you want, and be sure of your correctness.

### The dry workbench

Treat your work on the computer like the wet bench. Keep the area clean. Make the experiment repeatable, so anyone gets the same result.

- Be clear with every step.
- Keep your environment clean.
- Do not reinvent the wheel. Find working code that already exists.
- Add a command line interface, so each step is accessible.
- Assemble the steps into a repeatable standard operating procedure.
- Inspect, simplify, and pull apart convoluted steps.
- Test, iterate and refine.
- Automate, reuse and repeat.

### Who it is for

Working scientists at any career stage, from a first terminal session to a Nextflow pipeline. Anyone whose work has to live somewhere other than a laptop.

### What you need

A computer with a terminal, a browser, and a GitHub account. The lessons work on a Mac, on Windows with Git Bash, and on Linux. You do not need administrator rights. No terminal of your own? See [Other places to run these lessons](other-places-to-run.md).

### The order of the lessons

1. **Set the stage.** This lesson, then [The Rules](../elements-of-style-rules/README.md).
2. **Foundation.** [Command line, with Git Bash](../command-line-and-git-bash/README.md), [Version control with Git](../version-control/README.md), [Reproducible environments with Conda](../conda-environments/README.md), [Interactive computing with Jupyter](../interactive-computing/README.md).
3. **Build.** [Reusable command-line tools](../reusable-clis/README.md), [Containers](../containers/README.md), [Nextflow modules](../nextflow-modules/README.md), [Nextflow workflows](../nextflow-workflows/README.md), [Differential analysis](../differential-analysis/README.md).
4. **Durable.** [Documentation](../documentation/README.md), [Continuous integration](../continuous-integration/README.md).
5. **Scale.** [Federated computing](../federated-computing/README.md), [Federated learning](../federated-learning/README.md).
6. **Agent.** [MCP server](../mcp-server/README.md), [Agentic harness](../agentic-harness/README.md), [Publishing for agents](../publishing-for-agents/README.md).
7. **Run.** [Platforms](../platforms/README.md).

### The notebooks in this lesson

1. [Let's dive in](lets-dive-in.md) — set up your computer and run a first notebook.
