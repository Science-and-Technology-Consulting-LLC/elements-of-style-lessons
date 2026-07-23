# Workspace set-up

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-2-code-versioning/workspace-setup/)) — woven into
the [version-control](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`workspace-setup.ipynb`](workspace-setup.ipynb) — every code cell
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


## Pick a workspace

Everything in this curriculum runs equally well in three places:

- **Your laptop terminal** — the cheapest, always available, best for the
  first several lessons.
- **A Lifebit notebook server** — a browser-based terminal + JupyterLab that
  ships with `git`, `conda`, `docker`, `nextflow` already installed.
- **A CAVATICA Data Studio session** — the same idea, hosted by Seven Bridges
  on the CAVATICA cloud platform. This is where NICHD's Kids First / INCLUDE
  training runs.

Chrome (or any modern browser) — open each cloud-platform link in a new tab.

## Data Studio on CAVATICA — the specific case

Navigate to [https://cavatica.sbgenomics.com](https://cavatica.sbgenomics.com)
and log in. The Dashboard lists your projects on the left, analyses on the
right.

### Key details you feel in your bill

- *You don't pay for analyses that are stopped.* Stop them when you're done.
- Storage is a separate line-item and is always on. Move raw data to a
  cheap public store (Zenodo for DOI-versioned artefacts, GitHub for code +
  notebooks + workflow files) and keep only working copies in the paid
  workspace.
- Interactive Data Studio sessions run on **dedicated** instances (~$0.34/hr
  at time of writing). Workflow steps run on **spot** instances (~1/8 of the
  cost) — they're ephemeral: loaded, used, deleted. Cost-efficient and, as a
  side effect, a good reproducibility discipline.

The [Kids First DRC Cloud Cost Overview](https://github.com/kids-first/kf-cloud-credits#readme)
walks through pricing in detail.

### Best practice

Develop and debug on small files. Once the code is right, run it across the
hundreds or thousands of files. This costs less *and* catches bugs earlier.

## Start your notebook

Click **Start** on your Data Studio session. The JupyterLab launcher opens.
It stays active for about 30 minutes of idle time before shutting down (which
is exactly what you want — no accidental all-night bills).

If this is your first session, follow the platform's onboarding for account
setup; support is available during the training's breaks.

## Where to next

→ [`github-authenticate.ipynb`](github-authenticate.ipynb) — sign in to GitHub
from the terminal so you can push code up.
