# Continuous integration

*In the book: Section 4.5, Continuous Integration with GitHub Actions.*

This lesson shows you how to make GitHub check your work automatically on every push, so broken things are found in minutes. You will add a first check to a new repository and read the real workflows that keep this course working.

## Start here

### Before you start

The previous lesson is [Containers](../containers/README.md). You need an image to publish. For the first notebook you also need a GitHub account and `gh` signed in (see the notebook's top box).

### Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/continuous-integration/add-a-first-ci-job.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/continuous-integration/add-a-first-ci-job.ipynb)) and run each cell in order, top to bottom. You also need a GitHub account and `gh` signed in (see [github-authenticate](../version-control/github-authenticate.md)).

### What you should see

You create a small repository, add a workflow, and see a green tick on GitHub's **Actions** tab. Then you break the code on purpose and see a red cross. The notebook says what each command should print.

> **Picture to add:** the Actions tab of the practice repository with a green run (save a screenshot of the finished first job) (save as assets/overview.png)

### Where the files are

- `lessons/continuous-integration/add-a-first-ci-job.ipynb` and `.md`: the first CI job. **Needs a GitHub account and `gh` signed in.**
- `lessons/continuous-integration/publish-an-image-with-actions.ipynb` and `.md`: publish an image to GHCR. **Needs a GitHub account, `gh` signed in and Podman.**
- `lessons/continuous-integration/github-actions-for-maintenance-testing.ipynb` and `.md`: the maintenance-testing workflows to read.
- `.github/workflows/docs.yml` and `.github/workflows/ci.yml` in the repository: the two real workflows this course uses.
- `lessons/continuous-integration/assets/`: pictures for this lesson.

## Steps to execute

1. [`add-a-first-ci-job.md`](add-a-first-ci-job.md) — make a repository, add a check, watch it pass, then fail (needs a GitHub account and `gh` signed in)
2. [`publish-an-image-with-actions.md`](publish-an-image-with-actions.md) — build an image with Podman on GitHub and publish it to the GitHub Container Registry (needs a GitHub account, `gh` signed in and Podman)
3. [`github-actions-for-maintenance-testing.md`](github-actions-for-maintenance-testing.md) — read the workflows that keep a pipeline and its container images up to date

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what a GitHub Actions workflow is, and what `on`, `jobs`, `steps`, `uses` and `run` mean. Use a workflow that runs `ruff check .` as the example.
```

**Ask it to build.**

```text
Write a GitHub Actions workflow file that, on every push to main that changes files under container/, builds the Dockerfile in container/<name>/ with Podman and pushes it to ghcr.io/<owner>/<repo>/<name>, tagged with the commit hash. Use the least permissions needed, take the token from GITHUB_TOKEN, and make the image name lower case. Explain each line.
```

**Ask it to review.**

```text
Review this workflow for safety and repeatability. Check the permissions are the least needed, no secret is printed, versions of actions are pinned, and the image is tagged by something that never changes. List each problem and a fix.

<paste workflow>
```


## Further reading

- [GitHub Actions documentation](https://docs.github.com/en/actions) and [workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
- [Actions marketplace](https://github.com/marketplace?type=actions).
- [`actions/checkout`](https://github.com/actions/checkout), [`actions/setup-python`](https://github.com/actions/setup-python) and [`docker/build-push-action`](https://github.com/docker/build-push-action): the three you will use most.
- [Publishing to GitHub Pages from Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow): the pattern `docs.yml` uses.

## Supplementary information

### Why CI

The rule from [The Rules](../elements-of-style-rules/README.md):

> **Fail fast.** The sooner you find the broken thing, the cheaper it is to fix.

CI runs your tests, linters and builds automatically on every commit. You find broken things minutes after you wrote them, not a month later when a collaborator hits them.

### The anatomy of a workflow

A workflow is a file in `.github/workflows/*.yml`. The shape is always the same:

```yaml
name: What this workflow is called

on:                          # when to run
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:                     # one or more jobs (they run in parallel by default)
    runs-on: ubuntu-latest   # what OS to run on
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest
```

1. **`on:`** is the trigger: a push, a pull request, a button, or a schedule.
2. **`jobs:`** are units of work. Each job gets its own fresh machine.
3. **`steps:`** are the ordered actions inside a job. `uses:` pulls a ready-made action. `run:` runs a shell command.

### The two workflows in this repository

- **`.github/workflows/docs.yml`** builds the Sphinx site and deploys it to GitHub Pages on every push to `main`. It takes about two minutes. See [documentation](../documentation/README.md) for the file.
- **`.github/workflows/ci.yml`** checks that the notebooks parse, the Dockerfiles lint, and the R and Python code has no syntax errors. It runs on every push and pull request. It does not deploy.

### Marketplace actions

`uses: actions/checkout@v4` pulls a ready-made action from the [GitHub Actions marketplace](https://github.com/marketplace?type=actions). Pin the version (the `@v4`) so your builds do not change when an action updates.

| Action | What it does |
|--------|--------------|
| `actions/checkout@v4` | Clone the repository into the runner |
| `actions/setup-python@v5` | Install a specific Python version |
| `actions/setup-r@v2` | Install R |
| `docker/build-push-action@v5` | Build and push a container image |
| `hadolint/hadolint-action@v3` | Lint Dockerfiles |
| `actions/upload-pages-artifact@v3` | Package files for GitHub Pages |
| `actions/deploy-pages@v4` | Deploy to GitHub Pages |

### Secrets

Never commit passwords, API keys or tokens. Put them in **Settings → Secrets and variables → Actions** on the repository. Use them in a workflow as `${{ secrets.MY_TOKEN }}`. `GITHUB_TOKEN` is provided by GitHub automatically, so pushing a container to your own repository's registry needs no setup:

```yaml
- uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
```

### Add a new job

To add an R-lint job to `ci.yml`:

```yaml
  lint_r:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: r-lib/actions/setup-r@v2
      - run: Rscript -e 'lintr::lint_dir("R/")'
```

Push, watch the **Actions** tab, and repeat.

### Debugging a failing workflow

- The **Actions** tab shows every run. Click one to read the log of each step.
- Add `- run: echo "debug info"` steps to print values you are curious about.
- [`act`](https://github.com/nektos/act) runs workflows on your own computer.

## Next

[Documentation](../documentation/README.md): build a Sphinx site, then publish it with GitHub Actions.
