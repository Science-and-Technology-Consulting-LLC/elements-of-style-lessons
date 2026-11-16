# Building container images: fastqc and multiqc

You will build two small container images, one for the sequencing quality tool FastQC and one for MultiQC, so that each tool runs the same way on your laptop, on a cluster and inside a workflow.

**What you will do:**

- Write a `Dockerfile` and an `environment.yml` for [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/).
- Build the image and test it with `podman run`.
- Do the same for [MultiQC](https://multiqc.info/).
- Optionally, publish each folder to GitHub.

**What you need:**

- [Podman](https://podman.io/docs/installation), installed. On a Mac or Windows computer it must also be running (`podman machine start`). See the install notes in the [containers lesson](README.md).
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) and the `eos` environment from [conda environments](../conda-environments/README.md).
- A terminal. See [the command line and Git Bash](../command-line-and-git-bash/README.md).
- For the optional GitHub steps: a [GitHub account](https://github.com/signup), the [GitHub CLI](https://cli.github.com/) (`gh`), and the sign-in steps in [GitHub authentication](../version-control/github-authenticate.md).

## Start here

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`building-dockerfiles.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/containers/building-dockerfiles.ipynb) and run each cell in order, top to bottom.

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the six setup steps on the [Introduction page](../introduction/README.md) and the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Understand what you are building

*Why:* two new words come up in every step after this one.

- A **Dockerfile** is a plain-text file that lists the commands Podman follows to assemble an image: which base operating system to start from, which packages to install, which files to copy in.
- A **container image** is the finished, portable bundle that `podman build` makes from a Dockerfile. A **container** is a running copy of an image.

You will build **two** small images, `fastqc` and `multiqc`. They come back in the [multiqc-workflow case study](../../case-studies/multiqc-workflow/README.md).

> **Warning.** `podman build` copies *every file in the build directory* to Podman. If the folder is huge, the build is huge. Keep the build folder small: only what the image needs. A `.dockerignore` file can exclude files.


### Activate your conda environment

*Why:* you made the `eos` environment in the [conda environments lesson](../conda-environments/creating-a-conda-environment.md). Activating it puts its tools on your path.

Run the next cell.

```bash
conda activate eos
```

**What you should see:** no output. In a terminal, your prompt now starts with `(eos)`.

> **Check:** In a notebook with the Bash kernel, `conda activate` can fail with `CondaError: Run 'conda init' before 'conda activate'`. If you see it, close JupyterLab, activate `eos` in your terminal first, and start JupyterLab from that terminal. Please confirm that this is the right advice for Lifebit as well.

### Go to your home folder

*Why:* you will make folders and run `git init` in them. If you do that inside the cloned course folder, you put one Git repository inside another. Your home folder keeps them apart. Both image folders (`fastqc-docker` and `multiqc-docker`) will sit side by side here, which the next lesson expects.

Run the next cell.

```bash
cd ~
pwd
```

**What you should see:** your home folder, for example `/Users/yourname` on a Mac or `/c/Users/yourname` in Git Bash.

### Part 1: the `fastqc` image

### Create a clean build directory

*Why:* Podman looks for a file named *exactly* `Dockerfile`, in the folder where you build. A new empty folder keeps the build small.

Run the next cell.

```bash
mkdir fastqc-docker
cd fastqc-docker
touch Dockerfile
```

**What you should see:** no output. Check with `ls`: you are now inside `fastqc-docker`, and it holds one empty file named `Dockerfile`.

### Fill in the Dockerfile

*Why:* this file is the recipe. Open `Dockerfile` in an editor (VS Code, JupyterLab's editor, `nano` or `vim`) and paste:

```dockerfile
# Base image: condaforge/miniforge3 comes with conda pre-installed and uses only the conda-forge channel.
FROM docker.io/condaforge/miniforge3:26.9.4-2
LABEL description="Base container image with conda + fastqc"
ARG ENV_NAME="fastqc"

# Install the conda environment declared in environment.yml
COPY environment.yml /
RUN conda env create --quiet --name ${ENV_NAME} --file /environment.yml && conda clean -a

# Add the env's bin/ to PATH so the image's default shell finds fastqc
ENV PATH /opt/conda/envs/${ENV_NAME}/bin:$PATH
```

What the lines mean:

- `FROM` names the base image. We start from `condaforge/miniforge3`, a small image that has conda installed, so we do not have to install it ourselves. The tag `26.9.4-2` fixes the version, so the image does not change under you.
- `LABEL` attaches a note to the image.
- `ARG` sets a build-time variable, here the environment name.
- `COPY` copies a file from your folder into the image.
- `RUN` runs a command while the image is built.
- `ENV` sets a variable inside the image, here the search path for programs.
- Lines that start with `#` are comments.

Save the file.

### Create the `environment.yml`

*Why:* the Dockerfile copies a file called `environment.yml`. It lists the packages to install. Create it:

Run the next cell.

```bash
touch environment.yml
```

Open `environment.yml` and paste:

```yaml
name: fastqc
channels:
  - conda-forge
  - bioconda
dependencies:
  - fastqc
```

The [`bioconda`](https://bioconda.github.io/) channel is where community-vetted bioinformatics packages live. `fastqc` is the read-quality tool this image will provide. Save the file.

> **Check:** Does `conda env create` find `fastqc` and `multiqc` for Linux ARM when the build runs on an Apple Silicon Mac (M1 to M4)? This lesson was not tested there.

### Build the image

*Why:* `podman build` turns the Dockerfile into an image. The `-t fastqc` option **tags** (names) the image `fastqc`. The dot means: build in this folder. This step takes a few minutes the first time.

Make sure Podman is running. On a Mac or Windows computer, run `podman machine start` first.

> **Picture to add:** a terminal showing `podman machine list` with the machine running (save as assets/building-dockerfiles-step-7.png)

Run the next cell.

```bash
podman build -t fastqc .
```

**What you should see:** many lines of progress while Podman downloads the base image and installs fastqc. When it finishes without the word `ERROR`, the last line is `Successfully tagged localhost/fastqc:latest`, followed by the image ID.

### Confirm the image exists

*Why:* `podman images` lists the images on your machine.

Run the next cell.

```bash
podman images
```

**What you should see:** a table with the columns `REPOSITORY`, `TAG`, `IMAGE ID`, `CREATED` and `SIZE`. One row has `localhost/fastqc` under `REPOSITORY` and `latest` under `TAG`.

### Test the image

*Why:* a smoke test proves the tool runs inside the container. First, save the current folder's path in a variable so we can mount the folder into the container. To **mount** a folder is to make it visible inside the container.

Run the next cell.

```bash
PWD=$(pwd)
```

**What you should see:** no output.

Now run `fastqc -h` **inside** the container.

Run the next cell.

```bash
podman run --rm -v "$PWD:$PWD" -w "$PWD" fastqc fastqc -h
```

**What you should see:** the FastQC help text scrolls past. It starts with a line like `FastQC - A high throughput sequence QC analysis tool`, followed by `SYNOPSIS`.

> **Windows, Git Bash.** This command ran in Git Bash on a Windows computer without any extra prefix (a GitHub-hosted Windows runner, with Podman installed and its machine started). If a command on your own computer says that a path is not found, Git Bash may be rewriting the path. Put `MSYS_NO_PATHCONV=1` in front of the command and run it again.

What each part of the command means:

- `-it`: interactive, with a terminal attached (so output is not held back).
- `-v $PWD:$PWD`: mount the current folder into the container at the same path.
- `-w $PWD`: start the container in that same folder.
- `fastqc` (first): the image name.
- `fastqc -h` (last): the command to run inside the container.

You now have a portable fastqc that runs the same way on your laptop, on Lifebit, and inside any Nextflow module that names this container.

### Publish the source to GitHub (optional)

*Why:* never let a `Dockerfile` live on only one machine. Skip the sections marked *(optional)* if you do not have a GitHub account. The next lessons need the images, not the repositories.

First create a `README.md`. Run the next cell, then open `README.md` and paste the lines shown in the comments.

```bash
touch README.md
# open README.md in an editor and paste:
#
#   # fastqc-docker
#   Build a container for fastqc from bioconda.
#   podman build -t fastqc .
#   podman run --rm -v "$PWD:$PWD" -w "$PWD" fastqc fastqc -h
```

**What you should see:** no output. The file `README.md` now exists.

### Sign in to GitHub (optional)

*Why:* `gh` needs permission to create a repository for you. Follow the prompts; see [GitHub authentication](../version-control/github-authenticate.md) for a guided version. This opens a web page where you approve the sign-in.

Run the next cell.

```bash
gh auth login   # if you haven't yet — see github-authenticate.ipynb
```

**What you should see:** `gh` asks a few questions, then prints a line like `Logged in as your-username`.

### Tell Git who you are (optional)

*Why:* Git stamps your name and email on every commit. Edit the two values in the next cell before you run it: use your own email and your GitHub user name.

Run the next cell.

```bash
git config --global user.email 'you@example.com'
git config --global user.name  'your-github-username'
```

**What you should see:** no output.

### Commit (optional)

*Why:* a **commit** saves a snapshot of your files in Git. `git init` starts a repository in this folder.

Run the next cell.

```bash
git init -b main
git add . && git commit -m 'initial commit'
```

**What you should see:** a line like `Initialized empty Git repository`, then a line with `[main (root-commit)` and `initial commit`, and a count of files changed.

### Create the GitHub repository (optional)

*Why:* this publishes your folder. `gh repo create` asks questions. Answer: *Push an existing local repository to GitHub*, path `.`, name `fastqc-docker`, *Public*, remote name `origin`, *Yes* to push.

Run the next cell.

```bash
gh repo create   # answer: Push an existing local repository → path '.' → name fastqc-docker → Public → origin → Yes push
```

**What you should see:** on success `gh` prints:

```text
✓ Created repository <your-user>/fastqc-docker on GitHub
✓ Added remote https://github.com/<your-user>/fastqc-docker.git
✓ Pushed commits to https://github.com/<your-user>/fastqc-docker.git
```

> **Picture to add:** your new fastqc-docker repository page on GitHub (save as assets/building-dockerfiles-step-14.png)

The reference copy of this repository is [`adeslatt/fastqc-docker`](https://github.com/adeslatt/fastqc-docker).

### Part 2: the `multiqc` image

[MultiQC](https://multiqc.info/) gathers the per-sample reports that FastQC writes into one summary. Its Dockerfile is nearly the same.

### Choose one path

*Why:* you can either copy the finished reference version to compare, or build your own. Do **one** of the two. If you do both, `mkdir multiqc-docker` in *Go back to your home folder* stops with `File exists`.

**Path A (optional): clone the reference version.** Run the next cell. Then type `cd ~/multiqc-docker`, skip *Go back to your home folder* and *Create the build directory*, and continue with *Build and list the image*. Skip *Publish `multiqc-docker` (optional)* too; the clone is already a Git repository.

```bash
cd ~
git clone https://github.com/adeslatt/multiqc-docker.git
```

**What you should see:** `Cloning into 'multiqc-docker'...` and a `done` line. The folder `~/multiqc-docker` now exists.

**Path B: build your own from scratch.** Continue with *Go back to your home folder*.

### Go back to your home folder

*Why:* Part 1 left you inside `fastqc-docker`. The new folder must sit next to it, not inside it.

Run the next cell.

```bash
cd ~
pwd
```

**What you should see:** your home folder, the same path as in *Go to your home folder*.

### Create the build directory

Run the next cell.

```bash
mkdir multiqc-docker && cd multiqc-docker
touch Dockerfile
```

**What you should see:** no output. You are now inside `multiqc-docker`, which holds one empty `Dockerfile`.

Open `Dockerfile` and paste:

```dockerfile
FROM docker.io/condaforge/miniforge3:26.9.4-2
LABEL description="Base container image with conda + multiqc"
ARG ENV_NAME="multiqc"

COPY environment.yml /
RUN conda env create --quiet --name ${ENV_NAME} --file /environment.yml && conda clean -a

ENV PATH /opt/conda/envs/${ENV_NAME}/bin:$PATH
```

Then create `environment.yml` in the same folder and paste:

```yaml
name: multiqc
channels:
  - conda-forge
  - bioconda
dependencies:
  - multiqc
```

### Build and list the image

*Why:* the same two commands as Part 1. The first line creates the (empty) `environment.yml`; if you already made it and pasted the YAML, `touch` leaves it alone. The build takes a few minutes.

Run the next cell.

```bash
touch environment.yml   # then paste the YAML above into it
podman build -t multiqc .
podman images
```

**What you should see:** the build progress, then the `podman images` table. It now has a `multiqc` row as well as the `fastqc` row.

Now test it. Run the next cell.

```bash
PWD=$(pwd)
podman run --rm -v "$PWD:$PWD" -w "$PWD" multiqc multiqc -h
```

**What you should see:** the MultiQC help text, starting with a line like `Usage: multiqc [OPTIONS] [ANALYSIS DIRECTORY]`.

### Publish `multiqc-docker` (optional)

*Why:* the same routine as *Sign in to GitHub* through *Create the GitHub repository*. Do this only on Path B. Run the next cell, then answer the `gh repo create` questions: *Push an existing local repository*, path `.`, name `multiqc-docker`, *Public*.

```bash
touch README.md   # add a short description + build/run commands
git init -b main
git add . && git commit -m 'initial commit'
gh repo create   # answer: Push existing → . → multiqc-docker → Public
```

**What you should see:** the same three lines as in *Create the GitHub repository (optional)*, with `multiqc-docker` in them.

The reference copy of this repository is [`adeslatt/multiqc-docker`](https://github.com/adeslatt/multiqc-docker). It becomes the containerised step in the [multiqc-workflow](https://github.com/Science-and-Technology-Consulting-LLC/multiqc-workflow) case study.

### Recap

You now have two portable containers:

- **`fastqc`**: per-sample sequencing quality control.
- **`multiqc`**: combines fastqc's per-sample reports into one HTML page.

Both:

- build from the same base image (`condaforge/miniforge3`);
- install their tool through `environment.yml`, the same file you would use on your laptop;
- can live in their own GitHub repository (`fastqc-docker`, `multiqc-docker`);
- offer one command (`fastqc`, `multiqc`) that a [Nextflow module](../nextflow-modules/README.md) can call directly.

The [multiqc-workflow case study](../../case-studies/multiqc-workflow/README.md) joins them into a two-step pipeline: **fastqc, then multiqc**.

### If something goes wrong

- **`Cannot connect to Podman`, or `podman: command not found`.** Podman is not running or not installed. Run `podman machine start`, wait for it to finish, and try again. See [the containers lesson](README.md) for install links.
- **`the input device is not a TTY`.** Remove `-it` from the `podman run` command and run it again.
- **`CondaError: Run 'conda init'`, or `conda: command not found`.** Activate the environment in a terminal first, then start JupyterLab from that terminal (see the Check in *Activate your conda environment*).
- **`mkdir: multiqc-docker: File exists`.** You already cloned it in *Choose one path*. Use the cloned folder, or delete it and start Path B.

## Next

[Publish your images to a registry](publish-your-images.md): push these two images, so that a workflow on any computer can download them. Or go back to the [containers lesson](README.md).
