# Let's dive in

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-1-reasoning/lets-dive-in/)) — woven into
the [introduction](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`lets-dive-in.ipynb`](../ipynb/lets-dive-in.ipynb) — every code cell
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


## Get a machine up before the reasoning starts

Before we spend any time on the *"how does a workflow work"* discussion, we
get a notebook running. Once it's up it stays up for about 30 minutes of
idle time, which is exactly the window Day 1 fills.

## Fast-track — CAVATICA account (if you're new)

If you haven't registered yet:

1. Go to [https://cavatica.sbgenomics.com/](https://cavatica.sbgenomics.com/).
2. Click **Create an account** or **Log in with eRA Commons**.
3. NICHD training runs one support hour after each daily class — use it.

Full click-by-click walkthroughs live in the
[platforms](../platforms/README.md) lesson:

- [`creating-a-cavatica-account.md`](../platforms/creating-a-cavatica-account.md)
- [`logging-into-cavatica-step-by-step.md`](../platforms/logging-into-cavatica-step-by-step.md)

## Log in and start a notebook

Once your account exists, the two-step opener is:

1. Log in to CAVATICA.
2. Create a project → **Data Studio → New Analysis → JupyterLab → Start**.

That drops you into a browser-based JupyterLab session with a terminal,
`git`, `conda`, `docker`, and `nextflow` pre-installed.

## If you're on your laptop instead

Same idea, less clicking:

```bash
conda activate eos-lessons
jupyter lab
```

The rest of Chapter 3 onwards works identically whether the terminal is
CAVATICA's, Lifebit's, or your laptop's.

## Where to next

→ [Chapter 3 — command-line-and-git-bash](../command-line-and-git-bash/README.md).
