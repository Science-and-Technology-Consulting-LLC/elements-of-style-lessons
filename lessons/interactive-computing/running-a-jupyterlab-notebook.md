# Running a JupyterLab notebook

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-1-reasoning/running-a-jupyterlab-notebook/)) — woven into
the [interactive-computing](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`running-a-jupyterlab-notebook.ipynb`](../ipynb/running-a-jupyterlab-notebook.ipynb) — every code cell
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


## About JupyterLab

*Project Jupyter is a non-profit, open-source project, born out of the IPython
Project in 2014.* Its mission is interactive computing across programming
languages — JupyterLab supports roughly 40 language kernels via community
plugins. Python and R are the two we use most in this curriculum.

## Get a real notebook to run

The rest of this walkthrough uses `exampleVolcanoPlotNotebook` — a small R
notebook that reads DESeq2 output and draws a volcano plot. The origin lives
at [`adeslatt/exampleVolcanoPlotNotebook`](https://github.com/adeslatt/exampleVolcanoPlotNotebook);
`NIH-NICHD/exampleVolcanoPlotNotebook` is the NICHD teaching fork of it.

### 1. Navigate to the repository

Open [https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook](https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook)
in your browser.

### 2. Copy the clone URL

Click the green **Code** button → **HTTPS** → the copy icon.

### 3. Clone it in the JupyterLab terminal

Open a terminal in JupyterLab (*File → New → Terminal*), then:

```bash
git clone https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook.git
```

```bash
cd exampleVolcanoPlotNotebook
ls
```

### 4. Open the notebook

In the JupyterLab file browser (left side), navigate into
`exampleVolcanoPlotNotebook/` and double-click `Reading-data-and-plotting-in-R.ipynb`.

If the R kernel isn't offered, either (a) you're on a Python-only environment
and need to register IRkernel — see
[conda-environments](../conda-environments/README.md) — or (b) you're on
CAVATICA and the analysis was started with a Python-only image; recreate it
with **R + Python (Bioconductor)**.

### 5. Run every cell top to bottom

The keyboard move is `Shift-Enter` to run the current cell and advance to the
next. When you're done exploring, the discipline is:

> **Kernel → Restart Kernel and Run All Cells.**

If the notebook still produces the same output, you have a *reproducible*
notebook. If not, you've just caught a hidden dependency between cells —
better now than in a paper review.

## Learning outcomes

By running this notebook end-to-end you have practised:

- Logging into your environment (laptop / Lifebit / CAVATICA).
- Starting an interactive JupyterLab session.
- Cloning a repo from GitHub.
- Executing notebook cells that use an R kernel.
- Producing your first visualisation (a volcano plot).

## Where to next

→ Back to the [interactive-computing lesson](README.md) for the fuller
notebook anatomy, cell-type reference, and the *Restart-and-Run-All* ritual.

→ Then [reusable-clis](../reusable-clis/README.md) — where the notebook
code graduates into a command-line-callable tool.
