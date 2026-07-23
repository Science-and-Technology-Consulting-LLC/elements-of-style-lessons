# Pre-training

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/pre-training/pre-training/)) — woven into
the [introduction](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`pre-training.ipynb`](../ipynb/pre-training.ipynb) — every code cell
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


## What pre-training is for

Before the five-day core walks start, spend an hour on the *account
plumbing*. Registrations take time to propagate; if the accounts are ready
by the time you begin Chapter 3, no time is lost on Day 1.

## The one-hour pre-training agenda

| Time | What |
|---|---|
| 11:00–11:10 | Welcome — motivation and rationale |
| 11:10–11:30 | Registration procedures |
| 11:30–11:50 | Kids First, INCLUDE, and CAVATICA registrations |
| 11:50–12:00 | Wrap-up and preview of the five course days |

## Accounts to register for

- **[GitHub](https://github.com/)** — code hosting and version control.
- **[Zenodo](https://zenodo.org/)** — DOI-assignable data + notebook
  archive. Free.
- **[ORCID](https://orcid.org/)** — a persistent researcher identifier.
  Every account below can be linked to your ORCID.
- **[Kids First DRC](https://kidsfirstdrc.org/)** — pediatric-data
  Data Resource Center.
- **[INCLUDE Data Hub](https://portal.includedcc.org/)** — Down-syndrome-cohort
  Data Hub.
- **[CAVATICA](https://cavatica.sbgenomics.com/)** — the compute platform
  the Kids First / INCLUDE walkthrough uses.

## Cloud credits and office hours

Kids First and INCLUDE each run a cloud-credit application process (small
compute budgets for training and early exploration). Monthly user-support
office hours run jointly with Velsera; the current schedule is linked from
the NICHD site.

## What comes next

→ [`lets-dive-in.md`](lets-dive-in.md) — Day-1 opener: create a CAVATICA
account and log in.

→ [`pre-training-creating-kids-first-and-other-accounts.md`](../platforms/pre-training-creating-kids-first-and-other-accounts.md) —
the account-creation click-by-click (in the `platforms` lesson).
