# Version control with Git


> *In the book: Chapter 4 — Version control with Git.*

:::{admonition} What you'll learn
:class: tip

- Make a repo your code can survive in.
- The edit → add → commit → push loop.
- When (and how) to branch, and how to recover when you don't.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBDwill drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

Git is how your code stops being a single fragile copy on a single laptop and
starts being a versioned, shareable, recoverable thing. You don't need to
know every Git command — you need about seven, plus a feel for when to use
each one.

:::{admonition} A note before we begin
:class: tip

If you're on the **All of Us Researcher Workbench** or another platform that
doesn't let you `git pull` directly, **don't skip this step.** You still
benefit from versioning your code locally, and the
[Bridge patterns](../bridges/index.md) page shows you how to keep your work
versioned even when copy/paste is the only road across.
:::

## What Git actually is

Git is a small program that watches a folder and remembers every snapshot
you tell it to remember. The folder is a **repository** (repo). A snapshot
is a **commit**. The history of commits is your project's memory.

GitHub is a website that hosts repos. Git works perfectly well without
GitHub — but GitHub is where most collaboration happens.

## Install / verify Git

The full install walk-through is in the
[command line + Git Bash](command-line-and-git-bash.md) lesson. Quick
reminder of where `git` actually comes from:

- **macOS:** *not* pre-installed. Typing `git --version` on a fresh Mac
  pops up the Xcode Command Line Tools installer; accept it.
- **Windows:** comes bundled with the **Git for Windows** installer —
  the same installer that gives you Git Bash. If Git Bash launches,
  `git` is on PATH.
- **Lifebit:** pre-installed on every notebook server.

::::{tab-set}

:::{tab-item} macOS
:sync: mac

```bash
# Open Terminal.app, then:
git --version
# If you see "command not found", accept the macOS Command Line Tools
# install prompt; on a fresh Mac, the very same line triggers it.
```
:::

:::{tab-item} Windows (Git Bash)
:sync: win

```bash
# In Git Bash (which IS Git for Windows — same installer):
git --version
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# Lifebit notebook servers ship git pre-installed. Just confirm:
git --version
```
:::

::::

## The first time only — tell Git who you are

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the same email you use on GitHub. This metadata gets stamped on every
commit you make.

## A repo from scratch, in seven moves

Pick up where Step 1 left off:

```bash
cd ~/elements-of-style-practice/day-1
git init                 # 1. turn this folder into a Git repo
git status               # 2. see what Git sees
git add notes.md         # 3. tell Git "track this file"
git status               # (look again — notes.md is now "staged")
git commit -m "first notes"   # 4. snapshot the staged changes
git log                  # 5. show the history (q to quit)
```

You now have one commit. Edit the file, then:

```bash
echo "another line" >> notes.md
git diff                 # 6. show what changed since the last commit
git add notes.md
git commit -m "add another line"   # 7. snapshot again
```

That's the loop: **edit → add → commit → repeat.**

## Putting it on GitHub

1. Go to https://github.com and create a new empty repo (don't initialize
   it with a README — your local repo already has files).
2. Copy the URL GitHub shows you (something like
   `https://github.com/yourname/day-1.git`).
3. Back in your terminal:

   ```bash
   git remote add origin https://github.com/yourname/day-1.git
   git branch -M main
   git push -u origin main
   ```

Refresh GitHub — your file is now there. Make another local commit, then
`git push`, and watch GitHub catch up.

## The seven commands you'll use the most

| Command | Use it when |
|---------|-------------|
| `git status` | Anytime — "what's the state of my repo?" |
| `git add <file>` | Telling Git "include this in the next snapshot" |
| `git commit -m "..."` | Taking the snapshot |
| `git log` | "What did I (or my collaborator) change recently?" |
| `git diff` | "What's different from the last commit?" |
| `git push` | "Send my commits up to GitHub" |
| `git pull` | "Bring down anything new from GitHub" |

## Going deeper: the survival guide

This page gives you the floor. The ceiling — branches, forks, multi-remote
workflows, untangling mistakes — is in the full
**Git Survival Guide**, which lives in the book companion repo as
[`chapters/version-control-as-survival/01_git_survival_guide.md`](git-survival-guide.md).

Read it when you hit a situation this page doesn't cover.

## Further reading

- [Pro Git book](https://git-scm.com/book/en/v2) — Scott Chacon, free
- [GitHub Docs](https://docs.github.com/) — for the platform side (PRs, issues, Actions)
- [GitHub CLI manual](https://cli.github.com/manual/) — `gh` command reference
- [GitHub Skills](https://skills.github.com/) — interactive courses
- [Learn Git Branching](https://learngitbranching.js.org/) — visual tutorial


## Where to next

→ Next lesson: [Reproducible environments with Conda](conda-environments.md)
