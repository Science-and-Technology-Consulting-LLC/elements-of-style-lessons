# Keeping your repository fork in sync

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-2-code-versioning/keeping-your-repository-fork-in-sync/))
— woven into the [version-control](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`keeping-your-repository-fork-in-sync.ipynb`](../ipynb/keeping-your-repository-fork-in-sync.ipynb) — every code cell
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


## The vocabulary of Git and GitHub

Four verbs come up over and over:

- **Clone** — make a working copy of someone else's repository.
- **Fork** — make your own copy of someone else's repository, one you will
  edit and possibly contribute back to.
- **Pull** — bring changes down (from a remote into your local copy).
- **Push** — send your local changes up to the remote.

## Fork the volcano plot repository

**Step 1** — In your browser, go to
[https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook](https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook).

**Step 2** — Click **Fork** (top right, next to *Edit Pins* / *Watch*).
Choose *your own* GitHub account as the fork destination.

A progress window shows the *Forking* in progress. On success the page
switches to `<your-github-username>/exampleVolcanoPlotNotebook`.

## Clone your fork

Grab a working copy on the machine where you'll be editing:

```bash
git clone https://github.com/<your-github-username>/exampleVolcanoPlotNotebook.git
cd exampleVolcanoPlotNotebook
```

## Sync the fork to the upstream

Time passes. The upstream repository (`NIH-NICHD/exampleVolcanoPlotNotebook`)
gets new commits. Your fork does not — until you sync it.

**In the GitHub web UI:**

1. Navigate to your fork's page.
2. GitHub tells you: *"This branch is N commits behind
   NIH-NICHD/exampleVolcanoPlotNotebook:main."*
3. Below the *Code* button, click **Sync fork → Update branch**.
4. GitHub reports *Successfully fetched and fast-forwarded*.

Your fork is now up to date with the upstream `main`.

**From the terminal** (once you've configured an `upstream` remote — see the
[git-survival-guide](../git-survival-guide.md) for the setup):

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## Where to next

→ Back to the [version-control lesson](README.md) for the full
survival guide, including branches, rebasing, and conflict resolution.

→ Then [conda-environments](../conda-environments/README.md).
