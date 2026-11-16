# Running a JupyterLab notebook

You will copy a real R notebook from GitHub, open it in JupyterLab, and run it from top to bottom. This matters because "Restart and Run All" is how you prove a notebook works.

**What you will do:**

- Clone a small R notebook project from GitHub.
- Open the notebook and choose the R kernel.
- Run every cell, then use **Restart Kernel and Run All Cells**.

**What you need:**

- JupyterLab running: [starting-a-jupyter-lab-notebook.md](starting-a-jupyter-lab-notebook.md).
- The R kernel registered: [exploring-an-r-notebook.md](exploring-an-r-notebook.md).
- [Git](https://git-scm.com/) installed ([command-line-and-git-bash](../command-line-and-git-bash/README.md)).

## Start here

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`running-a-jupyterlab-notebook.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/interactive-computing/running-a-jupyterlab-notebook.ipynb) and run each cell in order, top to bottom.


### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the six setup steps on the [Introduction page](../introduction/README.md) and the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Know the project

*Project Jupyter is a non-profit, open-source project, born out of the IPython Project in 2014.* Its mission is interactive computing across programming languages. JupyterLab supports roughly 40 language **kernels** (the programs that run your code) through community plugins. Python and R are the two this course uses most.

This walkthrough uses `exampleVolcanoPlotNotebook`, a small R notebook that reads DESeq2 output and draws a **volcano plot** (a scatter plot of how much and how reliably each gene changed). The original lives at [`adeslatt/exampleVolcanoPlotNotebook`](https://github.com/adeslatt/exampleVolcanoPlotNotebook). [`NIH-NICHD/exampleVolcanoPlotNotebook`](https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook) is a teaching fork of it.

**What you should see:** nothing. This step is reading only.

### Open the project page

In your browser, open [https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook](https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook).

**What you should see:** a GitHub page with a file list that includes `README.md` and `Reading-data-and-plotting-in-R.ipynb`.

### Copy the clone address

Click the green **Code** button, then **HTTPS**, then the copy icon. The address looks like `https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook.git`.

> **Picture to add:** the green Code button open on the HTTPS tab with the copy icon (save as assets/running-a-jupyterlab-notebook-step-3.png)

**What you should see:** a small box with the address and a copy icon.

### Go to your practice folder

You keep practice work in `~/eos-practice`. `~` means your home folder. The next cell makes the folder and moves into it.

```bash
mkdir -p ~/eos-practice
cd ~/eos-practice
pwd
```

**What you should see:** one line ending in `eos-practice`.

### Clone the project

To **clone** is to copy a GitHub project onto your computer. You can also do this in a JupyterLab terminal (*File*, *New*, *Terminal*). The command is the same.

```bash
[ -d exampleVolcanoPlotNotebook ] || git clone https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook.git
```

**What you should see:** lines that begin like this and end with `done.`:

```
Cloning into 'exampleVolcanoPlotNotebook'...
remote: Enumerating objects: 22, done.
...
Receiving objects: 100% (22/22), 210.63 KiB | 7.80 MiB/s, done.
Resolving deltas: 100% (6/6), done.
```

(The sizes may differ.)

### Look inside the project

`cd` moves into the new folder. `ls` lists what is in it.

```bash
cd exampleVolcanoPlotNotebook
ls
```

**What you should see:**

```
README.md  Reading-data-and-plotting-in-R.ipynb  install_dependencies.R
```

### Open the notebook

In the JupyterLab file browser (left side), open `eos-practice`, then `exampleVolcanoPlotNotebook`, and double-click `Reading-data-and-plotting-in-R.ipynb`.

If JupyterLab does not offer the *R* kernel, either you need to register [IRkernel](https://irkernel.github.io/) (see [exploring-an-r-notebook.md](exploring-an-r-notebook.md)), or your Lifebit image has Python only. In that case use an image with **R + Python (Bioconductor)**.

> **Picture to add:** the notebook open in JupyterLab with the kernel name "R" at the top right (save as assets/running-a-jupyterlab-notebook-step-7.png)

**What you should see:** the notebook opens in a new tab, and the top right corner says *R*.

### Run every cell, top to bottom

Press `Shift-Enter` to run the current cell and move to the next one. When you finish exploring, use the habit that proves a notebook works:

> **Kernel**, then **Restart Kernel and Run All Cells**.

If the notebook gives the same output, it is *reproducible*. If not, you found a hidden link between cells. Better to find it now than in a paper review.

**Expect some errors on the first run.** This notebook needs three things before it runs cleanly: the data (from Zenodo, DOI [10.5281/zenodo.7510587](https://doi.org/10.5281/zenodo.7510587)), the R packages (installed with `Rscript install_dependencies.R`), and one extra `library(rlang)` line. The [recap-workspace-setup lesson](../conda-environments/recap-workspace-setup.md) explains all three.

> **Check:** Does the NIH-NICHD copy of the notebook run cleanly from top to bottom for a beginner, or should students use the `adeslatt` copy?

> **Picture to add:** the volcano plot that the notebook draws, if it runs to the end (save as assets/running-a-jupyterlab-notebook-step-8.png)

**What you should see:** cells with numbers beside them, text output, and (if the data and packages are in place) a volcano plot.

### What you practised

- Logging into your environment (your laptop).
- Starting an interactive JupyterLab session.
- Cloning a repo from GitHub.
- Running notebook cells with an R kernel.
- Making your first visualisation, a volcano plot.

### If something goes wrong

- **`destination path 'exampleVolcanoPlotNotebook' already exists`.** You already cloned it. Skip the clone and run `cd exampleVolcanoPlotNotebook`.
- **No R kernel in the Launcher.** See [exploring-an-r-notebook.md](exploring-an-r-notebook.md) to install and register it.
- **An error such as "there is no package called ..." or a missing data file.** The notebook needs its packages and data. See the setup at the top of this notebook and the [recap-workspace-setup lesson](../conda-environments/recap-workspace-setup.md).

## Next

[exploring-an-r-notebook.md](exploring-an-r-notebook.md) if you have not done it, or back to the [interactive-computing lesson](README.md). Then [reusable-clis](../reusable-clis/README.md), where notebook code becomes a command-line tool.
