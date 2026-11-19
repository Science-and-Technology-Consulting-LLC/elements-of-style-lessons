# GitHub Actions for maintenance testing

We will read real GitHub Actions workflows that keep a research pipeline working over time. A pipeline that quietly stopped running two months ago is a paper you cannot reproduce.

*Part of the [continuous-integration](README.md) lesson. Please do [add a first CI job](add-a-first-ci-job.md) first if you have never written a workflow.*

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Containers](../containers/README.md), is done, and so is [add a first CI job](add-a-first-ci-job.md).
- To read the workflows you need nothing more. To use them on your own pipeline you need a [GitHub account](https://github.com/signup) and a repository.
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.

The pipelines in these workflows are written in [Nextflow](https://www.nextflow.io/), which we meet in [Introduction to Nextflow](../nextflow-workflows/README.md), a later lesson. Here we only read them, so you do not need to know Nextflow yet. To adapt the examples, you will later need a Nextflow pipeline with a small test dataset.

### What you will do

- Learn what *maintenance testing* is: re-running a small test of your pipeline on every change.
- Read a real test workflow from a published pipeline.
- Read a longer test workflow that you can adapt.
- Read the workflow that builds and publishes container images automatically.

## Steps to execute

### Understand why a research repository needs CI

Why: software drifts. Packages update, containers are rebuilt and workflow runners change. Automating the question "does this still run?" is how a [Nextflow](https://www.nextflow.io/) pipeline survives six months of that drift.

[GitHub Actions](https://docs.github.com/en/actions) runs your test data on every push, every pull request and every release. It is free for public repositories, runs on GitHub's own computers (*runners*), and gives each job about 8 GB of memory and a small disk. That is enough for a smoke test, not for a full analysis.

The pattern has four parts:

1. Keep a **tiny test dataset** in `data/test/`. Under 20 MB is plenty.
2. Add a **test profile** in your `nextflow.config` that points at that data. A *profile* is a named set of settings.
3. Write **one workflow file** at `.github/workflows/test.yml` that runs `nextflow run . -profile test` on every push and pull request.
4. If it goes red, you know within minutes. Without CI you find out when a reviewer tries to rerun your paper.

**What you should see:** nothing to run here. We now have the pattern. The next steps show it in real files.

### Read a real test workflow

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

### Read a version you can adapt

Why: this is a slightly newer form of the same idea. It runs the small test pipelines (`main-hello-py-greet.nf`, `main-hello-r-greet.nf` and `main-bulk-de.nf`) that sit in the top folder of this repository. This repository does not have a `ci.yml` of its own. Save the file as `.github/workflows/ci.yml` in your own repository to use it.

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

Two small differences from the example in *Read a real test workflow*: `actions/checkout@v4` (a newer version) and Nextflow installed with `curl` instead of `wget`. Both work.

**What you should see:** three steps in the job. First it gets your code, then it installs Nextflow, then it runs the pipelines with `-profile test`.

> **Picture to add:** the Actions tab of this repository showing a passing CI run (save as assets/github-actions-for-maintenance-testing-step-3.png)

### Read the image publish workflow

Why: GitHub Actions can also build and publish container images. This workflow uses Docker's actions. [Publish an image with Actions](publish-an-image-with-actions.md) does the same job with Podman. Every push to `main` builds each image in `container/<name>/`, tags it with `:latest` and with the Git commit ID, and uploads it to GHCR (GitHub's container registry).

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

### Recap

- **CI catches drift before you feel it.**
- **Testing is `nextflow run ... -profile test` in a fresh virtual machine.** GitHub provides the machine.
- **Image publish is the same idea.** Push to `main` and the image appears at GHCR. Later workflows pull it.

### If something goes wrong

- **The workflow never runs.** The `on:` section did not match what you did. A push to a branch not listed under `branches:` does nothing. Check the branch name.
- **A workflow fails with a YAML error.** YAML cares about spaces. Use spaces, never tabs, and keep each level indented the same amount as in the examples.
- **Image publish fails with `denied` or `permission`.** The job needs `packages: write` under `permissions:` (as in *Read the image publish workflow*), and the repository must allow Actions to write packages. See [GitHub's container registry docs](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

## Next

[Documentation](../documentation/README.md): build a Sphinx site and publish it with GitHub Actions. Or return to the [continuous-integration lesson](README.md).
