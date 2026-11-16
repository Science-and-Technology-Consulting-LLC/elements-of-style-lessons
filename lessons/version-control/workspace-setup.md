# Workspace set-up

You will check your computer and start JupyterLab in your own Bash terminal. This matters because every later lesson assumes this workspace.

**What you will do:**

- Check which tools your computer already has.
- Use your laptop terminal as your workspace.
- Learn what to watch for on cost.
- Start JupyterLab.

**What you need:**

- A computer with a terminal (see the Before you begin block). No computer of your own? See [Other places to run these lessons](../introduction/other-places-to-run.md).
- A modern web browser such as [Chrome](https://www.google.com/chrome/).

## Start here

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`workspace-setup.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/version-control/workspace-setup.ipynb) and run each cell in order, top to bottom.


### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Your workspace

A **workspace** is the computer and terminal where you type commands. Use your own laptop terminal. It costs nothing extra, it is always available, and it suits every lesson in the first part of the course. A cloud workspace is covered in [Other places to run these lessons](../introduction/other-places-to-run.md), for when your work outgrows a laptop.

**What you should see:** nothing yet. This step is reading only.

### Know the cost

Your laptop costs nothing extra. If you later use a cloud computer, it charges by the hour while it runs. Develop and debug on small files. Once the code is right, run it across the hundreds or thousands of files. This costs less and catches bugs earlier.

**What you should see:** nothing. This step is reading only.

### Start your notebook

In a terminal, go to the course folder and run `jupyter lab`. A browser tab opens with JupyterLab.

The next cell prints the folder this notebook is running in. `pwd` means "print working directory".

```bash
pwd
```

**What you should see:** a folder path ending in `version-control`, for example `/Users/you/elements-of-style-lessons/lessons/version-control`.

> **Picture to add:** JupyterLab with the file list on the left and the Launcher in the middle (save as assets/workspace-setup-step-3.png)

### If something goes wrong

- **`jupyter: command not found`.** JupyterLab is not installed in this terminal. Activate the `eos` environment (`conda activate eos`), or finish the [conda-environments lesson](../conda-environments/README.md).
- **The browser does not open.** Look in the terminal for a web address that starts with `http://localhost:8888`. Copy it into your browser.

## Next

[github-authenticate.md](github-authenticate.md): sign in to GitHub from the terminal so you can push code up.
