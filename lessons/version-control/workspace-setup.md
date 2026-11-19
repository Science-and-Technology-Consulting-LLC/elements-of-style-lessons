# Workspace set-up

You will check where you are working and what it costs. This matters because every later lesson assumes this workspace.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous step, [why-git-and-setup.md](why-git-and-setup.md), is done.
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.

## Steps to execute

### Your workspace

A **workspace** is the computer and terminal where you type commands. Use your own laptop terminal. It costs nothing extra, it is always available, and it suits every lesson in the first part of the course. No computer of your own, or work that outgrows a laptop? See [Other places to run these lessons](../introduction/other-places-to-run.md).

**What you should see:** nothing yet. This step is reading only.

### Know the cost

Your laptop costs nothing extra. If you later use a cloud computer, it charges by the hour while it runs. Develop and debug on small files. Once the code is right, run it across the hundreds or thousands of files. This costs less and catches bugs earlier.

**What you should see:** nothing. This step is reading only.

### Check where you are

JupyterLab is already running, from the Introduction. The next cell prints the folder this notebook is running in. `pwd` means "print working directory".

```bash
pwd
```

**What you should see:** a folder path ending in `version-control`, for example `/Users/you/elements-of-style-lessons/lessons/version-control`.

> **Picture to add:** JupyterLab with the file list on the left and the Launcher in the middle (save as assets/workspace-setup-step-3.png)

### If something goes wrong

- **`jupyter: command not found`.** Activate the `eos` environment (`conda activate eos`). Starting JupyterLab is explained in step 5 of the [Introduction page](../introduction/README.md).

## Next

[github-authenticate.md](github-authenticate.md): sign in to GitHub from the terminal so you can push code up.
