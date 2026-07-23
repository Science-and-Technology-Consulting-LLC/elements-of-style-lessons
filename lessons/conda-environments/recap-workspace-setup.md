# Recap — workspace setup

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-3-containerization/recap-workspace-setup/)) — woven into
the [conda-environments](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`recap-workspace-setup.ipynb`](recap-workspace-setup.ipynb) — every code cell
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


## What you have built so far

### Day 1 — reasoning

- Met the [Elements of Style](../elements-of-style-rules/README.md) approach.
- Opened a JupyterLab notebook (on CAVATICA in the NICHD course, or on your
  laptop / Lifebit here). See [interactive-computing](../interactive-computing/README.md).
- Inspected a real R notebook — `exampleVolcanoPlot.ipynb`.

### Day 2 — code versioning

- Learned what Git, GitHub, version control, and attribution give you.
- Forked, cloned, edited, staged, committed, pushed, and opened a pull
  request. See the [version-control walkthroughs](../../version-control/ipynb/).

## The missing pieces in the volcano-plot notebook

The R notebook `Reading-data-and-plotting-in-R.ipynb` needs three things
before it runs cleanly:

1. **The data** — from Zenodo at DOI [10.5281/zenodo.7510587](https://doi.org/10.5281/zenodo.7510587).
2. **The R package dependencies** — installed once via
   `Rscript install_dependencies.R`.
3. **One extra `library()` call** — `library(rlang)` — that wasn't declared
   in the original.

These fixes are in the upstream copy at
[`adeslatt/exampleVolcanoPlotNotebook`](https://github.com/adeslatt/exampleVolcanoPlotNotebook),
and — if you've synced your fork with `NIH-NICHD/exampleVolcanoPlotNotebook`
per the [`keeping-your-repository-fork-in-sync`](../../version-control/ipynb/keeping-your-repository-fork-in-sync.ipynb)
walkthrough — into your fork too.

## Navigate to the right directory

Start from your personal directory (named after your GitHub username):

```bash
cd <your-github-username>
```

```bash
git status
```

If `git status` complains about not being in a repo, you're one
level too high. `ls -l` to see what's around:

```bash
ls -l
```

```bash
cd exampleVolcanoPlotNotebook
git status
```

```bash
git diff
```

## The "start over" move

Sometimes your local copy has drifted from the remote in ways that aren't
worth untangling. If (and *only* if) your work is already safely pushed to
GitHub, the fastest recovery is to wipe the local directory and re-clone.

### Two navigation shortcuts

- `.` is the *current* directory.
- `..` is the *parent* directory (one level up).

Confirm where you are:

```bash
cd .
ls -l
```

Move up one level:

```bash
cd ..
ls -l
```

Wipe the tangled clone:

```bash
rm -f -R exampleVolcanoPlotNotebook
```

(`-f` forces without prompting, `-R` recurses into subdirectories. See
[ExplainShell](https://explainshell.com/explain?cmd=rm+-f+-R) for the
breakdown.)

Then re-clone a fresh copy:

```bash
git clone https://github.com/adeslatt/exampleVolcanoPlotNotebook.git
```

> **Note on the URL** — the origin is `adeslatt/exampleVolcanoPlotNotebook`;
> `NIH-NICHD/exampleVolcanoPlotNotebook` is a fork of it for the NICHD
> teaching context. Either works; the `adeslatt` upstream is where fixes
> land first.

Open the notebook, clear all outputs (JupyterLab: *Edit → Clear All Outputs*),
restart the kernel (*Kernel → Restart Kernel*), and re-run.

## Where to next

You now have git + conda + the courage to blow away a broken clone and start
over. Time for [containers](../containers/README.md).
