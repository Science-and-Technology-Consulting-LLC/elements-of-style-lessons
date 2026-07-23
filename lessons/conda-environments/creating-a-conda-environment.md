# Creating a `conda` environment

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-3-containerization/creating-a-conda-environment/)) — woven into
the [conda-environments](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`creating-a-conda-environment.ipynb`](creating-a-conda-environment.ipynb) — every code cell
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


## What conda is

`conda` is the application we use to control our environment and manage
package installs. A **conda environment** is an isolated bubble — its own
Python or R interpreter, its own set of installed packages. Nothing you
install into an environment leaks out and pollutes the system.

Making a *clean* environment first is a discipline: every assumption about
what is or isn't installed becomes explicit. Without it you inherit whatever
happens to be on the shared machine — a common cause of *"works on my
machine, breaks in the container."*

When we later build a Docker image (see [containers](../containers/README.md))
we typically start `FROM` a conda base image, so the same tool follows us
from laptop → container → workflow → federated node.

## Where you can run this

The NICHD walkthrough uses a free browser terminal — [Google Cloud Shell](https://shell.cloud.google.com/).
It's ephemeral (small disk, wiped between sessions), which makes it a good
sandbox for practising the install steps. The same commands work on your
laptop, on Lifebit, and on CAVATICA Data Studio.

## Anaconda's package search

Whenever you need to install *thing X*, the fastest lookup is a browser
search for `anaconda thing-X`, e.g. [anaconda.org search](https://anaconda.org/search).
Alongside packages you'll find tutorials, sample datasets, and hosted
notebooks — for instance [JupyterLab basics](https://anaconda.org/ijstokes/open-data-science-with-anaconda/notebook).

## Clean up the workspace first

If you're in Google Cloud Shell (limited disk), tidy up before starting:

```bash
ls -l
```

```bash
ls -la      # -a also shows hidden files (dotfiles)
```

Any command's flags can be looked up on [ExplainShell](https://explainshell.com) — e.g. [`ls -la`](https://explainshell.com/explain?cmd=ls+-la).

## Install Miniconda

We install **Miniconda** — the minimal conda installer from Anaconda. Full
Anaconda ships a lot of extras we don't need for this course.

First, confirm which OS + architecture we're on:

```bash
uname -a
```

For Linux x86_64 (Google Cloud Shell, most Lifebit hosts, most Cavatica
compute), we grab the matching installer:

```bash
which wget
```

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ls -l Miniconda3-latest-Linux-x86_64.sh
```

Now run the installer:

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Answer the prompts:

- **Press `ENTER`** to review the license (`SPACE` scrolls it faster).
- **`yes`** to accept the license terms.
- **`ENTER`** to accept the default install location.
- **`yes`** when asked *"Do you wish the installer to initialize Miniconda3 by running conda init?"*

Then reboot the shell so `conda` is on your `PATH`:

```bash
exec -l bash
```

```bash
which conda
```

If everything worked, `which conda` prints the path to the newly
installed `conda` and the shell prompt gains a `(base)` prefix.

## Create your first clean environment

Name your environment for the project. This course is *Elements of Style*,
so `eos` is a natural short name:

```bash
conda create -n eos -y
```

Activate it:

```bash
conda activate eos
```

Your prompt should now start with `(eos)` instead of `(base)`. You
are now inside the isolated bubble; anything you `conda install` from here
lands in `eos` only.

List every environment on the machine:

```bash
conda env list
```

## Recap

You just:

- Started a Bash shell in a browser via Google Cloud Shell (or your local
  terminal).
- Discovered Anaconda's community package library.
- Used `wget` to fetch the Miniconda installer.
- Installed `conda`.
- Created and activated a clean `eos` environment.

## Where to next

→ [`recap-workspace-setup.ipynb`](recap-workspace-setup.ipynb) — a
Day-1 + Day-2 recap that puts conda into context alongside the earlier
notebook and git work.

→ Then on to [containers](../containers/README.md), where the conda
environment becomes the seed for a Docker image.
