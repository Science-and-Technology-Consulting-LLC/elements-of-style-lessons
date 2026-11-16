# Starting a JupyterLab notebook

You will start [JupyterLab](https://jupyterlab.readthedocs.io/) on your laptop and learn what its screen shows. This matters because every later lesson runs inside it.

**What you will do:**

- Learn what JupyterLab is.
- Start it from a terminal.
- Recognise the file browser, the Launcher and the menu bar.

**What you need:**

- The `eos` conda environment, from [conda-environments](../conda-environments/README.md).
- A web browser such as [Chrome](https://www.google.com/chrome/).

## Start here

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`starting-a-jupyter-lab-notebook.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/interactive-computing/starting-a-jupyter-lab-notebook.ipynb) and run each cell in order, top to bottom.


### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the six setup steps on the [Introduction page](../introduction/README.md) and the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Know what JupyterLab is

Before you can *run* a notebook you need one to run. **JupyterLab** is a web page that lets you open notebooks, files and terminals side by side. It runs on a computer (yours, or a Lifebit server) and shows up in your browser.

You will start it in one of two places, described in the next two steps.

**What you should see:** nothing. This step is reading only.

### On your laptop: start JupyterLab

Finish the [conda-environments lesson](../conda-environments/README.md) first. Then, in a **terminal** (not in a notebook cell), type these two commands, one per line, and press `Enter` after each. The first one turns on the `eos` environment. The second one starts JupyterLab. JupyterLab keeps running until you stop it, so it cannot run as a notebook cell.

```text
conda activate eos
jupyter lab
```

**What you should see:** your terminal prompt starts with `(eos)`. JupyterLab opens in your default browser. In the terminal you see log lines that include a web address like `http://localhost:8888/lab?token=...`. If no browser opens, copy that address into a browser yourself. To stop JupyterLab later, press `Ctrl-C` twice in that terminal.

> **Picture to add:** the terminal after `jupyter lab`, with the localhost address line (save as assets/starting-a-jupyter-lab-notebook-step-2.png)

### Optional: start JupyterLab on Lifebit instead

Skip this step if you started JupyterLab on your laptop in *On your laptop: start JupyterLab*. It needs a Lifebit account: see [Other places to run these lessons](../introduction/other-places-to-run.md).

[Lifebit](https://lifebit.ai/)'s notebook servers have JupyterLab already installed.

1. From the workspace dashboard, click **Notebook**, then **Launch**.
2. Pick a compute size.
3. Wait for the browser tab to open. It opens straight into JupyterLab.

The terminal is under **File**, **New**, **Terminal**.

> **Picture to add:** the Lifebit dashboard with the Notebook and Launch buttons (save as assets/starting-a-jupyter-lab-notebook-step-3.png)

**What you should see:** a new browser tab with JupyterLab in it.

### Recognise the screen

However you got here, you now see:

- A **file browser** on the left.
- A **Launcher** in the middle, with tiles: *Python 3*, *R* (if you registered IRkernel, see [conda-environments](../conda-environments/README.md)), *Terminal* and *Text File*.
- A **menu bar** across the top: *File, Edit, View, Run, Kernel, Tabs* and more.

> **Picture to add:** JupyterLab with the file browser, the Launcher tiles and the menu bar labelled (save as assets/starting-a-jupyter-lab-notebook-step-4.png)

**What you should see:** all three parts above. If the *R* tile is missing, see below.

### If something goes wrong

- **`conda: command not found`.** Conda is not installed, or you opened this terminal before installing it. Close it, open a new one, and see [conda-environments](../conda-environments/README.md).
- **`jupyter: command not found`.** The `eos` environment is not active. Run `conda activate eos` first.
- **The browser does not open.** Copy the `http://localhost:8888/lab?token=...` address from the terminal into your browser.
- **There is no R tile.** R is not registered with Jupyter. Follow the one-time steps in [exploring-an-r-notebook.md](exploring-an-r-notebook.md).

## Next

[running-a-jupyterlab-notebook.md](running-a-jupyterlab-notebook.md): clone your first notebook project and run its cells from top to bottom. For the fuller tour, go back to the [interactive-computing lesson](README.md).
