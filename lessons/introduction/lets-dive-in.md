# Let's dive in

You have JupyterLab open and this notebook in front of you. In this walkthrough you look around, learn to move through a notebook, and test that your tools work. Every later lesson assumes you can do these things.

**What you will do:**

- Find the parts of the JupyterLab window.
- Run your first cell.
- Check which tools your computer has.

**What you need:**

- JupyterLab open on this notebook. The steps to get here are on the [Introduction page](README.md).
- The `(eos)` environment active in the terminal where JupyterLab runs.

## Start here

### Before you begin

If you are reading this page in a web browser and not in JupyterLab, go back to the [Introduction page](README.md) and do its six steps first. They end with this notebook open.

## Steps to execute

### What you see

JupyterLab is a web page that works like a small desktop. It has four parts:

- **The menu bar** runs across the top: File, Edit, View, Run, Kernel, Tabs, Settings and Help.
- **The left bar** is a column of small icons at the left edge. The top icon opens the file list.
- **The main area** is the large space in the middle. It shows this notebook in a tab. Each file you open gets its own tab.
- **The status bar** is the thin strip along the bottom.

> **Picture to add:** the whole JupyterLab window with this notebook open, with the four parts labelled: menu bar, left bar, main area, status bar (save as assets/jupyterlab-window.png)

### Find your way: the menu at the top

You will use six menus often.

- **File.** *Save Notebook* keeps your work. *New* makes a new notebook, a terminal or a text file. *Shut Down* stops JupyterLab.
- **Edit.** *Clear Outputs of All Cells* wipes the results, so you can run the notebook from a clean start.
- **View.** Shows or hides the left bar and the other panels.
- **Run.** *Run Selected Cell* runs the cell you clicked on. *Run All Cells* runs the whole notebook, top to bottom.
- **Kernel.** The kernel is the engine that runs your code. *Restart Kernel* starts the engine again with a clean memory. *Interrupt Kernel* stops a cell that is taking too long.
- **Help.** Links to the JupyterLab documentation.

The other two menus matter less. **Tabs** lists your open tabs. **Settings** holds the theme: choose *Theme* to switch between light and dark.

> **Picture to add:** the menu bar, with the File menu open (save as assets/jupyterlab-menu-file.png)

> **Picture to add:** the Run menu and the Kernel menu, one beside the other (save as assets/jupyterlab-menu-run-kernel.png)

### Find your way: the bar on the left

The icons in the left bar open panels. Click an icon to open its panel. Click it again to close the panel.

- **File Browser** (a folder). Lists the files and folders on your computer, starting where you launched JupyterLab. Double-click a folder to go in. Double-click a file to open it. Click the folder icon in the path above the list to go back to the top.
- **Running Terminals and Kernels** (a circle with a square). Lists what is running now. Use it to shut down a notebook or a terminal you no longer need.
- **Table of Contents** (a list). Shows the headings of the open notebook. Click a heading to jump to it. This helps in a long lesson.
- **Extension Manager** (a puzzle piece). Adds extra features. You do not need it in these lessons.

Above the file list there are buttons too. The blue **+** opens the *Launcher*, a page of tiles. A tile starts a new notebook, a terminal or a text file. Under **Notebook** you will see **Python 3**, **Bash** and **R**: these are the kernels you registered. The lessons use **Bash**.

> **Picture to add:** the left bar with the File Browser panel open, with each icon labelled (save as assets/jupyterlab-left-bar.png)

> **Picture to add:** the Launcher showing the Python 3, Bash and R tiles (save as assets/jupyterlab-launcher.png)

### Find your way: the notebook toolbar

A notebook is a stack of **cells**. There are two kinds that you will meet.

- A **Markdown cell** holds text, like this one. You read it.
- A **Code cell** holds a command, with `[ ]:` at its left. You run it.

The toolbar sits just above the notebook. From the left, its buttons are:

- **Save** (a disk).
- **Add a cell** (a plus).
- **Cut, copy, paste** (scissors, two pages, a clipboard).
- **Run** (a play triangle). Runs the cell you chose, then moves to the next one.
- **Stop** (a square). Interrupts a cell that is still running.
- **Restart the kernel** (a circular arrow).
- **Run all** (two triangles).
- **Cell type** (a drop-down that says *Code* or *Markdown*).

At the top right of the notebook you see the name of the kernel. For these lessons it must say **Bash**. If it says something else, click the name, choose **Bash** from the list, and press **Select**.

> **Picture to add:** the notebook toolbar with each button labelled, and the kernel name **Bash** at the top right (save as assets/jupyterlab-toolbar.png)

### Run your first cell

Click on the grey box below. A blue bar appears at the left of it. Then press **Shift and Return** together.

```bash
echo "Hello from JupyterLab"
pwd
```

**What you should see:** the words `Hello from JupyterLab`, then a path that ends in `elements-of-style-lessons/lessons/introduction`. That path is the folder that holds this notebook. While the cell runs, the left of it shows `[*]:`. When it is done, a number appears, such as `[1]:`. The number counts the cells you have run since the kernel started.

Press **Shift and Return** again on the next cell. Each press runs one cell and moves down. You can also click the **Run** button in the toolbar.

If a cell hangs, click the **Stop** button. If the notebook gets confusing, choose **Kernel**, then **Restart Kernel and Clear Outputs of All Cells**, and run it again from the top.

> **Picture to add:** the cell above after it ran, showing the `[1]:` number and the output (save as assets/jupyterlab-first-cell.png)

### Open a terminal inside JupyterLab

You can also type commands in a terminal without leaving JupyterLab. Choose **File**, then **New**, then **Terminal**. A new tab opens with a prompt. Run `conda activate eos` in it before you use the lesson tools.

### Stop JupyterLab

When you finish, choose **File**, then **Shut Down**. Or click in the terminal where you ran `jupyter lab` and press `Ctrl-C`. To start again later, open a terminal, go into the `elements-of-style-lessons` folder, run `conda activate eos`, and run `jupyter lab`.

### Check your tools

This cell asks your computer where each program lives. Where a program is missing, the cell says `MISSING`. Only `bash`, `git` and `python3` must be present today. The other lessons tell you when they need the rest.

| Tool | Check by hand | If missing, see |
|---|---|---|
| [Bash](https://www.gnu.org/software/bash/) | `bash --version` | [Command line](../command-line-and-git-bash/README.md) |
| [Git](https://git-scm.com/) | `git --version` | [Command line](../command-line-and-git-bash/README.md) |
| [Conda](https://docs.conda.io/) | `conda --version` | [Conda environments](../conda-environments/README.md) |
| [GitHub CLI](https://cli.github.com/) (`gh`) | `gh --version` | [Version control](../version-control/why-git-and-setup.md) |
| [Podman](https://podman.io/docs/installation) | `podman --version` | [Containers](../containers/README.md) |
| [Nextflow](https://www.nextflow.io/) | `nextflow -version` | [Introduction to Nextflow](../nextflow-workflows/README.md) |
| [Python 3](https://www.python.org/) | `python3 --version` | [Conda environments](../conda-environments/README.md) |

Run all the checks at once:

```bash
for cmd in bash git conda gh podman nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s\n" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING\n" "$cmd"
  fi
done
```

**What you should see:** one line per tool. A tool that is present shows its location. A tool that is missing shows `MISSING`. For example:

```text
  bash       /bin/bash
  git        /path/to/eos/bin/git
  podman     MISSING
```

The exact paths on your computer will differ. Because you started from the `eos` environment, `git`, `conda`, `gh`, `nextflow` and `python3` all show a path. `podman` may show `MISSING` until *Install Podman later*.

### Install Podman later

[Podman](https://podman.io/docs/installation) runs *containers*, which are sealed boxes holding a program and everything it needs. Conda does not install Podman. You need it from the [containers lesson](../containers/README.md) on, and that lesson shows how to install it. Skip it today.

### Other places to run the lessons

Your own Bash terminal is the main way to follow these lessons. If you cannot use one, or later when the work grows, see [Other places to run these lessons](other-places-to-run.md). It covers Google Cloud Shell and Lifebit.

### If something goes wrong

- **The kernel name at the top right is not Bash.** Click the name, choose **Bash**, and press **Select**.
- **There is no Bash tile in the Launcher.** The kernel was registered outside the `eos` environment. In a terminal run `conda activate eos`, then `python -m bash_kernel.install`, stop JupyterLab, and start it again with `jupyter lab`.
- **A cell says `command not found`.** JupyterLab was started outside the `eos` environment. Stop it, run `conda activate eos` in the terminal, and run `jupyter lab` again.
- **A tool shows `MISSING`.** Compare it with the table in *Check your tools*. Podman is the one tool you install by hand.
- **You closed the browser tab by mistake.** JupyterLab still runs in the terminal. Open the address that starts with `http://localhost` again.

> **Check:** the menu names, the toolbar buttons and the left bar follow JupyterLab 4, the version `eos.yml` installs. Please compare each with your own window as you take the pictures, and tell me what differs.

For more on moving through notebooks, see the [Interactive computing lesson](../interactive-computing/README.md).

## Next

Continue with [The Rules](../elements-of-style-rules/README.md).
