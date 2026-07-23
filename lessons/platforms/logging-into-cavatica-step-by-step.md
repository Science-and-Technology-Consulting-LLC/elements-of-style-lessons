# Logging into CAVATICA — step by step

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-1-reasoning/logging-into-cavatica-step-by-step/)) — woven into
the [platforms](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`logging-into-cavatica-step-by-step.ipynb`](../ipynb/logging-into-cavatica-step-by-step.ipynb) — every code cell
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


## Step 1 — Navigate to CAVATICA

Open [https://cavatica.sbgenomics.com/home](https://cavatica.sbgenomics.com/home)
in a browser. **Chrome** is the tested browser for the training.

The initial login window offers eRA Commons, Google, and email-based
sign-in. **eRA Commons is the recommended path** — it links your CAVATICA
account to the NIH identity that knows which controlled-access datasets you
are authorised to view. Reference:
[CAVATICA account docs](https://docs.cavatica.org/).

## Step 2 — Authorise CAVATICA

You land on the **Gen3 login window** — the mechanism NIH uses to authorise
tools to fetch controlled-access data on your behalf. Click
**"Yes, I authorise"**. This is the moment dbGaP + eRA Commons authorisation
becomes visible to CAVATICA.

## Step 3 — The dashboard

What you see next depends on your history. New users get an empty dashboard
with a "Create a Project" prompt. Returning users see their existing
projects on the left and past analyses on the right.

## Step 4 — Create a project + start JupyterLab

From the dashboard, follow the two-step flow that
[`starting-a-jupyter-lab-notebook.md`](../interactive-computing/starting-a-jupyter-lab-notebook.md)
walks through in detail:

1. **Create a project** — name it, pick a billing group, **enable network
   access**.
2. **Data Studio → New Analysis → JupyterLab → Start**.

## Where to next

→ [`authenticating-on-cavatica.md`](authenticating-on-cavatica.md) — the
developer-token dance for `docker login` and Python client access.

→ [`working-with-apps-on-cavatica.md`](working-with-apps-on-cavatica.md) —
running the ~703 public workflows CAVATICA hosts.
