# Why Git and GitHub?

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-2-code-versioning/why-git-and-setup/)) — woven into
the [version-control](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`why-git-and-setup.ipynb`](why-git-and-setup.ipynb) — every code cell
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


## Motivation

**Git** is a version-control system for code with several benefits you feel
immediately:

- Protects code from being lost on local machines or ephemeral environments.
- Tracks every change as the project moves.
- Lets you revisit any older version of the code, notebooks, and documentation.
- Supports maintaining multiple versions at once (branches).

**GitHub** is a code-hosting platform for that version-controlled code:

- Access to a large community of open-source projects.
- Multiple contributors on the same project.
- A discoverable, transparent record of the methods behind a paper.

## Set-up in a terminal

Open a **Terminal** — on your laptop, on a Lifebit notebook server, or on a
Cavatica Data Studio session. The steps below work identically in all three.

### Editing files with `nano`

`nano` is a simple in-terminal file editor with four moves:

1. **Open** — `nano hello.txt` opens the file (or creates it if new).
2. **Write** — type as you would in any editor.
3. **Save** — `CTRL-O`, then `ENTER` to confirm.
4. **Exit** — `CTRL-X`.

Verify with `head`:

```bash
head hello.txt
```

### Create a conda environment for these lessons

We keep the tools we install for this course isolated in a conda environment
called `eos`. Details of *why* conda and *how* environments work live in the
[conda-environments](../conda-environments/README.md) lesson.

```bash
conda create -n eos -y
```

```bash
conda activate eos
```

Install the GitHub CLI:

```bash
conda install -c conda-forge gh -y
```

Optionally install a terminal editor other than `nano`:

```bash
conda install -c conda-forge emacs -y
```

## Configure your Git identity

Every commit records *who made it*. That is `user.name` and `user.email` at
the git level. Set them once, globally, and every future commit is stamped
with these values.

```bash
git config --global user.name  '<your github user name>'
git config --global user.email '<the email tied to your github account>'
```

Set your preferred in-terminal editor (optional):

```bash
git config --global core.editor nano
# or
# git config --global core.editor emacs
# git config --global core.editor vim
```

## Where to next

→ [`workspace-setup.ipynb`](workspace-setup.ipynb) — pick your
notebook environment: laptop, Lifebit, or Cavatica.

→ [`github-authenticate.ipynb`](github-authenticate.ipynb) — generate a
personal access token and sign in via `gh auth login`.
