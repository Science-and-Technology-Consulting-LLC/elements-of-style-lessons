# GitHub authentication

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-2-code-versioning/github-authenticate/)) — woven into
the [version-control](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`github-authenticate.ipynb`](github-authenticate.ipynb) — every code cell
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


## Why authenticate

To contribute to any GitHub repository — even one you own — you first prove
who you are. The GitHub CLI (`gh`) does this in one step, but it needs a
**Personal Access Token (PAT)**: a private secret key that tells GitHub
*this terminal session is Annie*.

`gh` came from the [Anaconda package library](https://anaconda.org/anaconda/repo)
(the same source we use for `conda install` in
[conda-environments](../conda-environments/README.md)). **CLI** stands for
*Command Line Interface* — the shell-driven applications we've been using for
two lessons now.

## Generate a Personal Access Token

In a browser, go to your GitHub account and follow six clicks:

1. Click your **profile avatar** (top right) → **Settings**.
2. Scroll to the bottom of the left sidebar and click **Developer settings**.
3. Click **Personal access tokens** (the third item from the top).
4. Click **Generate new token** (top right). Give it a note, e.g. `eos`.
5. Select all the scope options (you can trim later).
6. Click **Generate token** — and **copy the token immediately**. GitHub will
   never show it to you again. If you lose it, generate a fresh one.

## Authenticate

Back in the terminal:

```bash
gh auth login
```

`gh` will ask a few questions — the sensible answers:

- **What account** → *GitHub.com* (usually the default).
- **Preferred protocol** → *HTTPS*.
- **Authenticate with GitHub credentials** → *Yes*.
- **How to authenticate** → *Paste an authentication token*. Paste the PAT
  you just copied.

If everything worked, `gh` prints a happy checkmark and you are ready to
`git push` for real.

## Where to next

→ [`the-add-push-git-routine.ipynb`](the-add-push-git-routine.ipynb) — the
daily `add → commit → push` loop that turns work-in-progress into a shared
record.
