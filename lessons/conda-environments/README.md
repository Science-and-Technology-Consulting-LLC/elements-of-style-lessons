# Reproducible environments with Conda

> *In the book: Sections 5.2 and 5.3, Introduction to Anaconda and Packages; Creating a Conda Environment.*

This lesson gives you the `eos` conda environment, a named set of software versions that recreates the same setup on any machine, so your work stays runnable for years.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Version control with Git](../version-control/README.md), is done.

In JupyterLab, open `lessons`, then `conda-environments`, then `creating-a-conda-environment.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/conda-environments/creating-a-conda-environment.ipynb)). Run each cell in order, top to bottom.

### What you should see

- `conda --version` prints a version number.
- `conda env list` shows an environment called `eos`.
- Your terminal prompt starts with `(eos)` after `conda activate eos`.
- With the full `eos.yml` environment: `python --version` shows 3.11.x, and the JupyterLab Launcher shows Python 3, Bash and R tiles.

> **Picture to add:** a terminal with the `(eos)` prompt and the output of `conda env list` (save as assets/overview.png)

### Where the files are

- The lessons are in `lessons/conda-environments/` of the [course repository](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/conda-environments).
- The environment recipe is [`eos.yml`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/eos.yml) at the root of the repository.

## Steps to execute

1. [Creating a conda environment](creating-a-conda-environment.md): install Miniconda from scratch in a Linux Bash terminal, then create and activate a practice environment, `eos-practice`.
2. [Recap: workspace set-up](recap-workspace-setup.md): a Day 1 and Day 2 checkpoint. Move around a Git clone, use the `..` shortcut, and practise the "wipe the local tangle and clone again" recovery.

## Ask an AI assistant

*Optional.* How to use these prompts is explained in [Using the AI prompts](../introduction/README.md).

**Ask it to explain.**

```text
Explain the difference between conda, an environment, an environment.yml file and a channel, using the example of one bioinformatics tool. Keep it to ten lines.
```

**Ask it to build.**

```text
Write an environment.yml for a conda environment named <name> with Python 3.11 and these tools: <list>. Use the conda-forge and bioconda channels. Pin each version as exact as conda allows. Give me the command to create it and a one-line test that shows each tool starts.
```

**Ask it to review.**

```text
Review this environment.yml. List anything that makes it hard to repeat on another computer: unpinned versions, missing channels, packages installed with pip that conda also offers. Suggest a fix for each. Do not change the tools.

<paste file>
```


## Further reading

- [Miniforge](https://github.com/conda-forge/miniforge): installer
- [conda-forge](https://conda-forge.org/): the community package channel
- [Mamba](https://mamba.readthedocs.io/): a faster drop-in for conda
- [IRkernel](https://irkernel.github.io/): R kernel for Jupyter
- [conda documentation](https://docs.conda.io/): the authoritative reference

## Supplementary information

### Why this lesson matters

A notebook that worked yesterday usually still works today, until something updates underneath it. Conda freezes the floor under your feet. Pin the environment once and your work stays runnable for years.

### Two ways to think about conda

1. An **environment** is a folder full of compatible packages: Python, R, bioinformatics tools. You activate it before running code.
2. An **environment file** (`eos.yml` in this repository) is a recipe for that folder. Anyone with the recipe can recreate the folder.

You almost always want the recipe. Installing packages by hand "until it works" is the classic way to make work that nobody else, including future you, can reproduce.

> **Check:** The notebook `creating-a-conda-environment` makes an empty practice environment with `conda create -n eos-practice -y`, so it does not replace the `eos` that this page builds from `eos.yml`. Is that difference intended?

### Install Miniforge

The Introduction installs [Miniforge](https://github.com/conda-forge/miniforge), a clean conda install that uses the `conda-forge` channel by default. That is what you want for biomedical work. See step 3 of the [Introduction page](../introduction/README.md). To check that it is there:

```bash
conda --version
```

### What is in `eos.yml`

When resolved, `eos.yml` gives you:

- **Python 3.11 and JupyterLab**, with three registered kernels: Python 3, Bash and R (IRkernel).
- **R 4.x**, with a small tidyverse-adjacent set (`tibble`, `dplyr`, `ggplot2`, `docopt`).
- **Tools** you will reach for: `git`, `gh` (GitHub CLI), `nextflow`, `curl`, `wget`.
- **Python libraries** for the starter notebooks and case studies: `pandas`, `numpy`, `matplotlib`, `typer`, `pydantic`.
- The **Sphinx and MyST-NB** tools, so you can build the course site locally.

Podman is not installed by `eos.yml`, on purpose. A conda package of Podman exists, but on a Mac I could not make it start the virtual machine that Podman needs (it stopped with an error about `gvproxy`). Install Podman with the system package manager instead: `brew` on macOS, the Podman installer on Windows, `apt` or `dnf` on Linux. See [Install Podman](../containers/README.md).

### Create the `eos` environment from `eos.yml`

The Introduction already did this in step 4, with these lines. The first `conda env create` takes a few minutes, because conda downloads and resolves a few hundred packages. After that, activation is instant.

```bash
cd elements-of-style-lessons
conda env create -f eos.yml
conda activate eos
```

Confirm the essentials:

```bash
python --version    # 3.11.x
R --version         # 4.x
jupyter --version   # 4.x
gh --version
nextflow -version
```

The Introduction also registered the Bash and R kernels, which is why the Launcher shows Python 3, Bash and R tiles. `eos.yml` installs `bash_kernel` (with pip) and `r-irkernel` (with conda), and each needs that one-time registration.

### Editing the environment

When you need a new package, add it to `eos.yml`. Do not `pip install` ad hoc into the environment. Then run:

```bash
conda env update -f eos.yml --prune
```

The `--prune` flag also removes packages you deleted from the file. This keeps the file and the environment in sync, which is the whole point.

### Which environment am I in?

```bash
conda info --envs    # lists all environments; the active one has a *
which python         # the full path tells you where you are
```

If the path does not contain `envs/eos`, you forgot to run `conda activate eos`. This happens to everyone.

## Next

[Interactive computing with Jupyter](../interactive-computing/README.md): run your code in notebooks.
