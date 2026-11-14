# GitHub Actions for maintenance testing

You will read three real GitHub Actions workflows that keep a research pipeline working over time. This matters because a pipeline that quietly stopped running two months ago is a paper you cannot reproduce.

*Part of the [continuous-integration](README.md) lesson. Do [add a first CI job](add-a-first-ci-job.md) first if you have never written a workflow.*

## What you will do

- Learn what *maintenance testing* is: re-running a small test of your pipeline on every change.
- Read a real test workflow from a published pipeline.
- Read the test workflow used in this repository.
- Read the workflow that builds and publishes Docker images automatically.

## What you need

- Nothing to install to read the workflows. To use them on your own pipeline you need a [GitHub account](https://github.com/signup) and a repository.
- A [Nextflow](https://www.nextflow.io/) pipeline with a small test dataset, if you want to adapt the examples. See [nextflow-workflows](../nextflow-workflows/README.md).
- Containers, for the last workflow. See [containers](../containers/README.md).
- [JupyterLab](https://jupyter.org/) with a Bash kernel. The "Check your setup" section below covers the kernel.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`github-actions-for-maintenance-testing.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/continuous-integration/github-actions-for-maintenance-testing.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do Steps 4 and 6 of [Let's dive in](../introduction/lets-dive-in.md) first.

## Step 1. Understand why a research repository needs CI

Why: *continuous integration* (CI) means a computer re-runs your checks on every change. Software drifts. Packages update, containers are rebuilt and workflow runners change. Automating the question "does this still run?" is how a [Nextflow](https://www.nextflow.io/) pipeline survives six months of that drift.

[GitHub Actions](https://docs.github.com/en/actions) runs your test data on every push, every pull request and every release. It is free for public repositories, runs on GitHub's own computers (*runners*), and gives each job about 8 GB of memory and a small disk. That is enough for a smoke test, not for a full analysis.

The pattern has four parts:

1. Keep a **tiny test dataset** in `data/test/`. Under 20 MB is plenty.
2. Add a **test profile** in your `nextflow.config` that points at that data. A *profile* is a named set of settings.
3. Write **one workflow file** at `.github/workflows/test.yml` that runs `nextflow run . -profile test` on every push and pull request.
4. If it goes red, you know within minutes. Without CI you find out when a reviewer tries to rerun your paper.

**What you should see:** nothing to run here. You now have the pattern. The next steps show it in real files.

## Step 2. Read a real test workflow

Why: this shape is used by [Sheynkman-Lab/Long-Read-Proteogenomics](https://github.com/Sheynkman-Lab/Long-Read-Proteogenomics) and, with small edits, by nearly every [nf-core](https://nf-co.re/) pipeline.

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

Read three things in it:

1. **`on:`** decides when the workflow runs. Here it is a push to `dev`, every pull request and every release. Change `dev` to `main` if your repository has no `dev` branch.
2. **`strategy.matrix.nxf_ver`** runs the whole job once for each Nextflow version listed. Here that is one pinned old version and the latest. It catches breakage that shows up only on one of them.
3. **`nextflow run ... --config conf/test_with_sqanti.config`** is the real command. It is the same command you would run on your laptop. CI wraps it in a fresh Ubuntu machine.

**What you should see:** you can point to the three lines above in the file. If you can, you can read any test workflow.

## Step 3. Read the version used in this repository

Why: this repository uses a slightly newer form of the same idea. Save it as `.github/workflows/ci.yml` in your own repository to use it.

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

Two small differences from the step 4 example: `actions/checkout@v4` (a newer version) and Nextflow installed with `curl` instead of `wget`. Both work.

**What you should see:** three steps in the job. First it gets your code, then it installs Nextflow, then it runs the pipelines with `-profile test`.

> **Picture to add:** the Actions tab of this repository showing a passing CI run (save as assets/github-actions-for-maintenance-testing-step-3.png)

## Step 4. Read the Docker publish workflow

Why: GitHub Actions can also build and publish Docker images. Every push to `main` builds each image in `container/<name>/`, tags it with `:latest` and with the Git commit ID, and uploads it to GHCR (GitHub's container registry).

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

Every module that names `ghcr.io/.../scanpy-qc:latest` in its `container:` line picks up the freshest build the next time it runs.

**What you should see:** one `matrix` list of four image names. The job runs once for each name, so one workflow builds four images.

## Step 5. Recap

- **CI catches drift before you feel it.**
- **Testing is `nextflow run ... -profile test` in a fresh virtual machine.** GitHub provides the machine.
- **Docker publish is the same idea.** Push to `main` and the image appears at GHCR. Later workflows pull it.

## If something goes wrong

- **The workflow never runs.** The `on:` section did not match what you did. A push to a branch not listed under `branches:` does nothing. Check the branch name.
- **A workflow fails with a YAML error.** YAML cares about spaces. Use spaces, never tabs, and keep each level indented the same amount as in the examples.
- **Docker publish fails with `denied` or `permission`.** The job needs `packages: write` under `permissions:` (as in step 6), and the repository must allow Actions to write packages. See [GitHub's container registry docs](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

## Next

[Documentation](../documentation/README.md): every push also rebuilds and republishes the Sphinx site. Or return to the [continuous-integration lesson](README.md).
