# Starting a JupyterLab notebook

You have already started [JupyterLab](https://jupyterlab.readthedocs.io/) once, in the Introduction. Here we say what it is, show how to start it again, and show the Lifebit way. This matters because every later lesson runs inside it.

**What you will do:**

- Learn what JupyterLab is.
- Start it again from a terminal, or on Lifebit.
- Recognise the file browser, the Launcher and the menu bar.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Reproducible environments with Conda](../conda-environments/README.md), is done.
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.
- A web browser such as [Chrome](https://www.google.com/chrome/).

## Steps to execute

### Know what JupyterLab is

**JupyterLab** is a web page that lets you open notebooks, files and terminals side by side. It runs on a computer (yours, or a Lifebit server) and shows up in your browser.

**What you should see:** nothing. This step is reading only.

### On your laptop: start JupyterLab again

If JupyterLab is still open from the Introduction, skip this step. If you closed it, type these two commands in a **terminal** (not in a notebook cell), one per line, and press `Enter` after each. The first turns on the `eos` environment. The second starts JupyterLab. JupyterLab keeps running until you stop it, so it cannot run as a notebook cell.

```text
conda activate eos
jupyter lab
```

**What you should see:** your terminal prompt starts with `(eos)`. JupyterLab opens in your default browser. In the terminal you see log lines that include a web address like `http://localhost:8888/lab?token=...`. If no browser opens, copy that address into a browser yourself. To stop JupyterLab later, press `Ctrl-C` twice in that terminal.

> **Picture to add:** the terminal after `jupyter lab`, with the localhost address line (save as assets/starting-a-jupyter-lab-notebook-step-2.png)

### Optional: start JupyterLab on Lifebit instead

Skip this step if you started JupyterLab on your laptop. It needs a Lifebit account: see [Other places to run these lessons](../introduction/other-places-to-run.md).

[Lifebit](https://lifebit.ai/)'s notebook servers have JupyterLab already installed.

1. From the workspace dashboard, click **Notebook**, then **Launch**.
2. Pick a compute size.
3. Wait for the browser tab to open. It opens straight into JupyterLab.

The terminal is under **File**, **New**, **Terminal**.

> **Picture to add:** the Lifebit dashboard with the Notebook and Launch buttons (save as assets/starting-a-jupyter-lab-notebook-step-3.png)

**What you should see:** a new browser tab with JupyterLab in it.

### Recognise the screen

However you got here, you see a **file browser** on the left, a **Launcher** in the middle and a **menu bar** across the top. [Let's dive in](../introduction/lets-dive-in.md) names each part and what it does. The Launcher has tiles for *Python 3*, *Bash*, *R*, *Terminal* and *Text File*.

> **Picture to add:** JupyterLab with the file browser, the Launcher tiles and the menu bar labelled (save as assets/starting-a-jupyter-lab-notebook-step-4.png)

**What you should see:** all three parts above. If the *R* tile is missing, see below.

### If something goes wrong

- **`conda: command not found`.** Conda is not installed, or you opened this terminal before installing it. Close it, open a new one, and see the [Introduction page](../introduction/README.md).
- **`jupyter: command not found`.** The `eos` environment is not active. Run `conda activate eos` first.
- **The browser does not open.** Copy the `http://localhost:8888/lab?token=...` address from the terminal into your browser.
- **There is no R tile.** R is not registered with Jupyter. The Introduction does this in step 4. If it did not work, see [exploring-an-r-notebook.md](exploring-an-r-notebook.md).

## Next

[running-a-jupyterlab-notebook.md](running-a-jupyterlab-notebook.md): clone your first notebook project and run its cells from top to bottom. For the fuller tour, go back to the [interactive-computing lesson](README.md).
