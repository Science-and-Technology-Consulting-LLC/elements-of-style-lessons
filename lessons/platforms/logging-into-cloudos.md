# Logging into CloudOS

*Source: the platforms lesson. Part of the [platforms](index.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`logging-into-cloudos.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/logging-into-cloudos.ipynb) — every code cell
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
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/index.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/index.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/index.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/index.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/index.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/index.md) |

Run them all at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s\n" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING\n" "$cmd"
  fi
done
```

## Step 1 — Open the login page

Open <https://cloudos.lifebit.ai/login> in a browser.

## Step 2 — Use institutional login

Choose *Sign in with institutional login* and pick your institution from
the list. If it is not listed, ask at <https://lifebit.ai/contact>.

## Step 3 — Create a workspace

Create a workspace and pick the *biomedical analysis* template.

## Step 4 — Open JupyterLab

Open the workspace's JupyterLab. Then continue with
[`starting-a-jupyter-lab-notebook.md`](../interactive-computing/starting-a-jupyter-lab-notebook.md).

## Where to next

→ [`authenticating-on-cloudos.md`](authenticating-on-cloudos.md) — an API key
and `cloudos configure`, so you can run jobs from a terminal.
