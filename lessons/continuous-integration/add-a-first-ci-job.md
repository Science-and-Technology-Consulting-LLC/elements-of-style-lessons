# Add a first CI job to an empty repo

*Companion walkthrough to the [continuous-integration](README.md)
lesson — a minimal "green badge" CI setup you can graduate from.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`add-a-first-ci-job.ipynb`](add-a-first-ci-job.ipynb) — every code cell
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


## The goal

Any push to `main` or open PR triggers a job that lints Python and
proves the code parses. Two minutes end-to-end. Zero cost.

## Setup — a repo you own

```bash
cd ~
mkdir hello-ci && cd hello-ci
git init -b main
echo "print('hello')" > hello.py
git add . && git commit -m "seed"
gh repo create hello-ci --public --source=. --push
```

(You'll need `gh` authenticated — see the
[github-authenticate walkthrough](../version-control/github-authenticate.md).)

## Write the workflow

Create `.github/workflows/ci.yml`:

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install ruff
      - run: ruff check .
```

Commit and push:

```bash
git add .github/workflows/ci.yml
git commit -m "add first CI job"
git push
```

## Watch the run

On the repo's GitHub page → **Actions** tab → click the latest run. The
job takes ~30 seconds. Green tick = passing.

## Break it deliberately

```bash
echo "import os,sys;print('bad style')" >> hello.py
git commit -am "on purpose"
git push
```

The next run goes red. Fix the file, push again, watch it turn green.
That's the feedback loop CI gives you — cheap, fast, honest.

## Where to next

→ Back to the [continuous-integration lesson](README.md) for the
richer patterns (matrix testing, container publish, docs deploy).
