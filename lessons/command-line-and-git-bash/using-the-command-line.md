# Using the command line

In this walkthrough you type seven commands that move, make, copy, delete and download files. Every tool in the later lessons (`git`, `conda`, `docker`, `nextflow`) runs from the same terminal, so this is the skill you will use most.

**What you will do:**

- Look around a folder and find out where you are.
- Create, copy and delete a file, and create and delete a folder.
- Download a real data file from the web.

**What you need:**

- A terminal with Bash: *Terminal* on a Mac or Linux, [Git Bash](https://git-scm.com/download/win) on Windows. The [introduction lesson](../introduction/lets-dive-in.md) installs both.
- The `eos` conda environment from that lesson, which provides `wget` and JupyterLab. See [Conda environments](../conda-environments/README.md).
- An internet connection, for the last step.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`using-the-command-line.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/command-line-and-git-bash/using-the-command-line.ipynb) and run each cell in order, top to bottom.

## The steps

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

### Make a practice folder

The next steps create and delete files. Doing that in a folder of its own keeps the lesson files safe. `mkdir -p practice` makes a folder called `practice`. `cd practice` moves you into it. You meet both commands again below.

```bash
mkdir -p practice
cd practice
pwd
```

**What you should see:** one line, a path that ends in `/command-line-and-git-bash/practice`. Every later cell now runs inside that folder.

### `ls` lists the files in a folder

*Folder* and *directory* mean the same thing. `ls` lists what is in the current folder. The `-l` option gives the long form: permissions, owner, size and date. An *option* (or *flag*) changes how a command works.

```bash
ls -l
```

**What you should see:** nothing, or the line `total 0`. Your practice folder is empty.

You can paste any command you do not understand into [ExplainShell](https://explainshell.com/). It explains each part.

### `pwd` prints your location

`pwd` stands for *print working directory*. It shows the full address of the folder you are in. A path that starts at the top of the disk (like `/home/annie/work`) is an *absolute* path. A path that starts from where you are now (like `../data`) is a *relative* path. [This page](https://linuxfoundation.org/blog/classic-sysadmin-absolute-path-vs-relative-path-in-linux-unix/) explains the difference.

```bash
pwd
```

**What you should see:** the same path as in *Make a practice folder*, ending in `/practice`.

### `echo` and `>` create a file

`echo` prints text. The `>` sign sends that text into a file instead of the screen. If the file does not exist, it is created. If it exists, it is replaced. Here the new file is named `README.md`.

```bash
echo 'I am the header of your first README.md' > README.md
ls -l README.md
```

**What you should see:** one line that ends with `README.md`. The size is 40 bytes:

```text
-rw-r--r--  1 you  staff  40 Nov 13 15:33 README.md
```

Your name and the date will differ.

### `cp` copies a file

`cp` takes the file to copy, then the name for the copy.

```bash
cp README.md duplicated_README.md
ls -l README.md duplicated_README.md
```

**What you should see:** two lines, both 40 bytes, one for `README.md` and one for `duplicated_README.md`.

### `head` shows the start of a file

`head` prints the first lines of a file. To read a long file one page at a time in a terminal, use `less` and press `q` to quit. `less` does not work inside a notebook, but `head` does.

```bash
head README.md
```

**What you should see:**

```text
I am the header of your first README.md
```

### `rm` deletes a file

`rm` removes the file you name. The terminal has no trash bin. The file is gone for good, so check the name before you press Return.

```bash
rm duplicated_README.md
ls -l
```

**What you should see:** only `README.md` is left. The copy is gone.

### `mkdir` makes a folder

`mkdir` stands for *make directory*.

```bash
mkdir new_folder
ls -l
```

**What you should see:** a new line for `new_folder`. It starts with `d`, which means directory:

```text
drwxr-xr-x  2 you  staff  64 Nov 13 15:33 new_folder
```

### `rm -r` deletes a folder

The `-r` option means *recursive*. It removes the folder and everything inside it. Use it with care.

```bash
rm -r new_folder
ls -l
```

**What you should see:** `new_folder` is gone. Only `README.md` is left.

### `wget` downloads a file

`wget` fetches a file from a web address. This file is a table of results from an RNA-seq experiment (a count of how active each gene is), analysed with DESeq2. It lists genes with *p*-values below 0.05 and a fold change above 1.5. The [interactive computing lesson](../interactive-computing/README.md) uses it again for a volcano plot. The `-q` option keeps `wget` quiet.

```bash
ls -l
```

**What you should see:** a line for `deseq2_5k.csv`, about 580,000 bytes (about 570 KB):

```text
-rw-r--r--  1 you  staff  580861 Nov 13 15:33 deseq2_5k.csv
```

You have now used `ls`, `pwd`, `cp`, `rm`, `mkdir`, `rm -r` and `wget`. The folder `practice` stays on your disk. When you are finished, you can delete it from a terminal with `rm -r practice`.

## If something goes wrong

- **`wget: command not found`.** Neither a Mac nor Git Bash comes with `wget`. The `eos` environment does. Close JupyterLab, run `conda activate eos` in a terminal, start `jupyter lab` again and rerun the cell. As a stopgap, `curl -O https://zenodo.org/record/4302133/files/deseq2_5k.csv` does the same job.
- **`ls: cannot access` or `No such file`.** You skipped a step, or you are in the wrong folder. Run `pwd` and compare with *`pwd` prints your location*. Then run the steps again from the top.
- **The notebook asks you to choose a kernel.** Choose **Bash**. If it is not listed, repeat the kernel registration in the *Register the Bash kernel* step of [Let's dive in](../introduction/lets-dive-in.md) with `eos` active, then restart JupyterLab.

## Next

Continue with the [command line lesson](README.md) for the ten-command tour, then [Version control with Git](../version-control/README.md).
