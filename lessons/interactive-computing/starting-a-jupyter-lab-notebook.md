# Starting a JupyterLab notebook

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-1-reasoning/starting-a-jupyter-lab-notebook/)) — woven into
the [interactive-computing](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`starting-a-jupyter-lab-notebook.ipynb`](../ipynb/starting-a-jupyter-lab-notebook.ipynb) — every code cell
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


## Overview

Before you can *run* a notebook you need one to run. This walkthrough covers
the three places you're likely to open JupyterLab and the one-time setup
each of them needs.

## On your laptop

Once you've completed [conda-environments](../conda-environments/README.md)
and activated the `eos-lessons` env, launch JupyterLab from a terminal:

```bash
conda activate eos-lessons
jupyter lab
```

JupyterLab opens in your default browser. If it doesn't, look at the
terminal output for a URL of the form `http://localhost:8888/lab?token=…` and
paste it into a browser.

## On Lifebit

Lifebit's notebook servers ship JupyterLab pre-installed. From the workspace
dashboard, click **Notebook → Launch** and pick a compute size. The browser
tab opens straight into JupyterLab; the terminal is available under
*File → New → Terminal*.

## On CAVATICA (the NICHD course path)

CAVATICA's Data Studio hosts JupyterLab as a paid interactive session.
Three configuration moves matter on first use:

1. **Create a project.** Click *Create a Project* from the dashboard. Use a
   descriptive name (NICHD uses `Kids-First-INCLUDE-eos`). The project URL
   will incorporate your user ID.

2. **Select the billing group.** For NICHD training, participants share the
   billing group `EoS-Include-KidsFirst`. In a personal project you'll pick
   your own billing group.

3. **Enable network access.** This is *mandatory* — without it your notebook
   cannot `pip install`, `git clone`, or `wget`. Toggle **Allow network access**
   before starting.

Once the project is configured, navigate to **Data Studio → New Analysis**,
name it (NICHD example: `Kids-First-INCLUDE-eos-analysis`), select
**JupyterLab** as the environment, review, and hit **Start**.

## What "started" looks like

However you got here, you now see:

- A **file browser** on the left.
- A **launcher panel** in the centre showing tiles: *Python 3*, *R* (if
  you registered IRkernel — see [conda-environments](../conda-environments/README.md)),
  *Terminal*, *Text File*.
- A **menu bar** across the top: *File, Edit, View, Run, Kernel, Tabs, …*.

## Where to next

→ [`running-a-jupyterlab-notebook.ipynb`](running-a-jupyterlab-notebook.ipynb) —
clone your first notebook repository and run its cells end-to-end.

→ Back to the [interactive-computing lesson](README.md) for the fuller
tour of `.ipynb` cell types and the *Restart-and-Run-All* discipline.
