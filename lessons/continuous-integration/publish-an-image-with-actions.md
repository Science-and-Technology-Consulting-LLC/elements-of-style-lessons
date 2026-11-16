# Publish a container image with GitHub Actions

**This walkthrough needs a GitHub account, the GitHub command-line tool (`gh`) signed in to it, and [Podman](https://podman.io/docs/installation) on your computer.** It creates a real repository and a real package on your GitHub account.

You will put a tiny program in a container, test it on your computer, and then let GitHub build the image and publish it to the GitHub Container Registry (GHCR) every time you push. This matters because an image on a registry is one that Nextflow, a colleague or the Lifebit platform can pull, and the version on GitHub is built the same way every time.

*Part of the [continuous-integration](README.md) lesson.*

## Start here

### What you will do

- Build and test a one-file container image with Podman.
- Write a workflow that builds the image with Podman on GitHub's computer and pushes it to GHCR.
- Watch the run on the **Actions** tab.
- Find the published image, make it public, and pull it back to your computer.

### What you need

- A [GitHub account](https://github.com/signup) (free).
- The [GitHub CLI (`gh`)](https://cli.github.com/), installed and signed in. See [github-authenticate](../version-control/github-authenticate.md). Check with `gh auth status`.
- [Git](https://git-scm.com/), set up with your name and email. See [why-git-and-setup](../version-control/why-git-and-setup.md).
- [Podman](https://podman.io/docs/installation), installed. On a Mac or Windows computer its machine must be running (`podman machine start`). See [containers](../containers/README.md).
- A first CI job behind you. See [add-a-first-ci-job](add-a-first-ci-job.md).
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`publish-an-image-with-actions.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/continuous-integration/publish-an-image-with-actions.ipynb) and run each cell in order, top to bottom.

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git`, `gh` and `podman`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

> **Check:** I wrote this lesson without running it. It needs a GitHub login and Podman, and neither was available where I edited it. Please run it once from a fresh `~/eos-practice` and tell me what differs. The Podman steps on GitHub's side rely on Podman 4.9.3 being installed on the `ubuntu-latest` runner, as listed in the [runner image notes](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md).

## Steps to execute

### Confirm you are signed in to GitHub

Why: *Create the repository and push* makes a repository on GitHub. It fails if `gh` does not know who you are.

```bash
gh auth status
```

**What you should see:** a line that says `Logged in to github.com` followed by your GitHub user name. If not, run `gh auth login`, or follow [github-authenticate](../version-control/github-authenticate.md).

### Make a one-file image

Why: the smallest useful image has one program and one command. This cell makes a folder `hello-image` in `~/eos-practice`, with a Python file and a `Dockerfile`. A *Dockerfile* is a text file that lists how to build an image. Podman reads it the same way Docker does. The `FROM` line names the base image in full, `docker.io/library/python`, so Podman does not have to ask which registry you mean.

```bash
mkdir -p ~/eos-practice/hello-image
cd ~/eos-practice/hello-image
cat > hello.py <<'EOF'
print("hello from a container")
EOF
cat > Dockerfile <<'EOF'
FROM docker.io/library/python:3.11-slim
COPY hello.py /hello.py
ENTRYPOINT ["python", "/hello.py"]
EOF
ls
```

**What you should see:** the two file names, `Dockerfile` and `hello.py`.

### Build and test the image on your computer

Why: test the image before you let GitHub build it. A failure on your computer is quicker to read than one on GitHub. On a Mac or Windows computer, Podman must be running: run `podman machine start` first.

```bash
podman build -t hello-image .
podman run --rm hello-image
```

**What you should see:** build lines that end with `Successfully tagged localhost/hello-image:latest`, then the line `hello from a container`. `--rm` removes the finished container.

> **Picture to add:** the terminal after `podman run --rm hello-image`, showing the greeting (save as assets/publish-an-image-with-actions-step-3.png)

### Look at the workflow

Why: a *workflow* is a recipe that GitHub follows on its own computer. This one runs when you push a change to the image files. It logs in to GHCR with a token that GitHub makes for each run, builds the image with Podman, and pushes it. Here is what each part does:

- `paths:` limits the run to pushes that touch the image files or this workflow. A change to a README does not rebuild the image.
- `permissions: packages: write` lets the run publish a package. Without it the push is refused.
- `${GITHUB_REPOSITORY,,}` is the repository name in lower case. A registry rejects capital letters in an image name.
- The tag is the commit hash (`github.sha`). Every push gets its own tag, so a rebuild never changes an image that an earlier run already used.

Read the file below. The next cell writes it for you.

```yaml
name: Publish image
on:
  push:
    branches: [main]
    paths:
      - "Dockerfile"
      - "hello.py"
      - ".github/workflows/publish.yml"
env:
  REGISTRY: ghcr.io
jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - name: Name the image in lower case
        run: echo "IMAGE=${REGISTRY}/${GITHUB_REPOSITORY,,}" >> "$GITHUB_ENV"
      - name: Log in to GHCR
        run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u "${{ github.actor }}" --password-stdin
      - name: Build the image
        run: podman build -t "${IMAGE}:${{ github.sha }}" .
      - name: Push the image
        run: podman push "${IMAGE}:${{ github.sha }}"
```

### Write the workflow file

Why: GitHub only runs workflows it finds in `.github/workflows/`. The folder name starts with a dot.

```bash
mkdir -p .github/workflows
cat > .github/workflows/publish.yml <<'EOF'
name: Publish image
on:
  push:
    branches: [main]
    paths:
      - "Dockerfile"
      - "hello.py"
      - ".github/workflows/publish.yml"
env:
  REGISTRY: ghcr.io
jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - name: Name the image in lower case
        run: echo "IMAGE=${REGISTRY}/${GITHUB_REPOSITORY,,}" >> "$GITHUB_ENV"
      - name: Log in to GHCR
        run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u "${{ github.actor }}" --password-stdin
      - name: Build the image
        run: podman build -t "${IMAGE}:${{ github.sha }}" .
      - name: Push the image
        run: podman push "${IMAGE}:${{ github.sha }}"
EOF
ls -a .github/workflows
```

**What you should see:** the file name `publish.yml`.

### Create the repository and push

Why: this saves ("commits") your three files, creates a public repository called `hello-image` on your GitHub account, and uploads the files. The upload starts the workflow.

```bash
git init -b main
git add .
git commit -m "first image and workflow"
gh repo create hello-image --public --source=. --push
```

**What you should see:** lines from Git that include `first image and workflow`, then lines from `gh` that show the new repository's address, such as `https://github.com/<your-name>/hello-image`.

### Watch the run

Why: this is the payoff. GitHub builds your image on its own computer.

1. Open `https://github.com/<your-name>/hello-image`.
2. Click the **Actions** tab.
3. Click the newest run, named `first image and workflow`.

**What you should see:** a job named `publish` with five steps. After one to two minutes every step has a green tick.

> **Picture to add:** the Actions tab with one green run and its five steps open (save as assets/publish-an-image-with-actions-step-6.png)

### Find the image and make it public

Why: a new package on GHCR is private. Nextflow, a colleague or Lifebit can only pull it without logging in once it is public.

1. On your repository's page, find **Packages** on the right and click `hello-image`.
2. Click **Package settings**.
3. In the **Danger Zone**, click **Change visibility**, choose **Public**, and confirm.

**What you should see:** the package page shows the tag, which is a long string of letters and numbers (your commit hash), and a line that starts `podman pull ghcr.io/`.

> **Picture to add:** the package page with its commit-hash tag and the pull command (save as assets/publish-an-image-with-actions-step-7.png)

> **Check:** the menu names above are from memory of GitHub's current pages. Please confirm them and correct any that have moved.

### Pull the image back and run it

Why: this proves the image on the registry is the one you built. The cell asks Git for the commit hash and `gh` for your user name. `tr` makes the name lower case, as the workflow did.

```bash
GH_USER=$(gh api user -q .login | tr '[:upper:]' '[:lower:]')
SHA=$(git rev-parse HEAD)
podman pull ghcr.io/${GH_USER}/hello-image:${SHA}
podman run --rm ghcr.io/${GH_USER}/hello-image:${SHA}
```

**What you should see:** pull lines that end with an image ID, then `hello from a container`.

### If something goes wrong

- **`Cannot connect to Podman`, or `podman: command not found`.** Podman is not installed, or its machine is not running. On a Mac or Windows computer, run `podman machine start`, wait for it to finish, and run the cell again.
- **The `Push the image` step fails with `denied` or `permission`.** The job needs `packages: write` under `permissions:`, as in the file above. Check that you wrote it exactly, with the same indentation.
- **The build step fails with `invalid reference format`.** The image name has a capital letter. The `Name the image in lower case` step is there to prevent that. Check that it is in your file.
- **`gh repo create` says the repository name is taken.** You ran *Create the repository and push* before. Choose another name in place of `hello-image`, or delete the old practice repository on GitHub first.
- **The pull says `unauthorized`.** The package is still private. Do *Find the image and make it public*.
- **Nothing appears on the Actions tab.** The workflow file is not on GitHub, or it is not at `.github/workflows/publish.yml`.

## Supplementary information

### Why tag by commit

The tag `github.sha` names the exact commit that built the image. A Nextflow config that pins that tag will keep getting the same image, even after later pushes. The repositories `LRP2` and `sc-nsforest-qc-nf` publish this way.

### Build many images from one repository

A repository can hold several images, each in its own folder. A *matrix* runs the same steps once for each folder name. The LRP2 workflow in its `.github/workflows/docker-publish.yml` does this for seven images, with `paths: container/**` so that only a change under `container/` starts it.

### Docker's actions instead of Podman

Many repositories use the `docker/login-action` and `docker/build-push-action` actions. They do the same job. The lesson [GitHub Actions for maintenance testing](github-actions-for-maintenance-testing.md) reads one such workflow. Podman needs no extra action because it is already on GitHub's `ubuntu-latest` computer.

## Next

[Documentation](../documentation/README.md): build a Sphinx site, then publish it with Actions.
