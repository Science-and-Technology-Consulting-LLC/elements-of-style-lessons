# Publish your images to a registry

You will tag your two images with a full registry address and push them to GitHub's container registry, because a workflow can only use an image that it can download.

**What you will do:**

- Rebuild the `fastqc` and `multiqc` images.
- Give each image a full, versioned address.
- Log in to the registry and push both images.

**What you need:**

- The two images from [building container images](building-dockerfiles.md): `fastqc` and `multiqc`, in the folders `~/fastqc-docker` and `~/multiqc-docker`.
- [Podman](https://podman.io/docs/installation), installed. On a Mac or Windows computer it must also be running (`podman machine start`). See the [containers lesson](README.md).
- A [GitHub account](https://github.com/signup) and a personal access token (a password that only works for chosen tasks) with the `write:packages` permission. See [GitHub's guide to the container registry](https://docs.github.com/packages/working-with-a-github-packages-registry/working-with-the-container-registry).
- A terminal. See [the command line and Git Bash](../command-line-and-git-bash/README.md).

## Start here

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`publish-your-images.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-modules/publish-your-images.ipynb) and run each cell in order, top to bottom.

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Choose a registry

*Why:* a **registry** is a website that stores container images so that other computers can download them. There are two common choices.

| Registry | When to use it | Sign-in |
|---|---|---|
| **[GitHub Container Registry (GHCR)](https://docs.github.com/packages/working-with-a-github-packages-registry/working-with-the-container-registry)** | Default for open work. Free, unlimited public images, and it sits next to your code. | Personal access token with `write:packages` |
| **[Docker Hub](https://hub.docker.com/)** | The older default. The free tier now limits how often others can pull. | Docker Hub access token |

The [containers lesson](README.md) uses **GHCR**. Pick one per repository and stay with it.

### Go to your home folder

*Why:* the next cell uses the folder names `fastqc-docker` and `multiqc-docker`, so it must start in the folder that holds both. That is the home folder if you followed [building container images](building-dockerfiles.md).

Run the next cell.

```bash
cd ~
ls
```

**What you should see:** a list that includes `fastqc-docker` and `multiqc-docker`. If either is missing, go back to [building container images](building-dockerfiles.md).

### Rebuild the images (recap)

*Why:* this makes sure both images exist and are current. Because Podman remembers each step, the rebuild is fast if nothing changed.


Run the next cell.

```bash
cd fastqc-docker && podman build -t fastqc .
cd ../multiqc-docker && podman build -t multiqc .
```

**What you should see:** for each image, build lines ending without `ERROR`. Most steps say `CACHED` if you built the images before.

### Tag, log in and push to GHCR

*Why:* each image needs a *fully qualified* tag: `<registry>/<user>/<image>:<version>`. A **tag** is the name Podman uses for an image. Including a version means you can always get back the exact image that produced a result.

The cell below does four things: it tags both images, logs in, and pushes both. Before you run it:

1. Set two variables in your terminal, or in a cell above: `GHCR_USER` (your GitHub user name) and `GHCR_TOKEN` (your token). For example `export GHCR_USER=your-username`.
2. The cell uses the organisation name `science-and-technology-consulting-llc`. If you are not a member of that organisation, replace it with your own lowercase GitHub user name in the four `ghcr.io/...` addresses.

> **Check:** Students cannot push to `ghcr.io/science-and-technology-consulting-llc/`. Should this cell use the student's own GitHub user name instead?

Run the next cell.

```bash
podman tag fastqc  ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9
podman tag multiqc ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0

echo "$GHCR_TOKEN" | podman login ghcr.io -u "$GHCR_USER" --password-stdin

podman push ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9
podman push ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0
```

**What you should see:** `podman tag` prints nothing. The login prints `Login Succeeded`. Each push prints `The push refers to repository [ghcr.io/...]`, then one line per layer ending in `Pushed` (or `Layer already exists`), and a final line such as `v0.11.9: digest: sha256:... size: ...`.

> **Picture to add:** the GitHub page "Packages" of your account showing the pushed fastqc and multiqc images (save as assets/publish-your-images-step-4.png)

New packages on GHCR start **private**. To let a workflow on another computer pull the image without logging in, open the package on GitHub, go to its settings, and change its visibility to **Public**.

The registry address is now the *portable address* of your image. Your Nextflow module, and any CWL workflow, names it in a `container` line.

### If something goes wrong

- **`denied: permission_denied` on push.** The address names an organisation you are not in. Use your own lowercase GitHub user name in the address. Also check that your token has the `write:packages` permission.
- **`unauthorized`, or another error at the login line.** The user name or token is wrong or empty. Run `echo "$GHCR_USER"` to check the user name, set both variables again, and rerun the cell.
- **`cd: fastqc-docker: No such file or directory`.** You are not in the folder that holds the two image folders. Run *Go to your home folder* again.

## Next

[Continuous integration](../continuous-integration/README.md): let GitHub Actions build and push your images for you, so that you do not repeat these steps by hand. The *Use an image of your own* step of [two containers, two modules](../nextflow-modules/fastqc-and-multiqc-modules.md) then runs a published image in a workflow.
