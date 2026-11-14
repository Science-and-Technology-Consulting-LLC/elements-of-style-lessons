# Version control with Git

> *In the book: Sections 4.1 to 4.4, Code Versioning.*

This lesson gives you a Git and GitHub routine, so your code is no longer one fragile copy on one laptop but a saved, shareable history you can recover.

## Before you start

None. This is the first lesson after the course introduction. You need a free [GitHub account](https://github.com/signup).

## Do this

1. **Clone the course.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the first notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Open `lessons/version-control/why-git-and-setup.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/version-control/why-git-and-setup.ipynb)). Run each cell in order, top to bottom.

Then work through the other notebooks, in this order:

1. [why-git-and-setup.md](why-git-and-setup.md): why Git and GitHub, and one-time setup (`nano`, `conda`, `gh`, `git config`).
2. [workspace-setup.md](workspace-setup.md): check your computer and start JupyterLab.
3. [github-authenticate.md](github-authenticate.md): make a Personal Access Token and sign in with `gh auth login`.
4. [the-add-push-git-routine.md](the-add-push-git-routine.md): the daily edit, status, add, commit, push and pull request loop.
5. [keeping-your-repository-fork-in-sync.md](keeping-your-repository-fork-in-sync.md): fork, clone, and keep a fork up to date with the original.

## What you should see

- Git installed, with your name and email set.
- The GitHub CLI (`gh`) installed and signed in.
- One change of yours on GitHub, sent by `git push`, and a pull request offering it to the original project.
- A fork that matches the original project after you sync it.

> **Picture to add:** your fork's page on GitHub showing your commit on `README.md` (save as assets/overview.png)

## Where the files are

All files are in `lessons/version-control/` of the [course repository](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/version-control). Each walkthrough is a notebook (`.ipynb`) with a web page copy (`.md`). The longer reference is [git-survival-guide.md](git-survival-guide.md).

## Next

[Reproducible environments with Conda](../conda-environments/README.md)

## Background

### What Git is

Git is a small program that watches a folder and remembers every snapshot you tell it to remember. The folder is a **repository** (repo). A snapshot is a **commit**. The history of commits is your project's memory. GitHub is a website that hosts repos. Git works without GitHub, but GitHub is where most collaboration happens.

### Install or check Git

The full install steps are in the [command-line-and-git-bash lesson](../command-line-and-git-bash/README.md).

- **macOS:** Git is not pre-installed. Type `git --version` in Terminal. A window offers to install the Xcode Command Line Tools. Accept it.
- **Windows:** Git comes with the [Git for Windows](https://gitforwindows.org/) installer, which also gives you Git Bash.

### Tell Git who you are (first time only)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the same email you use on GitHub. Git stamps it on every commit.

### A repo from scratch, in seven moves

```bash
cd ~/eos-practice/day-1
git init                 # 1. turn this folder into a Git repo
git status               # 2. see what Git sees
git add notes.md         # 3. tell Git to track this file
git status               # look again: notes.md is now "staged"
git commit -m "first notes"   # 4. snapshot the staged changes
git log                  # 5. show the history (q to quit)
```

Edit the file, then:

```bash
echo "another line" >> notes.md
git diff                 # 6. show what changed since the last commit
git add notes.md
git commit -m "add another line"   # 7. snapshot again
```

The loop is: edit, add, commit, repeat.

> **Check:** The original page said "Pick up where Step 1 left off" and used the folder `~/elements-of-style-practice/day-1`. The other lessons use `~/eos-practice`. Is `day-1` created in an earlier lesson? Here it is shown with `~/eos-practice`.

### Putting it on GitHub

1. On [github.com](https://github.com), create a new empty repo. Do not add a README, because your local repo already has files.
2. Copy the web address GitHub shows, for example `https://github.com/yourname/day-1.git`.
3. In your terminal:

   ```bash
   git remote add origin https://github.com/yourname/day-1.git
   git branch -M main
   git push -u origin main
   ```

Refresh GitHub. Your file is there. Make another local commit, run `git push`, and watch GitHub catch up.

### The seven commands you will use most

| Command | Use it when |
|---------|-------------|
| `git status` | Anytime: "what is the state of my repo?" |
| `git add <file>` | Telling Git to include this in the next snapshot |
| `git commit -m "..."` | Taking the snapshot |
| `git log` | "What did I or my collaborator change recently?" |
| `git diff` | "What is different from the last commit?" |
| `git push` | "Send my commits up to GitHub" |
| `git pull` | "Bring down anything new from GitHub" |

### If you cannot `git pull` directly

On the All of Us Researcher Workbench and similar platforms you cannot `git pull` directly. Still version your code locally. The Bridge patterns page shows how to keep work versioned when copy and paste is the only way across.

> **Check:** The original linked this to `../../bridges/index.md`. That page is not in this folder tree. Where does it live now?

### Going deeper

The [Git survival guide](git-survival-guide.md) covers branches, forks, several remotes and untangling mistakes. Read it when you meet a situation this page does not cover.

### Further reading

- Scheuermann RH, Deslattes Mays A, Diller M, LeClair R, Spear W, Zhang Y. *A trustworthy data-driven biomedical knowledge base of cell phenotypes for the National Library of Medicine.* In **Knowledge Graphs in U.S. Government Agencies**. Springer, forthcoming. This is the reference frame for the [NLM-CKN](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/nlm-ckn/README.md) case study.
- [Pro Git book](https://git-scm.com/book/en/v2) by Scott Chacon, free
- [GitHub Docs](https://docs.github.com/) for the platform side (pull requests, issues, Actions)
- [GitHub CLI manual](https://cli.github.com/manual/): `gh` command reference
- [GitHub Skills](https://skills.github.com/): interactive courses
- [Learn Git Branching](https://learngitbranching.js.org/): visual tutorial
