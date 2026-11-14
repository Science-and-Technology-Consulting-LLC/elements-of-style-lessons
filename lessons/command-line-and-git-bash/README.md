# The command line, with Git Bash

This lesson gives you a Bash terminal that works the same on Mac, Windows and Linux, and the few commands that get you from lost to productive.

> *In the book: Section 3.7 — The Command Line with Git Bash.*

## Before you start

The previous lessons: [Introduction](../introduction/README.md) and [The Rules](../elements-of-style-rules/README.md).

## Do this

1. **Clone the repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook** `lessons/command-line-and-git-bash/using-the-command-line.ipynb`. From the repository folder, run `conda activate eos`, then `jupyter lab`. Open [`using-the-command-line.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/command-line-and-git-bash/using-the-command-line.ipynb) and run each cell in order, top to bottom. The same steps are on the web as [Using the command line](using-the-command-line.md).

## What you should see

- A `practice` folder appears next to the notebook.
- You create, copy and delete a file and a folder, and the listing changes after each step.
- A file named `deseq2_5k.csv`, about 580 KB, downloads into `practice`.

## Where the files are

- `lessons/command-line-and-git-bash/README.md` — this page.
- `lessons/command-line-and-git-bash/using-the-command-line.ipynb` — the notebook you run.
- `lessons/command-line-and-git-bash/using-the-command-line.md` — the same steps as a web page.
- `lessons/command-line-and-git-bash/assets/` — pictures for the lesson.
- `lessons/command-line-and-git-bash/practice/` — made when you run the notebook.

## Next

[Version control with Git](../version-control/README.md)

## Background

The terminal is the common language of biomedical computing. Cloud platforms, HPC clusters (shared computers for big jobs) and containers all take shell commands. You need about ten commands to be productive.

### One terminal for everyone

On Mac and Linux the built-in shell is already Bash (or zsh, which is close enough). On Windows the equivalent is **Git Bash**, which comes with the Git for Windows installer. Then a colleague on Windows and a colleague on a Mac see the same prompt and run the same commands.

Neither macOS nor a stock Windows install has Git. Install it once.

- **Windows.** Download the installer from [git-scm.com](https://git-scm.com/install/windows). Accept the defaults. Open **Git Bash** from the Start menu. Check with `git --version`.
- **macOS.** Open **Terminal** (`Cmd-Space`, type `Terminal`, press Return). Type `git --version`. If Git is missing, macOS offers to install the command line developer tools. Click **Install** and wait. Then run `git --version` again. You can instead run `brew install git` after installing [Homebrew](https://brew.sh), or use the [standalone installer](https://git-scm.com/download/mac).
- **Linux.** Bash is the default. Install Git with `apt install git` or `dnf install git` if it is missing.
- **No computer of your own, or a cloud platform?** See [Other places to run these lessons](../introduction/other-places-to-run.md).

> **Check:** Another page in this repo gives the Windows installer address as `git-scm.com/download/win` and this page gave `git-scm.com/install/windows`. Which one is current?

### Ten commands

Type each one, press Enter and read what comes back. Repetition will teach you.

| Command | What it does |
|---|---|
| `pwd` | Prints your working directory, the folder you are in. |
| `ls`, `ls -l`, `ls -la` | Lists files. `-l` gives sizes and dates. `-la` also shows hidden files, whose names start with `.`. |
| `cd ~`, `cd ..`, `cd -` | Goes to your home folder, up one level, or back to where you just were. |
| `mkdir name` | Makes a folder. |
| `touch name` | Makes an empty file. |
| `cp from to` | Copies a file. |
| `mv from to` | Renames or moves a file. |
| `cat name` | Prints a whole file. |
| `less name` | Scrolls through a file. Press `q` to quit. |
| `head name`, `tail name` | Prints the first or last 10 lines. |
| `man ls`, `ls --help` | Shows the manual page or a short help summary. |

If a command's flags look mysterious, paste it into [ExplainShell](https://explainshell.com/). It explains each part.

### A tiny exercise

```bash
cd ~
mkdir -p elements-of-style-practice/day-1
cd elements-of-style-practice/day-1
touch notes.md
ls -la
pwd
```

You should see `notes.md` listed. `pwd` should print a path that ends in `/elements-of-style-practice/day-1`. You have made a project folder. The next lesson turns a folder like it into a Git repository.

### The notebooks in this lesson

1. [Using the command line](using-the-command-line.md) — seven commands, one step at a time.

### Further reading

- [ExplainShell](https://explainshell.com/) — paste any command and see what each flag means
- [Git for Windows](https://git-scm.com/install/windows) — the installer that includes Git Bash
- [Miniforge](https://github.com/conda-forge/miniforge) — the terminal-friendly conda installer
- [The Linux Command Line](https://linuxcommand.org/tlcl.php) — William Shotts' free book
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/) — the definitive source
