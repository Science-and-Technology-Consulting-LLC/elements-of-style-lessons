# Building Dockerfiles — fastqc and multiqc

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-3-containerization/building-dockerfiles/)) — woven into
the [containers](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`building-dockerfiles.ipynb`](building-dockerfiles.ipynb) — every code cell
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


## Prerequisites

You've completed [conda-environments](../conda-environments/README.md) — you
know how to make a clean environment and install packages into it. This
walkthrough builds on that: instead of installing tools *into your machine*,
we install them *into a Docker image* — a portable, reproducible bundle you
can hand to a colleague, a workflow engine, or a cloud platform and know it
will behave the same everywhere.

We're going to build **two** small container images — `fastqc` and `multiqc`
— that will reappear in the
[`case-studies/multiqc-workflow/`](../../case-studies/multiqc-workflow/README.md)
worked example.

## What a Docker image and a Dockerfile are

A **Dockerfile** is a plain-text file listing the commands Docker needs to
assemble an image: what base OS to start from, what packages to install, what
files to copy in.

A **Docker image** is the finished, portable bundle produced by running
`docker build` against that Dockerfile.

> **Warning.** `docker build` copies *every file in the build directory* to
> the Docker daemon. If the directory is huge, so is the build. Keep the
> build directory small — only what the image actually needs. Use
> `.dockerignore` to exclude things explicitly.

## Setup

Activate your conda environment (from
[`creating-a-conda-environment.ipynb`](../../conda-environments/ipynb/creating-a-conda-environment.ipynb)):

```bash
conda activate eos
```

## Part 1 — the `fastqc` image

### Create a clean build directory

```bash
mkdir fastqc-docker
cd fastqc-docker
touch Dockerfile
```

Docker looks for a file named *exactly* `Dockerfile`. Open it in
your editor (VS Code, JupyterLab's editor, `nano`, `vim` — whichever) and
paste:

```dockerfile
# Base image: continuumio/miniconda3 comes with conda pre-installed.
FROM continuumio/miniconda3
LABEL description="Base docker image with conda + fastqc"
ARG ENV_NAME="fastqc"

# Install the conda environment declared in environment.yml
COPY environment.yml /
RUN conda env create --quiet --name ${ENV_NAME} --file /environment.yml && conda clean -a

# Add the env's bin/ to PATH so the image's default shell finds fastqc
ENV PATH /opt/conda/envs/${ENV_NAME}/bin:$PATH
```

Docker understands the directives `FROM`, `LABEL`, `ARG`, `COPY`, `RUN`, and
`ENV`. Lines starting with `#` are comments. We start `FROM continuumio/miniconda3`
so we don't have to install conda ourselves — it's already in the base image.

### Create the `environment.yml`

The Dockerfile refers to a file called `environment.yml`. Create it:

```bash
touch environment.yml
```

Paste this into `environment.yml`:

```yaml
name: fastqc
channels:
  - bioconda
  - defaults
dependencies:
  - fastqc
```

The `bioconda` channel is where community-vetted bioinformatics packages
live. `fastqc` is the read-QC tool this image will provide.

### Build the image

```bash
docker build -t fastqc .
```

The `-t fastqc` tags the built image with the name `fastqc`. The
`.` says *build in this directory* — Docker reads the `Dockerfile` here.

Confirm the image exists:

```bash
docker images
```

### Test the image

Set a variable so we can mount the current directory into the container:

```bash
PWD=$(pwd)
```

Now run `fastqc -h` **inside** the containerised environment:

```bash
docker run -it -v $PWD:$PWD -w $PWD fastqc fastqc -h
```

Breakdown:

- `-it` — interactive with a TTY (so stdout is not buffered).
- `-v $PWD:$PWD` — mount the host's current directory into the container
  under the same path.
- `-w $PWD` — set the container's working directory to that same path.
- `fastqc` (first) — the image name.
- `fastqc -h` (last) — the command to run inside the container.

If you saw the fastqc help text scroll past, congratulations: you have a
portable fastqc that will now run identically on your laptop, on Lifebit, on
CAVATICA, and inside any Nextflow module that names this container.

### Push the source to GitHub

Best practice — never let a `Dockerfile` live only on one machine. Add a
`README.md`, initialise the repo, commit, and publish via `gh`:

```bash
touch README.md
# open README.md in an editor and paste:
#
#   # fastqc-docker
#   Build a container for fastqc from bioconda.
#   docker build -t fastqc .
#   docker run -it -v $PWD:$PWD -w $PWD fastqc fastqc -h
```

```bash
gh auth login   # if you haven't yet — see github-authenticate.ipynb
```

```bash
git config --global user.email 'you@example.com'
git config --global user.name  'your-github-username'
```

```bash
git init -b main
git add . && git commit -m 'initial commit'
```

```bash
gh repo create   # answer: Push an existing local repository → path '.' → name fastqc-docker → Public → origin → Yes push
```

On success `gh` prints:

```
✓ Created repository <your-user>/fastqc-docker on GitHub
✓ Added remote https://github.com/<your-user>/fastqc-docker.git
✓ Pushed commits to https://github.com/<your-user>/fastqc-docker.git
```

The upstream reference version of this repo lives at
[`adeslatt/fastqc-docker`](https://github.com/adeslatt/fastqc-docker).

## Part 2 — the `multiqc` image

MultiQC aggregates the per-sample HTML reports fastqc emits into one summary.
Its Dockerfile is nearly identical.

Optionally, clone the reference version to compare with yours:

```bash
cd ~
git clone https://github.com/adeslatt/multiqc-docker.git
```

Otherwise, build your own from scratch:

```bash
mkdir multiqc-docker && cd multiqc-docker
touch Dockerfile
```

Paste into `Dockerfile`:

```dockerfile
FROM continuumio/miniconda3
LABEL description="Base docker image with conda + multiqc"
ARG ENV_NAME="multiqc"

COPY environment.yml /
RUN conda env create --quiet --name ${ENV_NAME} --file /environment.yml && conda clean -a

ENV PATH /opt/conda/envs/${ENV_NAME}/bin:$PATH
```

And `environment.yml`:

```yaml
name: multiqc
channels:
  - bioconda
  - defaults
dependencies:
  - multiqc
```

Build and test:

```bash
touch environment.yml   # then paste the YAML above into it
docker build -t multiqc .
docker images
```

```bash
PWD=$(pwd)
docker run -it -v $PWD:$PWD -w $PWD multiqc multiqc -h
```

Publish it exactly as you did for `fastqc-docker`:

```bash
touch README.md   # add a short description + build/run commands
git init -b main
git add . && git commit -m 'initial commit'
gh repo create   # answer: Push existing → . → multiqc-docker → Public
```

The upstream reference version of this repo lives at
[`adeslatt/multiqc-docker`](https://github.com/adeslatt/multiqc-docker) and
becomes the containerised step in the
[`multiqc-workflow`](https://github.com/Science-and-Technology-Consulting-LLC/multiqc-workflow)
case study.

## Recap

You now have two portable containers:

- **`fastqc`** — per-sample sequencing QC.
- **`multiqc`** — aggregates fastqc's per-sample reports into one HTML.

Both:

- Build from the same base image (`continuumio/miniconda3`).
- Install their tool via `environment.yml` (the *same* environment.yml you'd
  use on your laptop — the pattern is portable).
- Live in their own GitHub repo (`fastqc-docker`, `multiqc-docker`).
- Ship a working CLI verb (`fastqc`, `multiqc`) that a
  [Nextflow module](../nextflow-modules/README.md) can call directly.

The [multiqc-workflow case study](../../case-studies/multiqc-workflow/README.md)
composes them into a two-step pipeline: **fastqc → multiqc**.

## Where to next

→ Back to the [containers lesson](README.md) for the theoretical framing
(one container, one job, one CLI).

→ Then [nextflow-modules](../nextflow-modules/README.md) — wrap each of
these containers in a `.nf` module.
