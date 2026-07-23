# Pre-training

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/pre-training/pre-training/)) — woven into
the [introduction](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`pre-training.ipynb`](pre-training.ipynb) — every code cell
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
| 11:30–11:50 | Register the essential accounts (see below) |
| 11:50–12:00 | Wrap-up and preview of the five course days |

## Accounts to register for

The elements-of-style lessons run on your **laptop**, in
**[Google Cloud Shell](https://shell.cloud.google.com/)** (a free
browser-based terminal that needs only a Google account), or on
**[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs
to scale. Register the accounts below in that order — the first three
are essential; the rest are conditional.

### Essential — for every reader

- **GitHub** — code hosting and version control.
  Sign up: <https://github.com/signup>. Sign in: <https://github.com/login>.
  Followed up in [version-control/why-git-and-setup.md](../version-control/why-git-and-setup.md).
- **ORCID** — a persistent researcher identifier. Every account below can
  be linked to your ORCID.
  Sign up: <https://orcid.org/register>. Sign in: <https://orcid.org/signin>.
- **Zenodo** — DOI-assignable data + notebook archive. Free.
  Sign in via ORCID (recommended) or GitHub at
  <https://zenodo.org/login/>.

### If you'll run anything in a browser terminal or federated

- **Google Cloud Shell** — a free browser terminal that ships with `git`,
  `conda`, `docker`, and enough compute for the early lessons.
  Sign in with any Google account at <https://shell.cloud.google.com/>.
- **Lifebit CloudOS** — federated computing platform (headline platform in
  [platforms/README.md](../platforms/README.md)).
  Sign up: <https://cloudos.lifebit.ai/register>. Institutional-access
  requests: <https://lifebit.ai/contact>. Sign in:
  <https://cloudos.lifebit.ai/login>.

### If you're doing NICHD Kids First / INCLUDE work

The elements-of-style examples themselves don't use CAVATICA — the
Kids First / INCLUDE course does. Register these three only if you'll
work in that ecosystem:

- **Kids First DRC** — pediatric-data Data Resource Center.
  Sign up: <https://portal.kidsfirstdrc.org/> → *Create your account* →
  connect via **NIH Researcher Authentication Service (RAS)**.
- **INCLUDE Data Hub** — Down-syndrome-cohort Data Hub.
  Sign up: <https://portal.includedcc.org/> → *Sign Up* → connect via
  **ORCID** (recommended) or Google.
- **CAVATICA** — the compute platform Kids First / INCLUDE runs on.
  Sign up + sign in: <https://cavatica.sbgenomics.com/> → *Create an
  account* or *Log in with eRA Commons*. Full walkthroughs live in
  [platforms/creating-a-cavatica-account.md](../platforms/creating-a-cavatica-account.md)
  and its siblings under the `platforms` lesson.


## Cloud credits and office hours

Kids First and INCLUDE each run a cloud-credit application process (small
compute budgets for training and early exploration). Monthly user-support
office hours run jointly with Velsera; the current schedule is linked from
the NICHD site.

## What comes next

→ [`lets-dive-in.md`](lets-dive-in.md) — Day-1 opener: get a terminal
open on your laptop, in Google Cloud Shell, or on Lifebit.

→ Kids First / INCLUDE readers only:
[`pre-training-creating-kids-first-and-other-accounts.md`](../platforms/pre-training-creating-kids-first-and-other-accounts.md)
— the CAVATICA-flavoured account-creation click-by-click (in the
`platforms` lesson).
