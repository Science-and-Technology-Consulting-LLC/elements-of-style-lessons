# Working with apps on CAVATICA

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-5-workflow-execution/WorkingWithAppsOnCAVATICA/)) — woven into
the [platforms](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`working-with-apps-on-cavatica.ipynb`](working-with-apps-on-cavatica.ipynb) — every code cell
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


## Prerequisites

- A CAVATICA account
  ([`creating-a-cavatica-account.md`](creating-a-cavatica-account.md)).
- An authenticated session
  ([`authenticating-on-cavatica.md`](authenticating-on-cavatica.md)).
- A developer token for private apps.

## Public apps — ~703 of them and counting

CAVATICA hosts a large catalogue of **public apps** — CWL and Nextflow
workflows that anyone can browse and execute *without* copying them into
their own project workspace. Search from your project's **Apps** tab; e.g.,
type **"Fastqc Analysis"** and pick one of the public wrappers.

## File management

Data can be imported from a variety of sources, including
[Zenodo](https://zenodo.org/).

**Best practice.** Debug and test on small files; then execute against the
hundreds or thousands. Storage is a *paid line item* on CAVATICA — you pay
for the bytes you keep.

## A worked example — fastqc on Zenodo test data

1. Go to **Files → Add Files → FTP/HTTP**.
2. Paste the Zenodo URLs for the tiny test FASTQ pair:

   ```
   https://zenodo.org/record/7025773/files/test.20k_reads_1.fastq.gz
   https://zenodo.org/record/7025773/files/test.20k_reads_2.fastq.gz
   ```

3. In **Apps**, search for `fastqc`.
4. **Select app → Run** with the two imported files as input.
5. Watch the run panel as the compute instance initialises, runs, and
   finishes. Results land in the project's file store.

## Best practices highlighted in the NICHD walkthrough

- **Daily GitHub commits** of the scripts and configuration you use — the
  worked-example scripts belong in a repo, not only in CAVATICA's storage.
- **Reproducible workflow steps** — every step containerised, every
  container tagged.
- **Archive derivative datasets on Zenodo** (DOI-assignable) so results are
  citable in a manuscript.

## Where to next

→ Back to the [platforms lesson](README.md).

→ [continuous-integration](../continuous-integration/README.md) — automate
the maintenance-testing of these public and private apps.
