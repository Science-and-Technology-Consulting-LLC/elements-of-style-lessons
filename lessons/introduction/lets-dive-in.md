# Let's dive in

In this walkthrough you set up your computer and run your first notebook. Every later lesson assumes this setup, so it pays to get it right once.

**What you will do:**

- Install the programs the lessons use.
- Build one [conda environment](../conda-environments/README.md) that holds them all.
- Open [JupyterLab](https://jupyter.org/) and run two checks inside a notebook.

**What you need:**

- A computer: a Mac, Windows with Git Bash, or Linux. No computer of your own? See [Other places to run these lessons](other-places-to-run.md).
- [Git](https://git-scm.com/), the program that tracks changes to files. Step 1 installs it. If `git --version` fails, do Step 1 first, then come back to "Before you begin".
- [Miniforge](https://github.com/conda-forge/miniforge), the installer for conda. Step 2 installs it.
- A free [GitHub account](https://github.com/signup). You first need it in the [version control lesson](../version-control/README.md).
- A good internet connection. Step 3 downloads a few hundred packages.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`lets-dive-in.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/introduction/lets-dive-in.ipynb) and run each cell in order, top to bottom.

## The steps

### Step 1. Install a terminal and Git

A *terminal* is a window where you type instructions instead of clicking. *Bash* is the language those instructions are written in. Using Bash everywhere means a Mac, a Windows PC and a cloud machine all behave the same way.

- **Windows:** download and run the installer from [Git for Windows](https://git-scm.com/download/win). Accept the defaults. Then open **Git Bash** from the Start menu. Git for Windows installs both Git and Git Bash.
- **Mac:** open **Terminal** (press `Cmd-Space`, type `Terminal`, press Return). Type `git --version` and press Return. If a box offers to install the "command line developer tools", click **Install** and wait a few minutes.
- **Linux:** Bash is already your terminal. If Git is missing, install it with `sudo apt install git` (or `sudo dnf install git`).

Type this in the terminal, then press Return:

```text
git --version
```

**What you should see:** one line that starts with `git version` and ends with a number.

> **Picture to add:** a Mac Terminal window and a Windows Git Bash window, each showing the output of `git --version` (save as assets/lets-dive-in-step-1.png)

The [command line lesson](../command-line-and-git-bash/README.md) covers this step in more detail.

### Step 2. Install Miniforge

*Conda* is a program that installs other programs into a private folder, so one project cannot break another. *Miniforge* is the small installer that gives you conda.

- **Mac:** download the installer for your chip from the [Miniforge page](https://github.com/conda-forge/miniforge#install). Run it in Terminal. For an Apple chip the command is `bash Miniforge3-MacOSX-arm64.sh`. For an Intel chip use the `x86_64` file.
- **Windows:** download `Miniforge3-Windows-x86_64.exe` from [conda-forge.org/download](https://conda-forge.org/download/) and run it.

When the installer finishes, close your terminal and open a new one. Then type:

```text
conda --version
```

**What you should see:** the word `conda` followed by a version number.

### Step 3. Create the `eos` environment

An *environment* is a private folder of programs. The file `eos.yml` in the repository is the recipe. It lists Python, JupyterLab, Git, the GitHub command line (`gh`), [Nextflow](https://www.nextflow.io/) and more. You are already inside the repository folder from "Before you begin".

Type these two lines in the terminal. They are not notebook cells.

```text
conda env create -f eos.yml
conda activate eos
```

The first line takes several minutes the first time. Conda downloads and sorts out a few hundred packages.

**What you should see:** a long list of packages, then a prompt that starts with `(eos)`. The `(eos)` means the environment is active. Run `conda activate eos` in every new terminal before you start a lesson.

### Step 4. Register the Bash kernel

A *kernel* is the engine that runs the code in a notebook. This notebook uses the Bash kernel. You register it once. Running it again does no harm.

Run this cell. If you are working in a terminal instead, type the same two lines there, with `eos` active.

```bash
pip install bash_kernel
python -m bash_kernel.install
```

**What you should see:** a stream of lines that start with `Requirement already satisfied` or `Collecting`, and a last line that says `Installing IPython kernel spec`.

### Step 5. Start JupyterLab

*JupyterLab* is the program that opens notebooks in your web browser. Start it from a terminal where `(eos)` is active. It is not a notebook cell, because it keeps running until you stop it.

```text
jupyter lab
```

Restart it if it was already running, so it sees the new Bash kernel. To stop it later, click in that terminal and press `Ctrl-C`.

**What you should see:** a browser tab opens with JupyterLab. The Launcher has a **Bash** tile.

> **Picture to add:** the JupyterLab Launcher with the Bash tile visible (save as assets/lets-dive-in-step-5.png)

### Step 6. Check your tools

This cell asks your computer where each program lives. Where a program is missing, the cell says `MISSING`. Only `bash`, `git` and `python3` must be present today. The other lessons tell you when they need the rest.

| Tool | Check by hand | If missing, see |
|---|---|---|
| [Bash](https://www.gnu.org/software/bash/) | `bash --version` | [Command line](../command-line-and-git-bash/README.md) |
| [Git](https://git-scm.com/) | `git --version` | [Command line](../command-line-and-git-bash/README.md) |
| [Conda](https://docs.conda.io/) | `conda --version` | [Conda environments](../conda-environments/README.md) |
| [GitHub CLI](https://cli.github.com/) (`gh`) | `gh --version` | [Version control](../version-control/why-git-and-setup.md) |
| [Docker](https://docs.docker.com/get-docker/) | `docker --version` | [Containers](../containers/README.md) |
| [Nextflow](https://www.nextflow.io/) | `nextflow -version` | [Nextflow workflows](../nextflow-workflows/README.md) |
| [Python 3](https://www.python.org/) | `python3 --version` | [Conda environments](../conda-environments/README.md) |

Run all the checks at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s
" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING
" "$cmd"
  fi
done
```

**What you should see:** one line per tool. A tool that is present shows its location. A tool that is missing shows `MISSING`. For example:

```text
  bash       /bin/bash
  git        /path/to/eos/bin/git
  docker     MISSING
```

The exact paths on your computer will differ. If you started from the `eos` environment, `git`, `conda`, `gh`, `nextflow` and `python3` all show a path. `docker` may show `MISSING` until Step 7.

### Step 7. Install Docker later

[Docker](https://docs.docker.com/get-docker/) runs *containers*, which are sealed boxes holding a program and everything it needs. Conda does not install Docker. You need it from the [containers lesson](../containers/README.md) on. Skip it today.

### Step 8. Other places to run the lessons

Your own Bash terminal is the main way to follow these lessons. If you cannot use one, or later when the work grows, see [Other places to run these lessons](other-places-to-run.md). It covers Google Cloud Shell and Lifebit.

## If something goes wrong

- **`git: command not found` or `conda: command not found`.** On Windows, make sure you opened *Git Bash*, not Command Prompt or PowerShell. After installing Miniforge, close the terminal and open a new one.
- **No Bash tile in JupyterLab.** You registered the kernel outside the `eos` environment. Run `conda activate eos`, repeat Step 4, then restart JupyterLab (Step 5).
- **A tool shows `MISSING`.** Compare it with the table in Step 6. Run `conda activate eos` and run the cell again. Docker is the one tool you install by hand.

## Next

Continue with [The Rules](../elements-of-style-rules/README.md).
