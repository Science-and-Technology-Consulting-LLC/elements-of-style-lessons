# Publish your Sphinx site with GitHub Actions

**This walkthrough needs a GitHub account and the GitHub command-line tool (`gh`) signed in to it.** It creates a real repository and a real web site on your GitHub account.

You will put a small Sphinx site in a repository, and let GitHub rebuild and publish it every time you push. This matters because the documentation then never falls behind the code, and a broken link stops the publish instead of reaching your readers.

*Part of the [documentation](README.md) lesson.*

## Start here

### What you will do

- Make a small Sphinx site in a new repository.
- Turn on GitHub Pages for the repository.
- Add a workflow that builds the site and publishes it on every push.
- Break a link on purpose, watch the build stop, and fix it.

### What you need

- A [GitHub account](https://github.com/signup) (free).
- The [GitHub CLI (`gh`)](https://cli.github.com/), installed and signed in. See [github-authenticate](../version-control/github-authenticate.md). Check with `gh auth status`.
- [Git](https://git-scm.com/), set up with your name and email. See [why-git-and-setup](../version-control/why-git-and-setup.md).
- The `eos` environment from [conda-environments](../conda-environments/README.md), active in the terminal where you start JupyterLab.
- The ideas in [building-a-sphinx-site](building-a-sphinx-site.md) and in [add-a-first-ci-job](../continuous-integration/add-a-first-ci-job.md). You can do this lesson without them, but they explain what happens here.
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`publish-your-site-with-actions.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/documentation/publish-your-site-with-actions.ipynb) and run each cell in order, top to bottom.

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git`, `gh` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the six setup steps on the [Introduction page](../introduction/README.md) and the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md) first.

> **Check:** I wrote this lesson without running it. It needs a GitHub login. Please run it once from a fresh `~/eos-practice` and tell me what differs.

## Steps to execute

### Confirm you are signed in to GitHub

Why: *Create the repository and push the site* makes a repository on GitHub. It fails if `gh` does not know who you are.

```bash
gh auth status
```

**What you should see:** a line that says `Logged in to github.com` followed by your GitHub user name. If not, run `gh auth login`, or follow [github-authenticate](../version-control/github-authenticate.md).

### Install Sphinx and its add-ons

Why: [Sphinx](https://www.sphinx-doc.org/) turns text files into a web site. The version limits match the ones this course's own workflow uses, because newer releases of the add-ons broke each other for a while.

```bash
pip install "sphinx>=7,<7.3" sphinx-rtd-theme "myst-parser>=2,<4" "myst-nb<1.2" \
            sphinx-copybutton sphinx-design linkify-it-py
```

**What you should see:** many lines of text that end with `Successfully installed`, or only `already satisfied` lines. A line that starts with `ERROR` is a problem (see below).

### Make the site in a new folder

Why: the site lives in a folder of its own, `hello-docs`, in `~/eos-practice`. Keeping it away from the course folder means you cannot overwrite the course's own `docs`. The three files are the settings (`conf.py`), a home page and one more page.

````bash
mkdir -p ~/eos-practice/hello-docs/docs/source
cd ~/eos-practice/hello-docs
cat > docs/source/conf.py <<'EOF'
project = "Hello Docs"
author = "Your Name"
extensions = ["myst_nb", "sphinx_copybutton", "sphinx_design"]
myst_enable_extensions = ["colon_fence", "deflist", "linkify"]
html_theme = "sphinx_rtd_theme"
EOF
cat > docs/source/index.md <<'EOF'
# Hello Docs

Welcome.

```{toctree}
:maxdepth: 2

intro
```
EOF
cat > docs/source/intro.md <<'EOF'
# Intro

First page.
EOF
ls docs/source
````

**What you should see:** the three file names, `conf.py`, `index.md` and `intro.md`.

### Build the site on your computer

Why: build it here first. The `-W` option turns every warning into an error, so a broken link stops the build. A failure on your computer is quicker to read than one on GitHub.

```bash
sphinx-build -W -b html docs/source docs/build/html
```

**What you should see:** a stream of lines. The last two are `build succeeded.` and `The HTML pages are in docs/build/html.`

### Create the repository and push the site

Why: GitHub Pages needs a repository to publish from. This cell saves ("commits") the site files and creates a public repository `hello-docs` on your GitHub account. The built pages in `docs/build` are left out, because GitHub will build its own.

```bash
echo "docs/build/" > .gitignore
git init -b main
git add .
git commit -m "first Sphinx site"
gh repo create hello-docs --public --source=. --push
```

**What you should see:** lines from Git that include `first Sphinx site`, then lines from `gh` that show the new repository's address, such as `https://github.com/<your-name>/hello-docs`.

### Turn on GitHub Pages

Why: GitHub publishes a site only after you tell it to. Do this now, before the workflow exists, so the first workflow run has somewhere to publish.

1. Open `https://github.com/<your-name>/hello-docs`.
2. Click **Settings**, then **Pages** in the left menu.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.

**What you should see:** the **Source** box shows *GitHub Actions*. There is nothing else to click.

> **Picture to add:** the Settings, Pages screen with Source set to GitHub Actions (save as assets/publish-your-site-with-actions-step-6.png)

> **Check:** the menu names above are from memory of GitHub's current pages. Please confirm them and correct any that have moved.

### Look at the workflow

Why: a *workflow* is a recipe that GitHub follows on its own computer. This one has two jobs. `build` installs Sphinx and builds the site, and fails on any warning. `deploy` runs only after `build` succeeds and only on a push to `main`, and it publishes the pages. A pull request runs `build` alone, so a broken change is caught before it is merged.

- `permissions:` give the run the right to publish to Pages.
- `concurrency:` makes two publishes queue instead of racing.
- The `if:` lines keep the publish steps off pull requests.

The next cell writes this file for you:

```yaml
name: Deploy docs
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: false
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: |
          pip install "sphinx>=7,<7.3" sphinx-rtd-theme "myst-parser>=2,<4" "myst-nb<1.2" \
                      sphinx-copybutton sphinx-design linkify-it-py
      - run: sphinx-build -W -b html docs/source docs/build/html
      - if: github.event_name == 'push'
        uses: actions/upload-pages-artifact@v3
        with: { path: docs/build/html }
  deploy:
    if: github.event_name == 'push'
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

### Write the workflow file and push it

Why: GitHub only runs workflows it finds in `.github/workflows/`. The folder name starts with a dot. The push starts the first run.

```bash
mkdir -p .github/workflows
cat > .github/workflows/docs.yml <<'EOF'
name: Deploy docs
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: false
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: |
          pip install "sphinx>=7,<7.3" sphinx-rtd-theme "myst-parser>=2,<4" "myst-nb<1.2" \
                      sphinx-copybutton sphinx-design linkify-it-py
      - run: sphinx-build -W -b html docs/source docs/build/html
      - if: github.event_name == 'push'
        uses: actions/upload-pages-artifact@v3
        with: { path: docs/build/html }
  deploy:
    if: github.event_name == 'push'
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
EOF
git add .github/workflows/docs.yml
git commit -m "publish the site with Actions"
git push
```

**What you should see:** Git lists one new file, then `git push` prints lines that end with `main -> main`.

### Watch the run and open the site

Why: this is the payoff. GitHub builds your site and puts it on the web.

1. Open the repository and click the **Actions** tab.
2. Click the newest run, named `publish the site with Actions`.
3. Wait for both jobs, `build` and `deploy`, to show a green tick. This takes about two minutes.
4. Open `https://<your-name>.github.io/hello-docs/`.

**What you should see:** a page titled *Hello Docs* in the Read the Docs look, with *Intro* in the left menu.

> **Picture to add:** the Actions run with the build and deploy jobs both green (save as assets/publish-your-site-with-actions-step-9.png)

> **Picture to add:** the published Hello Docs home page in a browser (save as assets/publish-your-site-with-actions-step-9b.png)

### Break a link on purpose

Why: a check you have never seen fail is a check you cannot trust. This cell adds a link to a page that does not exist. With `-W` the build stops, and the old site stays up.

```bash
echo "See the [missing page](nowhere.md)." >> docs/source/intro.md
git commit -am "break a link on purpose"
git push
```

**What you should see:** the push works. On the **Actions** tab a new run turns red at the `sphinx-build` step. Click the failed step. The message names `intro.md` and the target `nowhere.md`. The published site is unchanged, because `deploy` never started.

> **Picture to add:** the red run with the sphinx-build error naming nowhere.md (save as assets/publish-your-site-with-actions-step-10.png)

### Fix it and see green again

Why: this is the whole loop: push, fail, fix, publish. The cell removes the line you added to `intro.md`.

```bash
grep -v 'missing page' docs/source/intro.md > intro.tmp && mv intro.tmp docs/source/intro.md
git commit -am "fix the link"
git push
```

**What you should see:** a new run that ends green, and the site is published again. When you finish, you can delete the practice repository: open it, choose **Settings**, scroll to the bottom and choose **Delete this repository**.

### If something goes wrong

- **`sphinx-build: command not found`.** The install went into a different Python. Run `conda activate eos` in the terminal, start JupyterLab from there, and run the install cell again.
- **The `deploy` job fails with `Get Pages site failed` or *Not Found*.** Pages is not turned on for the repository. Do *Turn on GitHub Pages*, then open the failed run and choose **Re-run all jobs**.
- **The build fails on your computer with `WARNING`.** Read the line above `build finished with problems`. It names the file and the problem, usually a link or a heading.
- **`gh repo create` says the repository name is taken.** You ran *Create the repository and push the site* before. Choose another name in place of `hello-docs`, or delete the old practice repository first.
- **The site opens with a 404 error.** The first deploy takes a minute or two. Wait, then reload. Check that the `deploy` job is green.

## Supplementary information

### Pins in the workflow

The `pip install` line holds Sphinx at 7.2 and the MyST add-ons at the versions that work with it. This course's own workflow, `.github/workflows/docs.yml`, does the same and says why in a comment.

### Pull requests

The workflow builds on every pull request but publishes only on `main`. That is the point of the `if:` lines: reviewers see a red tick when a change breaks the build, and nothing reaches the public site until it is merged.

### The same pattern for this course

The course site you are reading is built by [`docs.yml`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/.github/workflows/docs.yml) in the course repository. It has the same two jobs, with a few extras for the notebooks.

## Next

[Introduction to Nextflow](../nextflow-workflows/README.md): put your tools, containers and documentation to work in a pipeline.
