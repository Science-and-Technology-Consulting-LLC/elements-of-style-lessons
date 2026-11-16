# Keeping your repository fork in sync

You will catch your fork up with the original project when the original gets new changes. This matters because a fork does not update itself, and an old fork leads to conflicts.

**What you will do:**

- Learn four Git words: clone, fork, pull, push.
- Fork a project and clone your fork.
- Update your fork from the GitHub website.
- Update it from the terminal.

**What you need:**

- A free [GitHub account](https://github.com/signup).
- Git set up and `gh` signed in: [why-git-and-setup.md](why-git-and-setup.md) and [github-authenticate.md](github-authenticate.md).

## Start here

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`keeping-your-repository-fork-in-sync.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/version-control/keeping-your-repository-fork-in-sync.ipynb) and run each cell in order, top to bottom.


### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the six setup steps on the [Introduction page](../introduction/README.md) and the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Learn the four words

Four verbs come up again and again:

- **Clone**: make a working copy of a repository on your computer.
- **Fork**: make your own copy of someone else's repository on GitHub, one you will edit and may offer back.
- **Pull**: bring changes down, from GitHub into your local copy.
- **Push**: send your local changes up to GitHub.

**What you should see:** nothing. This step is reading only.

### Fork the practice project

You do this in a browser.

1. Open [NIH-NICHD/exampleVolcanoPlotNotebook](https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook).
2. Click **Fork** (top right, next to *Edit Pins* and *Watch*). Choose *your own* GitHub account as the owner.

> **Picture to add:** the repository page with the Fork button at the top right (save as assets/keeping-your-repository-fork-in-sync-step-2.png)

**What you should see:** a short "Forking" progress window. When it finishes, the page is named `<your-github-username>/exampleVolcanoPlotNotebook`. If you already forked it in [the-add-push-git-routine.md](the-add-push-git-routine.md), you can reuse that fork.

### Go to your practice folder

```bash
mkdir -p ~/eos-practice
cd ~/eos-practice
pwd
```

**What you should see:** one line ending in `eos-practice`.

### Clone your fork

This puts a working copy on the machine where you will edit. **Edit the next cell first**: replace `<your-github-username>` in the web address with your own. If you already cloned your fork in the last lesson, it is in `~/eos-practice/<your-github-username>/exampleVolcanoPlotNotebook`. Skip this step and `cd` into that folder instead.

```bash
git clone https://github.com/<your-github-username>/exampleVolcanoPlotNotebook.git
cd exampleVolcanoPlotNotebook
```

**What you should see:** `Cloning into 'exampleVolcanoPlotNotebook'...` and, at the end, `done.`.

### Sync from the GitHub website

Time passes. The original project (called **upstream**: `NIH-NICHD/exampleVolcanoPlotNotebook`) gets new commits. Your fork does not, until you sync it. The website is the easiest way.

1. Open your fork's page.
2. GitHub says your branch is "N commits behind NIH-NICHD/exampleVolcanoPlotNotebook:main".
3. Under the *Code* button area, click **Sync fork**, then **Update branch**.

> **Picture to add:** the "N commits behind" banner with the Sync fork button (save as assets/keeping-your-repository-fork-in-sync-step-5.png)

**What you should see:** GitHub reports that the branch was successfully fetched and fast-forwarded. Your fork now matches upstream `main`. If you have edited files on GitHub *and* on your computer, read the "stash" tip in the [Git survival guide](git-survival-guide.md) first.

### Tell your clone where upstream is

For terminal syncing, Git needs to know the address of the original project. You give it the name `upstream`. A **remote** is a named address of a copy of the project on GitHub. Your fork is already a remote named `origin`. The first cell adds `upstream`. The second lists all remotes.

```bash
git remote add upstream https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook.git
```

```bash
git remote -v
```

**What you should see:** four lines, two for `origin` (your fork) and two for `upstream`:

```
origin    https://github.com/<your-github-username>/exampleVolcanoPlotNotebook.git (fetch)
origin    https://github.com/<your-github-username>/exampleVolcanoPlotNotebook.git (push)
upstream  https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook.git (fetch)
upstream  https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook.git (push)
```

If `git remote add` says `remote upstream already exists`, it is already set. Go on.

### Sync from the terminal

This does the same job as the website button. The four commands in the next cell do this, in order:

- `git fetch upstream` downloads the new commits from the original project.
- `git checkout main` switches to your `main` branch (the main line of your work).
- `git merge upstream/main` combines the new commits into your `main`.
- `git push origin main` sends the result up to your fork.

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

**What you should see:** `Already up to date.` if there was nothing new. If there were new commits, Git lists the files that changed, and `git push` ends with `main -> main`.

### If something goes wrong

- **`'upstream' does not appear to be a git repository`.** You skipped *Tell your clone where upstream is*. Run the `git remote add upstream` cell, then try again.
- **A "merge conflict" message.** You and upstream changed the same lines. Do not panic. Nothing is lost. See the conflict section of the [Git survival guide](git-survival-guide.md).
- **`Permission denied` on push.** You are not signed in, or you cloned the original instead of your fork. Run `gh auth status`, and check the clone address has your user name.

## Next

Back to the [version-control lesson](README.md). Then [conda-environments](../conda-environments/README.md).
