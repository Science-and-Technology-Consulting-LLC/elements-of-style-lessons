# Creating a conda environment

You will install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and make a clean practice environment called `eos-practice`. This matters because a clean, named environment makes your work repeatable on any machine.

**What you will do:**

- Install `conda`, the program that manages software environments.
- Create an environment named `eos-practice`.
- Activate it and list your environments.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Version control with Git](../version-control/README.md), is done.
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.
- A Bash terminal on Linux, with an internet connection. On a Mac or Windows, the Introduction already installed [Miniforge](https://conda-forge.org/download/), so you can read this page and skip the Linux installer steps. No Linux terminal? [Other places to run these lessons](../introduction/other-places-to-run.md) covers Google Cloud Shell and Lifebit.

The Introduction already created the `eos` environment from `eos.yml`. This page shows by hand what that did, step by step. Run the steps below only in a practice account or folder you can delete: creating `eos` again, as the *Create your first clean environment* step does, replaces the one you have.

In JupyterLab, open `lessons`, then `conda-environments`, then [`creating-a-conda-environment.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/conda-environments/creating-a-conda-environment.ipynb). Run each cell in order, top to bottom.

## Steps to execute

### Know what conda is

`conda` is the program we use to control our software and manage installs. A **conda environment** is an isolated bubble: its own Python or R, and its own set of installed packages. Nothing you install into an environment leaks out and disturbs the rest of the computer.

A *clean* environment makes every assumption about what is or is not installed explicit. Without one you inherit whatever happens to be on a shared machine. That is a common cause of "works on my machine, breaks in the container".

When we build a container image later (see [containers](../containers/README.md)), we usually start from a conda base image. The same tool follows us from laptop to container to workflow to federated node.

**What you should see:** nothing. This step is reading only.

### Choose where to run this

The steps below use a Linux Bash terminal. Practise installs in a folder you can delete, so a mistake costs nothing. On a Mac or Windows, you already installed Miniforge in the Introduction, so you can stop at *Find out what computer you have*.

**What you should see:** nothing. This step is a choice.

### Know where to look up packages

When you need to install *thing X*, search the web for `anaconda thing-X`, or use the [anaconda.org search](https://anaconda.org/search). Alongside packages you find tutorials, sample data and hosted notebooks, such as [JupyterLab basics](https://anaconda.org/ijstokes/open-data-science-with-anaconda/notebook).

**What you should see:** nothing. This step is reading only.

### Look at your folder first

Look at what is in your folder before you start. `ls -l` lists the files in a folder, one per line. `ls -la` adds the hidden files, whose names start with a dot.

```bash
ls -l
```

```bash
ls -la      # -a also shows hidden files (dotfiles)
```

**What you should see:** a list that starts with a line like `total 12`, then one line per file or folder. The second list is longer, because it also shows hidden entries such as `.bashrc`. A brand new account shows only a few entries.

Not sure what a command's flags mean? Paste the command into [ExplainShell](https://explainshell.com), for example [`ls -la`](https://explainshell.com/explain?cmd=ls+-la).

### Find out what computer you have

We install **Miniconda**, the minimal conda installer from Anaconda. The full Anaconda includes many extras we do not need. First, confirm your operating system and architecture. `uname -a` prints them.

```bash
uname -a
```

**What you should see:** one long line. On most Linux machines it starts with `Linux` and contains `x86_64`. The next steps are for that case. If the line starts with `Darwin` (a Mac) or you are on Windows, stop here. You installed [Miniforge](https://conda-forge.org/download/) in the Introduction, so go on at *Create your first clean environment*.

> **Picture to add:** a Linux terminal after `uname -a`, showing the Linux and x86_64 words (save as assets/creating-a-conda-environment-step-5.png)

### Check that `wget` is installed

`wget` is a program that downloads files from a web address. `which` prints where a program lives, or nothing if it is missing.

```bash
which wget
```

**What you should see:** one line, for example `/usr/bin/wget`. If nothing prints, `wget` is missing. See "If something goes wrong".

### Download the installer

For Linux x86_64, we download the matching Miniconda installer. The second line lists the file so you can confirm it arrived.

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ls -l Miniconda3-latest-Linux-x86_64.sh
```

**What you should see:** a progress bar that ends with a line saying the file was saved, then one `ls -l` line that shows the file name `Miniconda3-latest-Linux-x86_64.sh` and its size.

### Run the installer (in a terminal)

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

### Restart the shell so `conda` is found

The command `exec -l bash` restarts your shell, so it re-reads your settings and finds `conda`. Run it in a **terminal**, not in a notebook cell, because it replaces the shell itself. Then check where `conda` lives.

```bash
exec -l bash
```

```bash
which conda
```

**What you should see:** a path such as `/home/you/miniconda3/bin/conda`, and your terminal prompt now starts with `(base)`. `base` is conda's built-in starting environment.

### Create your first clean environment

We already built `eos` in the Introduction. That is the environment for the course, so we leave it alone. Here we practise with a second one, named `eos-practice`. `-n eos-practice` sets the name, and `-y` answers "yes" to conda's questions. If an environment with that name already exists, creating it again replaces it, so check `conda env list` first (*List every environment*).

```bash
conda create -n eos-practice -y
```

**What you should see:** conda prints the folder it will use, then `done`, and a note on how to activate it.

### Activate it

To **activate** an environment is to start using it.

```bash
conda activate eos-practice
```

**What you should see:** no message. Your prompt now starts with `(eos-practice)` instead of `(base)`. You are inside the bubble. Anything you `conda install` from now on lands in `eos-practice` only.

> **Picture to add:** a terminal prompt that starts with (eos-practice) (save as assets/creating-a-conda-environment-step-11.png)

### List every environment

This shows all environments on the machine. The active one has a star.

```bash
conda env list
```

**What you should see:**

```
# conda environments:
#
base                     /home/you/miniconda3
eos                      /home/you/miniconda3/envs/eos
eos-practice          *  /home/you/miniconda3/envs/eos-practice
```

### Recap

You just:

- Started a Bash shell in your own terminal.
- Learned where to search for Anaconda packages.
- Used `wget` to fetch the Miniconda installer.
- Installed `conda`.
- Created and activated a clean `eos-practice` environment.
- Left the course environment `eos` as it was. Run `conda activate eos` to go back to it before you start JupyterLab.

### If something goes wrong

- **`wget: command not found`.** On a Mac, `wget` is not installed, and the Linux installer is the wrong one anyway. Use the [Miniforge](https://conda-forge.org/download/) you installed in the Introduction. On Linux, install `wget` with your package manager.
- **`conda: command not found` after the install.** The shell has not re-read its settings. Close the terminal and open a new one, or run `exec -l bash` again. If you skipped `conda init`, run `~/miniconda3/bin/conda init bash` and restart the shell.
- **`conda activate eos-practice` says to run `conda init`.** Run `conda init bash`, close the terminal, open a new one and try again. In a notebook cell this command may not work. Use a terminal.

> **Check:** No executed copy of this notebook was available, so the "What you should see" lines describe the typical result. Compare them with a real run.

## Next

[Recap: workspace set-up](recap-workspace-setup.md): a checkpoint that puts conda in context with the notebook and Git work.
