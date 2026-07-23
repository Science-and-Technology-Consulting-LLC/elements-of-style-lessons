# Building an R Dockerfile

*Companion walkthrough to the [containers](README.md) lesson — the R
sibling of [`building-dockerfiles`](building-dockerfiles.md).*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal / RStudio** — copy each R block into `R` or an RStudio
  console; copy shell blocks into your terminal.
- **In the paired notebook** [`building-an-r-dockerfile.ipynb`](building-an-r-dockerfile.ipynb) — every R cell
  is executed by the Jupyter **R (IRkernel)** kernel. Run the shell
  blocks in a terminal FIRST to install R + IRkernel; then pick the R
  kernel when you open the notebook.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### One time — install R and register IRkernel

```bash
conda activate eos-lessons        # or any env dedicated to R work
conda install -c conda-forge r-base r-irkernel -y
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

Restart JupyterLab; the launcher now shows an **R** tile.

### Every time — verify R can see its tools

```r
for (cmd in c("R", "Rscript", "git", "docker", "conda")) {
  where <- Sys.which(cmd)
  cat(sprintf("  %-10s %s
", cmd,
              ifelse(nchar(where) > 0, where, "MISSING")))
}
```


## What we build

A single-purpose R container that ships the `hello-r` CLI from
[`rscript-cli-in-fifteen-minutes`](../reusable-clis/rscript-cli-in-fifteen-minutes.md).
Same *one container, one job* rule; different base image.

## Create a clean build directory

```bash
mkdir hello-r-docker && cd hello-r-docker
touch Dockerfile
```

## The Dockerfile

Paste into `Dockerfile`:

```dockerfile
# Rocker publishes small, well-maintained R base images.
FROM rocker/r-ver:4.4.1
LABEL description="hello-r CLI — docopt-based R container"

# System deps needed by many R packages (curl, xml2, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
      libcurl4-openssl-dev libssl-dev libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

# docopt is our CLI parser
RUN R -e "install.packages('docopt', repos='https://cloud.r-project.org')"

# Copy the CLI in
COPY hello-r.R /usr/local/bin/hello-r
RUN chmod +x /usr/local/bin/hello-r

ENTRYPOINT ["hello-r"]
```

## Build

```bash
docker build -t hello-r .
docker images | head
```

## Smoke-test

```bash
docker run --rm hello-r --help
docker run --rm hello-r greet --name Annie
```

## The Bioconductor variant

For real biomedical R work you'll want Bioconductor packages
(DESeq2, limma, edgeR). Swap the base image:

```dockerfile
FROM bioconductor/bioconductor_docker:RELEASE_3_19
```

Rocker + Bioconductor cover 99% of what shows up in the
[case-studies/endometriosis](../../case-studies/endometriosis/README.md)
and
[`container/limma-voom/`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/container/limma-voom)
worked examples.

## Push to a registry

Same as the Python container's push — GHCR is the default:

```bash
echo "$GHCR_TOKEN" | docker login ghcr.io -u "$GHCR_USER" --password-stdin
docker tag hello-r ghcr.io/science-and-technology-consulting-llc/hello-r:0.1.0
docker push ghcr.io/science-and-technology-consulting-llc/hello-r:0.1.0
```

## Where to next

→ Back to [containers](README.md).

→ [nextflow-modules](../nextflow-modules/README.md) — wrap this
container as a `.nf` module.
