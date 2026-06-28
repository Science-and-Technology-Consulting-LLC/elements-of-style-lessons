# The command line, with Git Bash


> *In the book: Chapter 3 — Command line + Git Bash.*

:::{admonition} What you'll learn
:class: tip

- Open a terminal that looks the same on Mac, Windows, and Lifebit.
- Ten commands that get you from lost to productive.
- How to read a command and ask `--help` for the rest.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

The terminal is the lingua franca of biomedical computing. Cloud platforms,
HPC clusters, containers — almost all of them want to talk to you in shell
commands. The good news: you only need about ten commands to start being
productive.

The slightly inconvenient news: the terminal looks a little different on
Windows and macOS by default. We solve that in one step.

:::{admonition} Why this step matters
:class: tip

Every later step assumes you can open a terminal, see where you are, list
what's around you, and run a command. If those four things feel comfortable,
the rest of the curriculum unlocks.
:::

## One terminal for everyone — install Git Bash

We're going to use a Bash shell as our terminal across all three platforms.
On Mac and Linux the built-in shell is already Bash (or zsh, which is close
enough). On Windows, the equivalent is **Git Bash** — which arrives as part
of the *Git for Windows* installer.

The point: when a colleague on Windows and a colleague on a Mac open their
terminals, they see the same prompts and run the same commands.

:::{important}
Neither macOS nor a stock Windows install ships with git already on it. You
have to install git once, the first time. The good news: on Windows that one
install also gives you the Bash shell, and on Mac the install can be triggered
by typing one command.
:::

**Windows — one installer for both git and the shell:**

1. Go to <https://git-scm.com/download/win> and download the installer.
2. Run it. Accept the defaults — they're sensible.
3. After install, find **Git Bash** in the Start menu and open it.

That's it. Git Bash *is* Git for Windows; you don't install them
separately. Confirm with `git --version`.

**macOS — Terminal first, then git:**

1. Open **Terminal.app** (Spotlight: `Cmd-Space`, type "Terminal", Return).
2. Type `git --version` and press Return.
3. If git isn't installed yet, macOS pops up an "Install Command Line
   Developer Tools" dialog. Click **Install**, accept the licence, wait a
   few minutes.
4. When the dialog finishes, run `git --version` again. You'll see a real
   version number.

(Alternatives if you'd rather: `brew install git` after installing
[Homebrew](https://brew.sh), or a standalone installer from
<https://git-scm.com/download/mac>.)

**Linux:** Bash is your default shell; `git` is one `apt install git` (or
`dnf install git`) away if it isn't already present.

## Open your terminal — three ways

::::{tab-set}

:::{tab-item} macOS
:sync: mac

```bash
# Spotlight: Cmd-Space, type "Terminal", hit Return.
# On a fresh Mac, `git --version` triggers the macOS dialog
# to install Xcode Command Line Tools — accept it. Once
# the install finishes, run the command again.
git --version
```
:::

:::{tab-item} Windows (Git Bash)
:sync: win

```bash
# Git for Windows installs BOTH git AND the Bash shell.
# Download: https://git-scm.com/download/win — accept the
# installer defaults — then open "Git Bash" from the Start menu.
# At that point git is already on PATH; just confirm:
git --version
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# On a Lifebit notebook server, the terminal is already a Bash session
# with git pre-installed. Open the JupyterLab launcher and pick "Terminal".
git --version
```
:::

::::

After either path, the prompt you see should look about the same. That's
the whole point — the rest of this lesson works identically.

## A guided tour of ten commands

Type each command below at the prompt, hit Enter, and read what you get back.
Don't worry about memorising — repetition will do that for you.

### Where am I?

```bash
pwd
```

`pwd` = **p**rint **w**orking **d**irectory. It tells you your current
location in the filesystem. Think of it as "what room of the house am I in?"

### What's around me?

```bash
ls
ls -l
ls -la
```

`ls` lists files. `-l` gives the long form (sizes, dates). `-la` also shows
hidden files (the ones starting with `.`).

:::{admonition} Tip
:class: note

If a command's flags feel mysterious, paste them into
[ExplainShell](https://explainshell.com/) — it breaks them down piece by piece.
This is how existing trainings have always taught flags, and we
shamelessly continue the tradition.
:::

### Moving around

```bash
cd ~              # go to your home directory
cd Desktop        # go into Desktop (must exist)
cd ..             # go up one level
cd -              # go back to where you just were
```

### Making things, copying things, moving things

```bash
mkdir my-first-project        # make a directory
cd my-first-project
touch hello.txt               # create an empty file
cp hello.txt hello-copy.txt   # copy
mv hello-copy.txt greetings.txt  # rename / move
```

### Looking at the contents of a file

```bash
cat greetings.txt   # dump the whole thing
less hello.txt      # scroll through it (q to quit)
head hello.txt      # first 10 lines
tail hello.txt      # last 10 lines
```

### Getting help

```bash
man ls              # the manual page (q to quit)
ls --help           # shorter help summary
```

That's it. Ten core moves and you can navigate, inspect, and assemble
work on the command line.

## A tiny exercise

Before moving on, do this in your terminal:

```bash
cd ~
mkdir -p elements-of-style-practice/day-1
cd elements-of-style-practice/day-1
touch notes.md
ls -la
pwd
```

You should see `notes.md` listed, and `pwd` should report a path ending in
`/elements-of-style-practice/day-1`. If yes — congratulations, you've just
created a project folder. Step 2 will turn it into a Git repo.

## Where to next

→ Next lesson: [Version control with Git](version-control.md)
