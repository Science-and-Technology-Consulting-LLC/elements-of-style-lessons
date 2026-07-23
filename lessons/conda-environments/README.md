# Reproducible environments with Conda


> *In the book: Chapter 5 — Reproducible environments with Conda.*

:::{admonition} What you'll learn
:class: tip

- Why pinning beats remembering.
- Create the `eos` env and activate it everywhere.
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
question. One file — `eos.yml` (in the repo root) — lists everything, and
one command recreates the environment from scratch.

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
2. An **environment file** (`eos.yml` in this repo) is a *recipe* for
   that folder. Anyone with the recipe can recreate the folder.

You almost always want the recipe. Hand-installing packages "until it
works" is the classic way to make work that nobody else (including future
you) can reproduce.

## What's in `eos.yml`

The [`eos.yml`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/eos.yml)
at the root of this repo is the single environment file for the whole
curriculum. When resolved it gives you:

- **Python 3.11 + JupyterLab** with three registered kernels:
  **Python 3**, **Bash**, and **R** (IRkernel).
- **R 4.x** with a small tidyverse-adjacent set (`tibble`, `dplyr`,
  `ggplot2`, `docopt`).
- **Tools** every reader reaches for: `git`, `gh` (GitHub CLI),
  `nextflow`, `curl`, `wget`.
- **Python libraries** for the starter notebooks and case studies:
  `pandas`, `numpy`, `matplotlib`, `typer`, `pydantic`.
- The **Sphinx + MyST-NB** stack so you can build this site locally.

Docker is *not* installed by `eos.yml` — it needs the system package
manager (Docker Desktop on macOS/Windows, `apt`/`dnf` on Linux; it's
already on Lifebit compute). See [containers](../containers/README.md).

## Create the `eos` environment — per venue

::::{tab-set}

:::{tab-item} On your laptop (macOS)
:sync: mac

Install Miniforge once, then create the env from `eos.yml`.

```bash
# 1. Miniforge — the lightweight, conda-forge-first installer.
#    Apple Silicon or Intel — Miniforge has installers for both.
#    Download from https://github.com/conda-forge/miniforge#install
bash Miniforge3-MacOSX-arm64.sh    # or -x86_64 on Intel

# 2. Create the eos environment from the repo file.
cd elements-of-style-lessons
conda env create -f eos.yml
conda activate eos
```
:::

:::{tab-item} On your laptop (Windows Git Bash)
:sync: win

```bash
# 1. Download Miniforge3-Windows-x86_64.exe from
#    https://github.com/conda-forge/miniforge#install and run it.
#    Then reopen Git Bash so PATH picks up conda.
conda --version

# 2. Create the eos environment.
cd elements-of-style-lessons
conda env create -f eos.yml
conda activate eos
```
:::

:::{tab-item} In Google Cloud Shell
:sync: gcs

Open <https://shell.cloud.google.com/> (any Google account).
Miniconda isn't pre-installed — bootstrap it once, then create `eos`.

```bash
# 1. Install Miniconda (see creating-a-conda-environment.md for the
#    full walkthrough).
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda3
exec -l bash

# 2. Clone the repo and create the eos environment.
git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
cd elements-of-style-lessons
conda env create -f eos.yml
conda activate eos
```
:::

:::{tab-item} On Lifebit CloudOS
:sync: lifebit

```bash
# Lifebit notebook servers ship mamba/conda pre-installed —
# just clone and create.
git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
cd elements-of-style-lessons
conda env create -f eos.yml
conda activate eos
```
:::

::::

The first `conda env create` takes a few minutes — Conda is downloading
and resolving a few hundred packages. After that, activation is instant.

Confirm the essentials:

```bash
python --version    # 3.11.x
R --version         # 4.x
jupyter --version   # 4.x
gh --version
nextflow -version
```

## Register the Bash and R Jupyter kernels

`eos.yml` installs `bash_kernel` (pip) and `r-irkernel` (conda) but they
need a one-time registration so JupyterLab shows a **Bash** and an
**R** tile in the launcher:

```bash
conda activate eos
python -m bash_kernel.install
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

Restart JupyterLab; the launcher now shows Python 3, Bash, and R.

## Editing the environment

When you need a new package, add it to `eos.yml` (don't `pip install`
ad-hoc into the env), then:

```bash
conda env update -f eos.yml --prune
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

## In-depth walkthroughs

Two walkthroughs adapted from the NICHD Kids First / INCLUDE course:

- [`creating-a-conda-environment.md`](creating-a-conda-environment.md) —
  install Miniconda from scratch in Google Cloud Shell (or any Bash terminal),
  create and activate an `eos` environment.
- [`recap-workspace-setup.md`](recap-workspace-setup.md) —
  a Day-1 + Day-2 checkpoint: navigating a git clone, the `..` shortcut, and
  the classic *"wipe the local tangle and re-clone"* recovery move.

## Further reading

- [Miniforge](https://github.com/conda-forge/miniforge) — installer
- [conda-forge](https://conda-forge.org/) — the community package channel
- [Mamba](https://mamba.readthedocs.io/) — a faster drop-in for conda
- [IRkernel](https://irkernel.github.io/) — R kernel for Jupyter
- [conda documentation](https://docs.conda.io/) — the authoritative reference


## Where to next

→ Next lesson: [Interactive computing with Jupyter](interactive-computing.md)
