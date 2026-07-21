# Continuous integration

> *In the book: Chapter 12 — Continuous integration.*

:::{admonition} What you'll learn
:class: tip

- What continuous integration (CI) is and why every repo should have
  some form of it.
- The anatomy of a GitHub Actions workflow file.
- The two CI workflows in this repo — `docs.yml` (build + deploy the
  site) and `ci.yml` (validate notebooks, lint Dockerfiles, parse R and
  Python).
- How to add a new job, use a marketplace action, and manage secrets
  safely.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*A screenshot will land at `assets/overview.png` showing the Actions
tab of this repo with a green build. Reference it as
`![overview](assets/overview.png){width=520}` once captured.*
:::

## Why CI

The rule from [The Rules](elements-of-style-rules.md):

> **Fail fast.** The sooner you find the broken thing, the cheaper it
> is to fix.

CI runs your tests, your linters, your builds — automatically, on
every commit. You find broken things when they are cheap to fix
(minutes after you wrote them), not when a collaborator hits them a
month later.

## The anatomy of a workflow

Every GitHub Actions workflow lives in `.github/workflows/*.yml`. The
shape is always the same:

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

Three things to notice:

1. **`on:`** — the trigger. Push to `main`, pull requests, manual
   dispatch, scheduled cron — you pick.
2. **`jobs:`** — units of work. Each job gets its own fresh VM.
3. **`steps:`** — inside a job, ordered actions. `uses:` pulls a
   marketplace action; `run:` runs a shell command.

## The two workflows in this repo

### `.github/workflows/docs.yml`

Builds the Sphinx site and deploys it to GitHub Pages. Fires on every
push to `main`. About two minutes end-to-end.

```yaml
name: Build and Deploy Sphinx Documentation

on:
  push:
    branches: [main]

permissions:
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: pip install sphinx sphinx-rtd-theme myst-parser myst-nb sphinx-copybutton sphinx-design linkify-it-py
      - run: sphinx-build -W -b html docs/source docs/build/html
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs/build/html
      - uses: actions/deploy-pages@v4
```

### `.github/workflows/ci.yml`

Validates that the notebooks parse, the Dockerfiles lint, and the R /
Python code doesn't have syntax errors. Fires on every push and pull
request. No deploy — just validation.

## Marketplace actions

`uses: actions/checkout@v4` pulls a pre-built action from the
[GitHub Actions marketplace](https://github.com/marketplace?type=actions).
Pin the version (the `@v4`) so builds don't drift when an action
updates.

Common actions you'll reach for:

| Action | What it does |
|--------|--------------|
| `actions/checkout@v4` | Clone the repo into the runner |
| `actions/setup-python@v5` | Install a specific Python version |
| `actions/setup-r@v2` | Install R |
| `docker/build-push-action@v5` | Build and push a container image |
| `hadolint/hadolint-action@v3` | Lint Dockerfiles |
| `actions/upload-pages-artifact@v3` | Package for GitHub Pages deploy |
| `actions/deploy-pages@v4` | Deploy to GitHub Pages |

## Secrets

Never commit passwords, API keys, or tokens. Put them in
**Settings → Secrets and variables → Actions** on the repo. Reference
them in a workflow as `${{ secrets.MY_TOKEN }}`.

For pushing containers to a registry:

```yaml
- uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
```

`GITHUB_TOKEN` is provided automatically by GitHub — no configuration
needed for the common case of pushing to your own repo's registry.

## Add a new job

To add, e.g., an R-lint job to `ci.yml`:

```yaml
  lint_r:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: r-lib/actions/setup-r@v2
      - run: Rscript -e 'lintr::lint_dir("R/")'
```

Push, watch the Actions tab, iterate.

## Debugging a failing workflow

- The **Actions** tab shows every run, click one to see logs per step.
- Add `- run: echo "debug info"` steps to print variables you're
  curious about.
- Use `act` (a local CLI) to run workflows on your laptop:
  <https://github.com/nektos/act>.

## Further reading

- [GitHub Actions documentation](https://docs.github.com/en/actions) —
  authoritative reference.
- [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) —
  every field you can put in a `.yml`.
- [Actions marketplace](https://github.com/marketplace?type=actions) —
  browse ready-made actions.
- [`actions/checkout`](https://github.com/actions/checkout),
  [`actions/setup-python`](https://github.com/actions/setup-python),
  [`docker/build-push-action`](https://github.com/docker/build-push-action) —
  the three you'll use most.
- [nektos/act](https://github.com/nektos/act) — run GitHub Actions
  locally for faster iteration.
- [Publishing to GitHub Pages from Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) —
  the pattern this repo's `docs.yml` uses.

## Where to next

→ [Federated computing](federated-computing.md) — take the
containers + workflows + CI you've built and run them across
institutions.
