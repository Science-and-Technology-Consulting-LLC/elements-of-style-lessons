# Containers

> *In the book: Sections 5.5 and 5.6, What Is a Podman Image and a Dockerfile; Building and Testing Dockerfiles.*

This lesson shows you how to put one analysis tool in a sealed container, build it, test it and tag it, so that it runs the same way on any computer.

## Start here

### Before you start

The previous lesson is [Building reusable command-line tools](../reusable-clis/README.md). Your container will run one of those tools. You also need [Podman](https://podman.io/docs/installation).

### Do this

1. **Clone the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook** `lessons/containers/building-dockerfiles.ipynb`. From the repository folder, start JupyterLab with `jupyter lab`, then open the file. You can also [view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/containers/building-dockerfiles.ipynb). Run each cell in order, top to bottom.

### What you should see

Two container images on your machine, `fastqc` and `multiqc`, each started with a command such as `podman run ... fastqc -h` that prints the tool's help. The R walkthrough adds a third, `hello-r`.

> **Picture to add:** the output of `podman images` listing the `fastqc` and `multiqc` images (save as assets/overview.png)

### Where the files are

- The lesson folder is [`lessons/containers`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/containers).
- The images you build live in Podman, not in the folder. The files you write (`Dockerfile`, `environment.yml`) are in new folders in your home folder: `fastqc-docker`, `multiqc-docker` and `hello-r-docker`.
- Two finished example containers are in the book companion repository: [`scanpy-qc`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/container/scanpy-qc) and [`limma-voom`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/container/limma-voom).

## Steps to execute

1. [Building container images: fastqc and multiqc](building-dockerfiles.md) (notebook: `building-dockerfiles.ipynb`). Builds two real single-purpose images. They become the two steps of the [multiqc-workflow case study](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/multiqc-workflow/README.md).
2. [Building an R container image](building-an-r-dockerfile.md) (notebook: `building-an-r-dockerfile.ipynb`). Puts the `hello-r` tool in a container.
3. [Publish your images to a registry](publish-your-images.md) (notebook: `publish-your-images.ipynb`). Gives your `fastqc` and `multiqc` images a full address and pushes them to GitHub's container registry.

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what a container image is, what a Dockerfile does line by line, and how Podman and Docker differ for a beginner. Keep it to fifteen lines.
```

**Ask it to build.**

```text
Write a Dockerfile (it must build with Podman) for a container that runs <tool and version>. Requirements: start FROM a fully qualified base image such as docker.io/library/..., pin every version, install with conda or pip from a file, run as one job, no secrets, and set no ENTRYPOINT that hides errors. After the file, give the exact `podman build` and `podman run` commands and the output that shows it worked.
```

**Ask it to review.**

```text
Review this Dockerfile for one container, one job. Flag unpinned versions, files copied that the image does not need, an image that does more than one job, and anything that would make the build differ next month. For each problem suggest a one-line fix.

<paste Dockerfile>
```


## Further reading

- [Podman documentation](https://docs.podman.io/) and the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Open Container Initiative](https://opencontainers.org/)
- [BioContainers](https://biocontainers.pro/), a catalogue of ready-made bioinformatics containers
- [hadolint](https://github.com/hadolint/hadolint), a Dockerfile linter
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

## Supplementary information

A container is a sealed box with everything your code needs: the system libraries, the language, your package versions and your script. Hand it to a collaborator, a cluster or an AI agent and the work runs the way it did on your laptop.

**The rule: one container, one job.** A container that does QC *and* differential expression *and* plotting is hard to test and hard to fit into a workflow. A container that does QC is one brick you can snap together with Nextflow.

> **Short image names.** Podman may ask which registry to use for a name such as `python`. Write the full name, for example `docker.io/library/python:3.11-slim`, and it will not ask.

### The anatomy of a single-purpose Dockerfile

Every single-purpose Dockerfile does four things. This is the scanpy-qc one:

```dockerfile
# 1. Pick a small, well-known base.
FROM docker.io/library/python:3.11-slim

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

1. **Base image.** Pick a `-slim` Python image or a Bioconductor image for R. Avoid `latest`; pin the version.
2. **Pinned installs.** Pin every version, and use `--no-cache-dir` to keep the image small.
3. **One entry-point script.** If you want two, you have two containers.
4. **`ENTRYPOINT`.** Running the image with no arguments gives the real tool, with `--help` (see [reusable CLIs](../reusable-clis/README.md)).

### Install Podman

[Podman](https://podman.io/) builds and runs containers. It needs no background service, and the Lifebit platform uses it, so what you build here moves there unchanged. It reads the same `Dockerfile` that Docker reads. Podman can also read a file named `Containerfile`.

Podman is only for building and testing on your own machine. When you push to GitHub, a GitHub Actions job can build and push the image for you (see [continuous integration](../continuous-integration/README.md)), so you can skip Podman if you do not have admin rights.

::::{tab-set}

:::{tab-item} macOS
:sync: mac

On a Mac, Podman runs inside a small Linux virtual machine. You start it once after each restart.

```bash
brew install podman
podman machine init
podman machine start
podman --version
```
:::

:::{tab-item} Windows
:sync: win

Follow the [Podman for Windows](https://podman.io/docs/installation#windows) installation page. It sets up WSL2 for you. Restart if it asks. Then, in Git Bash:

```bash
podman machine init
podman machine start
podman --version
```
:::

:::{tab-item} Linux
:sync: linux

Podman runs directly on Linux, with no virtual machine.

```bash
sudo apt install podman    # Debian, Ubuntu
# sudo dnf install podman  # Fedora, Red Hat
podman --version
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# Podman is the container engine on Lifebit.
podman --version
```
:::

::::

> **Check:** I ran the Mac commands on an Apple-silicon Mac on 2026-11-16 (`brew install podman` installed Podman 6.2.0; `podman machine init`, `podman machine start`, `podman run` and `podman build` all worked). The Windows commands ran in Git Bash on a GitHub-hosted Windows runner (Podman installed with `winget`; a container ran, the fastqc image built, and `fastqc` ran). I have not run them on a student's own Windows computer, or on Linux. On Linux with SELinux, a mounted folder may need `:Z` after the path, as in `-v "$PWD:$PWD:Z"`.

### A first build

```bash
# Move into the directory that has the Dockerfile.
cd /path/to/container/scanpy-qc

# Build. Tag with the version, not just `latest`.
podman build -t scanpy-qc:1.0.0 .

# Smoke test: with no arguments you should see --help.
podman run --rm scanpy-qc:1.0.0 --help

# Real run: mount your data, pass real arguments.
podman run --rm \
    -v "$(pwd)/data:/data" \
    scanpy-qc:1.0.0 \
    --input /data/raw.h5ad \
    --output /data/qc.h5ad
```

> **Check:** The Dockerfile in the repository is `container/scanpy-qc/Dockerfile` with its files in `context/`. This page used to say `containers/scanpy-qc`. Is the build command run from `container/scanpy-qc` or from `container/scanpy-qc/context`?

Two habits to form now. **Always tag**: never push `:latest` without also pushing a version such as `:1.0.0`. **Mount data, do not `COPY` it**: the image processes data; it does not carry it.

### Pushing to a registry

A registry stores images so others can pull them. For this work the natural place is GitHub Container Registry (GHCR), next to the repository.

```bash
# Log in once (uses your GitHub personal access token with `write:packages`).
echo "$GHCR_TOKEN" | podman login ghcr.io -u "$GHCR_USER" --password-stdin

# Tag for GHCR, then push.
podman tag scanpy-qc:1.0.0 ghcr.io/adeslatt/scanpy-qc:1.0.0
podman push ghcr.io/adeslatt/scanpy-qc:1.0.0
```

The book companion's [`.github/workflows`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/.github/workflows) folder automates this: every push to `main` builds the image, tags it `:latest` and with the git hash, and pushes both.

### The smell test for "too much job"

Split the container if any of these is true: the Dockerfile is over about 50 lines; the image installs Python *and* R *and* Bioconductor; the entry script has more than one subcommand that takes half a page of arguments; or you add `if mode == 'qc'` branches.

### Apple Silicon and x86_64

If you build on an M-series Mac and a collaborator runs on AWS x86, either build a multi-arch image (`podman build --platform linux/amd64,linux/arm64 --manifest myimage .`, then `podman manifest push`) or force the platform at run time (`podman run --platform linux/amd64 ...`, slower but it works).

## Next

[Continuous integration](../continuous-integration/README.md): let GitHub build and publish your images.
