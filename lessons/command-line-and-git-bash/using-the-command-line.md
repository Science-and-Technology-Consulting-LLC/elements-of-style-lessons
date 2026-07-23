# Using the command line

*Adapted from the NICHD Kids First / INCLUDE course
(https://nih-nichd.github.io/classes/day-1-reasoning/using-the-command-line/) — woven into
the [command-line-and-git-bash](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`using-the-command-line.ipynb`](../ipynb/using-the-command-line.ipynb) — every code cell
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


## Why this notebook exists

A terminal window is the text interface where you type instructions to your
computer instead of clicking icons. Every workflow tool in the rest of this
curriculum — `git`, `conda`, `docker`, `nextflow` — is driven from the terminal.
Getting comfortable here is the single largest one-time investment you can make.

This walkthrough is exactly seven commands. Each one shows up in every
subsequent lesson.

:::{tip}
**ExplainShell** — when you meet an unfamiliar command in the wild, paste it
into [explainshell.com](https://explainshell.com) and it will annotate every
flag against the official man page.
:::

## 1. `ls` — list files in the current folder

`ls -l` lists everything in your current directory in long form (permissions,
owner, size, modification time).

```bash
ls -l
```

## 2. `pwd` — print working directory

`pwd` prints the absolute path of the folder you are currently in.

> An *absolute* path starts from the filesystem root (e.g. `/home/annie/work`).
> A *relative* path starts from wherever you are now (e.g. `../data`).
> See [Absolute vs. relative paths](https://linuxfoundation.org/blog/classic-sysadmin-absolute-path-vs-relative-path-in-linux-unix/)
> for the crisp explanation.

```bash
pwd
```

## 3. `cp` — copy a file

First, create a small file using `echo` with the `>` redirect operator, which
writes the string on the left into the file on the right:

```bash
echo 'I am the header of your first README.md' > README.md
ls -l README.md
```

Now make a copy:

```bash
cp README.md duplicated_README.md
ls -l README.md duplicated_README.md
```

View a file's contents with `more` or `less`:

```bash
more README.md
```

## 4. `rm` — delete a file

Removes the named file. There is no trash bin in the terminal — the file is gone.

```bash
rm duplicated_README.md
ls -l
```

## 5. `mkdir` — create a new directory (folder)

*Directory* and *folder* mean the same thing.

```bash
mkdir new_folder
ls -l
```

## 6. `rm -r` — delete a folder

The `-r` flag means *recursive* — remove the folder and everything inside it.

```bash
rm -r new_folder
ls -l
```

## 7. `wget` — download a file from a link

`wget` retrieves a file from a public URL. In the original NICHD lesson the
target was a Cavatica workspace path with a Zenodo file; that same file works
anywhere:

```bash
wget -q https://zenodo.org/record/4302133/files/deseq2_5k.csv
ls -l deseq2_5k.csv
```

The file contains DESeq2 results from an RNA-seq experiment
(*p*-values < 0.05, fold difference > 1.5). It reappears in the
[interactive-computing](../interactive-computing/README.md) lesson as the
input for a volcano-plot exercise.

## Where to next

You now have `ls`, `pwd`, `cp`, `rm`, `mkdir`, `rm -r`, and `wget` — the seven
commands you need to navigate a working directory, create and destroy files,
and pull data from the web.

→ Continue with the [command-line-and-git-bash lesson](README.md) proper
for the git-focused ten-command tour.

→ Then on to [version-control](../version-control/README.md).
