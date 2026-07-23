# The add–commit–push routine

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-2-code-versioning/the-add-push-git-routine/)) — woven into
the [version-control](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`the-add-push-git-routine.ipynb`](the-add-push-git-routine.ipynb) — every code cell
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


## Setup

Make a directory that carries your GitHub username — this is *your* place in
the shared workspace so the class doesn't collide file-names:

```bash
mkdir <your-github-username>
cd <your-github-username>
```

Clone your fork of the demo repository. If you already forked
[NIH-NICHD/exampleVolcanoPlotNotebook](https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook)
(see [`keeping-your-repository-fork-in-sync.ipynb`](keeping-your-repository-fork-in-sync.ipynb)),
replace `<your-github-username>` in the URL below with your own:

```bash
git clone https://github.com/<your-github-username>/exampleVolcanoPlotNotebook.git
cd exampleVolcanoPlotNotebook
```

## `git status` — the command you'll use every day

`git status` tells you what has changed in your local copy since the last
commit. Nothing is more useful.

```bash
git status
```

Expected output when nothing has changed:

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Edit a file

Open `README.md` in nano (or any editor) and add a line like:

```
Learn about Zenodo here: https://zenodo.org
```

Save (`CTRL-O`, `ENTER`) and exit (`CTRL-X`).

Confirm the file has the change:

```bash
head README.md
```

## Inspect changes with `git status`

```bash
git status
```

You'll now see:

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   README.md

no changes added to commit (use "git add" to update)
```

## `git add` — stage the change

`add` moves the change from "unstaged" to "staged" — a candidate for the
next commit:

```bash
git add README.md
```

## `git commit` — save it locally

A **commit message** is a note-to-future-self about *what* changed and
*why*. Present tense, short, specific.

```bash
git commit -m 'added Zenodo pointer to README'
```

## `git push` — send it to GitHub

```bash
git push
```

## `git status` — confirm all is quiet

```bash
git status
```

## The pull request

Once the change is on your fork, open the GitHub web UI:

1. Navigate to your fork's page.
2. GitHub shows a banner: *"This branch is 1 commit ahead of upstream"*.
3. Click **Contribute → Open pull request**.
4. Write a short PR description.
5. Submit.

The upstream maintainer now sees your proposed change and can accept it,
comment, or request changes.

## Recap

You just walked the whole loop:

- ✅ Cloned a fork.
- ✅ Edited a file.
- ✅ Inspected with `git status`.
- ✅ Staged with `git add`.
- ✅ Recorded a versioned snapshot with `git commit`.
- ✅ Sent it up with `git push`.
- ✅ Offered it upstream as a pull request.

Welcome to the world of documenting your work with GitHub.

## Where to next

→ [`keeping-your-repository-fork-in-sync.ipynb`](keeping-your-repository-fork-in-sync.ipynb) —
when the upstream repo moves forward, how to catch your fork up.
