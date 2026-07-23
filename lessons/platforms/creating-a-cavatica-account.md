# Creating a CAVATICA account

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-1-reasoning/creating-a-cavatica-account/)) — woven into
the [platforms](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`creating-a-cavatica-account.ipynb`](creating-a-cavatica-account.ipynb) — every code cell
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


## Two paths in

Navigate to [https://cavatica.sbgenomics.com/](https://cavatica.sbgenomics.com/).
You'll see two account-creation options:

1. **Create an account** — direct sign-up with email and password.
2. **Log in with eRA Commons** — reuse your NIH eRA Commons credentials.
   This is the recommended path for anyone who already has an eRA Commons
   ID, because it also unlocks controlled-access datasets you're already
   authorised to see.

## Official docs

The Seven Bridges / CAVATICA account documentation lives at
[docs.cavatica.org](https://docs.cavatica.org/) and covers the fine-print
of billing groups, project quotas, and eRA-Commons linkage.

## What you need to have ready

- An institutional email (for eRA Commons pairing).
- An [ORCID](https://orcid.org/) (recommended, for authoritative attribution
  on any published work run from this account).
- A payment method or a cloud-credit-program invitation (Kids First /
  INCLUDE fund a small credit pool for training).

## Where to next

→ [`logging-into-cavatica-step-by-step.md`](logging-into-cavatica-step-by-step.md) —
the click-by-click login.

→ [`pre-training-creating-kids-first-and-other-accounts.md`](pre-training-creating-kids-first-and-other-accounts.md) —
Kids First + INCLUDE registrations, and connecting them to CAVATICA.
