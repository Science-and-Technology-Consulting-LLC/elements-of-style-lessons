# Preamble — publishing your containers before you build the workflow

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-4-workflow-development/preamble/)) — woven into
the [nextflow-modules](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`preamble.ipynb`](../ipynb/preamble.ipynb) — every code cell
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


## Three registries you might publish to

| Registry | When to use it | Auth |
|---|---|---|
| **GitHub Container Registry (GHCR)** | Default for open work. Free, unlimited public images, natural home next to the repo. | PAT with `write:packages` |
| **CAVATICA image registry** (`pgc-images.sbgenomics.com`) | You're publishing an image *to be run inside CAVATICA workflows*. This is the NICHD path. | CAVATICA developer token |
| **Docker Hub** | Legacy default; free tier now rate-limits pulls. | Docker Hub PAT |

The NICHD walkthrough uses **CAVATICA**. The
[containers lesson](../containers/README.md) uses **GHCR**. Both work.
Pick one per repo, be consistent.

## Prerequisites

- Two built images from
  [building-dockerfiles.ipynb](../../containers/ipynb/building-dockerfiles.ipynb):
  `fastqc` and `multiqc`.
- A CAVATICA account and a personal image registry space at
  `pgc-images.sbgenomics.com/<your-userid>/`.
- A CAVATICA authentication token (Dashboard → Developer → Auth Token).

## Build the images (recap)

```bash
cd fastqc-docker && docker build -t fastqc .
cd ../multiqc-docker && docker build -t multiqc .
```

## Tag for CAVATICA

Each image gets a *fully qualified* tag: `<registry>/<user>/<image>:<version>`.
List images to grab the local image IDs:

```bash
docker images
```

Then tag each — replace `<userid>` with your CAVATICA username, and
`<image-id>` with the short hash `docker images` printed:

```bash
docker tag <image-id-fastqc> pgc-images.sbgenomics.com/<userid>/fastqc:v0.11.9
docker tag <image-id-multiqc> pgc-images.sbgenomics.com/<userid>/multiqc:v1.0dev0
```

## Authenticate to the CAVATICA registry

```bash
docker login pgc-images.sbgenomics.com -u <username> -p <cavatica-token>
```

## Push

```bash
docker push pgc-images.sbgenomics.com/<userid>/fastqc:v0.11.9
docker push pgc-images.sbgenomics.com/<userid>/multiqc:v1.0dev0
```

On success the registry URL becomes the *portable address* your
Nextflow module (and any CWL workflow) will reference in its `container`
directive.

## The Elements-of-Style equivalent — GHCR

For the LLC lessons repo, the same three-step loop points at **GHCR**
instead:

```bash
docker tag fastqc  ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9
docker tag multiqc ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0

echo "$GHCR_TOKEN" | docker login ghcr.io -u "$GHCR_USER" --password-stdin

docker push ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9
docker push ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0
```

The pattern doesn't change — only the hostname.

## Where to next

→ Back to the [nextflow-modules lesson](README.md) — wrap each of the two
published images in a `.nf` module.

→ Then [`building-a-nextflow-workflow.ipynb`](../../nextflow-workflows/ipynb/building-a-nextflow-workflow.ipynb) —
compose the modules into a runnable pipeline.
