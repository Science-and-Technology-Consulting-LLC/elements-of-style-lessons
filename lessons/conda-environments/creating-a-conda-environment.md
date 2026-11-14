# Creating a conda environment

You will install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and make a clean environment called `eos`. This matters because a clean, named environment makes your work repeatable on any machine.

**What you will do:**

- Install `conda`, the program that manages software environments.
- Create an environment named `eos`.
- Activate it and list your environments.

**What you need:**

- A Bash terminal on Linux, with an internet connection. A Mac or Windows needs a different installer: see the next line.
- On a Mac or Windows, use [Miniforge](https://conda-forge.org/download/) instead of the steps in this notebook that download the Linux installer. See the [lesson page](README.md).
- No Linux terminal? [Other places to run these lessons](../introduction/other-places-to-run.md) covers Google Cloud Shell and Lifebit.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`creating-a-conda-environment.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/conda-environments/creating-a-conda-environment.ipynb) and run each cell in order, top to bottom.

## Steps

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do Steps 4 and 6 of [Let's dive in](../introduction/lets-dive-in.md) first.

### Step 1. Know what conda is

`conda` is the program we use to control our software and manage installs. A **conda environment** is an isolated bubble: its own Python or R, and its own set of installed packages. Nothing you install into an environment leaks out and disturbs the rest of the computer.

Making a *clean* environment first is a good habit. It makes every assumption about what is or is not installed explicit. Without it you inherit whatever happens to be on a shared machine. That is a common cause of "works on my machine, breaks in the container".

When we build a Docker image later (see [containers](../containers/README.md)), we usually start from a conda base image. The same tool follows us from laptop to container to workflow to federated node.

**What you should see:** nothing. This step is reading only.

### Step 2. Choose where to run this

The steps below use a Linux Bash terminal. Practise installs in a folder you can delete, so a mistake costs nothing. On a Mac or Windows, stop at Step 5 and use the Miniforge installer instead.

**What you should see:** nothing. This step is a choice.

### Step 3. Know where to look up packages

When you need to install *thing X*, search the web for `anaconda thing-X`, or use the [anaconda.org search](https://anaconda.org/search). Alongside packages you find tutorials, sample data and hosted notebooks, such as [JupyterLab basics](https://anaconda.org/ijstokes/open-data-science-with-anaconda/notebook).

**What you should see:** nothing. This step is reading only.

### Step 4. Look at your folder first

Look at what is in your folder before you start. `ls -l` lists the files in a folder, one per line. `ls -la` adds the hidden files, whose names start with a dot.

```bash
ls -l
```

```bash
ls -la      # -a also shows hidden files (dotfiles)
```

**What you should see:** a list that starts with a line like `total 12`, then one line per file or folder. The second list is longer, because it also shows hidden entries such as `.bashrc`. A brand new account shows only a few entries.

Not sure what a command's flags mean? Paste the command into [ExplainShell](https://explainshell.com), for example [`ls -la`](https://explainshell.com/explain?cmd=ls+-la).

### Step 5. Find out what computer you have

We install **Miniconda**, the minimal conda installer from Anaconda. The full Anaconda includes many extras we do not need. First, confirm your operating system and architecture. `uname -a` prints them.

```bash
uname -a
```

**What you should see:** one long line. On most Linux machines it starts with `Linux` and contains `x86_64`. The next steps are for that case. If the line starts with `Darwin` (a Mac) or you are on Windows, stop here and install [Miniforge](https://conda-forge.org/download/) instead, then go on at Step 10.

> **Picture to add:** a Linux terminal after `uname -a`, showing the Linux and x86_64 words (save as assets/creating-a-conda-environment-step-5.png)

### Step 6. Check that `wget` is installed

`wget` is a program that downloads files from a web address. `which` prints where a program lives, or nothing if it is missing.

```bash
which wget
```

**What you should see:** one line, for example `/usr/bin/wget`. If nothing prints, `wget` is missing. See "If something goes wrong".

### Step 7. Download the installer

For Linux x86_64, we download the matching Miniconda installer. The second line lists the file so you can confirm it arrived.

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ls -l Miniconda3-latest-Linux-x86_64.sh
```

**What you should see:** a progress bar that ends with a line saying the file was saved, then one `ls -l` line that shows the file name `Miniconda3-latest-Linux-x86_64.sh` and its size.

### Step 8. Run the installer (in a terminal)

The installer asks you questions and waits for typed answers, so a notebook cell cannot run it. **Open a terminal and type the command there**, in the same folder as the downloaded file. The cell below shows the command.

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Answer the prompts:

- Press `Enter` to read the license. Press `Space` to scroll faster.
- Type `yes` to accept the license terms.
- Press `Enter` to accept the default install location.
- Type `yes` when it asks "Do you wish the installer to initialize Miniconda3 by running conda init?"

To skip all questions, you can run `bash Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda3` instead. That installs into `~/miniconda3` without asking. Afterwards run `~/miniconda3/bin/conda init bash`.

**What you should see:** many lines of progress, ending with a message that the installation is finished and a reminder to close and reopen your shell.

> **Picture to add:** the installer asking "Do you wish the installer to initialize Miniconda3" (save as assets/creating-a-conda-environment-step-8.png)

### Step 9. Restart the shell so `conda` is found

The command `exec -l bash` restarts your shell, so it re-reads your settings and finds `conda`. Run it in a **terminal**, not in a notebook cell, because it replaces the shell itself. Then check where `conda` lives.

```bash
exec -l bash
```

```bash
which conda
```

**What you should see:** a path such as `/home/you/miniconda3/bin/conda`, and your terminal prompt now starts with `(base)`. `base` is conda's built-in starting environment.

### Step 10. Create your first clean environment

Name the environment for the project. This course is *Elements of Style*, so `eos` is a natural short name. `-n eos` sets the name, and `-y` answers "yes" to conda's questions. If `eos` already exists, creating it again replaces it, so check `conda env list` first (Step 12).

```bash
conda create -n eos -y
```

**What you should see:** conda prints the folder it will use, then `done`, and a note on how to activate it.

### Step 11. Activate it

To **activate** an environment is to start using it.

```bash
conda activate eos
```

**What you should see:** no message. Your prompt now starts with `(eos)` instead of `(base)`. You are inside the bubble. Anything you `conda install` from now on lands in `eos` only.

> **Picture to add:** a terminal prompt that starts with (eos) (save as assets/creating-a-conda-environment-step-11.png)

### Step 12. List every environment

This shows all environments on the machine. The active one has a star.

```bash
conda env list
```

**What you should see:**

```
# conda environments:
#
base                     /home/you/miniconda3
eos                   *  /home/you/miniconda3/envs/eos
```

## Recap

You just:

- Started a Bash shell in your own terminal.
- Learned where to search for Anaconda packages.
- Used `wget` to fetch the Miniconda installer.
- Installed `conda`.
- Created and activated a clean `eos` environment.

## If something goes wrong

- **`wget: command not found`.** On a Mac, `wget` is not installed, and the Linux installer is the wrong one anyway. Use [Miniforge](https://conda-forge.org/download/). On Linux, install `wget` with your package manager.
- **`conda: command not found` after the install.** The shell has not re-read its settings. Close the terminal and open a new one, or run `exec -l bash` again. If you skipped `conda init`, run `~/miniconda3/bin/conda init bash` and restart the shell.
- **`conda activate eos` says to run `conda init`.** Run `conda init bash`, close the terminal, open a new one and try again. In a notebook cell this command may not work. Use a terminal.

> **Check:** No executed copy of this notebook was available, so the "What you should see" lines describe the typical result. Compare them with a real run.

## Next

[recap-workspace-setup.md](recap-workspace-setup.md): a checkpoint that puts conda in context with the notebook and Git work. Then [containers](../containers/README.md), where the environment becomes the seed for a Docker image.
