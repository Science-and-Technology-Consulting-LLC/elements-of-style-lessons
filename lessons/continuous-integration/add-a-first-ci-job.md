# Add a first CI job to an empty repo

**This walkthrough needs a GitHub account and the GitHub command-line tool (`gh`) signed in to it.** It creates a real repository on your GitHub account. If you have not done that yet, do the setup in the box under **What you need** first.

You will make a tiny repository, add a workflow that checks your Python code every time you push, and watch it pass and then fail. This matters because *continuous integration* (CI) means a computer re-checks your work on every change, so you find mistakes in minutes instead of months.

*Part of the [continuous-integration](README.md) lesson.*

## Start here

### What you will do

- Create a small repository on your computer and on GitHub.
- Add a workflow file that runs a Python style check on every push.
- Watch the check pass on GitHub's **Actions** tab.
- Break the code on purpose and watch the check fail.

### What you need

- A [GitHub account](https://github.com/signup) (free).
- The [GitHub CLI (`gh`)](https://cli.github.com/), installed and signed in. Sign in once with `gh auth login`; see [github-authenticate](../version-control/github-authenticate.md). Check with `gh auth status`.
- [Git](https://git-scm.com/), installed and set up with your name and email. See [why-git-and-setup](../version-control/why-git-and-setup.md).
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).
- [JupyterLab](https://jupyter.org/) with a Bash kernel. The "Check your setup" section below covers the kernel.

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`add-a-first-ci-job.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/continuous-integration/add-a-first-ci-job.ipynb) and run each cell in order, top to bottom.

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Confirm you are signed in to GitHub

Why: *Commit and push the workflow* creates a repository on GitHub. It fails if `gh` does not know who you are. Run this in a terminal (it also works in a notebook cell):

```text
gh auth status
```

**What you should see:** a line that says `Logged in to github.com` followed by your GitHub user name. If it says you are not logged in, run `gh auth login` and follow the prompts, or follow [github-authenticate](../version-control/github-authenticate.md).

### Make the repository

Why: CI needs a repository on GitHub to run in. This cell makes a folder called `hello-ci` in `~/eos-practice`, turns it into a Git repository, adds one Python file, saves ("commits") it, and creates a public repository with the same name on your GitHub account. `git init` starts tracking a folder. `git commit` saves a snapshot. `gh repo create` makes the copy on GitHub and `--push` uploads your snapshot to it.

```bash
mkdir -p ~/eos-practice/hello-ci
cd ~/eos-practice/hello-ci
git init -b main
echo "print('hello')" > hello.py
git add . && git commit -m "seed"
gh repo create hello-ci --public --source=. --push
```

**What you should see:** a few lines from Git, for example one that starts with `[main` and ends with `seed`, then lines from `gh` that say it created the repository and show its address, such as `https://github.com/<your-name>/hello-ci`. The exact lines depend on your versions.

> **Check:** the earlier run of this cell was done in a folder that already held a Git repository, so its output did not show a clean first run. Rerun it from a fresh `~/eos-practice` to confirm the exact lines.

### Look at the workflow

Why: a *workflow* is a recipe that GitHub follows on its own computer. It lives in `.github/workflows/`. This one runs whenever you push to `main` or open a pull request (a request to merge changes). It installs Python and [ruff](https://docs.astral.sh/ruff/) (a program that checks Python style), then runs `ruff check .`.

The next cell writes this file for you:

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install ruff
      - run: ruff check .
```

Run the cell to write the file:

```bash
mkdir -p .github/workflows
cat > .github/workflows/ci.yml <<'EOF'
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install ruff
      - run: ruff check .
EOF
```

**What you should see:** nothing. To check, run `ls .github/workflows` in a terminal opened in `~/eos-practice/hello-ci`. You should see `ci.yml`.

### Commit and push the workflow

Why: GitHub only runs workflows it has received. `git add` chooses the file, `git commit` saves it, and `git push` uploads it.

```bash
git add .github/workflows/ci.yml
git commit -m "add first CI job"
git push
```

**What you should see:** Git lists one new file, then `git push` prints lines that end with `main -> main`. That means GitHub has your workflow.

### Watch the run

Why: this is the payoff. GitHub starts the check the moment the push arrives.

1. Open your repository on GitHub: `https://github.com/<your-name>/hello-ci`.
2. Click the **Actions** tab.
3. Click the newest run, named `add first CI job`.

**What you should see:** the job takes about 30 seconds. A green tick means the check passed.

> **Picture to add:** the Actions tab with one green run named "add first CI job" (save as assets/add-a-first-ci-job-step-5.png)

### Break it on purpose

Why: a check you have never seen fail is a check you cannot trust. This cell adds a line of messy Python to `hello.py` and pushes it.

```bash
echo "import os,sys;print('bad style')" >> hello.py
git commit -am "on purpose"
git push
```

**What you should see:** the push succeeds. On the **Actions** tab a new run appears and turns red. Click it, then the failed step, to read the message from `ruff`. It names the file and the line it dislikes.

> **Picture to add:** the Actions tab showing the red failed run and the ruff error in the log (save as assets/add-a-first-ci-job-step-6.png)

### Fix it and see green again

Why: this is the whole loop: push, fail, fix, pass. In a terminal in `~/eos-practice/hello-ci`, open `hello.py`, delete the last line (`import os,sys;print('bad style')`), then run:

```text
git commit -am "fix style"
git push
```

**What you should see:** a new run on the **Actions** tab that ends with a green tick. That is the feedback loop CI gives you: cheap, fast and honest.

When you are done, you can delete the practice repository on GitHub: open it, choose **Settings**, scroll to the bottom and choose **Delete this repository**.

### If something goes wrong

- **`gh: command not found`, or `gh repo create` says you are not logged in.** Install [gh](https://cli.github.com/) and run `gh auth login`. See [github-authenticate](../version-control/github-authenticate.md).
- **`Author identity unknown` or `Please tell me who you are` from `git commit`.** Git does not know your name. Run `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`, then run the cell again. See [why-git-and-setup](../version-control/why-git-and-setup.md).
- **`mkdir` or `git init` complains that the folder exists, or `gh repo create` says the repository name is taken.** You ran *Commit and push the workflow* before. Pick another name in place of `hello-ci` in the cell, or delete the old practice repository first.
- **Nothing appears on the Actions tab.** The workflow file is not on GitHub yet. Run *Break it on purpose* again and check that the file is at `.github/workflows/ci.yml` (a folder that starts with a dot).

## Next

[Publish a container image with GitHub Actions](publish-an-image-with-actions.md): build and publish an image on every push. Or return to the [continuous-integration lesson](README.md).
