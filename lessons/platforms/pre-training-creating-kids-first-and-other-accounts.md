# Pre-training — Kids First, INCLUDE, and other accounts

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/pre-training/pre-training-creating-kids-first-and-other-accounts/)) — woven into
the [platforms](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`pre-training-creating-kids-first-and-other-accounts.ipynb`](pre-training-creating-kids-first-and-other-accounts.ipynb) — every code cell
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


## What this session sets up

Before the five-day course starts, three data-hub accounts are worth
having in place. Each takes minutes to register, and each links to the
same NIH identity so authorisation flows through.

## Kids First DRC

1. Navigate to [https://kidsfirstdrc.org/](https://kidsfirstdrc.org/).
2. Click **Create your account**.
3. Choose a *connection service* — pick **NIH Researcher Authentication
   Service (RAS)**. This is the service that knows which controlled-access
   datasets you are authorised for.
4. Enter basic profile information.
5. Agree to the **NIH Genomic Data User Code of Conduct**.
6. You land on the Kids First Portal Dashboard.

## INCLUDE Data Hub

1. Navigate to [https://portal.includedcc.org/](https://portal.includedcc.org/).
2. Click **Sign Up**.
3. Authenticate with **Google** or **ORCID**. (ORCID is the recommended
   path — it doubles as your authoritative researcher identifier.)
   *eRA Commons login for INCLUDE is on the roadmap.*

## CAVATICA

Register per [`creating-a-cavatica-account.md`](creating-a-cavatica-account.md).
Both Kids First and INCLUDE let you connect a CAVATICA project as your
compute workspace once your CAVATICA account exists.

## GA4GH — the framework behind the rules

Pediatric data and human data are **sensitive data**. The **Global Alliance
for Genomics & Health ([GA4GH](https://www.ga4gh.org/))** is the policy-framing
and technical-standards organisation whose mission is *responsible genomic
data sharing within a human-rights framework.* The three accounts above are
implementations of pieces of that framework.

## Where to next

→ [`creating-a-cavatica-account.md`](creating-a-cavatica-account.md).

→ [`logging-into-cavatica-step-by-step.md`](logging-into-cavatica-step-by-step.md).

→ Back to the [platforms lesson](README.md).
