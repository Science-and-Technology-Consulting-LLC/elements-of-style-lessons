# Reproducible environments with Conda


> *In the book: Chapter 5 — Reproducible environments with Conda.*

:::{admonition} What you'll learn
:class: tip

- Why pinning beats remembering.
- Create the `eos-lessons` env and activate it everywhere.
- Register the R kernel so Jupyter sees both R and Python.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

Reproducibility starts with knowing *which versions of which packages* your
code needs. Conda is the most common way biomedical projects answer that
question. One file — `environment.yml` — lists everything, and one command
recreates the environment from scratch.

:::{admonition} Why this step matters
:class: tip

A notebook that "worked yesterday" usually still works today — until
something updates underneath it. Conda freezes the floor under your feet.
Pin the env once and your work stays runnable for years.
:::

## Install Miniforge (the lightweight, conda-forge-first installer)

Miniforge is a clean Conda install that defaults to the `conda-forge`
channel — which is what you want for biomedical work.

- **macOS / Linux:** https://github.com/conda-forge/miniforge#install
- **Windows (with Git Bash):** download the Windows `.exe` from the same
  page and run it. Reopen Git Bash afterward.

Verify:

```bash
conda --version
```

## Two ways to think about Conda

1. An **environment** is a folder full of compatible packages — Python,
   R, bioinformatics tools, whatever. You activate it before running code.
2. An **`environment.yml`** is a recipe for that folder. Anyone with the
   recipe can recreate the folder.

You almost always want the recipe. Hand-installing packages "until it
works" is the classic way to make work that nobody else (including future
you) can reproduce.

## Install Miniforge (one time)

::::{tab-set}

:::{tab-item} macOS
:sync: mac

```bash
# Apple Silicon or Intel — Miniforge has installers for both.
# Download from https://github.com/conda-forge/miniforge#install
bash Miniforge3-MacOSX-arm64.sh    # or -x86_64 on Intel
```
:::

:::{tab-item} Windows (Git Bash)
:sync: win

```bash
# Download Miniforge3-Windows-x86_64.exe from
# https://github.com/conda-forge/miniforge#install — run it.
# Then reopen Git Bash so PATH picks up conda.
conda --version
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# Lifebit notebook servers ship mamba/conda pre-installed.
mamba --version    # or: conda --version
```
:::

::::

## Create the environment for this site

This lessons repo ships an `environment.yml` at the root. From the repo:

```bash
cd elements-of-style-lessons
conda env create -f environment.yml   # creates an env called "eos-lessons"
conda activate eos-lessons
```

The first run takes a few minutes — Conda is downloading and resolving a
few hundred packages. After that, activation is instant.

To confirm:

```bash
python --version
R --version
jupyter --version
```

You should see Python 3.10, R 4.x, and Jupyter all available.

## Register the R kernel for Jupyter

R notebooks in Jupyter need the **IRkernel** to be registered with Jupyter
once per environment. This repo's `environment.yml` already installs
`r-irkernel`; you just need to tell Jupyter about it:

```bash
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

Now when you open Jupyter and click *New*, you'll see both **Python 3** and
**R** as kernel options.

## Editing the environment

When you need a new package, add it to `environment.yml` (don't `pip
install` ad-hoc into the env), then:

```bash
conda env update -f environment.yml --prune
```

The `--prune` flag also removes packages you deleted from the file. This
keeps the file and the env in sync, which is the whole point.

## A common gotcha: which env am I in?

```bash
conda info --envs    # lists all envs; the active one has a *
which python         # full path tells you where you are
```

If the path doesn't include `envs/eos`, you forgot to `conda activate eos`.
Happens to everyone.

## Where to next

→ Next lesson: [Interactive computing with Jupyter](interactive-computing.md)
