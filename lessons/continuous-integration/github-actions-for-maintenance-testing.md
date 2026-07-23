# GitHub Actions for maintenance testing

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-5-workflow-execution/GitHubActionsForMaintenanceTesting/)) — woven into
the [continuous-integration](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`github-actions-for-maintenance-testing.ipynb`](github-actions-for-maintenance-testing.ipynb) — every code cell
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


## Why CI belongs in a research repo

Automating the *"does this still run?"* check is how a Nextflow pipeline
survives the six-months-later drift of package updates, container
rebuilds, and CWL runner upgrades. GitHub Actions runs your test
dataset on every push, every pull request, and every release — for
free, on GitHub's own runners, with roughly 8 GB of memory and small
disk (enough for a smoke test, not a full analysis).

## The pattern in one paragraph

- Keep a **tiny test dataset** in `data/test/` (< 20 MB is plenty).
- Add a **test profile** in your `nextflow.config` that points at that
  data.
- Write **one workflow file** at `.github/workflows/test.yml` that runs
  `nextflow run . -profile test` on every push and PR.
- If it goes red, you know within minutes; if you don't run CI, you
  find out six months later when the paper reviewer tries to rerun it.

## A real, canonical `.github/workflows/test.yml`

This is the shape used by
[Sheynkman-Lab/Long-Read-Proteogenomics](https://github.com/Sheynkman-Lab/Long-Read-Proteogenomics)
and, with minor edits, by nearly every nf-core pipeline.

```yaml
name: Testing for Long Reads Proteogenomics with SQANTI
on:
  push:
    branches:
      - dev
  pull_request:
  release:
    types: [published]

jobs:
  test:
    name: Run workflow tests
    runs-on: ubuntu-latest
    env:
      NXF_VER: ${{ matrix.nxf_ver }}
      NXF_ANSI_LOG: false
    strategy:
      matrix:
        nxf_ver: ['20.01.0', '']    # a pinned version + latest
    steps:
      - name: Check out pipeline code
        uses: actions/checkout@v2

      - name: Install Nextflow
        run: |
          wget -qO- get.nextflow.io | bash
          sudo mv nextflow /usr/local/bin/

      - name: Run pipeline with test data
        run: |
          nextflow run ${GITHUB_WORKSPACE} \
            --config conf/test_with_sqanti.config
```

Read three things:

1. **`on:`** decides when this runs. Push to `dev`, every PR, every
   release. Adjust to taste (`branches: [main]` for repos with no `dev`
   branch).
2. **`strategy.matrix.nxf_ver`** runs the whole job in parallel across
   more than one Nextflow version — catches breakage that only shows
   up on the pinned version *or* only on the latest.
3. **`nextflow run … --config conf/test_with_sqanti.config`** is the
   *actual* command. The magic is that this is the same command you'd
   run on your laptop; CI just wraps it in a fresh Ubuntu VM.

## The elements-of-style version — `.github/workflows/ci.yml`

For the containers-and-modules pattern used across this repo, the same
idea in a slightly more modern form:

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Nextflow
        run: |
          curl -s https://get.nextflow.io | bash
          sudo mv nextflow /usr/local/bin/

      - name: Run smoke test (hello-py + hello-r)
        run: |
          nextflow run main-hello-py-greet.nf -profile test
          nextflow run main-hello-r-greet.nf  -profile test

      - name: Run stitched pipeline (bulk DE) with test data
        run: |
          nextflow run main-bulk-de.nf -profile test
```

Two `uses:` differences from the NICHD example: `actions/checkout@v4`
(newer) and Nextflow install via `curl` instead of `wget` (both work).

## Automatic deployment — the docker-publish pattern

GitHub Actions also serves as *a compiler for Docker images.* Every
push to `main` builds each `container/<name>/` image, tags it with
both `:latest` and `:<git-sha>`, and pushes to GHCR:

```yaml
name: docker-publish
on:
  push:
    branches: [main]
  release:
    types: [published]

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    strategy:
      matrix:
        image: [scanpy-qc, limma-voom, hello-py, hello-r]
    steps:
      - uses: actions/checkout@v4

      - name: Log in to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: container/${{ matrix.image }}
          push: true
          tags: |
            ghcr.io/science-and-technology-consulting-llc/${{ matrix.image }}:latest
            ghcr.io/science-and-technology-consulting-llc/${{ matrix.image }}:${{ github.sha }}
```

Every module that names `ghcr.io/…/scanpy-qc:latest` in its `container:`
directive picks up the freshest build automatically.

## Recap

- **CI catches drift before you feel it.** A pipeline that quietly
  stopped running two months ago is a paper you can't reproduce.
- **Testing is `nextflow run … -profile test` in a VM.** GitHub gives
  you the VM.
- **Docker publish is the same story.** Push to `main` → image at GHCR.
  Downstream workflows pull the fresh image on their next run.

## Where to next

→ Back to the [continuous-integration lesson](README.md) for the
full theory (green-badge culture, matrix testing, secrets management).

→ Then [documentation](../documentation/README.md) — every push
also rebuilds and republishes *this* Sphinx site.
