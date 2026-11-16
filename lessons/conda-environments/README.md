# Reproducible environments with Conda

> *In the book: Sections 5.2 and 5.3, Introduction to Anaconda and Packages; Creating a Conda Environment.*

This lesson gives you the `eos` conda environment, a named set of software versions that recreates the same setup on any machine, so your work stays runnable for years.

## Start here

### Before you start

The previous lesson is [Version control with Git](../version-control/README.md). You need Git and a terminal.

### Do this

1. **Clone the course.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the first notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Open `lessons/conda-environments/creating-a-conda-environment.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/conda-environments/creating-a-conda-environment.ipynb)). Run each cell in order, top to bottom.

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

Work through the notebooks in this order:

1. [creating-a-conda-environment.md](creating-a-conda-environment.md): install Miniconda from scratch in a Linux Bash terminal, then create and activate an `eos` environment.
2. [recap-workspace-setup.md](recap-workspace-setup.md): a Day 1 and Day 2 checkpoint. Move around a Git clone, use the `..` shortcut, and practise the "wipe the local tangle and clone again" recovery.

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

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

> **Check:** The notebook `creating-a-conda-environment` makes an empty environment with `conda create -n eos -y`, while this page makes it from `eos.yml`. Is that difference intended?

### Install Miniforge

[Miniforge](https://github.com/conda-forge/miniforge) is a clean conda install that uses the `conda-forge` channel by default. That is what you want for biomedical work.

- **macOS and Linux:** [conda-forge.org/download](https://conda-forge.org/download/), or the [Miniforge install notes](https://github.com/conda-forge/miniforge#install).
- **Windows (with Git Bash):** download the Windows `.exe` from the same page and run it. Reopen Git Bash afterwards.

Check it:

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

The first `conda env create` takes a few minutes, because conda downloads and resolves a few hundred packages. After that, activation is instant.

**On your laptop (macOS).** Install Miniforge once, then create the environment from `eos.yml`:

```bash
# 1. Miniforge. Apple Silicon or Intel, there is an installer for both.
#    Download from https://github.com/conda-forge/miniforge#install
bash Miniforge3-MacOSX-arm64.sh    # or -x86_64 on Intel

# 2. Create the eos environment from the repo file.
cd elements-of-style-lessons
conda env create -f eos.yml
conda activate eos
```

**On your laptop (Windows Git Bash):**

```bash
# 1. Download Miniforge3-Windows-x86_64.exe from
#    https://conda-forge.org/download/ and run it.
#    Then reopen Git Bash so it finds conda.
conda --version

# 2. Create the eos environment.
cd elements-of-style-lessons
conda env create -f eos.yml
conda activate eos
```

**On Linux.** Install Miniforge the same way as on macOS, using the Linux installer. No Linux terminal? See [Other places to run these lessons](../introduction/other-places-to-run.md), which covers Google Cloud Shell and Lifebit.

Confirm the essentials:

```bash
python --version    # 3.11.x
R --version         # 4.x
jupyter --version   # 4.x
gh --version
nextflow -version
```

### Register the Bash and R Jupyter kernels

`eos.yml` installs `bash_kernel` (with pip) and `r-irkernel` (with conda). They need a one-time registration so JupyterLab shows a **Bash** tile and an **R** tile in the Launcher:

```bash
conda activate eos
python -m bash_kernel.install
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

Restart JupyterLab. The Launcher now shows Python 3, Bash and R.

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
