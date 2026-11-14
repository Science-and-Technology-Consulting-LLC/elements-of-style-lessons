# Continuous integration

*In the book: Section 4.5, Continuous Integration with GitHub Actions.*

This lesson shows you how to make GitHub check your work automatically on every push, so broken things are found in minutes. You will add a first check to a new repository and read the real workflows that keep this course working.

## Before you start

Do [documentation](../documentation/README.md) first. For the first notebook you also need a GitHub account and `gh` signed in (see the notebook's top box).

## Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/continuous-integration/add-a-first-ci-job.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/continuous-integration/add-a-first-ci-job.ipynb)) and run each cell in order, top to bottom. You also need a GitHub account and `gh` signed in (see [github-authenticate](../version-control/github-authenticate.md)).

## What you should see

You create a small repository, add a workflow, and see a green tick on GitHub's **Actions** tab. Then you break the code on purpose and see a red cross. The notebook says what each command should print.

> **Picture to add:** the Actions tab of the practice repository with a green run (save a screenshot of the finished first job) (save as assets/overview.png)

## Where the files are

- `lessons/continuous-integration/add-a-first-ci-job.ipynb` and `.md`: the first CI job. **Needs a GitHub account and `gh` signed in.**
- `lessons/continuous-integration/github-actions-for-maintenance-testing.ipynb` and `.md`: the maintenance-testing workflows to read.
- `.github/workflows/docs.yml` and `.github/workflows/ci.yml` in the repository: the two real workflows this course uses.
- `lessons/continuous-integration/assets/`: pictures for this lesson.

## Notebooks in order

1. [`add-a-first-ci-job.md`](add-a-first-ci-job.md) — make a repository, add a check, watch it pass, then fail (needs a GitHub account and `gh` signed in)
2. [`github-actions-for-maintenance-testing.md`](github-actions-for-maintenance-testing.md) — read the workflows that keep a pipeline and its Docker images up to date

## Next

[Federated computing](../federated-computing/README.md): take the containers, workflows and CI you have built and run them across institutions.

## Background

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

### Further reading

- Scheuermann RH, Deslattes Mays A, Diller M, LeClair R, Spear W, Zhang Y. *A trustworthy data-driven biomedical knowledge base of cell phenotypes for the National Library of Medicine.* In **Knowledge Graphs in U.S. Government Agencies**. Springer, forthcoming. The reference frame for the [NLM-CKN](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/nlm-ckn/README.md) case study.
- [GitHub Actions documentation](https://docs.github.com/en/actions) and [workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
- [Actions marketplace](https://github.com/marketplace?type=actions).
- [`actions/checkout`](https://github.com/actions/checkout), [`actions/setup-python`](https://github.com/actions/setup-python) and [`docker/build-push-action`](https://github.com/docker/build-push-action): the three you will use most.
- [Publishing to GitHub Pages from Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow): the pattern `docs.yml` uses.
