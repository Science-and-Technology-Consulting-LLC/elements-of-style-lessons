# Why Git and GitHub?

You will set up the tools that record your work, and tell Git who you are. This matters because every change you save is stamped with your name, so your methods stay traceable.

[Git](https://git-scm.com/) keeps the history of your files. [GitHub](https://github.com/) is the website where that history is shared. Along the way we will edit a text file in a terminal with [`nano`](https://www.nano-editor.org/).

> **Check:** This lesson uses conda before the conda lesson. Should students install conda first, or is the order meant to be this way?

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [The command line, with Git Bash](../command-line-and-git-bash/README.md), is done.
- A free [GitHub account](https://github.com/signup).
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.

The Introduction already made the `eos` environment, and its recipe (`eos.yml`) lists `git` and `gh`. So two steps below may find their work done. We say where.

## Steps to execute

### Make a practice folder

You will keep all practice files in one folder, `~/eos-practice`, so they stay apart from the course files. `~` means your home folder. `pwd` prints the folder you are in.

```bash
mkdir -p ~/eos-practice
cd ~/eos-practice
pwd
```

**What you should see:** one line ending in `eos-practice`, for example `/Users/you/eos-practice`.

### Write a file with `nano` (in a terminal)

[`nano`](https://www.nano-editor.org/) is a simple text editor that runs inside the terminal. A notebook cell cannot run it, so use a terminal for this step. Open a new terminal window as in step 1 of the [Introduction page](../introduction/README.md), and run `conda activate eos` there.

1. In the terminal, type `cd ~/eos-practice` and press `Enter`.
2. Type `nano hello.txt` and press `Enter`. This opens the file, or creates it if it is new.
3. Type any line of text, such as `hello Git`.
4. Save: press `Ctrl-O`, then `Enter` to confirm the file name.
5. Exit: press `Ctrl-X`.

> **Picture to add:** the nano screen with one line of text and the shortcut bar at the bottom (save as assets/why-git-and-setup-step-2.png)

**What you should see:** you are back at the normal prompt, and the file exists. The next cell shows its first lines with `head`. `head` prints the top of a file.

```bash
head hello.txt
```

**What you should see:** the line you typed, for example:

```
hello Git
```

If you did not use nano, you will see `head: hello.txt: No such file or directory`. Go back and make the file first.

### Create a conda environment called `eos`

A **conda environment** is a separate folder of installed programs. Putting the course tools in one named environment keeps them from clashing with anything else on your computer. The [conda-environments lesson](../conda-environments/README.md) explains this in full.

You made `eos` in the Introduction, so you will most likely see it in the list below. If you do, the create cell below will do nothing.

First, list the environments you already have. If `eos` is in the list, the next cell does nothing, so it never replaces your environment.

```bash
conda env list
```

**What you should see:** a table of names and folders. A fresh conda shows only `base`. Look for a line that starts with `eos`.

Now create the environment. `-n eos` names it, and `-y` answers "yes" to the questions. The cell first looks for `eos` and creates it only if it is missing.

```bash
conda env list | grep -q '^eos ' && echo 'eos already exists: nothing to create' || conda create -n eos -y
```

**What you should see:** conda prints the folder it will use, then `done`, then a message that says how to activate it (we did this in the Introduction, but here is what it looks like):

```
# To activate this environment, use
#
#     $ conda activate eos
```

Now **activate** the environment, which means "start using it". Your terminal prompt gains `(eos)` at the start.

```bash
conda activate eos
```

**What you should see:** no message. In a terminal, the prompt now starts with `(eos)`.

### Install the GitHub CLI

The GitHub CLI (`gh`) is a program that signs you in to GitHub from the terminal. **CLI** means *command-line interface*: a program you control by typing. `conda install` downloads it from the [conda-forge](https://conda-forge.org/) package channel. If `gh --version` below already prints a version, `gh` came with `eos`, and you can skip the install cell.

```bash
conda install -c conda-forge gh -y
```

**What you should see:** conda solves the environment, lists packages, then ends with `Executing transaction: done`. This can take a minute. Check that it worked:

```bash
gh --version
```

**What you should see:** a line like `gh version 2.x.x` followed by a web address.

#### Optional: install a different terminal editor

If you prefer `emacs` to `nano`, install it. It is a large download, so skip this unless you want it.

```bash
conda install -c conda-forge emacs -y
```

### Tell Git who you are

Every Git **commit** (a saved snapshot of your work) records who made it. Git reads your name and email from its settings. You set them once, with `--global`, and every future commit uses them.

**Edit the next cell first.** Replace each piece of text in angle brackets, including the `<` and `>`, with your own value. Use the email tied to your GitHub account. Keep the quotes.

```bash
git config --global user.name  '<your github user name>'
git config --global user.email '<the email tied to your github account>'
```

**What you should see:** nothing, if it worked. Check your settings:

```bash
git config --global --get user.name
git config --global --get user.email
```

**What you should see:** your name on one line and your email on the next.

### Choose your editor for Git messages (optional)

Git sometimes opens a text editor. This setting says which one. The first line below picks `nano`. The commented lines (they start with `#`) show how to pick `emacs` or `vim` instead.

```bash
git config --global core.editor nano
# or
# git config --global core.editor emacs
# git config --global core.editor vim
```

**What you should see:** nothing. The setting is saved.

### If something goes wrong

- **`conda: command not found`.** Conda is not installed, or this terminal was opened before you installed it. Close the terminal, open a new one, and try again. If it still fails, install conda as in step 3 of the [Introduction page](../introduction/README.md).
- **`conda activate eos` says to run `conda init`.** Run `conda init bash`, close the terminal, open a new one, then run `conda activate eos` again. In a notebook cell this command may not work. Run it in a terminal instead.
- **`git: command not found` on a Mac.** Type `git --version` in Terminal. A window offers to install the Xcode Command Line Tools. Accept it. On Windows, install [Git for Windows](https://gitforwindows.org/), which also gives you Git Bash.
- **`python: command not found` when you register the Bash kernel (step 4 of the [Introduction page](../introduction/README.md)).** Try `python3` in place of `python`.

## Next

[workspace-setup.md](workspace-setup.md): check your computer and start JupyterLab.
