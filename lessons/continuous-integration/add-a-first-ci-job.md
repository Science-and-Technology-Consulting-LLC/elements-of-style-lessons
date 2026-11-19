# Add a first CI job to an empty repo

**This walkthrough creates a real repository on your GitHub account.** It needs a GitHub account and the GitHub command-line tool (`gh`) signed in to it.

We will make a tiny repository, add a workflow that checks your Python code every time you push, and watch it pass and then fail. *Continuous integration* (CI) means a computer re-checks your work on every change, so you find mistakes in minutes instead of months.

*Part of the [continuous-integration](README.md) lesson.*

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Containers](../containers/README.md), is done.
- A [GitHub account](https://github.com/signup) (free), and Git set up with your name and email. We did this in [Why Git, and setup](../version-control/why-git-and-setup.md).
- The [GitHub CLI (`gh`)](https://cli.github.com/), signed in. We did this in [github-authenticate](../version-control/github-authenticate.md).
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.

### What you will do

- Create a small repository on your computer and on GitHub.
- Add a workflow file that runs a Python style check on every push.
- Watch the check pass on GitHub's **Actions** tab.
- Break the code on purpose and watch the check fail.

## Steps to execute

### Confirm you are signed in to GitHub

Why: *Make the repository* creates a repository on GitHub. It fails if `gh` does not know who you are. Please run this in a terminal (it also works in a notebook cell):

```text
gh auth status
```

**What you should see:** a line that says `Logged in to github.com` followed by your GitHub user name. If it says you are not logged in, run `gh auth login` and follow the prompts, or follow [github-authenticate](../version-control/github-authenticate.md).

### Make the repository

Why: CI needs a repository on GitHub to run in. This cell makes a folder called `hello-ci` in `~/eos-practice`, adds one Python file, saves ("commits") it, and creates a public repository with the same name on your GitHub account. `git init` and `git commit` are from [Version control with Git](../version-control/README.md). `gh repo create` makes the copy on GitHub and `--push` uploads your snapshot to it.

```bash
mkdir -p ~/eos-practice/hello-ci
cd ~/eos-practice/hello-ci
git init -b main
echo "print('hello')" > hello.py
git add . && git commit -m "seed"
gh repo create hello-ci --public --source=. --push
```

**What you should see:** a few lines from Git, for example one that starts with `[main` and ends with `seed`, then lines from `gh` that show the new repository's address, such as `https://github.com/<your-name>/hello-ci`. The exact lines depend on your versions.

> **Check:** the earlier run of this cell was done in a folder that already held a Git repository, so its output did not show a clean first run. Rerun it from a fresh `~/eos-practice` to confirm the exact lines.

### Look at the workflow

Why: a *workflow* is a recipe that GitHub follows on its own computer. It lives in `.github/workflows/`. This one runs whenever you push to `main` or open a pull request (a request to merge changes). It installs Python and [ruff](https://docs.astral.sh/ruff/) (a program that checks Python style), then runs `ruff check .`. The parts of a workflow file are described in [The anatomy of a workflow](README.md#the-anatomy-of-a-workflow).

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

**What you should see:** nothing. To check, run `ls .github/workflows` in a terminal opened in `~/eos-practice/hello-ci`. You will see `ci.yml`.

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

Why: this is the whole loop: push, fail, fix, pass. In a terminal in `~/eos-practice/hello-ci`, open `hello.py` and delete the last line (`import os,sys;print('bad style')`). Then run:

```text
git commit -am "fix style"
git push
```

**What you should see:** a new run on the **Actions** tab that ends with a green tick. That is the feedback loop CI gives you: fast and honest.

When you are done, you can delete the practice repository on GitHub: open it, choose **Settings**, scroll to the bottom and choose **Delete this repository**.

### If something goes wrong

- **`gh: command not found`, or `gh repo create` says you are not logged in.** Install [gh](https://cli.github.com/) and run `gh auth login`, as in [github-authenticate](../version-control/github-authenticate.md).
- **`Author identity unknown` or `Please tell me who you are` from `git commit`.** Git does not know your name. Run `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`, then run the cell again. This is in [Why Git, and setup](../version-control/why-git-and-setup.md).
- **`mkdir` or `git init` complains that the folder exists, or `gh repo create` says the repository name is taken.** You ran *Make the repository* before. Pick another name in place of `hello-ci` in the cell, or delete the old practice repository first.
- **Nothing appears on the Actions tab.** The workflow file is not on GitHub yet. Run *Commit and push the workflow* again and check that the file is at `.github/workflows/ci.yml` (a folder that starts with a dot).

## Next

[Publish a container image with GitHub Actions](publish-an-image-with-actions.md): build and publish an image on every push. Or return to the [continuous-integration lesson](README.md).
