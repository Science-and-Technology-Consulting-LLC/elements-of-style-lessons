# Building an R container image

You will put the `hello-r` command-line tool into a container, so that it runs the same way on any computer that has Podman. This is the R version of [building container images](building-dockerfiles.md).

**What you will do:**

- Write a Dockerfile that starts from a ready-made R image.
- Build the image and test it with `podman run`.
- See how to swap in a Bioconductor base image, and how to publish the image.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Building reusable command-line tools](../reusable-clis/README.md), is done. In particular, you have the `hello-r.R` script from [the Rscript CLI walkthrough](../reusable-clis/rscript-cli-in-fifteen-minutes.md).
- The first walkthrough, [Building container images](building-dockerfiles.md), is done.
- Podman is installed and, on a Mac or Windows computer, running (`podman machine start`). We install it in [Install Podman](README.md#install-podman).
- For the optional publish step: a [GitHub account](https://github.com/signup) and a personal access token (a password that only works for chosen tasks) with the `write:packages` permission. See [GitHub's guide to the container registry](https://docs.github.com/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

> **Where to type the commands.** The command boxes marked `bash` run in your **terminal**. The one notebook cell (*Check that R can see its tools*) uses the R kernel. If a command says *command not found*, see [the command line and Git Bash](../command-line-and-git-bash/README.md).

## Steps to execute

### Install R and register the R kernel (once)

*Why:* a **kernel** is the program that runs the code in a notebook cell. JupyterLab needs the R kernel, called IRkernel, before it can run R cells. The Introduction already installed it, so if the Launcher already shows an **R** tile, you can skip this step.

In your terminal, run:

```bash
conda activate eos        # or any env dedicated to R work
conda install -c conda-forge r-base=4.4 r-irkernel -y
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

**What you should see:** conda finishes without an error. The last command prints a line that ends with `Installed kernelspec ir`.

Restart JupyterLab. The Launcher now shows an **R** tile.

> **Picture to add:** the JupyterLab Launcher with the R tile visible (save as assets/building-an-r-dockerfile-step-1.png)

### Check that R can see its tools

*Why:* this cell finds each program and prints where it lives, or `MISSING`. For this lesson `podman` must be found.

Run the next cell.

```r
for (cmd in c("R", "Rscript", "git", "podman", "conda")) {
  where <- Sys.which(cmd)
  cat(sprintf("  %-10s %s\n", cmd,
              ifelse(nchar(where) > 0, where, "MISSING")))
}
```

**What you should see:** one line per program, each with a path, for example:

```text
  R          /.../envs/eos/bin/R
  Rscript    /.../envs/eos/bin/Rscript
  git        /.../envs/eos/bin/git
  podman     /usr/local/bin/podman
  conda      /Users/you/miniforge3/bin/conda
```

### What we build

A single-purpose R container that ships the `hello-r` tool from [the Rscript CLI walkthrough](../reusable-clis/rscript-cli-in-fifteen-minutes.md). The same *one container, one job* rule applies as for the Python containers; only the base image differs. A **base image** is the ready-made image you start from.


### Create a clean build directory

*Why:* a **build directory** is the folder Podman reads when it builds. Podman looks for a file named exactly `Dockerfile` in it. A new folder keeps the build small.

In your terminal, run:

```bash
cd ~
mkdir hello-r-docker && cd hello-r-docker
touch Dockerfile
```

**What you should see:** no output. Check with `pwd`: the path ends in `hello-r-docker`.

### Copy your script into the build directory

*Why:* the Dockerfile copies `hello-r.R` into the image, and Podman can only copy files from the build directory. Without this step the build stops with a `COPY failed` error.

If you made `hello-r-cli` in your home folder, run:

```bash
cp ../hello-r-cli/hello-r.R .
ls
```

If you made `hello-r-cli` somewhere else, copy `hello-r.R` by hand.

**What you should see:** `Dockerfile` and `hello-r.R` listed.

### Fill in the Dockerfile

*Why:* the Dockerfile is the recipe. Open `Dockerfile` in an editor and paste:

```dockerfile
# Rocker publishes small, well-maintained R base images.
FROM docker.io/rocker/r-ver:4.4.1
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

What the lines mean:

- `FROM` names the base image. [Rocker](https://rocker-project.org/) publishes R images with a fixed R version (here 4.4.1).
- `RUN` runs a command while the image is built. Here it installs system libraries, then the R package `docopt`.
- `COPY` copies your script into the image and `chmod +x` makes it executable.
- `ENTRYPOINT` is what runs when someone starts the container. Anything typed after the image name is handed to `hello-r`.

Save the file.

### Build the image

*Why:* `podman build` turns the Dockerfile into an image. `-t hello-r` names it `hello-r`. The dot means: build in this folder. The first build takes several minutes because Podman downloads R and installs packages.

Make sure Podman is running. On a Mac or Windows computer, run `podman machine start` first.

> **Picture to add:** a terminal showing `podman machine list` with the machine running (save as assets/building-an-r-dockerfile-step-6.png)

```bash
podman build -t hello-r .
podman images | head
```

**What you should see:** many progress lines, ending without `ERROR`. Then a table whose first row has `localhost/hello-r` under `REPOSITORY` and `latest` under `TAG`.

### Smoke-test the image

*Why:* a smoke test is the cheapest check that the tool works inside the container.

```bash
podman run --rm hello-r --help
podman run --rm hello-r greet --name Annie
```

`--rm` deletes the container when it stops, so nothing piles up.

**What you should see:** first the help screen from your usage text (the `greet` and `version` lines), then `Hello, Annie!`.

### The Bioconductor variant (read only)

*Why:* for real biomedical R work you will want Bioconductor packages such as DESeq2, limma and edgeR. To get them, swap the base image:

```dockerfile
FROM docker.io/bioconductor/bioconductor_docker:RELEASE_3_19
```

[Bioconductor](https://bioconductor.org/) images and Rocker images cover most of what shows up in the [endometriosis case study](../../case-studies/endometriosis/README.md) and the [`container/limma-voom/`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/container/limma-voom) worked example.

### Push to a registry (optional)

*Why:* a registry is a website that stores images so other people and other computers can pull them. GitHub's registry, GHCR, is the default for this course. You need a token with `write:packages` first (see Pre-requisites). Set `GHCR_USER` to your GitHub user name and `GHCR_TOKEN` to the token. Replace the organisation name in the last two lines with your own lowercase user name unless you belong to that organisation.

```bash
echo "$GHCR_TOKEN" | podman login ghcr.io -u "$GHCR_USER" --password-stdin
podman tag hello-r ghcr.io/science-and-technology-consulting-llc/hello-r:0.1.0
podman push ghcr.io/science-and-technology-consulting-llc/hello-r:0.1.0
```

**What you should see:** `Login Succeeded`, then lines for each layer ending in `Pushed`, and a final line with `0.1.0: digest: sha256:`.

### If something goes wrong

- **`COPY failed: file not found`.** `hello-r.R` is not in the build folder. Repeat *Copy your script into the build directory* and run `ls`.
- **`Cannot connect to Podman`, or `podman: command not found`.** Podman is not running. Run `podman machine start`, wait for it to finish, and build again.
- **`denied` when you push.** You do not have permission for that organisation name. Use `ghcr.io/<your-lowercase-github-name>/hello-r:0.1.0` in both the `tag` and `push` lines.

## Next

Back to the [Containers lesson](README.md), then [Nextflow modules and features](../nextflow-modules/README.md): wrap this container as a `.nf` module.
