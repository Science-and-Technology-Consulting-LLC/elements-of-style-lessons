# Containers


> *In the book: Chapter 8 — Containers.*

:::{admonition} What you'll learn
:class: tip

- Read a `Dockerfile` line by line and understand each piece.
- Build a single-purpose container locally and tag a real version.
- Recognise when a container is *too much job* — and split it.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

A container is a sealed box with everything your code needs to run: the
OS-level libraries, the language runtime, your specific package
versions, your script. Hand the container to a collaborator (or to a
cluster, or to an AI agent), and the work runs the same way it did on
your laptop.

:::{admonition} The rule
:class: tip

**One container, one job.** A container that does QC *and* differential
expression *and* plotting is a container that's hard to test, hard to
reason about, and hard to slot into a workflow. A container that does
QC *is one of the LEGO bricks you'll snap together with Nextflow.*
:::

## What this lesson teaches

By the end you'll be able to:

1. Read a `Dockerfile` line by line and explain what each line is doing
   *and why*.
2. Write a single-purpose `Dockerfile` for a Python or R analysis step.
3. Build it locally, run a smoke test, and tag it.
4. Push it to a container registry (GHCR or Docker Hub).
5. Recognise when a container is *too much job* — and split it.

## The two worked examples in the book companion

Two real, single-purpose containers live in the book companion repo.
Before you read the rest of this page, open both `Dockerfile`s in two
tabs and notice they're both well under 50 lines:

- **[`containers/scanpy-qc/`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/containers/scanpy-qc)** —
  Python 3.11 base, one job: scRNA-seq QC + h5ad conversion.
- **[`containers/limma-voom/`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/containers/limma-voom)** —
  R base, one job: pseudobulk differential expression.

Each one does exactly one thing. That isn't an accident — that's the
rule applied.

## The anatomy of a single-purpose Dockerfile

Here's the scanpy-qc Dockerfile broken into the four things every
single-purpose Dockerfile does. Yours will follow the same shape.

```dockerfile
# 1. Pick a small, well-known base.
FROM python:3.11-slim

# 2. Pin every version. "I think I had 1.9 something" is the enemy.
RUN pip install --no-cache-dir \
      scanpy==1.9.8 \
      anndata==0.10.7 \
      pandas==2.1.4 \
      numpy==1.26.4

# 3. Copy in exactly one entry-point script.
COPY scanpy_qc.py /opt/scanpy_qc.py
RUN chmod +x /opt/scanpy_qc.py

# 4. Set a sensible default that explains itself when run with no args.
ENTRYPOINT ["python", "/opt/scanpy_qc.py"]
```

That's it. Four sections, four reasons:

1. **Base image.** Pick `*-slim` Python or a Bioconductor image for R.
   Avoid `latest` — pin the major version.
2. **Pinned installs.** Every version pinned, `--no-cache-dir` so the
   image stays small. If a package floats, your container is no longer
   reproducible.
3. **One entry-point script.** *One.* If you find yourself wanting two,
   you have two containers.
4. **`ENTRYPOINT`.** When someone runs your image with no arguments,
   they get the actual tool — with `--help` if you wrote it that way
   (see [Reusable CLIs](reusable-clis.md)).

## Install Docker

::::{tab-set}

:::{tab-item} macOS
:sync: mac

```bash
# Docker Desktop for Mac: https://docs.docker.com/desktop/install/mac-install/
# After install, run it once so the engine starts.
docker --version
```
:::

:::{tab-item} Windows
:sync: win

```bash
# Docker Desktop for Windows: https://docs.docker.com/desktop/install/windows-install/
# Enable WSL2 backend when prompted. Restart, then:
docker --version
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# Docker (or Singularity) is pre-installed on Lifebit compute nodes.
# You'd usually let Nextflow handle container pulls; for ad-hoc runs:
docker --version
```
:::

::::

## A first build

In Git Bash or your terminal, with Docker Desktop running:

```bash
# Move into the directory that has the Dockerfile.
cd /path/to/containers/scanpy-qc

# Build. Tag with the version, not just `latest`.
docker build -t scanpy-qc:1.0.0 .

# Smoke test: just run it. With no arguments you should see --help.
docker run --rm scanpy-qc:1.0.0 --help

# Real run: mount your data, pass real arguments.
docker run --rm \
    -v "$(pwd)/data:/data" \
    scanpy-qc:1.0.0 \
    --input /data/raw.h5ad \
    --output /data/qc.h5ad
```

Two habits to form right now:

- **Always tag.** Never push `:latest` without also pushing `:1.0.0` (or
  whatever your version is). Six months from now you will need the
  exact image that produced a specific result.
- **Mount data, don't `COPY` it.** Data lives outside the image. The
  image only knows how to *process* data; it doesn't *carry* data.

## Pushing to a registry

You publish a container so other people (and other clusters, and AI
agents) can pull it. The most natural place for NIH-NLM work is
**GitHub Container Registry (GHCR)** because it lives next to the repo
that built the image.

```bash
# Log in once (uses your GitHub Personal Access Token with `write:packages`).
echo "$GHCR_TOKEN" | docker login ghcr.io -u "$GHCR_USER" --password-stdin

# Tag for GHCR.
docker tag scanpy-qc:1.0.0 ghcr.io/adeslatt/scanpy-qc:1.0.0

# Push.
docker push ghcr.io/adeslatt/scanpy-qc:1.0.0
```

The book companion's
[`.github/workflows/docker-publish.yml`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/.github/workflows)
pattern automates this: every push to `main` builds the image, tags it
with both `:latest` and `:<git-sha>`, and pushes both to GHCR. Steal
that pattern.

## The smell test for "too much job"

You have too much in one container if any of these are true:

- The Dockerfile is over ~50 lines.
- The image installs both Python *and* R *and* Bioconductor.
- The entry-point script has more than one subcommand that takes more
  than half a page of arguments.
- You catch yourself adding `if mode == 'qc'` versus `if mode == 'de'`
  branches in the entry script.

If any of those are true, split. The Nextflow workflow you'll build in
the next lesson will be much happier with two single-purpose
containers than with one omnibus container.

## Containers on Apple Silicon vs. x86_64

If you build on an M-series Mac and your collaborator runs on AWS x86,
you need to either:

- Build a multi-arch image: `docker buildx build --platform
  linux/amd64,linux/arm64 ...`, or
- Force the platform on the run side: `docker run --platform
  linux/amd64 ...` (slower, but works).

The book companion's containers are built multi-arch precisely for this
reason — `nsforest` and `scanpy-qc` both run on Apple-Silicon laptops
*and* on AWS instances.

## What you'll have at the end

A single-purpose `Dockerfile`, a built image tagged with a real version,
a pushed image at a registry your collaborator can pull from, and a
smoke-test command you can paste into any README. Once you have that,
[Nextflow](nextflow-workflows.md) becomes trivial — it's just wiring boxes
together.

## Further reading

- [Docker documentation](https://docs.docker.com/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) — every instruction
- [Open Container Initiative](https://opencontainers.org/) — the spec containers implement
- [BioContainers](https://biocontainers.pro/) — pre-built bioinformatics container catalog
- [hadolint](https://github.com/hadolint/hadolint) — Dockerfile linter
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)


## Where to next

→ [Nextflow modules](nextflow-modules.md) — wrap each CLI verb as a `.nf` module.
