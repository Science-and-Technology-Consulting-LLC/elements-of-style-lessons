# Preamble — publishing your containers before you build the workflow

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-4-workflow-development/preamble/)) — woven into
the [nextflow-modules](index.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`preamble.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-modules/preamble.ipynb) — every code cell
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


## Two registries you might publish to

| Registry | When to use it | Auth |
|---|---|---|
| **GitHub Container Registry (GHCR)** | Default for open work. Free, unlimited public images, natural home next to the repo. | PAT with `write:packages` |
| **Docker Hub** | Legacy default; free tier now rate-limits pulls. | Docker Hub PAT |

The [containers lesson](../containers/index.md) uses **GHCR**.
Pick one per repo, be consistent.

## Prerequisites

- Two built images from
  [building-dockerfiles.ipynb](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/containers/building-dockerfiles.ipynb):
  `fastqc` and `multiqc`.
- A GitHub personal access token with `write:packages`.

## Build the images (recap)

```bash
cd fastqc-docker && docker build -t fastqc .
cd ../multiqc-docker && docker build -t multiqc .
```

## Tag, log in and push to GHCR

Each image gets a *fully qualified* tag: `<registry>/<user>/<image>:<version>`.

```bash
docker tag fastqc  ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9
docker tag multiqc ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0

echo "$GHCR_TOKEN" | docker login ghcr.io -u "$GHCR_USER" --password-stdin

docker push ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9
docker push ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0
```

On success the registry URL becomes the *portable address* your
Nextflow module (and any CWL workflow) will reference in its `container`
directive.

## Where to next

→ Back to the [nextflow-modules lesson](index.md) — wrap each of the two
published images in a `.nf` module.

→ Then [`building-a-nextflow-workflow.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/building-a-nextflow-workflow.ipynb) —
compose the modules into a runnable pipeline.
