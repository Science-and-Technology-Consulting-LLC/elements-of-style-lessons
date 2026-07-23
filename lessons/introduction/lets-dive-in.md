# Let's dive in

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-1-reasoning/lets-dive-in/)) — woven into
the [introduction](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`lets-dive-in.ipynb`](lets-dive-in.ipynb) — every code cell
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


## Get a terminal open before the reasoning starts

Before we spend any time on the *"how does a workflow work"* discussion,
get a terminal open. Every subsequent chapter assumes one.

The elements-of-style lessons use **your laptop first**. If you don't
have a laptop terminal handy, **Google Cloud Shell** is a free
browser-based terminal that needs only a Google account. **Lifebit
CloudOS** is what you reach for when the work needs to scale.

## On your laptop (recommended for lessons 1–8)

```bash
conda activate eos-lessons
jupyter lab
```

That opens a browser-based JupyterLab with a terminal, `git`, `conda`,
`docker`, and `nextflow` on your PATH. If any of those is missing,
[conda-environments](../conda-environments/README.md) walks the install.

## In Google Cloud Shell (free, browser-based)

1. Open <https://shell.cloud.google.com/> and sign in with any Google
   account.
2. You land in a fully-provisioned bash terminal with `git`, `conda`,
   `docker` pre-installed.
3. If it's your first time, run through
   [conda-environments/creating-a-conda-environment.md](../conda-environments/creating-a-conda-environment.md)
   to bootstrap `conda` and the `eos` environment.

## On Lifebit CloudOS (when the work scales)

1. Sign up at <https://cloudos.lifebit.ai/register>.
2. Sign in at <https://cloudos.lifebit.ai/login>.
3. Create a workspace; open its JupyterLab terminal.

See [platforms/README.md](../platforms/README.md) for the fuller
Lifebit story.

## If you're doing NICHD Kids First / INCLUDE work

The elements-of-style examples don't use CAVATICA — but the Kids First /
INCLUDE course does. Full CAVATICA walkthroughs live in the
[platforms](../platforms/README.md) lesson:

- [`creating-a-cavatica-account.md`](../platforms/creating-a-cavatica-account.md)
- [`logging-into-cavatica-step-by-step.md`](../platforms/logging-into-cavatica-step-by-step.md)
- [`starting-a-jupyter-lab-notebook.md`](../interactive-computing/starting-a-jupyter-lab-notebook.md)

## Where to next

→ [Chapter 3 — command-line-and-git-bash](../command-line-and-git-bash/README.md).
